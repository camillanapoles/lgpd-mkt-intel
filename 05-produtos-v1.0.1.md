---
id: NEOGOV-V21-CAP05-PRODUTOS
filename: 05-produtos-v1.0.1.md
created_at: 2026-05-16T13:00:00Z
type: BUSINESS_PLAN_CHAPTER
chapter: 5
title: Portfólio de Produtos (P1-P5)
version: v1.0.1
data_source: data/neogov-pricing-cost-ssot-v1.0.8.json
sprint: W1.4.3
edicao: 1
branch: retificacao-validacao-preco-novo
canonical_chain: [ssot-v1.0.8, 04-solucao, 12-bmc]
quality_target: PMQS 9.0 · VVV >= 0.76
tags: [produtos, p1-p5, gargalos, ssot-v1.0.8]
mandatos_honrados: [RGO-9, D-015, AP-14]
---

# Capítulo 5 · Portfólio de Produtos

> **Por que os produtos derivam de gargalos, não de ideias?** Um portfólio inventado por intuição erra o mercado. Os 5 produtos NeoGov são a resposta 1:1 aos 4 gargalos universais (Cap 4) — engenharia reversa da demanda, não palpite de roadmap.

---

## §5.1 · Mapa produto → gargalo

| Produto | Resolve gargalo | Função |
|---|---|---|
| **P1 · Data Discovery** | Onde estão os dados? | Mapeamento automatizado de dados pessoais |
| **P2 · Anonimização** | LAI × LGPD | Anonimização que concilia transparência e privacidade |
| **P3 · LAI×LGPD (B2G/B2C)** | Tensão certidão × privacidade | Resolve o conflito estrutural setor público/cartório |
| **P4 · AI-DPO** | Encarregado terceirizado | DPO-as-a-service com IA (obrigação legal) |
| **P5 · ETL/Integração** | Dados dispersos legados | Pipeline de integração de sistemas |

> **Por que 5 e não 1 plataforma única?** Cada gargalo tem ciclo de venda e dor distintos. Modularizar permite que um cliente entre por um produto (ex: P4 AI-DPO, dor urgente) e expanda. Plataforma monolítica forçaria adoção total — fricção que mata conversão.

## §5.2 · Composição por segmento (do SSOT v1.0.8)

| Segmento | Produtos típicos |
|---|---|
| B2G Município | P1 + P3-B2G + P4 |
| B2B Saúde | P1 + P4 + P5 (dados clínicos massivos) |
| B2B Educação | P1 + P4 (dados de menores) |
| B2B DPO | P4 (núcleo) |
| B2B Cartório | P1 + P3-B2G + P4 (+ P5 nas classes altas) |

> Os pacotes não são arbitrários — derivam do VPC (Cap 13 · dor por segmento). Cartório III-C custom pode levar os 5 (Cap 15 §15.4).

## §5.3 · Por que isto sustenta a escala industrial

Os 5 produtos compartilham a *mesma espinha técnica* (IA própria · Cap 6) com parametrização por segmento. Adicionar um segmento = configurar, não reconstruir. É o que torna a margem industrial possível (Cap 15).

---

## §5.4 · PMQS + Devil's Advocate

PMQS Bruto 9.30 × VVV 0.78 = **7.25** 🟡 honesto

> ⚔️ "5 produtos = foco diluído p/ startup early-stage" → Procede como risco. Mitigação: roadmap de waves (Cap 14) entra produto a produto, não todos de uma vez. P1+P4 são o núcleo Wave 1.
> ⚔️ "P3 LAI×LGPD ainda é PoC" → Verdade · D001-NOVO-12 (POC P3) aberto · não vendido como pronto.

## §5.5 · Backlinks

| Consome / Alimenta |
|---|
| Cap 4 (gargalos) → Cap 5 → Cap 6 (tech) · Cap 12/13 (BMC/VPC) |

---

**FIM Cap 5 v1.0.1** · lê SSOT v1.0.8 · PMQS 7.25 honesto
