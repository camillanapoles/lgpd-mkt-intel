---
id: NEOGOV-V21-CAP13-VPC
filename: 13-vpc-v1.0.1.md
created_at: 2026-05-16T07:00:00Z
type: BUSINESS_PLAN_CHAPTER
chapter: 13
title: Value Proposition Canvas por Cluster
version: v1.0.1
data_source: data/neogov-pricing-cost-ssot-v1.0.2.json (price.validated)
parent_chapter: 12-bmc-v2.1.5.5
sprint: W1.2-RETIFICACAO-CONSOLIDACAO
edicao: 1
branch: retificacao-validacao-preco-novo
mandato_atendido: |
  USUARIO_2026-05-16: "prosseguir re-consolidacao Cap 12/13 sobre base validada"
canonical_chain:
  - APENDICE-K (DT TEST · POV por cluster)
  - APENDICE-L (base lógica FIEL)
  - 12-bmc-v2.1.5.5 (pricing validado)
  - 07-personas-latest (personas por cluster)
  - APENDICE-J (nomenclatura comercial)
metodologia:
  primaria: Value Proposition Canvas (Osterwalder · Strategyzer)
  secundaria: Jobs-To-Be-Done (Christensen)
  terciaria: alinhamento Customer Profile ↔ Value Map
quality_target: PMQS 9.5 · VVV >= 0.80
tags: [vpc, value-proposition, jobs-to-be-done, ssot-driven, por-cluster]
mandatos_honrados: [RGO-4 base estável, TEXT-AS-OBJECT, D-020 client-facing, VVV]
---

# Capítulo 13 · Value Proposition Canvas por Cluster
## v1.0.1 · Customer Profile ↔ Value Map · pricing `ssot.validated`

> Cada cluster tem um VPC: do lado direito o **Customer Profile** (Jobs, Pains, Gains), do lado esquerdo o **Value Map** (Products, Pain Relievers, Gain Creators). O "fit" só é válido quando o pricing validado (Apêndice K) é pagável pelo perfil — alinhamento já testado no DT TEST.

---

## §13.0 · Estrutura (TEXT-AS-OBJECT)

```
vpc[cluster] = {
  customer_profile: { jobs[], pains[], gains[] }
  value_map:        { products[], pain_relievers[], gain_creators[] }
  fit:              ssot.pricing_tiers[cluster] (price.validated · margem)
  fit_evidence:     APENDICE-K (DT TEST verdict)
}
```

---

## §13.1 · VPC · NeoGov Município (Família Alfa)

### 13.1.1 `vpc.alfa_m_pro` — Município Essencial

```
customer_profile (Secretário cidade <30k hab):
  jobs:   ["estar em compliance LGPD", "evitar multa ANPD", "responder pedidos cidadão",
           "não enfrentar licitação complexa de 6 meses"]
  pains:  ["orçamento TI R$200-800k limitado", "zero capacidade técnica interna",
           "medo de multa R$50k-50M", "pressão política crescente"]
  gains:  ["sono tranquilo anti-multa", "compliance turnkey", "sem dor de licitação"]

value_map:
  products:        [P1 Plataforma Core, P3-B2G básico]
  pain_relievers:  ["preço cabe em dispensa Art.75 IV (R$65.5k/ano teto)",
                    "turnkey · zero setup técnico do cliente",
                    "Wilton facilita canal político"]
  gain_creators:   ["RIPD automático", "atualização legal contínua", "soberania BR"]

fit: ssot.alfa_m_pro.price.validated = R$ 5.458/mês (= R$65.496/ano · cabe Art.75 IV)
     margem 79% · DT TEST verdict = PASS (c1✅ c2✅ c3✅ c4✅) · VVV 0.85
     → FIT FORTE: preço desenhado para o constraint legal do perfil
```

### 13.1.2 `vpc.alfa_m_plus_*` — Município Profissional

```
customer_profile (Gestor cidade 30-100k hab):
  jobs:   ["compliance robusto", "comparar 3 propostas no pregão", "melhor custo-benefício"]
  pains:  ["compra SEMPRE via licitação", "vendor lock-in possível", "budget R$800k-4M"]
  gains:  ["plataforma profissional", "diferencial técnico defensável em pregão"]

value_map:
  products:        [P1, P3-B2G completo, P5 leve (Dispensa)]
  pain_relievers:  ["Pregão: R$12.000 competitivo vs Voga",
                    "Dispensa: R$25.000 via cota Wilton Art.75",
                    "diferencial P3 LAI×LGPD único (D001-NOVO-12 POC valida)"]

fit: ssot.alfa_m_plus_pregao.validated = R$12.000 (56% margem · DT PASS condicional POC)
     ssot.alfa_m_plus_dispensa.validated = R$25.000 (62% margem · PASS canal Wilton)
     → FIT CONDICIONAL: depende POC P3 (D001-NOVO-12) + canal Wilton (risco JIANG declarado)
```

