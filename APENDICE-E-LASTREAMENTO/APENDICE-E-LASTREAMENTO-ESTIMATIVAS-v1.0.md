---
id: NEOGOV-V21-APENDICE-E
filename: APENDICE-E-LASTREAMENTO-ESTIMATIVAS-v1.0.md
created_at: 2026-05-15
type: LIVE_APPENDIX
status: ACTIVE
parent_decision: D-015 (sistema lastreamento)
parent_debt: D003 (arquitetura agentic soberana)
purpose: Lastrear todas as estimativas técnicas do D003 com flag visual, plano de saneamento e backlinks
total_estimativas: 28
distribuicao_flags: 8 FATO · 11 ANÁLOGO · 6 INFERÊNCIA · 2 ESTIMATIVA · 1 GAP
vvv_medio: 0.74 (honesto · refinado por saneamento)
tags: [lastreamento, D015, D003, governanca-dados, refatoracao-trivial]
---

# Apêndice E · Lastreamento de Estimativas (versão completa v1.0)

> Aplicação do sistema D-015 sobre todas as estimativas técnicas do Débito D003 (Arquitetura Agentic Soberana). Documento vivo · atualizado a cada validação que vira FATO.

## Convenção de Flags Visuais

| Flag | Cor | Significado | VVV típico | Critério |
|---|---|---|---:|---|
| 🟢 `[FATO]` | Verde | Dado primário verificável em fonte oficial | 0.90-1.00 | Lei, documento oficial empresa, contrato, transcrição validada |
| 🔵 `[ANÁLOGO]` | Azul | Caso similar documentado · empresa/produto comparável | 0.70-0.85 | Empresa similar usando solução comparável |
| 🟡 `[INFERÊNCIA]` | Amarelo | Derivação lógica defensável · sem análogo direto | 0.55-0.70 | Cálculo a partir de benchmarks setoriais combinados |
| 🟠 `[ESTIMATIVA]` | Laranja | Palpite operacional · necessita validação | 0.40-0.55 | Quando nem análogo nem inferência são possíveis |
| 🔴 `[GAP]` | Vermelho | Vazio · bloqueante para uso comercial | 0.20-0.40 | Espera entrevista, POC, decisão técnica |

## Sumário Executivo

| Categoria | # Estimativas | Distribuição | VVV médio |
|---|:---:|---|---:|
| C1 Modelo LLM | 6 | 3 FATO · 1 ANÁLOGO · 1 INFERÊNCIA · 1 GAP | 0.78 |
| C2 Cloud Soberana | 6 | 1 FATO · 3 ANÁLOGO · 2 INFERÊNCIA | 0.73 |
| C3 GPU/Hardware | 5 | 1 FATO · 2 ANÁLOGO · 2 INFERÊNCIA | 0.72 |
| C4 Framework Agentic | 3 | 2 FATO · 1 ANÁLOGO | 0.83 |
| C5 Vector DB / Knowledge | 3 | 1 FATO · 2 INFERÊNCIA | 0.68 |
| C6 Trabalho Humano + Operação | 5 | 2 FATO · 2 ANÁLOGO · 1 ESTIMATIVA | 0.75 |
| **TOTAL** | **28** | **9 FATO · 9 ANÁLOGO · 8 INFERÊNCIA · 1 ESTIMATIVA · 1 GAP** | **0.74** |

## Top 5 Estimativas de Maior Risco (saneamento prioritário)

| # | EST-ID | Razão | Impacto se errado | Ação prioritária |
|---|---|---|---|---|
| 1 | EST-013 GPU L40S BR | INFERÊNCIA · base de Tier B | ALTO · 40-60% custo recorrente Tier B | Cotação 3 fornecedores + cloud BR |
| 2 | EST-006 Sabiá-4 on-premise | 🔴 GAP confirmado · indisponível | CRÍTICO · invalida Tier C com Sabiá | Decidir Llama 3.1 ou aguardar Maritaca |
| 3 | EST-024 Tempo fine-tune Llama | INFERÊNCIA · esforço Tier C | ALTO · 1-3 meses dev × R$ 25k/mês | POC fine-tune sub-conjunto jurídico |
| 4 | EST-016 Setup ETL hospital | ESTIMATIVA · gap GAP03 | ALTO · setup P5 fura Art. 75 IV | POC pré-Wave-2A |
| 5 | EST-021 Qdrant sizing | INFERÊNCIA · dimensionamento KB | MÉDIO · subdimensionar = latência | POC com knowledge base real |

---

## C1 · Modelo LLM (6 estimativas)

### 🟢 EST-001 · Sabiá-4 pricing oficial Maritaca AI

```yaml
EST-ID: EST-001-sabia4-pricing
flag: 🟢 FATO
valor: R$ 5,00/MTok input · R$ 20,00/MTok output
unidade: R$/MTok (input · output)
context_window: 128.000 tokens
fonte: docs.maritaca.ai/pt/precos + megatek.ai/en/api/maritaca-ai (jan/2026) + maritaca.ai/api
saneamento:
  acao: Confirmar pricing volume enterprise (>10M tokens/mês)
  responsavel: Wilton (comercial)
  prazo: S2.5.1
usado_em:
  - DEBITO-D003 §2.1 modelo principal
  - Tier A (default escola privada)
  - SPRINT-3.0.1-redo P1 P3 P4 IA-cost
risco_se_errado: baixo · pricing público confirmado
ultima_revisao: 2026-05-15
```

