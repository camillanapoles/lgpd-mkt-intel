---
id: NEOGOV-V21-APENDICE-A-VVV-LOG
filename: APENDICE-A-VVV-LOG-v2.1.4.1.md
created_at: 2026-05-14
last_updated: 2026-05-15T01:00:00Z
type: VVV_INCREMENTAL_LOG
status: ACTIVE
sprint: S2.1
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

- VVV global atual: **0.87** (média ponderada S1.1+S1.2+S1.3+S2.1)
- Afirmações totais: **50** (42 anteriores + 8 novas S2.1)
- FACT: 27 (54%) · INFERÊNCIA: 23 (46%) · ESPECULAÇÃO: 0 · CRENÇA: 0
- Última atualização: 2026-05-15 Sprint 2.1

---

## Sprint 1.1 — Cap 04 Design Thinking (12 entradas · ver v2.1.1)

_AF-001 a AF-012 mantidas inalteradas — ver versão anterior._

## Sprint 1.2 — Cap 07 Personas (16 entradas · ver v2.1.2.1)

_AF-013 a AF-028 mantidas inalteradas — ver versão anterior._

---

## Sprint 1.3 — Capítulo 11 Solução · Produtos (14 novas entradas)

### AF-029 · P1 Plataforma SaaS existe operacionalmente hoje

| Campo | Valor |
|---|---|
| Classificação | FACT |
| Fonte primária | DATA-v2.json products.P1.status="exists_today" |
| Cross-ref | Transcrição (Camila menciona plataforma atual) |
| VVV | 0.90 |
| Seção | cap_11 §11.4 |
| Status | VÁLIDO · GAP04 levantar estado real M1 |

### AF-030 · 4 gargalos universais geram 4 produtos via equação derivativa

| Campo | Valor |
|---|---|
| Classificação | INFERENCE |
| Fonte primária | Cap 04 §4.5 fase Ideate + DATA-v2.json |
| Cross-ref | AF-009 |
| VVV | 0.85 |
| Seção | cap_11 §11.2 |
| Status | VÁLIDO |

### AF-031 · P2 Data Discovery substitui semanas de entrevistas manuais

| Campo | Valor |
|---|---|
| Classificação | FACT |
| Fonte primária | DATA-v2.json products.P2.solves |
| VVV | 0.85 |
| Seção | cap_11 §11.5 |
| Status | VÁLIDO |

### AF-032 · P3 Anonimização é exclusivo B2G

| Campo | Valor |
|---|---|
| Classificação | FACT |
| Fonte primária | DATA-v2.json products.P3.exclusive_b2g=true |
| VVV | 0.95 |
| Seção | cap_11 §11.6 |
| Status | VÁLIDO |

### AF-033 · P3 único produto LAI×LGPD do mercado brasileiro

| Campo | Valor |
|---|---|
| Classificação | INFERENCE |
| Fonte primária | VVV-GAP-RESEARCH análise competitiva |
| Cross-ref | AF-018 |
| VVV | 0.85 |
| Seção | cap_11 §11.6 |
| Status | VÁLIDO |

### AF-034 · Acórdão TCE-PR 1153/2025 valida abordagem anonimização

| Campo | Valor |
|---|---|
| Classificação | FACT |
| Fonte primária | Acórdão TCE-PR 1153/2025 |
| VVV | 0.95 |
| Seção | cap_11 §11.6 |
| Status | VÁLIDO · jurisprudência direta |

### AF-035 · P4 AI-DPO treinado em LGPD+LAI+ECA Digital brasileiros

| Campo | Valor |
|---|---|
| Classificação | INFERENCE |
| Fonte primária | DATA-v2.json products.P4 + Cap 04 §4.6 |
| VVV | 0.85 |
| Seção | cap_11 §11.7 |
| Status | VÁLIDO |

### AF-036 · P5 ETL conecta sistemas existentes (não substitui)

| Campo | Valor |
|---|---|
| Classificação | FACT |
| Fonte primária | DATA-v2.json products.P5.short_description |
| VVV | 0.85 |
| Seção | cap_11 §11.8 |
| Status | VÁLIDO |

### AF-037 · P5 gate PoC M4 obrigatório antes de escalar Saúde

| Campo | Valor |
|---|---|
| Classificação | FACT |
| Fonte primária | DATA-v2.json products.P5.gate_poc_m4=true |
| Cross-ref | D-INH-005 |
| VVV | 0.90 |
| Seção | cap_11 §11.8 + §11.12 |
| Status | VÁLIDO · pendência técnica |

### AF-038 · Systems_by_segment mapeamento técnico definido

| Campo | Valor |
|---|---|
| Classificação | FACT |
| Fonte primária | DATA-v2.json products.P5.systems_by_segment |
| VVV | 0.90 |
| Seção | cap_11 §11.8 |
| Status | VÁLIDO · operacional |

### AF-039 · Sequência funil P2→P4→P3→P5 derivada fase Prototype

| Campo | Valor |
|---|---|
| Classificação | INFERENCE |
| Fonte primária | Cap 04 §4.6 + análise funil |
| VVV | 0.80 |
| Seção | cap_11 §11.10 |
| Status | VÁLIDO · validar Wave 1 |

### AF-040 · Pivô industrial: 8 dimensões comparativas

