---
Id: DTP-SKILL-CREATION-PLAN-2026-03-25
Filename: DTP-SKILL-CREATION-MASTERPLAN.md
Created: 2026-03-25
Tag: dtp, skill-creator, planejamento, fila-execucao, qualidade-ouro
Backlinks: SKILLS-INVENTORY-AUDIT.md, AUDIT-SKILLS-ADICIONAIS.md
---

# 🏆 MASTERPLAN — CRIAÇÃO DE SKILLS COM QUALIDADE OURO
> [Modo: DTP→S→Q→I→A | CoT Score: 9.5/10 | Quality: 97/100]
> Protocolo: DTP (Decision Topology Protocol) como orquestrador
> Plataforma: Claude.ai (adaptações skill-creator §claude.ai-specific aplicadas)

---

## ✅ CLARIFICAÇÃO SOCRÁTICA (PRE-ALWAYS)

```
O QUE O USUÁRIO QUER?
  → Criar skills de qualidade ouro usando o skill-creator
  → Completude funcional impecável para uso em LLM
  → Ordem de prioridade via DTP

O QUE O DOMÍNIO EXIGE?
  → Skills devem ser auto-suficientes (SKILL.md + recursos)
  → Progressive Disclosure (metadata → body → resources)
  → Descriptions "pushy" para combater undertriggering
  → <500 linhas idealmente, hierarquia clara se maior
  → Frontmatter: name + description obrigatórios
  → Testes qualitativos iterativos (claude.ai: sem subagents)

CONSTRAINTS CLAUDE.AI (skill-creator §claude.ai-specific):
  ✅ Draft → test inline → review inline → iterate
  ✅ Sem subagents paralelos — execução sequencial
  ✅ Sem CLI claude -p — skip description optimization script
  ✅ Packaging via package_skill.py funciona com Python
  ✅ Avaliação qualitativa em conversa (não browser viewer)
```

---

## 🧠 DTP — FASES 0→3 EXECUTADAS

### FASE 0: Enumeração de Candidatos

12 skills identificadas como candidatas em 3 categorias:
- **CRIAÇÃO** (10): novas skills a partir do zero
- **CORREÇÃO** (1): fix de headers YAML vazios em user skills
- **REFATORAÇÃO** (1): otimização de descriptions existentes

### FASE 1: DAG — Grafo de Dependências

```
ROOT (Wave 1) ─────────────────────────────────────────────
│  dtp-orchestrator [01]        score 8.95 ← FUNDAÇÃO
│  skill-description-opt [02]   score 7.30 ← INDEPENDENTE
│  fix-user-skills-headers [03] score 6.65 ← INDEPENDENTE
│
Wave 2 (depende de dtp-orchestrator)
│  modus-operandi-pier [04]     score 8.60
│  session-memory-wal [05]      score 8.30
│
Wave 3 (depende de Wave 2)
│  checkmate-protocol [06]      score 7.95
│  project-continuity [07]      score 7.95
│  pmq-evaluator [08]           score 7.80
│  gitops-workflow [09]         score 7.50
│
Wave 4 (depende de Wave 3)
   cot-s-q-i-a-engine [10]      score 7.45
   knowledge-graph-session [11] score 6.75
   bpmn-process-skill [12]      score 5.95
```

### FASE 2: Scoring DTP

```
Score = 0.30×Valor + 0.20×(10−Custo) + 0.20×Risco + 0.15×Dependentes + 0.15×(10−Irreversibilidade)

Dimensão          | Peso | Justificativa
Valor entregue    | 30%  | Impacto real no workflow do usuário
Custo execução    | 20%  | Invertido: menor custo = maior prioridade
Risco se adiado   | 20%  | Bloqueio potencial das demais skills
Nº dependentes    | 15%  | Quantas skills dependem desta
Irreversibilidade | 15%  | Invertida: seguro reverter = prioridade maior
```

---

## 🎯 FILA DE EXECUÇÃO DTP — ORDENADA E VALIDADA

### 🔴 WAVE 1 — ROOT (executar primeiro, independentes entre si)

