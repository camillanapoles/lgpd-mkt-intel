---
id: NEOGOV-V21-APENDICE-C-INSIGHTS-CARRY
filename: APENDICE-C-INSIGHTS-CARRY.md
created_at: 2026-05-14
last_updated: 2026-05-14T23:50:00Z
type: INSIGHTS_INTER_SPRINT_LOG
status: ACTIVE
parent_doc: BUSINESS-PLAN-FINAL-v2.1
purpose: Descobertas em Sprint N que ajustam Sprint N+1 · garantia de continuidade
update_rule: Append no Sprint origem · consumido no Sprint destino · sempre mantido
final_destination: Apêndice C do BP final (nota de transparência metodológica)
tags: [insights, continuidade, inter-sprint, aprendizado]
---

# Apêndice C · Insights Inter-Sprint (Carry-Over)

> Toda descoberta feita durante um sprint que ajusta, confirma, contradiz ou adiciona dado para sprint seguinte é registrada aqui. Garante zero perda de contexto entre etapas de produção.

## Métricas

- Insights registrados: **4** (Sprint 1.1)
- Tipos: ADJUSTMENT · CONFIRMATION · CONTRADICTION · NEW_DATA
- Última atualização: 2026-05-14 Sprint 1.1

---

## Sprint 1.1 → Sprint 1.2 (Cap 04 DT → Cap 07 Personas)

### IN-001 · Insight central: 4 personas (não 5)

| Campo | Valor |
|---|---|
| Tipo | ADJUSTMENT |
| Sprint origem | S1.1 |
| Sprint destino | S1.2 |
| Descoberta | Durante mapeamento da fase Empathize, identifiquei 4 personas distintas com dor mapeada (procurador municipal, CIO estadual/federal, diretor saúde, mantenedor escolar) — não 5. A quinta persona "subsecretário federal de TIC" mencionada antes seria projeção do alvo declarado Wave 2C, não dor primária mapeada. |
| Ação em Sprint 1.2 | Sprint 1.2 produz **4 empathy maps detalhados** (não 5). CIO estadual e Subsecretário federal são consolidados em uma persona "Gestor B2G estadual/federal" pois compartilham estrutura de dor. |
| Impacto VVV | 0 (transparência metodológica) |
| Incorporado no BP | true |
| Seção BP afetada | cap_07_personas + cap_13_vpc |
| Status | PENDENTE (consumir em S1.2) |

### IN-002 · Confirmação: pivô serviço → indústria é tese central

| Campo | Valor |
|---|---|
| Tipo | CONFIRMATION |
| Sprint origem | S1.1 |
| Sprint destino | S1.3 |
| Descoberta | A fase Prototype do Cap 04 reforçou que a transição de R$600k/12 meses para R$15-50k/4-8 semanas via IA + ICT é a tese central. Não é só pricing — é mudança de paradigma operacional. |
| Ação em Sprint 1.3 | Sprint 1.3 (Cap 11 Produtos) deve abrir com "como cada produto é instrumento do pivô industrial". Cada produto descrito mostra: insumo NeoGov + IA = produto manufaturado. |
| Impacto VVV | +0.02 (afirmação já forte fica mais sustentada) |
| Incorporado no BP | true |
| Seção BP afetada | cap_11_produtos abertura |
| Status | PENDENTE (consumir em S1.3) |

### IN-003 · Novo dado: discurso comercial é específico por persona

| Campo | Valor |
|---|---|
| Tipo | NEW_DATA |
| Sprint origem | S1.1 |
| Sprint destino | S1.2 e Sprint 4 (S4.3 GTM) |
| Descoberta | Os 4 POVs revelaram insights surpreendentes específicos por persona: (1) procurador teme improbidade, não multa; (2) CIO estadual valoriza LAI×LGPD, não compliance geral; (3) diretor saúde busca integração, não outro sistema; (4) mantenedor escolar busca self-service, não consultoria. Isso muda o discurso comercial inteiro. |
| Ação em Sprint 1.2 | Para cada persona em Cap 07, registrar explicitamente o "insight surpreendente" como subseção própria. Para Sprint 4 (GTM), preparar 4 pitch decks distintos. |
| Impacto VVV | 0 |
| Incorporado no BP | true |
| Seção BP afetada | cap_07_personas + cap_14_gtm |
| Status | PENDENTE |

### IN-004 · Adjustment: produtos universais adaptáveis (não por segmento)

| Campo | Valor |
|---|---|
| Tipo | ADJUSTMENT |
| Sprint origem | S1.1 |
| Sprint destino | S1.3 e Sprint 3 (S3.1 BMC) |
| Descoberta | A fase Ideate convergiu para 4 gargalos universais que aparecem em múltiplos segmentos. Decisão D-004 formalizou: produtos são universais, varia o sistema integrado e o discurso. |
| Ação em Sprint 1.3 | Cap 11 deve apresentar cada produto como "universal" com seção "como se adapta por segmento". NÃO criar variações de produto por segmento. |
| Ação em Sprint 3 | Cap 12 BMC formaliza Customer Segments como 4 personas + 6 clusters de adaptação, mas mantém Value Propositions universais. |
| Impacto VVV | +0.03 (consolida tese de escalabilidade) |
| Incorporado no BP | true |
| Seção BP afetada | cap_11_produtos estrutura + cap_12_bmc |
| Status | PENDENTE |

---

## Sprint 1.2 → Sprint 1.3

_A ser preenchido após produção do Sprint 1.2._

## Sprint 1.3 → Sprint 2.1

_A ser preenchido após produção do Sprint 1.3._

---

## Template de insight (referência)

```yaml
insight_id: IN-NNN
sprint_origem: SX.X
sprint_destino: SY.Y
data: YYYY-MM-DD
tipo: ADJUSTMENT | CONFIRMATION | CONTRADICTION | NEW_DATA
descoberta: "..."
acao_em_sprint_destino: "..."
impacto_vvv: +0.NN | -0.NN | 0
incorporado_no_bp: true | false
secao_bp_afetada: cap_NN_nome
status: PENDENTE | INCORPORADO | DESCARTADO
```

## Princípios operacionais

1. **Append no momento da descoberta** — não esperar fim de sprint
2. **Consumir antes de começar próximo** — checklist start_of_sprint inclui ler este doc
3. **Incorporar no BP** — todo insight com `incorporado_no_bp: true` deve estar refletido no capítulo destino
4. **Transparência metodológica** — este doc é evidência de método iterativo (coerente com VVV)
