const state = {
    templates: [],
    currentId: null,
    params: {},
    debounceTimer: null,
    editor: null,
    userEdited: false,
};

const els = {
    list: document.getElementById("template-list"),
    search: document.getElementById("search"),
    title: document.getElementById("current-title"),
    desc: document.getElementById("current-desc"),
    form: document.getElementById("params-form"),
    editorTA: document.getElementById("code-editor"),
    sceneInfo: document.getElementById("scene-info"),
    copy: document.getElementById("copy-code"),
    reset: document.getElementById("reset-btn"),
    blank: document.getElementById("blank-btn"),
    render: document.getElementById("render-btn"),
    quality: document.getElementById("quality"),
    videoArea: document.getElementById("video-area"),
    videoStatus: document.getElementById("video-status"),
    log: document.getElementById("render-log"),
    toast: document.getElementById("toast"),
    snippetsBtn: document.getElementById("snippets-btn"),
    snippetsModal: document.getElementById("snippets-modal"),
    snippetsClose: document.getElementById("snippets-close"),
    snippetsSearch: document.getElementById("snippets-search"),
    snippetsCats: document.getElementById("snippets-cats"),
    snippetsList: document.getElementById("snippets-list"),
    snippetDetail: document.getElementById("snippet-detail"),
};

const snipState = {
    all: [],
    categories: [],
    activeCat: null,
    filter: "",
    selectedId: null,
    params: {},
};

const BLANK_CODE = `from manim import *

class MinhaCena(Scene):
    def construct(self):
        titulo = Text("Olá, Manim!", font_size=48, color=BLUE)
        self.play(Write(titulo))
        self.wait(1)
        self.play(titulo.animate.to_edge(UP))

        circulo = Circle(radius=1.5, color=YELLOW).set_fill(YELLOW, opacity=0.3)
        quadrado = Square(side_length=2.5, color=GREEN).set_fill(GREEN, opacity=0.3)

        self.play(Create(circulo))
        self.wait(0.5)
        self.play(Transform(circulo, quadrado))
        self.wait(1)
        self.play(*[FadeOut(m) for m in self.mobjects])
`;

function setupEditor() {
    state.editor = CodeMirror.fromTextArea(els.editorTA, {
        mode: "python",
        theme: "dracula",
        lineNumbers: true,
        indentUnit: 4,
        tabSize: 4,
        matchBrackets: true,
        autoCloseBrackets: true,
        lineWrapping: false,
    });
    state.editor.on("change", () => {
        if (!state.suppressChange) {
            state.userEdited = true;
        }
        updateSceneInfo();
    });
    state.editor.setValue("# Selecione um template ou clique em '+ Cena em branco' para começar.\n");
}

function setEditorCode(code) {
    state.suppressChange = true;
    state.editor.setValue(code);
    state.suppressChange = false;
    state.userEdited = false;
    updateSceneInfo();
}

function updateSceneInfo() {
    const code = state.editor.getValue();
    const matches = [...code.matchAll(/class\s+([A-Za-z_]\w*)\s*\(\s*Scene\s*\)\s*:/g)].map(m => m[1]);
    if (matches.length === 0) {
        els.sceneInfo.textContent = "⚠ Nenhuma classe Scene";
        els.sceneInfo.style.color = "var(--warn)";
    } else if (matches.length === 1) {
        els.sceneInfo.textContent = `Scene: ${matches[0]}`;
        els.sceneInfo.style.color = "var(--accent-2)";
    } else {
        els.sceneInfo.textContent = `Scenes: ${matches.join(", ")} (renderiza a 1ª)`;
        els.sceneInfo.style.color = "var(--accent-2)";
    }
}

