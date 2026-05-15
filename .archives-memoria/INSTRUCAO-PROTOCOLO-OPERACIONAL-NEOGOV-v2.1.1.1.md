---
id: NEOGOV-V21-PROTOCOLO-OPERACIONAL
filename: INSTRUCAO-PROTOCOLO-OPERACIONAL-NEOGOV-v2.1.1.1.md
alias: PROTOCOLO-OPERACIONAL-NEOGOV
created_at: 2026-05-15T15:00:00Z
type: GOVERNANCE_MASTER_DOCUMENT
designation: POP
function: GOVERNANCE_NEOGOV_PROJECT
parent_system: NeoGov BP v2.1 production
paradigm: S→Q→I→A_GOVERNANCE
integrates_with:
  - HIQM (qualidade consciente)
  - DTP (decisão topológica)
  - MO (modus operandi)
  - CM (check-mate)
  - WAL (continuidade)
  - SCORING_ENGINE (PMQS + VVV)
status: ACTIVE
authority: PROJECT_CONSTITUTION
supersedes: implícito em SESSION-STATE-v2.1.4.6
purpose: Documento ÚNICO de governance que consolida TODOS os mandatos NeoGov + lições aprendidas até ed.S3.0.1-INV
tags: [protocolo, governanca, neogov, master, lessons-learned, ia-propria, lastro, versionamento]
quality_score: registrado em produção
cot_score: 8.5/10
traces_available: [S,Q,I,A]
---

# 📜 Protocolo Operacional NeoGov BP v2.1 · GOVERNANCE MASTER

> Este documento é o **único** ponto de verdade para protocolo do projeto NeoGov v2.1.  
> Sobrescreve qualquer instrução conflitante anterior. SESSION-STATE refere-se a este documento.  
> Atualizar via padrão de versionamento mandatório (§5).

---

## 0 · ÍNDICE FUNCIONAL

| Seção | Tópico | Quando consultar |
|---|---|---|
| §1 | Constituição NeoGov (mandatos absolutos) | Antes de qualquer execução |
| §2 | Fontes canônicas hierárquicas | Antes de citar/inferir dado |
| §3 | Anti-padrões absolutos (proibidos) | Durante decisão de design/redação |
| §4 | Sistema de cores e marcadores visuais | Em toda estimativa/inferência |
| §5 | Padrão de versionamento (PROTOCOLO PERMANENTE) | Em toda edição de artefato |
| §6 | **Mandato Técnico IA Própria** (CRÍTICO) | Em qualquer modelagem de produto/custo |
| §7 | **D-015 Estimativa por Análogo com Lastro** (CRÍTICO) | Em qualquer estimativa numérica |
| §8 | Fila DTP corrigida (sequência bloqueante) | Para decidir próxima ação |
| §9 | Sistema de continuidade 4 camadas | Para localizar estado/decisão/insight |
| §10 | Tripé multi-output (entrega final) | Em consolidação |
| §11 | Workflow operacional (PIER · PEII-LLM · PMQS) | Em cada sprint |
| §12 | Gates e critérios de parada | Para validar conclusão de sprint |
| §13 | Apêndice · Hash de continuidade vigente | Para identificar estado atual |

---

## §1 · CONSTITUIÇÃO NEOGOV (mandatos absolutos)

### 1.1 · Proibições universais (Artigo 1)

```
🚫 NUNCA execute sem analisar CENÁRIO ATUAL e PLANEJAR (5W1H)
🚫 NUNCA execute sem resolver dependências primeiro
🚫 NUNCA siga plano obsoleto → re-avaliar após cada ação
🚫 NUNCA decida sem dados → INVESTIGAÇÃO precede decisão
🚫 NUNCA atue em DÚVIDA · NUNCA CHUTE
🚫 NUNCA gere PMQS inflado · VVV inflado · ou estimativa sem marcador 🟡
🚫 NUNCA assuma API externa de IA para dado pessoal/legal NeoGov
🚫 NUNCA modele custo antes de definir arquitetura técnica
```

### 1.2 · Imperativos universais (Artigo 2)