### 🟢 EST-002 · Sabiazinho-4 pricing oficial (lightweight tasks)

```yaml
EST-ID: EST-002-sabiazinho4-pricing
flag: 🟢 FATO
valor: R$ 1,00/MTok input · R$ 4,00/MTok output
unidade: R$/MTok
context_window: 128.000 tokens
fonte: docs.maritaca.ai/pt/precos + maritaca.ai/post/sabiazinho-4 (jan/2026)
melhorias_vs_sabiazinho3:
  - Maior cobertura de dados jurídicos brasileiros
  - Avanços em function calling e capacidades de agente
  - Janela 32k → 128k tokens
saneamento:
  acao: POC validar performance jurídica vs Sabiá-4 (custo 5x menor)
  responsavel: Camila (CTO)
  prazo: S2.5.2
usado_em:
  - Tarefas leves (classificação, extração simples)
  - Tier A volume alto
  - Agente Data Discovery (filtragem inicial)
  - SPRINT-3.0.1-redo P1 P2 IA-cost
estrategia_uso: Sabiazinho-4 default · Sabiá-4 escalado para casos complexos jurídicos
risco_se_errado: baixo
ultima_revisao: 2026-05-15
```

### 🟢 EST-003 · Sabiá-4 NÃO disponível on-premise

```yaml
EST-ID: EST-003-sabia4-onpremise-status
flag: 🟢 FATO
valor: "Currently, Sabiá 4 models are only available via API. We don't offer weights for download or licensing for on-premise use."
fonte: maritaca.ai/en/ FAQ oficial
implicacao_critica: |
  Tier C (on-premise no cliente · saúde/B2G federal) NÃO pode usar Sabiá-4.
  Precisa modelo alternativo (Llama 3.1 fine-tunado · Mistral · Qwen).
  Maritaca ofereceu opção de licenciamento on-premise? Confirmar via comercial.
saneamento:
  acao_1: Contato direto Maritaca (Rodrigo Nogueira) · roadmap on-premise?
  acao_2: Validar Llama 3.1 70B fine-tunado em corpus jurídico BR como Plano B
  acao_3: Considerar Maritaca rodando em VPC dedicada cliente (alternativa)
  responsavel: Camila + Wilton
  prazo: S2.5.2 (URGENTE · reformula Tier C)
usado_em:
  - DEBITO-D003 §2.2 Tier C (definição arquitetural Tier C precisa revisão)
risco_se_errado: CRÍTICO · invalida Tier C com modelo BR
ultima_revisao: 2026-05-15
flag_destaque: 🚨 IMPACTO ARQUITETURAL
```

### 🔵 EST-004 · Llama 3.1 70B inference cost (cloud)

```yaml
EST-ID: EST-004-llama31-inference-cost
flag: 🔵 ANÁLOGO
valor: R$ 0,80-2,50/MTok (cloud GPU BR · L40S/A100) · ou ~R$ 0,30/MTok via API agregador
unidade: R$/MTok equivalente
fonte_analogo:
  - L40S cloud rate: $1.50-2.00/USD-hr (getdeploying.com · mar/2026)
  - Throughput Llama 3.1 70B em L40S: ~200-400 tokens/segundo (benchmarks setor)
  - Cálculo: 1 hora = 720.000-1.440.000 tokens = R$ 5-10 por MTok efetivo
  - APIs agregadoras (Groq, Together): $0.59-0.88/MTok blended · ~R$ 3-5/MTok
saneamento:
  acao: POC Llama 3.1 70B em Magalu Cloud GPU · medir throughput real
  responsavel: Camila (CTO)
  prazo: S2.5.2
usado_em:
  - Tier B (B2G · GPU dedicada compartilhada)
  - Tier C (on-premise · Plano B substituindo Sabiá)
  - SPRINT-3.0.1-redo P2 P3 P4 IA-cost Tier B/C
risco_se_errado: alto · IA é 25-40% do custo Tier B/C
ultima_revisao: 2026-05-15
```

### 🟡 EST-005 · Llama 3.1 70B vs Sabiá-4 performance jurídico BR

```yaml
EST-ID: EST-005-llama-vs-sabia-jurídico
flag: 🟡 INFERÊNCIA
valor: Sabiá-4 ~15-30% superior em tarefas jurídicas BR sem fine-tune adicional
unidade: % delta performance benchmarks BR
fonte_inferencia:
  - Sabiá-4 corpus jurídico BR explícito no treinamento (docs.maritaca.ai)
  - Llama 3.1 70B é multilingual mas não especializado em direito BR
  - Inferência: fine-tune Llama 3.1 com dataset jurídico BR pode fechar gap
  - Custo fine-tune: estimar 1-3 meses dev · ver EST-024
saneamento:
  acao_1: POC comparativo · OAB-Bench + extração contratos LGPD
  acao_2: Avaliar fine-tune Llama 3.1 com dataset jurídico próprio NeoGov
  responsavel: Camila + Simone (validação jurídica output)
  prazo: S2.5.2
usado_em:
  - Decisão modelo Tier B (Sabiá API + cloud BR vs Llama 3.1 + GPU dedicada)
  - Decisão modelo Tier C (Llama fine-tuned · Sabiá não disponível on-premise)
risco_se_errado: médio · afeta qualidade output jurídico (core competence NeoGov)
ultima_revisao: 2026-05-15
```