async function init() {
    setupEditor();
    try {
        const res = await fetch("/api/templates");
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        const data = await res.json();
        state.templates = data.templates;
        renderTemplateList();
    } catch (e) {
        els.list.innerHTML = `<div class="placeholder" style="padding:20px;text-align:center;color:var(--danger)">Erro: ${e.message}</div>`;
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

    if (state.userEdited &&
        !confirm("Você editou o código. Trocar de template vai descartar suas mudanças. Continuar?")) {
        return;
    }

    state.currentId = id;
    state.params = {};
    t.params.forEach(p => { state.params[p.name] = p.default; });

    els.title.textContent = `${t.icon} ${t.title}`;
    els.desc.textContent = t.description;
    els.render.disabled = false;
    renderTemplateList(els.search.value);
    renderForm(t);
    regenerateCode();
}

function escAttr(s) {
    return String(s).replace(/&/g, "&amp;").replace(/"/g, "&quot;").replace(/</g, "&lt;");
}

function renderForm(t) {
    els.form.innerHTML = t.params.map(p => {
        const cur = state.params[p.name] !== undefined ? state.params[p.name] : p.default;
        const hint = p.hint ? `<small class="field-hint">${p.hint}</small>` : "";
        let control;
        if (p.type === "select") {
            control = `<select data-name="${p.name}">
                ${p.options.map(o => `<option value="${escAttr(o.value)}" ${String(o.value) === String(cur) ? 'selected' : ''}>${o.label}</option>`).join("")}
            </select>`;
        } else if (p.type === "latex") {
            control = `<input type="text" data-name="${p.name}" data-kind="latex" class="latex-input" value="${escAttr(cur)}" placeholder="ex: \\frac{a}{b}" spellcheck="false">`;
        } else if (p.type === "list_text" || p.type === "list_latex") {
            control = `<textarea data-name="${p.name}" data-kind="${p.type}" rows="5" class="${p.type === 'list_latex' ? 'latex-input' : ''}" spellcheck="false">${escAttr(cur)}</textarea>`;
        } else if (p.type === "number") {
            control = `<input type="number" data-name="${p.name}" value="${escAttr(cur)}" step="any">`;
        } else {
            control = `<input type="text" data-name="${p.name}" value="${escAttr(cur)}">`;
        }
        return `<div class="field">
            <label>${p.label}</label>
            ${control}
            ${hint}
        </div>`;
    }).join("");

    els.form.querySelectorAll("input, select, textarea").forEach(el => {
        el.addEventListener("input", () => {
            const name = el.dataset.name;
            let val;
            if (el.type === "number") {
                val = parseFloat(el.value);
                if (isNaN(val)) {
                    el.style.borderColor = "var(--danger)";
                    return;
                }
                el.style.borderColor = "";
            } else {
                val = el.value;
            }
            state.params[name] = val;
            scheduleRegenerate();
        });
    });
}

function scheduleRegenerate() {
    clearTimeout(state.debounceTimer);
    state.debounceTimer = setTimeout(regenerateCode, 350);
}

async function regenerateCode() {
    if (!state.currentId) return;
    if (state.userEdited) return; // não sobrescreve edições do usuário automaticamente
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
            toast(data.error, "error");
        } else {
            setEditorCode(data.code);
        }
    } catch (e) {
        toast(e.message, "error");
    }
}

els.copy.addEventListener("click", () => {
    const text = state.editor.getValue();
    if (!text) return;
    navigator.clipboard.writeText(text).then(() => toast("Código copiado!", "success"));
});

els.reset.addEventListener("click", () => {
    if (!state.currentId) {
        toast("Nenhum template ativo", "error");
        return;
    }
    if (state.userEdited && !confirm("Descartar suas edições e regerar do template?")) return;
    state.userEdited = false;
    regenerateCode();
});

els.blank.addEventListener("click", () => {
    if (state.userEdited && !confirm("Descartar suas edições?")) return;
    state.currentId = null;
    state.params = {};
    els.title.textContent = "✏️ Cena em branco";
    els.desc.textContent = "Edite livremente o código abaixo e clique em Executar para renderizar.";
    els.form.innerHTML = `<p class="muted center">Sem parâmetros.<br><small>Edite o código diretamente.</small></p>`;
    els.render.disabled = false;
    renderTemplateList(els.search.value);
    setEditorCode(BLANK_CODE);
});

els.search.addEventListener("input", e => renderTemplateList(e.target.value));