### 13.1.3 `vpc.alfa_m_enterprise` + `vpc.alfa_fe`

```
customer_profile (CIO cidade grande / Procurador federal):
  jobs:   ["plataforma enterprise SLA", "showcase soberania LGPD", "auditoria contínua"]
  pains:  ["OneTrust caro (R$50-200k)", "RFP 6-24 meses", "incumbent internacional"]
  gains:  ["soberania BR", "especialização jurídica nativa", "custo 24-75% menor"]

value_map:
  products:        [P1 Enterprise, P3-B2G, P3-B2C, P5 premium]
  pain_relievers:  ["50% mais barato que OneTrust BR", "Simone autoridade jurídica",
                    "IA própria BR (não API externa)", "ICT registrável"]

fit: alfa_m_enterprise R$38.000 (51% margem · PASS) · alfa_fe R$50.000 (38% · PASS ciclo longo)
     → FIT FORTE no valor · FIT FRACO no tempo (ciclo 12-24 meses · não Wave 1)
```

---

## §13.2 · VPC · NeoGov Saúde (Família Beta)

### 13.2.1 `vpc.beta_*` — Hospitais (3 portes)

```
customer_profile (CIO/CFO hospital · VARIA por porte):
  jobs:   ["proteger prontuário sensível", "integrar Tasy/MV ao compliance",
           "atender LAI estadual + auditoria"]
  pains:  ["multa ANPD prontuário R$50M", "budget TI varia 100x por porte",
           "integração sistema legada complexa"]
  gains:  ["ROI claro vs multa", "ETL turnkey Tasy/MV", "compliance contínuo"]

value_map:
  products:        [P1, P2 ETL, P3-B2G, P3-B2C, P4, P5] (SUPERSET · produto mais completo)
  pain_relievers:  ["estratificação 3 portes (não preço único surreal)",
                    "Pequeno R$12k · Médio R$28k · Grande R$65k",
                    "P2 ETL conecta Tasy/MV nativamente"]

fit: beta_pequeno R$12k (Y1 -31% INVESTIMENTO · Y2+ 15% · LTV/CAC 7.6x)
     beta_medio R$28k (Y1 breakeven · Y2+ 30%)
     beta_grande R$65k (Y1 19% · Y2+ 40%)
     → FIT SEGMENTADO: Y1 investimento estratégico declarado (Apêndice L elo fraco honesto)
     → DT TEST verdict = ADJUST (aceito · não PASS cego)
```

---

## §13.3 · VPC · NeoGov Educação (Família Gamma) ⭐ pós-DT-TEST

### 13.3.1 `vpc.gamma_pequena` — Escola Pequena (preço REDUZIDO)

```
customer_profile (Diretor escola 50-200 alunos):
  jobs:   ["compliance ECA Digital (vigência 17/03/2026)", "LGPD básico", "sem advogado caro"]
  pains:  ["sem orçamento LGPD dedicado", "fatura R$300k-1.5M apertada",
           "ECA Digital novo assusta", "sensível a preço"]
  gains:  ["compliance simples e barato", "ECA Digital coberto", "sem complexidade"]

value_map:
  products:        [P1 Basic] (NÃO usa AI-DPO · NÃO paga GPU · ABC peso=0)
  pain_relievers:  ["R$597/mês ≈ 1 mensalidade (psicologicamente digerível)",
                    "ECA Digital diferencial REAL (sem concorrente especializado)",
                    "self-service · zero fricção"]

fit: ssot.gamma_pequena.price.validated = R$ 597 ⬇️ (era R$800 · DT TEST reduziu)
     margem 69% (CSC só R$187 · ABC revelou) · DT verdict = PASS_FORTE
     → FIT FORTE: preço reduzido captura adoção · ECA Digital janela monopólio
     → land grab estratégico: capturar antes de concorrente acordar (trade-off declarado)
```

### 13.3.2 `vpc.gamma_media` + `vpc.gamma_enterprise`

