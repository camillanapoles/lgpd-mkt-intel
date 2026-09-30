---
id: NEOGOV-V21-APENDICE-A-VVV-LOG
filename: APENDICE-A-VVV-LOG.md
created_at: 2026-05-14
last_updated: 2026-05-14T23:50:00Z
type: VVV_INCREMENTAL_LOG
status: ACTIVE
parent_doc: BUSINESS-PLAN-FINAL-v2.1
purpose: Rastreabilidade auditável de TODA afirmação factual do BP NeoGov v2.1
update_rule: Cresce monotonicamente · 1 entrada por afirmação verificável
final_destination: Apêndice A do BP final (Word docx)
tags: [vvv, validacao, auditoria, rastreabilidade]
---

# Apêndice A · Log de Validação VVV

> Este documento rastreia toda afirmação factual, inferência e especulação presentes no Business Plan NeoGov v2.1. Cresce a cada sprint de produção e é incorporado como Apêndice A do BP final.

## Classificação

| Tag | Significado | VVV ref |
|---|---|---|
| `[FATO]` | Dado empírico verificável em fonte primária | 0.90-1.00 |
| `[INFERÊNCIA]` | Lógica válida a partir de fatos | 0.70-0.89 |
| `[ESPECULAÇÃO]` | Indução com confiança < 90% | 0.50-0.69 |
| `[CRENÇA]` | Não-fundamentado · requer flag UNVERIFIED | < 0.50 |

## Métricas globais

- VVV global atual: **0.92** (Sprint 1.1 fechado)
- Afirmações totais: **12**
- FACT: 7 · INFERÊNCIA: 5 · ESPECULAÇÃO: 0 · CRENÇA: 0
- Última atualização: 2026-05-14 Sprint 1.1

---

## Sprint 1.1 — Capítulo 04 Design Thinking

### AF-001

| Campo | Valor |
|---|---|
| Afirmação | NeoGov tem knowledge jurídico LGPD + capacidade ICT IA combinados |
| Classificação | FACT |
| Fonte primária | transcricao-reuniao-neogov.txt (06/05/2026) |
| VVV | 1.00 |
| Seção | cap_04 §4.1 |
| Status | VÁLIDO |

### AF-002

| Campo | Valor |
|---|---|
| Afirmação | Nenhum concorrente combina knowledge jurídico LGPD profundo + capacidade ICT no mesmo nível |
| Classificação | INFERENCE |
| Fonte primária | BP v2.0 §3.3 análise competitiva |
| Fonte secundária | VVV-GAP-RESEARCH (Confidata, OneTrust, TrustArc) |
| VVV | 0.85 |
| Seção | cap_04 §4.1 |
| Status | VÁLIDO |

### AF-003

| Campo | Valor |
|---|---|
| Afirmação | 76,7% órgãos federais em grau inexpressivo/inicial de adequação LGPD |
| Classificação | FACT |
| Fonte primária | TCU Acórdão 1.384/2022 + auditoria 2024 |
| VVV | 0.95 |
| Seção | cap_04 §4.3 |
| Status | VÁLIDO |

### AF-004

| Campo | Valor |
|---|---|
| Afirmação | Art. 52 §3° LGPD isenta setor público de multa pecuniária |
| Classificação | FACT |
| Fonte primária | Lei 13.709/2018 Art. 52 §3° |
| VVV | 1.00 |
| Seção | cap_04 §4.4 |
| Status | VÁLIDO |

### AF-005

| Campo | Valor |
|---|---|
| Afirmação | ANPD prioriza poder público no Mapa 2026-2027 |
| Classificação | FACT |
| Fonte primária | gov.br/anpd dez/2025 |
| VVV | 0.95 |
| Seção | cap_04 §4.4 |
| Status | VÁLIDO |

### AF-006

| Campo | Valor |
|---|---|
| Afirmação | ECA Digital (Lei 15.211/2025) vigente desde março/2026 |
| Classificação | FACT |
| Fonte primária | Lei 15.211/2025 |
| VVV | 0.95 |
| Seção | cap_04 §4.4 |
| Status | VÁLIDO |

### AF-007

| Campo | Valor |
|---|---|
| Afirmação | Educação privada: zero SaaS dedicado existente |
| Classificação | FACT |
| Fonte primária | VVV auditado BP v2.0 §1.3 |
| VVV | 0.95 |
| Seção | cap_04 §4.4 |
| Status | VÁLIDO |

### AF-008

| Campo | Valor |
|---|---|
| Afirmação | Mesma estrutura de dor aparece em 4 segmentos, variando sistemas e urgência |
| Classificação | INFERENCE |
| Fonte primária | mapeamento empathy maps 4 personas |
| Fonte secundária | transcricao-reuniao-neogov.txt |
| VVV | 0.85 |
| Seção | cap_04 §4.3 |
| Status | VÁLIDO · será validado no Cap 07 |

### AF-009

| Campo | Valor |
|---|---|
| Afirmação | 5 produtos derivam de equação gargalo + insumo NeoGov |
| Classificação | INFERENCE |
| Fonte primária | BP v2.0 §2.2 |
| Fonte secundária | DATA-v2.json products |
| VVV | 0.90 |
| Seção | cap_04 §4.6 |
| Status | VÁLIDO |

### AF-010

| Campo | Valor |
|---|---|
| Afirmação | Pivô de R$600k/12 meses para R$15-50k/4-8 semanas |
| Classificação | INFERENCE |
| Fonte primária | BP v2.0 §Sumário |
| Fonte secundária | transcricao Camila "corpo a corpo está ficando passado" |
| VVV | 0.85 |
| Seção | cap_04 §4.6 |
| Status | VÁLIDO |

### AF-011

| Campo | Valor |
|---|---|
| Afirmação | Confidata pricing R$497-R$3.497/mês |
| Classificação | FACT |
| Fonte primária | Site público Confidata |
| VVV | 0.95 |
| Seção | cap_04 §4.7 |
| Status | VÁLIDO |

### AF-012

| Campo | Valor |
|---|---|
| Afirmação | Art. 75 IV "d" Lei 14.133/2021 aplica-se a ICT com IP registrado INPI |
| Classificação | FACT |
| Fonte primária | Lei 14.133/2021 Art. 75 IV |
| Fonte secundária | Análise jurídica Gislênia (BP v2.0) |
| VVV | 0.90 |
| Seção | cap_04 §4.6 |
| Status | VÁLIDO · condicionado ao registro INPI prévio |

---

## Sprint 1.2 — Capítulo 07 Personas

_A ser preenchido durante execução do Sprint 1.2._

## Sprint 1.3 — Capítulo 11 Solução · Produtos

_A ser preenchido durante execução do Sprint 1.3._