els.render.addEventListener("click", async () => {
    const code = state.editor.getValue();
    if (!code.trim()) {
        toast("Editor vazio", "error");
        return;
    }
    const sceneMatches = [...code.matchAll(/class\s+([A-Za-z_]\w*)\s*\(\s*Scene\s*\)\s*:/g)];
    if (sceneMatches.length === 0) {
        toast("Nenhuma classe Scene encontrada no código", "error");
        return;
    }

    els.render.disabled = true;
    els.render.innerHTML = `<span class="spinner"></span> Renderizando...`;
    els.videoStatus.textContent = "Executando Manim...";
    els.videoArea.innerHTML = `<div class="placeholder"><div class="placeholder-icon">⏳</div><p>Renderizando o vídeo...<br><small class="muted">Pode levar de 10s a 3 min.</small></p></div>`;
    els.log.classList.add("hidden");
    els.log.textContent = "";

    try {
        const res = await fetch("/api/render-code", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({
                code: code,
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
            els.videoStatus.textContent = `Pronto ✓ (${data.scene})`;
            toast("Vídeo renderizado!", "success");
        }
    } catch (e) {
        els.videoArea.innerHTML = `<div class="placeholder"><div class="placeholder-icon">⚠️</div><p>${e.message}</p></div>`;
        els.videoStatus.textContent = "Falha";
        toast(e.message, "error");
    }

    els.render.disabled = false;
    els.render.innerHTML = `<span class="btn-text">▶ Executar &amp; Renderizar</span>`;
});

// -------------------- Snippets --------------------

async function loadSnippets() {
    if (snipState.all.length) return;
    try {
        const res = await fetch("/api/snippets");
        const data = await res.json();
        snipState.all = data.snippets;
        snipState.categories = data.categories;
        renderSnippetCats();
        renderSnippetList();
    } catch (e) {
        toast("Erro ao carregar snippets: " + e.message, "error");
    }
}

function renderSnippetCats() {
    const cats = ["Todas", ...snipState.categories];
    els.snippetsCats.innerHTML = cats.map(c =>
        `<span class="cat-chip ${ (c === "Todas" && !snipState.activeCat) || c === snipState.activeCat ? 'active' : '' }" data-cat="${c}">${c}</span>`
    ).join("");
    els.snippetsCats.querySelectorAll(".cat-chip").forEach(chip => {
        chip.addEventListener("click", () => {
            snipState.activeCat = chip.dataset.cat === "Todas" ? null : chip.dataset.cat;
            renderSnippetCats();
            renderSnippetList();
        });
    });
}

function renderSnippetList() {
    const f = snipState.filter.toLowerCase();
    const list = snipState.all.filter(s => {
        if (snipState.activeCat && s.category !== snipState.activeCat) return false;
        if (!f) return true;
        return s.title.toLowerCase().includes(f) ||
               s.description.toLowerCase().includes(f) ||
               (s.tags || []).some(t => t.toLowerCase().includes(f));
    });
    els.snippetsList.innerHTML = list.map(s => `
        <div class="snippet-item ${snipState.selectedId === s.id ? 'active' : ''}" data-id="${s.id}">
            <div class="si-cat">${s.category}</div>
            <div class="si-title">${s.title}</div>
            <div class="si-desc">${s.description}</div>
        </div>
    `).join("") || `<p class="muted center" style="padding:20px">Nada encontrado.</p>`;
    els.snippetsList.querySelectorAll(".snippet-item").forEach(it => {
        it.addEventListener("click", () => selectSnippet(it.dataset.id));
    });
}

async function selectSnippet(id) {
    snipState.selectedId = id;
    const s = snipState.all.find(x => x.id === id);
    if (!s) return;
    snipState.params = {};
    s.params.forEach(p => { snipState.params[p.name] = p.default; });
    renderSnippetList();
    await renderSnippetDetail();
}

async function renderSnippetDetail() {
    const s = snipState.all.find(x => x.id === snipState.selectedId);
    if (!s) return;

    // pega preview do código com params atuais
    let previewCode = "";
    try {
        const res = await fetch(`/api/snippets/${s.id}/render`, {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({params: snipState.params}),
        });
        const data = await res.json();
        previewCode = data.code || data.error || "";
    } catch (e) {
        previewCode = "Erro ao gerar preview: " + e.message;
    }

    const requiresNote = s.requires_var && s.requires_var.length
        ? `<div class="requires-note">⚠ Este snippet usa as variáveis: <strong>${s.requires_var.join(", ")}</strong>. Crie-as antes no código.</div>`
        : "";

    const fullSceneNote = s.is_full_scene
        ? `<div class="requires-note" style="border-left-color: var(--accent); color: var(--accent)">ℹ Este snippet é uma <strong>cena completa</strong> — substitui o código atual.</div>`
        : "";

    const paramsHtml = s.params.map(p => {
        const cur = snipState.params[p.name] !== undefined ? snipState.params[p.name] : p.default;
        if (p.type === "select") {
            return `<div class="field"><label>${p.label}</label>
                <select data-name="${p.name}">
                    ${p.options.map(o => `<option value="${o.value}" ${o.value === cur ? 'selected':''}>${o.label}</option>`).join("")}
                </select></div>`;
        }
        const inputType = p.type === "number" ? "number" : "text";
        return `<div class="field"><label>${p.label}</label>
            <input type="${inputType}" data-name="${p.name}" value="${escapeAttr(cur)}" ${p.type === 'number' ? 'step="any"' : ''}>
            </div>`;
    }).join("") || `<p class="muted" style="grid-column:1/-1">Sem parâmetros.</p>`;

    els.snippetDetail.innerHTML = `
        <div class="cat-tag">${s.category}</div>
        <h3>${s.title}</h3>
        <p class="desc">${s.description}</p>
        <div class="tags">${(s.tags||[]).map(t => `<span class="tag">${t}</span>`).join("")}</div>
        ${fullSceneNote}
        ${requiresNote}
        <div class="snippet-params">${paramsHtml}</div>
        <div class="snippet-preview">${escapeHtml(previewCode)}</div>
        <div class="snippet-actions">
            <button class="btn primary" id="insert-snippet">＋ Inserir no Editor</button>
            <button class="btn ghost" id="copy-snippet">Copiar</button>
        </div>
    `;

    els.snippetDetail.querySelectorAll(".snippet-params [data-name]").forEach(el => {
        const handler = () => {
            const name = el.dataset.name;
            const v = el.type === "number" ? parseFloat(el.value) : el.value;
            snipState.params[name] = v;
            renderSnippetDetail();
        };
        // 'input' para texto/número, 'change' para select (evita perder foco a cada tecla)
        el.addEventListener(el.tagName === "SELECT" ? "change" : "input", handler);
    });

    document.getElementById("insert-snippet").addEventListener("click", () => insertSnippet(s, previewCode));
    document.getElementById("copy-snippet").addEventListener("click", () => {
        navigator.clipboard.writeText(previewCode);
        toast("Código copiado", "success");
    });
}

function insertSnippet(s, code) {
    if (s.is_full_scene) {
        if (state.editor.getValue().trim() &&
            !confirm("Este snippet é uma cena completa e vai substituir o código atual. Continuar?")) {
            return;
        }
        setEditorCode(code);
    } else {
        // Insere com indentação para casar com `def construct(self):`
        const indented = code.split("\n").map(l => l ? "        " + l : l).join("\n");
        const cursor = state.editor.getCursor();
        const cur = state.editor.getValue();
        // Se tem placeholder de classe Scene, insere antes do final do construct
        if (/class\s+\w+\s*\(\s*Scene\s*\)\s*:/.test(cur)) {
            // tenta inserir antes do último FadeOut(*self.mobjects) ou no final do construct
            state.editor.replaceRange("\n" + indented + "\n", cursor);
        } else {
            // Sem scene: cria estrutura
            const scene = `from manim import *\n\nclass MinhaCena(Scene):\n    def construct(self):\n${indented}\n`;
            setEditorCode(scene);
        }
        state.userEdited = true;
    }
    closeSnippetsModal();
    toast(`Snippet "${s.title}" inserido`, "success");
}

function openSnippetsModal() {
    els.snippetsModal.classList.remove("hidden");
    loadSnippets();
}
function closeSnippetsModal() {
    els.snippetsModal.classList.add("hidden");
}

els.snippetsBtn.addEventListener("click", openSnippetsModal);
els.snippetsClose.addEventListener("click", closeSnippetsModal);
els.snippetsModal.querySelector(".modal-backdrop").addEventListener("click", closeSnippetsModal);
els.snippetsSearch.addEventListener("input", e => {
    snipState.filter = e.target.value;
    renderSnippetList();
});

function escapeHtml(s) {
    return String(s).replace(/[&<>"']/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
}
function escapeAttr(s) { return escapeHtml(s); }

// -------------------- Toast --------------------

function toast(msg, type = "") {
    els.toast.textContent = msg;
    els.toast.className = `toast ${type}`;
    setTimeout(() => els.toast.classList.add("hidden"), 3500);
}

// -------------------- Manim Compiler --------------------

async function compilerGenerate(prompt) {
    try {
        const res = await fetch("/api/compiler/generate", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({prompt: prompt}),
        });
        const data = await res.json();
        if (data.error) {
            toast(data.error, "error");
            return null;
        }
        setEditorCode(data.code);
        state.currentId = data.template_id;
        state.params = data.params || {};
        els.title.textContent = "🤖 " + prompt.substring(0, 40);
        els.desc.textContent = "Template: " + data.template_id;
        els.render.disabled = false;
        toast("Código gerado!", "success");
        return data.code;
    } catch (e) {
        toast(e.message, "error");
        return null;
    }
}

async function compilerRender(prompt, quality) {
    const code = await compilerGenerate(prompt);
    if (!code) return;

    els.render.disabled = true;
    els.render.innerHTML = '<span class="spinner"></span> Renderizando...';
    els.videoStatus.textContent = "Executando Manim...";
    els.videoArea.innerHTML = '<div class="placeholder"><div class="placeholder-icon">⏳</div><p>Renderizando...</p></div>';

    try {
        const res = await fetch("/api/compiler/render", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({prompt: prompt, quality: quality}),
        });
        const data = await res.json();

        if (!res.ok || data.error) {
            els.videoArea.innerHTML = '<div class="placeholder"><div class="placeholder-icon">⚠️</div><p>' + escapeHtml(data.error || "Erro") + '</p></div>';
            els.videoStatus.textContent = "Falha";
            toast(data.error || "Erro", "error");
        } else {
            els.videoArea.innerHTML = '<video controls autoplay loop><source src="' + data.video_url + '" type="video/mp4"></video>';
            els.videoStatus.textContent = "Pronto ✓";
            toast("Vídeo renderizado!", "success");
        }
    } catch (e) {
        els.videoArea.innerHTML = '<div class="placeholder"><p>' + escapeHtml(e.message) + '</p></div>';
        els.videoStatus.textContent = "Falha";
        toast(e.message, "error");
    }

    els.render.disabled = false;
    els.render.innerHTML = '<span class="btn-text">▶ Executar &amp; Renderizar</span>';
}

async function exportCode(filename) {
    const code = state.editor.getValue();
    const blob = new Blob([code], {type: "text/x-python"});
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = filename || "scene.py";
    a.click();
    URL.revokeObjectURL(url);
    toast("Arquivo exportado!", "success");
}

// Event listeners para compiler
document.getElementById("compiler-generate").addEventListener("click", () => {
    const prompt = document.getElementById("compiler-prompt").value.trim();
    if (prompt) compilerGenerate(prompt);
});

document.getElementById("compiler-render").addEventListener("click", () => {
    const prompt = document.getElementById("compiler-prompt").value.trim();
    if (prompt) compilerRender(prompt, els.quality.value);
});

document.getElementById("export-btn").addEventListener("click", () => {
    exportCode("manim_scene.py");
});

// Exemplos clicáveis
document.querySelectorAll(".example-btn").forEach(btn => {
    btn.addEventListener("click", () => {
        const example = btn.dataset.example;
        document.getElementById("compiler-prompt").value = example;
        compilerGenerate(example);
    });
});

init();
