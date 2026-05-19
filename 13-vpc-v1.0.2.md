---
id: NEOGOV-V21-CAP13-VPC
filename: 13-vpc-v1.0.2.md
created_at: 2026-05-16T09:15:00Z
type: BUSINESS_PLAN_CHAPTER
chapter: 13
title: Value Proposition Canvas por Cluster + Cartórios
version: v1.0.2
supersedes: 13-vpc-v1.0.1.md (lia SSOT v1.0.2 · sem cartórios)
data_source: data/neogov-pricing-cost-ssot-v1.0.7.json
parent_chapter: 12-bmc-v2.1.5.6
sprint: W1.3-PROPAGACAO-SSOT
edicao: 1
branch: retificacao-validacao-preco-novo
mandato_atendido: USUARIO_2026-05-16 "PROSSIGA P2 · WAL contínuo"
canonical_chain: [ssot-v1.0.7, APENDICE-K, APENDICE-N, 12-bmc-v2.1.5.6]
metodologia: Value Proposition Canvas (Osterwalder) + JTBD (Christensen)
quality_target: PMQS 9.5 · VVV >= 0.78
tags: [vpc, value-proposition, 5-segmentos, cartorios, ssot-v1.0.7]
mandatos_honrados: [RGO-4, RGO-9, TEXT-AS-OBJECT, AP-14, AP-06]
---

# Capítulo 13 · Value Proposition Canvas + Cartórios
## v1.0.2 · 5 segmentos · pricing `ssot v1.0.7`

> **Mudança vs v1.0.1**: add VPC do 5º segmento (B2B-Notarial · Cartórios) · lê SSOT v1.0.7.

---

## §13.0 · Estrutura (TEXT-AS-OBJECT)

```
vpc[cluster] = { customer_profile{jobs,pains,gains}, value_map{products,relievers,creators},
                 fit: ssot.pricing_tiers[*].price.validated, evidence: APENDICE-K/N }
```

---

## §13.1-13.4 · VPC Alfa/Beta/Gamma/Épsilon (mantidos de v1.0.1 · RGO-3/AP-06)

Conteúdo conforme `13-vpc-v1.0.1.md §13.1-13.4` (4 famílias · não reescrever aprovado). Fit atualizado para `ssot v1.0.7` (preços idênticos · Apêndice K inalterado para esses 16 tiers).

```
Resumo fit (inalterado): 9 FIT FORTE · 2 condicional (Alfa-M Plus) · 1 segmentado (Beta)
```

---

## §13.5 · VPC · NeoGov Cartórios (B2B-Notarial) ⭐ NOVO

### 13.5.1 `vpc.cartorio_classe1` — Serventia Classe I

```
customer_profile (titular cartório pequeno · ≤R$100k/semestre arrecadação · FATO):
  jobs:  ["cumprir CNJ Prov.134/2022 + Prov.213/2026", "terceirizar DPO (sem equipe)",
          "evitar sanção Corregedoria", "cibersegurança mínima viável"]
  pains: ["assimetria estrutural (Min.Campbell reconhece)", "sem orçamento TI",
          "Prov.213 fev/2026 novo", "arrecadação baixa"]
  gains: ["compliance turnkey barato", "DPO terceirizado IA", "transição proporcional CNJ"]

value_map:
  products:        [P1 Basic, P4 AI-DPO]
  pain_relievers:  ["R$597/mês ancorado em 3,6% da faixa-classe FATO (≤R$200k/ano)",
                    "P4 cobre terceirização DPO (Prov.134 art.6 permite)",
                    "sem concorrente notarial-especializado + IA"]

fit: ssot.cartorio_classe1.price.validated = R$ 597/mês · margem 57% · VVV 0.55
     🟡 D-015: preço = faixa-classe FATO · posição na faixa = estimativa (D001-NOVO-7 piloto)
     → FIT CONDICIONAL HONESTO (base FATO · WTP a calibrar)
```

### 13.5.2 `vpc.cartorio_classe2` — Serventia Classe II

```
customer_profile (cartório médio · ≤R$500k/semestre · 4-10 func):
  jobs:  ["LGPD + LAI×LGPD certidões inteiro teor", "gap assessment Prov.134",
          "trilhas auditoria Prov.213"]
  pains: ["certidão inteiro teor × LGPD tensão real", "compartilhamento SIRC"]
  gains: ["P3-B2G resolve LAI×LGPD", "compliance + cibersec integrado"]

value_map: [P1, P3-B2G, P4, P5-leve] · R$2.900/mês (3,5% faixa-classe FATO)
fit: ssot.cartorio_classe2.validated R$2.900 · margem 38% · VVV 0.55 · FIT CONDICIONAL
```

### 13.5.3 `vpc.cartorio_classe3_*` — Serventia Classe III (sub-estratificada)

> **Atualizado v1.0.8**: o tier único provisório foi substituído por 3 sub-tiers (resolve D17 · Cap 15 §15.4). Razão: arrecadação R$1M-143M é heterogênea demais para um preço só.

```
customer_profile (cartório grande · >R$500k/semestre · sub-estratificado):
  jobs:  ["rigor máximo Prov.213", "dados sensíveis massivos", "continuidade negócios"]
  pains: ["volume dados massivo", "exposição reputacional", "auditoria CNJ rigorosa"]

value_map: [P1, P3-B2G, P3-B2C, P4, P5] · 3 sub-tiers (ssot.business_segments.b2b_notarial):
  III-A R$5.000  (arrecad. R$1-3M/ano  · ~55%)
  III-B R$15.000 (arrecad. R$3-10M/ano · ~35%)
  III-C R$30.000+ custom (arrecad. >R$10M · ~10% · cauda até R$143M)
fit: ⚠️ FIT INDEFINIDO · range arrecadação absurdo p/ tier único
     → D001-NOVO-17 sub-estratificar III-A/B/C OBRIGATÓRIO antes de fit definitivo
     VVV 0.45 (o mais baixo · honestamente declarado · não fabricar fit)
```

---

## §13.6 · Matriz de Fit Consolidada (5 segmentos · 19 tiers)

| Segmento | Tiers | Fit dominante | Risco declarado |
|---|:--:|:--:|---|
| B2G Setor Público | 5 | 🟢 FORTE (3) · 🟡 cond. (2) | POC P3 · canal Wilton |
| B2B Saúde | 6 | 🟡 SEGMENTADO | Y1 investimento |
| B2B Educação | 3 | 🟢 FORTE | volume materializar |
| B2B Profissional | 2 | 🟢 FORTE | — |
| **B2B Notarial** | 3 | 🟡 **CONDICIONAL HONESTO** | WTP + sub-estratificar III |

```
9 FIT FORTE · 4 condicional · 1 segmentado · 3 cartório condicional-honesto
Cartórios: base FATO (faixa-classe) mas WTP/sub-estratificação a calibrar (não fabricar)
```

---

## §13.7 · Backlinks

| Consome | Como |
|---|---|
| Cap 14 GTM | VPC → mensagem venda por segmento |
| Cap 15 Financeiro | fit → conversão esperada |
| Cap 17 Riscos | fits condicionais + cartório sigilo = riscos |

---

**FIM Cap 13 v1.0.2** · 5 segmentos · lê SSOT v1.0.7 · PMQS estimado 8.3 · VVV 0.78 · RGO-4 ✅
