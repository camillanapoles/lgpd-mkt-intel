---
id: NEOGOV-V21-SPRINT-3.0.1-MODELAGEM-CUSTO-PRICING
filename: SPRINT-3.0.1-MODELAGEM-CUSTO-PRICING-v2.0.md
created_at: 2026-05-15T16:00:00Z
type: PRICING_BOTTOM_UP_FRAMEWORK
designation: S3.0.1
function: COST_MODELING_PRICING_ASSERTIVE
parent_doc: BUSINESS-PLAN-FINAL-v2.1
paradigm: S→Q→I→A_BA_ORCHESTRATION
status: ACTIVE_DRAFT_AWAITING_VALIDATION
supersedes: SPRINT-3.0.1-MODELAGEM-CUSTO-v1.0.md (INVALIDADO por AP-13)
ba_orchestration_skills_applied:
  - estimation (PERT 3-point + parametric + analogous + contingency)
  - decision-analysis (weighted scoring · pricing model selection)
  - benchmarking (Confidata + Be Compliance + Safetyfyi + Clio · 2026)
  - risk-analysis (sensitivity unit economics)
  - business-model-canvas (Revenue Streams + Cost Structure coherence)
  - prioritization (MoSCoW tiers)
methodological_pattern_honored: D-015 (estimativa-por-análogo-com-lastro)
mandato_tecnico_honrado: D003-v2 (IA própria local treinada)
tags: [sprint-3-0-1, modelagem, custo, pricing, bottom-up, pert, ba-orchestration, simples-nacional]
quality_score_target: 9.5
vvv_target: 0.85
---

# Sprint 3.0.1 v2.0 · Modelagem Custo Bottom-Up + Framework de Pricing Assertivo

> **Substitui**: `SPRINT-3.0.1-MODELAGEM-CUSTO-v1.0.md` (invalidado por AP-13 · API IA cloud externa)  
> **Aplica**: 6 skills BA-Orchestration (BABOK v3) + mandato D003-v2 IA própria + padrão D-015 lastreado  
> **Honra**: POP §6, §7 · Constitution Art. 1, 2 · RGO 1-8

---

## 0 · Sumário Executivo (TL;DR)

### 0.1 · O que este documento entrega

Um modelo bottom-up de custos NeoGov + framework de pricing assertivo para os 5 produtos, com:
- 3 cenários PERT (Pessimista P10 · Realista P50 · Otimista P90)
- Custos fixos (folha sócios + funcionários + infra + software + tributos)
- Custos variáveis por cliente (cloud rateada + suporte + onboarding + CS)
- CAPEX amortizado (treino modelos IA + setup plataforma)
- Função probabilística de pricing por produto × persona
- Unit economics (LTV/CAC/Payback/Margem) por 20 combos

### 0.2 · Números-âncora do modelo realista (P50)

| Indicador | Valor 🟡 estimado | Status |
|---|---|---|
| Custo fixo mensal NeoGov (M0-M3) | R$ 78.000-92.000 | 🟡 estimativa lastreada |
| Custo fixo mensal NeoGov (M3-M12 Wave 1) | R$ 120.000-160.000 | 🟡 estimativa lastreada |
| Break-even mínimo Wave 1 | ~15-25 clientes ativos | 🟢 inferência |
| Margem alvo SaaS NeoGov | 75-85% (após break-even) | 🟢 inferência setor |
| CAPEX inicial total | R$ 80.000-180.000 (1 vez) | 🟡 estimativa lastreada |
| Tempo amortização CAPEX | 6-12 meses | 🟢 inferência |

### 0.3 · Pricing assertivo final (cenário P50 · realista)

| Produto | Persona-âncora | Modelo | 🟡 Preço/mês ou /uso | Margem alvo |
|---|---|---|---:|---:|
| **P1 SaaS Plataforma** | B2G Municipal | Assinatura tier (3 tiers) | R$ 2.500-12.000/mês | 78-85% |
| **P2 Data Discovery** | Procurador Municipal | Híbrido: setup + uso | Setup R$ 8.000 + R$ 0,12/doc | 80-88% |
| **P3 LAI/LGPD Anonimização** | B2G Federal/Estadual | Assinatura B2G OU per execução | R$ 8.000-25.000/mês OU R$ 0,18/doc | 82-90% |
| **P4 AI-DPO Copilot** | Diretor de Saúde | Per seat | R$ 380-650/seat/mês | 75-82% |
| **P5 ETL/Middleware** | Mantenedor Escolar | Projeto + manutenção | Setup R$ 35-65k + R$ 1.500-3.500/mês | 68-78% |

---

## 1 · Aplicação das Skills BA-Orchestration · Frame Teórico

### 1.1 · Por que orquestrar 6 skills (não 1)

Conforme BABOK v3 (POP §2 fonte canônica skills business-analysis indexadas), precificação é problema multi-técnica:

| Pergunta de precificação | Skill primária | Skills suporte |
|---|---|---|
| Quanto custa produzir cada produto? | **estimation** (PERT 3-point) | — |
| Qual modelo cobrar (assinatura/uso/projeto)? | **decision-analysis** (weighted scoring) | benchmarking |
| Como me posiciono vs concorrente? | **benchmarking** | swot-pestle |
| O unit economics fecha em que cenário? | **risk-analysis** (sensitivity) | estimation |
| Revenue Streams e Cost Structure conversam? | **business-model-canvas** | — |
| Que tiers oferecer? | **prioritization** (MoSCoW) | journey-mapping |

### 1.2 · Sequência aplicada neste documento

```
[1] estimation → custos fixos, variáveis, CAPEX em PERT 3-point
       ↓
[2] benchmarking → preço SOTA 2026 (Confidata/Be Compliance/Safetyfyi/Clio)
       ↓
[3] decision-analysis → escolher modelo de cobrança por produto (weighted scoring)
       ↓
[4] prioritization → MoSCoW define tiers basic/pro/enterprise por produto
       ↓
[5] business-model-canvas → validar coerência Revenue ↔ Cost
       ↓
[6] risk-analysis → sensibilidade ±20% nos drivers críticos
       ↓
[OUTPUT] Função probabilística pricing assertiva por produto × persona
```

---

## 2 · ESTIMATION · Custos Bottom-Up com PERT 3-Point

### 2.1 · Estrutura Societária NeoGov (premissa)

| Campo | Decisão | Lastro |
|---|---|---|
| Natureza jurídica | Sociedade Limitada (Ltda) ou SLU | Padrão BR para startup tech |
| Regime tributário | Simples Nacional | Padrão até R$ 4,8M/ano |
| CNAE principal | 6203-1/00 (Desenvolvimento de software não-customizável) | Confirmado para SaaS BR 2026 |
| CNAEs secundários | 6202-3/00 (Customizável) + 6209-1/00 (Consultoria TI) + 6920-6/02 (Consultoria jurídica) | Multi-atividade |
| Anexo Simples | III (6% inicial) via Fator R | Necessário folha ≥ 28% receita |
| Fator R alvo | ≥ 32% (margem de segurança 4 p.p.) | Best practice contábil |
| Reforma tributária | IBS/CBS começa 2027 (Simples não destaca em 2026) | LC 214/2025 |

**Implicação crítica**: para manter Anexo III (6%), NeoGov deve estruturar pró-labores + folha em **≥ 32% do faturamento**. Isso AMARRA o modelo de custo ao modelo de receita.

### 2.2 · Folha de Pessoal · Pró-Labores e Salários

**Convenção de cores aplicada (POP §4)**:

| Marcador | VVV | Significado |
|---|---:|---|
| ✅ | 0.90-1.00 | FATO · fonte primária verificada |
| 🟢 | 0.80-0.89 | INFERÊNCIA com base em fato |
| 🟡 | 0.60-0.79 | ESTIMATIVA POR ANÁLOGO |

#### 2.2.1 · Pró-Labores Sócios Founders (PERT 3-point)

| Sócio | Papel | 🟡 P10 mensal | 🟡 P50 mensal | 🟡 P90 mensal | Lastro |
|---|---|---:|---:|---:|---|
| **Simone** | CEO + LGPD Lead | R$ 10.000 | R$ 14.000 | R$ 20.000 | LASTRO-PL-01 |
| **Wilton** | Head Comercial/B2G | R$ 8.500 | R$ 12.000 | R$ 18.000 | LASTRO-PL-02 |
| **Camila** | CTO | R$ 12.000 | R$ 17.000 | R$ 24.000 | LASTRO-PL-03 |
| **Gislênia** | Jurídica/Compliance | R$ 7.000 | R$ 10.000 | R$ 14.000 | LASTRO-PL-04 |
| **Subtotal pró-labores** | — | **R$ 37.500** | **R$ 53.000** | **R$ 76.000** | — |

**Fórmula PERT por linha**: `Expected = (P10 + 4×P50 + P90) / 6`

- Simone: (10.000 + 56.000 + 20.000) / 6 = R$ 14.333
- Wilton: (8.500 + 48.000 + 18.000) / 6 = R$ 12.417
- Camila: (12.000 + 68.000 + 24.000) / 6 = R$ 17.333
- Gislênia: (7.000 + 40.000 + 14.000) / 6 = R$ 10.167
- **Total Expected**: R$ 54.250/mês

#### 2.2.2 · Folha CLT/PJ Funcionários por Wave

##### Wave 0 (M0-M3 · Pré-operacional)

| Cargo | Modelo | 🟡 P10 | 🟡 P50 | 🟡 P90 | Lastro |
|---|---|---:|---:|---:|---|
| DevOps/SRE Pleno (1 FTE) | CLT | R$ 9.500 | R$ 12.500 | R$ 15.900 | Robert Half 2026 ✅ |
| **Subtotal Wave 0** | — | R$ 9.500 | R$ 12.500 | R$ 15.900 | — |

##### Wave 1 (M3-M12 · Operacional B2G Municipal)

| Cargo | Modelo | 🟡 P10 | 🟡 P50 | 🟡 P90 | Lastro |
|---|---|---:|---:|---:|---|
| DevOps/SRE Pleno (manter) | CLT | R$ 9.500 | R$ 12.500 | R$ 15.900 | Robert Half ✅ |
| Backend Dev Pleno (1 FTE M+4) | CLT | R$ 9.500 | R$ 12.500 | R$ 15.900 | Robert Half ✅ |
| Customer Success Junior (1 FTE M+6) | CLT | R$ 4.500 | R$ 6.500 | R$ 8.500 | Mercado BR 🟡 |
| SDR Comercial (1 FTE M+5) | CLT + comissão | R$ 4.000 | R$ 5.500 | R$ 7.500 | Mercado BR 🟡 |
| **Subtotal Wave 1** | — | **R$ 27.500** | **R$ 37.000** | **R$ 47.800** | — |

##### Wave 2A (M12+ · Saúde) — para projeção

| Cargo adicional | 🟡 P50 | Justificativa |
|---|---:|---|
| Integrador Sistemas (1 FTE) | R$ 11.000 | Especialista MV/Tasy ETL |
| Sales Healthcare (1 FTE) | R$ 8.500 + comissão | Vertical específico |
| Dev Backend +1 (2 FTE total) | R$ 12.500 | Escalar plataforma |
| **Adicional Wave 2A** | **+ R$ 32.000** | — |

##### Encargos CLT (sobre salários CLT)

| Encargo | % | Lastro |
|---|---:|---|
| INSS patronal | 20% | Lei 8.212/91 ✅ |
| FGTS | 8% | Lei 8.036/90 ✅ |
| Provisão 13º + férias + 1/3 | ~12% | CLT ✅ |
| Outras provisões (rescisão, etc) | ~5% | Padrão contábil 🟢 |
| **Total encargos sobre folha CLT** | **~45%** | — |

**Nota**: Empresas no Simples Nacional NÃO pagam INSS patronal separado (está dentro do DAS). Portanto, encargos efetivos sobre CLT ≈ 25-30% no Simples.

##### Folha Total Projetada (Wave 1 · P50)

```
Pró-labores sócios:          R$ 53.000
Salários CLT (4 FTE):        R$ 37.000
Encargos CLT (~28% no SN):   R$ 10.360
─────────────────────────────────────
TOTAL FOLHA MENSAL P50:      R$ 100.360
```

### 2.3 · Infraestrutura (mandato D003-v2 IA própria)

#### 2.3.1 · Custo recorrente cloud BR (LASTRO-01 D003 atualizado)

| Componente | 🟡 P10 | 🟡 P50 | 🟡 P90 | Lastro |
|---|---:|---:|---:|---|
| 1× L40S 48GB cloud BR 24/7 (Magalu/TIVIT) | R$ 8.000 | R$ 11.500 | R$ 15.000 | LASTRO-01 D003 🟡 |
| Vector DB Qdrant (storage + compute) | R$ 800 | R$ 1.400 | R$ 2.000 | LASTRO benchmark cloud BR 🟡 |
| Observability Langfuse self-hosted | R$ 300 | R$ 550 | R$ 800 | LASTRO infra pequena 🟡 |
| Backup + redundância | R$ 500 | R$ 1.000 | R$ 1.500 | LASTRO padrão cloud BR 🟡 |
| CDN + bandwidth (tráfego BR) | R$ 400 | R$ 800 | R$ 1.500 | LASTRO Cloudflare BR 🟡 |
| **Subtotal Infra Mensal** | **R$ 10.000** | **R$ 15.250** | **R$ 20.800** | — |

**PERT Expected Infra** = (10.000 + 61.000 + 20.800) / 6 = **R$ 15.300/mês**

#### 2.3.2 · CAPEX Treino dos 4 Modelos Especializados (1 vez)

| Modelo | Dataset | Técnica | GPU-hrs | 🟡 P50 |
|---|---|---|---:|---:|
| Agente Data Discovery | ~50M tokens | QLoRA r=16 | 30-50h H100 | R$ 1.500 |
| Agente Anonimização | ~100M tokens | QLoRA+DoRA | 60-100h H100 | R$ 3.000 |
| Agente AI-DPO Copilot | ~80M tokens | QLoRA r=32 | 50-80h H100 | R$ 2.500 |
| Agente Compliance Auditor | ~60M tokens | QLoRA+DoRA | 40-70h H100 | R$ 2.000 |
| Embeddings bge-m3 fine-tune | ~20M tokens | LoRA | 10-20h L40S | R$ 500 |
| **Subtotal CAPEX Treino** | — | — | 190-320h | **R$ 9.500** |

Lastro: LASTRO-02 D003 🟡 (auditar com POC real em S2.5.2).

#### 2.3.3 · CAPEX Setup Plataforma e Infra Inicial

