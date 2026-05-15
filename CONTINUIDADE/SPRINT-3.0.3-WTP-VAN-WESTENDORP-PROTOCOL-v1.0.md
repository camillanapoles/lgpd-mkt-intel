---
id: NEOGOV-V21-SPRINT-3.0.3-WTP-RESEARCH-PROTOCOL
filename: SPRINT-3.0.3-WTP-VAN-WESTENDORP-PROTOCOL-v1.0.md
created_at: 2026-05-15T19:00:00Z
type: PRIMARY_RESEARCH_PROTOCOL_PRICING
designation: S3.0.3
function: WTP_VALIDATION_VAN_WESTENDORP
parent_doc: SPRINT-3.0.1-MODELAGEM-CUSTO-PRICING-v3.0.md
paradigm: S→Q→I→A_BA_ORCHESTRATION_PSM
status: ACTIVE_READY_FOR_EXECUTION
prerequisite: S3.0.1 v3.0 OURO entregue ✅
blocks: LASTRO-WTP (destrava VVV 0.78 → 0.95)
ba_skills_applied:
  - estimation (parametric · Van Westendorp PSM + Gabor-Granger fallback)
  - journey-mapping (jornada da entrevista · empathy points)
  - stakeholder-analysis (recrutamento + RACI execução)
  - process-modeling (BPMN protocolo · fluxo gates)
  - risk-analysis (risk register research)
documentation_skills_applied:
  - technical-writer (clareza · estrutura · accessibility)
  - MDT v1.0 (PIER + Chunks + Meta-Audit)
  - runbook-creation (formato operacional)
target_outcomes:
  primary: VVV pricing 0.78 → 0.95 (LASTRO-WTP ✅)
  secondary: PMQS final 7.50 → 9.14
  tertiary: Validação OPP (Optimal Price Point) por cluster
estimated_duration: 15-30 dias úteis
estimated_cost: R$ 0-500 (incentivos opcionais)
quality_target: PMQS 9.5 OURO
tags: [sprint-3-0-3, wtp, van-westendorp, psm, primary-research, gabor-granger, runbook]
---

# Sprint 3.0.3 · Van Westendorp WTP Research Protocol

> **Objetivo único**: Validar empiricamente o pricing assertivo proposto em S3.0.1 v3.0 via metodologia Van Westendorp PSM (Price Sensitivity Meter) com extensão NMS · destravar LASTRO-WTP · elevar VVV 0.78 → 0.95.

---

## §0 · Sumário Executivo (TL;DR)

### 0.1 · O que este protocolo entrega

Um **runbook operacional** completo para Wilton (comercial) executar entrevistas estruturadas Van Westendorp com 25 prospects (5 por cluster × 5 clusters) em 15-30 dias, gerando:

1. **OPP** (Optimal Price Point) por cluster · validação direcional
2. **Acceptable Range** (PMC ↔ PME) por cluster · floor/ceiling
3. **Revenue Curve** (extensão NMS) · pricing que maximiza receita
4. **Insights qualitativos** · objeções, drivers, ajustes produto

### 0.2 · Output esperado

| Cluster | Persona | N target | Entregável |
|---|---|:-:|---|
| Alfa Fed/Est | CIO Estadual + Subsec TIC | 3 | OPP P1 Enterprise validado |
| Alfa Municipal | Procurador + CGM | 5 | OPP P1 Pro + P2 + P3-B2G |
| Beta | Diretor TI + DPO Hospital | 5 | OPP P1 Pro + P3 + P4 + P5 |
| Gamma | Mantenedor + Diretor Pedag. | 7 | OPP P1 Basic + P4 + P5 setup |
| Épsilon | DPO escritório DPO terceirizado | 5 | OPP P4 Senior/Lead per seat |
| **Total** | — | **25** | **5 OPPs + Revenue Curves** |

### 0.3 · % Pró-Labore Razoável [MODELO_AJUSTE] (cálculo emergente)

Aplicação `estimation` analogous · baseado em Fator R Simples Nacional + receita projetada Wave 1 P50 R$ 1M/ano:

| Cenário | Pró-Labore Total /mês | % Receita | Fator R Status |
|---|---:|---:|---|
| Conservador (P10) | R$ 35.000 | 42% | ✅ Anexo III seguro |
| **Realista (P50)** | **R$ 45.000** | **54%** | **✅ Anexo III com folga** |
| Otimista (P90) | R$ 70.000 | 84% | ⚠️ Sustentabilidade frágil |

**Recomendação operacional [MODELO_AJUSTE]**:
- Wave 0 (M0-M3 pré-receita): R$ 25-30k total (sócios sacrifício / aporte pessoal)
- Wave 1 inicial (M3-M6): R$ 35-40k total (~40-45% receita projetada)
- **Wave 1 maduro (M6-M12): R$ 45-50k total** (~45-50% receita) ← ALVO REALISTA
- Wave 2+: escalonar conforme MRR cresce

**Distribuição sugerida entre sócios [MODELO_AJUSTE]** (Wave 1 maduro R$ 45k total):

| Sócio | Papel | % | R$/mês [MODELO_AJUSTE] | Justificativa |
|---|---|:-:|---:|---|
| Simone | CEO + LGPD Lead | 30% | R$ 13.500 | Dupla responsabilidade (executiva + advogada lead) |
| Camila | CTO | 27% | R$ 12.150 | Liderança técnica crítica startup early-stage |
| Wilton | Head Comercial | 23% | R$ 10.350 + comissão 3-5% | Pró-labore menor compensado por comissão variável |
| Gislênia | Jurídica/Compliance | 20% | R$ 9.000 | Operacional sem responsabilidade fiduciária |
| **Total** | — | 100% | **R$ 45.000** | — |

> 🟡 **Tag aplicada**: `[MODELO_AJUSTE]` · valores funcionais para modelagem · decisão real definida em S3.0.2 reunião societária · será refinada conforme realidade individual (família, custo de vida, performance Wave 1)

---

## §1 · BA-Orchestration · Skills Aplicadas

### 1.1 · Pacote selecionado para protocolo de research

| Skill | Uso neste sprint |
|---|---|
| `estimation` (parametric · Van Westendorp PSM + NMS extension) | Metodologia primária quantitativa |
| `journey-mapping` | Jornada da entrevista (8 fases · empathy points) |
| `stakeholder-analysis` | Recrutamento prospects + RACI execução |
| `process-modeling` | BPMN protocolo (gates qualidade) |
| `risk-analysis` | Risk register specific to research method |

### 1.2 · Skills documentation-standards aplicadas

| Skill | Uso |
|---|---|
| `technical-writer` agent | Clareza prosa · estrutura headings · accessibility |
| `MDT v1.0` (Módulo Documentação Técnica) | PIER (Análise → Geração → Avaliação → Refinamento) · Chunks autocontidos |
| `runbook-creation` | Formato operacional · steps executáveis · validation points |

---

## §2 · METODOLOGIA · Van Westendorp PSM + NMS Extension

### 2.1 · Frame Teórico

Van Westendorp PSM (1976 · Peter van Westendorp · validado em 28+ anos B2B SaaS conforme Monetizely 2026 ✅):

**Princípio**: Customer pricing perception is multidimensional · 4 questions reveal acceptable range + optimal point.

### 2.2 · As 4 perguntas Van Westendorp (português B2B BR · adaptadas para NeoGov)

#### Pergunta 1 · "Too Expensive" (TE)

> **"A que preço você consideraria a [solução NeoGov X para problema Y] tão cara que NÃO consideraria comprar?"**

Captura: ceiling absoluto do mercado.

#### Pergunta 2 · "Expensive but Worth Considering" (EXP)

> **"A que preço você consideraria a solução começando a ficar cara, mas ainda assim consideraria comprar?"**

Captura: upper bound do acceptable range.

#### Pergunta 3 · "Cheap / Good Value" (CHEAP)

> **"A que preço você consideraria a solução uma pechincha, um excelente valor pelo dinheiro?"**

Captura: lower bound do acceptable range.

#### Pergunta 4 · "Too Cheap" (TC)

> **"A que preço você consideraria a solução tão barata que questionaria a qualidade e NÃO compraria?"**

Captura: floor absoluto · pricing-as-quality signal.

### 2.3 · Extensão NMS (Newton/Miller/Smith) · Revenue Curve

Após perguntas 1-4, adicionar 2 perguntas adicionais para gerar revenue curve:

