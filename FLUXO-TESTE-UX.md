# Fluxo de Teste UX - LGPD Market Intelligence

**Data:** 2025-05-08
**Persona:** Gestor Publico / Reuniao Estrategica
**Abordagem:** 5-second rule + task-based usability

---

## Resumo Executivo

Este documento define 10 cenarios de teste validando que a apresentacao LGPD transmite a mensagem principal em 5 segundos, permite comparacao de cenarios (Bull/Bear/Base), oferece BMC interativo, roadmap navegavel, SWOT filtravel, e funciona perfeitamente em mobile.

---

## Cenarios de Teste

### 1. Dashboard Inicial - KPIs em 5 Segundos

**Objetivo:** Usuario identifica proposta + KPIs + CTAs em <= 5s

**Usuario clica:** N/A (apenas visualizacao inicial)

**Esperado:**
- Proposta de valor visivel: "Conformidade LGPD para Prefeituras"
- 3 KPIs principais: 5.570 municipios, 72% sem LGPD, R$60Mi TAM/ano
- CTAs claros: "Ver Pesquisa" e "Roadmap MVP"

**Pass/Fail:**
- [ ] Hero H1 >= 24px (mobile) / 48px+ (desktop)
- [ ] KPIs em grid visivel sem scroll
- [ ] Contraste >= 4.5:1 (WCAG AA)
- [ ] CTAs com touch target >= 44x44px

---

### 2. Selector de Cenarios - Comparacao Bull/Bear/Base

**Objetivo:** Toggle instantaneo entre planos Prefeituras/Empresas

**Usuario clica:** Abas "Prefeituras" e "Empresas" na secao Pricing

**Esperado:**
- Toggle < 150ms
- Highlight visual no plano ativo (border + box-shadow)
- Precos atualizados sem layout shift

**Pass/Fail:**
- [ ] Transicao 150-300ms ease-out
- [ ] .tab-btn.active com background var(--c-accent)
- [ ] CLS < 0.1 durante troca
- [ ] Planos reorganizam fluido

---

### 3. BMC Interativo

**Objetivo:** Cards de Business Model Canvas expandem com detalhes

**Usuario clica:** Qualquer card/bloco do BMC

**Esperado:**
- Hover: translateY(-3px) + shadow
- Click: feedback em <100ms
- Expansao respeita line-length 60-75 chars
- Mobile: sheet/modal, nao inline

**Pass/Fail:**
- [ ] Hover state visivel
- [ ] Click feedback <100ms
- [ ] Texto legivel (nao muito longo)
- [ ] Mobile: modal/sheet, nao inline expansion

---

### 4. Roadmap Timeline Interativa

**Objetivo:** Timeline navegavel com fases claramente separadas

**Usuario rola:** Seccao Roadmap

**Esperado:**
- Reveal animation (opacity + translateY)
- Stagger 30-50ms entre itens
- Timeline dots coloridos (20px)
- Mobile: adaptada (horizontal scroll simplificada)

**Pass/Fail:**
- [ ] .reveal.visible ativa animacao
- [ ] Stagger implementado
- [ ] Dots >= 20px, contraste suficiente
- [ ] Mobile nao quebra layout

---

### 5. SWOT Interativo - Filtro por Categoria

**Objetivo:** Filtrar S/W/O/T com feedback visual claro

**Usuario clica:** Filtros S/W/O/T

**Esperado:**
- Active state: border + background
- Itens filtrados: opacidade 0.5 (NUNCA 0)
- Icon + texto (nao so cor)
- Screen reader anuncia mudanca

**Pass/Fail:**
- [ ] Active state visivel
- [ ] Opacidade 0.5 (WCAG)
- [ ] Icon/texto para distinguish
- [ ] Aria-live anuncia filtro

---

### 6. Mobile - Tela Pequena (375px)

**Objetivo:** Tudo funciona sem horizontal scroll

**Usuario acessa:** Smartphone (375x667px)

**Esperado:**
- Nav bar nao cobre conteudo
- Grids colapsam para 1 coluna
- Buttons >= 44x44px
- Zero horizontal scroll

**Pass/Fail:**
- [ ] Nav: h-14 + padding-bottom em main
- [ ] Grids: grid-cols-1
- [ ] Buttons: min-height 44px
- [ ] Overflow-x: hidden verificado

---

### 7. Acessibilidade - Navegacao por Teclado

**Objetivo:** Full keyboard navigation

**Usuario usa:** Tab para navegar

**Esperado:**
- Focus ring visivel (2-4px)
- Ordem logica DOM
- Skip link no topo
- Heading hierarchy: h1 -> h2

**Pass/Fail:**
- [ ] Focus ring 2px solid
- [ ] Tab order logica
- [ ] Skip link presente
- [ ] H1 unico, h2s sequenciais

---

