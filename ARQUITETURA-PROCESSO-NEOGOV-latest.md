---
id: NEOGOV-ARQUITETURA-PROCESSO-MASTER
filename: ARQUITETURA-PROCESSO-NEOGOV-v1.GOV.1.md
alias: ARQ-PROC-NEOGOV
created_at: 2026-05-15T17:50:00Z
type: PROCESS_ARCHITECTURE_MASTER
designation: ARQ-PROC
function: UNIFIED_PROCESS_ARCHITECTURE
parent_system: NeoGov BP v2.1
paradigm: OMNI_v3.0 ⊕ POP_v2.1.1.1 → S→Q→I→A_DEC_EXEC_COR
integrates:
  - PROTOCOLO_OPERACIONAL_PADRAO.md (OMNI v3.0 · DEC/EXEC/COR + KDI + WAL + SCORING)
  - INSTRUCAO-PROTOCOLO-OPERACIONAL-NEOGOV-latest.md (POP v2.1.1.1 · governance NeoGov)
  - skills/ENGINE-MODULES/COGNITIVE_ARCHITECTURE_COMPLETE.md (S→Q→I→A engine)
  - skills/ENGINE-MODULES/HOLISTIC_ITERATIVE_QUALITY_MODULE_v1.0.md (HIQM ≥95%)
  - skills/ENGINE-MODULES/STRATEGIC-ACTION-ENGINE-v4.0.md (SAE quantificado)
  - skills/ENGINE-MODULES/MODULO-DOCUMENTACAO-TECNICA-v1.0.md (MDT PIER+chunks)
  - skills/SHUN_TZU-ART_OF_WAR/MEEST-AE_v2.1.md (estratégia + MSP segmentação)
status: ACTIVE
authority: PROCESS_CONSTITUTION (subordinada ao POP §1)
hash: ARQ-PROC-v1.GOV.1-UNIFICATION-OMNI-POP
purpose: Documento ÚNICO de processo executável que une os 2 protocolos vigentes
tags: [arquitetura, processo, master, omni, pop, neogov, governance]
quality_target: PMQS ≥ 8.0 · VVV ≥ 0.90
---

# 🏛️ Arquitetura de Processo NeoGov · Unificação OMNI v3.0 ⊕ POP v2.1.1.1

> Documento mestre que torna **executável** a união dos dois protocolos vigentes.  
> Constituição → Engine cognitiva → Ciclo DEC/EXEC/COR → Continuidade → Versionamento → Saída.  
> Subordinado ao POP §1 (constituição NeoGov). Sobrescreve detalhes operacionais conflitantes do OMNI v3.0 quando colidirem com o POP.

---

## §0 · ÍNDICE FUNCIONAL

| Seção | Tópico | Quando consultar |
|---|---|---|
| §1 | Mapa de unificação (OMNI ⊕ POP) | Para entender de onde vem cada elemento |
| §2 | Constituição operacional consolidada (Camada 0) | Antes de qualquer execução |
| §3 | Engine cognitiva S→Q→I→A (Camada 0.5) | Em todo pensamento gerador |
| §4 | Ciclo DEC · EXEC · COR (Camada 1) | Para dispatch de qualquer ação |
| §5 | KDI · Knowledge Discovery & Injection (Gate obrigatório) | Início de cada sprint ou troca de domínio |
| §6 | Workflow PIER → PEII-LLM → PMQS (dentro do EXEC) | Em produção de artefato |
| §7 | Scoring Engine: PMQS · VVV · PMQS_final | Em toda avaliação |
| §8 | Sistema de continuidade 4 camadas + WAL | Inter-sessão/inter-sprint |
| §9 | Versionamento mandatório (DIRETÓRIO ./FILENAME/ + latest na raiz) | Em toda edição |
| §10 | Marcadores visuais ✅🟢🟡🟠🔴 | Em toda afirmação numérica |
| §11 | Gates e critérios de parada | Validar conclusão |
| §12 | Anti-padrões (proibidos absolutos) | Decisão de design/redação |
| §13 | Tripé multi-output | Entrega final |
| §14 | Estrutura de diretórios consolidada | Localização física |
| §15 | Checklist de ativação (pré-sprint) | Antes de iniciar trabalho |
| §16 | Glossário consolidado | Referência terminológica |

---

## §1 · MAPA DE UNIFICAÇÃO (OMNI v3.0 ⊕ POP v2.1.1.1)

### 1.1 · Relação de autoridade entre os dois protocolos

```
┌────────────────────────────────────────────────────────────────┐
│  POP v2.1.1.1 (NeoGov)              OMNI v3.0 (genérico)       │
│  ════════════════════              ═══════════════════════     │
│  CONSTITUTION NeoGov §1            Constitution Module §1      │
│  Fontes canônicas §2          ←→   KDI · TOOL · SKILL §2-4    │
│  Anti-padrões §3              ⊕    (sem equivalente)          │
│  Marcadores visuais §4        ⊕    (sem equivalente)          │
│  Versionamento §5             ←→   GitOps §4 + WAL §5         │
│  Mandato IA Própria §6        ⊕    (sem equivalente · NeoGov-specific)
│  D-015 Lastro §7              ⊕    (sem equivalente)          │
│  Fila DTP §8                  ←→   PROTOCOLO_OMNI §7 (DEC)    │
│  4 camadas continuidade §9    ←→   WAL_INTERFACE §5           │
│  Tripé multi-output §10       ⊕    (sem equivalente)          │
│  PIER·PEII·PMQS §11           ←→   SKILL_LIBRARY §4 + DEC §7  │
│  Gates §12                    ←→   Critérios de Parada §9     │
└────────────────────────────────────────────────────────────────┘

Regra de prevalência:
└─ Em conflito operacional: POP NeoGov vence (autoridade PROJECT_CONSTITUTION)
└─ Em ausência POP: OMNI v3.0 supre detalhamento (KDI, SCORING, WAL_INTERFACE)
└─ Em complementaridade: ambos se somam (⊕)
```