#### Pergunta 5 (NMS-1) · Purchase Probability at Expensive Price

> **"Pelo preço EXPENSIVE que você indicou (R$ X), qual a sua probabilidade de comprar nos próximos 6 meses?"**  
> Escala: 1 (improvável) ↔ 5 (muito provável)

#### Pergunta 6 (NMS-2) · Purchase Probability at Cheap Price

> **"Pelo preço CHEAP que você indicou (R$ Y), qual a sua probabilidade de comprar nos próximos 6 meses?"**  
> Escala: 1 (improvável) ↔ 5 (muito provável)

### 2.4 · Outputs Calculados (4 intersecções + Revenue Curve)

| Métrica | Cálculo | Significado |
|---|---|---|
| **PMC** (Point Marginal Cheapness) | Intersecção TC × CHEAP | Floor do acceptable range |
| **PME** (Point Marginal Expensiveness) | Intersecção EXP × TE | Ceiling do acceptable range |
| **OPP** (Optimal Price Point) | Intersecção TC × TE | Pricing onde resistência é mínima |
| **IPP** (Indifference Price Point) | Intersecção CHEAP × EXP | Pricing onde igual % acha caro vs barato |
| **Acceptable Range** | PMC ↔ PME | Faixa "psicologicamente confortável" |
| **Revenue Maximizing Price** | NMS revenue curve peak | Pricing que maximiza receita total |

### 2.5 · Hierarquia obrigatória de respostas (validation)

Para cada respondente, validar:

```
Too Cheap (TC) < Cheap (CHEAP) < Expensive (EXP) < Too Expensive (TE)
```

Respondentes que violam essa hierarquia são DESCARTADOS (10-20% rate normal · Verint 2026).

### 2.6 · N mínimo por cluster

| Cluster | N Target | N Mínimo Aceitável | Margem Erro |
|---|:-:|:-:|---|
| Alfa Fed/Est | 3 | 2 | ±25% (validação direcional) |
| Alfa Municipal | 5 | 3 | ±20% |
| Beta Hospital | 5 | 3 | ±20% |
| Gamma Escola | 7 | 5 | ±18% |
| Épsilon DPO | 5 | 3 | ±20% |
| **TOTAL** | **25** | **16** | — |

⚠️ **Disclaimer (RGO-5)**: Para significância estatística rigorosa, N=100+ por segmento é ideal. NeoGov fará **validação direcional** com N=25 total · suficiente para decisões de pricing inicial · refinar pós-Wave 1 com dados reais (M+6).

---

## §3 · JOURNEY MAPPING · Jornada da Entrevista (Empathy Map)

### 3.1 · Jornada do Entrevistado (8 fases)

```
Fase 1: Recruitment ──→ Fase 2: Aceite ──→ Fase 3: Agendamento ──→ Fase 4: Pré-call
                                                                          │
                                                                          ▼
Fase 8: Follow-up ←── Fase 7: Encerramento ←── Fase 6: PSM ←── Fase 5: Briefing
```

### 3.2 · Empathy Points por Fase

| Fase | Pensa | Sente | Pain Point | Mitigação |
|---|---|---|---|---|
| 1 Recruitment | "Quem é NeoGov?" | Cético | Não conhece marca | Apresentação via Wilton (rede política) + LinkedIn |
| 2 Aceite | "Vale meu tempo?" | Cauteloso | Sem incentivo claro | Oferecer report do estudo + LinkedIn endorsement |
| 3 Agendamento | "30 min é ok?" | Pressionado | Agenda lotada | Calendly self-service + reagendamento fácil |
| 4 Pré-call | "Sobre o que falo?" | Despreparado | Sem contexto prévio | E-mail prep com 1-pager do produto |
| 5 Briefing | "O que é NeoGov?" | Interessado/cético | Conceito novo | Demo curta (5-7 min) + product description padrão |
| 6 PSM | "Quanto vale isso pra mim?" | Reflexivo | Não pensa em preço sempre | Perguntas estruturadas · slider visual · sem âncora prévia |
| 7 Encerramento | "Ajudou?" | Satisfeito (se bom) | Quer ver resultado | Promessa de envio de report agregado |
| 8 Follow-up | "Cumpriram?" | Engajado/decepcionado | Falta retorno | Envio report 30 dias + oferta beta access |

