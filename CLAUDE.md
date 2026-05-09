# Vinicio Project Guidelines

## Purpose

Interactive Strategic Decision Engine published on GitHub Pages. Not a dashboard that shows data — a scoring system where every item adds/subtracts from strategic position, recalculating in real-time based on user choices.

## **Mandatos**

$1 LEIA DO O DIRETORIO RECURSIVAMENTE @SHUN_TZU-ART_OF_WAR
$2 SIGA A ORDEM DE LEITURA CONFORME DOCS

$3  COMPREENDA A ENGINE OMNIBUS localizada em @SHUN_TZU-ART_OF_WAR/OMNIBUS/  ➞ esta engine eh utilizada em MEEST-AE [MODULO ESTRATEGICO]

$4 LEIA O Modulo estratégico em ordem de versions ➞  CADA VERSÃO APRENSENTA FUNCIONALIDADE ADICIONAL ➞  LEIA TODOS EM ORDEM 1.0 ➞ 2.0 ➞  2.1 ETC

$5 SPLICAR MEEST-AE E TODO OMBIBUS  PARA  REAZIKIZAR  AS TAREFA INTERATIZAR POSTERIORES.

$6 GÊRAR REGRAS E NORMAS PRA GARSBTIR MANUTENÇÃO CONTINUIDADE DO LONGOS CONTEXTOS ➞  


## Expected Deliverable

Vue app deployed at https://camillanapoles.github.io/lgpd-mkt-intel/ with:

- **Engine 100% dinamica item a item** — score recalcula com cada interacao
- **Dados de pesquisa = campo de batalha** — estaticos por definicao, sao as pecas no tabuleiro
- **Sliders = "e se mudar X"** — simulam cenarios what-if e recalculam tudo
- **Analise por canal** — cada audience com sua propria analise de cenario e pesquisa
- **Avaliacao geral + opcao por canal** — visao global e detalhamento por publico-alvo
- **Info button (i) por card** — explica o que eh cada item para quem nao conhece o jargao
- **Fonte VVV visivel** — cada card mostra link/fonte exata da informacao
- **Status page** — [PESQUISANDO] [CONCLUIDO] por item de pesquisa

## Architecture: Static Data vs Dynamic Interaction

```
DADOS ESTATICOS (cenário atual)          INTERACAO DINAMICA (what-if)
━━━━━━━━━━━━━━━━━━━━━━━━━━━           ━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• 38 itens SNTI com VVV                 • Sliders: LOIs, Advisor, Funding, ANPD
• 12 oportunidades com TAM              • slider_overrides → recalcula VVV por item
• 5 audiences com personas              • Score global reativo (header + tab)
• Game Theory payoff matrices           • Alertas por dimensao com acao recomendada
• PESTLE, Porter, SWOT, BMC             • Dimensao < 60 = CAUTELA, < 40 = NAO ATACAR
• Stakeholders, RACI                    • What-If badge mostra overrides ativos
```

**Principio**: dados de pesquisa sao as pecas do xadrez — estaticos, verificados. Sliders simulam "e se mover esta peca?" e o engine recalcula toda a posicao.

## Single Source of Truth

`presentation-vue/public/strategic-data-unified.json` — unico JSON, todas as tabs consomem dele. Qualquer agente que adicione informacao deve:
1. Colocar no JSON com VVV + fonte
2. Validar build passa
3. Deploy via GitHub Actions (bun)

## VVV Framework (Verificacao Verdade Valida)

Every data point must have VVV score (0.0-1.0):
- 1.0 = fato da transcricao
- 0.8-0.95 = fonte oficial citada
- 0.5-0.7 = analise fundamentada
- 0.0-0.4 = gap/nao verificado

Every card must show:
- VVV score visual (bar)
- Fonte/link exato (botao "i" expande com info)
- Status: [PESQUISANDO] | [CONCLUIDO] | [VALIDADO]

## Working Approach

- Coordinated multi-agent with parallel execution
- Incremental updates, no radical changes
- Business analysis agents produce data → validation agents verify VVV → UX agents improve presentation
- GitOps: commit → push main → GitHub Actions deploy
- Status page tracks research progress per item

## Governance (GOVERNANCE.md)

10 regras derivadas do OMNIBUS v10.0 + MEEST-AE v2.1. Arquivo: `presentation-vue/GOVERNANCE.md`.

Regras-chave:
- **R1**: VVV com Decay Temporal — `vvv_decay = vvv × 1/(1 + 0.30 × meses)`. Score SNTI usa `vvv_decay`, nao `vvv` estatico
- **R2**: Cartas na Mesa — cada item = carta com `id + description + dimensao + vvv + vvv_source + vvv_updated + fator + polaridade + criterios_dinamicos + certeza_agregada + shelf_life + proxima_revisao`
- **R3**: Sub-Engine por publico-alvo — cada audiencia tem seu proprio score SNTI (global vs por-público toggle)
- **R5**: Score honesto mesmo se baixo — NUNCA inflar VVV
- **R6**: Engine dinamico item-a-item — PROIBIDO scores hardcoded, logica de scoring no template, valores magicos sem VVV
- **R7**: Orquestracao reativa — slider muda → reavaliar TODOS os scores (global + dimensoes + itens)
- **R10**: Segregacao — JSON=dados, Vue=apresentacao, App.vue=orquestracao

**Leitura obrigatoria ao iniciar sessao**: GOVERNANCE.md + memory/MEMORY.md

## MEEST-AE Framework

Modulo Estrategico baseado em Sun Tzu. Versoes:
- **v1.0**: 7 principios inviolaveis, FDC-U, S→Q→I→A pipeline, VVV
- **v2.0**: DTS (50+ ferramentas), CNM (Cartas na Mesa), Decay Temporal (λ=0.30 SaaS)
- **v2.1**: MSP (Segmentacao + Personas), Sub-Engine por segmento, SWOT por persona

Aplicacao: cada item no JSON deve seguir estrutura CNM (R2). Info button mostra carta completa.

## Validation Rules

Every adjustment must have methodological + strategic justification grounded in market, business, benchmarking, stakeholder relevance. Without VVV justification, change is rejected.

## Quality Standard

- Build passa limpo (`bun run build`)
- Deploy ativo no GitHub Pages
- Score SNTI honesto (mesmo se baixo)
- E2E tests por tab (pendente)
- Info button explica cada card para leigos

## Pending Requirements

- [ ] Info button (i) por card com explicacao + fonte
- [ ] Status page [PESQUISANDO]/[CONCLUIDO] por item
- [ ] E2E tests por tab
- [ ] VVV audit contra transcritos (R5: 0.60 → 0.85+)
- [ ] Fontes file:linha nos itens SNTI (R1: 0.93 → 0.97)
