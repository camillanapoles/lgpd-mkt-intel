---
Id: SKILL-CREATION-BLUEPRINT-v1.0
Filename: SKILL-CREATION-BLUEPRINT.md
Created: 2026-03-26
Tag: blueprint, bpmn, skills, agentskills, knowledge-graph, processo, fractal
Backlinks: DTP-SKILL-CREATION-MASTERPLAN.md, agentskills.io/specification
Skills-Aplicadas: engenheiro-processos-master, graphrag-universal
---

# 🏗️ BLUEPRINT — CRIAÇÃO DE SKILLS (AgentSkills Format)
> [Modo: DTP→S→Q→I→A | Engenheiro-Processos-Master + GraphRAG-Universal]  
> Base epistêmica: agentskills.io (specification + best-practices) + DTP-MASTERPLAN  
> Decomposição fractal: N1 Cadeia de Valor → N2 Processo → N3 Subprocesso

---

## PARTE I — KNOWLEDGE GRAPH (GraphRAG-Universal)
> Entidades e relações extraídas da base indexada

### Mapa de Entidades

```
ENTIDADES CORE (GraphRAG)
══════════════════════════════════════════════════════════

[ Skill ]──────HAS_COMPONENT──────► [ SKILL.md ]
[ Skill ]──────HAS_COMPONENT──────► [ scripts/ ]
[ Skill ]──────HAS_COMPONENT──────► [ references/ ]
[ Skill ]──────HAS_COMPONENT──────► [ assets/ ]
[ Skill ]──────HAS_COMPONENT──────► [ evals/ ]

[ SKILL.md ]───HAS_PHASE──────────► [ Frontmatter ]
[ SKILL.md ]───HAS_PHASE──────────► [ Body ]
[ Frontmatter ]─HAS_COMPONENT─────► [ name ]          ← max 64 chars, kebab-case
[ Frontmatter ]─HAS_COMPONENT─────► [ description ]   ← max 1024 chars, 3ª pessoa
[ Body ]────────HAS_PHASE─────────► [ When-to-Use ]
[ Body ]────────HAS_PHASE─────────► [ Process ]
[ Body ]────────HAS_PHASE─────────► [ Examples ]
[ Body ]────────HAS_PHASE─────────► [ Gotchas ]
[ Body ]────────HAS_PHASE─────────► [ Integration ]

[ description ]─TRIGGERS──────────► [ Agent Discovery ]
[ Agent Discovery ]─PRECEDES───────► [ Agent Activation ]
[ Agent Activation ]─PRECEDES──────► [ Agent Execution ]

[ Skill ]──────VALIDATED_BY────────► [ Eval Set ]
[ Eval Set ]───HAS_PHASE──────────► [ Train Set ]     ← 60% queries
[ Eval Set ]───HAS_PHASE──────────► [ Validation Set ]← 40% queries
[ Eval Set ]───MEASURED_BY─────────► [ Trigger Rate ] ← threshold 0.5

[ Skill ]──────OPTIMIZED_BY────────► [ Description Loop ]
[ Description Loop ]─APPLIES───────► [ Broaden if narrow ]
[ Description Loop ]─APPLIES───────► [ Narrow if broad ]
[ Description Loop ]─PRODUCES──────► [ PMQ Score ]

[ Skill ]──────PACKAGED_BY─────────► [ package_skill.py ]
[ Skill ]──────VALIDATES_WITH──────► [ skills-ref validate ]
```

### Grafo de Relacionamentos por Camadas

```
PROGRESSIVE DISCLOSURE (3 Tiers)
══════════════════════════════════════════════════════════

TIER 1 — Startup (~50-100 tokens/skill)
         [ name ] + [ description ]
                    ↓
         Agent carrega em session start
         Agent DECIDE: Relevante? → SIM/NÃO

TIER 2 — Activation (<5000 tokens)
         [ SKILL.md body ]
                    ↓
         Carregado quando task matches description
         Agent lê instruções completas

TIER 3 — On-Demand (variável)
         [ scripts/ ] [ references/ ] [ assets/ ]
                    ↓
         Carregados quando instruções referenciam
         Menor uso de contexto agregado

RELAÇÕES CRÍTICAS:
  undertriggering ←─── description muito NARROW
  false-triggering ←── description muito BROAD
  overfitting ←─────── otimizar contra ALL queries (sem split train/val)
  soundness ────────── SKILL.md < 500 linhas (contexto público)
```