```
✅ SEMPRE enumere TODOS os caminhos antes de escolher
✅ SEMPRE respeite ordem topológica (dependências)
✅ SEMPRE re-avalie campo após cada execução
✅ SEMPRE INVESTIGUE, COLETE INFORMAÇÕES, PESQUISE
✅ SEMPRE priorize soluções SOTA 2026 + fundamentos estáveis validados
✅ SEMPRE dispatch para protocolo correto conforme estado atual
✅ SEMPRE marque estimativa com 🟡 e crie LASTRO rastreável (§7)
✅ SEMPRE versione artefato com edição antecipada (§5)
```

### 1.3 · Regras de ouro NeoGov

```
🔶 RGO-1 · Cada execução MUDA o campo → re-avaliar ANTES da próxima
🔶 RGO-2 · Nenhuma task é "done" sem EVIDÊNCIA REAL
🔶 RGO-3 · Minimizar refatoração = decidir na ordem certa
🔶 RGO-4 · Maximizar qualidade = não construir sobre base instável
🔶 RGO-5 · Honestidade Epistêmica supera Aparência de Completude
🔶 RGO-6 · Auditabilidade Reversa: toda decisão deve ser rastreável
🔶 RGO-7 · Tradução cognitiva técnico→benefício (IN-014 · D-012)
🔶 RGO-8 · Modelo de IA é OBJETO DE PRODUTO (mandato §6)
```

---

## §2 · FONTES CANÔNICAS (hierarquia de autoridade)

Ordem decrescente · em conflito vence a de cima.

| Rank | Fonte | Path | VVV |
|---|---|---|---:|
| 1 | Lógica geradora DT (inst-lgpd.md) | `/mnt/user-data/uploads/inst-lgpd.md` | 1.00 |
| 2 | SESSION-STATE-latest | `continuity/SESSION-STATE-latest.md` | 1.00 |
| 3 | Este protocolo (POP-latest) | `continuity/INSTRUCAO-PROTOCOLO-OPERACIONAL-NEOGOV-latest.md` | 1.00 |
| 4 | BP v2.0 aprovado | `/mnt/user-data/uploads/NEOGOV-BUSINESS-PLAN-FINAL.{docx,md}` | 1.00 |
| 5 | DATA v2 estruturado | `/mnt/user-data/uploads/NEOGOV-DATA-v2.json` | 0.95 |
| 6 | Transcrição reunião primária | `/mnt/user-data/uploads/transcricao-reuniao-neogov.txt` | 1.00 |
| 7 | Anexos vivos (A/B/C) | `anexos/APENDICE-{A,B,C}-latest.md` | 1.00 |
| 8 | Débitos técnicos D001/D002/D003 | `continuity/DEBITO-D00X-*.md` | 1.00 |
| 9 | Capítulos -latest (04, 07, 11, 02) | `content/{NN}-{nome}-latest.md` | 0.85-0.92 |
| 10 | Drafts NEOGOV-* (legados v2.0) | `/mnt/user-data/uploads/NEOGOV-*` | INSUMO ONLY |

**Regra**: drafts `NEOGOV-BSC-*`, `NEOGOV-FDCU-*`, `NEOGOV-02.5/02.6/02.7` são **insumos de iteração**, NÃO fontes operacionais. Não citá-los como autoridade.

---

## §3 · ANTI-PADRÕES ABSOLUTOS (proibidos)

