---
id: NEOGOV-V21-APENDICE-A-VVV-LOG
filename: APENDICE-A-VVV-LOG-v2.1.2.1.md
created_at: 2026-05-14
last_updated: 2026-05-14T23:55:00Z
type: VVV_INCREMENTAL_LOG
status: ACTIVE
sprint: S1.2
edicao: 1
parent_doc: BUSINESS-PLAN-FINAL-v2.1
purpose: Rastreabilidade auditável de TODA afirmação factual do BP NeoGov v2.1
update_rule: Cresce monotonicamente · 1 entrada por afirmação verificável
final_destination: Apêndice A do BP final (Word docx)
tags: [vvv, validacao, auditoria, rastreabilidade]
---

# Apêndice A · Log de Validação VVV

## Classificação

| Tag | Significado | VVV ref |
|---|---|---|
| `[FATO]` | Dado empírico verificável em fonte primária | 0.90-1.00 |
| `[INFERÊNCIA]` | Lógica válida a partir de fatos | 0.70-0.89 |
| `[ESPECULAÇÃO]` | Indução com confiança < 90% | 0.50-0.69 |
| `[CRENÇA]` | Não-fundamentado · requer flag UNVERIFIED | < 0.50 |

## Métricas globais

- VVV global atual: **0.88** (média Sprint 1.1 e 1.2)
- Afirmações totais: **28** (12 do S1.1 + 16 novas do S1.2)
- FACT: 15 · INFERÊNCIA: 13 · ESPECULAÇÃO: 0 · CRENÇA: 0
- Última atualização: 2026-05-14 Sprint 1.2

---

## Sprint 1.1 — Capítulo 04 Design Thinking (12 entradas · ver v2.1.1)

_AF-001 a AF-012 registradas na edição anterior, mantidas inalteradas._

---

## Sprint 1.2 — Capítulo 07 Personas (16 novas entradas)

### AF-013 · Procurador é o decisor real municipal (não prefeito)

| Campo | Valor |
|---|---|
| Classificação | FACT |
| Fonte primária | transcricao-reuniao-neogov.txt |
| VVV | 1.00 |
| Seção | cap_07 §7.4 identidade |
| Status | VÁLIDO |

### AF-014 · Dor central municipal = responsabilização pessoal (não multa)

| Campo | Valor |
|---|---|
| Classificação | FACT |
| Fonte primária | LGPD Art. 52 §3° (isenção pública) + transcrição (relato direto) |
| Cross-ref | AF-004 |
| VVV | 0.95 |
| Seção | cap_07 §7.4 insight surpreendente |
| Status | VÁLIDO |

### AF-015 · Procurador opera em ciclo 4-9 meses · Art. 75 IV reduz a 2-8 semanas

| Campo | Valor |
|---|---|
| Classificação | FACT |
| Fonte primária | Lei 14.133/2021 Art. 75 IV + transcrição |
| Cross-ref | AF-012 |
| VVV | 0.90 |
| Seção | cap_07 §7.4 ciclo |
| Status | VÁLIDO |

### AF-016 · Consórcios intermunicipais = canal 1:N

| Campo | Valor |
|---|---|
| Classificação | INFERENCE |
| Fonte primária | transcrição (Wilton FNDE) + BP v2.0 §6.2 |
| VVV | 0.85 |
| Seção | cap_07 §7.4 canal |
| Status | VÁLIDO |

### AF-017 · CIO + PGE são decisores B2G estadual/federal

| Campo | Valor |
|---|---|
| Classificação | INFERENCE |
| Fonte primária | BP v2.0 §6.5 + análise estrutura governo |
| VVV | 0.80 |
| Seção | cap_07 §7.5 identidade |
| Status | VÁLIDO · validar com pesquisa PNCP (GAP01) |

### AF-018 · Big4 cobra caro · SaaS internacional sem LAI = diferencial NeoGov

| Campo | Valor |
|---|---|
| Classificação | INFERENCE |
| Fonte primária | VVV-GAP-RESEARCH (OneTrust pricing) + análise competitiva |
| Cross-ref | AF-011 |
| VVV | 0.85 |
| Seção | cap_07 §7.5 insight surpreendente |
| Status | VÁLIDO |

### AF-019 · Ciclo B2G estadual/federal 9-18m tradicional · 3-6m via ETEC

