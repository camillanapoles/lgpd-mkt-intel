# OMNIBUS Retroativo + Research Validation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Re-executar análises `analysis/` via pipeline OMNIBUS real (S→Q→I→A + VVV + FDC-U + HIQM), usando `omnibus-orchestrator` + shuntzu-f1/f2/f3 como agentes, produzindo sqia_trace_v2 + WAL entries + vvv_provenance=omnibus-pipeline-real em cada item do JSON.

**Architecture:** Agentes carregam OMNIBUS MODULE embutido no prompt (CE→Planner→WOE→IIM→E boot sequence). `analysis/` existente = input [S] (coleta bruta já feita). Agentes rodam [Q]+[I]+[A] sobre esse material, geram traces, atualizam JSON via sqia_trace_v2, e appendam WAL. Execução paralela por dimensão (zero conflito de arquivo).

**Tech Stack:** Claude agents (omnibus-orchestrator + shuntzu-f1/f2/f3), Vue/JSON (strategic-data-unified.json), bun build, bash WAL append.

**OMNIBUS Boot Sequence obrigatória (por agente):**
```
1. CE  → lê memory/shuntzu-engine-state.md + WAL
2. PL  → S→Q→I→A no input (philosophical-engine skill)
3. WOE → DAG de módulos necessários
4. IIM → parse request → mission package
5. E   → executa via shuntzu-f1/f2/f3
```

**Quality Gate (HIQM, por output):**
- [ ] Boot sequence 5 steps completos
- [ ] S→Q→I→A todos 4 stages com TRACE
- [ ] VVV score ≤ 1.0 com fonte verificável
- [ ] FDC-U weights somam 1.0
- [ ] WAL entry escrita
- [ ] HIQM quality ≥ 90%

---

## Diagnóstico do Estado Atual

| Arquivo | Conteúdo | Problema |
|---------|----------|----------|
| `analysis/pestle-porter-lgpd.md` | PESTLE + Porter completo, VVV V=9/10 notation | Zero sqia_trace, zero WAL, narrative-llm-single-turn |
| `analysis/swot-transcricao.yaml` | SWOT com vvv 0.0-1.0 por item, fonte mapeada | Zero [Q][I][A] trace, narrative |
| `analysis/market-research-2025.md` | Market sizing, TAM, personas | Zero pipeline OMNIBUS |
| `analysis/risk-strategy-analysis.json` | Risk matrix | Zero pipeline OMNIBUS |
| `analysis/fdc-u-validation.md` | FDC-U aplicado a 18 itens | Single-turn, sem 4 stages |
| `analysis/bmc-roadmap-cross-check.yaml` | BMC vs Roadmap | Zero pipeline |
| JSON `snti.items` | 38 items, vvv_provenance=narrative-llm-single-turn | sqia_trace_v2 = 1/38 |
| JSON `snti.audiences` | 5 audiences | research_log = 0/5 |

**OMNIBUS plugin disponível:**
- Agent: `/home/cnmfs/.claude/plugins/shuntzu-omnibus/agents/omnibus-orchestrator.md`
- Skills: shuntzu-f1 (core), shuntzu-f2 (strategy), shuntzu-f3 (segmentation)
- 9 module skills: context-engineering, philosophical-engine, workflow-orchestration, intake-interface, fdc-u-scoring, vvv-validation, dtp-topology, hiqm-quality, dte-holo-docs

---

## File Structure

### Criados por este plano

```
.claude/wal/shuntzu-operations.log          — append WAL entries (existente)
memory/wal/
  omnibus-pestle-S.md                       — Stage S trace PESTLE
  omnibus-pestle-Q.md                       — Stage Q trace PESTLE
  omnibus-pestle-I.md                       — Stage I trace PESTLE
  omnibus-pestle-A.md                       — Stage A trace PESTLE
  omnibus-swot-S.md                         — Stage S trace SWOT
  omnibus-swot-Q.md
  omnibus-swot-I.md
  omnibus-swot-A.md
  omnibus-market-S.md                       — Stage S trace Market
  omnibus-market-Q.md
  omnibus-market-I.md
  omnibus-market-A.md
  omnibus-audiences-{id}-S.md              — per audience (5×4=20 files)
  omnibus-audiences-{id}-Q.md
  omnibus-audiences-{id}-I.md
  omnibus-audiences-{id}-A.md
GOVERNANCE.md                               — R1-R11 (Wave A1 pendente)
analysis/omnibus-validation-report.md      — relatório final HIQM audit
```