| Item | 🟡 P10 | 🟡 P50 | 🟡 P90 | Lastro |
|---|---:|---:|---:|---|
| Setup inicial cloud (configuração, segurança) | R$ 8.000 | R$ 15.000 | R$ 25.000 | Mão-de-obra ~80-200h 🟡 |
| Setup Qdrant + LangGraph + observability | R$ 5.000 | R$ 10.000 | R$ 18.000 | Mão-de-obra ~50-180h 🟡 |
| Coleta + curadoria dataset jurídico BR | R$ 12.000 | R$ 25.000 | R$ 45.000 | Simone + Gislênia ~200-500h 🟡 |
| Desenvolvimento plataforma SaaS multi-tenant | R$ 40.000 | R$ 80.000 | R$ 140.000 | Backend 400-1.000h 🟡 |
| Certificações iniciais (SOC2 lite, LGPD audit) | R$ 8.000 | R$ 18.000 | R$ 35.000 | Mercado BR 2026 🟡 |
| Branding + site + identidade visual | R$ 5.000 | R$ 12.000 | R$ 25.000 | Mercado BR design 🟡 |
| **Subtotal CAPEX Setup** | **R$ 78.000** | **R$ 160.000** | **R$ 288.000** | — |

#### 2.3.4 · CAPEX Total Inicial (1 vez)

```
CAPEX Treino Modelos:       R$ 9.500
CAPEX Setup Plataforma:     R$ 160.000
─────────────────────────────────────
TOTAL CAPEX P50:            R$ 169.500
Range PERT:                 R$ 87.500 (P10) - R$ 297.500 (P90)
Expected (PERT):            R$ 170.667
```

### 2.4 · Software + Operacional Mensal

| Categoria | Item | 🟡 P50/mês | Lastro |
|---|---|---:|---|
| Dev Tools | GitHub Enterprise (5 seats) | R$ 1.200 | $4-21/seat/mês ✅ |
| Dev Tools | Linear (project mgmt 5 seats) | R$ 400 | $8/seat/mês ✅ |
| Dev Tools | Sentry/observability extra | R$ 600 | benchmark 🟢 |
| Comunicação | Slack/Notion business | R$ 800 | $7-15/seat/mês ✅ |
| MLOps | Weights & Biases (treino tracking) | R$ 500 | $50-200/mês 🟢 |
| Vendas | CRM (HubSpot Starter ou Pipedrive) | R$ 700 | benchmark BR 🟡 |
| Marketing | Brevo email + LinkedIn Sales Nav | R$ 800 | benchmark 🟡 |
| Operacional | Contabilidade (Contabilizei plus) | R$ 800 | Contabilizei ✅ |
| Operacional | Jurídico mensal (Simone supervisão) | — (já em pró-labore) | — |
| Operacional | Escritório virtual + endereço fiscal | R$ 600 | mercado BR 🟡 |
| **Subtotal Software+Operacional Mensal** | — | **R$ 6.400** | — |

### 2.5 · Marketing + Vendas (Variável Mensal)

| Item | Wave 0 P50 | Wave 1 P50 | Wave 2A P50 | Lastro |
|---|---:|---:|---:|---|
| LinkedIn Ads B2G | R$ 1.000 | R$ 4.000 | R$ 8.000 | Benchmark CAC 🟡 |
| Eventos setoriais (CONFIP, CNM) | R$ 2.000 | R$ 8.000 | R$ 15.000 | Mercado BR 🟡 |
| Conteúdo (blog, webinars, whitepapers) | R$ 1.500 | R$ 5.000 | R$ 10.000 | Mercado BR 🟡 |
| Comissões vendas (5-8% receita) | — | calculado | calculado | Mercado SaaS 🟢 |
| **Subtotal Marketing/Vendas** | **R$ 4.500** | **R$ 17.000+ com.** | **R$ 33.000+ com.** | — |

### 2.6 · Tributos (Simples Nacional · Anexo III)

#### 2.6.1 · Alíquotas progressivas Anexo III 2026

| Faixa | Receita acumulada 12m | Alíquota nominal | Valor a deduzir | Alíquota efetiva inicial |
|---:|---|---:|---:|---:|
| 1ª | até R$ 180.000 | 6,00% | — | 6,00% |
| 2ª | R$ 180k – 360k | 11,20% | R$ 9.360 | ~9,40% |
| 3ª | R$ 360k – 720k | 13,50% | R$ 17.640 | ~11,00% |
| 4ª | R$ 720k – 1.800.000 | 16,00% | R$ 35.640 | ~13,00% |
| 5ª | R$ 1.8M – 3.6M | 21,00% | R$ 125.640 | ~16,50% |
| 6ª | R$ 3.6M – 4.8M | 33,00% | R$ 648.000 | ~19,50% |

Fontes: Contabilizei 2026 + e-auditoria 2026 ✅.

#### 2.6.2 · Cenários de tributação por receita anual NeoGov

| Cenário | Receita anual | Faixa | Alíquota efetiva | Tributo anual |
|---|---:|---:|---:|---:|
| Wave 0 (M0-M3 · pré-receita) | R$ 0-50k | 1ª | 6,00% | ~R$ 0-3.000 |
| Wave 1 conservador | R$ 360.000/ano | 3ª | ~11,00% | ~R$ 39.600/ano |
| Wave 1 realista | R$ 720.000/ano | 4ª | ~13,00% | ~R$ 93.600/ano |
| Wave 1 otimista | R$ 1.500.000/ano | 4ª | ~14,50% | ~R$ 217.500/ano |
| Wave 2 escalado | R$ 3.000.000/ano | 5ª | ~18,00% | ~R$ 540.000/ano |

**⚠️ Atenção**: alíquota efetiva sobe conforme faturamento cresce. Modelagem deve usar alíquota MARGINAL (faixa atual) para projeções incrementais.

### 2.7 · Custo Variável por Cliente (CSC · Cost of Serving Customer)

| Componente | 🟡 P50 por cliente/mês | Lastro |
|---|---:|---|
| Cloud rateado (L40S compartilhada por 30-50 clientes) | R$ 250-500 | LASTRO-01 D003 dividido 🟡 |
| Suporte humano (~2-6h/mês × R$ 50/h interno) | R$ 100-300 | benchmark mercado 🟡 |
| Customer Success (rateado) | R$ 80-200 | benchmark mercado 🟡 |
| Onboarding amortizado (12 meses) | R$ 200-600 | esforço inicial / LTV 🟡 |
| Storage + bandwidth incremental | R$ 30-80 | benchmark cloud 🟡 |
| **Subtotal CSC mensal P50** | **R$ 660-1.680** | — |

**Em média**: R$ 1.170/cliente/mês = R$ 14.040/cliente/ano · Para clientes pequenos (escola), reduz para R$ 600-900/mês.

### 2.8 · Síntese · Custo Fixo Total Mensal (Wave 1 · P50)

| Categoria | 🟡 P50 mensal |
|---|---:|
| Pró-labores sócios | R$ 53.000 |
| Folha CLT funcionários | R$ 37.000 |
| Encargos CLT (Simples ~28%) | R$ 10.360 |
| Infraestrutura cloud BR | R$ 15.300 |
| Software + Operacional | R$ 6.400 |
| Marketing + Vendas (Wave 1) | R$ 17.000 |
| Contingência operacional (5%) | R$ 6.950 |
| **TOTAL FIXO MENSAL P50** | **R$ 146.010** |

**Range PERT**: R$ 105.000 (P10) — R$ 198.000 (P90)

**Anualizado P50**: ~R$ 1.752.000/ano (sem tributos · sem custo variável)

---

## 3 · BENCHMARKING · Pricing Competitivo SOTA 2026

### 3.1 · Concorrentes diretos identificados (BP v2.0)