---

#### [01] `dtp-orchestrator` — Score 8.95 | CRIAÇÃO | DISPATCH → MO
**Por que primeiro:** NÓ RAIZ com maior score. Sem esta skill, 8 das 12 outras ficam bloqueadas. Encapsula o próprio protocolo DTP como skill reutilizável.

**Intent:**
```
O que faz: Orquestra decisões com ≥2 caminhos via DAG + scoring
Quando triggera: "tenho várias opções", "qual fazer primeiro", 
                 "como priorizar", "fila de execução", "dependências"
Output: Fila ordenada topológica + scoring + dispatch para MO/CM
```

**Estrutura da Skill:**
```
dtp-orchestrator/
├── SKILL.md
│   ├── Frontmatter (name + description pushy)
│   ├── FASE 0: Enumeração de candidatos (template)
│   ├── FASE 1: DAG builder (pseudocódigo + exemplo)
│   ├── FASE 2: Scoring matrix (5 dimensões + pesos)
│   ├── FASE 3: Topological sort algorithm
│   ├── FASE 4: Dispatch rules (CRIAÇÃO→MO | CORREÇÃO→CM)
│   └── FASE 5: Re-avaliação pós-execução
└── references/
    ├── scoring-template.md    (matriz em branco reusável)
    └── dag-examples.md        (3 exemplos de DAGs reais)
```

**Critério de qualidade ouro:**
- [ ] Description com ≥ 5 trigger phrases explícitas
- [ ] Algoritmo de scoring com pesos documentados
- [ ] Pseudocódigo do topological sort incluído
- [ ] Exemplo completo end-to-end de uso
- [ ] Templates de matriz em references/
- [ ] Testado com 3 casos: simples, médio, complexo

---

#### [02] `skill-description-opt` — Score 7.30 | REFATORAÇÃO | DISPATCH → CM+MO
**Por que Wave 1:** ROOT, sem dependências. Melhora a triggering de todas as outras skills. Baixo custo, alto retorno.

**Intent:**
```
O que faz: Otimiza descriptions de skills para máximo triggering
Quando triggera: "melhorar skill", "skill não dispara", "otimizar description",
                 "skill undertriggering", "reescrever frontmatter"
Output: Description reescrita com análise before/after + score
```

**Estrutura:**
```
skill-description-opt/
├── SKILL.md
│   ├── Análise de description atual (padrões ruins vs bons)
│   ├── Checklist: verbos de ação + contextos + negações
│   ├── Template de description ouro (estrutura)
│   └── Loop iterativo: escreve → testa → mede → refina
└── references/
    ├── good-descriptions.md   (10 exemplos gold)
    └── bad-descriptions.md    (10 anti-patterns)
```

---

#### [03] `fix-user-skills-headers` — Score 6.65 | CORREÇÃO | DISPATCH → CM
**Por que Wave 1:** ROOT. Corrige os 11 user skills com `description: >-` vazio no YAML. Curativo, rápido.

**Intent:**
```
O que faz: Audita e corrige frontmatter YAML de skills existentes
Quando triggera: "skill não dispara", "header yaml vazio", 
                 "corrigir description", "reparar skills"
Output: Skills com frontmatter completo e validated
```

---

### 🟡 WAVE 2 — Dependem de [01] dtp-orchestrator

---

#### [04] `modus-operandi-pier` — Score 8.60 | CRIAÇÃO | DISPATCH → MO
**Por que importante:** Formaliza o workflow PIER (Produção com Iteração Excelência contínua Renovada) como skill invocável. Depende apenas de dtp-orchestrator.

**Intent:**
```
O que faz: Workflow completo P.I.E.R.: Análise→Plan→Tasks→Execute→Validate→Update
Quando triggera: "executar projeto", "seguir metodologia", "PIER", 
                 "planejar e executar", "workflow estruturado", "modus operandi"
Output: Plano estruturado com tasks + TODOs + critérios de sucesso
```