### 1.2 · Princípio de unificação

> POP define **O QUÊ** é proibido/imperativo e **QUÊ** está versionado/lastreado/marcado.  
> OMNI define **COMO** o processo flui (DEC→EXEC→COR), **COMO** validar (VVV embutido em SCORING), **COMO** persistir (WAL).  
> Esta arquitetura junta os dois numa visão executável única.

---

## §2 · CONSTITUIÇÃO OPERACIONAL CONSOLIDADA (Camada 0)

### 2.1 · Proibições absolutas (POP §1.1 + OMNI §1.1)

```
🚫 NUNCA execute sem analisar CENÁRIO + PLANEJAR (5W1H)
🚫 NUNCA execute sem resolver dependências primeiro
🚫 NUNCA siga plano obsoleto → re-avaliar após cada ação
🚫 NUNCA decida sem dados → INVESTIGAÇÃO precede decisão
🚫 NUNCA atue em DÚVIDA · NUNCA CHUTE
🚫 NUNCA gere PMQS inflado · VVV inflado
🚫 NUNCA estimativa sem marcador 🟡 + LASTRO
🚫 NUNCA assuma API externa de IA para dado pessoal/legal NeoGov
🚫 NUNCA modele custo antes de definir arquitetura técnica
```

### 2.2 · Imperativos universais (POP §1.2 + OMNI §1.2)

```
✅ SEMPRE enumere TODOS os caminhos antes de escolher
✅ SEMPRE respeite ordem topológica (dependências)
✅ SEMPRE re-avalie campo após cada execução
✅ SEMPRE INVESTIGUE / COLETE / PESQUISE antes de afirmar
✅ SEMPRE priorize SOTA 2026 + fundamentos estáveis validados
✅ SEMPRE DISPATCH para protocolo correto conforme estado atual
✅ SEMPRE marque estimativa com 🟡 + LASTRO rastreável (POP §7)
✅ SEMPRE versione artefato com edição antecipada (§9)
```

### 2.3 · Regras de Ouro fundidas (POP §1.3 + OMNI §1.3)

| ID | Regra | Origem |
|---|---|---|
| RGO-1 | Cada execução MUDA o campo → re-avaliar ANTES da próxima | POP+OMNI |
| RGO-2 | Nenhuma task é "done" sem EVIDÊNCIA REAL | POP+OMNI |
| RGO-3 | Minimizar refatoração = decidir na ordem certa | POP+OMNI |
| RGO-4 | Maximizar qualidade = não construir sobre base instável | POP+OMNI |
| RGO-5 | Honestidade Epistêmica > Aparência de Completude · NUNCA opere domínio desconhecido sem KDI prévio | POP+OMNI |
| RGO-6 | Auditabilidade Reversa · SCORE sem VVV validado é ZERO (falha segura) | POP+OMNI |
| RGO-7 | Tradução cognitiva técnico→benefício (IN-014 · D-012) · Recursão DEC↔COR limitada a 3 ciclos | POP+OMNI |
| RGO-8 | Modelo de IA é OBJETO DE PRODUTO (mandato §6 POP) · Skills/Tools selecionados EXPLICITAMENTE pelo KDI | POP+OMNI |

---

## §3 · ENGINE COGNITIVA S→Q→I→A (Camada 0.5)

> Todo pensamento gerador percorre **obrigatoriamente** S→Q→I→A antes de produzir output.

### 3.1 · Pipeline de 4 fases

```
[S] SOCRÁTICO (Deconstruct)
    └─ Epómetrismo: listar APENAS o verificavelmente conhecido
    └─ Maiêutica: extrair premissas ocultas (XY problem)
    └─ Divisão: fragmentar em elementos atômicos
    └─ Definição: precisão terminológica operacional
    Output: [TRACE-S]

[Q] QUESTIONADOR (Interrogate)
    └─ 5N: Negação · Nuance · Núcleo · Nexo · Nulidade
    └─ Classificação: FACT | INFERENCE | SPECULATION | BELIEF
    └─ "Por quê?" 3× recursivo em cada conclusão intermediária
    Output: [TRACE-Q] + classificação epistemológica

[I] INOVADOR (Synthesize)
    └─ Analogia estrutural (3+ isomorfismos distantes)
    └─ Recombinação: {Inverter, Escalar, Substituir, Transpor, Hibridizar}
    └─ Insight de fronteira (gap epistêmico)
    └─ Compressão fractal Micro/Meso/Macro
    Output: [TRACE-I]

[A] ADVERSARIAL (Stress-Test)
    └─ Advocatus Diaboli: refutar completamente [I]
    └─ Edge cases · worst case · contraditórios
    └─ Checklist viés: Confirmação · Âncora · Recência · Autoridade · Ação
    └─ Falsificação Popperiana
    Output: [TRACE-A]
```

### 3.2 · Métrica Quality-of-Thought (CoT)

```
QUALITY_CoT = (Profundidade[S] × Rigidez[Q] × Originalidade[I] × Robustez[A])
              / (Vieses_não_mitigados + 1)

Threshold: Se QUALITY_CoT < 7.0 → RETORNAR ao [S] com input refinado
```

---

## §4 · CICLO DEC · EXEC · COR (Camada 1)

### 4.1 · Diagrama arquitetural unificado