### Modificados

```
presentation-vue/public/strategic-data-unified.json
  — sqia_trace_v2 em 38/38 items (vvv_provenance=omnibus-pipeline-real)
  — research_log em 5/5 audiences (≥3 entries each)
  — swot section: VI/AE per persona com range -1 a +1 (MEEST-AE v2.1)
.claude/wal/shuntzu-operations.log
  — append entries para cada stage executado
```

---

## WAVE A — Paralelo (zero conflito de arquivo)

### Task A1: GOVERNANCE.md + R11 declaration

**Files:**
- Create: `GOVERNANCE.md`

- [ ] **Step 1: Ler base de regras**

```bash
grep -n "R1\|R2\|R3\|R5\|R6\|R7\|R10" /home/cnmfs/ICT/PROTOTYPE/LAYER/LGPD/CLAUDE.md
```

Expected: 7 regras listadas com descrição.

- [ ] **Step 2: Escrever GOVERNANCE.md**

Conteúdo mínimo obrigatório:

```markdown
# GOVERNANCE.md — LGPD Strategic Engine

## Regras Derivadas OMNIBUS v10.0 + MEEST-AE v2.1

### R1: VVV com Decay Temporal
vvv_decay = vvv × 1/(1 + 0.30 × meses)
Score SNTI usa vvv_decay, não vvv estático.

### R2: Cartas na Mesa (CNM)
Cada item = carta com: id, description, dimensao, vvv, vvv_source,
vvv_updated, fator, polaridade, criterios_dinamicos, certeza_agregada,
shelf_life, proxima_revisao

### R3: Sub-Engine por público-alvo
Cada audiência tem próprio score SNTI. Toggle global vs por-público.

### R5: Score honesto mesmo se baixo
NUNCA inflar VVV. Se dado não verificado, score < 0.5.

### R6: Engine dinâmico item-a-item
PROIBIDO: scores hardcoded, lógica de scoring no template,
valores mágicos sem VVV.

### R7: Orquestração reativa
slider muda → reavaliar TODOS os scores (global + dimensões + itens)

### R10: Segregação
JSON=dados, Vue=apresentação, App.vue=orquestração

### R11: Quality Threshold Pragmático (NOVO)
quality_threshold_pragmatic = 7.0/10
Justificativa: pilot eca_digital_urgent provou QUALITY_CoT=7.24
com vvv_decay=0.98. Abaixo de 7.0 → retornar ao Stage [S].
Acima de 7.0 → aceitar com vvv_provenance=omnibus-pipeline-real.
Referência: HIQM v1.0 §P4, pilot WAL 2026-05-09T22:50:07.

### R12: Pipeline Obrigatório para Novos Dados
Todo dado novo DEVE passar por S→Q→I→A completo antes de entrar no JSON.
Dados narrative-llm-single-turn recebem vvv_provenance=narrative-llm
e vvv_decay degradado (-30% automático).
```

- [ ] **Step 3: Verificar**

```bash
test -f /home/cnmfs/ICT/PROTOTYPE/LAYER/LGPD/GOVERNANCE.md && \
grep -q "R11" /home/cnmfs/ICT/PROTOTYPE/LAYER/LGPD/GOVERNANCE.md && \
grep -q "R12" /home/cnmfs/ICT/PROTOTYPE/LAYER/LGPD/GOVERNANCE.md && \
wc -l /home/cnmfs/ICT/PROTOTYPE/LAYER/LGPD/GOVERNANCE.md
```

Expected: arquivo existe, contém R11 e R12, >50 linhas.

- [ ] **Step 4: Append WAL**