---

## PARTE II — DECOMPOSIÇÃO FRACTAL (Engenheiro-Processos-Master)

### N1 — CADEIA DE VALOR: Skill Factory

```
╔══════════════════════════════════════════════════════════════════╗
║                   SKILL FACTORY — CADEIA DE VALOR                ║
╠══════════════╦═══════════════════╦══════════════════════════════╗
║              ║                   ║                              ║
║  [CONCEBER]  ║    [CONSTRUIR]    ║       [VALIDAR & PUBLICAR]   ║
║              ║                   ║                              ║
║ 1. Ideia     ║ 3. Estrutura      ║ 6. Eval Trigger Rate         ║
║ 2. DTP Score ║ 4. Frontmatter    ║ 7. Eval Output Quality       ║
║              ║ 5. Body + Extras  ║ 8. GitOps + Package          ║
╚══════════════╩═══════════════════╩══════════════════════════════╝
       ↑                                           ↓
       └─────────────── KAIZEN LOOP ───────────────┘
                  PMQ < 9.5 → REFINAR
```

---

### N2 — PROCESSO: Criação de Skill (BPMN Pool Principal)

```bpmn
┌──────────────────────────────────────────────────────────────────────────────┐
│ POOL: SKILL AUTHOR                                                           │
├──────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  (START)                                                                     │
│    │                                                                         │
│    ▼                                                                         │
│  [FASE 0: Clarificação Socrática]                                           │
│    │  "O que essa skill faz?"                                                │
│    │  "Quando deve ativar?"                                                  │
│    │  "O que NÃO deve ativar?"                                               │
│    │                                                                         │
│    ▼                                                                         │
│  [FASE 1: DTP Scoring]                                                       │
│    │  Score = f(Valor, Custo, Risco, Dependentes, Irreversibilidade)         │
│    │                                                                         │
│    ▼                                                                         │
│  <Gateway: Score ≥ threshold?>                                               │
│    │ NÃO ─────────────────────────────────────────────► [Descartar/Adiar]   │
│    │ SIM                                                                     │
│    ▼                                                                         │
│  [FASE 2: Criar Estrutura de Diretório]                                      │
│    │  skill-name/                                                            │
│    │  ├── SKILL.md                                                           │
│    │  ├── scripts/   (se necessário)                                         │
│    │  ├── references/(se necessário)                                         │
│    │  ├── assets/    (se necessário)                                         │
│    │  └── evals/     (queries de teste)                                      │
│    │                                                                         │
│    ▼                                                                         │
│  [FASE 3: Escrever Frontmatter]  ─────────► Sub-Processo SP1                │
│    │  name + description                                                     │
│    │                                                                         │
│    ▼                                                                         │
│  [FASE 4: Escrever Body SKILL.md] ─────────► Sub-Processo SP2               │
│    │  <500 linhas                                                            │
│    │                                                                         │
│    ▼                                                                         │
│  [FASE 5: Criar Eval Set]  ─────────────────► Sub-Processo SP3              │
│    │  20 queries (60% train / 40% val)                                       │
│    │                                                                         │
│    ▼                                                                         │
│  [FASE 6: Testar Trigger Rate]                                               │
│    │  Rodar cada query × 3 runs                                              │
│    │  Trigger Rate = triggers / runs                                         │
│    │                                                                         │
│    ▼                                                                         │
│  <Gateway: Trigger Rate OK?> ─────────────────► Sub-Processo SP4            │
│    │ NÃO ───────────────────────────────────────► [Otimizar Description]    │
│    │ SIM                                                                     │
│    ▼                                                                         │
│  [FASE 7: Testar Output Quality]                                             │
│    │  With-Skill vs Without-Skill                                            │
│    │                                                                         │
│    ▼                                                                         │
│  <Gateway: PMQ ≥ 9.5?>                                                       │
│    │ NÃO ───────────────────────────────────────► [Refinar SKILL.md Body]   │
│    │ SIM                                                                     │
│    ▼                                                                         │
│  [FASE 8: Validar + Packager]                                                │
│    │  skills-ref validate ./skill-name                                       │
│    │  python -m scripts.package_skill <path>                                 │
│    │                                                                         │
│    ▼                                                                         │
│  [FASE 9: GitOps]                                                            │
│    │  branch: skill/[nome]                                                   │
│    │  commit: "feat(skill): add [nome] v1.0 — PMQ [score]"                  │
│    │  tag: v[major].[wave].[position]                                        │
│    │                                                                         │
│    ▼                                                                         │
│  (END ✅)                                                                    │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

### N3 — SUBPROCESSOS (Detalhamento Atômico)

#### SP1 — Escrever Frontmatter (Description Engineering)

```bpmn
┌──────────────────────────────────────────────────────────────────┐
│ SUBPROCESSO SP1: FRONTMATTER                                     │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  (START)                                                         │
│    │                                                             │
│    ▼                                                             │
│  [T1] Definir name]                                              │
│    │  • lowercase + hyphens only                                 │
│    │  • max 64 chars                                             │
│    │  • gerund form recomendado (processing-pdfs)                │
│    │  • sem: "anthropic", "claude", generics (helper, utils)     │
│    │                                                             │
│    ▼                                                             │
│  [T2] Rascunhar description v0]                                  │
│    │  Template: "[VERBO IMPERATIVO] [O QUE FAZ] em [CONTEXTO].   │
│    │  Use SEMPRE que [TRIGGER 1], [TRIGGER 2], [TRIGGER 3].      │
│    │  NÃO usar para [ANTI-CASO]."                                │
│    │                                                             │
│    ▼                                                             │
│  [T3] Aplicar Checklist Description Gold]                        │
│    │  ☐ 3ª pessoa (não "I can help you...")                       │
│    │  ☐ ≥5 trigger phrases explícitas                            │
│    │  ☐ ≥1 anti-caso (NÃO usar para)                             │
│    │  ☐ Verbos imperativos (Use, Activate, Apply)                │
│    │  ☐ Pushy: "mesmo que usuário não mencione X"                │
│    │  ☐ < 1024 chars (hard limit)                                │
│    │                                                             │
│    ▼                                                             │
│  <Gateway: Checklist OK?>                                        │
│    │ NÃO ──────────────────────────────► [Reescrever description]│
│    │ SIM                                                         │
│    ▼                                                             │
│  (END SP1 → próximo: SP2)                                        │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘

