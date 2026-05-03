# Coleção de Vídeos Educacionais - Matemática Ensino Médio

Esta coleção contém animações criadas com Manim para auxiliar no aprendizado de matemática do ensino médio.

## Conteúdos

### 1. Aritmética Básica
**Arquivo:** `aritmetica_basica.py`

- Números primos e Crivo de Eratóstenes
- MDC (Máximo Divisor Comum)
- MMC (Mínimo Múltiplo Comum)
- Regras de sinais

### 2. Frações
**Arquivo:** `fracoes_ensino_medio.py`

- Introdução a frações (numerador e denominador)
- Adição de frações (mesmo e diferentes denominadores)
- Multiplicação e divisão de frações

### 3. Potências e Radiciação
**Arquivo:** `potencias_radiciacao.py`

- Definição de potências
- Propriedades das potências
- Definição de radiciação
- Propriedades das raízes
- Simplificação de radical
- Operações misturadas

### 4. Equações e Sistemas
**Arquivo:** `equacoes_sistemas.py`

- Equações do 1º grau
- Equações do 2º grau (Fórmula de Bhaskara)
- Sistemas lineares 2×2
- Classificação de sistemas (determinado, impossível, indeterminado)
- Regras de sinais aplicadas

### 5. Geometria Básica
**Arquivo:** `geometria_basica.py`

- Áreas e perímetros (quadrado, retângulo, triângulo, círculo)
- Teorema de Pitágoras
- Relações trigonométricas no triângulo retângulo
- Volume das figuras sólidas
- Semelhança de triângulos

### 6. Funções e Gráficos
**Arquivo:** `funcoes_graficos.py`

- Função do 1º grau (linear): coeficiente angular e linear
- Função do 2º grau (quadrática): parábola, vértice, zeros
- Domínio e contradomínio
- Função exponencial
- Função logarítmica

### 7. Trigonometria
**Arquivo:** `trigonometria.py`

- Circunferência trigonométrica
- Funções seno e cosseno (gráficos)
- Identidades fundamentais
- Lei dos senos e lei dos cossenos
- Amplitude, período e fase
- Fórmulas de soma e diferença
- Ângulos notáveis (30°, 45°, 60°)

### 8. Estatística e Probabilidade
**Arquivo:** `estatistica_probabilidade.py`

- Média, mediana e moda
- Variância e desvio padrão
- Probabilidade básica
- Operações com probabilidades
- Eventos independentes
- Distribuição binomial
- Diagrama de Venn
- Quartis e AIQ (Amplitude Interquartílica)
- Correlação e regressão linear

## Como Executar

Para renderizar os vídeos, use:

```bash
manim -pql nome_arquivo.py NomeDaClasse
```

Exemplo:
```bash
manim -pql aritmetica_basica.py NumerosPrimos
```

**Opções de qualidade:**
- `-p`: reproduz o vídeo após renderizar
- `-q`: qualidade (l=baixa, m=média, h=alta, f=full)
- Recomenda-se usar `-pql` para visualização rápida durante o desenvolvimento

## Estrutura

Cada arquivo contém múltiplas classes `Scene`, cada uma representando um tópico ou conceito específico.

Todos os arquivos são compatíveis com Manim CE (Community Edition).

## Requisitos

Instale as dependências:
```bash
pip install -r requirements.txt
```

O requirements.txt contém:
```
manim
```

## Notas

- As animações foram criadas para serem claras e educativas
- Cada cena inclui explicações visuais e texto
- Os exemplos usam valores típicos encontrados em problemas de ensino médio
- Cores foram usadas para destacar conceitos importantes
- Fórmulas são apresentadas de forma gradual e animada