### 🔴 EST-006 · Sabiá-4 licenciamento on-premise (futuro)

```yaml
EST-ID: EST-006-sabia4-onpremise-future
flag: 🔴 GAP
valor: INDISPONÍVEL · não há roadmap público
fonte: Maritaca AI FAQ oficial (confirmado em EST-003)
implicacao: Tier C precisa Plano B (Llama 3.1 fine-tunado) · revisão arquitetural
saneamento:
  acao: Contato comercial Maritaca · pedir cotação licenciamento on-premise customizado
  responsavel: Wilton + Camila
  prazo: S2.5.2
usado_em:
  - DEBITO-D003 §2.2 Tier C (revisão pendente)
risco_se_errado: crítico (já é GAP confirmado)
ultima_revisao: 2026-05-15
flag_destaque: 🚨 BLOQUEIO ARQUITETURAL TIER C
```

---

## C2 · Cloud Soberana (6 estimativas)

### 🔵 EST-007 · Magalu Cloud Tier A (cliente Gamma escola privada)

```yaml
EST-ID: EST-007-magalu-tier-A-cost
flag: 🔵 ANÁLOGO
valor: R$ 400-1.500/cliente/mês (VM dedicada + storage + bandwidth)
unidade: R$/cliente/mês
fonte_analogo:
  - Sysvale (BA · 11 anos · saúde pública) usa Magalu Cloud multi-tenant para 200+ municípios
  - magalu.cloud/blog/sysvale (dez/2025): "cada município conta com máquina virtual dedicada"
  - Performance reportada: processamento 2x · memória 35% · armazenamento 2-5x mais rápido
  - Análogo direto ao perfil NeoGov Tier A (multi-tenant SaaS regulamentado)
saneamento:
  acao_1: Cotação direta Magalu Cloud · perfil "100 clientes Gamma multi-tenant"
  acao_2: POC 1 cliente real 30 dias · medir custo efetivo
  responsavel: Camila (especificação técnica) + Wilton (negociação)
  prazo: S2.5.3
usado_em:
  - Tier A default Gamma escola privada
  - SPRINT-3.0.1-redo P1 SaaS · linha cloud
  - SPRINT-3.0.1-redo P4 AI-DPO · linha cloud (Gamma)
risco_se_errado: médio · 30-50% do custo P1 · erro 30% afeta margem 8-12pp
ultima_revisao: 2026-05-15
```

### 🔵 EST-008 · Locaweb Cloud Tier A (alternativa Magalu)

```yaml
EST-ID: EST-008-locaweb-tier-A-cost
flag: 🔵 ANÁLOGO
valor: R$ 300-1.200/cliente/mês (Locaweb 50-70% mais barata que AWS · Magalu para baseline)
unidade: R$/cliente/mês
fonte_analogo:
  - Locaweb Cloud lançada 2025 (NeoFeed · mar/2026): "50-70% mais barata que AWS"
  - 150 clientes em 6 meses · 1.800 clientes projetados em 5 anos
  - Data center São Paulo + redundância secundária
  - Foco SMB/PME (alinha com perfil Gamma escola privada)
saneamento:
  acao: Cotação Locaweb Cloud · compare vs Magalu (EST-007)
  responsavel: Camila + Wilton
  prazo: S2.5.3
usado_em:
  - Tier A alternativa Magalu (multi-fornecedor para evitar lock-in)
  - SPRINT-3.0.1-redo benchmarks comparativos
risco_se_errado: baixo (estamos com 2 análogos · diversificação)
ultima_revisao: 2026-05-15
```

### 🟡 EST-009 · TIVIT Private Cloud Tier B (B2G médio)

```yaml
EST-ID: EST-009-tivit-tier-B-cost
flag: 🟡 INFERÊNCIA
valor: R$ 1.500-5.000/cliente/mês (private cloud dedicada com VPN)
unidade: R$/cliente/mês
fonte_inferencia:
  - TIVIT positioning premium "private cloud + LGPD compliance" (cloud.tivit.com)
  - Setor: financeiro/saúde regulado (alinha B2G)
  - Premium ~2-3x sobre Magalu Cloud público (inferência setor)
saneamento:
  acao_1: Cotação direta TIVIT · perfil "B2G médio cluster"
  acao_2: Considerar Magalu Cloud BMG (dedicated alternativa) como comparativo
  responsavel: Wilton (acesso enterprise) + Camila
  prazo: S2.5.3
usado_em:
  - Tier B opção 1 (default B2G médio)
  - SPRINT-3.0.1-redo P2 P3 Tier B Alfa
risco_se_errado: médio · cloud Tier B é 20-35% do custo
ultima_revisao: 2026-05-15
```

### 🔵 EST-010 · Serpro/Dataprev nuvem soberana federal (Tier C+)