REGRAS DESCRIPTION:
  ✅  "Analyze CSV and tabular data — compute summary statistics,
       add derived columns, generate charts. Use when the user has
       a CSV, TSV, or Excel file, even if they don't explicitly
       mention 'CSV' or 'analysis'."

  ❌  "Process CSV files."           ← muito narrow
  ❌  "Help with data."              ← muito broad + genérico
  ❌  "I can analyze your CSV data." ← 1ª pessoa (inválido)
```

#### SP2 — Escrever Body SKILL.md (Anatomia Gold Standard)

```bpmn
┌──────────────────────────────────────────────────────────────────┐
│ SUBPROCESSO SP2: BODY SKILL.md                                   │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  (START)                                                         │
│    │                                                             │
│    ▼                                                             │
│  [T1] Seção: When to Use (ativação)                             │
│    │  • ✅ casos de uso diretos                                   │
│    │  • ❌ anti-casos explícitos                                  │
│    │                                                             │
│    ▼                                                             │
│  [T2] Seção: Core Concepts]                                     │
│    │  • Apenas o que Claude NÃO sabe nativamente                 │
│    │  • Cada parágrafo: "justifica seus tokens?"                 │
│    │                                                             │
│    ▼                                                             │
│  [T3] Seção: Processo / Fases]                                  │
│    │  • IMPERATIVO ("Execute", "Valide", "Salve")                │
│    │  • Freedom calibrado:                                       │
│    │    HIGH: várias abordagens válidas                          │
│    │    MED:  padrão preferido com variações                     │
│    │    LOW:  sequência exata (operações frágeis)                │
│    │                                                             │
│    ▼                                                             │
│  [T4] Seção: Exemplos (≥2)]                                     │
│    │  • Input → Output pairs                                     │
│    │  • Edge cases incluídos                                     │
│    │                                                             │
│    ▼                                                             │
│  [T5] Seção: Gotchas (Alta Prioridade!)]                        │
│    │  • Falhas experience-derived                                │
│    │  • Formato: "1. Título: O que vai errado + como prevenir"   │
│    │                                                             │
│    ▼                                                             │
│  [T6] Seção: Integration]                                       │
│    │  • Referências a skills relacionadas (plain text, sem links)│
│    │                                                             │
│    ▼                                                             │
│  [T7] Mover conteúdo longo → references/]                       │
│    │  • Se SKILL.md > 500 linhas → extrair para references/     │
│    │  • Usar relative paths: ./references/file.md               │
│    │  • Máximo 1 nível de profundidade                           │
│    │                                                             │
│    ▼                                                             │
│  <Gateway: SKILL.md ≤ 500 linhas?>                              │
│    │ NÃO ──────────────────────────────► [Extrair para refs/]   │
│    │ SIM                                                         │
│    ▼                                                             │
│  (END SP2 → próximo: SP3)                                        │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