```
INPUT (solicitação)
    │
    ▼
┌──────────────────────────────────────────────────────────┐
│ PRE-ALWAYS (obrigatório · POP §11.1 + OMNI §8)           │
│   [1] Clarificação Socrática (deprender objetivo real)   │
│   [2] OBJETIVO_GLOBAL mensurável + imutável              │
│   [3] WAL.snapshot · recuperar contexto anterior         │
└──────────────────────┬───────────────────────────────────┘
                       ▼
┌──────────────────────────────────────────────────────────┐
│ GATE_KDI (obrigatório RGO-5 · OMNI §2)                   │
│   Domínio conhecido? ──┬── SIM: usar KDI_OUTPUT do WAL   │
│                        └── NÃO: ATIVAR KDI completo      │
│   KDI_OUTPUT = {                                          │
│     conhecimento_dominio,                                 │
│     skills_recomendadas,                                  │
│     ferramentas_necessarias,                              │
│     mapeamento_workflow                                   │
│   }                                                       │
│   Threshold: KDI_SCORE ≥ 9.5 · senão DPIER (ampliar)     │
└──────────────────────┬───────────────────────────────────┘
                       ▼ KDI_OUTPUT completo
┌──────────────────────────────────────────────────────────┐
│ CAMADA_DECISÃO (DTP · POP §8 + OMNI §7)                  │
│   Fase 1 · ENUMERAÇÃO SOCRÁTICA (todos os caminhos)      │
│   Fase 2 · DAG (grafo de dependências · ordem topológica)│
│   Fase 3 · SCORING (PMQS pesos POP §11.2 × VVV)          │
│   Fase 4 · DISPATCH                                       │
│     ├── tipo CRIAÇÃO → CAMADA_EXECUÇÃO                   │
│     ├── tipo CORREÇÃO → CAMADA_CORREÇÃO                  │
│     ├── tipo REFATORAÇÃO → COR (branch) → EXEC (rebuild) │
│     └── tipo INVESTIGAÇÃO → KDI inline                   │
└──────────────────────┬───────────────────────────────────┘
                       ▼ fila ordenada + skills + tools
┌──────────────────────────────────────────────────────────┐
│ CAMADA_EXECUÇÃO (MO · OMNI §7 + POP §11)                 │
│   [0] Ancoragem · WAL.snapshot + Constitution check       │
│   [1] Gate pré-execução (dependências DONE? depth<3?)    │
│   [2] Skill Selector (do KDI_OUTPUT)                     │
│   [3] PIER → PEII-LLM (§6 desta arquitetura)             │
│   [4] WAL.commit + atualização 4 camadas (§8)            │
│   [5] Continuidade · próximo da fila                     │
│   FALHA → DISPATCH CAMADA_CORREÇÃO                       │
└──────────────────────┬───────────────────────────────────┘
                       │ evidência_falha
                       ▼
┌──────────────────────────────────────────────────────────┐
│ CAMADA_CORREÇÃO (CM · OMNI §7)                           │
│   [0] Checkpoint (branch fix/timestamp · recursion++)    │
│   [1] Investigação · logs · evidências                   │
│   [2] Análise de impactos (recomputar DAG)               │
│   [3] Planejamento (hotfix vs refactor vs rollback)      │
│   [4] Execução da correção                               │
│   [5] Teste (unitário · integração · regressão)          │
│   [6] Validação (PMQS≥9.5 + VVV=1.0)                     │
│       ├── SUCESSO → reset_recursion + retorna EXEC       │
│       ├── FALHA depth<3 → DISPATCH DECISÃO (nova estr.)  │
│       └── FALHA depth≥3 → ESCALADA HUMANA (RGO-7)        │
│   [7] Reintegração                                       │
│   [8] Finalização (limpa branch)                         │
└──────────────────────────────────────────────────────────┘
                       │
                       ▼
              ┌─────────────────┐
              │ RE-AVALIAÇÃO    │
              │ (próximo ciclo  │
              │  OU parada §11) │
              └─────────────────┘
```

### 4.2 · Triggers de cada camada

| Camada | Trigger |
|---|---|
| DECISÃO | ≥2 caminhos · incerteza de ordem · risco retrabalho · domínio desconhecido |
| EXECUÇÃO | fila_ordenada recebida do DECISÃO + Dispatch completo |
| CORREÇÃO | evidência_falha de EXEC ou DEC + recursion_check OK (depth<3) |
| INVESTIGAÇÃO | gap de conhecimento detectado · KDI inline |

---

## §5 · KDI · KNOWLEDGE DISCOVERY & INJECTION (Gate Obrigatório)

### 5.1 · Quando ativar (RGO-5)

```
KDI obrigatório se:
  - Início de novo sprint
  - Mudança de domínio (e.g., sair de modelagem custo → entrar em jurídico)
  - Termo desconhecido na solicitação
  - Sem KDI prévio salvo no WAL para este contexto
```

### 5.2 · Método (5 fases · OMNI §2)

```
[1] ANÁLISE SEMÂNTICA · quebrar objetivo em domínios técnicos
[2] SKILL MATCHING   · consultar biblioteca (BABOK + ENGINE-MODULES + skills/)
[3] TOOL MATCHING    · consultar registry (Read/Edit/Skill/Bash/Agent)
[4] ORQUESTRAÇÃO     · ordenar por dependências · associar tools
[5] VALIDAÇÃO KDI    · VVV_AUDITOR + score ≥ 9.5 (senão DPIER)
```

### 5.3 · KDI_OUTPUT obrigatório (estrutura)

```yaml
KDI_OUTPUT:
  conhecimento_dominio:
    conceitos_chave: []
    melhores_praticas: []
    riscos_comuns: []
    fontes_referencia: []      # URLs/docs para VVV
  
  skills_recomendadas:
    - skill_id: "business-analysis:estimation"
      justificativa: "..."
      momento_ativacao: PRE|DURANTE|POS
      dependencias: []
      fase_bpm: CAMADA_DECISAO|EXECUCAO|CORRECAO
  
  ferramentas_necessarias:
    - tool_id: "Read|Edit|Skill|Bash|Agent"
      categoria: datasource|web|code|visualization|memory
      proposito: "..."
      fallback: "..."
  
  mapeamento_workflow:
    - fase: "..."
      skill_aplicada: "..."
      tools_utilizadas: []
      output_esperado: "..."
      criterio_sucesso: "..."
```

### 5.4 · Skills disponíveis no projeto (catálogo essencial)

Skills NeoGov-aplicáveis (uso preferencial via Skill tool):