```yaml
EST-ID: EST-010-serpro-tier-C-cost
flag: 🔵 ANÁLOGO
valor: R$ 0 a R$ 3.500/mês (depende de homologação · custo varia muito)
unidade: R$/mês (cliente B2G federal)
fonte_analogo:
  - Nuvem de Governo Soberana lançada 2025 (Serpro + Dataprev)
  - 250+ órgãos federais conectados (brunotutorias.com.br · fev/2026)
  - "Software desenvolvido localmente" · 100% soberana
  - Pricing não público · acessado via processo licitatório federal
saneamento:
  acao_1: Contato Wilton (acesso FNDE) · entender modelo de homologação Serpro
  acao_2: Verificar se NeoGov ICT pode rodar SOBRE infraestrutura Serpro
  acao_3: Alternativa: NeoGov empacotada · cliente B2G consome via Serpro
  responsavel: Wilton (acesso político) + Simone (jurídico contratos federais)
  prazo: S2.5.3 (gate B2G federal)
usado_em:
  - Tier C+ (B2G federal sensível · ministérios, autarquias)
  - SPRINT-3.0.1-redo cenário enterprise federal
risco_se_errado: baixo · alternativa estratégica · não bloqueante para outros tiers
ultima_revisao: 2026-05-15
```

### 🔵 EST-011 · AWS São Paulo + SCC (alternativa controlada)

```yaml
EST-ID: EST-011-aws-sp-scc-cost
flag: 🔵 ANÁLOGO
valor: R$ 800-2.500/cliente/mês (premium 30-40% vs Magalu/Locaweb)
unidade: R$/cliente/mês
fonte_analogo:
  - AWS region São Paulo (sa-east-1) confirmada
  - Standard Contractual Clauses (SCC) declarado em aws.amazon.com/compliance/brazil-data-privacy
  - Premium tipicamente 30-40% sobre cloud BR puro
  - LGPD compliance declarado mas "controlado por corporação estrangeira" (capitaldigital.com.br)
saneamento:
  acao: Cotação AWS BR via parceiro · verificar elegibilidade para clientes sensitivos
  responsavel: Camila
  prazo: S2.5.3
usado_em:
  - Alternativa para clientes que exigem AWS (existentes)
  - Migração path para clientes que querem sair de AWS internacional
risco_se_errado: baixo · não é default
ultima_revisao: 2026-05-15
```

### 🟡 EST-012 · Storage/Bandwidth por cliente típico

```yaml
EST-ID: EST-012-storage-bandwidth-cost
flag: 🟡 INFERÊNCIA
valor: R$ 50-300/cliente/mês (storage 50-500 GB + bandwidth 100 GB-1 TB)
unidade: R$/cliente/mês
fonte_inferencia:
  - Storage SSD Magalu Cloud ~R$ 0,50/GB/mês (cotação pública)
  - Bandwidth Magalu Cloud ~R$ 0,20/GB transferido
  - Cliente típico Gamma: ~100 GB storage + ~200 GB bandwidth/mês = R$ 90/mês
  - Cliente típico Beta: ~500 GB storage + ~1 TB bandwidth/mês = R$ 450/mês
saneamento:
  acao: Validar com cotação Magalu (consolidada com EST-007)
  responsavel: Camila
  prazo: S2.5.3
usado_em:
  - Componente cloud em todos os tiers
  - Diferencia custo entre persona Gamma · Alfa · Beta
risco_se_errado: baixo · component menor (5-15% do cloud)
ultima_revisao: 2026-05-15
```

---

## C3 · GPU/Hardware (5 estimativas)

### 🟢 EST-013 · NVIDIA L40S cloud rate internacional 2026

```yaml
EST-ID: EST-013-l40s-cloud-rate
flag: 🟢 FATO
valor: $1.70/hr média on-demand · range $0.28-7.58/hr · 720 hr/mês = $1,224/mês (R$ 6.487/mês)
unidade: USD/hr · convertido R$ 5,30
fonte: getdeploying.com/gpus/nvidia-l40s (atualizado 2 dias atrás · mai/2026)
  - 29 cloud providers tracked
  - VRAM 48 GB ideal para Llama 3.1 70B em 4-bit quantized
  - 30-40% mais barato que A100/H100 · melhor para inferência
saneamento:
  acao_1: Verificar disponibilidade L40S em Magalu Cloud GPU
  acao_2: Cotação Vast.ai (spot $0.28-1.50/hr) para POC
  responsavel: Camila
  prazo: S2.5.4
usado_em:
  - Tier B GPU dedicada
  - POC Llama 3.1 70B fine-tune
risco_se_errado: baixo · pricing global tracked diariamente
ultima_revisao: 2026-05-15
```

### 🟡 EST-014 · NVIDIA L40S compra Brasil

```yaml
EST-ID: EST-014-l40s-capex-brazil
flag: 🟡 INFERÊNCIA
valor: R$ 130.000-280.000 por unidade (importada · com impostos)
unidade: R$ (CAPEX)
fonte_inferencia:
  - L40S preço internacional ~$8.000-10.000 USD (mercado · referência 2025)
  - Câmbio 5.30 BRL = R$ 42-53k base
  - Importação BR (II + ICMS + ISS + logística): 3-4x preço base (típico setor)
  - = R$ 130-260k posto Brasil
  - Alternativa cloud (EST-013): break-even em ~24-36 meses
saneamento:
  acao_1: Cotação 3 fornecedores BR (Bludata, NTI Brasil, Aldo, R&S)
  acao_2: Análise CAPEX vs OPEX 36 meses
  acao_3: Considerar A100 80GB ($10-17k USD) como alternativa
  responsavel: Camila + Financeiro
  prazo: S2.5.4
usado_em:
  - Tier C on-premise (cliente paga + NeoGov instala)
  - Decisão buy-vs-rent Tier B
risco_se_errado: alto · CAPEX impacta modelo financeiro Tier B/C
ultima_revisao: 2026-05-15
```