| # | Anti-padrão | Origem da lição | Resultado se violado |
|---|---|---|---|
| AP-01 | Filename `NEOGOV-BP*` ou `CIT-AI-TECH-*` para novo artefato | Memória recente | Confusão com drafts antigos |
| AP-02 | Tratar persona como cluster | Iteração 02.5→02.6 | Perde behavioral clustering |
| AP-03 | Reescrever conteúdo aprovado BP v2.0 | Continuidade contratual | Quebra rastreabilidade |
| AP-04 | Especular sem tag `[INFERÊNCIA]` ou `[ESPECULAÇÃO]` | Constitution L0 | VVV inflado · perda epistêmica |
| AP-05 | Fee-for-service como modelo | Camila CTO transcrição | Não escala · viola DT industrial |
| AP-06 | Esquecer Wave 4 Delta = vitória sem batalha | Sun Tzu Cap III §3 | Perde insight estratégico |
| AP-07 | DT como decoração (não gerador) | Iteração 02.7→04 v2.1 | DT vira ornamento · inútil |
| AP-08 | Frameworks ocidentais isolados | D-005 keystone | Quebra coerência metodológica |
| AP-09 | Editar artefato sem criar edição antecipada | §5 versionamento | Perde histórico · risco race |
| AP-10 | Apagar/sobrescrever edição anterior | §5 versionamento | Quebra auditabilidade |
| AP-11 | Inflar VVV inventando fontes | D-007 PMQS realista | Auto-engano · falência epistêmica |
| AP-12 | Linguagem manufatureira/"IA+ICT" external-facing | D-012 retificação cognitiva | Cliente percebe tecnologia como fim |
| AP-13 | **Assumir API IA cloud externa para dado pessoal/legal** | **D003 v1 invalidado** | **Viola LGPD operacional · contradição fatal** |
| AP-14 | **Modelar custo antes de definir arquitetura técnica** | **S3.0.1 v1.0 invalidado · D-014** | **Refatoração total · CAPEX errado** |
| AP-15 | **Estimativa sem marcador visual 🟡 e LASTRO** | **D-015 emergente** | **Refatoração futura cega** |

---

## §4 · SISTEMA DE CORES E MARCADORES VISUAIS (D-015)

Toda afirmação numérica/quantitativa em qualquer artefato NeoGov DEVE usar este sistema.

| Marcador | Tipo | VVV equivalente | Ação | Quando refatorar |
|---|---|---:|---|---|
| ✅ Verde | FATO · fonte primária verificada | 0.90-1.00 | Usar livre | Não precisa (revalidar anualmente) |
| 🟢 Verde-escuro | INFERÊNCIA com base em fato | 0.80-0.89 | Usar com tag `[INFERÊNCIA]` | Quando contexto mudar |
| 🟡 Amarelo | **ESTIMATIVA POR ANÁLOGO** | 0.60-0.79 | Usar com tag + LASTRO | **Quando dado primário chegar** |
| 🟠 Laranja | ESPECULAÇÃO fundamentada | 0.40-0.59 | Usar com tag `[ESPECULAÇÃO]` | Urgência alta |
| 🔴 Vermelho | ESPECULAÇÃO sem base | <0.40 | **NÃO USAR** | Refatorar antes de qualquer uso |

**Aplicação obrigatória em**: tabelas de custo, projeções financeiras, estimativas de mercado, métricas de unit economics, prazos, volumes, percentuais.

**Não se aplica em**: citações literais de leis (são FATO), dados de fonte primária (FATO), princípios qualitativos sem número.

---

## §5 · PADRÃO DE VERSIONAMENTO (PROTOCOLO PERMANENTE · MANDATÓRIO)

### 5.1 · Sintaxe

```
{filename}-v[N].{SPRINT}.{EDICAO}.{ext}     ← versionado, imutável
{filename}-latest.{ext}                       ← cópia da última edição
```

### 5.2 · Componentes

| Componente | Regra |
|---|---|
| `v[N]` | Versão maior do ARTEFATO (não muda durante release · ex: v2.x) |
| `SPRINT` | Sprint atual (1.1, 1.2, 2.1, 3.0.1...) |
| `EDICAO` | Contador incremental dentro do sprint, começa em 1 |
| `latest` | Cópia que SEMPRE aponta para a edição mais recente |

### 5.3 · Regra crítica

> A edição seguinte é criada ANTES de receber edits.  
> Cria-se primeiro `{file}-v2.X.Y.{ext}` (vazio ou cópia da anterior), recebe edits nele, e ATUALIZA `{file}-latest.{ext}`.

Garante:
- **Histórico imutável** · toda edição anterior preservada
- **Rastreabilidade** · qualquer leitor pega `-latest` e tem garantia da versão mais recente
- **Reversibilidade** · qualquer edição anterior recuperável
- **Atomicidade** · sem race condition entre edits

### 5.4 · Reescrita estratégica

```
└─ Em edições PEQUENAS ou LOCAIS → priorizar EDIT no original (patch)
└─ Se custo > benefício (alterações relevantes) → REESCRITA + nova edição
```

### 5.5 · Aplicação

Aplica-se a TODOS artefatos em: `content/`, `anexos/`, `continuity/`, `data/`, `app/`.

