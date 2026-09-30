---
id: NEOGOV-V21-DECISIONS-LOG
filename: APENDICE-B-DECISIONS-LOG-v2.0.5.md
created_at: 2026-05-16T02:15:00Z
type: DECISIONS_LOG_FDCU
parent_session: NEOGOV-V21-WAVE1-W1.2-PATCH-PRICING-SCENARIOS-2026-05-16
supersedes: APENDICE-B-DECISIONS-LOG-v2.0.4.md
status: ACTIVE
mandato: M-003 (FDC-U mínimo 3 opções) · D-019 (BABOK permanente) · D-W1.2-002 · D-W1.2-003 · D-W1.2-004
tags: [decisions, fdcu, mandatos-neogov, audit-d001, cost-decomposition, pricing-scenarios]
---

# APÊNDICE B · DECISIONS LOG · v2.0.3

> Toda decisão estratégica registrada com FDC-U + rationale + opções rejeitadas + critério vencedor.

---

## Decisão D-EXEC-001 · Caminho de prosseguimento

**Score FDC-U**: 8.90 · **Vencedor**: Auditar D001 → Orq → Caps · ✅ EXECUTADA

---

## Decisão D-EXEC-002 · Estrutura Multi-Agente

**Score FDC-U**: 8.90 · **Vencedor**: B1 · 6 agentes especializados · ✅ EXECUTADA

---

## Decisão D-EXEC-003 · Prioridade Entregável Final

**Score FDC-U**: 8.05 · **Vencedor**: C4 · Tripé paralelo · ✅ EXECUTADA

---

## Decisão D-AUDIT-D001 · Auditoria Sprint 3.0.1 v3.0

**PMQS bruto**: 9.62 · **VVV**: 0.78 · **Veredicto**: 🟢 APROVADO PARCIALMENTE · ✅ EXECUTADA

---

## Decisão D-W1.1-001 · Auditoria Cap 02 VMV

**Score FDC-U**: 9.30 · **Vencedor**: Aceitar v2.1.4.3 · ✅ EXECUTADA

---

## Decisão D-W1.2-001 · Estrutura Cap 12 BMC

**Score FDC-U**: 9.50 · ✅ EXECUTADA

---

## Decisão D-W1.2-002 · Pricing Bottom-Up Cost-Plus + Otimização Matemática

**Score FDC-U**: 9.85 · **Vencedor**: D · Reescrita combinada (cost-plus + sanity-check análogo)
**Status**: ✅ APLICADA (Apêndice D + Cap 12 v2.1.5.2)

---

## Decisão D-W1.2-003-v2 · Cost Decomposition Expert por Produto × Cluster × Demanda

**Contexto**: Após Apêndice D produzido, usuário identificou falha crítica: "como calculou o custo? onde está custos de infra? por produto cálculo diferente · VVV expert ANTES de prosseguir · por produto e demanda de uso".

**Auto-auditoria adversarial v1.0.1 revelou 13 gaps confessos** (infra superficial · sem função matemática · compliance zero · etc).

**Opções enumeradas** (M-003):

- **A · Manter v1.0.1** (raso · gaps confessos)
- **B · Activity-Based Costing pleno + função matemática + cross-validation salários + multi-provider + compliance + funções por produto** (v2.0.1)
- **C · Patchear v1.0.1** com adições incrementais
- **D · Rewrite sem cross-validation** (intermediário)

**FDC-U Scoring**:

| Dimensão | Peso | A | **B (v2.0.1)** | C | D |
|---|:--:|:--:|:--:|:--:|:--:|
| Rigor ABC pleno | 0.20 | 5 | **10** | 7 | 8 |
| Função matemática f(volume_uso) | 0.15 | 3 | **10** | 5 | 7 |
| VVV expert ≥ 0.85 custos | 0.20 | 4 | **10** | 6 | 7 |
| Mandato usuário cumprido | 0.20 | 4 | **10** | 6 | 8 |
| Honestidade epistêmica RGO-5 | 0.10 | 6 | **10** | 7 | 8 |
| Reutilização Sprint 3.0.1 | 0.05 | 8 | 9 | 9 | 8 |
| Velocidade output | 0.05 | 10 | 6 | 8 | 7 |
| Auditabilidade reversa | 0.05 | 5 | **10** | 7 | 7 |
| **SCORE PONDERADO** | **1.00** | 4.95 | **🥇 9.70** | 6.40 | 7.55 |

