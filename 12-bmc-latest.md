---
id: NEOGOV-V21-CAP12-BMC
filename: 12-bmc-v2.1.5.6.md
created_at: 2026-05-16T09:10:00Z
type: BUSINESS_PLAN_CHAPTER
chapter: 12
title: Business Model Canvas + Pricing Validado + 5 Segmentos
version: v2.1.5.6
supersedes: 12-bmc-v2.1.5.5.md (lia SSOT v1.0.2 · pré-cartórios · pré-correção N)
data_source: data/neogov-pricing-cost-ssot-v1.0.8.json (latest · validado · header alinhado ao corpo patcheado W1.4.1)
sprint: W1.3-PROPAGACAO-SSOT
edicao: 1
branch: retificacao-validacao-preco-novo
mandato_atendido: |
  USUARIO_2026-05-16: "PROSSIGA P2 · propagar SSOT v1.0.7 aos Caps · WAL contínuo"
canonical_chain:
  - data/neogov-pricing-cost-ssot-v1.0.7.json (fonte única · 19 tiers · 5 segmentos)
  - APENDICE-K (DT TEST · price.validated Gamma/Épsilon/Alfa/Beta)
  - APENDICE-N (cartórios FATO-corrigido · sigilo arrecadação declarado)
  - APENDICE-L (base lógica FIEL)
  - data/curva-ponto-sucesso-global.png
quality_target: PMQS 9.5 · VVV >= 0.80 · base estável RGO-4
tags: [bmc, pricing-validado, 5-segmentos, ssot-v1.0.7, cartorios-fato]
mandatos_honrados: [RGO-4 base estável, RGO-9 honestidade, TEXT-AS-OBJECT, AP-14 edição antecipada, AP-04 nomenclatura]
---

# Capítulo 12 · Business Model Canvas + Pricing Validado
## v2.1.5.6 · Lê `ssot v1.0.7` · 19 tiers · 5 segmentos de negócio

> **Mudança vs v2.1.5.5**: agora lê SSOT v1.0.7 (não v1.0.2). Inclui (a) cartórios FATO-corrigidos pós auditoria hostil (Apêndice N), (b) agrupamento em 5 business_segments, (c) declaração honesta do bloqueio de sigilo da arrecadação cartório (D001-NOVO-16).

---

## §12.0 · Proveniência (resposta epistemológica · Apêndice L)

```
pricing_chain = {
  custo:      FATO     → web_search Magalu R$6.310/GPU (re-validado 2x)
  rateio:     MÉTODO   → ABC Kaplan&Cooper (proporcional)
  validação:  LÓGICA   → DT TEST 5ª fase IDEO (Apêndice K)
  cartórios:  FATO+honestidade → faixa-classe CNJ Prov.74/2018 (arrecad. SIGILOSA · Apêndice N)
  fidelidade: Apêndice L → FIEL · elos fracos declarados
}
```

---

## §12.1-12.6 · Blocos BMC (mantidos de v2.1.5.2 · RGO-3)

Segmentos, Proposta de Valor, Canais, Relacionamento, Recursos, Atividades, Parcerias permanecem conforme `12-bmc-v2.1.5.2.md §12.1-12.6` (não afetados · não reescrever o que funciona · AP-06).

---

## §12.7 · ESTRUTURA DE RECEITA · 5 Segmentos · `ssot.business_segments`

### 12.7.1 B2G · Setor Público (`ssot.business_segments.b2g_setor_publico`)

| Nome comercial | Preço validado | Cobrança | Margem |
|---|---:|---|:--:|
| NeoGov Município · Essencial | R$ 5.458/mês | Assinatura | 79% |
| NeoGov Município · Profissional (Licitação) | R$ 12.000/mês | Assinatura | 56% |
| NeoGov Município · Profissional (Dispensa) | R$ 25.000/mês | Assinatura | 62% |
| NeoGov Município · Avançado | R$ 38.000/mês | Premium + uso | 51% |
| NeoGov Estadual & Federal | R$ 50.000/mês + R$25k setup | Premium + retainer | 38% |

### 12.7.2 B2B · Saúde (`ssot.business_segments.b2b_saude`)

| Nome comercial | Preço validado | Cobrança | Margem |
|---|---:|---|:--:|
| NeoGov Saúde · Hospital Pequeno (Ano 1) | R$ 12.000/mês + R$25k setup | Setup + manutenção | -31% ⚠️ invest. |
| NeoGov Saúde · Hospital Pequeno (Recorrente) | R$ 12.000/mês | Assinatura | 15% |
| NeoGov Saúde · Hospital Médio (Ano 1) | R$ 28.000/mês + R$50k setup | Setup + manutenção | -1% ⚠️ |
| NeoGov Saúde · Hospital Médio (Recorrente) | R$ 28.000/mês | Assinatura | 30% |
| NeoGov Saúde · Hospital Grande (Ano 1) | R$ 65.000/mês + R$100k setup | Setup + manutenção | 19% |
| NeoGov Saúde · Hospital Grande (Recorrente) | R$ 65.000/mês | Assinatura | 40% |