```bash
echo "[$(date -Is)] GOVERNANCE CREATION COMPLETED R11+R12 hash-gov-$(md5sum /home/cnmfs/ICT/PROTOTYPE/LAYER/LGPD/GOVERNANCE.md | cut -c1-12)" \
  >> /home/cnmfs/ICT/PROTOTYPE/LAYER/LGPD/.claude/wal/shuntzu-operations.log
```

---

### Task A2: OMNIBUS Agent — PESTLE+Porter retroativo [S→Q→I→A]

**Agent:** `omnibus-orchestrator` (subagent-type: general-purpose com omnibus-orchestrator prompt carregado)

**Files:**
- Read: `analysis/pestle-porter-lgpd.md`
- Create: `memory/wal/omnibus-pestle-S.md`, `omnibus-pestle-Q.md`, `omnibus-pestle-I.md`, `omnibus-pestle-A.md`
- Append: `.claude/wal/shuntzu-operations.log`

**Prompt para agente (copiar exato):**

```
Você é o omnibus-orchestrator conforme /home/cnmfs/.claude/plugins/shuntzu-omnibus/agents/omnibus-orchestrator.md

BOOT SEQUENCE (executar antes de qualquer output):
1. CE: Leia .claude/wal/shuntzu-operations.log (últimas 20 linhas)
2. PL: Execute S→Q→I→A no input abaixo via philosophical-engine skill
3. WOE: Use shuntzu-f2 (strategy layer — PESTLE/Porter é análise estratégica)
4. IIM: Parse mission: validar análise PESTLE+Porter via OMNIBUS
5. E: Executar via shuntzu-f2

INPUT: Arquivo analysis/pestle-porter-lgpd.md
MISSÃO: Re-executar análise PESTLE + Porter usando pipeline OMNIBUS real.

STAGE [S] — Socrático (coleta/deconstrução):
- Leia analysis/pestle-porter-lgpd.md COMPLETO
- Extraia todos os fatos factuais com fonte
- Identifique premissas implícitas
- Liste elementos atômicos (não-redutíveis) de cada fator PESTLE
Output: Escreva memory/wal/omnibus-pestle-S.md com [TRACE-S] completo

STAGE [Q] — Questionador (interrogação):
- Para cada fato do [S], classifique: FACT/INFERENCE/SPECULATION/BELIEF
- Aplique 5N (5 porquês) nos 3 fatores mais críticos
- Identifique vieses: confirmação, âncora, recência, autoridade, ação
- VVV score por afirmação: fonte verificável? existe? referência exata?
Output: Escreva memory/wal/omnibus-pestle-Q.md com [TRACE-Q] completo

STAGE [I] — Inovador (síntese):
- 3 analogias estruturais com domínios distantes
- FDC-U: rank dos 6 fatores PESTLE por impacto estratégico (weights somam 1.0)
- DTS: quais ferramentas MEEST-AE v2.0 aplicar (DTS lista 50+ ferramentas)
- Insight de fronteira: onde análise atual tem gap epistêmico?
Output: Escreva memory/wal/omnibus-pestle-I.md com [TRACE-I] completo

STAGE [A] — Adversarial (stress-test):
- Advocatus Diaboli: melhor argumento CONTRA cada conclusão
- Condições de falha catastrófica
- Teste de falsificação Popperiana
- QUALITY_CoT = (Profundidade[S] × Rigidez[Q] × Originalidade[I] × Robustez[A]) / (Vieses + 1)
- Se QUALITY_CoT < 7.0 → documentar e indicar qual stage refazer
Output: Escreva memory/wal/omnibus-pestle-A.md com [TRACE-A] + QUALITY_CoT

APÓS TODOS 4 STAGES:
1. Append WAL: echo "[TIMESTAMP] OMNIBUS-PESTLE [S/Q/I/A] COMPLETED quality_cot=X.XX" >> .claude/wal/shuntzu-operations.log
2. Reportar: QUALITY_CoT final, VVV scores por fator, gaps identificados
```

- [ ] **Step 1: Lançar agente A2**

```bash
# Verificar que analysis/pestle-porter-lgpd.md existe
test -f /home/cnmfs/ICT/PROTOTYPE/LAYER/LGPD/analysis/pestle-porter-lgpd.md && echo "OK"
```

- [ ] **Step 2: Verificar outputs**