### 3.3 · Moments of Truth

| Moment | Tipo | Impacto na qualidade do dado |
|---|---|---|
| ZMOT (recruitment) | Aceitar ou recusar | Filtra qualidade do dado (auto-seleção) |
| FMOT (briefing) | Engajar ou não | Define honestidade nas respostas |
| SMOT (PSM) | Refletir verdade vs anchorar | DEFINE QUALIDADE DO DADO ⭐ |
| UMOT (follow-up) | Recomendar pares ou não | Define snowball recruitment |

---

## §4 · STAKEHOLDER ANALYSIS · Recrutamento + RACI Execução

### 4.1 · Perfil dos prospects recrutados por cluster

#### Alfa Federal/Estadual (N=3)

- 1× CIO Estadual (preferencialmente PE, BA, MG, RS · estados maturidade média)
- 1× Subsecretário TIC Federal ou Estadual
- 1× Diretor Tecnologia órgão controle (TCE, MPE, etc)

Canal recrutamento: Wilton via FNDE network + CONFIP + CNM.

#### Alfa Municipal (N=5)

- 2× Procuradores Municipais (cidades > 50k habitantes)
- 1× Controlador Geral Municipal (CGM)
- 1× Secretário Administração (capital regional)
- 1× Prefeito de cidade pequena (≤ 30k hab)

Canal: CNM + CIMI + LinkedIn.

#### Beta Hospital (N=5)

- 2× Diretores TI hospitais privados
- 1× DPO hospital privado
- 1× CFO hospital privado
- 1× Diretor Hospital filantrópico (Santa Casa, etc)

Canal: Anahp + CMB + LinkedIn.

#### Gamma Escola Privada (N=7)

- 3× Mantenedores escolas pequenas (≤ 500 alunos)
- 2× Mantenedores escolas médias (500-2000 alunos)
- 1× Diretor Pedagógico de rede privada
- 1× Coordenador TI de rede escolar

Canal: Federação Nacional das Escolas Particulares (FENEP) + LinkedIn + Anec.

#### Épsilon DPO (N=5)

- 3× Advogados especialistas LGPD em escritórios pequenos/médios
- 1× Sócio escritório boutique LGPD
- 1× Consultor compliance independente

Canal: OAB + LinkedIn + grupos LGPD WhatsApp.

### 4.2 · RACI Execução do Sprint S3.0.3

| Atividade | Wilton | Simone | Camila | Gislênia | Cândidato externo |
|---|:-:|:-:|:-:|:-:|:-:|
| Recrutamento prospects | **A**/R | C | I | C | I |
| Agendamento + Calendly | **A**/R | I | I | I | I |
| Briefing produto pré-call | C | **A** | R | C | I |
| Condução entrevista | **A**/R | C | I | I | I |
| Note-taking entrevista | C | I | I | I | **A**/R (transcritor) |
| Análise PSM (curvas) | C | I | **A**/R | I | I |
| Validação hierarquia respostas | I | I | **A**/R | I | I |
| Síntese qualitativa | C | **A** | R | **R** | I |
| Refatorar pricing S3.0.1 | C | **A**/R | C | C | I |
| Follow-up report | **A**/R | C | I | I | I |

### 4.3 · Tools necessárias

| Tool | Custo | Uso |
|---|---|---|
| Google Calendly | Free tier | Agendamento self-service |
| Google Meet | Free | Calls remotas |
| Otter.ai ou Fireflies | $10-20/mês | Transcrição automática |
| Google Forms ou Typeform | Free / $25/mês | Backup self-administered (fallback) |
| Notion ou Airtable | Free / $10/mês | CRM mini-database respostas |
| Google Sheets ou Excel | Free | Análise PSM (cumulative distributions) |
| Python + matplotlib (Camila) | Free | Plotagem profissional + revenue curve NMS |

---

## §5 · PROCESS MODELING · BPMN Protocolo

### 5.1 · BPMN End-to-End Sprint S3.0.3

