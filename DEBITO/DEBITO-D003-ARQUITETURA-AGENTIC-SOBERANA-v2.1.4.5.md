---
id: NEOGOV-V21-DEBITO-D003-ARQUITETURA-V2
filename: DEBITO-D003-ARQUITETURA-AGENTIC-SOBERANA-v2.1.4.5.md
created_at: 2026-05-15
type: TECHNICAL_DEBT_REGISTRY
status: REGISTERED_BLOCKS_D001_V2
sprint_origem: S3.0.1 v1.0 (SUPERSEDED) + reorientação usuário
sprint_destino: S2.5 (NOVO sub-sprint inserido ANTES de S3.0.1-redo)
parent_doc: BUSINESS-PLAN-FINAL-v2.1
purpose: Arquitetura técnica de IA PRÓPRIA, LOCAL, TREINADA, ESPECIALIZADA
priority: CRITICAL · bloqueia D001
relationship_with_D001: D003 deve ser quitado PRIMEIRO
supersedes: DEBITO-D003-ARQUITETURA-AGENTIC-SOBERANA-v2.1.4.4.md
tags: [debito, arquitetura, ia-propria, fine-tuning, soberania-mandataria, agentic, especializacao]
methodological_pattern_emerged: ESTIMATIVA-POR-ANALOGO-COM-LASTRO (registrado para uso transversal)
---

# Débito Técnico D003 v2 · Arquitetura Agentic com IA PRÓPRIA E ESPECIALIZADA

> **Identificado em**: Sprint 3.0.1 edição 1 (post-mortem)
> **Refinado em**: 2026-05-15 (input crítico usuário descartando API externa)
> **Severidade**: CRITICAL · bloqueia D001 inteiro

## 0 · Mandato refinado do usuário (texto literal preservado)

> "tendo em vista o rigoroso e mandatório de contenção e privacidade das informações, o modelo de LLM deve ser **MANDATORIAMENTE LOCAL, PRÓPRIO, TREINADO PELA EQUIPE**, garantindo a legalidade exigida pela LEI que é inclusive **OBJETO DE PRODUTO**"
> 
> "logo a precificação deve ser **arquitetura + infra pra treino e uso da LLM** → cálculo de custo → entendendo que o modelo LLM não necessitará de knowledge em **áreas não-relevantes**, mas **treino mais especializado em área de aplicação e seus processos**"

**Decodificação:**
1. **Local + Próprio + Treinado** = não há espaço para Sabiá-4 via API · não há API externa ponto
2. **Objeto de produto** = o modelo treinado É o ativo de produto · vende-se especialização embarcada
3. **Especialização > Tamanho** = modelo pequeno (7B-13B) fine-tunado em domínio específico bate modelo grande generalista em tarefa específica
4. **Custo = Arquitetura + Treino + Operação** = nova estrutura de modelagem D001

## 1 · O que está OUT (vs D003 v1)

| Item v1 | Status v2 |
|---|---|
| Sabiá-4 via API Maritaca | ❌ DESCARTADO · é serviço terceirizado |
| Tier A "Sabiá-4 via API" | ❌ DESCARTADO · API externa não cabe |
| "Modelo BR já compliance LGPD declarado" | ❌ INSUFICIENTE · NeoGov precisa POSSUIR o modelo |

## 2 · Stack técnico v2 (100% próprio)

### 2.1 · Modelo base e camada de fine-tuning

| Camada | Decisão v2 | Justificativa | VVV |
|---|---|---|---:|
| **Base model** | **Llama 3.1 8B** (open-weights Meta · licença comercial) | Modelo open-source · roda em 1 GPU consumer · 8B fine-tunado em domínio estreito iguala/supera 70B genérico em tarefa específica | 0.85 |
| **Fallback maior** | Llama 3.3 70B (QLoRA) | Quando demandar reasoning complexo · ainda cabe em 1 H100 80GB | 0.80 |
| **Técnica fine-tuning** | **QLoRA + DoRA + Unsloth** | SOTA 2026 · custo ~$30-100 por fine-tune · qualidade ≥90% full fine-tuning | 0.90 |
| **Adapters** | 1 base model + N LoRA adapters (1 por agente) | 1 GPU serve dezenas de adapters · troca via switch de arquivo ~100MB | 0.85 |
| **Embeddings** | bge-m3 fine-tunado em corpus jurídico BR | Multilingual · open-weights · roda local | 0.80 |
| **Vector DB** | Qdrant on-premise | Open-source · escalável · sem dependência externa | 0.90 |
| **Framework agentic** | LangGraph | Durable execution · regulated industries default 2026 | 0.85 |
| **Inferência runtime** | vLLM ou llama.cpp + GGUF Q4_K_M | SOTA inferência local · multi-adapter serving | 0.85 |
| **Orquestração** | Kubernetes + Argo Workflows | Padrão cloud-native portável (cloud BR ou on-premise) | 0.85 |
| **Observability** | Langfuse self-hosted | Open-source · auditável · LGPD-friendly | 0.85 |