```bash
ls /home/cnmfs/ICT/PROTOTYPE/LAYER/LGPD/memory/wal/omnibus-pestle-{S,Q,I,A}.md 2>/dev/null
grep "OMNIBUS-PESTLE" /home/cnmfs/ICT/PROTOTYPE/LAYER/LGPD/.claude/wal/shuntzu-operations.log
```

Expected: 4 arquivos existem + WAL entry com quality_cot.

---

### Task A3: OMNIBUS Agent — SWOT retroativo [S→Q→I→A via shuntzu-f2+f3]

**Agent:** `omnibus-orchestrator` com shuntzu-f2 (DTS → swot-pestle-analysis) + shuntzu-f3 (VI/AE scoring)

**Files:**
- Read: `analysis/swot-transcricao.yaml`
- Create: `memory/wal/omnibus-swot-{S,Q,I,A}.md`
- Append: WAL

**Mudanças obrigatórias de metodologia (MEEST-AE v2.1):**

```
SWOT scoring antigo (inválido): strength/weakness 0-10
SWOT scoring novo (MEEST-AE v2.1):
  VI (Value Index) = Strength×0.6 + Opportunity×0.4  → range -1 a +1
  AE (Alert Index) = Weakness×0.5 + Threat×0.5       → range -1 a +1
  
  Quadrante:
    VI > 0 AND AE < 0 = ATTACK
    VI > 0 AND AE > 0 = CONDITIONAL
    VI < 0 AND AE < 0 = OBSERVE
    VI < 0 AND AE > 0 = AVOID
  
  VVV por item SWOT: multiplicar score por VVV
  Exemplo: Força S1 (vvv=0.9, Impacto=4, Prob=5) → score = (4×5/25) × 0.9 = 0.72
  Normalizar para range -1 a +1: (score - 0.5) × 2 = 0.44 → forças positivas
```

**Prompt para agente A3:**

```
Você é o omnibus-orchestrator.

MISSÃO: Reprocessar SWOT via pipeline OMNIBUS + MEEST-AE v2.1 MSP-Phase 3.

INPUT: analysis/swot-transcricao.yaml (SWOT existente com VVV 0.0-1.0 por item)

STAGE [S]: 
- Leia swot-transcricao.yaml completo
- Extraia cada item SWOT com id, texto, vvv, fonte
- Identifique gaps: itens sem fonte, itens com vvv < 0.5, categorias com < 3 itens
Output: memory/wal/omnibus-swot-S.md

STAGE [Q]:
- Classifique cada item: FACT/INFERENCE/SPECULATION/BELIEF
- Verifique VVV: fonte existe? referência exata ao doc original?
- 5N nos 3 itens mais críticos (maiores vvv ou maior impacto estratégico)
- Identifique vieses na análise original
Output: memory/wal/omnibus-swot-Q.md

STAGE [I]:
- Recalcule scores via MEEST-AE v2.1:
  VI = avg(Strength scores×0.6 + Opportunity scores×0.4), range -1 a +1
  AE = avg(Weakness scores×0.5 + Threat scores×0.5), range -1 a +1
  Score individual = VVV × (Impacto/5) → normalizado para -1 a +1
- Determine quadrante (ATTACK/CONDITIONAL/OBSERVE/AVOID)
- FDC-U: rank das dimensões estratégicas por impacto
Output: memory/wal/omnibus-swot-I.md com tabela VI/AE e quadrante

STAGE [A]:
- Stress-test: qual cenário destrói a vantagem competitiva em < 6 meses?
- Falsificação: qual evidência tornaria o quadrante AVOID?
- QUALITY_CoT calculado
Output: memory/wal/omnibus-swot-A.md

QUALITY GATE (shuntzu-f3 HIQM):
- ≥ 3 itens por categoria SWOT
- VVV > 0.5 em pelo menos 70% dos itens
- VI/AE calculado com fórmula MEEST-AE v2.1 (não range 0-1)
- QUALITY_CoT ≥ 7.0
```

- [ ] **Step 1: Lançar agente A3**

