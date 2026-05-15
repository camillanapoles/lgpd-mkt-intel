---
id: NEOGOV-V21-APENDICE-B-DECISIONS-LOG
filename: APENDICE-B-DECISIONS-LOG.md
created_at: 2026-05-14
last_updated: 2026-05-14T23:50:00Z
type: DECISIONS_RATIONALE_LOG
status: ACTIVE
parent_doc: BUSINESS-PLAN-FINAL-v2.1
purpose: Registrar TODA decisão de produção com opções consideradas e rationale
update_rule: Append-only · cresce a cada decisão tomada
final_destination: Apêndice B do BP final (Word docx)
tags: [decisoes, rationale, governanca, dtp]
---

# Apêndice B · Log de Decisões e Rationale

> Documento append-only que registra cada decisão tomada durante a produção do BP NeoGov v2.1. Permite ao leitor auditar **por que** cada escolha foi feita.

## Métricas

- Decisões registradas: **5** (Sprint 1.1)
- Decisões herdadas: 7 (D-INH-001 a D-INH-007)
- Decisões revisadas: 0
- Decisões refutadas: 0
- Última atualização: 2026-05-14 Sprint 1.1

## Decisões pré-existentes (herdadas do BP v2.0 — VVV=1.0)

| ID | Decisão | Fonte original |
|---|---|---|
| D-INH-001 | NeoGov como ICT privado | BP v2.0 §Sumário |
| D-INH-002 | 5 produtos (Plataforma + Data Discovery + Anonimização + AI-DPO + ETL) | BP v2.0 §2.2 |
| D-INH-003 | Educação Privada FDC-U 9.0 = Wave 2B paralela | BP v2.0 §4 |
| D-INH-004 | Wave 1 Setor Público = motor de caixa | BP v2.0 §6.2 |
| D-INH-005 | Saúde Privada condicional PoC ETL M4 | BP v2.0 §6.3 |
| D-INH-006 | Art. 75 IV Lei 14.133 = via única B2G | BP v2.0 §1 |
| D-INH-007 | INPI obrigatório antes de venda B2G | BP v2.0 §6 |

---

## Decisões de produção v2.1

### D-001 · Adoção IDEO 5 fases canônicas como framework Design Thinking

| Campo | Valor |
|---|---|
| Sprint | 1.1 |
| Data | 2026-05-14 |
| Contexto | Escolha do framework Design Thinking a usar como espinha dorsal do Capítulo 04 |
| Opção A | IDEO 5 fases (Empathize → Define → Ideate → Prototype → Test) **ESCOLHIDA** |
| Opção B | d.school 6 fases (com Discover prévio) — REJEITADA |
| Opção C | Double Diamond (Discover/Define/Develop/Deliver) — REJEITADA |
| Rationale | IDEO 5 fases é adotada em inst-lgpd.md (fonte canônica VVV=1.0). Coerência com fonte canônica + simplicidade. d.school adiciona fase Discover redundante com Empathize. Double Diamond é mais usado em design de produto puro, não em estratégia. |
| Impacto próximos sprints | Personas (Cap 07) seguem mesma fase Empathize. Produtos (Cap 11) seguem mesma fase Prototype. VPC (Cap 13) é refinamento da fase Define. |
| Revisível | NÃO — framework definido para todo o documento |

### D-002 · Tese central "industrial, não consultoria" formalizada como pivô

| Campo | Valor |
|---|---|
| Sprint | 1.1 |
| Data | 2026-05-14 |
| Contexto | Como apresentar a transição do modelo R$600k/12 meses para R$15-50k/4-8 semanas |
| Opção A | Apresentar como "evolução natural" — REJEITADA (subestima a mudança) |
| Opção B | Apresentar como **pivô estratégico explícito derivado da fase Ideate** **ESCOLHIDA** |
| Opção C | Apresentar apenas no capítulo de Solução (Cap 11) — REJEITADA (perde a justificativa metodológica) |
| Rationale | A transformação serviço → indústria é a tese central do plano. Apresentá-la no Cap 04 como output do método DT torna explícito que não é decisão arbitrária, é consequência da análise. |
| Impacto próximos sprints | Cap 11 retoma esta tese mostrando os 5 produtos como instrumentos do pivô. Cap 12 BMC formaliza o modelo de negócio industrial. |
| Revisível | NÃO |