---

## §6 · MANDATO TÉCNICO IA PRÓPRIA (D003 v2 · CRÍTICO INEGOCIÁVEL)

### 6.1 · Texto literal do mandato (preservado)

> "O modelo de LLM deve ser **MANDATORIAMENTE LOCAL, PRÓPRIO, TREINADO PELA EQUIPE**, garantindo a legalidade exigida pela LEI que é inclusive **OBJETO DE PRODUTO**"  
> "A precificação deve ser **arquitetura + infra pra treino e uso da LLM** → cálculo de custo → entendendo que o modelo LLM não necessitará de knowledge em **áreas não-relevantes**, mas **treino mais especializado em área de aplicação e seus processos**"

### 6.2 · Decodificação operacional

| Princípio | Implicação técnica |
|---|---|
| Local + Próprio + Treinado | Sem API externa (Anthropic, OpenAI, Maritaca Sabiá-4 via API) |
| Objeto de produto | O modelo treinado É o ativo de produto vendido · especialização embarcada |
| Especialização > Tamanho | 7B-13B fine-tunado em domínio supera 70B generalista em tarefa específica |
| Custo = Arquitetura + Treino + Operação | Modelagem D001 deve incluir CAPEX + OPEX + amortização |
| Não-relevância ignorada | Não treinar em cultura geral, programação não-jurídica, idiomas extras |

### 6.3 · Stack mandatado (D003 v2)

| Camada | Decisão | VVV |
|---|---|---:|
| Base model | Llama 3.1 8B (open-weights · licença comercial) | 0.85 |
| Fallback maior | Llama 3.3 70B QLoRA | 0.80 |
| Fine-tuning | QLoRA + DoRA + Unsloth | 0.90 |
| Adapters | 1 base + N LoRA (1 por agente · ~100MB cada) | 0.85 |
| Embeddings | bge-m3 fine-tunado em corpus jurídico BR | 0.80 |
| Vector DB | Qdrant on-premise | 0.90 |
| Framework agentic | LangGraph | 0.85 |
| Inferência | vLLM + GGUF Q4_K_M | 0.85 |
| Orquestração | Kubernetes + Argo Workflows | 0.85 |
| Observability | Langfuse self-hosted | 0.85 |
| Cloud | Magalu / TIVIT / Locaweb / HostDime BR | 0.70-0.85 |

### 6.4 · Tiers de deploy (todos 100% próprios)

| Tier | Uso | Infra | Custo/cliente/mês 🟡 |
|---|---|---|---:|
| A · Compartilhada | Gamma escola privada + pequenos | 1× L40S 48GB cloud BR · multi-adapter | R$ 200-500 |
| B · Dedicada | B2G Alfa + médios | 1× L40S dedicada OU MIG H100 | R$ 1.500-4.000 |
| C · On-premise | Beta saúde + B2G federal sensível | Cliente fornece OU NeoGov instala | Setup R$ 80-300k + R$ 3-15k/mês |

Detalhamento completo: `continuity/DEBITO-D003-ARQUITETURA-AGENTIC-SOBERANA-latest.md`.

### 6.5 · Quando aplicar este mandato

- ✅ Em qualquer modelagem de custo de produto NeoGov
- ✅ Em qualquer capítulo do BP que mencione tecnologia (Cap 11, 12, 15)
- ✅ Em qualquer apresentação a stakeholder (investidor, B2G, parceiro)
- ✅ Em qualquer decisão de compra/contrato de infra
- ❌ NÃO substituir por API externa "por simplicidade" ou "MVP rápido"

---

## §7 · D-015 · ESTIMATIVA POR ANÁLOGO COM LASTRO (PADRÃO TRANSVERSAL OBRIGATÓRIO)

### 7.1 · Origem

> "Buscar análogo/alternativo com características parecidas (tamanho, uso) para estimar [ressaltando em cores e alertas a estimativa] e o que deve ser feito para sanar → memorizar lastrear o dado para que na alteração já facilite a refatoração do cálculo" (usuário · 2026-05-15)

### 7.2 · Convenção visual (3 marcadores obrigatórios)

Toda estimativa baseada em análogo (não dado primário) deve ter:

1. **🟡 Emoji amarelo** antes do número/célula
2. **`[ESTIMATIVA POR ANÁLOGO]`** ou `[ESTIMATIVA]` ao lado
3. **Lastro rastreável** em seção §LASTROS do documento (ou anexo D)

### 7.3 · Anatomia do lastro (formato padrão)

```yaml
LASTRO-XX:
  campo_lastreado: "Custo L40S cloud BR R$ 8.000-15.000/mês"
  marcador: 🟡 ESTIMATIVA POR ANÁLOGO
  vvv: 0.70
  
  analogo_usado:
    fonte: "HostDime BR · servidor com GPU para IA · post fev/2026"
    url: "https://www.hostdime.com.br/blog/..."
    valor_observado: "L40S aluguel benchmark BR similar"
    adaptacao: "+15% para colocation premium + redundância"
  
  dado_primario_necessario:
    o_que: "Cotação real Magalu/TIVIT/Locaweb para L40S 48GB 24/7"
    como_obter: "Solicitar cotação direta 3 provedores BR"
    quem_executa: "Camila CTO · GAP-CAMILA-02"
    sprint_destino: "S2.5.3 · Validar cloud soberana"
  
  refatoracao_facilitada:
    formula: "custo_mensal = preco_gpu_hora × 720 × 1.15 + storage + bandwidth"
    variaveis_lastreadas:
      - preco_gpu_hora: VARIÁVEL ALTERÁVEL (default: 14.50 → cotar)
      - taxa_overhead: 1.15
      - storage_mensal: VARIÁVEL (default: R$ 800 → cotar)
    
    impacto_se_mudar: "Componente afeta TODOS os 5 produtos via OPEX rateado"
    documentos_a_atualizar:
      - "SPRINT-3.0.1 §custo OPEX"
      - "APENDICE-D-MODELO-CUSTO.xlsx"
      - "Cap 11 §pricing"
```

### 7.4 · Honra a princípios

| Honra | Princípio |
|---|---|
| Valor 1 | Honestidade Epistêmica |
| Valor 5 | Auditabilidade Reversa |
| RGO-1 | Re-avaliar campo após cada ação |
| RGO-2 | Evidência real, não aparente |
| D-007 | Não inflar VVV |

### 7.5 · Aplicação retroativa obrigatória

Antes de refazer qualquer sprint, **auditar células do anterior** e classificar com sistema de cores §4. Qualquer 🔴 deve ser refatorada antes do uso.

---

## §8 · FILA DTP CORRIGIDA (sequência bloqueante)

### 8.1 · Estado atual (hash · ATIVO)

```
NEOGOV-V21-S3.0.1-INVALIDADO+D003-V2-IA-PROPRIA-AWAIT-S2.5
```

### 8.2 · Bloqueios constitucionais (resolver antes de prosseguir)

```
═══════════════════════════════════════════════════════════
🛑 BLOQUEIO CONSTITUCIONAL · ordem obrigatória
═══════════════════════════════════════════════════════════

🥇 PRÓXIMO · Sprint 2.5 · Quitar D003 v2 (CRITICAL)
   ├─ S2.5.1 → Validar stack com Camila CTO (GAP-CAMILA-01)
   ├─ S2.5.2 → POC fine-tune Llama 3.1 8B (corpus LGPD pequeno · ~R$ 50)
   ├─ S2.5.3 → Cotações REAIS cloud BR (Magalu/TIVIT/Locaweb/HostDime)
   │            (substitui 🟡 amarelos por ✅ verdes)
   ├─ S2.5.4 → Arquitetura 3-tier final + custos lastreados
   ├─ S2.5.5 → Cap 11 §arquitetura adicionado como diferencial competitivo
   Gate 2.5 · D003 v2 quitado ✅

🥈 Em seguida · Sprint 3.0 · Quitar D001 (CRITICAL)
   ├─ S3.0.1-redo → Modelagem custo bottom-up com IA SOBERANA
   │   ├─ CAPEX treino dos modelos (1 vez · amortizado)
   │   ├─ OPEX infra recorrente (rateado entre clientes)
   │   ├─ Custo humano (jurídico + DevOps + suporte)
   │   └─ Custo aquisição (CAC) e onboarding
   ├─ S3.0.2 → Unit economics (LTV/CAC/Payback) · 20 combos persona×produto
   ├─ S3.0.3 → Pricing assertivo · margem alvo 80-92% (realista com IA própria)
   ├─ S3.0.4 → APENDICE-D-MODELO-CUSTO.xlsx · planilha viva 5 abas
   └─ S3.0.5 → Retificar Cap 11 §pricing (VVV 0.65 → 0.85+)
   Gate 3.0 · D001 quitado ✅

🥉 Em seguida · Sprint 5.0.5 · Quitar D002 (MEDIUM)
   └─ Auditoria cognitiva Caps 04/07/11 (aplicar IN-014 surgically)
   Gate 5.0.5 · D002 quitado ✅

═══════════════════════════════════════════════════════════
✅ PORTÃO ABERTO · plano principal retoma
═══════════════════════════════════════════════════════════
```