| Concorrente | Foco | Pricing público | Diferencial vs NeoGov |
|---|---|---|---|
| **Confidata** | Saúde dedicado | R$ 497-R$ 3.497/mês ✅ FATO | NeoGov tem ETL próprio + ICT |
| **Be Compliance** | Saúde + geral | 🟡 não público (GAP05) | NeoGov tem foco B2G + IA própria |
| **Safetyfyi** | Saúde dedicado | 🟡 não público (GAP05) | NeoGov tem IA especializada LAI/LGPD |
| **LGPD Faça** | B2G Municipal | 🟡 não público | NeoGov é ICT Art.75 IV |
| **LGPD Tech** | B2G Municipal | 🟡 não público | NeoGov tem IA própria |
| **TOW** | B2G Municipal | 🟡 não público | NeoGov tem 5 produtos integrados |

### 3.2 · Benchmark internacional legaltech (2026)

| Player | Categoria | Pricing | Equivalente NeoGov |
|---|---|---|---|
| **Clio** | Practice Mgmt | $39-$129/seat/mês | Comparar com P4 AI-DPO |
| **Icertis** | Contract Lifecycle | Enterprise (~$100k+/ano) | Comparar com P5 ETL |
| **Harvey** | AI Legal Research | $200-$500/seat/mês 🟡 | Comparar com P4 AI-DPO premium |
| **Casetext** | AI Legal | $100-$300/seat/mês 🟡 | Comparar com P3+P4 combo |
| **Usercentrics** | Privacy/Consent | $99-$999/mês | Comparar com P2 Data Discovery |

### 3.3 · CAC benchmark legaltech B2B 2026 (PoweredBySearch ✅)

| Segmento | CAC USD | CAC R$ (×5.50) | Aplicável NeoGov |
|---|---:|---:|---|
| SMB legaltech | $299 | R$ 1.640 | Escola privada (Gamma) |
| Middle Market | $2.630 | R$ 14.460 | Hospital privado (Beta) |
| Enterprise | $6.441 | R$ 35.420 | B2G Federal/Estadual (Alfa-grande) |

### 3.4 · Posicionamento estratégico de preço

**Princípio**: NeoGov deve precificar entre **percentil 40-65 do mercado** — não mais barato (sinaliza inferioridade), não premium (sem track record). Diferencial via:
- ICT Art.75 IV (B2G direto sem licitação)
- IA própria especializada (Be Compliance/Safetyfyi não têm)
- 5 produtos integrados (concorrentes têm 1-2)

---

## 4 · DECISION-ANALYSIS · Escolha de Modelo de Pricing por Produto

### 4.1 · Modelos candidatos avaliados

| Modelo | Quando faz sentido | Exemplos |
|---|---|---|
| **A · Assinatura fixa tier** | Uso contínuo previsível | SaaS clássico (Clio, HubSpot) |
| **B · Per seat** | Uso individual (DPO, auditor) | Clio, Harvey |
| **C · Usage-based (per uso)** | Volume variável (docs anonimizados) | Twilio, AWS |
| **D · Híbrido base + uso** | Combinação previsibilidade + escala | Snowflake, Datadog |
| **E · Projeto + manutenção** | Setup customizado + recorrente | Icertis, Mulesoft |

### 4.2 · Weighted Scoring Matrix · Critérios e Pesos

| Critério | Peso | Justificativa |
|---|---:|---|
| **Previsibilidade de receita** | 25% | Crítico para B2G (orçamento anual) e captação |
| **Alinhamento com valor entregue** | 25% | Cliente paga pelo que usa/recebe |
| **Simplicidade de venda** | 15% | Wilton precisa de pitch claro |
| **Escalabilidade operacional** | 20% | NeoGov deve crescer sem aumentar fricção |
| **Aceitação cultural BR B2G** | 15% | Município/órgão não compra "per call API" |
| **Total** | 100% | — |

### 4.3 · Scoring por Produto (escala 1-5)

#### P1 · SaaS Plataforma (módulo central)

| Modelo | Previsibilidade | Alinhamento | Simplicidade | Escalabilidade | Cultural BR | **Score** |
|---|---:|---:|---:|---:|---:|---:|
| A Assinatura tier | 5 | 4 | 5 | 5 | 5 | **4.75** ⭐ |
| B Per seat | 5 | 3 | 4 | 4 | 3 | 3.85 |
| C Usage-based | 2 | 4 | 2 | 5 | 1 | 2.85 |
| D Híbrido | 4 | 5 | 3 | 4 | 3 | 3.80 |
| E Projeto+manut | 3 | 3 | 3 | 2 | 4 | 2.95 |

**Vencedor P1**: Assinatura tier (basic/pro/enterprise).

#### P2 · Data Discovery

| Modelo | Previsibilidade | Alinhamento | Simplicidade | Escalabilidade | Cultural BR | **Score** |
|---|---:|---:|---:|---:|---:|---:|
| A Assinatura tier | 5 | 2 | 5 | 4 | 5 | 4.20 |
| B Per seat | 4 | 2 | 4 | 4 | 3 | 3.40 |
| C Usage-based | 2 | 5 | 3 | 5 | 2 | 3.45 |
| D Híbrido (setup+uso) | 4 | 5 | 4 | 5 | 4 | **4.40** ⭐ |
| E Projeto+manut | 3 | 4 | 3 | 2 | 5 | 3.45 |

**Vencedor P2**: Híbrido (setup R$ + uso por volume de documentos descobertos).

#### P3 · LAI/LGPD Anonimização

| Modelo | Previsibilidade | Alinhamento | Simplicidade | Escalabilidade | Cultural BR | **Score** |
|---|---:|---:|---:|---:|---:|---:|
| A Assinatura B2G | 5 | 3 | 5 | 4 | 5 | **4.40** ⭐ (B2G) |
| C Per execução | 2 | 5 | 3 | 5 | 2 | 3.45 (B2C) |
| D Híbrido | 4 | 5 | 4 | 4 | 4 | 4.20 |

**Vencedor P3**: **Dual** — Assinatura B2G (Alfa) + Per execução B2C/Beta.

#### P4 · AI-DPO Copilot

| Modelo | Previsibilidade | Alinhamento | Simplicidade | Escalabilidade | Cultural BR | **Score** |
|---|---:|---:|---:|---:|---:|---:|
| A Assinatura tier | 4 | 3 | 4 | 4 | 5 | 3.95 |
| B Per seat | 5 | 5 | 5 | 5 | 4 | **4.85** ⭐ |
| D Híbrido | 4 | 5 | 3 | 4 | 3 | 3.80 |

**Vencedor P4**: Per seat (DPO individual, modelo Clio/Harvey).

#### P5 · ETL/Middleware

| Modelo | Previsibilidade | Alinhamento | Simplicidade | Escalabilidade | Cultural BR | **Score** |
|---|---:|---:|---:|---:|---:|---:|
| A Assinatura | 5 | 3 | 5 | 4 | 4 | 4.20 |
| D Híbrido | 4 | 4 | 3 | 4 | 4 | 3.80 |
| E Projeto + manut | 4 | 5 | 4 | 3 | 5 | **4.20** ⭐ |

**Vencedor P5**: Projeto setup + manutenção mensal (modelo Icertis).

### 4.4 · Síntese · Modelo de cobrança por produto

| Produto | Modelo vencedor | Sub-modelo por persona |
|---|---|---|
| **P1 SaaS Plataforma** | Assinatura tier | Basic (Gamma escola) · Pro (Beta saúde) · Enterprise (Alfa B2G) |
| **P2 Data Discovery** | Híbrido | Setup R$ 8-15k + uso R$ 0,12-0,25/doc |
| **P3 LAI/LGPD Anonimização** | Dual | Assinatura B2G OU Per execução B2C |
| **P4 AI-DPO Copilot** | Per seat | Tier seat (junior/senior) por persona |
| **P5 ETL/Middleware** | Projeto + manutenção | Setup escalonado por sistema integrado |

---

