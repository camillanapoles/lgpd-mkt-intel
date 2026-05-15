---
id: NEOGOV-V21-APENDICE-C-INSIGHTS-CARRY
filename: APENDICE-C-INSIGHTS-CARRY-v2.1.4.2.md
created_at: 2026-05-14
last_updated: 2026-05-15T01:30:00Z
type: INSIGHTS_INTER_SPRINT_LOG
status: ACTIVE
sprint: S2.1
edicao: 2
parent_doc: BUSINESS-PLAN-FINAL-v2.1
purpose: Descobertas em Sprint N que ajustam Sprint N+1 · garantia de continuidade
update_rule: Append no Sprint origem · consumido no Sprint destino · sempre mantido
final_destination: Apêndice C do BP final (nota de transparência metodológica)
tags: [insights, continuidade, inter-sprint, aprendizado]
---

# Apêndice C · Insights Inter-Sprint (Carry-Over)

## Métricas

- Insights registrados: **14** (13 anteriores + 1 novo IN-014 S2.1 ed.2)
- Insights consumidos: 7 (IN-001 a IN-006, IN-008)
- Insights pendentes: 7 (IN-007, IN-009, IN-010, IN-011, IN-012, IN-013, IN-014)
- Última atualização: 2026-05-15 Sprint 2.1 edição 2 (retificação cognitiva)

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

### IN-008 · NeoGov vende KNOWLEDGE MANUFATURADO — **INCORPORADO**

| Campo | Valor |
|---|---|
| Status | ✅ INCORPORADO em Cap 02 §2.2 (categoria nova) + §2.4 verbo "Manufaturar" |
| Como foi incorporado | §2.2 mapeia 4-vértice (categoria nova) entre SaaS · Consultoria · Plataforma · NeoGov. §2.4 justifica "manufaturar" como categoria distintiva. Gerou D-011. |
| Impacto VVV | +0.03 (categoria nova como diferencial = barreira competitiva) |
| Sprint origem | S1.3 |
| Sprint destino | S2.1 (cumprido) |

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

### IN-011 · CRITICAL · Pricing top-down é insuficiente · S3.0 obrigatório antes do BMC

| Campo | Valor |
|---|---|
| Tipo | CONTRADICTION (auto-identificado pós-Gate) |
| Sprint origem | S1.3 edição 2 (pós-Gate Sprint 1) |
| Sprint destino | **S3.0 NOVO** (antes do Cap 12 BMC) |
| Severidade | CRITICAL |
| Descoberta | Pricing apresentado no Cap 11 §11.4-11.8 tem VVV 0.65 — inferência top-down baseada em Confidata. Insuficiente como input para BMC Revenue Streams + Cost Structure. Usuário identificou gap explícito pós-Gate exigindo modelagem bottom-up assertiva. |
| Ação em S3.0 | (a) Modelagem custo bottom-up por produto (infra IA, cloud, suporte, CAC). (b) Diferenciar por modelo de cobrança (assinatura vs API vs usage). (c) Margem alvo por produto/persona. (d) Unit economics (LTV/CAC/Payback). (e) Pesquisa concorrentes (GAP05 Be Compliance + Safetyfyi). (f) Retificar Cap 11 §pricing com valores assertivos VVV 0.85+. |
| Entregável | `content/15-financeiro-base.md` + `APENDICE-D-MODELO-CUSTO.xlsx` + retificação Cap 11 |
| Impacto VVV | +0.20 esperado (0.65 → 0.85+) |
| Incorporado no BP | true (sprint dedicado) |
| Seção BP afetada | cap_11_produtos §pricing (retificação) · cap_12_bmc inputs · cap_14_gtm inputs · cap_15_financeiro |
| Bloqueio | Sprint 3.1 (Cap 12 BMC) NÃO pode iniciar sem Sprint 3.0 concluído |
| Status | PENDENTE · documento detalhado em `continuity/DEBITO-D001-PRICING-FRAMEWORK-v2.1.3.1.md` |
| Decisão associada | D-010 (registrada em APENDICE-B) |

---

## Sprint 2.1 → Sprint 2.2 / Sprint 4 (NOVOS · Cap 02 → Caps 01 e 16)

### IN-012 · 5 Princípios Operacionais derivados (regras de decisão reutilizáveis)