| Categoria | Skill | Quando |
|---|---|---|
| Estimativa | `business-analysis:estimation` | Análogo, paramétrico, três pontos |
| Stakeholders | `business-analysis:stakeholder-analysis` | Power/Interest + RACI |
| Jornada | `business-analysis:journey-mapping` | Touchpoints + emoções |
| Risco | `business-analysis:risk-analysis` | Registro + mitigação |
| Decisão | `business-analysis:decision-analysis` | Tabelas + scoring ponderado |
| Processo | `business-analysis:process-modeling` | BPMN + swimlanes |
| Estratégia | `business-analysis:swot-pestle-analysis` | SWOT/PESTLE/Porter |
| BMC | `business-analysis:business-model-canvas` | 9 blocos |
| Documentação | `documentation-standards:runbook-creation` | Runbooks operacionais |
| Arquitetura | `documentation-standards:arc42-documentation` | Sistema docs arc42 |

Engines locais (`skills/ENGINE-MODULES/`):
- `COGNITIVE_ARCHITECTURE_COMPLETE.md` — S→Q→I→A Layer 0/0.5/1/2
- `HOLISTIC_ITERATIVE_QUALITY_MODULE_v1.0.md` — HIQM ≥95%
- `STRATEGIC-ACTION-ENGINE-v4.0.md` — SAE (SWOT quantificado + 5Whys + 5W1H)
- `MODULO-DOCUMENTACAO-TECNICA-v1.0.md` — MDT PIER+chunks+meta-audit
- `MODULO-PESQUISA-SISTEMATICA-v1.md` — pesquisa sistemática
- `skills/SHUN_TZU-ART_OF_WAR/MEEST-AE_v2.1.md` — MEEST-AE (segmentação MSP + DTS + CNM)

---

## §6 · WORKFLOW PIER → PEII-LLM → PMQS (dentro do EXEC)

### 6.1 · Macro-fluxo (POP §11.1)

```
[PRE-ALWAYS] Clarificação Socrática
    ↓
[KDI] Knowledge Discovery & Injection (§5)
    ↓
[PIER] Gerar 3-5 abordagens · avaliar · selecionar vencedora
    │ Product · Interview · Evaluation · Research
    ↓
[PEII-LLM] 7 fases de refinamento iterativo
    │ [1] Análise estratégica · [2] V1 · [3] Auto-avaliação PMQS
    │ [4] Refinamento iterativo · [5] Revisão crítica final
    │ [6] Entrega · [7] Meta-learning
    ↓
[PMQS] Validar ≥ 8.0 realista · ≥ 9.5 alvo ouro (§7)
    ↓
[VVV] Validar fontes · multiplicador 0.0-1.0 (§7)
    ↓
[KAIZEN] Registrar aprendizados · padronizar
    ↓
[WAL] Commit + atualização 4 camadas continuidade (§8)
```

### 6.2 · Convergência PEII-LLM (POP §11.3)

```
Se PMQS_n ≥ 9.5 → entrega
Se PMQS_n < 9.5 E (PMQS_n − PMQS_{n−1}) > 3% → refinar
Se PMQS_n < 9.5 E aumento ≤ 3% por 4 iterações → DPIER (ampliar horizontes)
```

---

## §7 · SCORING ENGINE · PMQS + VVV

### 7.1 · PMQS · 7 critérios + multiplicador (POP §11.2)

| Critério | Peso |
|---|---:|
| CE · Completude e Especificidade | 15% |
| PI · Precisão das Informações | 15% |
| CC · Clareza Cristalina | 10% |
| PRI · Profundidade e Rigor | 20% |
| RA · Relevância Absoluta | 15% |
| EIC · Estrutura e Coerência | 10% |
| OVA · Originalidade e Valor | 15% |
| **VVV** | **Multiplicador 0.0–1.0** |

Fórmula final:
```
PMQS_bruto = Σ(peso_i × métrica_i)
PMQS_final = PMQS_bruto × VVV
```

### 7.2 · Targets canônicos NeoGov (POP §11.2 + D-007)

- **Realista**: PMQS_final ≥ **8.0** (não inflar · D-007)
- **Ouro**: PMQS_final ≥ **9.5** (pode não ser atingido em todos os sprints)

### 7.3 · VVV embutido · falha segura (OMNI §6 + RGO-6)

```
VVV = validacao_verdade_verificada ?? 0.0   # default 0 = falha segura

Procedimento:
  [1] Verificar se fonte existe (URL acessível · doc existe)
  [2] Verificar se referência existe DENTRO da fonte
      ├─ NÃO → VVV = 0.0 · Flag REFERENCIA_NAO_VERIFICADA
      └─ SIM → prosseguir
  [3] Documentar mapa_fontes × evidencias
  [4] Calcular VVV proporcional ao nível de validação

VVV = 0 → PMQS_final = 0 (impossibilita aprovação)
```

### 7.4 · Pesos de decisão (DTP scoring · OMNI §6)

Para ordenação de candidatos no DAG:

| Peso | Valor |
|---|---:|
| valor_entregue | 0.30 |
| custo_execucao (invertido) | -0.20 |
| risco_adiamento | 0.20 |
| num_dependentes | 0.15 |
| irreversibilidade | 0.15 |

---

## §8 · CONTINUIDADE 4 CAMADAS + WAL

### 8.1 · As 4 camadas vivas (POP §9)

| Camada | Arquivo (na raiz) | Função | Destino BP final |
|---|---|---|---|
| **WAL Master** | `SESSION-STATE-latest.md` | Estado vivo · hash chain · fila DTP · métricas | Operacional |
| **VVV Log** | `APENDICE-A-VVV-LOG-latest.md` | Toda afirmação factual + VVV | Apêndice A |
| **Decision Log** | `APENDICE-B-DECISIONS-LOG-latest.md` | Toda decisão + rationale + opções rejeitadas | Apêndice B |
| **Insight Carry** | `APENDICE-C-INSIGHTS-CARRY-latest.md` | Insights inter-sprint | Nota técnica |
| **Lastreamento** | `APENDICE-E-LASTREAMENTO-latest.md` | Lastros D-015 das estimativas | Apêndice E |

