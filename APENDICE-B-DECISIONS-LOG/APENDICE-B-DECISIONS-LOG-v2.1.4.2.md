---
id: NEOGOV-V21-APENDICE-B-DECISIONS-LOG
filename: APENDICE-B-DECISIONS-LOG-v2.1.4.2.md
created_at: 2026-05-14
last_updated: 2026-05-15T01:30:00Z
type: DECISIONS_RATIONALE_LOG
status: ACTIVE
sprint: S2.1
edicao: 2
parent_doc: BUSINESS-PLAN-FINAL-v2.1
purpose: Registrar TODA decisão de produção com opções consideradas e rationale
update_rule: Append-only · cresce a cada decisão tomada
final_destination: Apêndice B do BP final (Word docx)
tags: [decisoes, rationale, governanca, dtp]
---

# Apêndice B · Log de Decisões e Rationale

## Métricas

- Decisões registradas: **12** (D-001 a D-012)
- Decisões herdadas: 7 (D-INH-001 a D-INH-007)
- Última atualização: 2026-05-15 Sprint 2.1 edição 2 (retificação cognitiva)

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

## Decisões Sprint 2.1

### D-011 · VMV derivado e justificado (não aspiracional poético)

| Campo | Valor |
|---|---|
| Sprint | 2.1 |
| Data | 2026-05-15 |
| Contexto | Como apresentar Visão, Missão e Valores do Cap 02 |
| Opção A | VMV padrão (frases curtas inspiracionais sem derivação) — REJEITADA (score 5.4) |
| Opção B | VMV derivado mostrando origem de cada elemento + operacionalização **ESCOLHIDA** (score 9.6) |
| Opção C | VMV minimalista (1 frase cada sem desenvolvimento) — REJEITADA (score 5.6) |
| Rationale | VMV genérico inspiracional perde valor estratégico. VMV derivado: (a) mostra coerência com Cap 04/07/11, (b) torna valores testáveis com tabelas "Como se manifesta · Como NÃO se manifesta", (c) consume IN-008 (categoria nova) explicitamente, (d) gera os 5 Princípios Operacionais §2.6 reutilizáveis em decisões cotidianas. |
| Diferencial metodológico | Tensão produtiva explícita entre valores (§2.5 final) — anti-padrão de valores corporativos "lindos mas vazios". |
| Impacto próximos sprints | Cap 12 BMC deriva Value Propositions dos 3 advérbios da Missão. Cap 14 GTM materializa Valor 4 (Acessibilidade Real) via tier diferenciado. Cap 16 Equipe deriva contratação dos Valores 2 e 5. |
| Revisível | NÃO |

### D-012 · Retificação Cognitiva da Missão por análise de marketing externo

| Campo | Valor |
|---|---|
| Sprint | 2.1 edição 2 |
| Data | 2026-05-15 |
| Contexto | Usuário (CEO/founder NeoGov) leu Missão v2.1.4.1 e identificou 2 problemas cognitivos: (a) "manufaturar knowledge" soa anti-ético / sub-valoriza esforço humano, (b) "IA + ICT" vende tecnologia, não benefício. Pediu retificação com adição de "produtividade + simplificação cumprimento legal". |
| Opção A | Manter Missão v2.1.4.1 e adicionar nota explicativa — REJEITADA (não resolve dissonância cognitiva) |
| Opção B | Reescrever Missão com proposta do usuário + auditar coerência downstream **ESCOLHIDA** |
| Opção C | Reescrita parcial só substituindo termos problemáticos — REJEITADA (perde oportunidade de retificar cognitivamente todo o Cap 02) |
| Rationale | Análise cognitiva por persona (5 audiências testadas) confirmou: nova Missão (a) identifica vilão claro = "complexidade legal", (b) entrega benefícios humanos = "produtividade + sem peso", (c) respeita profissional jurídico = "expertise legal", (d) posiciona tecnologia como meio (não fim) = "aplicação de tecnologia avançada". Métricas cognitivas melhoram para todas 4 personas + investidor. |
| Mudanças aplicadas | (1) Missão reescrita §2.4 + análise verbo a verbo · (2) §2.2 reformulado com 3 marcadores cognitivos · (3) Visão §2.3 ajustada para "compliance LGPD simplificado" + "segurança jurídica e produtividade" · (4) Valor 2 renomeado para "Expertise Jurídica como Ativo Estratégico" · (5) Valor 3 renomeado para "Engenharia Aplicada, Não Artesanato" · (6) Princípio 4 atenuado (IA aplica, não substitui) |
| Afirmação afetada | AF-046 marcada SUPERSEDED · AF-051 substituta criada |
| Insight emergente | IN-014 · "tradução cognitiva técnico→benefício" como padrão para TODO o BP |
| Impacto próximos sprints | Cap 13 VPC bloco Gain Creators usa benefícios da Missão. Cap 14 GTM padrão IN-014 para tom de campanha. Sprint 1 (Caps 04, 07, 11) **podem precisar de auditoria cognitiva** — registrar como débito D002. |
| Revisível | SIM (Missão pode ser refinada conforme feedback de campo) |

---

## Template de entrada de decisão (referência)

_Mantido inalterado — ver v2.1.1._