| Campo | Valor |
|---|---|
| Tipo | NEW_DATA |
| Sprint origem | S2.1 |
| Sprint destino | S4.1 (Cap 16 Equipe e Governança) |
| Descoberta | A produção do Cap 02 §2.6 gerou 5 Princípios Operacionais que são regras de decisão recorrentes (ouvir/rejeitar mercado, registrar/publicar INPI, customizar/padronizar, contratar/treinar agente, entrar/esperar segmento). Esses princípios são input direto para governança e processos. |
| Ação em S4.1 | Cap 16 Equipe e Governança traduz cada princípio em política operacional: matriz de decisão, RACI, OKRs. |
| Impacto VVV | 0 |
| Incorporado no BP | true |
| Seção BP afetada | cap_16_equipe_governanca |
| Status | PENDENTE |

### IN-013 · Tensão produtiva entre valores exige liderança mediadora

| Campo | Valor |
|---|---|
| Tipo | NEW_DATA |
| Sprint origem | S2.1 |
| Sprint destino | S4.1 (Cap 16) + S5.3 (Cap 03 Sumário) |
| Descoberta | Cap 02 §2.5 final identifica que os 5 Valores operam em tensão produtiva (Industrial vs Acessibilidade, Honestidade vs Knowledge-Ativo, Auditabilidade vs Industrial). Isso implica que a liderança da NeoGov tem uma função específica: **mediar essas tensões**, não fingir que não existem. |
| Ação em S4.1 | Cap 16 descreve papel do CEO/comitê executivo como "mediador de tensão entre valores" — não apenas executivo operacional. |
| Ação em S5.3 | Cap 03 Sumário Executivo destaca essa diferenciação metodológica como vantagem competitiva (concorrentes têm "valores paralelos lindos"). |
| Impacto VVV | 0 |
| Incorporado no BP | true |
| Seção BP afetada | cap_16_equipe_governanca · cap_03_sumario |
| Status | PENDENTE |

---

## Sprint 2.1 edição 2 — Insight de retificação cognitiva (NOVO)

### IN-014 · "Tradução cognitiva técnico → benefício" como padrão para TODO o BP

| Campo | Valor |
|---|---|
| Tipo | NEW_DATA · ADJUSTMENT META |
| Sprint origem | S2.1 edição 2 (retificação D-012) |
| Sprint destino | **AUDITORIA RETROATIVA** (Caps 04, 07, 11) + **TODOS os capítulos futuros** |
| Severidade | ALTA · padrão metodológico transversal |
| Descoberta | A retificação da Missão D-012 não foi um ajuste isolado — revelou um **padrão cognitivo aplicável a todo o BP**: para audiência externa (cliente, investidor, parceiro), termos técnicos como "manufaturar knowledge", "IA + ICT", "ICT", "knowledge proprietário" precisam ser TRADUZIDOS em benefícios humanos sentidos. Toda menção técnica deve ter pareamento com: (a) vilão combatido, (b) benefício entregue, (c) respeito ao profissional humano envolvido. |
| Padrão de aplicação | "[termo técnico] → [benefício humano] sem [vilão concreto]" |
| Exemplos retificados (Cap 02) | "manufaturar knowledge" → "simplificar cumprimento da LGPD através de expertise legal" · "IA + ICT" → "aplicação de tecnologia avançada" |
| Ação retroativa | Auditar Caps 04, 07, 11 para termos técnicos sem tradução cognitiva. Registrar débito D002 se necessário. |
| Ação prospectiva | TODOS os capítulos futuros (12-18) aplicam IN-014: cada termo técnico recebe tradução cognitiva imediata + benefício humano pareado. |
| Impacto VVV | Neutro · mas eleva PMQS bruto por melhor CC (Clareza Cristalina) e RA (Relevância Absoluta) |
| Incorporado no BP | parcial (Cap 02 retificado) · pendente nos demais |
| Seção BP afetada | TODOS os capítulos (transversal) |
| Status | PARCIAL · auditoria Caps 04/07/11 pendente como débito D002 inferido |
| Decisão associada | D-012 |
| Débito gerado | **D002 · Auditoria Cognitiva Retroativa Caps 04, 07, 11** (criar continuity/DEBITO-D002-COGNITIVO.md) |

---

## Sprint 2 → Sprint 3 (será preenchido)

## Sprint 3 → Sprint 4 (será preenchido)

---

## Princípios operacionais (mantidos)

1. **Append no momento da descoberta** — não esperar fim de sprint
2. **Consumir antes de começar próximo** — checklist start_of_sprint inclui ler este doc
3. **Incorporar no BP** — todo insight com `incorporado_no_bp: true` deve estar refletido no capítulo destino
4. **Transparência metodológica** — este doc é evidência de método iterativo (coerente com VVV)