### 8.2 · Regra de atualização (PRINCÍPIO DE OURO)

> **Nenhum sprint começa sem ler as 4 camadas. Nenhum sprint termina sem incrementar as 4 camadas.**

Sprint N executa:
```
produz capítulo {NN-nome}-latest.md
    │
    ├─→ INCREMENTA VVV-LOG (toda afirmação validada)
    │
    ├─→ INCREMENTA DECISIONS-LOG (toda decisão tomada)
    │
    ├─→ INCREMENTA INSIGHTS-CARRY (descobertas que afetam próximos)
    │
    ├─→ INCREMENTA LASTREAMENTO (toda 🟡 nova)
    │
    └─→ ATUALIZA SESSION-STATE (hash + status + próximo)
            │
            ▼
        GATE de aprovação
            │
            ▼
    Sprint N+1 LÊ as 5 camadas ANTES de começar
```

### 8.3 · WAL · interface unificada (OMNI §5)

```
WAL.snapshot()        → captura estado [N] · injeta CONSTITUTION · valida checksum
WAL.commit()          → persiste em gitops + memory + artifact · incrementa estado
WAL.checkout(N)       → restaura estado anterior
WAL.diff(N, N-1)      → calcula delta
WAL.recursion_check() → verifica depth DEC↔COR (limite 3 · RGO-7)
WAL.reset_recursion() → zera depth após reintegração bem-sucedida
```

Operação WAL inclui:
- `estado_atual` [N] mutável
- `contexto_constitucional` (herança + checksum)
- `snapshot` (DAG · fila · scores · evidências · skills · tools)
- `recursao_tracker` (depth + max_depth=3 + histórico)
- `persistencia` (git + memory_space + artifact)

---

## §9 · VERSIONAMENTO MANDATÓRIO · DIRETÓRIO ./FILENAME/ + LATEST NA RAIZ

### 9.1 · Sintaxe (POP §5 · refinada pela instrução do usuário)

```
./{FILENAME-base}/{filename-base}-v[N].{SPRINT}.{EDICAO}.{ext}   ← versionado, imutável
./{filename-base}-latest.{ext}                                    ← cópia na RAIZ
```

### 9.2 · Componentes

| Componente | Regra |
|---|---|
| `{FILENAME-base}/` | Subdiretório com o nome-base do artefato (sem versão) |
| `v[N]` | Versão maior do ARTEFATO (não muda durante release · ex: v2.x) |
| `SPRINT` | Sprint atual (1.1, 1.2, 2.1, 3.0.1, GOV, ...) |
| `EDICAO` | Contador incremental dentro do sprint, começa em 1 |
| `latest` | Cópia que SEMPRE aponta para a edição mais recente · vive na RAIZ |

### 9.3 · Regra crítica

> A edição seguinte é criada **ANTES** de receber edits.  
> Cria-se primeiro `./FILENAME/{file}-v2.X.Y.{ext}` (vazio ou cópia da anterior), recebe edits nela, e **ATUALIZA** `./{file}-latest.{ext}` na raiz.

### 9.4 · Exemplo aplicado (este documento)

```
./ARQUITETURA-PROCESSO-NEOGOV/                         ← diretório versionamento
  ├── ARQUITETURA-PROCESSO-NEOGOV-v1.GOV.1.md          ← versão imutável (esta)
  └── (futuro) ARQUITETURA-PROCESSO-NEOGOV-v1.GOV.2.md ← próxima edição

./ARQUITETURA-PROCESSO-NEOGOV-latest.md                ← cópia na raiz (sempre atualizada)
```

### 9.5 · Aplicação aos artefatos existentes (consolidação)

| Artefato base | Diretório versionamento | Latest na raiz |
|---|---|---|
| `INSTRUCAO-PROTOCOLO-OPERACIONAL-NEOGOV` | (a criar) `./INSTRUCAO-PROTOCOLO-OPERACIONAL-NEOGOV/` | `./INSTRUCAO-PROTOCOLO-OPERACIONAL-NEOGOV-latest.md` ✅ |
| `SESSION-STATE` | `./SESSION-STATE/` ✅ | `./SESSION-STATE-latest.md` ✅ |
| `APENDICE-A-VVV-LOG` | `./APENDICE-A-VVV-LOG/` ✅ | `./APENDICE-A-VVV-LOG-latest.md` ✅ |
| `APENDICE-B-DECISIONS-LOG` | `./APENDICE-B-DECISIONS-LOG/` ✅ | `./APENDICE-B-DECISIONS-LOG-latest.md` ✅ |
| `APENDICE-C-INSIGHTS-CARRY` | `./APENDICE-C-INSIGHTS-CARRY/` ✅ | `./APENDICE-C-INSIGHTS-CARRY-latest.md` ✅ |
| `APENDICE-E-LASTREAMENTO` | `./APENDICE-E-LASTREAMENTO/` ✅ | `./APENDICE-E-LASTREAMENTO-latest.md` ✅ |
| `DEBITO-D00X-*` | `./DEBITO/` ✅ | `./DEBITO/...-latest.md` ⚠️ (latest fora da raiz) |
| Capítulos `{NN}-{nome}` | `./CONTINUIDADE/` ✅ | `./{NN}-{nome}-latest.md` ✅ |
| Sprints | `./CONTINUIDADE/` ✅ | `./SPRINT-X.X.X-latest.md` ✅ |
| `BLUEPRINT-ALINHAMENTO-SOCIETARIO-PROLABORES` | (a criar) `./BLUEPRINT-ALINHAMENTO-SOCIETARIO-PROLABORES/` | `./BLUEPRINT-...-latest.md` ✅ |
| **ESTE documento** | `./ARQUITETURA-PROCESSO-NEOGOV/` ✅ | `./ARQUITETURA-PROCESSO-NEOGOV-latest.md` |

### 9.6 · Reescrita estratégica (POP §5.4)

```
└─ Em edições PEQUENAS ou LOCAIS → priorizar EDIT no original (patch)
└─ Se custo > benefício (alterações relevantes) → REESCRITA + nova edição
```

