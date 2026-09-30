---
id: NEOGOV-V21-APENDICE-B-DECISIONS-LOG
filename: APENDICE-B-DECISIONS-LOG-v2.1.3.2.md
created_at: 2026-05-14
last_updated: 2026-05-15T00:25:00Z
type: DECISIONS_RATIONALE_LOG
status: ACTIVE
sprint: S1.3
edicao: 2
parent_doc: BUSINESS-PLAN-FINAL-v2.1
purpose: Registrar TODA decisão de produção com opções consideradas e rationale
update_rule: Append-only · cresce a cada decisão tomada
final_destination: Apêndice B do BP final (Word docx)
tags: [decisoes, rationale, governanca, dtp]
---

# Apêndice B · Log de Decisões e Rationale

## Métricas

- Decisões registradas: **10** (D-001 a D-010)
- Decisões herdadas: 7 (D-INH-001 a D-INH-007)
- Última atualização: 2026-05-15 Sprint 1.3 edição 2 (débito D001)

## Decisões herdadas BP v2.0

_D-INH-001 a D-INH-007 mantidas — ver v2.1.1._

## Decisões Sprint 1.1 (D-001 a D-005)

_Mantidas — ver v2.1.1._

## Decisões Sprint 1.2 (D-006 a D-008)

_Mantidas — ver v2.1.2.1._

---

## Decisões Sprint 1.3

### D-009 · Estrutura "fichas profundas + matriz + sequência" para Capítulo 11

| Campo | Valor |
|---|---|
| Sprint | 1.3 |
| Data | 2026-05-15 |
| Contexto | Como apresentar os 5 produtos no Cap 11 |
| Opção A | Lista linear (5 produtos descritos sequencialmente) — REJEITADA (perde rigor derivativo) |
| Opção B | 5 fichas profundas + matriz síntese + sequência de venda **ESCOLHIDA** |
| Opção C | Por persona (Procurador usa X+Y, Mantenedor usa Z) — REJEITADA (duplica Cap 07) |
| Rationale | Cada produto merece tratamento individual com equação derivativa, persona-âncora, adaptação por sistema. Matriz §11.9 fornece visão comparativa. Sequência §11.10 fornece playbook comercial. Reaproveitamento alto como `<ProdutoCard>` no Vue. |
| Impacto próximos sprints | Cap 12 BMC tem 5 produtos estruturados (Value Propositions). Cap 13 VPC tem 4 personas × 5 produtos = 20 combos mapeáveis. Cap 14 GTM herda sequência §11.10 como playbook. |
| Revisível | NÃO |

### D-010 · Inserir Sprint 3.0 · Modelagem de Precificação Assertiva (NOVO)

| Campo | Valor |
|---|---|
| Sprint | 1.3 edição 2 (pós-Gate Sprint 1) |
| Data | 2026-05-15 |
| Contexto | Usuário identificou gap crítico: Cap 11 §pricing tem VVV 0.65 (inferência top-down baseada em Confidata). Insuficiente para compor BMC Revenue Streams + Cost Structure. |
| Opção A | Modelagem antes do Sprint 2 (sprint S1.4 emergencial) — REJEITADA (atrasa VMV) |
| Opção B | **Sprint 3.0 NOVO antes do BMC ESCOLHIDA** (FDC-U 9.18) |
| Opção C | Manter ordem · pricing provisório · refazer no Cap 15 — REJEITADA (retrabalho downstream) |
| Rationale | Sprint 3.0 fornece inputs assertivos (custo bottom-up + unit economics + WTP) para Cap 12 BMC (Revenue Streams, Cost Structure) e Cap 14 GTM (preço afeta canal). Preserva momentum Sprint 2 (identidade). Análise FDC-U deu 9.18 vs 8.40 (A) e 6.34 (C). |
| Impacto próximos sprints | Sprint 2 (VMV+Capa) inalterado. **Sprint 3.0 NOVO** antes do BMC. Sprint 3.1-3.3 (BMC+VPC+Porter) reordenados como dependentes. Sprint 4.2 (Financeiro) absorve resultado do S3.0. |
| Entregáveis S3.0 | (1) Modelagem custo bottom-up · (2) Unit economics · (3) Pricing assertivo · (4) APENDICE-D-MODELO-CUSTO.xlsx · (5) Retificação Cap 11 §pricing |
| Bloqueio | Sprint 3.1 BMC NÃO pode iniciar sem Sprint 3.0 concluído (gate explícito) |
| Revisível | NÃO (decisão estrutural sobre o roadmap) |
| Documento de detalhamento | `continuity/DEBITO-D001-PRICING-FRAMEWORK-v2.1.3.1.md` |

---

## Template de entrada de decisão (referência)

_Mantido inalterado — ver v2.1.1._