### 🔵 EST-015 · A100 cloud rate (alternativa L40S)

```yaml
EST-ID: EST-015-a100-cloud-rate
flag: 🔵 ANÁLOGO
valor: $1.29-2.50/hr on-demand · spot $0.13-1.00/hr
unidade: USD/hr · R$ 6,84-13,25/hr equivalente
fonte: getdeploying.com/gpus/nvidia-a100 (mai/2026) · jarvislabs.ai (abr/2026)
  - 38 cloud providers tracked
  - 80 GB VRAM · suporta Llama 3.1 70B FP16 sem quantização
  - Preço caiu 13% desde mai/2025
saneamento:
  acao: Comparar A100 vs L40S em POC Llama 3.1 (custo × performance)
  responsavel: Camila
  prazo: S2.5.4
usado_em:
  - Alternativa Tier B (modelos sem quantização)
  - POC training/fine-tune
risco_se_errado: baixo (estamos com 3 opções: L40S, A100, H100)
ultima_revisao: 2026-05-15
```

### 🟡 EST-016 · Energia + manutenção on-premise

```yaml
EST-ID: EST-016-onpremise-opex
flag: 🟡 INFERÊNCIA
valor: R$ 1.500-4.500/mês por GPU (energia + cooling + manutenção)
unidade: R$/mês/GPU
fonte_inferencia:
  - L40S TDP 350W · A100 SXM4 400W · H100 SXM5 700W
  - Energia BR industrial ~R$ 0,80/kWh
  - L40S 24/7: 350W × 720h × R$ 0,80/kWh = R$ 202/mês energia
  - Cooling overhead 30-50% = +R$ 60-100/mês
  - Datacenter colocation BR ~R$ 600-1.500/mês 1U server
  - Manutenção/depreciação 10% ao ano sobre CAPEX
saneamento:
  acao_1: Cotação colocation BR (Equinix, Ascenty, Odata)
  acao_2: Considerar cliente fornece datacenter (hospital com infra própria)
  responsavel: Camila + Financeiro
  prazo: S2.5.4
usado_em:
  - Tier C on-premise OPEX
  - Cálculo break-even buy-vs-rent
risco_se_errado: médio · OPEX é 30-50% do CAPEX/ano amortizado
ultima_revisao: 2026-05-15
```

### 🔵 EST-017 · Magalu Cloud GPU on-demand BR

```yaml
EST-ID: EST-017-magalu-gpu-cost
flag: 🔵 ANÁLOGO
valor: ESTIMAR R$ 12-25/hr para GPU equivalente L40S/A100 BR
unidade: R$/hr (cloud BR)
fonte_analogo:
  - Magalu Cloud oferece GPU (positioning soberano)
  - Locaweb declarou 50-70% mais barata que AWS
  - AWS BR sa-east-1 ~p4d.24xlarge (8×A100): ~$32/hr ≈ R$ 170/hr (R$ 21/GPU/hr)
  - Magalu equivalente: estimar R$ 12-15/GPU/hr (30-40% desconto vs AWS)
saneamento:
  acao: Cotação direta Magalu Cloud GPU section · perfil "L40S 1 unidade 24/7"
  responsavel: Camila
  prazo: S2.5.3 (junto cotação Magalu Cloud geral)
usado_em:
  - Tier B GPU dedicada (alternativa AWS internacional)
  - Permite ficar 100% BR sem CAPEX
risco_se_errado: médio · validar via cotação real
ultima_revisao: 2026-05-15
```

---

## C4 · Framework Agentic (3 estimativas)

### 🟢 EST-018 · LangGraph licenciamento

```yaml
EST-ID: EST-018-langgraph-licensing
flag: 🟢 FATO
valor: R$ 0 (open-source MIT license) · LangSmith opcional R$ 0-2.000/mês
unidade: R$/mês (componente observability)
fonte: docs LangChain oficial + comparativos 2026
detalhes:
  - LangGraph v1.0 GA outubro/2025 · v1.0.10 atual
  - Default para "regulated industries" (uvik.net · mai/2026)
  - LangSmith pago para observability/auditoria (R$ 0 free tier · R$ 200-2.000/mês)
  - Alternativa: LangSmith self-hosted (zero ongoing)
saneamento:
  acao: Decidir LangSmith cloud vs self-hosted
  responsavel: Camila
  prazo: S2.5.4
usado_em:
  - Framework agentic principal todos os tiers
  - Custo licenciamento próximo a zero (open-source)
risco_se_errado: baixo
ultima_revisao: 2026-05-15
```

### 🟢 EST-019 · Qdrant licenciamento (Vector DB)