### 9.7 · Decision Log obrigatório

> Toda edição deve ter justificativa validada armazenada em DECISIONS-LOG (Camada 8.1) — append-only com opções rejeitadas.

---

## §10 · MARCADORES VISUAIS · D-015 (POP §4 + §7)

### 10.1 · Sistema de cores (obrigatório em toda afirmação numérica)

| Marcador | Tipo | VVV | Ação | Refatorar quando |
|---|---|---:|---|---|
| ✅ Verde | FATO · fonte primária verificada | 0.90-1.00 | Usar livre | Revalidar anualmente |
| 🟢 Verde-escuro | INFERÊNCIA com base em fato | 0.80-0.89 | Usar c/ tag `[INFERÊNCIA]` | Contexto mudar |
| 🟡 Amarelo | ESTIMATIVA POR ANÁLOGO | 0.60-0.79 | Usar c/ tag + LASTRO | Dado primário chegar |
| 🟠 Laranja | ESPECULAÇÃO fundamentada | 0.40-0.59 | Usar c/ tag `[ESPECULAÇÃO]` | Urgência alta |
| 🔴 Vermelho | ESPECULAÇÃO sem base | < 0.40 | **NÃO USAR** | Antes de qualquer uso |

### 10.2 · Aplicação obrigatória

Tabelas de custo · projeções financeiras · estimativas de mercado · unit economics · prazos · volumes · percentuais.

### 10.3 · Não se aplica

Citações literais de leis (FATO) · dados de fonte primária (FATO) · princípios qualitativos sem número.

### 10.4 · Anatomia do LASTRO (POP §7.3)

Toda estimativa 🟡 exige entrada em `APENDICE-E-LASTREAMENTO-latest.md`:

```yaml
LASTRO-XX:
  campo_lastreado: "..."
  marcador: 🟡 ESTIMATIVA POR ANÁLOGO
  vvv: 0.70
  analogo_usado:
    fonte: "..."
    url: "..."
    valor_observado: "..."
    adaptacao: "..."
  dado_primario_necessario:
    o_que: "..."
    como_obter: "..."
    quem_executa: "..."
    sprint_destino: "..."
  refatoracao_facilitada:
    formula: "..."
    variaveis_lastreadas: []
    impacto_se_mudar: "..."
    documentos_a_atualizar: []
```

---

## §11 · GATES E CRITÉRIOS DE PARADA

### 11.1 · Critérios de parada válidos (POP §12 + OMNI §9)

| Critério | Condição |
|---|---|
| ✅ Sucesso completo | Progresso 100% AND VVV ≥ 0.85 AND PMQS ≥ 8.0 |
| ⚖️ Custo marginal > Valor marginal | Continuar não justifica · documentar no WAL |
| ⛔ Bloqueio externo irredutível | Dependência externa não resolvível · WAL-handoff |
| 🛑 Recursão limite | DEC↔COR > 3 ciclos · ESCALADA HUMANA (RGO-7) |

### 11.2 · Gates por bloqueio constitucional (POP §8.2 · estado atual)

| Gate | Sprint | Critério para abrir | Libera |
|---|---|---|---|
| Gate D003 | S2.5 | Stack validado Camila + cotações cloud BR + POC fine-tune | S3.0 |
| Gate D001 | S3.0 | Modelagem custo lastreada + unit economics + pricing | S3.1 BMC |
| Gate D002 | S5.0.5 | Caps 04/07/11 com IN-014 tradução cognitiva | Consolidação |

### 11.3 · Anti-padrão de gate

🚫 Declarar gate aberto sem evidência real · 🚫 pular gate "para acelerar" · 🚫 reabrir gate fechado sem nova decisão registrada (decision log).

---

## §12 · ANTI-PADRÕES ABSOLUTOS (POP §3)

| # | Anti-padrão | Resultado |
|---|---|---|
| AP-01 | Filename `NEOGOV-BP*` ou `CIT-AI-TECH-*` para novo artefato | Confusão com drafts antigos |
| AP-02 | Tratar persona como cluster | Perde behavioral clustering |
| AP-03 | Reescrever conteúdo aprovado BP v2.0 | Quebra rastreabilidade |
| AP-04 | Especular sem tag `[INFERÊNCIA]`/`[ESPECULAÇÃO]` | VVV inflado |
| AP-05 | Fee-for-service como modelo | Não escala · viola DT |
| AP-06 | Esquecer Wave 4 Delta = vitória sem batalha | Perde insight estratégico |
| AP-07 | DT como decoração (não gerador) | DT vira ornamento |
| AP-08 | Frameworks ocidentais isolados | Quebra coerência metodológica |
| AP-09 | Editar artefato sem criar edição antecipada | Perde histórico |
| AP-10 | Apagar/sobrescrever edição anterior | Quebra auditabilidade |
| AP-11 | Inflar VVV inventando fontes | Falência epistêmica |
| AP-12 | Linguagem manufatureira/"IA+ICT" external-facing | Cliente percebe tecnologia como fim |
| AP-13 | **Assumir API IA cloud externa para dado pessoal/legal** | Viola LGPD operacional |
| AP-14 | **Modelar custo antes de definir arquitetura técnica** | Refatoração total |
| AP-15 | **Estimativa sem marcador 🟡 e LASTRO** | Refatoração futura cega |

---

## §13 · TRIPÉ MULTI-OUTPUT (POP §10)

| Formato | Path | Geração | Audiência |
|---|---|---|---|
| **Markdown** (canônico) | `content/{NN}-{nome}-latest.md` | Fonte de verdade (escrita direta) | Git · auditável |
| **Word DOCX** | `NEOGOV-BUSINESS-PLAN-FINAL.docx` | Pandoc + template | Executivos · stakeholders |
| **Vue 3 App** | `app/dist/` (GitHub Pages) | Vite + GitHub Actions | Prospects · público |

**Regra**: Markdown é canônico. Word e Vue são gerados a partir dele. **Nunca o inverso.**