### 8. Charts - Grafico de Municipios

**Objetivo:** Grafico acessivel com tooltip + legenda

**Usuario visualiza:** Canvas chartPref

**Esperado:**
- Cores acessiveis (nao so verde/vermelho)
- Tooltip ao hover/tap
- Legenda proxima
- Table alternativa para SR

**Pass/Fail:**
- [ ] Padrao + icon/texto
- [ ] Tooltip com valor + %
- [ ] Legenda visivel
- [ ] <table> com dados

---

### 9. Performance - Carregamento Inicial

**Objetivo:** CWV "Good" (LCP < 2.5s, FID < 100ms, CLS < 0.1)

**Usuario abre:** URL primeira vez (cache limpo)

**Esperado:**
- Fontes com font-display: swap
- Imagens WebP/AVIF, lazy load
- Reserva espaco (CLS < 0.1)
- Scripts defer/async

**Pass/Fail:**
- [ ] Font-display: swap
- [ ] WebP/AVIF com srcset
- [ ] Width/height em imagens
- [ ] Scripts nao bloqueiam render

---

### 10. Dark Mode / Contrast Check

**Objetivo:** Todos os textos legiveis em dark gradient

**Usuario alterna:** Dark mode (se suportado)

**Esperado:**
- Contraste >= 4.5:1
- Bordas visiveis
- States distinguishaveis
- Semantic colors claras

**Pass/Fail:**
- [ ] Text: slate-300/400 em dark
- [ ] Borders: rgba(255,255,255,.08)
- [ ] States: hover/active visiveis
- [ ] Error/solution colors testadas

---

## Checklist UX

### CRITICAL (Block)

- [ ] Contraste minimo 4.5:1 para texto
- [ ] Touch targets >= 44x44px
- [ ] Alt text descritivo
- [ ] Keyboard navigation funcional

### HIGH (Warn)

- [ ] Zero horizontal scroll em mobile
- [ ] Feedback visual <100ms
- [ ] Viewport meta correto
- [ ] Heading hierarchy sequencial

### MEDIUM (Info)

- [ ] Animacoes 150-300ms + reduced-motion
- [ ] Fontes com font-display: swap
- [ ] Espacamento 4pt/8dp
- [ ] Cor nao como unico indicador

---

## Acessibilidade WCAG AA

| Criterio | Nivel | Test |
|----------|-------|------|
| 1.4.3 Contrast | AA | Text < 24px: 4.5:1 |
| 2.4.7 Focus Visible | AA | 2-4px indicator |
| 1.1.1 Non-text Content | A | Alt descritivo |
| 2.1.1 Keyboard | A | Full keyboard access |
| 1.4.10 Reflow | AA | No horizontal scroll 320px |
| 1.4.4 Resize text | AA | 200% zoom funcional |

---

## Mobile Breakpoints

### Small (320-374px)
- Nav: sticky, nao esconder conteudo
- Grids: 1 coluna
- Typography: base 16px
- Touch: 44x44px min
- Charts: horizontal bar
- Tables: scroll horizontal

### Medium (375-767px)
- Nav: hamburger se >5 items
- Cards: full width
- Timeline: vertical se preciso
- Modals: sheet bottom-up

### Large (768-1023px)
- Grids: 2 colunas
- Nav: todos links visiveis
- Tables: full width
- Images: srcset

### XLarge (1024px+)
- Grids: 3-4 colunas
- Max-width: max-w-6xl/7xl
- Spacing: aumentado
- Charts: full detail

---

## Performance Targets

| Metrico | Target | Ferramenta |
|---------|--------|------------|
| LCP | < 2.5s | Lighthouse |
| FID | < 100ms | CrUX |
| CLS | < 0.1 | Lighthouse |
| TTI | < 3.5s | WebPageTest |
| FCP | < 1.8s | Lighthouse |

---

## Protocolo de Teste

### Pre-teste
1. Limpar cache (incognito)
2. Viewport 375x667px + 1920x1080px
3. prefers-reduced-motion: reduce
4. DevTools aberto (Lighthouse)

### Durante teste
1. Gravar sessao
2. Notar friction points
3. Medir tempo por tarefa
4. Verificar console (erros JS)

### Pos-teste
1. Lighthouse audit
2. axe DevTools
3. Compilar findings por prioridade
4. Relatorio com screenshots

---

## Criteria de Sucesso

- **5-second rule:** Proposta + 3 KPIs + CTAs em 5s
- **Task completion:** 90%+ sem assistencia
- **Satisfaction:** SUS score > 70
- **Errors:** Zero critical blocking tasks

---

## Arquivos Relacionados

- JSON detalhado: `test-flow-ux.json`
- Apresentacao: `index.html`
- Dados: `strategic-data.json`

---

**Gerado via ui-ux-pro-max skill**