### 8.3 · Plano principal pós-portão

```
SPRINT 2 (continuação)
└─ S2.2 → 01-capa-ficha-sumario

SPRINT 3 (BMC + VPC + Porter · com inputs assertivos)
├─ S3.1 → 12-bmc
├─ S3.2 → 13-vpc
└─ S3.3 → 09-porter

SPRINT 4 (operacional)
├─ S4.1 → 16-equipe-governanca
├─ S4.2 → 15-financeiro detalhado
└─ S4.3 → 14-gtm-waves

SPRINT 5 (refinamentos finais)
├─ S5.1 → 08-clusters-fdcu refinar
├─ S5.2 → 05/06/10/17/18 ajustes
└─ S5.3 → 03-sumario-executivo

CONSOLIDAÇÃO
├─ C.1 → BUSINESS-PLAN-FINAL-v2.1.docx
├─ C.2 → modelo financeiro completo XLSX
├─ C.3 → Vue App + GitHub Actions
└─ C.4 → PDF + slides
```

---

## §9 · SISTEMA DE CONTINUIDADE · 4 CAMADAS

| Camada | Documento | Propósito |
|---|---|---|
| **WAL Master** | `continuity/SESSION-STATE-latest.md` | Estado live · hash chain · fila DTP · métricas |
| **VVV Log** | `anexos/APENDICE-A-VVV-LOG-latest.md` | Toda afirmação factual com tag + VVV (53 afirmações) |
| **Decision Log** | `anexos/APENDICE-B-DECISIONS-LOG-latest.md` | Toda decisão com rationale + opções rejeitadas (12 D + 7 herdadas) |
| **Insight Carry** | `anexos/APENDICE-C-INSIGHTS-CARRY-latest.md` | Insights emergentes não-consumidos (14 IN · 7 pendentes) |

### 9.1 · Regra de atualização

Toda execução de sprint atualiza as 4 camadas:
1. WAL Master · novo hash · nova entrada na cadeia
2. VVV Log · novas afirmações registradas
3. Decision Log · novas decisões registradas (se houver)
4. Insight Carry · novos insights registrados (se houver)

### 9.2 · Sync com outputs

`/mnt/user-data/outputs/neogov-v21/{content,anexos,continuity}/` deve refletir `/home/claude/neogov-v21/...` após cada sprint.

---

## §10 · TRIPÉ MULTI-OUTPUT (entrega final)

Toda entrega NeoGov é sincronizada em **3 formatos** (princípio DRY):

| Formato | Path | Geração | Audiência |
|---|---|---|---|
| **Markdown** | `content/{NN}-{nome}-latest.md` | Fonte de verdade (escrita direta) | Git · auditável · editável |
| **Word docx** | `BUSINESS-PLAN-FINAL-v2.1.docx` | Pandoc + template oficial | Executivos · imprensa · stakeholders |
| **Vue 3 App** | `app/dist/` (GitHub Pages) | Vite + GitHub Actions | Demo navegável · prospects · público |

**Regra**: Markdown é canônico. Word e Vue são gerados a partir dele. Nunca o inverso.

---

## §11 · WORKFLOW OPERACIONAL POR SPRINT

### 11.1 · Macro-fluxo (PIER → PEII-LLM → PMQS → Kaizen)

