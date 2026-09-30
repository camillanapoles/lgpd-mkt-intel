---
id: NEOGOV-V21-APENDICE-C-INSIGHTS-CARRY
filename: APENDICE-C-INSIGHTS-CARRY-v2.1.3.1.md
created_at: 2026-05-14
last_updated: 2026-05-15T00:10:00Z
type: INSIGHTS_INTER_SPRINT_LOG
status: ACTIVE
sprint: S1.3
edicao: 1
parent_doc: BUSINESS-PLAN-FINAL-v2.1
purpose: Descobertas em Sprint N que ajustam Sprint N+1 · garantia de continuidade
update_rule: Append no Sprint origem · consumido no Sprint destino · sempre mantido
final_destination: Apêndice C do BP final (nota de transparência metodológica)
tags: [insights, continuidade, inter-sprint, aprendizado]
---

# Apêndice C · Insights Inter-Sprint (Carry-Over)

## Métricas

- Insights registrados: **10** (4 S1.1 + 3 S1.2 + 3 S1.3)
- Insights consumidos: 6 (IN-001, IN-002, IN-003, IN-004, IN-005, IN-006)
- Insights pendentes: 4 (IN-007 destino S4.3, IN-008/009/010 novos)
- Última atualização: 2026-05-15 Sprint 1.3

---

## Sprint 1.1 → Sprint 1.2 — TODOS CONSUMIDOS

| ID | Status |
|---|---|
| IN-001 (4 personas) | ✅ INCORPORADO Cap 07 §7.2 |
| IN-002 (pivô industrial) | ✅ INCORPORADO Cap 11 §11.1 + §11.11 |
| IN-003 (discurso específico) | ✅ INCORPORADO Cap 07 §7.4-7.7 |
| IN-004 (produtos universais) | ✅ INCORPORADO Cap 11 §11.3 (template adaptação por segmento) |

## Sprint 1.2 → Sprint 1.3 — TODOS CONSUMIDOS

| ID | Status |
|---|---|
| IN-005 (Persona × Produto-Âncora) | ✅ INCORPORADO Cap 11 todas as 5 subseções §11.4-11.8 |
| IN-006 (P3 = âncora B2G universal) | ✅ INCORPORADO Cap 11 §11.6 (subseção dedicada) |
| IN-007 (Mantenedor pitch educativo) | ⏭ PENDENTE · destino S4.3 (Cap 14 GTM) |

---

## Sprint 1.3 → Sprint 2.1/2.2 (NOVOS · Cap 11 → Caps 02, 01)

### IN-008 · NeoGov vende KNOWLEDGE MANUFATURADO (não software puro nem consultoria)

| Campo | Valor |
|---|---|
| Tipo | NEW_DATA |
| Sprint origem | S1.3 |
| Sprint destino | S2.1 (Cap 02 VMV) |
| Descoberta | A análise pivô industrial §11.11 revela que NeoGov não é SaaS puro (concorrência OneTrust) nem consultoria pura (concorrência Big4). O produto vendido é **knowledge jurídico manufaturado em produto via IA**. Essa categoria não existe no mercado brasileiro — é categoria nova. |
| Ação em S2.1 | Visão e Missão devem refletir explicitamente "knowledge manufaturado" como tese. Não copiar VMV de SaaS típico nem de consultoria típica. |
| Impacto VVV | 0 (insight emergente) |
| Incorporado no BP | true (em S2.1) |
| Seção BP afetada | cap_02_vmv |
| Status | PENDENTE |

### IN-009 · Há 3 fontes de receita distintas (não apenas SaaS)

| Campo | Valor |
|---|---|
| Tipo | NEW_DATA |
| Sprint origem | S1.3 |
| Sprint destino | S3.1 (Cap 12 BMC) |
| Descoberta | O Cap 11 evidencia que NeoGov tem 3 modelos de receita distintos: (a) **Assinatura mensal** (P1, P4), (b) **Projeto + assinatura** (P2, P5), (c) **Usage-based** (P3 por documento). Isso é mais complexo que SaaS típico — exige modelagem BMC cuidadosa em Revenue Streams. |
| Ação em S3.1 | BMC bloco Revenue Streams deve detalhar os 3 modelos com proporção esperada de receita por modelo (estimativa). |
| Impacto VVV | 0 |
| Incorporado no BP | true |
| Seção BP afetada | cap_12_bmc |
| Status | PENDENTE |

### IN-010 · Sistema "systems_by_segment" é ativo estratégico (não detalhe técnico)

| Campo | Valor |
|---|---|
| Tipo | NEW_DATA |
| Sprint origem | S1.3 |
| Sprint destino | S3.1 (Cap 12 BMC) + S4.3 (Cap 14 GTM) |
| Descoberta | O mapeamento de sistemas-alvo (e-Cidade, MV, Tasy, Class, Phonexao, etc.) é mais que detalhe técnico — é o "BOM" (Bill of Materials) operacional da NeoGov. Determina partnerships estratégicos (BMC bloco Key Partnerships) e canal de venda (Cap 14). |
| Ação em S3.1 | BMC Key Partnerships inclui fabricantes desses sistemas (MV, Sponte, etc.) como parceiros potenciais. |
| Ação em S4.3 | GTM Cap 14 explora canal "parceria com vendor do sistema" como alternativa ao outbound direto. |
| Impacto VVV | 0 |
| Incorporado no BP | true |
| Seção BP afetada | cap_12_bmc · cap_14_gtm |
| Status | PENDENTE |

---

## Sprint 2 → Sprint 3 (será preenchido)

## Sprint 3 → Sprint 4 (será preenchido)

---

## Princípios operacionais (mantidos)

1. **Append no momento da descoberta** — não esperar fim de sprint
2. **Consumir antes de começar próximo** — checklist start_of_sprint inclui ler este doc
3. **Incorporar no BP** — todo insight com `incorporado_no_bp: true` deve estar refletido no capítulo destino
4. **Transparência metodológica** — este doc é evidência de método iterativo (coerente com VVV)