#### SP3 — Criar Eval Set (Trigger Testing)

```bpmn
┌──────────────────────────────────────────────────────────────────┐
│ SUBPROCESSO SP3: EVAL SET                                        │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  (START)                                                         │
│    │                                                             │
│    ▼                                                             │
│  [T1] Criar ~20 queries realistas]                              │
│    │  • 8-10 should_trigger: true                                │
│    │  • 8-10 should_trigger: false                               │
│    │  • Incluir: file paths, typos, linguagem casual             │
│    │                                                             │
│    ▼                                                             │
│  [T2] Variar dimensões de trigger queries]                      │
│    │  • Phrasing: formal/casual/abreviado                        │
│    │  • Explicitness: direto / implícito                         │
│    │  • Complexity: simples / multi-step                         │
│    │                                                             │
│    ▼                                                             │
│  [T3] Criar near-miss negatives (mais valiosos!)]               │
│    │  Ex skill CSV-analyzer:                                     │
│    │  ✅ "I need to update formulas in Excel" → should: false    │
│    │  ❌ "Write a fibonacci function" → muito óbvio, testa nada  │
│    │                                                             │
│    ▼                                                             │
│  [T4] Split 60/40 (Train/Val)]                                  │
│    │  • train_queries.json  (60%)                                │
│    │  • validation_queries.json (40%)                            │
│    │  • Shuffle aleatório, proporcional pos/neg                  │
│    │                                                             │
│    ▼                                                             │
│  (END SP3 → próximo: SP4)                                        │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘

ESTRUTURA evals/evals.json:
```json
{
  "skill_name": "nome-da-skill",
  "evals": [
    {
      "id": 1,
      "query": "...",
      "should_trigger": true,
      "files": ["evals/files/exemplo.csv"]
    }
  ]
}
```
```

#### SP4 — Otimizar Description (Optimization Loop)