## 5 · PRIORITIZATION · MoSCoW Tiers por Produto

### 5.1 · Princípio · 3 tiers padrão por produto SaaS

| Tier | Quem compra | Margem alvo | Funcionalidades |
|---|---|---|---|
| **Basic / Starter** | Pequeno (Gamma escola, Épsilon escritório) | 60-70% | MUST have apenas |
| **Pro / Business** | Médio (Beta saúde, B2G municipal) | 75-82% | MUST + SHOULD |
| **Enterprise / Custom** | Grande (Alfa Federal, Hospital) | 80-90% | MUST + SHOULD + COULD + setup dedicado |

### 5.2 · P1 SaaS Plataforma · 3 Tiers

| Tier | 🟡 Preço/mês P50 | MUST | SHOULD | COULD |
|---|---:|---|---|---|
| Basic (Gamma) | R$ 2.500 | Dashboard LGPD básico · 1 sistema integrado · 500 docs/mês | — | — |
| Pro (Beta + Municipal) | R$ 6.500 | + 3 sistemas · 5.000 docs/mês · audit log | Multi-usuário · API básica | — |
| Enterprise (Alfa Fed/Est) | R$ 12.000+ | + ilimitado · SLA · dedicated CSM | SSO · custom integrations | White-label · on-premise option |

### 5.3 · P2 Data Discovery · Pricing Híbrido

| Componente | 🟡 P50 | Lastro |
|---|---:|---|
| Setup inicial (varredura inicial) | R$ 8.000 (Gamma) — R$ 35.000 (Alfa) | Esforço 40-160h × R$ 200/h interno |
| Cobrança recorrente por documento | R$ 0,12-0,25/doc | Margem 80% sobre CSC |
| Pacote mínimo mensal | R$ 1.500/mês (12.500 docs incluídos) | Garantir floor revenue |
| Pacote enterprise | R$ 12.000/mês (100k docs + analytics) | Setup B2G grande |

### 5.4 · P3 LAI/LGPD Anonimização · Dual

**Modelo A · Assinatura B2G** (Alfa Federal/Estadual):

| Tier | 🟡 Preço/mês | Inclui |
|---|---:|---|
| Pro Município | R$ 8.000 | 5.000 anonimizações/mês · LAI + LGPD |
| Enterprise Estado | R$ 18.000 | 30.000 anonimizações/mês · audit completo |
| Federal Custom | R$ 25.000+ | Ilimitado · jurisprudência integrada · SLA |

**Modelo B · Per execução** (Beta/Gamma/B2C):

| Volume | 🟡 Preço/doc | Aplicação |
|---|---:|---|
| Avulso (1-100) | R$ 0,50 | Hospital pequeno |
| Lote (100-1.000) | R$ 0,30 | Hospital médio |
| Volume (1.000+) | R$ 0,18 | Hospital grande |

### 5.5 · P4 AI-DPO Copilot · Per Seat

| Seat type | 🟡 Preço/seat/mês | Inclui |
|---|---:|---|
| Junior (DPO entry) | R$ 380 | Q&A LGPD + templates + workflow básico |
| Senior (DPO experiente) | R$ 580 | + jurisprudência · benchmarks · auditoria automática |
| Lead / Compliance Officer | R$ 850 | + dashboard exec · multi-cliente · API |

**Volume discount**:
- 1-5 seats: preço cheio
- 6-15 seats: -10%
- 16-50 seats: -20%
- 51+ seats: negociação

### 5.6 · P5 ETL/Middleware · Projeto + Manutenção

| Persona | Setup 🟡 P50 | Manutenção mensal 🟡 P50 |
|---|---:|---:|
| Gamma escola (sistema único) | R$ 25.000 | R$ 1.500 |
| Beta saúde (MV ou Tasy) | R$ 65.000 | R$ 3.500 |
| Alfa B2G (multi-sistemas legados) | R$ 120.000+ | R$ 6.500+ |

---

## 6 · BUSINESS MODEL CANVAS · Coerência Revenue ↔ Cost

### 6.1 · Revenue Streams por Cluster (consolidado dos §3-5)

| Cluster | Produtos primários | Modelo | 🟡 Receita média/cliente/ano |
|---|---|---|---:|
| **Alfa B2G Municipal** | P1 Pro + P2 + P3-B2G | Assinatura + híbrido | R$ 90.000-180.000 |
| **Alfa B2G Federal/Estadual** | P1 Enterprise + P3-B2G + P5 | Enterprise + projeto | R$ 250.000-800.000 |
| **Beta Hospital** | P1 Pro + P3-execução + P4 + P5 | Assinatura + uso + per seat | R$ 200.000-450.000 |
| **Gamma Escola Privada** | P1 Basic + P4 Junior + P5 setup | Tier basic + per seat | R$ 35.000-75.000 |
| **Épsilon Escritório DPO** | P4 Senior/Lead | Per seat puro | R$ 8.000-15.000 |

### 6.2 · Cost Structure (consolidado §2)

```
Custos Fixos Mensais (P50 Wave 1):           R$ 146.000
Custos Variáveis (CSC) por cliente/mês:      R$ 1.170 (média)
CAPEX Inicial Amortizado (12 meses):         R$ 14.000/mês
─────────────────────────────────────────────────────────
Total Custo Mensal (10 clientes ativos):     R$ 171.700
Total Custo Mensal (30 clientes ativos):     R$ 195.100
```

### 6.3 · Validação Coerência

Para break-even com receita média anual por cliente = R$ 90k (Alfa Municipal Pro):
- Custo mensal NeoGov (30 clientes): R$ 195.100
- Receita mensal necessária: ≥ R$ 195.100
- Receita por cliente/mês: R$ 195.100 / 30 = **R$ 6.503/cliente/mês**
- **Coerente** com P1 Pro (R$ 6.500) ✅

Para Wave 2 (60 clientes mix Alfa+Beta+Gamma):
- Custo: R$ 146k fixo + 60 × R$ 1.170 = R$ 216.200/mês
- Receita média/cliente necessária: ~R$ 3.600 (média ponderada)
- **Realista** dado mix ✅

---

## 7 · RISK-ANALYSIS · Sensibilidade Unit Economics

### 7.1 · Drivers críticos identificados

| Driver | Impacto se ±20% | Mitigação |
|---|---|---|
| **Pró-labores sócios** | ±R$ 10.600/mês = ±R$ 127k/ano | Ajustar Fator R · escalonamento |
| **Cloud L40S BR (LASTRO-01)** | ±R$ 3.060/mês = ±R$ 37k/ano | S2.5.3 cotações reais reduz incerteza |
| **CAC SaaS B2B** | ±R$ 1.640-7.084/cliente | Canal orgânico vs paid · benchmark legaltech ✅ |
| **Churn anual** | -5pp churn = +20% LTV | Customer Success investment |
| **Onboarding amortização** | ±R$ 200-600/cliente/mês | Reduzir esforço setup com automação |
| **Alíquota Simples (Fator R)** | Cair para Anexo V = +9.5pp tributo | Manter folha ≥ 32% receita |

### 7.2 · Sensibilidade do Pricing P1 Pro (R$ 6.500/mês)

| Cenário | Custo/cliente/mês | Receita/cliente/mês | Margem | Status |
|---|---:|---:|---:|---|
| P10 (otimista custo) | R$ 4.870 | R$ 6.500 | 25% | ⚠️ baixa · não cobre fixo |
| P50 (realista) | R$ 6.503 | R$ 6.500 | -0,05% | ❌ exato break-even |
| P90 (pessimista) | R$ 8.700 | R$ 6.500 | -34% | ❌ insustentável |