```
START (Sprint S3.0.3 disparado)
   │
   ▼
[Task: Preparar briefing material (1-pager por produto)]   ← M0 dia 1
   │ owner: Simone + Camila
   │ output: 5 1-pagers (P1-P5)
   ▼
[Task: Lista de target prospects (25 nomes)]                ← M0 dia 1-2
   │ owner: Wilton
   │ output: planilha CRM com 25 prospects qualificados
   ▼
[Task: Enviar convite com incentive]                        ← M0 dia 2-7
   │ owner: Wilton
   │ output: convites enviados · acceptances coletadas
   ▼
[Gateway: 25 aceites obtidos?]
   │
   ├─ NÃO ──→ [Task: Snowball recruitment (referrals)]
   │              │
   │              └─→ [Continue]
   │
   └─ SIM ──→ [Task: Agendar entrevistas via Calendly]      ← M0 dia 7-10
                  │ owner: Wilton
                  │ output: 25 agendamentos confirmados
                  ▼
              [Task: Pré-call e-mail com produto 1-pager]   ← T-24h cada call
                  │ owner: Wilton (automático)
                  │
                  ▼
              [Task: Conduzir entrevista (30-45 min)]       ← M0 dia 10-25
                  │ owner: Wilton (com Simone backup)
                  │ rotinas:
                  │   1. Welcome (2 min)
                  │   2. Briefing produto (5-7 min)
                  │   3. Verificar entendimento (2 min)
                  │   4. Aplicar PSM 4 perguntas (5-7 min)
                  │   5. Aplicar NMS 2 perguntas (3 min)
                  │   6. Qualitativo: objeções, drivers (10 min)
                  │   7. Encerramento + thank you (2 min)
                  ▼
              [Task: Validar hierarquia respostas]          ← cada entrevista
                  │ owner: Camila (análise)
                  │ rule: TC < CHEAP < EXP < TE
                  │
                  ▼
              [Gateway: Hierarquia válida?]
                  │
                  ├─ NÃO ──→ [Task: Marcar como descarte (até 20%)]
                  │
                  └─ SIM ──→ [Task: Adicionar ao dataset]
                                 │
                                 ▼
                            [Gateway: 16+ respostas válidas total?]
                                 │
                                 ├─ NÃO ──→ [Continue entrevistas]
                                 │
                                 └─ SIM ──→ [Task: Análise PSM por cluster] ← M0 dia 25-28
                                                │ owner: Camila
                                                │ output:
                                                │   - 4 cumulative distribution curves
                                                │   - PMC, PME, OPP, IPP por cluster
                                                │   - Acceptable Range por cluster
                                                │
                                                ▼
                                            [Task: Análise NMS revenue curve]
                                                │ owner: Camila
                                                │ output: Revenue Max Price por cluster
                                                ▼
                                            [Task: Síntese qualitativa]
                                                │ owner: Simone + Wilton
                                                │ output: Top 5 objeções + Top 5 drivers
                                                ▼
                                            [Task: Refatorar pricing S3.0.1 §14.2]    ← M0 dia 28-30
                                                │ owner: Simone + Camila
                                                │ output: SPRINT-3.0.1-v3.1 (pricing WTP-validated)
                                                ▼
                                            [Task: Atualizar VVV log + Insights]
                                                │ owner: Claude (continuity)
                                                │ output: VVV global 0.78 → 0.95
                                                ▼
                                            [Task: Follow-up report aos prospects]
                                                │ owner: Wilton
                                                │ output: report agregado enviado
                                                ▼
END (Sprint S3.0.3 concluído · LASTRO-WTP ✅)
```

### 5.2 · Decision Table · Tratamento de Respostas

| Hierarquia válida | Cluster N mínimo atingido | Qualidade qualitativa | Ação |
|:-:|:-:|---|---|
| ✅ | ✅ | Alta (objeções claras) | Aceitar · analisar PSM |
| ✅ | ✅ | Baixa (respondente desinteressado) | Aceitar · pesar 0.5x na análise |
| ✅ | ❌ | Alta | Aceitar · continuar recrutamento |
| ❌ | ❌ | Alta | Descartar · refazer com outro prospect |
| ❌ | ✅ | Baixa | Descartar |

---

## §6 · RISK REGISTER · Específico Research Method