```yaml
EST-ID: EST-019-qdrant-licensing
flag: 🟢 FATO
valor: R$ 0 (Apache 2.0 open-source) · Qdrant Cloud opcional $25-$500/mês
unidade: R$/mês
fonte: qdrant.tech oficial
detalhes:
  - Open-source · pode rodar local (Tier C) ou em container (Tier A/B)
  - Performance reportada 4-15x mais rápido que alternativas
  - Suporta filtros · payload · multi-tenancy
saneamento:
  acao: POC dimensionar índice para knowledge base NeoGov (~10-50k docs)
  responsavel: Camila
  prazo: S2.5.4
usado_em:
  - Camada RAG todos os agentes
  - Tier C on-premise (vai rodar local no cliente)
risco_se_errado: baixo · open-source · pode trocar para pgvector
ultima_revisao: 2026-05-15
```

### 🔵 EST-020 · Custo dev/integração framework agentic

```yaml
EST-ID: EST-020-dev-cost-framework
flag: 🔵 ANÁLOGO
valor: R$ 80.000-200.000 (3-6 meses dev · 1 sênior + 1 pleno)
unidade: R$ (CAPEX dev inicial · amortizar em 3 anos)
fonte_analogo:
  - LangGraph learning curve "1-2 semanas até produtividade" (uvik.net · mai/2026)
  - Multi-agent regulated industry: típico 4-6 meses dev MVP
  - Equipe 1 sênior (R$ 15k×1,28=R$ 19.2k/mês) + 1 pleno (R$ 8k×1,28=R$ 10.2k/mês)
  - 3-6 meses × R$ 29,4k/mês = R$ 88-176k
saneamento:
  acao: Validar com Camila (CTO já tem experiência? equipe contratada?)
  responsavel: Camila
  prazo: S2.5.1 (GAP-CAMILA-01)
usado_em:
  - Componente fixo amortizado em todos produtos
  - SPRINT-3.0.1-redo P1-P5 linha "fixos alocados"
risco_se_errado: alto · subdimensionar = atraso M1-M3
ultima_revisao: 2026-05-15
```

---

## C5 · Vector DB / Knowledge (3 estimativas)

### 🟢 EST-021 · BGE-M3 embeddings (open-source)

```yaml
EST-ID: EST-021-bge-m3-embeddings
flag: 🟢 FATO
valor: R$ 0 (open-source · pode rodar local em CPU/GPU)
unidade: R$ (zero)
fonte: huggingface.co/BAAI/bge-m3 + Maritaca recomenda Multilingual-E5-large (FAQ)
detalhes:
  - BGE-M3 (BAAI): multilingual, 8192 tokens context, top benchmarks
  - Multilingual-E5-large: recomendado pela Maritaca para RAG
  - Ambos open-source · rodam local sem dependência externa
saneamento:
  acao: POC benchmark BGE-M3 vs E5-large em corpus jurídico BR
  responsavel: Camila
  prazo: S2.5.4
usado_em:
  - Camada RAG todos os agentes
  - Zero custo de licenciamento
risco_se_errado: baixo
ultima_revisao: 2026-05-15
```

### 🟡 EST-022 · Qdrant sizing (knowledge base NeoGov)

```yaml
EST-ID: EST-022-qdrant-sizing
flag: 🟡 INFERÊNCIA
valor: 8-32 GB RAM · 50-200 GB storage por instância (depende do volume)
unidade: GB RAM/storage
fonte_inferencia:
  - Knowledge base NeoGov inicial: ~10-50k documentos jurídicos (Simone+Gislênia)
  - 1024-dim embedding × 50k docs × 4 bytes = 200 MB vetores
  - Payload adicional (metadata, texto): 5-50 GB
  - RAM: índice + cache ~8-32 GB típico para esta escala
  - Crescimento: +20% por trimestre conforme knowledge evolui
saneamento:
  acao: POC carregar 5k docs jurídicos · medir RAM/storage real
  responsavel: Camila + Simone (preparar corpus)
  prazo: S2.5.4
usado_em:
  - Sizing instâncias Qdrant
  - Custo infra RAG em todos tiers
risco_se_errado: médio · subdimensionar = latência
ultima_revisao: 2026-05-15
```

### 🟡 EST-023 · Preparação knowledge base inicial

```yaml
EST-ID: EST-023-knowledge-base-prep
flag: 🟡 INFERÊNCIA
valor: R$ 30.000-90.000 (esforço Simone+Gislênia organizar corpus)
unidade: R$ (CAPEX inicial · 1-3 meses)
fonte_inferencia:
  - 10-50k documentos jurídicos a organizar/anotar
  - Simone+Gislênia + assistente jurídico ~1-3 meses
  - Custo: 2-3 pessoas × R$ 15k/mês × 1-3 meses
  - Inclui: estruturação, tagging, validação de qualidade, versionamento
saneamento:
  acao_1: Inventário do que já existe (Simone+Gislênia produziram em consultoria)
  acao_2: Definir gaps (LAI/LGPD intersect, ECA Digital, jurisprudência recente)
  acao_3: Cronograma 12 semanas com entregáveis incrementais
  responsavel: Simone + Gislênia (jurídico) + Camila (técnico estruturação)
  prazo: S2.5.5 (paralelo a fim de S2.5)
usado_em:
  - Pré-requisito todos os agentes (eles consomem knowledge base)
  - Custo amortizado em 3 anos sobre todos clientes
risco_se_errado: médio · subestimar = MVP atrasa
ultima_revisao: 2026-05-15
```

---

## C6 · Trabalho Humano + Operação (5 estimativas)