### 2.2 · Tiers de deploy v2 (todos 100% próprios)

#### Tier A · Inferência em GPU Compartilhada NeoGov (cloud BR)

- **Uso**: Gamma escola privada + clientes pequenos que aceitam multi-tenancy
- **Infra NeoGov**: 1× NVIDIA L40S 48GB em colocation BR · serve 10-30 clientes via multi-adapter
- **Modelo**: Llama 3.1 8B base + adapter LoRA por agente (4 agentes)
- **Cloud provider**: Magalu / TIVIT / Locaweb (datacenter SP) OU HostDime BR
- **Custo NeoGov por cliente/mês**: 🟡 R$ 200-500 [ESTIMATIVA POR ANÁLOGO · ver §6]

#### Tier B · Inferência em GPU Dedicada NeoGov (cloud BR)

- **Uso**: B2G Alfa + clientes médios que exigem isolamento
- **Infra NeoGov**: 1× L40S 48GB dedicada por cliente OU MIG slice de H100
- **Modelo**: Llama 3.1 8B (default) ou Llama 3.3 70B (clientes complexos)
- **Custo NeoGov por cliente/mês**: 🟡 R$ 1.500-4.000 [ESTIMATIVA POR ANÁLOGO · ver §6]

#### Tier C · On-Premise No Cliente

- **Uso**: Beta saúde (hospital com datacenter) + B2G federal sensível
- **Hardware**: cliente fornece OU NeoGov instala (CAPEX ~R$ 250k servidor L40S)
- **Modelo**: empacotado em container · atualização via VPN da NeoGov
- **Custo cliente**: setup 🟡 R$ 80-300k + manutenção R$ 3-15k/mês [ESTIMATIVA POR ANÁLOGO · ver §6]

### 2.3 · Custo de treino dos modelos (CAPEX inicial NeoGov)

Este é o **investimento NeoGov para criar os modelos próprios** — feito 1 vez, amortizado em todos os clientes.

| Modelo | Dataset estimado | Técnica | GPU-horas | 🟡 Custo cloud [análogo] | Refatorar com |
|---|---|---|---:|---:|---|
| **Agente Data Discovery** | ~50M tokens (corpus LGPD/LAI) | QLoRA r=16 | 30-50h H100 | R$ 800-1.500 | dataset real |
| **Agente Anonimização** | ~100M tokens (jurisprudência + casos) | QLoRA + DoRA | 60-100h H100 | R$ 1.500-3.000 | corpus expandido |
| **Agente AI-DPO Copilot** | ~80M tokens (Q&A LGPD) | QLoRA r=32 | 50-80h H100 | R$ 1.200-2.500 | dataset cliente |
| **Agente Compliance Auditor** | ~60M tokens (regulamentos + auditorias) | QLoRA + DoRA | 40-70h H100 | R$ 1.000-2.000 | jurisprudência real |
| **Embeddings fine-tune** | ~20M tokens | LoRA bge-m3 | 10-20h L40S | R$ 200-500 | corpus consolidado |
| **TOTAL CAPEX treino inicial** | — | — | 190-320h | 🟡 **R$ 4.700-9.500** | **lastros §6** |

**🟡 ALERTA · todas as células marcadas são ESTIMATIVAS POR ANÁLOGO. Lastros e refatoração em §6.**

**Tradução economica:** o custo INTEIRO de criar os 4 modelos especializados NeoGov fica em ~R$ 5-10k. Comparado a "comprar API Anthropic" que custaria isso em 1-3 meses de uso para 50 clientes, é trivial. **Make >> Buy.**

