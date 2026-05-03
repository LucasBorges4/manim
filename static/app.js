const state = {
    templates: [],
    currentId: null,
    params: {},
    debounceTimer: null,
};

const els = {
    list: document.getElementById("template-list"),
    search: document.getElementById("search"),
    title: document.getElementById("current-title"),
    desc: document.getElementById("current-desc"),
    form: document.getElementById("params-form"),
    code: document.getElementById("code-view"),
    copy: document.getElementById("copy-code"),
    render: document.getElementById("render-btn"),
    quality: document.getElementById("quality"),
    videoArea: document.getElementById("video-area"),
    videoStatus: document.getElementById("video-status"),
    log: document.getElementById("render-log"),
    toast: document.getElementById("toast"),
};

async function init() {
    try {
        const res = await fetch("/api/templates");
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        const data = await res.json();
        state.templates = data.templates;
        renderTemplateList();
    } catch (e) {
        els.list.innerHTML = `<div class="placeholder" style="padding:20px;text-align:center;color:var(--danger)">Erro ao carregar templates: ${e.message}</div>`;
        toast("Falha ao carregar templates", "error");
    }
}

function renderTemplateList(filter = "") {
    const f = filter.toLowerCase();
    const filtered = state.templates.filter(t =>
        !f || t.title.toLowerCase().includes(f) ||
        t.description.toLowerCase().includes(f) ||
        t.category.toLowerCase().includes(f)
    );
    els.list.innerHTML = filtered.map(t => `
        <div class="template-card ${state.currentId === t.id ? 'active' : ''}" data-id="${t.id}">
            <div class="icon">${t.icon}</div>
            <div class="info">
                <h4>${t.title}</h4>
                <span class="cat">${t.category}</span>
            </div>
        </div>
    `).join("");
    els.list.querySelectorAll(".template-card").forEach(card => {
        card.addEventListener("click", () => selectTemplate(card.dataset.id));
    });
}

function selectTemplate(id) {
    const t = state.templates.find(x => x.id === id);
    if (!t) return;
    state.currentId = id;
    state.params = {};
    t.params.forEach(p => { state.params[p.name] = p.default; });

    els.title.textContent = `${t.icon} ${t.title}`;
    els.desc.textContent = t.description;
    els.render.disabled = false;
    renderTemplateList(els.search.value);
    renderForm(t);
    updateCode();
}

function renderForm(t) {
    els.form.innerHTML = t.params.map(p => {
        if (p.type === "select") {
            return `
                <div class="field">
                    <label for="p-${p.name}">${p.label}</label>
                    <select id="p-${p.name}" data-name="${p.name}">
                        ${p.options.map(o => `<option value="${o.value}" ${o.value === p.default ? 'selected' : ''}>${o.label}</option>`).join("")}
                    </select>
                </div>
            `;
        }
        return `
            <div class="field">
                <label for="p-${p.name}">${p.label}</label>
                <input type="number" id="p-${p.name}" data-name="${p.name}"
                       value="${p.default}" step="${p.step || 1}">
            </div>
        `;
    }).join("");

    els.form.querySelectorAll("input, select").forEach(el => {
        el.addEventListener("input", () => {
            const name = el.dataset.name;
            let val;
            if (el.type === "number") {
                val = parseFloat(el.value);
                if (isNaN(val)) {
                    el.style.borderColor = "var(--danger)";
                    return; // não atualiza enquanto inválido
                }
                el.style.borderColor = "";
            } else {
                val = el.value;
            }
            state.params[name] = val;
            scheduleCodeUpdate();
        });
    });
}

function validateParams() {
    const inputs = els.form.querySelectorAll("input[type='number']");
    for (const i of inputs) {
        if (i.value === "" || isNaN(parseFloat(i.value))) {
            i.style.borderColor = "var(--danger)";
            i.focus();
            return false;
        }
    }
    return true;
}

function scheduleCodeUpdate() {
    clearTimeout(state.debounceTimer);
    state.debounceTimer = setTimeout(updateCode, 250);
}

async function updateCode() {
    if (!state.currentId) return;
    try {
        const res = await fetch("/api/generate", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({
                template_id: state.currentId,
                params: state.params,
            }),
        });
        const data = await res.json();
        if (data.error) {
            els.code.textContent = `# Erro: ${data.error}`;
        } else {
            els.code.textContent = data.code;
            if (window.Prism) Prism.highlightElement(els.code);
        }
    } catch (e) {
        els.code.textContent = `# Erro: ${e.message}`;
    }
}

els.copy.addEventListener("click", () => {
    const text = els.code.textContent;
    if (!text) return;
    navigator.clipboard.writeText(text).then(() => toast("Código copiado!", "success"));
});

els.search.addEventListener("input", e => renderTemplateList(e.target.value));

els.render.addEventListener("click", async () => {
    if (!state.currentId) return;
    if (!validateParams()) {
        toast("Preencha todos os parâmetros corretamente", "error");
        return;
    }

    els.render.disabled = true;
    els.render.innerHTML = `<span class="spinner"></span> Renderizando...`;
    els.videoStatus.textContent = "Renderizando, aguarde (até ~3 min)...";
    els.videoArea.innerHTML = `<div class="placeholder"><div class="placeholder-icon">⏳</div><p>Renderizando o vídeo com Manim...<br><small class="muted">Isso pode levar de 10s a 3 min dependendo da qualidade.</small></p></div>`;
    els.log.classList.add("hidden");
    els.log.textContent = "";

    try {
        const res = await fetch("/api/render", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({
                template_id: state.currentId,
                params: state.params,
                quality: els.quality.value,
            }),
        });
        const data = await res.json();

        if (!res.ok || data.error) {
            els.videoArea.innerHTML = `<div class="placeholder"><div class="placeholder-icon">⚠️</div><p>${data.error || "Erro ao renderizar."}</p></div>`;
            if (data.log) {
                els.log.textContent = data.log;
                els.log.classList.remove("hidden");
            }
            els.videoStatus.textContent = "Falha";
            toast(data.error || "Erro ao renderizar", "error");
        } else {
            els.videoArea.innerHTML = `
                <video controls autoplay loop>
                    <source src="${data.video_url}" type="video/mp4">
                </video>
            `;
            els.videoStatus.textContent = "Pronto ✓";
            toast("Vídeo renderizado!", "success");
        }
    } catch (e) {
        els.videoArea.innerHTML = `<div class="placeholder"><div class="placeholder-icon">⚠️</div><p>${e.message}</p></div>`;
        els.videoStatus.textContent = "Falha";
        toast(e.message, "error");
    }

    els.render.disabled = false;
    els.render.innerHTML = `<span class="btn-text">▶ Renderizar</span>`;
});

function toast(msg, type = "") {
    els.toast.textContent = msg;
    els.toast.className = `toast ${type}`;
    setTimeout(() => els.toast.classList.add("hidden"), 3500);
}

init();
