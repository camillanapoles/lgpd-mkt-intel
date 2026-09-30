---
id: NEOGOV-V21-APENDICE-C-INSIGHTS-CARRY
filename: APENDICE-C-INSIGHTS-CARRY-v2.1.2.1.md
created_at: 2026-05-14
last_updated: 2026-05-14T23:55:00Z
type: INSIGHTS_INTER_SPRINT_LOG
status: ACTIVE
sprint: S1.2
edicao: 1
parent_doc: BUSINESS-PLAN-FINAL-v2.1
purpose: Descobertas em Sprint N que ajustam Sprint N+1 · garantia de continuidade
update_rule: Append no Sprint origem · consumido no Sprint destino · sempre mantido
final_destination: Apêndice C do BP final (nota de transparência metodológica)
tags: [insights, continuidade, inter-sprint, aprendizado]
---

# Apêndice C · Insights Inter-Sprint (Carry-Over)

## Métricas

- Insights registrados: **7** (4 do S1.1 + 3 novos do S1.2)
- Insights consumidos: 2 (IN-001, IN-003 incorporados no Cap 07)
- Insights pendentes (para próximos sprints): 5
- Última atualização: 2026-05-14 Sprint 1.2

---

## Sprint 1.1 → Sprint 1.2 (CONSUMIDOS NESTE SPRINT)

### IN-001 · Insight central: 4 personas (não 5) — **INCORPORADO**

| Campo | Valor |
|---|---|
| Status | ✅ INCORPORADO em Cap 07 §7.2 |
| Como foi incorporado | CIO estadual + Subsec federal consolidados em "Gestor B2G estadual/federal" com nota de variação · gerou DECISÃO D-008 |
| Impacto VVV | Neutro (transparência preservada) |

### IN-002 · Pivô industrial é tese central — **CARREGADO PARA S1.3**

| Campo | Valor |
|---|---|
| Status | PENDENTE · destino Sprint 1.3 (Cap 11) |
| Ação prevista S1.3 | Cap 11 abre com pivô explícito + cada produto como instrumento do pivô |

### IN-003 · Discurso comercial específico por persona — **INCORPORADO**

| Campo | Valor |
|---|---|
| Status | ✅ INCORPORADO em Cap 07 §7.4-7.7 |
| Como foi incorporado | Subseção "Insight Surpreendente" explícita em cada uma das 4 personas com pivô discursivo único |
| Impacto VVV | +0.03 reforçando posicionamento competitivo |

### IN-004 · Produtos universais adaptáveis — **CARREGADO PARA S1.3 e S3.1**

| Campo | Valor |
|---|---|
| Status | PENDENTE · destino Sprint 1.3 (Cap 11) e Sprint 3.1 (Cap 12 BMC) |
| Ação prevista S1.3 | Cap 11 estrutura cada produto como universal com seção "como se adapta por segmento" |

---

## Sprint 1.2 → Sprint 1.3 (NOVOS · Cap 07 → Cap 11)

### IN-005 · Mapeamento Persona × Produto-Âncora descoberto

| Campo | Valor |
|---|---|
| Tipo | NEW_DATA |
| Sprint origem | S1.2 |
| Sprint destino | S1.3 |
| Descoberta | Cada persona tem um produto-âncora específico: Procurador → P3 Anonimização · Gestor B2G → P3 Anonimização · Diretor Saúde → P5 ETL · Mantenedor → P1 Plataforma. Produto-âncora ≠ produto-de-entrada (Data Discovery é entrada em todos), mas é o produto que entrega valor central por persona. |
| Ação em Sprint 1.3 | Cap 11 deve apresentar cada produto com seção "Persona-âncora primária + como se adapta para outras personas". |
| Impacto VVV | 0 (insight emergente do mapeamento) |
| Incorporado no BP | true (em S1.3) |
| Seção BP afetada | cap_11_produtos |
| Status | PENDENTE |

### IN-006 · Anonimização LAI/LGPD é produto-âncora B2G universal

| Campo | Valor |
|---|---|
| Tipo | CONFIRMATION |
| Sprint origem | S1.2 |
| Sprint destino | S1.3 e S3.1 (Cap 12 BMC) |
| Descoberta | Tanto Procurador municipal quanto Gestor B2G estadual/federal têm o mesmo produto-âncora (P3 Anonimização LAI/LGPD). Isso confirma que esse produto é o **diferencial competitivo central** da NeoGov para todo o setor público, não apenas municipal. |
| Ação em Sprint 1.3 | P3 deve receber maior espaço no Cap 11 + status "produto-âncora B2G universal" explícito. |
| Ação em Sprint 3.1 | BMC Value Propositions destaca P3 como proposta de valor diferenciada B2G. |
| Impacto VVV | +0.02 (consolida posicionamento) |
| Incorporado no BP | true |
| Seção BP afetada | cap_11_produtos · cap_12_bmc |
| Status | PENDENTE |

### IN-007 · Mantenedor escolar pede pitch educativo (não persuasivo)

| Campo | Valor |
|---|---|
| Tipo | NEW_DATA |
| Sprint origem | S1.2 |
| Sprint destino | S4.3 (Cap 14 GTM) |
| Descoberta | Diferentemente das outras 3 personas que sabem da dor LGPD, o Mantenedor escolar **não reconhece ECA Digital como problema próprio ainda**. O pitch precisa primeiro educar (oceano azul ainda não "verde") e depois vender. Marketing precisa de etapa de educação pré-funil. |
| Ação em Sprint 4.3 | GTM Cap 14 inclui estratégia de "marketing educativo" para Gamma (whitepapers ECA Digital, webinars FENEP, lives diretor escola). Diferente de outbound clássico. |
| Impacto VVV | 0 |
| Incorporado no BP | true |
| Seção BP afetada | cap_14_gtm |
| Status | PENDENTE |

---

## Sprint 1.3 → Sprint 2.1

_A ser preenchido após produção do Sprint 1.3._

---

## Princípios operacionais (mantidos)

1. **Append no momento da descoberta** — não esperar fim de sprint
2. **Consumir antes de começar próximo** — checklist start_of_sprint inclui ler este doc
3. **Incorporar no BP** — todo insight com `incorporado_no_bp: true` deve estar refletido no capítulo destino
4. **Transparência metodológica** — este doc é evidência de método iterativo (coerente com VVV)
