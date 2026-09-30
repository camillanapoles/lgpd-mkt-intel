# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## Natureza do Repositório

Este NÃO é um repositório de código-fonte. É um **workspace de planejamento estratégico** para o projeto **NeoGov BP v2.1** (Business Plan v2.1) — produto de governança LGPD/ICT. Todos os artefatos são documentos analíticos (Markdown, DOCX, JSON, XLSX). O "build" é a consolidação documental final (Markdown canônico → Pandoc DOCX + Vue3 app + PDF).

Idioma operacional: **Português (pt-BR)**.

## Documento Constitucional (LEITURA OBRIGATÓRIA ANTES DE QUALQUER AÇÃO)

`INSTRUCAO-PROTOCOLO-OPERACIONAL-NEOGOV-latest.md` é o **POP (Protocolo Operacional Master)** — autoridade constitucional do projeto. Sobrescreve qualquer instrução conflitante. Em qualquer dúvida operacional, consultar §0 (índice funcional) desse arquivo.

Hierarquia de fontes canônicas (POP §2, ordem decrescente de autoridade):
1. `inst-lgpd.md` (lógica geradora DT, externa)
2. `SESSION-STATE-latest.md` (WAL Master)
3. `INSTRUCAO-PROTOCOLO-OPERACIONAL-NEOGOV-latest.md` (POP)
4. `NEOGOV-BUSINESS-PLAN-FINAL.{docx,md}` (BP v2.0 aprovado)
5. `NEOGOV-DATA-v2.json`
6. Anexos vivos `APENDICE-{A,B,C,E}-latest.md`
7. Débitos `DEBITO/DEBITO-D00X-*.md`
8. Capítulos `{NN}-{nome}-latest.md`

Drafts `NEOGOV-BSC-*`, `NEOGOV-FDCU-*` são **insumos**, não autoridade operacional.

## Padrão de Versionamento (POP §5 — MANDATÓRIO)

```
{filename}-v[N].{SPRINT}.{EDICAO}.{ext}   ← imutável, versionado
{filename}-latest.{ext}                    ← cópia da edição mais recente
```

Regra crítica: **criar a próxima edição ANTES de receber edits** (preserva histórico imutável). Após editar, atualizar a cópia `-latest`.

Cada subpasta (`CONTINUIDADE/`, `SESSION-STATE/`, `DEBITO/`, `APENDICE-A-VVV-LOG/`, etc.) mantém o histórico versionado; a raiz mantém apenas o `-latest`.

## Sistema de Continuidade (POP §9 — 4 camadas)

Toda execução de sprint atualiza obrigatoriamente:

| Camada | Arquivo | Função |
|---|---|---|
| WAL Master | `SESSION-STATE-latest.md` | Estado vivo + hash de continuidade + fila DTP |
| VVV Log | `APENDICE-A-VVV-LOG-latest.md` | Toda afirmação factual com tag + VVV score |
| Decision Log | `APENDICE-B-DECISIONS-LOG-latest.md` | Toda decisão com rationale + opções rejeitadas |
| Insight Carry | `APENDICE-C-INSIGHTS-CARRY-latest.md` | Insights emergentes para próximos sprints |

Nenhum sprint começa sem ler as 4 camadas; nenhum sprint termina sem incrementá-las.

## Sistema de Marcadores Visuais (POP §4 — D-015)

**Toda afirmação numérica/quantitativa** em qualquer artefato DEVE usar:

| Marcador | Tipo | VVV |
|---|---|---:|
| ✅ Verde | FATO verificado | 0.90–1.00 |
| 🟢 Verde-escuro | INFERÊNCIA com base em fato | 0.80–0.89 |
| 🟡 Amarelo | ESTIMATIVA POR ANÁLOGO (exige LASTRO) | 0.60–0.79 |
| 🟠 Laranja | ESPECULAÇÃO fundamentada | 0.40–0.59 |
| 🔴 Vermelho | ESPECULAÇÃO sem base — NÃO USAR | <0.40 |

Toda estimativa 🟡 requer: emoji + tag `[ESTIMATIVA POR ANÁLOGO]` + entrada em `APENDICE-E-LASTREAMENTO-latest.md` no formato YAML do POP §7.3.

## Mandato Técnico Inegociável (POP §6 — D003 v2)