### D-003 · Discurso comercial específico por persona (não unificado)

| Campo | Valor |
|---|---|
| Sprint | 1.1 |
| Data | 2026-05-14 |
| Contexto | Decidir se haveria um discurso comercial único ou 4 discursos específicos por persona |
| Opção A | Discurso unificado tipo "compliance LGPD via IA" — REJEITADA |
| Opção B | 4 discursos específicos derivados dos 4 POVs **ESCOLHIDA** |
| Rationale | A fase Define revelou insights surpreendentes diferentes por persona: procurador municipal teme improbidade (não multa), CIO estadual valoriza LAI×LGPD (não compliance geral), diretor de saúde busca integração (não outro sistema), mantenedor escolar busca self-service (não consultoria). Unificar destrói o valor de cada insight. |
| Impacto próximos sprints | Cap 07 detalha cada persona com discurso próprio. Cap 13 VPC formaliza pain relievers específicos. Cap 14 GTM tem canais específicos por persona. |
| Revisível | NÃO — base de toda a estratégia comercial |

### D-004 · Produtos universais adaptáveis (não produtos por segmento)

| Campo | Valor |
|---|---|
| Sprint | 1.1 |
| Data | 2026-05-14 |
| Contexto | Decidir estrutura do portfolio: produtos diferentes por segmento OU produtos universais com adaptação |
| Opção A | Produtos diferentes por segmento (1 produto LGPD-Saúde, 1 LGPD-Edu, etc.) — REJEITADA |
| Opção B | Produtos universais que se adaptam ao sistema do cliente **ESCOLHIDA** |
| Rationale | A fase Empathize descobriu que a estrutura da dor é a mesma em 4 segmentos — variando apenas os sistemas integrados. Produtos universais aproveitam essa estrutura para escala. Produtos por segmento criariam 4 times de desenvolvimento. |
| Impacto próximos sprints | Cap 11 apresenta 5 produtos universais com adaptação por sistema integrado. Cap 14 GTM mostra mesmo produto vendido para 4 personas com discurso diferente. |
| Revisível | NÃO — define arquitetura do portfolio |

### D-005 · Capítulo 04 abre como pedra angular (não apêndice metodológico)

| Campo | Valor |
|---|---|
| Sprint | 1.1 |
| Data | 2026-05-14 |
| Contexto | Posicionamento do Capítulo 04 dentro do BP — abertura ou apêndice metodológico |
| Opção A | Apêndice metodológico ao final do BP — REJEITADA |
| Opção B | Capítulo 04 logo após Sumário Executivo, antes da Análise de Mercado **ESCOLHIDA** |
| Opção C | Diluído em cada capítulo — REJEITADA |
| Rationale | O leitor precisa entender PRIMEIRO como as conclusões foram derivadas, para então aceitar as conclusões. Posicionar DT como Cap 04 torna o restante do BP "consequência natural" do método. Apêndice perde força. |
| Impacto próximos sprints | Cap 07/11/12/13 referenciam Cap 04 explicitamente. Sumário Executivo (Cap 03) menciona DT como método de governança contínua. |
| Revisível | NÃO |

---

## Template de entrada de decisão (referência)

```yaml
decisao_id: D-NNN
sprint: SX.X
data: YYYY-MM-DD
contexto: "..."
opcoes_consideradas:
  - opcao_A: "..." [escolhida | rejeitada · motivo]
  - opcao_B: "..." [escolhida | rejeitada · motivo]
escolha: "..."
rationale: "..."
fonte_apoio: "..."
impacto_proximos_sprints: "..."
revisivel: true | false
```