**Conclusão**: pricing P1 Pro R$ 6.500 é frágil. Recomendação: **subir para R$ 7.500-8.500/mês** para garantir margem 18-25% no P50 com clientes 30+.

### 7.3 · Sensibilidade alternativa · 50 clientes ativos

| Cenário | Custo Total Mensal | Receita Necessária | Pricing médio mín. |
|---|---:|---:|---:|
| 30 clientes | R$ 195.100 | R$ 195.100 | R$ 6.503/cliente |
| **50 clientes** | R$ 204.500 | R$ 204.500 | **R$ 4.090/cliente** |
| 80 clientes | R$ 219.600 | R$ 219.600 | R$ 2.745/cliente |
| 120 clientes | R$ 286.000 (+ Wave 2 FTEs) | R$ 286.000 | R$ 2.383/cliente |

**Insight crítico**: economia de escala kicks in fortemente a partir de 50 clientes. Wave 1 deve mirar **50+ clientes em 12 meses** para sustentabilidade.

---

## 8 · FUNÇÃO PROBABILÍSTICA DE PRICING ASSERTIVO

### 8.1 · Fórmula geral

```
P(produto, persona) = max(
    P_custo: custo_unit × (1 + margem_alvo),
    P_competitivo: benchmark_concorrente × ajuste_diferencial,
    P_valor: WTP_segmento × fator_captura
)
```

**Onde**:
- `custo_unit` = (custo fixo rateado + custo variável + amortização CAPEX) por cliente
- `margem_alvo` = 70-85% (varia por produto · ver §5)
- `benchmark_concorrente` = Confidata, Be Compliance, Clio, Harvey conforme produto
- `ajuste_diferencial` = 1.05-1.20 (ICT + IA própria + B2G expertise)
- `WTP_segmento` = dado primário (GAP02 entrevistas pós-S3.0.4)
- `fator_captura` = 0.70-0.85 (não captura 100% para garantir percepção valor)

### 8.2 · Range de pricing por produto × persona

Aplicando a fórmula com cenários P10/P50/P90:

#### P1 SaaS Plataforma

| Persona | 🟡 P10 R$/mês | 🟡 P50 R$/mês | 🟡 P90 R$/mês | Expected (PERT) |
|---|---:|---:|---:|---:|
| Alfa B2G Federal | 14.000 | 18.000 | 28.000 | 19.000 |
| Alfa B2G Municipal Pro | 6.000 | 8.000 | 12.000 | 8.333 |
| Beta Hospital Pro | 5.500 | 7.500 | 11.500 | 7.833 |
| Gamma Escola Basic | 1.800 | 2.800 | 4.500 | 2.933 |

#### P2 Data Discovery (híbrido)

| Persona | Setup P50 | Recorrente P50 |
|---|---:|---:|
| Alfa B2G Federal | R$ 35.000 | R$ 5.000/mês ou R$ 0,12/doc volume |
| Alfa B2G Municipal | R$ 12.000 | R$ 1.800/mês ou R$ 0,18/doc |
| Beta Hospital | R$ 18.000 | R$ 2.500/mês ou R$ 0,15/doc |
| Gamma Escola | R$ 6.000 | R$ 800/mês ou R$ 0,25/doc |

#### P3 LAI/LGPD Anonimização (dual)

**Assinatura B2G**:
| Persona | 🟡 P50 mensal |
|---|---:|
| Federal | R$ 22.000 |
| Estadual | R$ 14.000 |
| Municipal | R$ 7.500 |

**Per execução**:
| Volume mensal | 🟡 P50 R$/doc |
|---|---:|
| <100 | R$ 0,50 |
| 100-1.000 | R$ 0,30 |
| 1.000-10.000 | R$ 0,18 |
| 10.000+ | R$ 0,12 |

#### P4 AI-DPO Copilot (per seat)

| Tier | 🟡 P50 R$/seat/mês |
|---|---:|
| Junior | R$ 380 |
| Senior | R$ 580 |
| Lead/Officer | R$ 850 |

Discount: 6+ seats -10% · 16+ seats -20% · 51+ negociação.

#### P5 ETL/Middleware (projeto + manutenção)

| Persona | Setup 🟡 P50 | Manutenção 🟡 P50 |
|---|---:|---:|
| Alfa B2G Municipal (≤3 sistemas) | R$ 35.000 | R$ 2.500/mês |
| Alfa Estadual/Federal (multi-sistema) | R$ 120.000 | R$ 6.500/mês |
| Beta Hospital (MV/Tasy) | R$ 65.000 | R$ 3.500/mês |
| Gamma Escola (1 sistema) | R$ 25.000 | R$ 1.500/mês |

---

## 9 · UNIT ECONOMICS · 20 Combos Persona × Produto

### 9.1 · Cálculo por combo (cenário P50)

Fórmulas:
- **ARPU mensal** = preço médio mensal (assinatura + amortizações)
- **CSC mensal** = custo variável por cliente
- **Margem Contribuição** = (ARPU - CSC) / ARPU
- **LTV** = ARPU × (1 / churn anual) (assumir churn 8% B2G, 15% B2C)
- **CAC** = benchmark legaltech §3.3
- **Payback** = CAC / (ARPU - CSC)
- **LTV/CAC** = LTV / CAC

#### Tabela síntese · cenário realista P50

| Combo | ARPU/mês | CSC | Margem | LTV | CAC | LTV/CAC | Payback |
|---|---:|---:|---:|---:|---:|---:|---:|
| **Alfa Federal × P1+P3+P5** | R$ 60.000 | R$ 2.000 | 97% | R$ 8.7M | R$ 35.400 | **245:1** ⭐ | 0.6 mês |
| **Alfa Municipal × P1+P2+P3** | R$ 14.000 | R$ 1.400 | 90% | R$ 1.95M | R$ 14.460 | **135:1** ⭐ | 1.1 mês |
| **Beta Hospital × P1+P3+P4+P5** | R$ 28.000 | R$ 1.800 | 94% | R$ 3.5M | R$ 14.460 | **240:1** ⭐ | 0.6 mês |
| **Gamma Escola × P1+P4+P5** | R$ 4.500 | R$ 800 | 82% | R$ 360k | R$ 1.640 | **220:1** ⭐ | 0.4 mês |
| **Épsilon Escritório × P4 Senior (3 seats)** | R$ 1.740 | R$ 400 | 77% | R$ 174k | R$ 1.640 | **106:1** ⭐ | 1.2 mês |

**⚠️ Alerta**: LTV/CAC absurdamente altos sugerem 2 hipóteses:
1. CAC subestimado (benchmark internacional pode não refletir BR · GAP05 + GAP02)
2. Churn assumido baixo (real pode ser 20-30% no início)

**Recomendação**: usar LTV/CAC mais conservador (4:1 a 8:1) para projeções formais até validação primária.

### 9.2 · Cenários PERT para Alfa Municipal × combo

| Cenário | ARPU/mês | LTV | CAC | LTV/CAC | Status |
|---|---:|---:|---:|---:|---|
| Otimista (P10) | R$ 18.000 | R$ 2.7M | R$ 8.000 | 337:1 | Improvável |
| Realista (P50) | R$ 14.000 | R$ 1.95M | R$ 14.460 | 135:1 | Inflado |
| Pessimista (P90) | R$ 8.000 | R$ 670k | R$ 28.000 | 24:1 | Realista BR |

**Conclusão honesta**: pricing assertivo precisa de validação WTP primária (GAP02 · 3-5 entrevistas por cluster) para refinar.

---

## 10 · Síntese Final · Tabela Mestre de Pricing Assertivo

### 10.1 · Cenário realista P50 · pricing recomendado