```
[PRE-ALWAYS] Clarificação Socrática
    ↓
[KDI] Knowledge Discovery & Injection (skill seleção)
    ↓
[PIER] Gerar 3-5 abordagens · avaliar · selecionar vencedora
    ↓
[PEII-LLM] 7 fases · refinamento iterativo
    ↓
[PMQS] Validar ≥ 8.0 realista · ≥ 9.5 alvo ouro
    ↓
[VVV] Validar fontes · multiplicador 0.0-1.0
    ↓
[KAIZEN] Registrar aprendizados · padronizar
    ↓
[WAL] Commit · update 4 camadas continuidade · novo hash
```

### 11.2 · PMQS · pesos canônicos NeoGov

| Critério | Peso |
|---|---:|
| CE · Completude e Especificidade | 15% |
| PI · Precisão das Informações | 15% |
| CC · Clareza Cristalina | 10% |
| PRI · Profundidade e Rigor | 20% |
| RA · Relevância Absoluta | 15% |
| EIC · Estrutura e Coerência | 10% |
| OVA · Originalidade e Valor | 15% |
| **VVV** | **Multiplicador 0-1** |

**Alvo realista NeoGov**: PMQS final ≥ **8.0** (D-007 · não inflar)  
**Alvo ouro NeoGov**: PMQS final ≥ **9.5** (pode não ser atingido em todos os sprints)

### 11.3 · Convergência

```
Se PMQS_n >= 9.5 → entrega
Se PMQS_n < 9.5 E (PMQS_n - PMQS_{n-1}) > 3% → refinar
Se PMQS_n < 9.5 E aumento ≤ 3% por 4 iterações → DPIER (ampliar horizontes)
```

---

## §12 · GATES E CRITÉRIOS DE PARADA

### 12.1 · Critérios de parada válidos

| Critério | Condição |
|---|---|
| ✅ Sucesso completo | Progresso == 100% do Objetivo Global AND VVV ≥ 0.85 AND PMQS ≥ 8.0 |
| ⚖️ Custo marginal > Valor marginal | Continuar não justifica o retorno · documentar no WAL |
| ⛔ Bloqueio externo irredutível | Dependência externa não resolvível · gerar WAL-handoff |
| 🛑 Recursão limite | DEC↔COR > 3 ciclos · ESCALADA HUMANA obrigatória |

### 12.2 · Gates por bloqueio

| Gate | Critério para abrir | Após abrir |
|---|---|---|
| Gate D003 (S2.5) | Stack validado por Camila + cotações cloud BR + POC fine-tune executado | Libera S3.0 |
| Gate D001 (S3.0) | Modelagem custo lastreada + unit economics + pricing assertivo | Libera S3.1 BMC |
| Gate D002 (S5.0.5) | Caps 04/07/11 com tradução cognitiva aplicada (IN-014) | Libera consolidação |

### 12.3 · Anti-padrão de gate

🚫 Declarar gate aberto sem evidência real · 🚫 pular gate "para acelerar" · 🚫 reabrir gate fechado sem nova decisão registrada (decision log)

---

## §13 · APÊNDICE · HASH DE CONTINUIDADE VIGENTE

### 13.1 · Cadeia de hashes (auditável)

| Hash | Sprint | Status |
|---|---|---|
| `NEOGOV-V21-S0-INIT-AWAIT-S1.1` | S0 | FECHADO |
| `NEOGOV-V21-S1.1-DONE-AWAIT-S1.2` | S1.1 | FECHADO |
| `NEOGOV-V21-S1.2-DONE-AWAIT-S1.3` | S1.2 | FECHADO |
| `NEOGOV-V21-S1.3-DONE+DEBT-D001-AWAIT-S2.1` | S1.3 | FECHADO |
| `NEOGOV-V21-S2.1-RETIFICADO+DEBT-D001-D002-BLOQUEANTES-AWAIT-RESOLUCAO` | S2.1 | SUPERSEDED |
| `NEOGOV-V21-S3.0.1-MODELAGEM-CUSTO-AWAIT-S3.0.2` | S3.0.1-v1 | INVALIDADO ❌ |
| `NEOGOV-V21-S3.0.1-INVALIDADO+D003-CRITICAL-AWAIT-S2.5` | S3.0.1-INV | SUPERSEDED |
| `NEOGOV-V21-S3.0.1-INVALIDADO+D003-V2-IA-PROPRIA-AWAIT-S2.5` | D003-v2 | **ATIVO** |