Modelo de LLM é **OBJETO DE PRODUTO**: **MANDATORIAMENTE LOCAL, PRÓPRIO, TREINADO PELA EQUIPE**. Sem API externa (Anthropic/OpenAI/Maritaca) para dado pessoal/legal. Stack: Llama 3.1 8B base + QLoRA/DoRA + Qdrant + LangGraph + vLLM + cloud BR (Magalu/TIVIT/Locaweb). Detalhamento: `DEBITO/DEBITO-D003-ARQUITETURA-AGENTIC-SOBERANA-v2.1.4.5.md`.

## Constituição (POP §1) — Proibições e Imperativos

```
🚫 NUNCA execute sem analisar CENÁRIO e PLANEJAR (5W1H)
🚫 NUNCA decida sem dados · NUNCA CHUTE · NUNCA atue em DÚVIDA
🚫 NUNCA gere PMQS/VVV inflado · NUNCA estimativa sem 🟡 + LASTRO
🚫 NUNCA assuma API externa de IA para dado pessoal/legal NeoGov
🚫 NUNCA modele custo antes de definir arquitetura técnica

✅ SEMPRE enumere TODOS os caminhos antes de escolher
✅ SEMPRE respeite ordem topológica (dependências)
✅ SEMPRE INVESTIGUE / COLETE / PESQUISE antes de afirmar
✅ SEMPRE versione artefato com edição antecipada
✅ SEMPRE marque estimativa com 🟡 + lastro rastreável
```

Anti-padrões absolutos enumerados em POP §3 (AP-01 a AP-15).

## Engine Cognitiva e Skills

**Pipeline obrigatório S→Q→I→A** (Layer 0.5 — `skills/ENGINE-MODULES/COGNITIVE_ARCHITECTURE_COMPLETE.md`):
- [S] Socrático (deconstruir / epómetrismo / maiêutica)
- [Q] Questionador (5N + classificação FACT/INFERENCE/SPECULATION/BELIEF)
- [I] Inovador (analogia estrutural, recombinação, compressão fractal micro/meso/macro)
- [A] Adversarial (advocatus diaboli, falsificação popperiana, checklist de viés)

Módulos relevantes em `skills/`:
- `ENGINE-MODULES/COGNITIVE_ARCHITECTURE_COMPLETE.md` — Layer 0/0.5/1/2
- `ENGINE-MODULES/HOLISTIC_ITERATIVE_QUALITY_MODULE_v1.0.md` — HIQM (qualidade ≥95%)
- `ENGINE-MODULES/STRATEGIC-ACTION-ENGINE-v4.0.md` — SAE
- `ENGINE-MODULES/MODULO-DOCUMENTACAO-TECNICA-v1.0.md` — MDT
- `SHUN_TZU-ART_OF_WAR/MEEST-AE_v2.1.md` — MEEST-AE (estratégia + segmentação MSP)

**Skills de análise de negócio** disponíveis (plugin `business-analysis:*`): preferir invocação via Skill tool ao realizar:
- Estimativas → `estimation` (parametric / analogous)
- Stakeholders → `stakeholder-analysis`
- Jornadas → `journey-mapping`
- Riscos → `risk-analysis`
- Decisões → `decision-analysis`
- Processos → `process-modeling`
- SWOT/PESTLE/Porter → `swot-pestle-analysis`
- BMC → `business-model-canvas`

## Workflow por Sprint (POP §11)

```
PRE-ALWAYS (Clarificação) → KDI (skill selection) → PIER (3-5 abordagens)
  → PEII-LLM (7 fases) → PMQS (≥8.0 realista, ≥9.5 ouro) → VVV → KAIZEN → WAL
```

PMQS pesos canônicos: CE 15% · PI 15% · CC 10% · PRI 20% · RA 15% · EIC 10% · OVA 15% · VVV (multiplicador 0–1). Alvo realista: **≥ 8.0** (D-007 — não inflar).

## Tripé Multi-Output (POP §10)

Markdown é canônico. DOCX e Vue app são gerados a partir dele — nunca o inverso.

| Formato | Path | Audiência |
|---|---|---|
| Markdown | `content/{NN}-{nome}-latest.md` | Git, auditável |
| Word DOCX | `NEOGOV-BUSINESS-PLAN-FINAL.docx` | Executivos, stakeholders |
| Vue 3 App | `app/dist/` (GitHub Pages) | Prospects, público |

## Estado Atual (verificar `SESSION-STATE-latest.md` antes de agir)