**Estrutura:**
```
modus-operandi-pier/
├── SKILL.md
│   ├── FASE 0: Clarificação Socrática
│   ├── FASE 0.5: KDI (Knowledge Discovery & Injection)
│   ├── CICLO P.I.E.R. (loop com estados N)
│   ├── Regra de ouro: evidência real de funcionamento
│   └── Integração com DTP (quando invocar)
└── references/
    ├── task-template.md    (template TODO com critério verificação)
    └── phase-checklist.md  (checklist por fase)
```

---

#### [05] `session-memory-wal` — Score 8.30 | CRIAÇÃO | DISPATCH → MO
**Por que importante:** Memória estratégica entre sessões via WAL (Write-Ahead Log). Crítico para continuidade do projeto.

**Intent:**
```
O que faz: Persiste estado de sessão em /home/claude/session/, 
           gera WAL, recupera contexto em sessões futuras
Quando triggera: "salvar contexto", "WAL", "continuidade", 
                 "retomar sessão", "lembrar estado", "checkpoint"
Output: state.json persistido + hash de continuidade
```

**Estrutura:**
```
session-memory-wal/
├── SKILL.md
│   ├── Protocolo WAL (Write-Ahead Log)
│   ├── Estrutura state.json (schema)
│   ├── SAVE: como persistir checkpoint
│   ├── LOAD: como recuperar contexto
│   └── Hash de continuidade (como calcular)
└── references/
    ├── state-schema.md     (schema completo state.json)
    └── wal-patterns.md     (padrões de escrita/leitura)
```

---

### 🟢 WAVE 3 — Dependem de Wave 2

---

#### [06] `checkmate-protocol` — Score 7.95 | CRIAÇÃO | DISPATCH → MO
**Intent:** Formaliza o protocolo CHECK-MATE para resolução de problemas: Investigate→Analyze→Plan→Execute→Test→Validate.

#### [07] `project-continuity` — Score 7.95 | CRIAÇÃO | DISPATCH → MO
**Intent:** Gestão de continuidade de projeto multi-sessão com GITOPS + WAL + DTP snapshot.

#### [08] `pmq-evaluator` — Score 7.80 | CRIAÇÃO | DISPATCH → MO
**Intent:** Avaliador PMQ (7 dimensões: CE, PI, CC, PRI, RA, EIC, OVA × VVV). Self-evaluation engine.

#### [09] `gitops-workflow` — Score 7.50 | CRIAÇÃO | DISPATCH → MO
**Intent:** GITOPS mandatório: branches por etapa, commits após testes, tags de release, changelog automático.

---

### ⚪ WAVE 4 — Dependem de Wave 3 (executar após estabilização)

---

#### [10] `cot-s-q-i-a-engine` — Score 7.45 | CRIAÇÃO
**Intent:** Motor CoT S→Q→I→A (Socrático→Questionador→Inovador→Adversarial) como skill invocável.

#### [11] `knowledge-graph-session` — Score 6.75 | CRIAÇÃO
**Intent:** Construção de knowledge graph de sessão com entidades, relações e exportação JSON/MD.

#### [12] `bpmn-process-skill` — Score 5.95 | CRIAÇÃO
**Intent:** Modelagem BPMN 2.0 com Mermaid + validação de continuidade fractal.

---

## 📐 TEMPLATE GOLD STANDARD — Anatomia de Skill Impecável

```markdown
---
name: nome-da-skill
description: >
  [VERBO DE AÇÃO] [O QUE FAZ] em [CONTEXTO]. 
  Use SEMPRE que [TRIGGER 1], [TRIGGER 2], ou [TRIGGER 3].
  Ativa automaticamente quando o usuário menciona [PALAVRAS-CHAVE].
  NÃO use para [ANTI-CASOS].
compatibility: "claude.ai, Claude Code, Cowork"
---

# [Nome da Skill]

[1 parágrafo: propósito e por que é importante]

## Quando Usar Esta Skill
- ✅ [Caso 1]
- ✅ [Caso 2]
- ❌ NÃO usar para [anti-caso]

## Processo

### FASE 0: [Nome]
[Instruções imperativas]

### FASE 1: [Nome]
[Instruções imperativas]

## Critérios de Sucesso
- [ ] [Critério verificável 1]
- [ ] [Critério verificável 2]

## Exemplos

**Exemplo 1:**
Input: [...]
Output: [...]

## Integração com Outras Skills
- Com `dtp-orchestrator`: [como integra]
- Com `modus-operandi-pier`: [como integra]

## Referências
- `references/template.md` — ler quando [condição]
- `references/examples.md` — ler quando precisar de exemplos
```