**Vencedor**: **B · Apêndice E v2.0.1 expert · 9.70**

**Rationale**:
- 35+ lastros primários BR 2026 com URLs (vs 14 em v1.0.1)
- 15 atividades de infra mapeadas (vs 5 em v1.0.1)
- 6 providers cotados (vs 1 em v1.0.1)
- Salários cross-validated 3 fontes (Robert Half + Catho + Glassdoor)
- Compliance ISO 27001/SOC 2/LGPD modelado (R$ 47k→R$ 18k/mês escalado por wave)
- Função matemática TC(produto, volume, cluster) por cada um dos 6 produtos
- VVV expert custos = 0.86 (target ≥ 0.85 ATINGIDO)
- VVV WTP/k declarado 0.50 honestamente (RGO-5)

**Devil's Advocate aplicado**: 7 contras refutados §12 Apêndice E v2.0.1

**Output principal**: APENDICE-E-COST-DECOMPOSITION-v2.0.1.md (1.116 linhas)

**Impacto nos números**:
- CSC variável Wave 1 P75: R$ 72k → R$ 82k (+14% honesto vs v1.0.1 incompleto)
- Fixos: R$ 146k → R$ 153k (+5%, incluindo compliance + operacional)
- Profit P75: +R$ 29k → +R$ 12k (mais realista · v1.0.1 era otimista)
- CSC Alfa-F/E revelado real: R$ 28.570/mês (vs R$ 17.394 v1.0.1)
- CSC Beta Hospital Y1: R$ 25.460/mês (vs R$ 17.441 v1.0.1)

**Sub-débitos priorizados** (Wave 1 piloto):
1. D001-NOVO-7: WTP Van Westendorp por cluster (M+1)
2. D001-NOVO-8: Volume real tokens IA cluster (M+3)
3. D001-NOVO-1: Elasticidade k regressão (M+6)
4. D001-NOVO-6: Horímetro Simone/Gislênia P5 (M+3)
5. D001-NOVO-5: Validar P2 setup Tasy (M+6)
6. D001-NOVO-4: PoC vLLM Magalu BR (M+2)
7. D001-NOVO-3: LogNormal Wave 2 estatística (Wave 2)

**Status**: ✅ APLICADA · v2.0.1 produzida · aguarda validação usuário antes patch Cap 12

**Revisível**: SIM · trigger M+6 piloto Wave 1

---

## Decisão D-W1.2-004 · Pricing Model & Scenarios Paramétricos (Apêndice F)

**Contexto**: Após validação Apêndice E v2.0.1, usuário pediu: "preço final por produto+cluster · forma de cobrança (uso/plano) · função paramétrica break-even · ponto sucesso global empresa · 3 cenários reais Wave 1+ · manipulação posterior".

**Opções enumeradas** (M-003):

- **A · Pricing tabular sem função** (status quo v2.1.5.2)
- **B · Pricing + Função paramétrica básica**
- **C · Pricing + Função + 3 cenários + Manipulação posterior** (Apêndice F)
- **D · Calculator Vue.js app completo dashboards** (overkill Wave 1)

**FDC-U Scoring**:

| Dimensão | Peso | A | B | **C (Apêndice F)** | D |
|---|:--:|:--:|:--:|:--:|:--:|
| Atende mandato usuário completo | 0.25 | 2 | 6 | **10** | 9 |
| Manipulação posterior | 0.20 | 1 | 7 | **10** | 10 |
| Cenários realistas | 0.15 | 3 | 5 | **10** | 8 |
| Decisão executável | 0.15 | 4 | 7 | **10** | 8 |
| Velocidade output | 0.10 | 10 | 8 | 7 | 4 |
| Audit trail | 0.10 | 5 | 7 | **10** | 9 |
| Reutilização tripé docs | 0.05 | 5 | 7 | 9 | **10** |
| **SCORE PONDERADO** | **1.00** | 3.20 | 6.55 | **🥇 9.65** | 8.45 |