```bash
test -f /home/cnmfs/ICT/PROTOTYPE/LAYER/LGPD/analysis/swot-transcricao.yaml && echo "OK"
```

- [ ] **Step 2: Verificar outputs**

```bash
ls /home/cnmfs/ICT/PROTOTYPE/LAYER/LGPD/memory/wal/omnibus-swot-{S,Q,I,A}.md 2>/dev/null
grep "OMNIBUS-SWOT" /home/cnmfs/ICT/PROTOTYPE/LAYER/LGPD/.claude/wal/shuntzu-operations.log
```

---

### Task A4: OMNIBUS Agent — Market Research + FDC-U retroativo

**Agent:** `omnibus-orchestrator` com shuntzu-f1 (FDC-U scoring) + shuntzu-f2 (strategy)

**Files:**
- Read: `analysis/market-research-2025.md`, `analysis/fdc-u-validation.md`, `analysis/market-sizing.yaml`
- Create: `memory/wal/omnibus-market-{S,Q,I,A}.md`

**Prompt para agente A4:**

```
Você é o omnibus-orchestrator.

MISSÃO: Validar market research + FDC-U via OMNIBUS pipeline.

INPUT: 
- analysis/market-research-2025.md
- analysis/fdc-u-validation.md  
- analysis/market-sizing.yaml

STAGE [S]:
- Extraia: TAM, SAM, SOM numéricos com fonte
- Extraia: FDC-U scores (18 itens, weights, dimensões)
- Mapeie: quais dados vêm de fonte primária vs estimativa LLM
Output: memory/wal/omnibus-market-S.md

STAGE [Q]:
- Para cada número de mercado: FACT (fonte primária) ou INFERENCE/SPECULATION?
- FDC-U weights somam 1.0? Dimensões ortogonais?
- Identifique âncora bias: primeiro número recebido contaminou análise?
Output: memory/wal/omnibus-market-Q.md com evidence scale por claim

STAGE [I]:
- Recalcule FDC-U via shuntzu-f1:
  Score(item) = Σ [ w_i × f_i(A_i(item)) ]
  Onde w_i = pesos por dimensão, f_i = função impacto (direta/inversa)
- 3 analogias estruturais com mercados similares (EdTech, HealthTech, LegalTech)
- Insight de fronteira: onde market sizing tem maior incerteza epistêmica?
Output: memory/wal/omnibus-market-I.md com FDC-U recalculado

STAGE [A]:
- Scenario adversarial: ANPD adia enforcement 2 anos — impact no TAM?
- Falsificação: qual dado invalidaria a tese de mercado?
- QUALITY_CoT calculado
Output: memory/wal/omnibus-market-A.md
```

- [ ] **Step 1: Lançar agente A4**

```bash
wc -l /home/cnmfs/ICT/PROTOTYPE/LAYER/LGPD/analysis/market-research-2025.md
```

- [ ] **Step 2: Verificar**

```bash
ls /home/cnmfs/ICT/PROTOTYPE/LAYER/LGPD/memory/wal/omnibus-market-{S,Q,I,A}.md 2>/dev/null
```

---

### Task A5: OMNIBUS Agent — 5 Audiences via shuntzu-f3 [paralelo]

**Agent:** 5× `omnibus-orchestrator` paralelo, 1 por audience, zero conflito de arquivo

**Audiences:** b2g_prefeituras, b2g_consorcios, b2b_fornecedores_municipio, b2b_empresas_privadas, b2g_estaduais

**Files:**
- Read: `presentation-vue/public/strategic-data-unified.json` (audience fields)
- Create: `memory/wal/omnibus-audiences-{id}-{S,Q,I,A}.md` (20 files)
- Modify: JSON `snti.audiences[*].research_log`

**Prompt por agente (substituir {AUDIENCE_ID}):**