---

## §14 · ESTRUTURA DE DIRETÓRIOS CONSOLIDADA

```
./                                                ← RAIZ (apenas -latest aqui)
├── ARQUITETURA-PROCESSO-NEOGOV-latest.md         ← cópia (ESTE)
├── INSTRUCAO-PROTOCOLO-OPERACIONAL-NEOGOV-latest.md
├── PROTOCOLO_OPERACIONAL_PADRAO.md               ← OMNI v3.0 (referência externa)
├── SESSION-STATE-latest.md
├── APENDICE-A-VVV-LOG-latest.md
├── APENDICE-B-DECISIONS-LOG-latest.md
├── APENDICE-C-INSIGHTS-CARRY-latest.md
├── APENDICE-E-LASTREAMENTO-latest.md
├── {NN}-{capitulo}-latest.md                     ← capítulos BP
├── SPRINT-X.X.X-latest.md                        ← sprints
├── BLUEPRINT-ALINHAMENTO-SOCIETARIO-PROLABORES-latest.md
├── NEOGOV-BUSINESS-PLAN-FINAL.{md,docx}          ← BP v2.0 aprovado
├── NEOGOV-DATA-v2.json                           ← dados estruturados
├── CLAUDE.md                                     ← guidance para Claude Code
│
├── ARQUITETURA-PROCESSO-NEOGOV/                  ← histórico versionado
│   └── ARQUITETURA-PROCESSO-NEOGOV-v1.GOV.1.md
│
├── SESSION-STATE/                                ← histórico WAL
│   └── SESSION-STATE-v2.1.X.X.md
│
├── APENDICE-A-VVV-LOG/                           ← histórico VVV
├── APENDICE-B-DECISIONS-LOG/                     ← histórico decisões
├── APENDICE-C-INSIGHTS-CARRY/                    ← histórico insights
├── APENDICE-E-LASTREAMENTO/                      ← histórico lastros
│
├── CONTINUIDADE/                                 ← histórico capítulos+sprints
│   ├── {NN}-{capitulo}-vX.X.X.md
│   └── SPRINT-X.X.X-vX.X.md
│
├── DEBITO/                                       ← débitos técnicos
│   ├── DEBITO-D001-PRICING-FRAMEWORK-vX.X.X.md
│   ├── DEBITO-D002-AUDITORIA-COGNITIVA-vX.X.X.md
│   └── DEBITO-D003-ARQUITETURA-AGENTIC-SOBERANA-vX.X.X.md
│
├── skills/                                       ← módulos cognitivos
│   ├── ENGINE-MODULES/
│   │   ├── COGNITIVE_ARCHITECTURE_COMPLETE.md
│   │   ├── HOLISTIC_ITERATIVE_QUALITY_MODULE_v1.0.md
│   │   ├── STRATEGIC-ACTION-ENGINE-v4.0.md
│   │   ├── MODULO-DOCUMENTACAO-TECNICA-v1.0.md
│   │   └── MODULO-PESQUISA-SISTEMATICA-v1.md
│   ├── SHUN_TZU-ART_OF_WAR/
│   │   └── MEEST-AE_v2.1.md
│   └── .omc/                                     ← OMC sessions+state
│
└── .archives-memoria/                            ← drafts antigos
```

---

## §15 · CHECKLIST DE ATIVAÇÃO (pré-sprint · POP §14 + OMNI §11)

```
PRÉ-EXECUÇÃO (ler · não executar nada antes)
[ ] Constitution checksum verificado
[ ] Hash de continuidade ATIVO em SESSION-STATE-latest.md conferido
[ ] Mandatos absolutos §2 relembrados (proibições + imperativos + RGO)
[ ] Fontes canônicas (POP §2) disponíveis
[ ] Anti-padrões §12 mentalmente carregados
[ ] WAL inicializado · recursion_depth = 0
[ ] KDI executado (ou recuperado do WAL) com KDI_SCORE ≥ 9.5

DURANTE EXECUÇÃO
[ ] Sistema marcadores §10 aplicado em estimativas
[ ] Padrão versionamento §9 aplicado em edits (./FILENAME/ + latest)
[ ] Mandato IA Própria honrado (POP §6) se sprint envolve técnica
[ ] D-015 §10.4 aplicado em toda estimativa por análogo
[ ] Fila DTP §11.2 conferida (próximo sprint correto)
[ ] PIER → PEII-LLM → PMQS §6 seguido

ENTREGA
[ ] PMQS_bruto calculado · VVV calculado · PMQS_final ≥ 8.0
[ ] 4 camadas continuidade §8 incrementadas
[ ] WAL.commit executado · hash atualizado
[ ] Gate §11.2 conferido (se for bloqueio)
[ ] Decision Log com rationale registrado
```

---

## §16 · GLOSSÁRIO CONSOLIDADO