**Vencedor**: **C · Apêndice F · 9.65**

**Outputs entregues**:
1. **Pricing FINAL consolidado** 11 cluster·tiers com modelo de cobrança operacional
2. **Modelo de cobrança matriz** (subscription/usage/per seat/one-time/mix) por produto
3. **Estrutura de tiers** (NeoGov Municipal/Estadual-Federal/Saúde/Educação/Profissional + Add-ons)
4. **Função paramétrica Receita** R(t) = R_sub + R_usage + R_seat + R_onetime + R_addons
5. **Função paramétrica Custo** C(t) = CF(t) + CSC(t) (com growth scale + compliance por wave)
6. **Função Break-Even** N_BE = CF / Margem_por_cliente (formula fechada por mix)
7. **Função Sucesso Global** S(t) = (ARR ≥ 12M) AND (M_op ≥ 25%) AND (LTV/CAC ≥ 3) AND (VVV ≥ 0.92)
8. **3 cenários realistas Wave 1+**: 
   - A · Conservador P25 (12 clientes W1 · sucesso M60 marginal)
   - **B · Normal P50 (25 clientes W1 · sucesso M36 atingido)**
   - C · Otimista P75 (50 clientes W1 · sucesso M24 antecipado)
9. **Pseudocódigo Python e Vue.js** para implementação direta (calculator manipulável)
10. **Estrutura Excel/Google Sheets** com sheets de inputs/cenários/scenario-active/charts

**Devil's Advocate**: 6 contras refutados §13 Apêndice F

**Sub-débito** D001-NOVO-9 (calibrar LTV/CAC weighted via piloto Wave 1 · M+12)

**Status**: ✅ APLICADA · Apêndice F v1.0.1 produzido (~1.000 linhas)

**Insights consumidos**: IN-017 (subsídio cruzado) · IN-018 (CSC subestimado) · IN-019 (decomposição revela realidade) · IN-020 (todos tiers margem positiva)

---

## Decisões herdadas (registradas em sessões anteriores)

| ID | Decisão | Sessão | Status |
|---|---|---|---|
| D-ARC-001 | Arquitetura LLM Híbrida (Sabiá API + Llama local) | F2 Decisão | ✅ Aprovada |
| D-SAU-001 | Postergar entrada em Saúde | F2 Decisão | ✅ Aprovada (mas revisada · Beta entry Wave 1-2 cenário C) |
| D-010 | Inserir Sprint 3.0 modelagem precificação | S1.3 carry | ✅ Executado (S3.0.1 v3.0) |
| D-011 | VMV derivado e justificado (Cap 02) | S2.1 | ✅ Executada |
| D-012 | Retificação Cognitiva Missão (L1/L2 pattern) | S2.1 edição 2 | ✅ Executada |
| D-015 | Estimativa por Análogo com Lastro | POP v2.1.1.1 | ✅ Permanente |
| D-019 | BABOK BA-Orchestration permanente | POP v2.1.1.2 | ✅ Permanente |
| D-020 | CLIENT-FACING vs INTERNAL separation | POP v2.1.1.2 | ✅ Permanente |
| D-021 | PRE-ALWAYS checklist explícito | POP v2.1.1.2 | ✅ Permanente |

---

## Decisão D-W1.2-005 · Validação Adversarial Pricing sem Máscara (Apêndice G)

**Contexto**: Usuário pediu validação cenário vs Design Thinking por cluster · VVV sem viés · comparação pricing vs concorrência real · pagabilidade óbvia (Beta saúde real?).

**Opções**: A·Manter otimista · **B·Aplicar ajustes adversariais** · C·Reescrever zero · D·Adiar piloto

**FDC-U**: B vencedor **9.45** (honestidade epistêmica RGO-5 + defensável investidor + pagabilidade real)

**Outputs**: 3 gaps surreais identificados (Alfa-M Plus licitação · Beta hospital único · cenário C Wave 1) · pricing ajustado 16 tiers · cenários revisados −12% · VVV honesto 0.83→0.72