### 13.2 · Próxima ação imediata

```
🥇 Aguardar input usuário sobre:
   (1) Confirmar sequenciamento S2.5 antes de S3.0
   (2) Validar este protocolo (POP v2.1.1) como GOVERNANCE MASTER
   (3) Decidir como executar S2.5.1 (precisa de Camila CTO presencial OU avançar com gaps marcados?)
```

---

## §14 · CHECKLIST DE ATIVAÇÃO (antes de qualquer sprint)

```
[ ] Hash de continuidade ATIVO conferido
[ ] Constitution §1 mandatos absolutos relembrados
[ ] Fontes canônicas §2 disponíveis
[ ] Anti-padrões §3 mentalmente carregados
[ ] Sistema de cores §4 será aplicado em estimativas
[ ] Padrão de versionamento §5 será aplicado em edits
[ ] Mandato IA Própria §6 honrado (se sprint envolve modelagem técnica)
[ ] D-015 §7 (estimativa por análogo) será aplicado
[ ] Fila DTP §8 conferida (próximo sprint correto)
[ ] 4 camadas de continuidade §9 prontas para atualização
[ ] Workflow §11 (PIER → PEII-LLM → PMQS) preparado
[ ] Gates §12 conhecidos (não tentar pular)
```

---

## §15 · GLOSSÁRIO DE SIGLAS

| Sigla | Significado |
|---|---|
| BP | Business Plan |
| BMC | Business Model Canvas (Osterwalder) |
| CAC | Customer Acquisition Cost |
| CAPEX | Capital Expenditure (investimento) |
| CM | Check-Mate (protocolo correção) |
| CTO | Chief Technology Officer (Camila) |
| DPA | Data Processing Agreement |
| DT | Design Thinking (IDEO 5 fases) |
| DTP | Decision Topology Protocol |
| ECA | Estatuto da Criança e Adolescente Digital (Lei 15.211/2025) |
| FDC-U | Framework Decisional de Cluster (13 dimensões) |
| GAP | Knowledge Gap (validação externa pendente) |
| GTM | Go-to-Market |
| HIQM | Holistic Iterative Quality Module |
| ICT | Instituição Científica e Tecnológica (Art. 75 IV Lei 14.133) |
| IN | Insight (cabeça do Apêndice C) |
| JTBD | Jobs to Be Done |
| KDI | Knowledge Discovery & Injection |
| LAI | Lei de Acesso à Informação (Lei 12.527/2011) |
| LGPD | Lei Geral de Proteção de Dados (Lei 13.709/2018) |
| LLM | Large Language Model |
| LoRA | Low-Rank Adaptation (técnica fine-tuning) |
| LTV | Lifetime Value |
| MO | Modus Operandi |
| OPEX | Operational Expenditure (custo recorrente) |
| PIER | Production with Iterative Excellence (Product, Interview, Evaluation, Research) |
| PMQS | Production · Maturity · Quality · Score |
| PNCP | Portal Nacional de Contratações Públicas |
| POC | Proof of Concept |
| POP | Protocolo Operacional (este documento) |
| POV | Point of View (DT fase Define) |
| QLoRA | Quantized LoRA |
| RGO | Regra de Ouro |
| SaaS | Software as a Service |
| TCE | Tribunal de Contas do Estado |
| TCU | Tribunal de Contas da União |
| VMV | Visão · Missão · Valores |
| VPC | Value Proposition Canvas (Osterwalder) |
| VVV | Validation · Verification · Veracity |
| WAL | Write-Ahead Log |
| WTP | Willingness To Pay |

---

## §16 · CHANGELOG DESTE PROTOCOLO

| Versão | Data | Mudança |
|---|---|---|
| v2.1.1.1 | 2026-05-15 | Versão inicial consolidada · incorpora D003 v2 + D-015 + lições S3.0.1-INV |

---

**FIM DO PROTOCOLO OPERACIONAL MASTER**

Este documento substitui qualquer instrução conflitante. Em caso de dúvida operacional, consultar §0 ÍNDICE FUNCIONAL.

`POP-v2.1.1.1 · ATIVO · GOVERNANCE`