### 12.7.3 B2B · Educação (`ssot.business_segments.b2b_educacao`)

| Nome comercial | Preço validado | Cobrança | Margem |
|---|---:|---|:--:|
| NeoGov Educação · Escola Pequena | R$ 597/mês ⬇️ | Assinatura | 69% |
| NeoGov Educação · Escola Média | R$ 1.797/mês ⬇️ | Assinatura | 80% |
| NeoGov Educação · Rede & Escola Grande | R$ 5.000/mês | Assinatura | 76% |

### 12.7.4 B2B · Profissional / DPO (`ssot.business_segments.b2b_profissional`)

| Nome comercial | Preço validado | Cobrança | Margem |
|---|---:|---|:--:|
| NeoGov Profissional · DPO Individual | R$ 997/licença/mês ⬇️ | Por seat | 77% |
| NeoGov Profissional · Escritório DPO | R$ 797/licença/mês ⬇️ | Por seat (volume) | 79% |

### 12.7.5 B2B · Notarial / Cartórios (`ssot.business_segments.b2b_notarial`) ⭐ NOVO

| Nome comercial | Preço validado | Cobrança | Margem | VVV |
|---|---:|---|:--:|:--:|
| NeoGov Cartórios · Classe I | R$ 597/mês | Assinatura | 57% | 0.55 🟡 |
| NeoGov Cartórios · Classe II | R$ 2.900/mês | Premium | 38% | 0.55 🟡 |
| NeoGov Cartórios · Classe III | R$ 9.000/mês (provisório) | Premium | s/ margem fixa | 0.45 🟡 |

> **Honestidade (RGO-9 · `ssot._audit_flag`)**: preço cartório ancorado em **faixa-classe CNJ Prov.74/2018** (Classe I ≤R$100k/sem · II ≤R$500k/sem · III >R$500k/sem — FATO). A arrecadação **individual por serventia é SIGILOSA** (CNJ oficial · D001-NOVO-16) — não há FATO público mais granular. Classe III precisa **sub-estratificação** (D001-NOVO-17 · range R$1M-143M absurdo p/ tier único). 13.567 serventias (FATO CNJ).

---

## §12.11 · ESTRUTURA DE CUSTO (3 camadas DDD + ABC · Apêndice H/I)

```
ssot.cost_model = {
  layer_1a_platform (shared · rateável ABC):  R$ 10.988/mês  → FATO Magalu
  layer_1b_dev (NÃO ratea):                   R$  4.574/mês  → CF
  fixed_costs_company.total:                  R$ 142.251/mês
}
rateio ABC: escola Gamma Pequena peso GPU=0 (não paga IA)
```

---

## §12.12 · PONTO DE SUCESSO (curva · `data/curva-ponto-sucesso-global.png`)

| N clientes | Lucro/mês | Status | ARR |
|---:|---:|:--:|---:|
| 31 (Wave1 P75) | -R$ 21k | 🔴 burn aceitável | R$ 2.3M |
| **37** | **R$ 0** | **⚖️ break-even global** | — |
| **163** | — | **🎯 sucesso global (margem 49%)** | R$ 12.1M |
| 600 (Wave5) | +R$ 2.2M | ✅ industrial | R$ 44.4M |

> **Atualizado**: curva recalculada com cartório FATO — ver `data/curva-ponto-sucesso-global-v2.png` (lê SSOT v1.0.8). Wave 1 break-even=37 inalterado (cartório é Wave 3-5); uplift cartório Wave 3-5 = +R$312k/mês (cenário separado · 🟡 2% TAM).

---

## §12.13 · Síntese

```
Modelo viável: N≥37 break-even · N≥163 sucesso global
5 segmentos · 19 tiers · pricing validado DT TEST sobre base FIEL (Apêndice L)
Cartórios = 5º segmento (B2B-Notarial · 13.567 serventias · FATO faixa-classe)
4 reduções estratégicas (Gamma/Épsilon volume play) · 12 mantidos · 3 cartórios novos
```

## §12.14 · Backlinks

| Consome | Como |
|---|---|
| Cap 13 VPC v1.0.2 | Value Proposition por cluster + 5 segmentos |
| Cap 15 Financeiro | DRE/FCD usa `ssot v1.0.7` + curva |

---

**FIM Cap 12 v2.1.5.6** · lê SSOT v1.0.7 · PMQS estimado 8.4 · VVV 0.80 · RGO-4 ✅