**Status**: ✅ APLICADA · Apêndice G v1.0.1 (785 linhas) · 6 Devil's Advocate

---

## Decisão D-W1.2-006 · DDD Architectural Cost Optimization (Apêndice H)

**Contexto**: Usuário pediu revisar custo · infra SOTA · guarda-chuva DDD · produto mais completo engloba todos · engenharia otimização.

**Opções**: A·Manter E sem DDD · **B·Apêndice H DDD 3 camadas** · C·Refazer E inline · D·H complementa sem substituir

**FDC-U**: B vencedor **9.55** (rigor arquitetural + identifica double-counting + otimização real + mandato arquiteto SOTA)

**Outputs**: 3 camadas DDD (Platform/Product/Service) · Beta Full = superset · stack SOTA 2026 · CSC Gamma/Épsilon revelado −47% a −84% · industrial scale validado

**Status**: ✅ APLICADA · Apêndice H v1.0.1 (693 linhas) · 6 Devil's Advocate

---

## Decisão D-W1.2-007 · ABC Proportional Cost Allocation (Apêndice I)

**Contexto**: Usuário identificou 2 falhas: (1) rateio uniforme CFA=CF/N injusto · (2) requisitos guarda-chuva validados? escola não usa AI-DPO.

**Opções**: A·Rateio uniforme · **B·ABC drivers por produto** · C·Rateio por receita · D·Sem ratear

**FDC-U**: B vencedor **9.65** (rigor arquitetural + atende mandato + justiça per cluster + SOTA SaaS 2026)

**Outputs**: L1A/L1B decomposição · matriz drivers (Gamma peso GPU=0 ✅) · CFA proporcional · margens reais 77-86% · capacity sizing Wave 1-5 · break-even honesto 34 clientes

**Status**: ✅ APLICADA · Apêndice I v1.0.1 (687 linhas) · 6 Devil's Advocate

---

## Decisão D-W1.2-008 · Consolidação Cap 12 BMC v2.1.5.3

**Contexto**: 6 apêndices produzidos · capítulos consumidores (13/15/18) precisam fonte única.

**Opções**: A·Manter v2.1.5.2 · **B·Patch incremental consolidado preservando aprovadas** · C·Reescrever Cap 12 zero · D·Apêndice consolidador separado

**FDC-U Scoring**:

| Dimensão | Peso | A | **B** | C | D |
|---|:--:|:--:|:--:|:--:|:--:|
| Fonte única consumidores | 0.25 | 3 | **10** | 9 | 7 |
| Preserva aprovado (AP-06) | 0.20 | 10 | **10** | 2 | 8 |
| Velocidade | 0.15 | 10 | **8** | 3 | 7 |
| Coerência narrativa | 0.15 | 6 | **9** | 7 | 6 |
| Auditabilidade | 0.15 | 5 | **10** | 8 | 9 |
| RGO-4 base estável | 0.10 | 4 | **10** | 6 | 7 |
| **SCORE** | **1.00** | 5.95 | **🥇 9.55** | 6.05 | 7.20 |

**Vencedor**: B · Patch incremental consolidado · **9.55**

**Outputs**: §12.7-TER pricing FINAL 16 tiers · §12.11-CONSOLIDADO DDD · §12.12-v3 cenários · §12.13-BIS função · §12.14-BIS ABC · §12.17 consumidores · PMQS final 7.73 ✅

**Status**: ✅ APLICADA · 12-bmc-v2.1.5.3.md (1.217 linhas) · seções aprovadas preservadas

---

## Decisão D-W1.2-009 · Nomenclatura Comercial DE-PARA (Apêndice J)

**Contexto**: Usuário identificou que nomes técnicos Alfa/Beta/Gamma/Épsilon · "Beta-Grande Full Bundle" · "Épsilon DPO 1 seat (P4 leve)" · "Y1/Y2+" são incompreensíveis para humanos/cliente/investidor. Pediu nomenclatura legível e explicada, primeiro decodificando quem é cada cluster.

**Opções**: A·Manter técnico · B·Substituir GLOBAL · **C·Duas camadas + Apêndice J ponte + híbrido client-facing** · D·Renomear clusters direto