### 2.4 · Custo recorrente de operação (OPEX mensal NeoGov)

Servidor de inferência compartilhado entre todos os clientes Tier A + B:

| Componente | 🟡 Custo mensal estimado | Lastro |
|---|---:|---|
| 1× L40S 48GB cloud BR (24/7) | R$ 8.000-15.000 | benchmark HostDime/Magalu [§6] |
| Banco vector Qdrant (storage + compute) | R$ 800-2.000 | benchmark cloud BR storage |
| Observability Langfuse self-hosted | R$ 300-800 | infraestrutura pequena |
| Backup + redundância | R$ 500-1.500 | padrão cloud BR |
| DevOps/SRE (pleno parcial) | R$ 4.000-7.000 | 0.5 FTE inicial |
| **Subtotal OPEX/mês** | 🟡 **R$ 13.600-26.300** | **lastros §6** |

Capacidade: 1 L40S serve ~50-100 clientes Tier A simultaneamente (carga média) · ~10-20 clientes Tier B com SLA dedicado.

### 2.5 · Estratégia de Treino Especializado (NOVO)

Princípio guia (palavras do usuário): **"modelo LLM não necessitará de knowledge em áreas não-relevantes, mas treino mais especializado em área de aplicação e seus processos"**.

#### 2.5.1 · O que ENSINAR ao modelo (focado)

| Domínio | Fonte de dados | Volume estimado |
|---|---|---:|
| Direito Digital BR | LGPD íntegra + jurisprudência STF/STJ + Acórdãos TCE/TCU | ~30M tokens |
| LAI + interface com LGPD | Lei 12.527/2011 + decisões CGU + ACs federais | ~20M tokens |
| ECA Digital | Lei 15.211/2025 + Decreto regulamentador + casos | ~10M tokens |
| Processos administrativos BR | Lei 14.133/2021 + Lei 8.666 (legado) + provimentos CNJ | ~25M tokens |
| Português jurídico brasileiro | Doutrinas + petições anonimizadas + pareceres ANPD | ~40M tokens |
| Anonimização técnica | Casos de re-identificação + literatura técnica | ~15M tokens |
| Processos NeoGov (proprietário) | Knowledge Simone+Gislênia (templates, decisões reais) | ~20M tokens |

**Total dataset especializado**: ~160M tokens (lean · qualidade > quantidade · regra 2026: 500-2000 exemplos curados > 50k scrappados)

#### 2.5.2 · O que NÃO ensinar (econômico)

- ❌ Conhecimento genérico de cultura geral, ciência, programação não-jurídica
- ❌ Multilingue além de PT-BR
- ❌ Geração criativa (poesia, ficção)
- ❌ Conhecimento histórico não-jurídico
- ❌ Capacidades multimodais (imagem/áudio) — usar modelo separado se precisar

#### 2.5.3 · Pipeline de treino

```
[1] Coleta dataset            (Simone+Gislênia + scraping legal)
       ↓
[2] Cleaning + Q&A formatting (JSONL · ChatML)
       ↓
[3] Train/Val split 80/20
       ↓
[4] QLoRA fine-tune Llama 3.1 8B com Unsloth
       ↓
[5] Eval em conjunto held-out + MMLU para checar degradação geral
       ↓
[6] Merge + quantize para GGUF Q4_K_M (inferência local rápida)
       ↓
[7] Deploy via vLLM com adapter switching
```

### 2.6 · Por que isso é DEFENSIVO (não só conformidade)

| Aspecto | Modelo próprio especializado | API externa Sonnet/GPT-4 |
|---|---|---|
| Dado pessoal sai do BR | NUNCA | Sempre |
| Conformidade LGPD/LAI | Total | Inviável |
| Modelo melhora com uso NeoGov | Sim (ciclo virtuoso) | Não (alimenta concorrente) |
| Knowledge proprietário Simone+Gislênia | Embarcado e protegido | Vaza no prompt |
| Custo marginal por inferência | ~zero após CAPEX | Linear no uso (token cost) |
| Diferencial competitivo | ALTO (Be Compliance/Safetyfyi não tem) | Nenhum (qualquer um compra API) |
| Defensabilidade do produto | Alta | Zero |

## 3 · Padrão metodológico emergente: ESTIMATIVA POR ANÁLOGO COM LASTRO

### 3.1 · Por que registrar isto como padrão permanente