```
gamma_media: R$1.797 ⬇️ (era R$2.500 · psicológico <R$2k · margem 80% · PASS_FORTE)
gamma_enterprise: R$5.000 (MANTIDO · escola grande não price-sensitive · RGO-3)

customer_profile: escolas maiores · fatura R$1.5-50M · budget folgado
value_map: P1+P4 (média) · P1+P3-B2G+P4 (grande) · ECA+IA diferencial
fit: ambos PASS · média volume play · grande mantém margem
```

---

## §13.4 · VPC · NeoGov Profissional (Família Épsilon) ⭐ pós-DT-TEST

### 13.4.1 `vpc.epsilon_dpo` — DPO Individual (preço REDUZIDO)

```
customer_profile (Advogado/DPO autônomo):
  jobs:   ["responder dúvidas LGPD rápido", "manter-se atualizado", "escalar atendimento"]
  pains:  ["hora vale R$300-800 (tempo é gargalo)", "atualização legal contínua",
           "compete iComp R$1.200 / LGPD Cloud R$199"]
  gains:  ["produtividade 5h+/mês poupadas", "IA jurídica confiável", "preço acessível"]

value_map:
  products:        [P4 AI-DPO Copilot]
  pain_relievers:  ["R$997 < R$1.000 psicológico · -17% vs iComp",
                    "IA própria treinada jurídico BR",
                    "atualização legal automática"]

fit: ssot.epsilon_dpo.price.validated = R$ 997 ⬇️ (era R$1.500 · DT reduziu)
     margem 77% (CSC só R$226) · DT verdict = PASS_FORTE
     → FIT FORTE: vence iComp em preço E features · land grab mercado DPO fragmentado
```

### 13.4.2 `vpc.epsilon_escritorio`

```
R$797/seat ⬇️ (era R$1.200 · -34% volume agressivo · margem 79% · PASS_FORTE)
customer_profile: escritório boutique 3+ DPOs · compra volume
value_map: P4 multi-seat + P3-B2C light · volume discount
fit: PASS_FORTE · captura escritórios via preço agressivo
```

---

## §13.5 · Matriz de Fit Consolidada

| `vpc[cluster]` | Fit Customer↔Value | Pricing validado | DT verdict | Risco declarado |
|---|:--:|---:|:--:|---|
| alfa_m_pro | 🟢 FORTE | R$ 5.458 | PASS | — |
| alfa_m_plus_pregao | 🟡 CONDICIONAL | R$ 12.000 | PASS cond. | POC P3 (D001-NOVO-12) |
| alfa_m_plus_dispensa | 🟡 CONDICIONAL | R$ 25.000 | PASS | canal Wilton (JIANG) |
| alfa_m_enterprise | 🟢 FORTE | R$ 38.000 | PASS | ciclo longo |
| alfa_fe | 🟢 FORTE valor | R$ 50.000 | PASS | ciclo 12-24m |
| beta_* (3 portes) | 🟡 SEGMENTADO | R$12-65k | ADJUST | Y1 investimento |
| gamma_pequena | 🟢 FORTE | R$ 597 ⬇️ | PASS_FORTE | volume não-materializar |
| gamma_media | 🟢 FORTE | R$ 1.797 ⬇️ | PASS_FORTE | — |
| gamma_enterprise | 🟢 FORTE | R$ 5.000 | PASS | — |
| epsilon_dpo | 🟢 FORTE | R$ 997 ⬇️ | PASS_FORTE | — |
| epsilon_escritorio | 🟢 FORTE | R$ 797/seat | PASS_FORTE | — |

---

## §13.6 · Síntese

```
9 de 11 clusters: FIT FORTE (pricing validado pagável pelo perfil · DT TEST PASS)
2 clusters: FIT CONDICIONAL declarado (Alfa-M Plus · POC+canal · risco honesto)
1 família: FIT SEGMENTADO (Beta · Y1 investimento · LTV/CAC compensa)

A redução de preço Gamma/Épsilon (DT TEST) FORTALECEU o fit:
  preço agora alinhado ao Customer Profile (sensível a preço · self-service)
  → não foi perda de margem · foi otimização de fit (margem ainda 69-80%)
```

---

## §13.7 · Backlinks

| Consome | Como |
|---|---|
| Cap 14 GTM | VPC → mensagem de venda por cluster |
| Cap 15 Financeiro | fit → conversão esperada por cluster |
| Cap 17 Riscos | fits condicionais = riscos mapeados |

---

**FIM Cap 13 v1.0.1** · PMQS estimado 8.3 · VVV 0.80 · base FIEL (Apêndice L) · pricing `ssot.validated`
