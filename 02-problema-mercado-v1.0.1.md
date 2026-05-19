---
id: NEOGOV-V21-CAP02-MERCADO
filename: 02-problema-mercado-v1.0.1.md
created_at: 2026-05-16T12:40:00Z
type: BUSINESS_PLAN_CHAPTER
chapter: 2
title: Problema & Mercado
version: v1.0.1
data_source: data/neogov-pricing-cost-ssot-v1.0.8.json
sprint: W1.4.3
edicao: 1
branch: retificacao-validacao-preco-novo
canonical_chain: [ssot-v1.0.8, 12-bmc, 14-gtm]
quality_target: PMQS 9.0 · VVV >= 0.78
tags: [problema, mercado, lgpd, ssot-v1.0.8]
mandatos_honrados: [RGO-9 honestidade, D-015 estimativa marcada, AP-14]
---

# Capítulo 2 · Problema & Mercado

> **Por que começar pelo problema, não pela solução?** Investidores compram a *dor*, não o produto. Um problema mal definido torna qualquer solução irrelevante. Este capítulo estabelece a tensão que justifica tudo o que vem depois.

---

## §2.1 · O problema central

A LGPD (Lei 13.709/2018) está em **fiscalização crescente** (ANPD ativa · sanções aplicadas). Ela obriga conformidade de dados a praticamente toda organização que trate dados pessoais — mas o **modelo dominante de atendimento é artesanal**: consultoria corpo-a-corpo, ciclos longos, preço alto (≈R$600k/12 meses · referência transcrição equipe).

```
Tensão estrutural:
  DEMANDA = obrigação legal vigente · massiva · não-opcional
  OFERTA  = consultoria sob medida · não-escalável · cara
  GAP     = organizações que precisam mas não podem pagar o modelo artesanal
```

## §2.2 · Por que o modelo atual não escala

| Modelo artesanal | Consequência |
|---|---|
| Diagnóstico manual por cliente | Custo linear (não há economia de escala) |
| Consultor sênior por engajamento | Gargalo humano · não replicável |
| Preço R$600k/12m | Exclui a base da pirâmide (municípios pequenos, escolas) |

> **Insight (Camila CTO · transcrição VVV=1.0)**: "corpo-a-corpo está ficando passado". O modelo que funcionou para grandes contas **não atende** os 5.570 municípios nem a cauda longa de hospitais/escolas/cartórios.

## §2.3 · O mercado (FATO + estimativa marcada)

| Segmento | Universo | Fonte |
|---|---|---|
| Municípios | 5.570 | IBGE (FATO) |
| Cartórios/serventias | 13.567 | CNJ Justiça Aberta (FATO · Cap 17) |
| Hospitais | dezenas de milhares | CNES (FATO · ordem de grandeza) |
| Escolas | base massiva | INEP 2024 (FATO) |
| Empresas (B2B geral) | milhões | universo amplo 🟡 D-015 |

> 🟡 D-015: dimensionamento financeiro de cada segmento (TAM/SAM/SOM) está no Cap 3. Aqui só o universo bruto FATO — não inflar.

## §2.4 · Por que agora (janela)

A janela existe pela **defasagem temporal**: a obrigação legal já vige e é fiscalizada, mas a capacidade de atendimento do mercado permanece artesanal. Quem industrializar primeiro captura a demanda reprimida. Prov. CNJ 213/2026 (cartórios) adiciona urgência regulatória nova.

---

## §2.5 · PMQS + Devil's Advocate

PMQS Bruto 9.30 × VVV 0.80 = **7.44** 🟡 honesto

> ⚔️ "R$600k/12m sem fonte primária forte" → referência da transcrição da equipe (VVV alto) · marcado como referência, não dado de mercado universal.
> ⚔️ "Universo B2B 'milhões' é vago" → declarado 🟡 D-015 · Cap 3 dimensiona com rigor.

## §2.6 · Backlinks

| Alimenta |
|---|
| Cap 3 (oportunidade dimensionada) · Cap 4 (solução) · Cap 14 (GTM) |

---

**FIM Cap 2 v1.0.1** · lê SSOT v1.0.8 · PMQS 7.44 honesto