- Hash ativo: `NEOGOV-V21-S3.0.3-v1.0-WTP-PROTOCOL-READY-FOR-EXECUTION-BLUEPRINT-BAS-DOCUMENTED`
- Sprint atual: **S3.0.3 v1.0** entregue (Van Westendorp WTP Protocol)
- Bloqueios constitucionais ativos (POP §8): Sprint **2.5** (D003 v2 — IA Própria) precede **3.0** (D001 — custos) precede **5.0.5** (D002 — auditoria cognitiva)

## Organização de Diretórios

| Pasta | Conteúdo |
|---|---|
| Raiz | Cópias `-latest` de capítulos, anexos, protocolo, BP |
| `CONTINUIDADE/` | Histórico versionado de capítulos e sprints |
| `SESSION-STATE/` | Histórico versionado do WAL master |
| `APENDICE-A-VVV-LOG/` | Histórico do log de validação |
| `APENDICE-B-DECISIONS-LOG/` | Histórico do log de decisões |
| `APENDICE-C-INSIGHTS-CARRY/` | Histórico do log de insights |
| `APENDICE-E-LASTREAMENTO/` | Histórico do log de lastros |
| `DEBITO/` | Débitos técnicos D001/D002/D003 versionados |
| `skills/ENGINE-MODULES/` | Módulos cognitivos da engine |
| `skills/SHUN_TZU-ART_OF_WAR/` | MEEST-AE (estratégia) |
| `skills/.omc/` | Sessões e estado OMC |
| `.archives-memoria/` | Drafts antigos e memória legada |

## Convenções de Citação de Fontes (citação mandatória)

Toda resposta com afirmação factual cita em linha:
- `[FILE: path:L##-L##]` para arquivos do repo
- `[WEB: url]`, `[MCP: server/tool]`, `[TRAINING]`, `[INFERRED: from X]` conforme aplicável

Finalizar com seção **Sources**.

## Gates e Critérios de Parada (POP §12)

- ✅ Sucesso: progresso = 100% objetivo AND VVV ≥ 0.85 AND PMQS ≥ 8.0
- ⚖️ Custo marginal > valor marginal → documentar no WAL
- ⛔ Bloqueio externo irredutível → gerar WAL-handoff
- 🛑 DEC↔COR > 3 ciclos → ESCALADA HUMANA obrigatória

Nunca declarar gate aberto sem evidência; nunca pular gate; nunca reabrir gate fechado sem nova decisão registrada (decision log).

---

## Sources

- [FILE: INSTRUCAO-PROTOCOLO-OPERACIONAL-NEOGOV-latest.md:L1-L609] — POP master, hierarquia de fontes, versionamento, marcadores visuais, mandato D003, fila DTP, 4 camadas, PMQS, gates, anti-padrões
- [FILE: INSTRUCAO_INJCIAL.md:L1-L55] — Constituição inicial (Artigos 1/2/3, fases DTP)
- [FILE: SESSION-STATE-latest.md:L1-L100] — Estado atual Sprint 3.0.3, hash de continuidade
- [FILE: MEMORY-BACKUP.md:L1-L8] — Índice de memória legada (pricing/clusters/ETL/produtos)
- [FILE: PLANO-CONTINUIDADE-LAST.md:L1-L120] — Arquitetura de continuidade e versionamento
- [FILE: skills/ENGINE-MODULES/COGNITIVE_ARCHITECTURE_COMPLETE.md:L1-L259] — Engine S→Q→I→A, Layer 0/0.5/1/2
- [FILE: skills/ENGINE-MODULES/HOLISTIC_ITERATIVE_QUALITY_MODULE_v1.0.md:L1-L60] — HIQM
- [FILE: skills/SHUN_TZU-ART_OF_WAR/MEEST-AE_v2.1.md:L1-L80] — MEEST-AE v2.1
- [INFERRED: from `ls` da raiz e subpastas] — Organização de diretórios e padrão de cópias `-latest`


---

# APÊNDICE — App Estratégica (presentation-vue, linha LGPD_old)

# Vinicio Project Guidelines

## Purpose

Interactive Strategic Decision Engine published on GitHub Pages. Not a dashboard that shows data — a scoring system where every item adds/subtracts from strategic position, recalculating in real-time based on user choices.

## **Mandatos**

$1 LEIA DO O DIRETORIO RECURSIVAMENTE @SHUN_TZU-ART_OF_WAR
$2 SIGA A ORDEM DE LEITURA CONFORME DOCS

$3 COMPREENDA A ENGINE OMNIBUS localizada em @SHUN_TZU-ART_OF_WAR/OMNIBUS/ ➞ esta engine eh utilizada em MEEST-AE [MODULO ESTRATEGICO]