| Sigla | Significado | Origem |
|---|---|---|
| ARQ-PROC | Arquitetura de Processo (este documento) | NEW |
| BP | Business Plan | POP |
| BMC | Business Model Canvas | POP |
| CAC | Customer Acquisition Cost | POP |
| CAPEX | Capital Expenditure | POP |
| CM | Check-Mate (camada correção) | POP+OMNI |
| CoT | Chain of Thought | OMNI |
| CTO | Chief Technology Officer (Camila) | POP |
| DAG | Directed Acyclic Graph (dependências) | OMNI |
| DEC | Decision Layer (camada decisão) | OMNI |
| DPIER | Deep PIER (ampliação de horizontes) | OMNI |
| DT | Design Thinking | POP |
| DTP | Decision Topology Protocol | POP+OMNI |
| DTS | Dynamic Tool Selector | MEEST-AE |
| EXEC | Execution Layer | OMNI |
| FDC-U | Framework Decisional de Cluster | POP |
| GAP | Knowledge Gap | POP |
| GTM | Go-to-Market | POP |
| HIQM | Holistic Iterative Quality Module | ENGINE |
| ICT | Instituição Científica e Tecnológica (Art. 75 IV Lei 14.133) | POP |
| IN | Insight | POP |
| JTBD | Jobs to Be Done | POP |
| KDI | Knowledge Discovery & Injection | OMNI |
| LAI | Lei de Acesso à Informação (Lei 12.527/2011) | POP |
| LGPD | Lei Geral de Proteção de Dados (Lei 13.709/2018) | POP |
| LLM | Large Language Model | POP |
| LoRA / QLoRA / DoRA | Técnicas de fine-tuning | POP |
| LTV | Lifetime Value | POP |
| MEEST-AE | Módulo Estratégico Sun Tzu Aplicação Empresarial | MEEST |
| MDT | Módulo de Documentação Técnica | ENGINE |
| MO | Modus Operandi (camada execução) | OMNI |
| MSP | Módulo de Segmentação e Personas | MEEST |
| NMS | Newton/Miller/Smith extension (Van Westendorp) | POP |
| OMNI | Documento `PROTOCOLO_OPERACIONAL_PADRAO.md` v3.0 | OMNI |
| OPEX | Operational Expenditure | POP |
| OPP | Optimal Price Point | POP |
| PIER | Production with Iterative Excellence | POP+OMNI |
| PMC | Point of Marginal Cheapness | POP |
| PME | Point of Marginal Expensiveness | POP |
| PMQS | Production · Maturity · Quality · Score | POP+OMNI |
| PNCP | Portal Nacional de Contratações Públicas | POP |
| POC | Proof of Concept | POP |
| POP | Protocolo Operacional NeoGov v2.1.1.1 | POP |
| RGO | Regra de Ouro | POP+OMNI |
| SAE | Strategic Action Engine | ENGINE |
| SaaS | Software as a Service | POP |
| TCE | Tribunal de Contas do Estado | POP |
| TCU | Tribunal de Contas da União | POP |
| VMV | Visão · Missão · Valores | POP |
| VPC | Value Proposition Canvas | POP |
| VVV | Validation · Verification · Veracity (multiplicador 0-1) | POP+OMNI |
| WAL | Write-Ahead Log | POP+OMNI |
| WTP | Willingness To Pay | POP |

---

## §17 · CHANGELOG DESTE DOCUMENTO

| Versão | Data | Mudança |
|---|---|---|
| v1.GOV.1 | 2026-05-15 | Versão inicial · unifica OMNI v3.0 ⊕ POP v2.1.1.1 · incorpora regra de diretório `./FILENAME/` + `-latest` na raiz |

---

## §18 · PRÓXIMAS AÇÕES SUGERIDAS

Estado atual conhecido (do `SESSION-STATE-latest.md`):
- Hash: `NEOGOV-V21-S3.0.3-v1.0-WTP-PROTOCOL-READY-FOR-EXECUTION-BLUEPRINT-BAS-DOCUMENTED`
- Sprint atual: **S3.0.3 v1.0** entregue
- Bloqueios constitucionais ativos: S2.5 (D003) → S3.0 (D001) → S5.0.5 (D002)

Próximo passo recomendado pelo POP §8 (aguarda input usuário):
1. Disparar S3.0.3 execução real (Wilton — 30 dias)
2. Disparar S2.5 D003 em paralelo (Camila — 10-15 dias)
3. Reunião societária S3.0.2 (Simone — Blueprint BAS)
4. Outro artefato book final (sumário executivo, plano implementação, etc.)
5. APENDICE-D xlsx com lastros atuais

---

**FIM DA ARQUITETURA DE PROCESSO**

Este documento é subordinado ao POP §1 (Constitution NeoGov). Em conflito com OMNI v3.0, POP vence. Em complementaridade, ambos se somam.

`ARQ-PROC-v1.GOV.1 · ATIVO · GOVERNANCE`

---

## Sources

- [FILE: INSTRUCAO-PROTOCOLO-OPERACIONAL-NEOGOV-latest.md:L1-L609] — POP v2.1.1.1 master (constituição, fontes, versionamento, marcadores, mandato D003, fila DTP, 4 camadas, PMQS, gates, anti-padrões)
- [FILE: PROTOCOLO_OPERACIONAL_PADRAO.md:L1-L1275] — OMNI v3.0 (Constitution, KDI, TOOL_REGISTRY, SKILL_LIBRARY, WAL_INTERFACE, SCORING_ENGINE, PROTOCOLO_OMNI DEC/EXEC/COR, critérios de parada, checklist ativação)
- [FILE: SESSION-STATE-latest.md:L1-L255] — estado atual S3.0.3 + hash + bloqueios constitucionais + 10 lastros estabelecidos
- [FILE: skills/ENGINE-MODULES/COGNITIVE_ARCHITECTURE_COMPLETE.md:L1-L259] — engine S→Q→I→A · Layer 0/0.5/1/2 · QUALITY_CoT
- [FILE: skills/ENGINE-MODULES/HOLISTIC_ITERATIVE_QUALITY_MODULE_v1.0.md:L1-L60] — HIQM ≥95% iterativo
- [FILE: skills/ENGINE-MODULES/STRATEGIC-ACTION-ENGINE-v4.0.md:L1-L80] — SAE quantificado (SWOT matricial + 5Whys + 5W1H)
- [FILE: skills/ENGINE-MODULES/MODULO-DOCUMENTACAO-TECNICA-v1.0.md:L1-L100] — MDT PIER+chunks+meta-audit
- [FILE: skills/SHUN_TZU-ART_OF_WAR/MEEST-AE_v2.1.md:L1-L80] — MEEST-AE v2.1 (engine completa + MSP segmentação)
- [FILE: APENDICE-E-LASTREAMENTO-latest.md:L1-L120] — convenções de flags D-015 e lastreamento
- [FILE: DEBITO/DEBITO-D003-ARQUITETURA-AGENTIC-SOBERANA-v2.1.4.5.md:L1-L80] — mandato IA Própria D003 v2
- [INFERRED: from `ls` da raiz + subpastas] — estrutura atual de diretórios e padrão de cópias `-latest`