```bpmn
┌──────────────────────────────────────────────────────────────────┐
│ SUBPROCESSO SP4: DESCRIPTION OPTIMIZATION LOOP                   │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  (START — trigger rate NOT OK)                                   │
│    │                                                             │
│    ▼                                                             │
│  [T1] Avaliar description atual vs Train Set]                   │
│    │  Trigger Rate = triggers / (runs × n_queries)              │
│    │  threshold padrão = 0.5                                     │
│    │                                                             │
│    ▼                                                             │
│  <Gateway: Qual tipo de falha?>                                  │
│    │                                                             │
│    ├─ should-trigger NÃO dispara ──────────► description NARROW │
│    │    └─ Ampliar escopo, adicionar contextos                   │
│    │                                                             │
│    ├─ should-NOT-trigger dispara ──────────► description BROAD  │
│    │    └─ Adicionar anti-casos, especificidade                  │
│    │                                                             │
│    └─ ambos ───────────────────────────────► Reframe estrutural  │
│         └─ Framing totalmente diferente                          │
│                                                                  │
│    ▼                                                             │
│  [T2] Regras Anti-Overfitting]                                  │
│    │  ⚠ NÃO adicionar keywords específicas de queries falhadas  │
│    │  ✅ Generalizar a CATEGORIA que as queries representam      │
│    │  ✅ Verificar < 1024 chars                                  │
│    │                                                             │
│    ▼                                                             │
│  [T3] Testar description revisada vs Train Set]                 │
│    │                                                             │
│    ▼                                                             │
│  <Gateway: Train OK + iteração ≤ 5?>                            │
│    │ NÃO e iter < 5 ──────────────────────► [Voltar T1]        │
│    │ SIM                                                         │
│    ▼                                                             │
│  [T4] Selecionar MELHOR iteração via Validation Set]            │
│    │  (melhor = maior validation pass rate, não a última)        │
│    │                                                             │
│    ▼                                                             │
│  (END SP4 → Continuar Fase 7: Output Quality)                   │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

---

## PARTE III — CHECKLIST GOLD STANDARD (PMQ ≥ 9.5)

```
CHECKLIST OBRIGATÓRIO — CRITÉRIOS DE ENTREGA

FRONTMATTER (CE — Completude):
  ☐ name: lowercase, hyphens, ≤ 64 chars, gerund form preferido
  ☐ description: ≥ 5 trigger phrases, ≥ 1 anti-caso, 3ª pessoa
  ☐ description: < 1024 chars
  ☐ Sem "anthropic" / "claude" no name

BODY (PRI — Profundidade):
  ☐ Seção "When to Use" com ✅ e ❌ claros
  ☐ Core Concepts: apenas o que Claude não sabe nativamente
  ☐ Processo em imperativo ("Execute", "Valide", "Salve")
  ☐ Freedom calibrado (HIGH/MED/LOW por operação)
  ☐ ≥ 2 exemplos Input→Output completos
  ☐ Seção Gotchas com falhas específicas + prevenção
  ☐ SKILL.md ≤ 500 linhas (ou hierarquia com references/)
  ☐ Paths relativos em file references (./references/xxx.md)
  ☐ Seção Integration sem hyperlinks (plain text)

EVAL SET (RA — Relevância):
  ☐ ≥ 20 queries (10 pos / 10 neg)
  ☐ Near-miss negatives incluídos
  ☐ Split 60/40 Train/Val feito ANTES de otimizar
  ☐ Trigger Rate ≥ 0.5 no Validation Set
  ☐ Output quality testada With vs Without Skill

TRIGGERING (OVA — Originalidade):
  ☐ Description "pushy" (cobre casos implícitos)
  ☐ Palavras-chave do domínio específicas
  ☐ Otimização via loop (máx 5 iterações, anti-overfit)
  ☐ Melhor iteração = validação pass rate (não a última)

INTEGRAÇÃO (EIC — Estrutura):
  ☐ Referências a skills dependentes no body
  ☐ Compatibilidade declarada (se aplicável)
  ☐ WAL/continuidade documentada (para skills DTP/MO)

ENTREGA (PI — Precisão):
  ☐ skills-ref validate ./skill-name ✅
  ☐ python -m scripts.package_skill <path> ✅
  ☐ GitOps: branch + commit message + tag
  ☐ commit msg: "feat(skill): add [nome] v1.0 — PMQ [score]"