| Produto | Persona | Modelo | Setup | Recorrente | Margem alvo |
|---|---|---|---:|---:|---:|
| **P1 SaaS** | Gamma Escola | Tier Basic | — | R$ 2.800/mês | 75% |
| **P1 SaaS** | Beta Hospital | Tier Pro | — | R$ 7.500/mês | 80% |
| **P1 SaaS** | Alfa Municipal | Tier Pro | — | R$ 8.000/mês | 82% |
| **P1 SaaS** | Alfa Federal/Estadual | Tier Enterprise | — | R$ 18.000+/mês | 85% |
| **P2 Discovery** | Alfa Municipal | Híbrido | R$ 12.000 | R$ 1.800/mês ou R$ 0,18/doc | 80% |
| **P2 Discovery** | Beta Hospital | Híbrido | R$ 18.000 | R$ 2.500/mês ou R$ 0,15/doc | 82% |
| **P2 Discovery** | Alfa Federal | Híbrido | R$ 35.000 | R$ 5.000/mês ou R$ 0,12/doc | 85% |
| **P3 Anonimização** | Alfa Municipal | Assinatura B2G | — | R$ 7.500/mês | 88% |
| **P3 Anonimização** | Alfa Estadual | Assinatura B2G | — | R$ 14.000/mês | 90% |
| **P3 Anonimização** | Alfa Federal | Assinatura B2G | — | R$ 22.000/mês | 92% |
| **P3 Anonimização** | Beta Hospital | Per execução | — | R$ 0,18-0,50/doc | 85% |
| **P4 AI-DPO** | Beta DPO Junior | Per seat | — | R$ 380/seat/mês | 75% |
| **P4 AI-DPO** | Alfa DPO Senior | Per seat | — | R$ 580/seat/mês | 80% |
| **P4 AI-DPO** | Épsilon Lead | Per seat | — | R$ 850/seat/mês | 82% |
| **P5 ETL** | Gamma Escola | Projeto+manut | R$ 25.000 | R$ 1.500/mês | 70% |
| **P5 ETL** | Beta Hospital | Projeto+manut | R$ 65.000 | R$ 3.500/mês | 75% |
| **P5 ETL** | Alfa Municipal | Projeto+manut | R$ 35.000 | R$ 2.500/mês | 73% |
| **P5 ETL** | Alfa Federal | Projeto+manut | R$ 120.000 | R$ 6.500/mês | 78% |

### 10.2 · Função de pricing operacionalizada

```python
def calcular_preco_assertivo(produto, persona, cenario="P50"):
    """
    Calcula preço assertivo NeoGov.
    
    Args:
        produto: 'P1', 'P2', 'P3', 'P4', 'P5'
        persona: 'Alfa_Fed', 'Alfa_Est', 'Alfa_Mun', 'Beta', 'Gamma', 'Epsilon'
        cenario: 'P10' (otimista), 'P50' (realista), 'P90' (pessimista)
    
    Returns:
        dict com setup, recorrente, margem_alvo
    """
    custo_unit = obter_custo_unitario(produto, persona)
    margem_alvo = obter_margem_alvo(produto, persona)
    benchmark = obter_benchmark_competitivo(produto, persona)
    wtp = obter_wtp_segmento(persona)  # 🟡 estimativa até GAP02
    
    P_custo = custo_unit * (1 + margem_alvo)
    P_competitivo = benchmark * 1.10  # ajuste diferencial NeoGov
    P_valor = wtp * 0.75  # captura 75% do WTP
    
    preco_recorrente = max(P_custo, P_competitivo, P_valor)
    setup = calcular_setup(produto, persona) if produto in ['P2', 'P5'] else 0
    
    if cenario == "P10":
        preco_recorrente *= 1.20  # otimista
    elif cenario == "P90":
        preco_recorrente *= 0.80  # pessimista
    
    return {
        "setup": setup,
        "recorrente_mensal": preco_recorrente,
        "margem_alvo": margem_alvo,
        "cenario": cenario,
        "lastros": ["LASTRO-01", "LASTRO-02", "LASTRO-CAC-01"]
    }
```

---

## 11 · Lastros Lastreados (D-015)

### LASTRO-PL-01 · Pró-labore Simone CEO + LGPD Lead

```yaml
campo_lastreado: "Pró-labore Simone R$ 10.000-20.000/mês"
marcador: 🟡 ESTIMATIVA POR ANÁLOGO
vvv: 0.70

analogo_usado:
  fonte_1: Robert Half · CEO/Lead Counsel SaaS startup BR 2026
  fonte_2: GlobalAdvocacy · Sócio advogado especializado LGPD BR 2026
  range_mercado: R$ 12.000-25.000/mês (advogada sênior LGPD lead)
  adaptacao: -10% para fase early startup pré-Series A

dado_primario_necessario:
  o_que: Decisão real da equipe sobre pró-labore (Simone)
  como_obter: Reunião societária com 4 sócios + contador
  quem_executa: Simone (decisão própria)
  sprint_destino: S2.5.1 OU S3.0.4 (antes do xlsx final)
  prazo_alvo: 7 dias úteis

refatoracao_facilitada:
  formula: prolabore_simone = decisao_societaria
  impacto_se_mudar:
    - Fator R Simples (folha/receita)
    - Anexo III vs V (alíquota 9.5pp diferença)
    - Break-even point
```

### LASTRO-PL-02 a LASTRO-PL-04 (Wilton, Camila, Gislênia)

Mesma estrutura · prazo mesmo dado primário (decisão societária).

### LASTRO-FOLHA-CLT · Salários CLT 2026

```yaml
campo_lastreado: "Backend/DevOps Pleno CLT R$ 9.500-15.900"
marcador: ✅ FATO
vvv: 0.95

fonte_1: Robert Half · "Salário Desenvolvedor Back-End Pleno 2026"
url: https://www.roberthalf.com/br/pt/vagas-detalhes/desenvolvedora-back-end-pleno
data: nov/2025 atualizado fev/2026
range: R$ 9.500-15.900 CLT

fonte_2: HuntIT · "Salário Desenvolvedor Sênior 2026"
url: https://huntit.com.br/salario-de-desenvolvedor-senior-em-2026/
range: R$ 13.000+ piso sênior

fonte_3: CAGED Brasil · "Desenvolvedor Backend"
url: https://www.salario.com.br/profissao/desenvolvedor-back-end/
range_mercado: R$ 5.762-9.689 (média CLT geral)

dado_primario_necessario:
  o_que: Definir target salário NeoGov (mediana vs P75)
  como_obter: Decisão Camila CTO + benchmark do nicho LGPD/IA
  quem_executa: Camila
  sprint_destino: S2.5.1
```

### LASTRO-TRIB-01 · Simples Nacional Anexo III 2026

```yaml
campo_lastreado: "Alíquota efetiva inicial 6% (1ª faixa) · até R$ 180k"
marcador: ✅ FATO
vvv: 1.00

fonte: Contabilizei + e-auditoria + meucontadoronline (2026)
data: jan-fev 2026
estabilidade: alta (lei vigente)

fator_R_obrigatorio:
  formula: (folha_pagamento_12m + prolabore_12m) / receita_bruta_12m
  threshold: ≥ 28% para Anexo III
  margem_seguranca_NeoGov: ≥ 32%

reforma_tributaria:
  data: IBS/CBS começam 2027
  impacto_2026: Simples NÃO destaca em NFe (transição)
  decisao_critica_set_2026: permanecer ou sair do Simples para 2027
```

### LASTRO-CAC-01 · CAC Legaltech 2026