### 🟢 EST-024 · Salário Engenheiro IA pleno Brasil 2026

```yaml
EST-ID: EST-024-salario-engenheiro-ia
flag: 🟢 FATO
valor: R$ 10.000/mês (pleno) · custo empresa R$ 12.800/mês (×1,28)
unidade: R$/mês
fonte: Numerando + Glassdoor + Robert Half 2026 (já validado S3.0.1 v1.0 - mantido)
detalhes:
  - Pleno IA/ML: R$ 8-13k/mês
  - Senior IA/ML: R$ 15-25k/mês
  - Encargos Simples Nacional 8% + benefícios = ×1,28
saneamento:
  acao_1: Validar disponibilidade no mercado · Camila tem rede para contratar?
  acao_2: Considerar PJ vs CLT vs internacional (custo varia 30-50%)
  responsavel: Camila + RH
  prazo: S2.5.5
usado_em:
  - Dev fine-tune Llama 3.1 (Tier C)
  - Manutenção contínua agentes
  - Custo fixo NeoGov
risco_se_errado: baixo · dados de mercado robustos
ultima_revisao: 2026-05-15
```

### 🔵 EST-025 · Salário Jurídico LGPD pleno

```yaml
EST-ID: EST-025-salario-juridico-lgpd
flag: 🔵 ANÁLOGO
valor: R$ 8.000-15.000/mês (pleno especialista LGPD)
unidade: R$/mês
fonte_analogo:
  - Advogado pleno BR 2026: R$ 6-12k (genérico · jusbrasil)
  - Especialista LGPD: premium 30-50% (escassez)
  - Custo empresa: ×1,28 = R$ 10.2-19.2k/mês
saneamento:
  acao: Validar com Simone (sabe mercado · acabou de sair de empresa do setor)
  responsavel: Simone
  prazo: S2.5.5
usado_em:
  - Custo operacional knowledge base evolução
  - Suporte jurídico contínuo aos agentes
  - Custo fixo NeoGov
risco_se_errado: baixo · core competence team já mapeada
ultima_revisao: 2026-05-15
```

### 🔵 EST-026 · Tempo onboarding por persona

```yaml
EST-ID: EST-026-onboarding-time
flag: 🔵 ANÁLOGO
valor: Gamma 8-16h · Alfa 40-120h · Beta 200-600h
unidade: horas
fonte_analogo:
  - SaaS B2B SMB onboarding típico: 4-20h (Hubspot, Pipefy benchmarks)
  - B2G SaaS: 3-5x mais por causa de processos (Sysvale case)
  - Setor saúde integração legado: 10-30x base (relatos setor)
  - Custo: hora pleno R$ 12.800/176 = R$ 73/hora
saneamento:
  acao: Validar com primeiros clientes reais (M1-M3)
  responsavel: Camila + Wilton
  prazo: pós M1
usado_em:
  - Componente [3] Onboarding em todos os produtos
  - SPRINT-3.0.1-redo todos produtos
risco_se_errado: médio · subestimar = margem inicial baixa
ultima_revisao: 2026-05-15
```

### 🟢 EST-027 · Encargos Simples Nacional + benefícios

```yaml
EST-ID: EST-027-encargos-simples
flag: 🟢 FATO
valor: 1,28× sobre salário bruto (8% encargos + 19,44% provisões + 8% benefícios médios)
unidade: multiplicador
fonte: calculadorabrasil.com.br + gov.br/Simples Nacional 2026
detalhes:
  - FGTS 8%
  - Provisões férias+13º+rescisão: 19,44%/mês
  - Benefícios médios (VR, VT, plano saúde): 8% sobre salário
  - Total: ~28% sobre bruto = ×1,28 custo total
saneamento: não necessário (lei vigente)
usado_em:
  - Cálculo custo total empregado em todas estimativas C6
  - SPRINT-3.0.1-redo todos componentes humanos
risco_se_errado: zero (dado regulatório)
ultima_revisao: 2026-05-15
```

### 🟠 EST-028 · Tempo fine-tune Llama 3.1 70B em corpus jurídico BR

```yaml
EST-ID: EST-028-llama-finetune-time
flag: 🟠 ESTIMATIVA
valor: 2-4 meses (1 sênior IA + 1 pleno + 4-8 H100 cloud durante treino)
unidade: meses (esforço dev) + GPU-hours (custo treino)
fonte_estimativa:
  - LoRA/QLoRA fine-tune Llama 70B em dataset custom: ~15h em 4×H100 (jarvislabs.ai)
  - Custo cloud: 15h × $3/hr × 4 GPUs = $180 por iteração
  - Iterações necessárias: 5-15 (com validação jurídica entre cada)
  - Custo cloud total: ~$1-3k = R$ 5-16k
  - Trabalho humano: 2-4 meses × R$ 30k/mês equipe = R$ 60-120k
  - Total CAPEX fine-tune: R$ 65-136k (amortizado em 3 anos)
saneamento:
  acao_1: POC mini-fine-tune sub-conjunto jurídico (OAB-Bench)
  acao_2: Avaliar se vale o esforço vs usar Sabiá API com sistema prompt cuidadoso
  acao_3: Considerar parceria Maritaca para licenciamento futuro
  responsavel: Camila (técnico) + Simone (validação jurídica)
  prazo: S2.5.4 (decisão estratégica Tier C)
usado_em:
  - Tier C custo dev inicial
  - Decisão Plano A (esperar Maritaca on-premise) vs Plano B (fine-tune Llama)
risco_se_errado: ALTO · sub-estimar = M3-M6 atrasa Tier C
ultima_revisao: 2026-05-15
flag_destaque: 🚨 DECISÃO ESTRATÉGICA TIER C
```

