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
