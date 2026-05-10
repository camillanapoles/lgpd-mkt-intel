---
type: shuntzu-cnm-cards
version: 1.0.0
last_updated: 2026-05-09T22:35:00-03:00
reference_rule: ~/.claude/rules/shuntzu-continuity.md
governance: presentation-vue/GOVERNANCE.md (R2 — Cartas na Mesa)
data_source: presentation-vue/public/strategic-data-unified.json
data_path: snti.dimensions.<dim>.items[]
---

# Cartas na Mesa (CNM)

Lightweight pointer index of 38 SNTI cards. Full schema (description, vvv_source, fator, polaridade, criterios_dinamicos, certeza_agregada, shelf_life, proxima_revisao, sqia_trace, vvv_decay) lives in JSON — do NOT duplicate here. This file tracks WHICH cards exist, their current VVV snapshot, and dimension binding.

Per GOVERNANCE.md R2, each carta has:
`id + description + dimensao + vvv + vvv_source + vvv_updated + fator + polaridade + criterios_dinamicos + certeza_agregada + shelf_life + proxima_revisao`

## Card Inventory (38 total)

| # | id | dimensao | vvv | description (short) |
|---|------|----------|-----|---------------------|
| 1 | team_alignment | dao | 0.85 | Alinhamento medio da equipe |
| 2 | raci_coverage | dao | 0.90 | 4 atividades com RACI definido |
| 3 | prefeitura_alignment_low | dao | 0.80 | Prefeituras alinhamento 0.3 |
| 4 | consorcio_early_validation | dao | 0.70 | Consorcios sem validacao precoce |
| 5 | advisor_missing | dao | 0.30 | Co-founder/Advisor nao confirmado |
| 6 | tce_not_mapped | dao | 0.85 | TCEs mapeados — 7 TCEs + TCU |
| 7 | anpd_enforcement | ceu | 0.95 | ANPD agencia independente ativa |
| 8 | eca_digital_urgent | ceu | 0.98 | ECA Digital Marco 2026 |
| 9 | lei_14133_dispensa | ceu | 0.98 | Dispensa licitacao ate R$50K |
| 10 | window_2026_2027 | ceu | 0.85 | Janela oportunidade 2026-2027 |
| 11 | election_2028_risk | ceu | 0.78 | Eleicoes 2028 desaceleracao |
| 12 | anpd_agenda_2025_26 | ceu | 0.89 | Agenda regulatoria AI+gov+child |
| 13 | cloud_market_growth | ceu | 0.94 | Cloud BR $18.1B → $86.6B |
| 14 | ict_qualification | terra | 0.95 | Prerrogativas ICT Art.75 IV |
| 15 | dc_brasil_100pct | terra | 0.95 | DC Brasil Art.26 |
| 16 | pricing_below_dispensa | terra | 0.90 | Unico abaixo R$65K/ano com DPO |
| 17 | confidata_threat | terra | 0.70 | Confidata pivot municipal |
| 18 | onetrust_potential | terra | 0.50 | OneTrust entrada BR 12-24m |
| 19 | buyer_power_high | terra | 0.84 | Poder compradores moderado-alto |
| 20 | rivalry_high | terra | 0.82 | Rivalidade competitiva mod-alta |
| 21 | tam_4011_municipios | terra | 0.95 | 4.011 municipios sem LGPD |
| 22 | aws_dependency | terra | 0.70 | Dependencia AWS sa-east-1 |
| 23 | no_brand | terra | 0.70 | Brand awareness baixo |
| 24 | wilton_articulacao | comandante | 0.90 | Wilton — articulacao consorcios/TCEs |
| 25 | gislene_juridica | comandante | 0.85 | Gislene — parecer dispensa + INPI |
| 26 | camilla_tech | comandante | 0.80 | Camilla — MVP + infraestrutura |
| 27 | simone_compliance | comandante | 0.90 | Simone — base juridica AI-DPO |
| 28 | dpo_pool_gap | comandante | 0.80 | Pool DPOs — plano validado |
| 29 | no_iso | comandante | 0.70 | Sem ISO 27001 |
| 30 | advisor_vvv03 | comandante | 0.30 | Advisor VVV=0.3 (DUP de dao:advisor_missing) |
| 31 | roadmap_6_fases | metodo | 0.85 | Roadmap 6 fases definido |
| 32 | sprints_planned | metodo | 0.80 | 4 sprints planejados |
| 33 | critical_path_defined | metodo | 0.80 | Caminho critico INPI→Alpha→PoC |
| 34 | lois_zero | metodo | 0.00 | LOIs assinadas — BLOQUEIO |
| 35 | custo_dev_unknown | metodo | 0.40 | Custo desenvolvimento desconhecido |
| 36 | conversao_zero | metodo | 0.00 | Taxa conversao desconhecida |
| 37 | financial_confidence_low | metodo | 0.65 | Confidence financeiro 0.65 |
| 38 | model_contabilizei_validated | metodo | 0.80 | Modelo Contabilizei validado |

## Dimension Roll-up

| Dim | Count | Avg VVV | Lowest | Highest |
|-----|-------|---------|--------|---------|
| dao | 6 | 0.73 | 0.30 (advisor_missing) | 0.90 (raci_coverage) |
| ceu | 7 | 0.91 | 0.78 (election_2028_risk) | 0.98 (eca_digital_urgent, lei_14133_dispensa) |
| terra | 10 | 0.80 | 0.50 (onetrust_potential) | 0.95 (ict_qualification, dc_brasil_100pct, tam_4011_municipios) |
| comandante | 7 | 0.75 | 0.30 (advisor_vvv03) | 0.90 (wilton_articulacao, simone_compliance) |
| metodo | 8 | 0.54 | 0.00 (lois_zero, conversao_zero) | 0.85 (roadmap_6_fases) |

## Decay State (R1)

- Decay formula: `vvv_decay = vvv × 1/(1 + 0.30 × meses_since_vvv_updated)`
- All cards `vvv_updated = 2026-05-09` → decay factor = 1.0 currently
- First decay tick at 2026-06-09 (1 month) → factor = 0.769
- Stale flag at 6 months (2026-11-09) → factor = 0.357 (revalidate)

## Critical Cards (Immediate Attention)

- **lois_zero** (vvv=0.00) — execution gap, blocks scoring credibility
- **conversao_zero** (vvv=0.00) — no real conversion data
- **advisor_missing / advisor_vvv03** (vvv=0.30) — duplicate; consider merge per GOVERNANCE
- **custo_dev_unknown** (vvv=0.40) — unknown CAPEX

## Lookup

For full carta details: read `presentation-vue/public/strategic-data-unified.json`, navigate to `snti.dimensions.<dim>.items[]` and find by `id`.