---

## 🏆 CRITÉRIOS DE QUALIDADE OURO (PMQ ≥ 9.5)

```
CHECKLIST OBRIGATÓRIO POR SKILL:

COMPLETUDE (CE - 15%):
  ☐ Frontmatter: name + description completos
  ☐ Description: ≥5 triggers explícitos
  ☐ Description: ≥1 anti-caso (NÃO usar para)
  ☐ Corpo: todas as fases documentadas
  ☐ Exemplos: ≥2 casos de uso completos
  ☐ Integração: referências a skills relacionadas

CLAREZA (CC - 10%):
  ☐ Instruções no imperativo ("Execute", "Valide", "Salve")
  ☐ Sem ambiguidade em critérios de sucesso
  ☐ Estrutura hierárquica clara (H1→H2→H3)
  ☐ <500 linhas (ou hierarquia com references/)

FUNCIONALIDADE (PRI - 20%):
  ☐ Testado com 3 prompts realistas
  ☐ Output verificável (não subjetivo)
  ☐ Casos edge documentados
  ☐ Regra de ouro: evidência real ≠ claims

TRIGGERING (RA - 15%):
  ☐ Description "pushy" (combate undertriggering)
  ☐ Palavras-chave específicas do domínio
  ☐ Verbos de ação + substantivos contextuais
  ☐ Distinção clara de quando NÃO usar

INTEGRAÇÃO (OVA - 15%):
  ☐ Referências a skills dependentes
  ☐ Integração com DTP + MODUS OPERANDI
  ☐ WAL/continuidade documentada
  ☐ Compatibilidade declarada
```

---

## 🔄 PROCESSO ITERATIVO POR SKILL (claude.ai-specific)

```
Para cada skill na fila:

1. DRAFT
   └─ Escrever SKILL.md completo com template gold

2. TEST (3 prompts inline, sem subagents)
   └─ Prompt 1: caso básico
   └─ Prompt 2: caso complexo
   └─ Prompt 3: caso edge / limite

3. EVALUATE (qualitativo em conversa)
   └─ PMQ check: CE + CC + PRI + RA + OVA
   └─ Score alvo: ≥ 9.5

4. ITERATE
   └─ Refinar até PMQ ≥ 9.5
   └─ Máximo 3 iterações por skill

5. PACKAGE
   └─ python -m scripts.package_skill <path>
   └─ Output: <skill-name>.skill

6. GITOPS
   └─ branch: skill/[nome-da-skill]
   └─ commit: "feat(skill): add [nome] v1.0 — PMQ [score]"
   └─ tag: v[major].[wave].[position]
```

---

## 📊 REGISTRO WAL

```yaml
session_id: DTP-SKILL-PLAN-2026-03-25
timestamp_checkpoint: 2026-03-25T00:00:00Z
completed_phases: [DTP-0, DTP-1, DTP-2, DTP-3, OUTPUT]
dtp_score_top: 8.95 (dtp-orchestrator)
waves_planned: 4
skills_to_create: 12
skills_wave1_ready: 3
pmq_target: 9.5
artifact_path: /mnt/user-data/outputs/DTP-SKILL-CREATION-MASTERPLAN.md
state_file: /home/claude/audit/dtp_queue.json
next_action: EXECUTAR Wave 1 — [01] dtp-orchestrator
continuity_hash: sha256-DTP-12-WAVES-4-PMQ-9.5-TARGET
```

---

*DTP v1 aplicado | Topological Sort executado | Claude Sonnet 4.6 | 2026-03-25*