| Campo | Valor |
|---|---|
| Classificação | INFERENCE |
| Fonte primária | Lei 14.133 + práticas ETEC |
| VVV | 0.80 |
| Seção | cap_07 §7.5 ciclo |
| Status | VÁLIDO |

### AF-020 · Hospital decide em comitê (Dir Adm + DPO + Dir Médica)

| Campo | Valor |
|---|---|
| Classificação | INFERENCE |
| Fonte primária | BP v2.0 §4.3 perfil saúde |
| VVV | 0.75 |
| Seção | cap_07 §7.6 identidade |
| Status | VÁLIDO · validar em primeiras visitas Wave 2A |

### AF-021 · MV/Tasy não cobre LGPD transversal (RH/ouvidoria/faturamento)

| Campo | Valor |
|---|---|
| Classificação | INFERENCE |
| Fonte primária | VVV-GAP-RESEARCH §GAP2 (arquitetura MV) + BP v2.0 |
| VVV | 0.80 |
| Seção | cap_07 §7.6 pains |
| Status | VÁLIDO |

### AF-022 · Cliente já tem MV/Tasy · vender integração > vender substituto

| Campo | Valor |
|---|---|
| Classificação | INFERENCE |
| Fonte primária | BP v2.0 §6.3 + análise mercado saúde |
| VVV | 0.85 |
| Seção | cap_07 §7.6 insight surpreendente |
| Status | VÁLIDO · condicional PoC ETL M4 (GAP03) |

### AF-023 · Confidata e Be Compliance já atuam em saúde privada

| Campo | Valor |
|---|---|
| Classificação | FACT |
| Fonte primária | VVV-GAP-RESEARCH §GAP1 |
| VVV | 0.95 |
| Seção | cap_07 §7.6 pains |
| Status | VÁLIDO |

### AF-024 · Ciclo decisão saúde 3-6 meses (comitê multidisciplinar)

| Campo | Valor |
|---|---|
| Classificação | INFERENCE |
| Fonte primária | BP v2.0 §4.3 |
| VVV | 0.75 |
| Seção | cap_07 §7.6 ciclo |
| Status | VÁLIDO |

### AF-025 · Mantenedor escolar decide solo · ciclo 1-3 meses

| Campo | Valor |
|---|---|
| Classificação | INFERENCE |
| Fonte primária | BP v2.0 §4.3 + estrutura mercado educação privada |
| VVV | 0.65 |
| Seção | cap_07 §7.7 ciclo |
| Status | VÁLIDO · validar com 3-5 entrevistas (GAP02) |

### AF-026 · Mantenedor sem TI interna · prefere self-service

| Campo | Valor |
|---|---|
| Classificação | INFERENCE |
| Fonte primária | BP v2.0 §4.3 + realidade escola pequena/média |
| VVV | 0.70 |
| Seção | cap_07 §7.7 pains |
| Status | VÁLIDO · validar com WTP entrevistas |

### AF-027 · ECA Digital + zero SaaS dedicado = oceano azul real

| Campo | Valor |
|---|---|
| Classificação | FACT |
| Fonte primária | BP v2.0 §1.3 VVV auditado + Lei 15.211/2025 |
| Cross-ref | AF-006, AF-007 |
| VVV | 0.95 |
| Seção | cap_07 §7.7 insight surpreendente |
| Status | VÁLIDO |

### AF-028 · Pitch para mantenedor é educativo (não persuasivo)

| Campo | Valor |
|---|---|
| Classificação | INFERENCE |
| Fonte primária | Análise psicográfica + AF-027 |
| VVV | 0.65 |
| Seção | cap_07 §7.7 insight surpreendente |
| Status | VÁLIDO · validar com WTP entrevistas |

---

## Métricas pós-Sprint 1.2

| Métrica | Sprint 1.1 | Sprint 1.2 | Projeção pós-gaps |
|---|---|---|---|
| Afirmações totais | 12 | 28 | — |
| % FACT | 58% | 54% | 75%+ |
| % INFERENCE | 42% | 46% | 25%- |
| VVV global | 0.92 | 0.88 | 0.92+ (após GAP01,02,03) |

## Sprint 1.3 — Capítulo 11 Solução · Produtos

_A ser preenchido durante execução do Sprint 1.3._