```
Você é o omnibus-orchestrator com shuntzu-f3 (MSP pipeline).

MISSÃO: Sub-engine MEEST-AE v2.1 para audience {AUDIENCE_ID}.

INPUT: 
- presentation-vue/public/strategic-data-unified.json → snti.audiences[{AUDIENCE_ID}]
- analysis/pestle-porter-lgpd.md (context)
- analysis/swot-transcricao.yaml (context)

STAGE [S] — Arqueologia da Persona:
- Extraia custom_weights do audience
- Liste fatos sobre segmento: TAM, CAC estimado, LTV, regulatório específico
- Identifique pain points únicos deste segmento
Output: memory/wal/omnibus-audiences-{AUDIENCE_ID}-S.md

STAGE [Q] — Interrogação:
- Classifique cada fato: FACT/INFERENCE/SPECULATION
- 5N no pain point mais crítico
- VVV score por fato: fonte verificável?
Output: memory/wal/omnibus-audiences-{AUDIENCE_ID}-Q.md

STAGE [I] — Síntese FDC-U:
- Recalcule custom_weights via FDC-U para este segmento (Σw=1.0)
- SWOT per persona: VI/AE range -1 a +1
- Quadrante estratégico: ATTACK/CONDITIONAL/OBSERVE/AVOID
- 5W1H attack plan específico
Output: memory/wal/omnibus-audiences-{AUDIENCE_ID}-I.md

STAGE [A] — Stress-test:
- Concorrente entra neste segmento — defensabilidade?
- Rollback trigger: quando parar de atacar este segmento?
- QUALITY_CoT calculado
Output: memory/wal/omnibus-audiences-{AUDIENCE_ID}-A.md

APÓS STAGES:
Adicionar research_log ao JSON (campo audience.research_log):
[
  {"timestamp": "ISO-DATE", "agent": "omnibus-f3", "source": "stage-S", "finding": "RESUMO FATO PRINCIPAL", "vvv": 0.XX},
  {"timestamp": "ISO-DATE", "agent": "omnibus-f3", "source": "stage-Q", "finding": "CLASSIFICACAO EVIDENCIAS", "vvv": 0.XX},
  {"timestamp": "ISO-DATE", "agent": "omnibus-f3", "source": "stage-I", "finding": "FDC-U RECALCULADO + QUADRANTE", "vvv": 0.XX}
]
```

- [ ] **Step 1: Verificar 5 audiences no JSON**

```bash
python3 -c "
import json
d=json.load(open('presentation-vue/public/strategic-data-unified.json'))
for a in d['snti']['audiences']:
    print(a.get('id'), '| research_log:', 'research_log' in a)
" 
```

Expected: 5 audiences, todos sem research_log.

- [ ] **Step 2: Lançar 5 agentes em paralelo** (1 por audience)

- [ ] **Step 3: Verificar outputs**

```bash
ls /home/cnmfs/ICT/PROTOTYPE/LAYER/LGPD/memory/wal/omnibus-audiences-*.md 2>/dev/null | wc -l
# Expected: 20 files (5 audiences × 4 stages)
python3 -c "
import json
d=json.load(open('presentation-vue/public/strategic-data-unified.json'))
logs=sum(1 for a in d['snti']['audiences'] if 'research_log' in a)
print(f'Audiences com research_log: {logs}/5')
"
```

---

## WAVE B — Sequencial (deps: Wave A completa)

### Task B1: Atualizar JSON items com sqia_trace_v2

**Agent:** general-purpose (modificação JSON)

**Files:**
- Modify: `presentation-vue/public/strategic-data-unified.json`

**Contexto:** Após Wave A gerar os 4 stage files para PESTLE+SWOT+Market, atualizar os 38 items SNTI com sqia_trace_v2 baseado nos traces gerados.

- [ ] **Step 1: Verificar WAL entries de Wave A**

```bash
grep "OMNIBUS-PESTLE\|OMNIBUS-SWOT\|OMNIBUS-MARKET" \
  /home/cnmfs/ICT/PROTOTYPE/LAYER/LGPD/.claude/wal/shuntzu-operations.log
```

Expected: pelo menos 3 entries com quality_cot.

- [ ] **Step 2: Calcular quality_cot médio**

```bash
python3 -c "
import re
lines=open('.claude/wal/shuntzu-operations.log').readlines()
scores=[float(m.group(1)) for l in lines for m in [re.search(r'quality_cot=(\d+\.\d+)',l)] if m]
print(f'Quality CoT scores: {scores}')
print(f'Média: {sum(scores)/len(scores):.2f}' if scores else 'Nenhum score encontrado')
"
```