```

---

## PARTE IV — TEMPLATES PRONTOS

### Template Frontmatter Gold

```yaml
---
name: verbo-substantivo                 # ex: processing-pdfs, analyzing-csvs
description: >
  [VERBO IMPERATIVO] [O QUE FAZ ESPECIFICAMENTE] em [CONTEXTO ESPECÍFICO].
  Use SEMPRE que [TRIGGER EXPLÍCITO 1], [TRIGGER 2], ou [TRIGGER 3].
  Ativa automaticamente quando o usuário menciona [PALAVRAS-CHAVE DO DOMÍNIO],
  mesmo que não mencione explicitamente "[KEYWORD CANÔNICA]".
  NÃO usar para [ANTI-CASO 1] ou [ANTI-CASO 2].
---
```

### Template Body Gold

```markdown
# [Nome da Skill]

[1 parágrafo: propósito + por que importa para o agente]

## Quando Usar Esta Skill
- ✅ [Caso de uso 1 — específico]
- ✅ [Caso de uso 2 — específico]
- ❌ NÃO usar para [anti-caso — próximo mas diferente]

## Processo

### FASE 1: [Nome]
[Instruções imperativas. "Execute X", "Valide Y"]
**Freedom**: HIGH | MED | LOW — [justificativa]

### FASE 2: [Nome]
[Instruções. Se frágil: sequência exata obrigatória]

## Exemplos

**Exemplo 1 — Caso Base:**
```
Input:  [prompt realista com contexto]
Output: [resultado esperado específico]
```

**Exemplo 2 — Edge Case:**
```
Input:  [caso limite]
Output: [como o agente deve lidar]
```

## Gotchas

1. **[Título do Problema]**: [O que vai errado] + [Como prevenir].
2. **[Outro problema]**: [Descrição + prevenção].

## Integração

- nome-skill-A — [como esta skill complementa A]
- nome-skill-B — [quando usar em conjunto com B]

## Referências

- [Referência interna](./references/detalhe.md) — quando precisar de [condição]
```

### Template evals/evals.json

```json
{
  "skill_name": "nome-da-skill",
  "evals": [
    {
      "id": 1,
      "prompt": "[Prompt realista — com contexto, path, linguagem natural]",
      "expected_output": "[Descrição legível de sucesso — o que o agente deve produzir]",
      "should_trigger": true,
      "files": []
    },
    {
      "id": 2,
      "prompt": "[Near-miss query — parece relacionado mas NÃO deve triggerar]",
      "expected_output": "[Agente deve resolver sem invocar esta skill]",
      "should_trigger": false,
      "files": []
    }
  ]
}
```

---

## PARTE V — FLUXO COMPLETO (Visão Executiva)

```
SKILL FACTORY — FLUXO INTEGRADO (N1 + N2 + N3)

┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  [IDEIA] ──► [DTP Score] ──► Score < threshold? ──► DESCARTAR      │
│                                     │                               │
│                                     ▼ Score OK                      │
│                                                                     │
│  ┌──────────── FASE CONSTRUÇÃO ────────────┐                        │
│  │                                         │                        │
│  │  [Criar Diretório]                      │                        │
│  │       ├── SKILL.md                      │                        │
│  │       ├── scripts/     (opcional)       │                        │
│  │       ├── references/  (se > 500L)      │                        │
│  │       ├── assets/      (opcional)       │                        │
│  │       └── evals/       (queries)        │                        │
│  │                                         │                        │
│  │  [SP1: Frontmatter]                     │                        │
│  │    name (kebab, ≤64) +                  │                        │
│  │    description (3ª pessoa, pushy, ≤1024)│                        │
│  │                                         │                        │
│  │  [SP2: Body SKILL.md]                   │                        │
│  │    When-to-Use → Process → Examples     │                        │
│  │    → Gotchas → Integration (≤500L)      │                        │
│  │                                         │                        │
│  └──────────── FASE CONSTRUÇÃO ────────────┘                        │
│                                                                     │
│  ┌──────────── FASE VALIDAÇÃO ─────────────┐                        │
│  │                                         │                        │
│  │  [SP3: Criar Eval Set]                  │                        │
│  │    20 queries (60/40 split)             │                        │
│  │    near-miss negatives obrigatórios     │                        │
│  │                                         │                        │
│  │  [Testar Trigger Rate] × 3 runs/query   │                        │
│  │    ├── Rate < 0.5? → [SP4: Otimizar]   │                        │
│  │    └── Rate ≥ 0.5? → continua          │                        │
│  │                                         │                        │
│  │  [SP4: Description Optimization Loop]   │                        │
│  │    Narrow → Ampliar / Broad → Estreitar │                        │
│  │    Anti-overfit: generalizar categoria  │                        │
│  │    Máx 5 iterações → selecionar melhor  │                        │
│  │                                         │                        │
│  │  [Testar Output Quality]                │                        │
│  │    With-Skill vs Without-Skill          │                        │
│  │    PMQ < 9.5? → Refinar Body            │                        │
│  │                                         │                        │
│  └──────────── FASE VALIDAÇÃO ─────────────┘                        │
│                                                                     │
│  ┌──────────── FASE PUBLICAÇÃO ────────────┐                        │
│  │                                         │                        │
│  │  [Validar]  skills-ref validate ./      │                        │
│  │  [Package]  package_skill.py            │                        │
│  │  [GitOps]   branch → commit → tag       │                        │
│  │                                         │                        │
│  └──────────── FASE PUBLICAÇÃO ────────────┘                        │
│                                                                     │
│                   ✅ SKILL ENTREGUE                                  │
│                   (Versionada · Testada · Packageada)               │
└─────────────────────────────────────────────────────────────────────┘
```

---

## PARTE VI — CONSTRAINTS E MANDATOS (Specification Hard Limits)

```
HARD LIMITS (skills-ref validate irá falhar se violados):
  ├─ name: apenas lowercase letters, numbers, hyphens
  ├─ name: máx 64 chars
  ├─ name: sem "anthropic", "claude"
  ├─ name: sem XML tags
  ├─ description: obrigatória e não-vazia
  ├─ description: máx 1024 chars
  └─ description: sem XML tags

SOFT LIMITS (best practice, não falham validate):
  ├─ SKILL.md body: ≤ 500 linhas
  ├─ description: 3ª pessoa (discovery issues se 1ª pessoa)
  ├─ name: gerund form preferido (processing-pdfs)
  ├─ references/: arquivos focados, um nível de profundidade
  └─ file references: relative paths apenas (./references/xxx.md)

ANTI-PATTERNS (causam undertriggering ou falha de qualidade):
  ├─ description vaga: "Process files." → não dispara
  ├─ body assumindo que Claude sabe tudo: desperdiça tokens
  ├─ otimizar description contra todo o eval set → overfitting
  ├─ selecionar última iteração (não a de maior val pass rate)
  └─ SKILL.md > 500L sem mover para references/
```

---

## REGISTRO WAL

```yaml
session_id: BLUEPRINT-SKILL-CREATION-2026-03-26
timestamp_checkpoint: 2026-03-26T00:00:00Z
completed_phases: [KDI, GraphRAG-Mapping, BPMN-N1, BPMN-N2, BPMN-N3-SP1-SP4, Templates, Checklist]
skills_aplicadas: [engenheiro-processos-master, graphrag-universal]
base_epistemica: [agentskills.io/specification, agentskills.io/best-practices, agentskills.io/optimizing-descriptions, agentskills.io/evaluating-skills, DTP-SKILL-CREATION-MASTERPLAN.md]
pmq_estimado: 9.6
artifact_path: /mnt/user-data/outputs/SKILL-CREATION-BLUEPRINT.md
next_action: USAR como referência para criar skills Wave 1 (DTP-MASTERPLAN)
continuity_hash: sha256-BLUEPRINT-BPMN-N3-SP4-PMQ-9.6
```

---

*Blueprint gerado via engenheiro-processos-master (BPMN N1→N3) + graphrag-universal (entity mapping) | 2026-03-26*