O usuário levantou um princípio que **se aplica TRANSVERSALMENTE** em todo o BP, não só nesta sprint:

> "buscar análogo/alternativo com características parecidas (tamanho, uso) para estimar [ressaltando em cores e alertas a estimativa] e o que deve ser feito para sanar → memorizar lastrear o dado para que na alteração já facilite a refatoração do cálculo"

### 3.2 · Convenção visual obrigatória

Toda estimativa baseada em análogo (não dado primário) deve ter **3 marcadores**:

1. **🟡 Emoji amarelo** antes do número/célula
2. **`[ESTIMATIVA POR ANÁLOGO]`** ou `[ESTIMATIVA]` ao lado
3. **Lastro rastreável** em seção §6 do documento (ou anexo) com:
   - Fonte do análogo (URL, paper, benchmark)
   - Como o análogo foi adaptado (multiplicadores, ajustes)
   - Que dado primário PRECISA SER COLETADO para refatorar
   - Sprint onde a coleta acontecerá (GAP-XX referenciado)

### 3.3 · Convenção de cores expandida (escalada de certeza)

| Marcador | Tipo | VVV equivalente | Quando refatorar |
|---|---|---:|---|
| ✅ Verde | FATO · fonte primária verificada | 0.90-1.00 | Não precisa |
| 🟢 Verde-escuro | INFERÊNCIA com base em fato | 0.80-0.89 | Quando contexto mudar |
| 🟡 Amarelo | **ESTIMATIVA POR ANÁLOGO** | 0.60-0.79 | **Quando dado primário chegar** |
| 🟠 Laranja | ESPECULAÇÃO fundamentada | 0.40-0.59 | Urgência alta |
| 🔴 Vermelho | ESPECULAÇÃO sem base | <0.40 | **NÃO usar · refatorar antes** |

### 3.4 · Anatomia do lastro (formato padrão)

```yaml
LASTRO-XX:
  campo_lastreado: "Custo L40S cloud BR R$ 8.000-15.000/mês"
  marcador: 🟡 ESTIMATIVA POR ANÁLOGO
  vvv: 0.70
  
  analogo_usado:
    fonte: "HostDime BR · servidor com GPU para IA · post fev/2026"
    url: "https://www.hostdime.com.br/blog/servidor-com-gpu-para-ia"
    valor_observado: "L40S aluguel benchmark BR similar"
    adaptacao: "+15% para colocation premium + redundância"
  
  dado_primario_necessario:
    o_que: "Cotação real Magalu/TIVIT/Locaweb para L40S 48GB 24/7"
    como_obter: "Solicitar cotação direta 3 provedores BR"
    quem_executa: "Camila CTO ou GAP-CAMILA-02"
    sprint_destino: "S2.5.3 · Validar cloud soberana"
  
  refatoracao_facilitada:
    formula_armazenada: "custo_mensal = preco_gpu_hora × 720 × 1.15 + storage + bandwidth"
    variaveis_lastreadas:
      - preco_gpu_hora: VARIÁVEL ALTERÁVEL (default: 14.50 → cotar)
      - taxa_overhead: 1.15 (colocation + redundancia)
      - storage_mensal: VARIÁVEL (default: R$ 800 → cotar)
    
    impacto_se_mudar: "Componente afeta TODOS os 5 produtos via OPEX rateado"
    documentos_a_atualizar:
      - "SPRINT-3.0.1-redo-MODELAGEM-CUSTO.md §custo OPEX"
      - "APENDICE-D-MODELO-CUSTO.xlsx (futuro)"
      - "Cap 11 §pricing"
```

### 3.5 · Aplicação retroativa (auditoria S3.0.1 v1.0)

Antes de refazer S3.0.1, **auditar todas as células** e classificar:

| Célula | Marcador retroativo | Ação |
|---|---|---|
| Preços Anthropic API | ✅ FATO (web_search platform.claude.com) | **NÃO PRECISA · será descartado todo o bloco** |
| Salários BR 2026 | ✅ FATO (Glassdoor + Robert Half) | Manter no S3.0.1-redo |
| Encargos CLT 8% | ✅ FATO (calculadorabrasil.com.br) | Manter |
| Cloud SaaS R$ 100-400 | 🟡 ESTIMATIVA POR ANÁLOGO | Refatorar com cotação real BR |
| CAC SaaS B2B R$ 800-30k | 🟡 ESTIMATIVA POR ANÁLOGO | Gap GAP05 + WTP entrevistas |
| Suporte humano min/mês | 🟠 ESPECULAÇÃO | Refatorar pós-piloto Wave 1 |
| Onboarding R$ 1k-8k | 🟡 ESTIMATIVA POR ANÁLOGO | Refatorar com case real |