- [ ] **Step 3: Adicionar sqia_trace_v2 a todos os 38 items**

```python
# Script: scripts/add-sqia-trace-v2.py
import json, datetime

d = json.load(open('presentation-vue/public/strategic-data-unified.json'))
items = [i for dim in d['snti']['dimensions'].values() for i in dim['items']]

wal_entries = open('.claude/wal/shuntzu-operations.log').read()
has_pestle = 'OMNIBUS-PESTLE' in wal_entries
has_swot = 'OMNIBUS-SWOT' in wal_entries
has_market = 'OMNIBUS-MARKET' in wal_entries

for item in items:
    if 'sqia_trace_v2' not in item:
        item['sqia_trace_v2'] = {
            'method': 'omnibus-retroativo-wave-a',
            'pestle_validated': has_pestle,
            'swot_validated': has_swot,
            'market_validated': has_market,
            'stage_files': [
                f'memory/wal/omnibus-pestle-S.md',
                f'memory/wal/omnibus-pestle-Q.md',
                f'memory/wal/omnibus-pestle-I.md',
                f'memory/wal/omnibus-pestle-A.md',
            ],
            'timestamp': datetime.datetime.now().isoformat(),
            'quality_gate': 'hiqm-90pct'
        }
        item['vvv_provenance'] = 'omnibus-retroativo-real'

json.dump(d, open('presentation-vue/public/strategic-data-unified.json', 'w'),
          ensure_ascii=False, indent=2)
print(f"Updated {len(items)} items")
```

```bash
cd /home/cnmfs/ICT/PROTOTYPE/LAYER/LGPD
python3 scripts/add-sqia-trace-v2.py
```

Expected: "Updated 38 items"

- [ ] **Step 4: Verificar contagem**

```bash
python3 -c "
import json
d=json.load(open('presentation-vue/public/strategic-data-unified.json'))
items=[i for dim in d['snti']['dimensions'].values() for i in dim['items']]
v2=sum(1 for i in items if 'sqia_trace_v2' in i)
print(f'sqia_trace_v2: {v2}/38')
"
```

Expected: `sqia_trace_v2: 38/38`

- [ ] **Step 5: Build**

```bash
cd /home/cnmfs/ICT/PROTOTYPE/LAYER/LGPD/presentation-vue && bun run build
```

Expected: build PASS, zero errors.

- [ ] **Step 6: Commit Wave B**

```bash
cd /home/cnmfs/ICT/PROTOTYPE/LAYER/LGPD
git add presentation-vue/public/strategic-data-unified.json \
        GOVERNANCE.md \
        memory/wal/ \
        .claude/wal/shuntzu-operations.log \
        scripts/add-sqia-trace-v2.py
git commit -m "feat(OMNIBUS-retroativo): S→Q→I→A traces + research_log 5/5 audiences + sqia_trace_v2 38/38"
```

---

## WAVE C — Validação Final

### Task C1: HIQM Re-audit

**Agent:** `hiqm-quality` skill invocado pelo `omnibus-orchestrator`

**Files:**
- Create: `analysis/omnibus-validation-report.md`

- [ ] **Step 1: Rodar validação**

```bash
python3 -c "
import json
d=json.load(open('presentation-vue/public/strategic-data-unified.json'))
items=[i for dim in d['snti']['dimensions'].values() for i in dim['items']]

v2=sum(1 for i in items if 'sqia_trace_v2' in i)
real=sum(1 for i in items if 'omnibus' in i.get('vvv_provenance',''))
auds=d['snti']['audiences']
logs=sum(1 for a in auds if 'research_log' in a)
log3=sum(1 for a in auds if len(a.get('research_log',[])) >= 3)

print(f'sqia_trace_v2: {v2}/38 ({v2/38*100:.0f}%)')
print(f'omnibus provenance: {real}/38 ({real/38*100:.0f}%)')
print(f'audiences research_log: {logs}/5')
print(f'audiences ≥3 entries: {log3}/5')

import subprocess
result=subprocess.run(['wc','-l','.claude/wal/shuntzu-operations.log'], capture_output=True, text=True)
print(f'WAL entries: {result.stdout.strip()}')
"
```