**FDC-U**: C vencedor **9.65** (legibilidade humana + preserva metodologia AP-06 + D-020 compliance + auditabilidade DE-PARA)

**Outputs**:
- Apêndice J v1.0.1 · DE-PARA canônico (7 clusters decodificados · 16 tiers · 6 produtos · sufixos)
- Cap 12 §12.7-TER.2 patcheado formato híbrido (NeoGov Município Essencial [Alfa-M Pro])
- Nota tradução + ref Apêndice J nos Apêndices F/G/I
- Glossário: "Ano 1/Recorrente" · "licença" · "Full Bundle" · "P4 leve" explicados
- 2 camadas: análise (cluster preservado FDC-U/Sun Tzu) · comercial (nome legível)

**Decodificação canônica**:
- Alfa = Setor Público · Beta = Saúde · Gamma = Educação · Delta = Federações
- Épsilon = Profissional Liberal · Zeta = Empresarial · Omega = Hiper-regulado

**Status**: ✅ APLICADA · Apêndice J v1.0.1 · Cap 12 v2.1.5.4 · 4 Devil's Advocate · PMQS 9.28

---

## Estatísticas atualizadas (v2.0.5)

```yaml
total_decisoes_registradas: 19 (11 Wave 1 FDC-U + 1 audit + 7 herdadas)
total_fdcu_aplicados_wave_1: 11 (EXEC-001/002/003 + W1.1-001 + W1.2-002 a 009)
score_medio_decisoes_FDCU_wave_1: 9.35 (13 decisões)
threshold_aprovacao_minimo: 7.5 (good)
todas_decisoes_acima_threshold: SIM (mínima 8.05)
mandato_M_003_compliance: SIM (todas ≥ 3 opções)
devils_advocate_aplicado: SIM (cumulativo 42+ contras refutados)
correcoes_metodologicas_aplicadas: 5 (D-012 cognitiva · D-W1.2-002 pricing · D-W1.2-003-v2 custos · D-W1.2-006 DDD · D-W1.2-007 ABC)
artefatos_substantivos_wave_1: 7 (Apêndices D+E+F+G+H+I + Cap 12 v2.1.5.3)
total_linhas_tecnicas_wave_1: ~6.500
```

---

## Hash de continuidade

```
hash_continuidade: NEOGOV-V21-WAVE1-W1.2-NOMENCLATURA-COMERCIAL-v2.1.5.4-AWAIT-W1.3-2026-05-16
parent: NEOGOV-V21-WAVE1-W1.2-ABC-PROPORTIONAL-COMPLETE-AWAIT-W1.3-2026-05-16
proxima_acao: W1.3 Cap 13 VPC (com nomenclatura comercial Apêndice J)
```

---

## BRANCH RETIFICAÇÃO · Decisões D-W1.2-RETIF-001 a 004 (consolidado SESSION-STATE v2.0.8)

| ID | Decisão | Contexto | Score FDC-U | Doc |
|---|---|---|:--:|---|
| D-W1.2-RETIF-001 | DT TEST 5ª fase · validar preço novo ANTES de Cap 12/13 | Usuário detectou Cap 12/13 usavam preço velho (RGO-4) | 9.55 | Apêndice K |
| D-W1.2-RETIF-002 | Auditoria base lógica FATO/MÉTODO/LÓGICA + re-validação externa | Usuário pediu justificativa epistemológica | 9.40 | Apêndice L |
| D-W1.2-RETIF-003 | Agrupar(K2)→Cartórios(K1) · ordem topológica RGO-3 | Add cartórios + agrupamento business_segments | 9.50 | Apêndice M |
| D-W1.2-RETIF-004 | Auditoria hostil cartórios · 3 fabricações corrigidas FATO sem máscara | Usuário não confiava nos valores cartório | 9.70 | Apêndice N |

**Aprendizado-chave**: novo público = web_search das premissas factuais ANTES do DT TEST (não depois). Falha localizada cartórios reconhecida e corrigida; cadeia D-L permanece fiel (auditada Apêndice L).

**SSOT**: v1.0.1→v1.0.6 · auditado campo-a-campo · price.validated 100% sync · 3 _audit_flag CSC cartório (D-015).