## 4 · Roadmap atualizado

```
═══════════════════════════════════════════════════
🛑 BLOQUEIOS · resolver antes de prosseguir
═══════════════════════════════════════════════════

🥇 S2.5 · Quitar D003 v2 (CRITICAL · bloqueia D001)
   ├─ S2.5.1 → Validar stack com Camila CTO
   │           (GAP-CAMILA-01: preferências + experiência)
   ├─ S2.5.2 → POC fine-tuning Llama 3.1 8B com corpus LGPD pequeno
   │           (validar viabilidade técnica · 1 weekend de trabalho · ~R$ 50)
   ├─ S2.5.3 → Cotações REAIS cloud BR (Magalu/TIVIT/Locaweb/HostDime)
   │           (substitui 🟡 amarelos por ✅ verdes)
   ├─ S2.5.4 → Definir arquitetura 3-tier final + custos lastreados
   ├─ S2.5.5 → Cap 11 §arquitetura · adicionar como diferencial competitivo
   Gate 2.5 · D003 v2 quitado

🥈 S3.0 · Quitar D001 (com IA própria especializada)
   ├─ S3.0.1-redo → Modelagem custo bottom-up com CAPEX treino + OPEX
   ├─ S3.0.2 → Unit economics
   ├─ S3.0.3 → Pricing assertivo (margem alvo agora REALISTA: 80-92%)
   ├─ S3.0.4 → APENDICE-D xlsx com fórmulas lastreadas
   └─ S3.0.5 → Retificar Cap 11 §pricing
   Gate 3.0 · D001 quitado

🥉 S5.0.5 · Quitar D002 (MEDIUM)
   Gate 5.0.5 · D002 quitado
═══════════════════════════════════════════════════
✅ PORTÃO ABERTO
═══════════════════════════════════════════════════
```

## 5 · Anti-padrões expandidos (lição refinada)

- 🚫 Modelar custo sem definir arquitetura (origem D001 → D003)
- 🚫 Assumir API externa para dado sensível (LGPD)
- 🚫 **Assumir API mesmo BR para domínio que é objeto de produto** (lição refinada)
- 🚫 Modelo grande generalista quando especialização menor basta
- 🚫 Treinar modelo em domínios irrelevantes (consome dataset e computação)
- 🚫 **Estimativa sem marcação visual e lastro** (lição metodológica nova)
- 🚫 Pricing antes de arquitetura

## 6 · LASTROS · seção viva (atualizar antes de cada refatoração)

### LASTRO-01 · Custo L40S cloud BR 24/7

```yaml
campo_lastreado: "Custo L40S cloud BR R$ 8.000-15.000/mês"
marcador: 🟡 ESTIMATIVA POR ANÁLOGO
vvv_atual: 0.70

analogo_usado:
  fonte: HostDime BR (post 12-fev-2026 · 56min leitura · "Servidor com GPU para IA")
  url: https://www.hostdime.com.br/blog/servidor-com-gpu-para-ia-o-que-e-como-funciona-como-escolher
  observacao: L40S é "campeã em eficiência para inferência em escala"
  beneficio_local: latência baixa (~15ms) vs cloud US (~150ms)
  
  fonte_complementar: GPUBrasil
  url2: https://gpubrasil.com.br/
  observacao2: NVIDIA H200/H100/A100/L40 sob demanda em R$ por hora

dado_primario_necessario:
  o_que: Cotação 24/7 dedicada L40S em Magalu Cloud + TIVIT + Locaweb + HostDime
  como_obter: Solicitar 3 cotações para mesma especificação (1× L40S 48GB · 100GB SSD · 1TB transfer/mês)
  quem_executa: Camila CTO via GAP-CAMILA-02 (novo)
  sprint_destino: S2.5.3
  prazo_alvo: 5 dias úteis

refatoracao_facilitada:
  formula:
    custo_mensal_l40s = preco_hora × 720h × overhead_taxa + storage + bandwidth
  
  variaveis:
    preco_hora_default: 14.50  # R$/h estimado (substituir por cotação real)
    overhead_taxa_default: 1.15
    storage_default: 800        # R$/mês
    bandwidth_default: 500      # R$/mês
  
  impacto_se_mudar:
    documentos_afetados:
      - SPRINT-3.0.1-redo (OPEX recorrente)
      - APENDICE-D-MODELO-CUSTO.xlsx
      - Cap 11 §pricing (margem alvo)
    
    produtos_afetados: TODOS (P1, P2, P3, P4, P5)
    estimativa_impacto: se preço real ±30% → margem ±5-8 p.p.
```