$4 LEIA O Modulo estratégico em ordem de versions ➞ CADA VERSÃO APRENSENTA FUNCIONALIDADE ADICIONAL ➞ LEIA TODOS EM ORDEM 1.0 ➞ 2.0 ➞ 2.1 ETC

$5 SPLICAR MEEST-AE E TODO OMBIBUS PARA REAZIKIZAR AS TAREFA INTERATIZAR POSTERIORES.

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

# ACOES PARA CONTROLE DE ATUACAO:

# 📜 CONSTITUTION MODULE (Mandatos Absolutos)

## ⛔ INEGOCIÁVEIS UNIVERSAIS [Referência única de verdade]

**ARTIGO 1 - Proibições Universais** (Aplicável a todas as camadas)

```
🚫 NUNCA execute sem resolver dependências primeiro
🚫 NUNCA siga plano obsoleto ➞ re-avaliar após cada ação
🚫 NUNCA decida sem dados ➞ INVESTIGAÇÃO precede decisão
🚫 NUNCA atue em DUVIDA
🚫 NUNCA CHUTE
🚫 NUNCA EXECUTE ANTES SEM INVESTIGAR / PLANEJAR
```

**ARTIGO 2 - Imperativos Universais** (Aplicável a todas as camadas)

```
✅ SEMPRE enumere TODOS os caminhos antes de escolher
✅ SEMPRE respeite ordem topológica (dependências)
✅ SEMPRE re-avalie campo após cada execução
✅ SEMPRE INVESTIGUE, COLETE INFORMACOES DE ESTADO E PESQUISA
✅ SEMPRE PRIORIZAR SOLUCOES BEST PRACTICIES SOTA 2026
✅ SEMPRE DISPATCH para protocolo correto conforme estado atual
```

**ARTIGO 3 - Regras de Ouro** (Invariâncias operacionais)

```
🔶 REGRA_DE_OURO_1: Cada execução MUDA o campo ➞ re-avaliar ANTES da próxima
🔶 REGRA_DE_OURO_2: Nenhuma task é "done" sem EVIDÊNCIA DE FUNCIONAMENTO REAL
🔶 REGRA_DE_OURO_3: Minimizar refatoração = decidir na ordem certa
🔶 REGRA_DE_OURO_4: Maximizar qualidade = não construir sobre base instável
```

# LAYER 0 - PRINCÍPIOS EPISTEMOLÓGICOS INVIOLÁVEIS

## 0.1 MANDATOS ABSOLUTOS

```
PRIORITY[CRITICAL]:
  ├─ NO_HALLUCINATION: Geração proibida de fatos, fontes ou dados inexistentes
  ├─ TRUTH_VALIDATION: Toda afirmação factual requer âncora em fonte verificável (primária > secundária > terciária)
  ├─ RECENCY_BIAS[3M]: Em domains voláteis (tech, econ, sci), dados dos últimos 3 meses têm peso superior
  ├─ ZERO_BIAS_PROTOCOL: Neutralidade epistêmica - suspender juízos de valor sem evidência quantificável
  └─ BEST_PRACTICES_CURRENT: Priorizar estado da arte dos últimos 3 meses + fundamentos estáveis validados
```

## 0.2 SISTEMA DE GAMIFICAÇÃO E QUALIDADE

```
METRIC: QUALITY_SCORE (0-100)
RULES:
  Base: 100 pts por resposta
  Penalty[-1]: Elogio ao usuário sem evidência factual ou validação lógica rigorosa (DIMINUIREI 1 PT NA AVALIAÇÃO)
  Penalty[-5]: Violação de NO_HALLUCINATION
  Penalty[-3]: Falha no stress-test adversarial (Layer 0.5-A)
  Penalty[-2]: Não identificação de viés próprio
  Bonus[+2]: Detecção de bias não-solicitado no input
  Bonus[+5]: Cross-domain correlation não-óbvia validada

THRESHOLD: Se QUALITY_SCORE < 95, reprocessar antes de output final
```