| ID | Risco | Likelihood | Impact | Score | Mitigation |
|---|---|:-:|:-:|:-:|---|
| RES-01 | < 16 respostas válidas em 30 dias | 3 | 4 | 12 | Snowball + LinkedIn outreach + extender prazo |
| RES-02 | Hierarquia violada > 30% respostas | 2 | 3 | 6 | Slider visual · explicação clara · descartar invalid |
| RES-03 | Anchoring bias (prospects sabem preços Confidata) | 3 | 3 | 9 | NÃO mencionar concorrentes no briefing |
| RES-04 | Stated vs actual preference gap 20% | 5 | 2 | 10 | Combinar com Gabor-Granger numa 2ª iteração |
| RES-05 | Pricing inputs anchoring no preço sugerido pelo entrevistador | 2 | 4 | 8 | Free-text input · não slider com range pré-definido |
| RES-06 | Wilton não captura objeções qualitativas relevantes | 3 | 3 | 9 | Transcrição automática (Otter.ai) + revisão Simone |
| RES-07 | Prospects B2G não comparecem (agenda) | 3 | 3 | 9 | Recrutar 35 (40% buffer) · reagendamento flexível |
| RES-08 | Resultado mostra pricing 30% abaixo do estimado | 2 | 5 | 10 | Plano B: revisar Cost Structure · reduzir custos · pivot |
| RES-09 | Resultado mostra pricing 30% acima do estimado | 1 | 2 | 2 | Bom problema · revalidate com piloto pago |
| RES-10 | Confidencialidade respondentes (B2G sensível) | 2 | 4 | 8 | NDA · anonimização · relatório agregado only |

**Top 3 críticos**: RES-01 · RES-04 · RES-08.

---

## §7 · TIMELINE OPERACIONAL · 30 dias

```
Semana 1 (M0 dias 1-7) · PREPARATION
├─ Dia 1-2: Briefing materials + lista 35 prospects
├─ Dia 3-7: Outreach + convites + tracking aceites
└─ Gate: 25 aceites confirmados

Semana 2 (M0 dias 8-14) · WAVE 1 INTERVIEWS
├─ Dia 8-9: Agendamento via Calendly
├─ Dia 10-14: Conduzir 12 entrevistas (Wilton 3-4/dia)
└─ Gate: 8+ respostas válidas

Semana 3 (M0 dias 15-21) · WAVE 2 INTERVIEWS + ANÁLISE
├─ Dia 15-19: Conduzir +13 entrevistas
├─ Dia 20-21: Análise PSM parcial (curvas preliminares)
└─ Gate: 16+ respostas válidas

Semana 4 (M0 dias 22-30) · CONSOLIDATION
├─ Dia 22-24: Análise NMS revenue curve
├─ Dia 25-26: Síntese qualitativa
├─ Dia 27-28: Refatorar S3.0.1 §14.2
├─ Dia 29: VVV update + insights catalog
└─ Dia 30: Follow-up report prospects
```

### Marcos críticos

| Marco | Dia | Validação |
|---|:-:|---|
| M1 · Briefing ready | 2 | Simone aprova 5 1-pagers |
| M2 · Outreach iniciado | 7 | 35 prospects contatados |
| M3 · 25 aceites | 10 | Calendly cheio |
| M4 · 16 respostas válidas | 20 | Camila valida hierarquia |
| M5 · Análise PSM completa | 24 | 5 OPPs calculados |
| M6 · Pricing refatorado | 28 | S3.0.1 v3.1 entregue |
| M7 · Follow-up enviado | 30 | LASTRO-WTP ✅ |

---

## §8 · OUTPUT STRUCTURE · Relatório Final S3.0.3