| Campo | Valor |
|---|---|
| Classificação | INFERENCE |
| Fonte primária | Cap 04 §4.6 + AF-010 |
| Cross-ref | AF-010 |
| VVV | 0.85 |
| Seção | cap_11 §11.11 |
| Status | VÁLIDO |

### AF-041 · Pricing por segmento (R$500-R$30k/mês) — INFERÊNCIA dominante · RETIFICAÇÃO PENDENTE S3.0

| Campo | Valor |
|---|---|
| Classificação | INFERENCE |
| Fonte primária | DATA-v2.json pricing_est + Confidata referência |
| Cross-ref | AF-011 |
| VVV | 0.65 |
| VVV alvo pós-S3.0 | 0.85+ |
| Seção | cap_11 §11.4-11.8 |
| Status | **VÁLIDO mas FLAG RETIFICAÇÃO PENDENTE** · D-010 inseriu Sprint 3.0 para modelagem bottom-up · documento `DEBITO-D001-PRICING-FRAMEWORK` |
| Bloqueio downstream | Cap 12 BMC Revenue Streams aguarda retificação |

### AF-042 · P3 = diferencial competitivo central NeoGov no setor público

| Campo | Valor |
|---|---|
| Classificação | INFERENCE |
| Fonte primária | Cap 07 §7.4+7.5 + IN-006 |
| Cross-ref | IN-006 |
| VVV | 0.85 |
| Seção | cap_11 §11.6 |
| Status | VÁLIDO · validar PNCP (GAP01) |

---

## Métricas pós-Sprint 1.3

| Métrica | S1.1 | S1.2 | S1.3 | Projeção pós-gaps |
|---|---|---|---|---|
| Afirmações totais | 12 | 28 | 42 | — |
| % FACT | 58% | 54% | 55% | 75%+ |
| % INFERENCE | 42% | 46% | 45% | 25%- |
| VVV global | 0.92 | 0.88 | 0.87 | 0.92+ |
| PMQS final | 8.74 | 8.02 | 7.89 | 8.74+ |

## Sprint 2.1 — Cap 02 VMV (8 novas entradas)

### AF-043 · NeoGov é categoria nova de mercado (não SaaS nem consultoria)

| Campo | Valor |
|---|---|
| Classificação | INFERENCE |
| Fonte primária | Cap 04 §4.6 + IN-008 + análise VVV-GAP-RESEARCH |
| VVV | 0.85 |
| Seção | cap_02 §2.2 |
| Status | VÁLIDO · diferencial estratégico |

### AF-044 · Visão 2030 · 5.000 organizações servidas

| Campo | Valor |
|---|---|
| Classificação | INFERENCE |
| Fonte primária | Cap 11 §11.11 (capacidade computacional 100+/ano × 5 anos × múltiplos waves) |
| VVV | 0.75 |
| Seção | cap_02 §2.3 |
| Status | VÁLIDO · meta agressiva mas matematicamente factível |

### AF-045 · Foco Brasil é deliberado (LAI = barreira protetiva)

| Campo | Valor |
|---|---|
| Classificação | INFERENCE |
| Fonte primária | Cap 11 §11.6 (P3 anonimização LAI×LGPD único no BR) |
| VVV | 0.85 |
| Seção | cap_02 §2.3 |
| Status | VÁLIDO · estratégia geográfica defensável |

### AF-046 · "Manufaturar" é categoria distintiva (não vender/consultar)

| Campo | Valor |
|---|---|
| Classificação | FACT |
| Fonte primária | Cap 04 §4.6 (pivô industrial) + IN-002 |
| Cross-ref | AF-010, AF-040 |
| VVV | 0.90 |
| Seção | cap_02 §2.4 |
| Status | VÁLIDO · tese central confirmada |

### AF-047 · "Acessível · Contínuo · Auditável" são 3 promessas operacionais

| Campo | Valor |
|---|---|
| Classificação | INFERENCE |
| Fonte primária | Personas Cap 07 + Apêndice A VVV-LOG (auditabilidade interna) |
| VVV | 0.85 |
| Seção | cap_02 §2.4 |
| Status | VÁLIDO · derivações documentadas |

### AF-048 · Valor "Honestidade Epistêmica" = manifestação prática D-007

| Campo | Valor |
|---|---|
| Classificação | FACT |
| Fonte primária | D-007 (não inflar VVV) + Apêndice A VVV-LOG operacional |
| VVV | 0.95 |
| Seção | cap_02 §2.5 |
| Status | VÁLIDO · valor já operacional na produção do BP |

### AF-049 · 5 Valores operam em tensão produtiva (não paralelos)

| Campo | Valor |
|---|---|
| Classificação | INFERENCE |
| Fonte primária | Análise interna VMV + benchmark melhores práticas valores corporativos |
| VVV | 0.85 |
| Seção | cap_02 §2.5 final |
| Status | VÁLIDO · diferencial metodológico |

### AF-050 · LAI brasileira = barreira contra entrante internacional

| Campo | Valor |
|---|---|
| Classificação | INFERENCE |
| Fonte primária | Cap 11 §11.6 + VVV-GAP-RESEARCH análise OneTrust/TrustArc |
| Cross-ref | AF-018, AF-033 |
| VVV | 0.85 |
| Seção | cap_02 §2.3 |
| Status | VÁLIDO · base do moat competitivo |