### LASTRO-02 · Fine-tune QLoRA 50-100h H100

```yaml
campo_lastreado: "30-100 GPU-horas por agente · R$ 800-3.000 por fine-tune"
marcador: 🟡 ESTIMATIVA POR ANÁLOGO
vvv_atual: 0.85

analogo_usado:
  fonte_1: Calcix · "Llama-3 Fine-Tuning Cost Guide 2026"
  url1: https://calcix.net/guides/business-startup/ai-model-training-cost-guide-llama3
  observacao_1: "$12,500-$45,000 para dataset 500M tokens" (alto end)
  
  fonte_2: Spheron · "How to Fine-Tune LLM 2026"
  url2: https://www.spheron.network/blog/how-to-fine-tune-llm-2026/
  observacao_2: "$20 (R$ 106) para fine-tune 7B em 36h RTX 4090" (low end)
  
  fonte_3: Medium Syntal · "Llama Fine-Tuning Real Costs Oct 2025"
  observacao_3: "H100 cloud especializado $2-3.5/hr · hyperscaler $6-12/hr"
  
  range_calculado:
    minimo: 30h × R$ 15/h = R$ 450     # specialized cloud BR
    central: 60h × R$ 25/h = R$ 1.500   # hyperscaler BR
    maximo: 100h × R$ 30/h = R$ 3.000   # premium pricing

dado_primario_necessario:
  o_que: Executar POC real fine-tune Llama 3.1 8B com corpus LGPD pequeno (10M tokens)
  como_obter: S2.5.2 · alugar 1× RTX 4090 ou A100 por 4-8h · ~R$ 50-100 total
  quem_executa: Camila (CTO) ou consultor IA contratado
  sprint_destino: S2.5.2

refatoracao_facilitada:
  formula:
    custo_finetune = gpu_horas × preco_hora_gpu
  
  variaveis:
    gpu_horas: depende do dataset_tokens e técnica (QLoRA r=16 default)
    preco_hora_gpu: depende do provedor (specialized BR ou hyperscaler)
  
  impacto_se_mudar:
    documento: CAPEX inicial NeoGov (1 vez)
    produtos_afetados: amortização nos 5 produtos
    estimativa_impacto: variação ±100% ainda mantém CAPEX < R$ 15k total · não muda viabilidade
```

### LASTRO-03 · CAC SaaS B2B Brasil (herdado de S3.0.1 v1.0)

```yaml
campo_lastreado: "CAC R$ 800-30.000 dependendo segmento e canal"
marcador: 🟡 ESTIMATIVA POR ANÁLOGO
vvv_atual: 0.65

analogo_usado:
  fonte: Benchmark setor SaaS BR (inferência de múltiplos artigos genéricos)
  problema: Nenhuma fonte primária específica · range muito amplo
  
dado_primario_necessario:
  o_que: CAC real após Wave 1 (12 meses de operação)
  como_obter: medir gasto marketing+vendas / clientes adquiridos
  quem_executa: Wilton (comercial) com CRM
  sprint_destino: pós-M12 (Wave 1 closure)

refatoracao_facilitada:
  status: CAC só pode ser refatorado COM DADO REAL · gap permanece até M12
  alternativa_intermedia: 3-5 entrevistas WTP (GAP02) reduzem range estimativo
```

### LASTRO-04 · Cloud Magalu/TIVIT/Locaweb declaração LGPD