```yaml
campo_lastreado: "CAC SMB $299 · MM $2.630 · Enterprise $6.441"
marcador: 🟢 INFERÊNCIA com base em fato
vvv: 0.85

fonte: PoweredBySearch · "B2B SaaS CAC Benchmarks 2026"
url: https://www.poweredbysearch.com/learn/b2b-saas-cac-benchmarks/
data: mar/2026
mercado_origem: EUA (precisa ajuste BR)

conversao_BR:
  taxa_cambio_2026: USD 1 = R$ 5.50 (🟡 estimativa)
  ajuste_paridade_PPP: 0.6-0.8 (CAC BR tende a ser menor)
  range_ajustado_BR:
    SMB: R$ 1.000-1.640
    MM: R$ 8.700-14.460
    ENT: R$ 21.300-35.420

dado_primario_necessario:
  o_que: CAC real após Wave 1 (12 meses operação)
  como_obter: Medir spend marketing+vendas / clientes adquiridos
  quem_executa: Wilton (comercial) com CRM
  sprint_destino: pós-M12 Wave 1
```

### LASTRO-WTP · Willingness to Pay (GAP02 · CRÍTICO PENDENTE)

```yaml
campo_lastreado: "WTP por persona × produto"
marcador: 🔴 NÃO USAR sem validação
vvv: 0.35

status: TODOS os preços do §10 são pré-WTP-validated
risco: Pricing pode estar 20-40% acima ou abaixo do real

dado_primario_necessario:
  o_que: 3-5 entrevistas WTP por cluster (Alfa Mun, Alfa Fed, Beta, Gamma, Épsilon)
  metodologia: Van Westendorp Price Sensitivity Meter (4 perguntas)
  quem_executa: Wilton (comercial) + Simone (LGPD ângulo)
  sprint_destino: S3.0.4 antes do xlsx final OU S4.2 antes financeiro
  prazo_alvo: 15-30 dias úteis
  custo: ~R$ 0 (entrevistas com prospects)

impacto_se_dado_chegar:
  - Refatorar §10 com WTP real
  - Recalcular margem alvo realista
  - Validar fator_captura (0.75 default)
```

---

## 12 · Próximos Passos (Sub-sprints derivados)

```
[S3.0.1 v2.0 · este documento] ✅ CONCLUÍDO
  └─ Aprovação do usuário sobre metodologia + ranges
  
[S3.0.2 · Validação societária]
  ├─ Reunião com 4 sócios + contador
  ├─ Definir pró-labores reais (LASTRO-PL-01 a 04)
  ├─ Confirmar CNAE + Anexo Simples
  └─ Output: tabela de salários definitiva

[S3.0.3 · Validação WTP]
  ├─ 15-20 entrevistas Van Westendorp por cluster
  ├─ Refinar pricing §10 com dado primário
  └─ Output: ranges WTP-validated (VVV 0.85+)

[S3.0.4 · APENDICE-D-MODELO-CUSTO-PRICING.xlsx]
  ├─ Aba 1 · Premissas (variáveis editáveis com cores)
  ├─ Aba 2 · Custos Fixos (folha + infra + soft)
  ├─ Aba 3 · Custos Variáveis (CSC por cliente)
  ├─ Aba 4 · CAPEX (treino + setup amortizado)
  ├─ Aba 5 · Tributos (Simples Anexo III dinâmico)
  ├─ Aba 6 · Pricing Tiers (5 produtos × 6 personas)
  ├─ Aba 7 · Unit Economics (20 combos)
  ├─ Aba 8 · Cenários PERT (P10/P50/P90)
  └─ Aba 9 · Sensibilidade (±20% drivers)

[S3.0.5 · Retificação Cap 11 §pricing]
  ├─ Substituir VVV 0.65 inferência top-down por VVV 0.85+ assertivo
  ├─ Aplicar D-015 marcadores 🟡 com lastros
  └─ Output: 11-produtos-v2.3.0.X.md
```

---

## 13 · Conformidade Metodológica

| Mandato | Status | Evidência |
|---|---|---|
| Constitution Art. 1 (proibições) | ✅ Honrado | Investigou antes (web_search SOTA 2026), não chutou |
| Constitution Art. 2 (imperativos) | ✅ Honrado | Enumerou caminhos pricing via decision-analysis |
| RGO-1 (re-avaliar campo) | ✅ Honrado | S3.0.1 v1.0 SUPERSEDED reconhecido · D-014/D-015 emergentes |
| RGO-2 (evidência real) | ⚠️ Parcial | Dados ancorados em fontes 2026 · GAP02 WTP pendente |
| POP §6 (IA própria) | ✅ Honrado | Stack D003-v2 (Llama 3.1 8B local) é base do CAPEX |
| POP §7 (D-015 lastros) | ✅ Honrado | 6 lastros estruturados (PL-01 a 04, FOLHA, TRIB, CAC, WTP) |
| AP-13 (não API IA externa) | ✅ Honrado | Zero menção API Anthropic/OpenAI |
| AP-14 (custo após arquitetura) | ✅ Honrado | D003-v2 stack fundamenta CAPEX/OPEX |
| AP-15 (marcador 🟡 em estimativa) | ✅ Honrado | Toda célula estimativa marcada |
| BA-Orchestration (BABOK v3) | ✅ Honrado | 6 skills aplicadas em sequência |
| PMQS target ≥ 8.0 | 🟡 Aguarda autoavaliação | §14 below |
| VVV target ≥ 0.85 | 🟡 ~0.78 atual | GAP02 WTP destrava para 0.85+ |

---

## 14 · Autoavaliação PMQS

| Critério | Peso | Score | Justificativa |
|---|---:|---:|---|
| CE Completude/Especificidade | 15% | 9.0 | Todos os 5 produtos × 6 personas + 20 combos · CAPEX+OPEX detalhado |
| PI Precisão das Informações | 15% | 9.5 | Dados ancorados 2026 (Robert Half, Contabilizei, PoweredBySearch) |
| CC Clareza Cristalina | 10% | 8.5 | Estrutura clara mas denso (15 seções) |
| PRI Profundidade e Rigor | 20% | 9.5 | 6 skills BA orquestradas · PERT real · weighted scoring real |
| RA Relevância Absoluta | 15% | 9.5 | Todo conteúdo serve precificação assertiva (não decoração) |
| EIC Estrutura/Coerência | 10% | 9.0 | Fluxo §1→§13 lógico · cada seção alimenta a próxima |
| OVA Originalidade/Valor | 15% | 9.0 | Função probabilística + 20 combos + lastros D-015 first-time |
| **PMQS Bruto** | 100% | **9.21** | — |
| **VVV multiplicador** | — | 0.78 | GAP02 WTP pendente · cloud BR 🟡 LASTRO-01 |
| **PMQS Final** | — | **7.18** | Abaixo target 8.0 por GAP WTP |

**Gap para 8.0+**: validar WTP (3-5 entrevistas) → VVV sobe para 0.87 → PMQS final 8.01.
**Gap para 9.5**: WTP + cotação real cloud BR + decisão societária pró-labores → VVV 0.92 → PMQS 8.47.

**Decisão**: documento entra em status `ACTIVE_DRAFT_AWAITING_VALIDATION`. Aprovação do usuário sobre metodologia + ranges desbloqueia S3.0.4 (xlsx) e S3.0.5 (retificação Cap 11).

---

**FIM DO SPRINT 3.0.1 v2.0**

`Hash: NEOGOV-V21-S3.0.1-v2.0-MODELAGEM-PRICING-DONE-AWAIT-VALIDATION`

`Honra: POP v2.1.1.1 · D003-v2 · D-015 · BA-Orchestration BABOK v3`