busque tambem en /tac adw aplique nos módulos estão
utilizandooa a Skill
refletir econforme o omnibus bootstrap e constfuir o adw OMNIBUS ➞
DEPOIS USANDO O ÔMINIBHS [SISTEMA] USAR O SHITZU MODUKOS 1, 2 E
2.1 CONFORME ORQUESTRADO leia iniciamentes de
@../SHUN_TZU-ART_OF_WAR/OMNIBUS/**.md ➞ ENTENDA MANDSTORIAMENTE
QUE SE TRATA DE ORQUESTRACAO DE AGEBTES [ENGENHARIA DE CONTEXTO]
CONTEBDO TODO FKUXO POR DOCUMENTO ➞ COMO UM MODULO E SCRIOTS DO
MODULO disto gerafa plugin ➞ em
OMNIBUS_MODULO/OMNIBUS_BOOTSTRAP_SYSTEM_v10.0.md EH COMO MAIN ➞
PARALELO OUTROS SCRIPT [ATUAM JUNRO DO ECOSISTEMA OMNIBUS] EM
OMNIBUS_MODULO/OMNIBUS/** TEM SCRIOTS CHAMADAS POR
OMNIBUS_MODULO/OMNIBUS_BOOTSTRAP_SYSTEM_v10.0.md , COMO DISSE POR
ANALOGIA UM MODULO LIB COM SCRIOTS D€STE. ENTENDEU?

OBJETIVO FINAL

└─ USAR AGENTES @/home/cnmfs/.claude/plugins/shuntzu-omnibus/agents/omnibus-orchestrator.md para atuar em research ➞ analysis/ completo (PESTLE, Porter, market-research, risk-strategy, FDC-U validation,Audiences: ['b2g_prefeituras', 'b2g_consorcios', 'b2b_fornecedores_municipio', 'b2b_empresas_privadas', 'b2g_est] ) ➞ NAOBTEM VALIDAÇÃO DE EXECUCAO CONFORME OMNIBUS
shuntzu-f3 MSP Phase 1 = Universe Mapping — descobrir
audiences reais dos docs de negócio, não assumir as 5
existentes.
└─ COM DADOS DE PESQUISA ➞ COLETAR OSNPROVAVEIS CHAINS UDANDO SHITZU-OMNIBUS [F1, F2 , F3] ➞ @/home/cnmfs/.claude/plugins/shuntzu-omnibus/skills/shuntzu-f3/SKILL.md

1. Agentes carregam OMNIBUS MODULE — S→Q→I→A, VVV, FDC-U, HIQM [e modulos convocados] embutidos no prompt
2. SWOT scoring muda — com VVV e Impacto(1-5) ×
   Probabilidade(1-5) conforme MEEST-AE v2.1 MSP-3
3. S→Q→I→A trace por item — cada item SWOT tem trace documentado
4. VI/AE formula muda — range -1 a +1 (nao 0 a 1) conforme MEEST-AE
   v2.1
5. Phase 0 de limpeza — dados antigos sem metodologia serao removidos
6. Quality gate explicito — ≥3 items/cat, SQIA em cada item, VVV com fonte

PARA ENTREGAVEL SER: o demandando em @CLAUDE.md
└─ ITERAVAO, INFORMACAO, BACKEND ➞ EH VIA AGENTE OMNIBUS + SHITZU-OMINIBUS

● ★ Insight ─────────────────────────────────────
JSON tem sqia_trace (campo antigo v1) mas não sqia_trace_v2.
Análises em analysis/ têm VVV scores (pestle-porter usa V=9/10 notation, swot-transcricao usa 0.0-1.0) mas zero traces S→Q→I→A, zero WAL entries, zero vvv_provenance=omnibus-pipeline-real. O plugin shuntzu-omnibus já existe com todos os 12 skills + orchestrator — o plano é usá-los como agentes reais sobre os dados existentes.

Dependência real:

PESTLE/SWOT/Market ──► F3-MSP (F3 USA outputs deles como
contexto)
│
▼
audiences validadas
│
▼
sub-engines por persona

PESTLE, SWOT, Market são INPUT de F3 — não o contrário.

F3-MSP já leu swot-transcricao.yaml (Stage S confirmado) como
fonte. Quando F3 chegar em [I] (síntese FDC-U), vai precisar dos
scores PESTLE e SWOT completados para calibrar os custom_weights por segmento.

Conclusão: PESTLE [A] + SWOT [I]+[A] + Market [I]+[A] devem completar antes de F3 chegar no Stage [I].

$1 MANDARO ABSOKUTO ➞ DESCONSIDERAR E NAONUTIKIZAR EM HIPOTESE ALGUMA DADOS DE PESQUISA QUE NAO TENHA SEGUIDOO FORMA E ORQUESTRACAO OMNIBUS ➞ garabta tb nao voltar a acontecer [arquive estes dados para nao atraoalahr andamenro]