---

## Plano de Saneamento Priorizado

### Sprint 2.5.1 · Validação com equipe NeoGov (GAP-CAMILA-01)

| EST-ID | Saneamento | Responsável | Output esperado |
|---|---|---|---|
| EST-020 | Dev framework: experiência Camila? | Camila | Confirma equipe + cronograma |
| EST-024 | Engenheiro IA: rede disponível? | Camila + RH | Pipeline 3-5 candidatos |
| EST-025 | Jurídico LGPD: mercado | Simone | Validar range + se há disponibilidade |
| EST-023 | Knowledge base: inventário | Simone+Gislênia | Lista do que existe + gaps |

### Sprint 2.5.2 · POC modelo LLM (decisão crítica Tier B/C)

| EST-ID | Saneamento | Responsável | Output esperado |
|---|---|---|---|
| EST-003 | Sabiá-4 on-premise: contato Maritaca | Wilton + Camila | Confirma se há opção licenciamento |
| EST-004 | Llama 3.1 inference: POC throughput | Camila | Tokens/s real + custo efetivo |
| EST-005 | Llama vs Sabiá performance jurídico | Camila + Simone | Benchmark OAB-Bench + extração contrato |
| EST-002 | Sabiazinho-4 lightweight: POC | Camila | Confirma serve para Tier A |

### Sprint 2.5.3 · Validação Cloud (cotações reais)

| EST-ID | Saneamento | Responsável | Output esperado |
|---|---|---|---|
| EST-007 | Magalu Cloud cotação | Camila + Wilton | Preço perfil multi-tenant 100 clientes |
| EST-008 | Locaweb Cloud cotação | Camila | Preço alternativa Magalu |
| EST-009 | TIVIT Private Cloud cotação | Wilton | Premium B2G |
| EST-010 | Serpro/Dataprev acesso | Wilton (FNDE) | Modelo homologação federal |
| EST-017 | Magalu Cloud GPU cotação | Camila | Preço L40S/A100 em BR |

### Sprint 2.5.4 · Desenho final arquitetura 3-tier

| EST-ID | Saneamento | Responsável | Output esperado |
|---|---|---|---|
| EST-013, EST-014, EST-015 | GPU buy-vs-rent decision | Camila + Financeiro | Análise 36 meses |
| EST-016 | Energia/colocation on-premise | Camila | Cotação 2-3 colocations BR |
| EST-018, EST-019 | Framework + Vector DB POC | Camila | LangGraph + Qdrant funcionando |
| EST-022 | Qdrant sizing | Camila | RAM/storage validados |
| EST-028 | Fine-tune Llama decisão | Camila + Simone | Plano A vs B Tier C |

### Sprint 2.5.5 · Knowledge base + Cap 11 §arquitetura

| EST-ID | Saneamento | Responsável | Output esperado |
|---|---|---|---|
| EST-021 | Embeddings benchmark | Camila | BGE-M3 vs E5-large |
| EST-023 | Knowledge base prep | Simone+Gislênia | Cronograma 12 semanas |
| EST-026 | Onboarding pilots | Camila + Wilton | Validação M1-M3 |

---

## Tabela de Backlinks (rastreamento reverso)

| Onde é usado | Estimativas envolvidas |
|---|---|
| **Tier A arquitetura** | EST-001, EST-002, EST-007, EST-008, EST-012, EST-018, EST-019, EST-021, EST-022 |
| **Tier B arquitetura** | EST-004, EST-005, EST-009, EST-013, EST-015, EST-016, EST-017 |
| **Tier C arquitetura** | EST-003 🚨, EST-004, EST-006 🚨, EST-010, EST-014, EST-016, EST-028 🚨 |
| **SPRINT-3.0.1-redo P1 SaaS** | EST-002, EST-007, EST-012, EST-026, EST-027 |
| **SPRINT-3.0.1-redo P2 Data Discovery** | EST-001, EST-002, EST-007, EST-009, EST-013 |
| **SPRINT-3.0.1-redo P3 Anonimização** | EST-001, EST-004, EST-005, EST-009, EST-013 |
| **SPRINT-3.0.1-redo P4 AI-DPO** | EST-001, EST-002, EST-007, EST-008, EST-018, EST-026 |
| **SPRINT-3.0.1-redo P5 ETL** | EST-013, EST-016, EST-020, EST-026, EST-027 |
| **Componente fixo (todos)** | EST-020, EST-023, EST-024, EST-025, EST-027 |

---

## Hash de continuidade

| Hash atual | Hash próximo |
|---|---|
| `NEOGOV-V21-S3.0.1-INVALIDADO+D003-CRITICAL-AWAIT-S2.5` | `NEOGOV-V21-S2.5-LASTREADO-AWAIT-VALIDACAO-CAMILA` |

**VVV consolidado APENDICE-E v1.0:** 0.74 honesto declarado · alvo pós-saneamento (S2.5.1-S2.5.5): 0.90+