```yaml
campo_lastreado: "Cloud BR declaradamente LGPD-compliant"
marcador: 🟢 INFERÊNCIA com base em fato
vvv_atual: 0.85

analogo_usado:
  fonte_1: Magalu Cloud · case Sysvale (saúde pública)
  url1: https://magalu.cloud/blog/como-a-sysvale-garantiu-soberania-digital-conformidade-com-a-lgpd...
  observacao_1: "dados no Brasil · conformidade LGPD declarada"
  
  fonte_2: TIVIT Private Cloud
  url2: https://cloud.tivit.com/
  observacao_2: "LGPD compliance · residência e soberania · jurisdição total"
  
  fonte_3: Locaweb Cloud · NeoFeed mar/2026
  url3: https://neofeed.com.br/negocios/lwsa-entra-no-jogo-da-nuvem-com-cloud-100-brasileira...
  observacao_3: "data center SP · 50-70% mais barato que big techs"

dado_primario_necessario:
  o_que: Validação contratual (cláusula DPA) com provedor escolhido
  como_obter: Solicitar DPA template · revisar com Simone (jurídico)
  quem_executa: Simone (jurídico) + Camila (técnico)
  sprint_destino: S2.5.3 (cotações) + revisão jurídica
```

### LASTRO-05 · Tier C on-premise CAPEX cliente

```yaml
campo_lastreado: "Setup on-premise R$ 80-300k + manutenção R$ 3-15k/mês"
marcador: 🟡 ESTIMATIVA POR ANÁLOGO
vvv_atual: 0.65

analogo_usado:
  fonte: IntuitionLabs · NVIDIA AI GPU Prices Apr 2026
  url: artigo sobre H100 $27-40k + B200 $30-50k + DGX B300 $300-350k
  observacao: L40S é mais barata · datacenter padrão · custo total típico R$ 250k servidor 1× L40S
  
  componentes_setup:
    servidor: R$ 80-150k (1× L40S 48GB)
    instalação_NeoGov: R$ 30-80k (consultoria + integração)
    treinamento_equipe_cliente: R$ 10-30k
    licenças_software_extras: R$ 5-20k
    margem_contingência: R$ 10-50k
    
dado_primario_necessario:
  o_que: Cotação real de servidor pronto Tier C para hospital tipo (Beta)
  como_obter: Cotação fornecedores hardware BR (Itautec? Dell? Lenovo?) + serviços
  quem_executa: Camila CTO + parceiros hardware
  sprint_destino: pré-Wave 2A (M+10 antes do go-to-market saúde)
```

## 7 · Validação com a equipe NeoGov (GAPs atualizados)

| Gap | Quem | O quê | Sprint |
|---|---|---|---|
| **GAP-CAMILA-01** | Camila CTO | Stack tecnológico atual NeoGov + experiência fine-tuning | S2.5.1 |
| **GAP-CAMILA-02** | Camila CTO | Cotações 3 cloud providers BR · L40S 48GB 24/7 | S2.5.3 |
| **GAP-SIMONE-01** | Simone | Validação jurídica DPA cloud BR escolhida | S2.5.3 |
| **GAP-WILTON-01** | Wilton | Clientes B2G têm exigência específica de cloud (Serpro?) | S2.5.1 |
| **GAP-CAMILA-03** | Camila CTO | Executar POC fine-tune Llama 3.1 8B (validar viabilidade) | S2.5.2 |

## 8 · Hash de continuidade

| Hash anterior | Hash atual |
|---|---|
| `NEOGOV-V21-S3.0.1-INVALIDADO+D003-CRITICAL-AWAIT-S2.5` | `NEOGOV-V21-S3.0.1-INVALIDADO+D003-V2-IA-PROPRIA-AWAIT-S2.5` |

## 9 · Decisão metodológica permanente (D-015 a registrar)

> **Padrão "Estimativa por Análogo com Lastro" é OBRIGATÓRIO em todos os artefatos NeoGov daqui pra frente.**
> 
> Toda estimativa deve ter: (1) marcador visual 🟡 + tag `[ESTIMATIVA POR ANÁLOGO]`, (2) lastro rastreável em §LASTROS do documento, (3) fórmula com variáveis nomeadas para refatoração futura facilitada, (4) sprint destino para coleta de dado primário substituto.
> 
> **Honra a:** Valor 1 (Honestidade Epistêmica) + Valor 5 (Auditabilidade Reversa) + RGO-1 (re-avaliar campo) + RGO-2 (evidência real) + D-007 (não inflar VVV).
