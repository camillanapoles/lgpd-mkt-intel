---
id: NEOGOV-V21-APENDICE-B-DECISIONS-LOG
filename: APENDICE-B-DECISIONS-LOG-v2.1.2.1.md
created_at: 2026-05-14
last_updated: 2026-05-14T23:55:00Z
type: DECISIONS_RATIONALE_LOG
status: ACTIVE
sprint: S1.2
edicao: 1
parent_doc: BUSINESS-PLAN-FINAL-v2.1
purpose: Registrar TODA decisão de produção com opções consideradas e rationale
update_rule: Append-only · cresce a cada decisão tomada
final_destination: Apêndice B do BP final (Word docx)
tags: [decisoes, rationale, governanca, dtp]
---

# Apêndice B · Log de Decisões e Rationale

## Métricas

- Decisões registradas: **6** (D-001 a D-006)
- Decisões herdadas: 7 (D-INH-001 a D-INH-007)
- Decisões revisadas: 0
- Decisões refutadas: 0
- Última atualização: 2026-05-14 Sprint 1.2

## Decisões pré-existentes (herdadas do BP v2.0)

_D-INH-001 a D-INH-007 mantidas inalteradas (ver v2.1.1)._

## Decisões Sprint 1.1 (D-001 a D-005)

_Mantidas inalteradas (ver v2.1.1)._

---

## Decisões Sprint 1.2

### D-006 · Estrutura "fichas profundas canvas" para Capítulo 07 (não tabela comparativa)

| Campo | Valor |
|---|---|
| Sprint | 1.2 |
| Data | 2026-05-14 |
| Contexto | Como apresentar as 4 personas no Cap 07 |
| Opção A | Tabela comparativa lado a lado das 4 personas — REJEITADA (falta profundidade individual) |
| Opção B | 4 fichas profundas canvas com estrutura idêntica de 7 elementos **ESCOLHIDA** |
| Opção C | Narrativa de jornada por persona — REJEITADA (perde reaproveitamento no Vue) |
| Rationale | Cada persona merece tratamento individual completo para sustentar o VPC do Cap 13. Estrutura idêntica facilita comparação direta. Síntese §7.8 fornece a visão comparativa que seria a opção A. Reaproveitamento alto como componente `<PersonaCard>` no Vue App. |
| Impacto próximos sprints | Cap 13 VPC tem 4 inputs estruturados prontos. Cap 14 GTM tem 4 perfis com canal/ciclo/ticket. Vue App tem template `<PersonaCard>` clonável. |
| Revisível | NÃO |

### D-007 · Aceitar PMQS 8.02 ao invés de inflar VVV artificialmente

| Campo | Valor |
|---|---|
| Sprint | 1.2 |
| Data | 2026-05-14 |
| Contexto | PMQS final do Cap 07 = 9.43 × 0.85 = 8.02 (abaixo do alvo 9.5) |
| Opção A | Refinar texto para subir PMQS bruto de 9.43 para 9.50 — REJEITADA (ganho mínimo, retrabalho alto) |
| Opção B | Inflar VVV inventando fontes — REJEITADA (VIOLAÇÃO MANDATO VVV) |
| Opção C | Aceitar PMQS 8.02 honesto com plano de upgrade futuro **ESCOLHIDA** |
| Rationale | Inflação artificial de VVV destrói o valor do próprio mecanismo VVV. PMQS bruto 9.43 já está no alvo qualitativo. O delta -1.48 vem da honestidade na classificação de 3 das 4 personas como [INFERÊNCIA] dependente de validação primária. Conforme GAPs forem fechados (GAP01 PNCP, GAP02 WTP, GAP03 PoC), VVV das personas Beta/Gamma/Alfa-E sobe organicamente. |
| Impacto próximos sprints | Reset do alvo PMQS de 9.5 para ≥ 8.0 com VVV honesto. Aceito que PMQS 9.5 só é atingível com VVV 1.0 (matematicamente). |
| Revisível | SIM · ao fechar GAPs externos, revisar VVV e re-calcular PMQS retroativamente |

### D-008 · Consolidar CIO estadual + Subsec federal em 1 persona "Gestor B2G"

| Campo | Valor |
|---|---|
| Sprint | 1.2 |
| Data | 2026-05-14 |
| Contexto | Insight IN-001 do Sprint 1.1 sugeria 4 personas (não 5) |
| Opção A | Manter 5 personas separadas (CIO estadual + Subsec federal) — REJEITADA |
| Opção B | Consolidar em 1 persona "Gestor B2G estadual/federal" com nota de variação **ESCOLHIDA** |
| Rationale | Estrutura de dor compartilhada (LAI×LGPD + sistemas legados + Big4 caro). Variação fica em ciclo (estadual mais rápido que federal via ETEC) e ticket (federal maior). Manter 5 personas inflaria sem ganho informacional. |
| Impacto próximos sprints | VPC Cap 13 tem 4 inputs (não 5). GTM Cap 14 com 4 estratégias. Nota de variação estadual/federal preservada na persona consolidada. |
| Revisível | SIM · se PNCP (GAP01) revelar dores divergentes, separar |

---

## Template de entrada de decisão (referência)

_Mantido inalterado (ver v2.1.1)._