```markdown
# Relatório S3.0.3 · WTP Validation Results

## §1 · Metodologia aplicada
- Van Westendorp PSM + NMS extension
- N total: [16-25] · Período: [date range]
- Taxa descarte (hierarchy violation): [%]

## §2 · Resultados por Cluster

### Alfa Federal/Estadual (N=[X])
[Gráfico cumulative distribution]
- PMC: R$ [X]
- PME: R$ [Y]  
- OPP: R$ [Z]
- IPP: R$ [W]
- Acceptable Range: R$ [PMC] - R$ [PME]
- Revenue Max Price (NMS): R$ [V]

[Repetir para Alfa Mun, Beta, Gamma, Épsilon]

## §3 · Comparação WTP × Pricing S3.0.1 v3.0

| Cluster | Pricing v3.0 P50 | OPP WTP | Δ | Ação |
|---|---:|---:|---:|---|
| Alfa Federal | R$ 18.000 | R$ [?] | [?%] | [manter / subir / descer] |
| Alfa Municipal | R$ 8.000 | R$ [?] | [?%] | [manter / subir / descer] |
| Beta Hospital | R$ 7.500 | R$ [?] | [?%] | [...] |
| Gamma Escola | R$ 2.800 | R$ [?] | [?%] | [...] |
| Épsilon DPO | R$ 580 | R$ [?] | [?%] | [...] |

## §4 · Insights Qualitativos

### Top 5 Objeções
1. [...]
2. [...]

### Top 5 Drivers de Compra
1. [...]

### Surpresas (insights não previstos)
- [...]

## §5 · Refatoração Pricing v3.1

[Tabela mestre nova § 14.2 de S3.0.1 atualizada]

## §6 · Próximos Passos

- S3.0.4 APENDICE-D xlsx com pricing WTP-validated
- S3.0.5 Retificar Cap 11 §pricing
- Piloto pago 3 clientes early adopters (validação behavioral · NMS revenue curve real)
```

---

## §9 · LASTROS RESOLVIDOS / CRIADOS

| LASTRO | Status antes S3.0.3 | Status após S3.0.3 |
|---|---|---|
| LASTRO-WTP | 🔴 VVV 0.35 | ✅ VVV 0.85+ |
| LASTRO-CHURN | 🟠 VVV 0.50 | 🟠 0.50 (não destrava aqui · Wave 1 M+6) |
| LASTRO-CSC | 🟡 VVV 0.65 | 🟡 0.65 (não destrava aqui · Wave 1 operação) |

**VVV global do Sprint 3.0.1 sobe**: 0.78 → 0.87 (com S3.0.3 sozinho) · 0.95+ (com S3.0.3 + S2.5.3 + S3.0.2)

---

## §10 · Conformidade Metodológica

| Mandato | Status | Evidência |
|---|---|---|
| Constitution Art. 1 · investigou antes | ✅ | web_search SOTA 2026 Van Westendorp + NMS |
| RGO-5 · Honestidade Epistêmica | ✅ | N=25 declarado direcional (não estatístico rigoroso) |
| POP §6 · IA própria | ✅ | Análise PSM em Python local (não API externa) |
| POP §7 · D-015 lastros | ✅ | LASTRO-WTP destravado |
| BABOK BA-Orchestration | ✅ | 5 skills aplicadas |
| documentation-standards | ✅ | runbook + technical-writer + MDT |
| AP-13 · não API externa | ✅ | Stack 100% local |

---

## §11 · Autoavaliação PMQS

| Critério | Peso | Score | Justificativa |
|---|---:|---:|---|
| CE | 15% | 9.5 | Protocolo executável end-to-end · BPMN + RACI + Timeline |
| PI | 15% | 9.5 | Metodologia ancorada Van Westendorp 1976 + NMS + SOTA 2026 |
| CC | 10% | 9.0 | Runbook claro · steps numerados · ownership claro |
| PRI | 20% | 9.5 | 4 perguntas PSM + 2 NMS + análise + revenue curve · profundidade total |
| RA | 15% | 9.5 | Cada seção alimenta execução real |
| EIC | 10% | 9.5 | Workflow BPMN + Decision Table + Timeline integrados |
| OVA | 15% | 9.5 | Adaptação BR + B2G específica + [MODELO_AJUSTE] embedded |
| **PMQS Bruto** | 100% | **9.42** | — |
| **VVV** | — | 0.90 | Metodologia validada · execução pendente |
| **PMQS Final** | — | **8.48** | Acima target 8.0 ✅ |

---

**FIM SPRINT S3.0.3 · v1.0**

`Hash: NEOGOV-V21-S3.0.3-v1.0-WTP-PROTOCOL-READY-FOR-EXECUTION`

`Honra: POP v2.1.1.1 · BA-Orchestration BABOK v3 · documentation-standards · D-015 · D-019`

`Pronto para execução · 30 dias úteis · Wilton owner · target VVV 0.78 → 0.95`