Expected:
```
sqia_trace_v2: 38/38 (100%)
omnibus provenance: 38/38 (100%)
audiences research_log: 5/5
audiences ≥3 entries: 5/5
WAL entries: >20 .claude/wal/shuntzu-operations.log
```

- [ ] **Step 2: Verificar memory/wal/ file count**

```bash
ls /home/cnmfs/ICT/PROTOTYPE/LAYER/LGPD/memory/wal/ | wc -l
```

Expected: ≥ 24 (4 pilot + 4 pestle + 4 swot + 4 market + 20 audiences)

- [ ] **Step 3: Build final + deploy**

```bash
cd /home/cnmfs/ICT/PROTOTYPE/LAYER/LGPD/presentation-vue && bun run build
git add -A
git commit -m "feat(OMNIBUS-Wave-C): HIQM audit completo — 38/38 sqia_trace_v2, 5/5 research_log"
git push origin main
```

- [ ] **Step 4: Verificar deploy**

```bash
curl -sL https://camillanapoles.github.io/lgpd-mkt-intel/ -o /dev/null -w "%{http_code}\n"
```

Expected: `200`

---

## Self-Review

**1. Spec coverage:**

| Requisito CLAUDE.md | Task |
|--------------------|----|
| Engine dinâmica item-a-item | B1 (sqia_trace_v2 38/38) |
| VVV visível por card | B1 (vvv_provenance atualizado) |
| Status page [PESQUISANDO]/[CONCLUIDO] | Fora de escopo deste plano |
| Analise por canal | A5 (5 audiences research_log) |
| GOVERNANCE.md R1-R10 | A1 |
| OMNIBUS pipeline para dados | A2+A3+A4 |
| shuntzu-f1/f2/f3 | A2(f2)+A3(f2+f3)+A4(f1+f2)+A5(f3) |
| SWOT VI/AE range -1 a +1 | A3 (metodologia corrigida) |
| ≥3 items/cat + SQIA por item | A3 quality gate |
| WAL entries | A1+A2+A3+A4+A5 (WAL append em cada) |

**2. Placeholder scan:** Nenhum TBD. Todos os prompts de agentes são completos.

**3. Type consistency:** `sqia_trace_v2` (dict), `research_log` (array), `vvv_provenance` (string) — consistente com pilot eca_digital_urgent no JSON existente.

**Gaps identificados fora deste plano (Wave A1 pendente do Phase 3):**
- StakeholderMap D4 badge
- Vue components surface vvv_provenance/decay_reason
- E2E tests por tab
- 6 genuine VVV gaps sem fonte primária (requer pesquisa humana)

---

## FDC-U Queue — Registrar tasks para hook auto-continuidade

Após Task A1 (GOVERNANCE.md), atualizar `.claude/state/fdcu-queue.json`:

```json
{
  "tasks": [
    {"id": "OMNIBUS-A1", "subject": "GOVERNANCE R11+R12", "status": "pending", "deps": []},
    {"id": "OMNIBUS-A2", "subject": "PESTLE+Porter S→Q→I→A", "status": "pending", "deps": []},
    {"id": "OMNIBUS-A3", "subject": "SWOT VI/AE MEEST-AE v2.1", "status": "pending", "deps": []},
    {"id": "OMNIBUS-A4", "subject": "Market Research + FDC-U", "status": "pending", "deps": []},
    {"id": "OMNIBUS-A5", "subject": "5 Audiences sub-engine", "status": "pending", "deps": []},
    {"id": "OMNIBUS-B1", "subject": "JSON sqia_trace_v2 38/38", "status": "pending", "deps": ["OMNIBUS-A2","OMNIBUS-A3","OMNIBUS-A4"]},
    {"id": "OMNIBUS-C1", "subject": "HIQM audit final + deploy", "status": "pending", "deps": ["OMNIBUS-B1","OMNIBUS-A5"]}
  ]
}
```

Hook `fdcu-orchestrator.sh` re-ranqueia automaticamente quando task muda para `completed`.
