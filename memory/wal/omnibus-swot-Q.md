# [TRACE-Q] SWOT — Stage Questionador
**Timestamp**: 2026-05-09T00:05:00-03:00
**Input**: omnibus-swot-S.md (40 itens inventariados)
**Pipeline**: OMNIBUS S→Q→I→A | MEEST-AE v2.1 | shuntzu-f2+f3

---

## Classificação Epistêmica

Legenda:
- **FACT**: declaração verificável com fonte primária e linha exata
- **INFERENCE**: conclusão lógica a partir de dados verificados
- **SPECULATION**: extrapolação plausível sem base documental direta
- **BELIEF**: opinião/posição estratégica do time sem evidência externa

| ID  | Cat | Classificação   | VVV Verificado? | Justificativa                                                                        |
|-----|-----|-----------------|-----------------|--------------------------------------------------------------------------------------|
| S1  | S   | FACT            | SIM — transcrição linha exata | Declaração direta dos participantes sobre escopo e foco de mercado |
| S2  | S   | INFERENCE       | SIM — transcrição           | Three-pillar descritos na reunião; "diferenciação vs. concorrentes" é inferência estratégica |
| S3  | S   | FACT            | SIM — lei citada exata      | Lei 14.133/2021 Art.75 IV é fato jurídico verificável. ETEC/CPSI dependem de qualificação confirmada |
| S4  | S   | BELIEF          | PARCIAL — insights doc      | Tecnologias descritas como diferencial, mas benchmarking contra concorrentes não está documentado |
| S5  | S   | FACT            | SIM — insights doc          | Nomes e papéis declarados — verificável, mas complementaridade é INFERENCE |
| S6  | S   | INFERENCE       | SIM — insights doc          | Cronograma declarado; "marcos claros" é qualificação subjetiva sem métricas de sucesso por sprint |
| S7  | S   | BELIEF          | PARCIAL — insights doc      | Posicionamento estratégico articulado pelo time; sem validação de mercado externo |
| S8  | S   | FACT            | SIM — transcrição           | Parceria NELGOV mencionada; "expertise comprovada" é INFERENCE — sem cases documentados |
| S9  | S   | BELIEF          | PARCIAL — analise-riscos    | "Concorrentes não oferecem" é asserção sem benchmark formal dos competidores |
| S10 | S   | SPECULATION     | FRACO — transcrição         | "Spread comprovado" mas valores reais não aparecem no YAML, apenas conceito do modelo |
| W1  | W   | FACT            | SIM — transcrição linha exata | Gap explicitamente reconhecido em reunião: ausência de validação econômica quantificada |
| W2  | W   | FACT            | SIM — transcrição linha exata | Citação direta: "método é bem-venda corpo a corpo" — não escalonável conforme declarado |
| W3  | W   | FACT            | SIM — transcrição linha exata | "Pergunta não respondida" é evidência direta de gap não preenchido |
| W4  | W   | FACT            | SIM — transcrição linha exata | "Duas ferramentas sem clareza de MVP" citado diretamente |
| W5  | W   | INFERENCE       | SIM — insights doc          | "Sem experiência municipal prévia" — lógico dado que é startup; risco real |
| W6  | W   | FACT            | SIM — analise-riscos         | Ausência de fornecedores mapeados é gap factual documentado |
| W7  | W   | FACT            | SIM — transcrição linha exata | Dúvida sobre OSCIP é explicitamente registrada na transcrição |
| W8  | W   | INFERENCE       | SIM — insights doc          | Gap identificado na reunião; "co-founder" é solução específica sugerida |
| W9  | W   | FACT            | SIM — insights doc          | Ausência de LOIs é verificável objetivamente |
| W10 | W   | FACT            | SIM — insights doc          | Gap de informação é meta-observação analítica direta |
| O1  | O   | FACT            | SIM — IBGE MUNIC 2024       | Dado estatístico de fonte primária nacional — mais alto VVV (1.0), verificável |
| O2  | O   | INFERENCE       | SIM — intel-mercado doc     | SAM derivado de filtro sobre TAM: "orçamento mas sem equipe" é critério inferido |
| O3  | O   | FACT            | SIM — intel-mercado doc     | Agenda ANPD 2025-2026 é política pública declarada — verificável |
| O4  | O   | FACT            | SIM — intel-mercado doc     | Auditoria TCU/TCEs 2024-25 com resultado "inexpressivo/inicial" — dado público |
| O5  | O   | INFERENCE       | SIM — intel-mercado doc     | "Mercado faminto" é síntese estratégica a partir de O1+O3+O4 |
| O6  | O   | FACT            | SIM — intel-mercado doc     | Credenciamento R$31.9M do CIMINAS/Granbel é dado verificável de licitação pública |
| O7  | O   | INFERENCE       | SIM — intel-mercado doc     | "Cavalo de Troia" = metáfora estratégica sobre dor LAI — a dor é FACT, a estratégia é INFERENCE |
| O8  | O   | BELIEF          | PARCIAL — intel-mercado     | "Concorrentes não endereçam" é asserção sem análise detalhada dos players |
| O9  | O   | SPECULATION     | FRACO — insights doc        | R$15-50K/ano é estimativa sem fonte primária de orçamento municipal verificada |
| O10 | O   | FACT            | SIM — Acórdão 1153/2025     | Acórdão TCE-PR com número específico é fato jurídico verificável |
| T1  | T   | FACT            | SIM — transcrição linha exata | Declaração direta sobre prefeituras; "40%" é estimativa dentro da conversa |
| T2  | T   | FACT            | SIM — insights doc          | >12 meses sales cycle B2G é dado setorial reconhecido e documentado |
| T3  | T   | FACT            | SIM — intel-mercado doc     | Lista de competidores com nomes é verificável — "preços agressivos" é INFERENCE |
| T4  | T   | FACT            | SIM — transcrição linha exata | Citação direta do participante sobre comportamento de prefeitos — analogia lixo |
| T5  | T   | FACT            | SIM — transcrição           | Fiscalização ANPD desde 2022 é público; "se intensificando" é INFERENCE |
| T6  | T   | INFERENCE       | SIM — transcrição           | Caso AIDS usado como exemplo; risco operacional é INFERENCE plausível |
| T7  | T   | SPECULATION     | FRACO — insights doc        | "6-12 meses" para cópia é estimativa sem base em velocidade real de roadmap dos concorrentes |
| T8  | T   | SPECULATION     | FRACO — analise-riscos      | Mudança regulatória futura é cenário por natureza especulativo |
| T9  | T   | SPECULATION     | FRACO — analise-riscos      | Turnover político é risco real mas probabilidade e frequência não documentadas |
| T10 | T   | SPECULATION     | FRACO — analise-riscos      | Rejeição técnica é risco genérico sem histórico de ocorrência em contratos similares |

**Distribuição epistêmica**:
- FACT: 22 itens (55%)
- INFERENCE: 10 itens (25%)
- SPECULATION: 6 itens (15%)
- BELIEF: 4 itens (10%)

> **Observação Q**: 40% dos itens são INFERENCE/SPECULATION/BELIEF. Para um instrumento de decisão estratégica, o ideal seria >70% FACT. Gap epistêmico relevante em especial nas forças (S4, S7, S9) e ameaças (T7-T10).

---

## 5N — Item Crítico 1: W1 (VVV=0.95, Impacto=CRÍTICO)
*"Viabilidade econômica NÃO validada — custo dev X preço X margem sem 80% confidence"*

**Por que a viabilidade não está validada?**
→ Porque nenhum desenvolvedor ou CTO formalizou orçamento de desenvolvimento em reunião.

**Por que o orçamento de desenvolvimento não foi formalizado?**
→ Porque o escopo do produto ainda não está definido (W4) — impossível orçar o indefinido.

**Por que o escopo do produto não está definido?**
→ Porque o time está debatendo "duas ferramentas vs. plataforma integrada" sem decisão de MVP (W4, L1668-L1669).

**Por que a decisão de MVP não foi tomada?**
→ Porque a estratégia de go-to-market não está fechada: sell jurídico primeiro ou tech first? Cada opção implica MVP diferente.

**Por que a estratégia de GTM não está fechada?**
→ Porque sem OSCIP ativa (W7) e sem LOIs (W9), o canal de vendas primário é incerto — sem canal definido, qualquer MVP pode ser o MVP errado.

**Conclusão 5N-W1**: O gap de viabilidade econômica é sintoma terminal de um problema de sequência: canal → MVP → custo → pricing. Resolver W7 e W9 antes de W1 é o caminho lógico, não o inverso.

---

## 5N — Item Crítico 2: O1 (VVV=1.00, Impacto=TAM estratégico)
*"TAM: 5.570 municípios, ~72% SEM estrutura LGPD — IBGE MUNIC 2024"*

**Por que 72% dos municípios não têm estrutura LGPD?**
→ Porque LGPD foi promulgada em 2018 com vigência de 2020, mas municípios pequenos não têm capacidade técnica ou jurídica interna.

**Por que municípios pequenos não têm capacidade técnica para LGPD?**
→ Porque carecem de servidores especializados em proteção de dados e os recursos do FPM são consumidos por saúde e educação obrigatórias.

**Por que a pressão regulatória não gerou adequação mesmo após 6 anos?**
→ Porque a ANPD estava em fase educativa até 2024 — sem sanção efetiva, sem urgência percebida pelo gestor local.

**Por que a ausência de sanção importa para o modelo de negócio?**
→ Porque T4 confirma: prefeitos agem com (a) processo/inelegibilidade, (b) votos, (c) sobra de orçamento. Sem sanção efetiva, urgência não se converte em contrato.

**Por que isso é crítico para a janela de oportunidade?**
→ Porque a "janela 2025-2026" (O5) pressupõe que a transição ANPD de educativo para fiscalização realmente acelera. Se a transição for gradual, o TAM permanece endereçável mas a velocidade de conversão será muito menor que o modelo assume.

**Conclusão 5N-O1**: O TAM de 4.011 municípios é real mas a taxa de conversão anual é muito menor — a urgência de compra depende da velocidade real de enforcement da ANPD, que é variável exógena de alto impacto não controlada pelo time.

---

## 5N — Item Crítico 3: T2 (VVV=0.95, Impacto=ALTO — destrói runway)
*"Sales cycle B2G >12 meses — burocracia, licitações, turnover político"*

**Por que o ciclo de vendas B2G é >12 meses?**
→ Porque prefeituras exigem processo de contratação formal: proposta → análise jurídica → empenho orçamentário → licitação (exceto Art.75) → contrato → onboarding.

**Por que isso é ameaça crítica para o modelo ICT?**
→ Porque mesmo com dispensa licitação (S3), os processos internos de empenho e aprovação da prefeitura continuam existindo e não são contornados pelo Art.75.

**Por que o Art.75 não elimina o ciclo longo?**
→ Porque Art.75 elimina *licitação*, não o processo administrativo interno — empenho, aval do prefeito, verificação de limite de crédito, análise da controladoria ainda ocorrem.

**Por que isso ameaça o runway do projeto?**
→ Porque com 4 sprints em Junho 2026 e sem LOIs (W9), o primeiro contrato pago pode chegar somente em meados/fim de 2027, consumindo todo o runway antes da primeira receita.

**Por que o time não calculou o runway necessário?**
→ Porque W1 (viabilidade econômica) e W3 (time técnico não dimensionado) ainda não foram resolvidos — o cálculo de runway requer custo de desenvolvimento + custo de vendas + overhead × ciclo de vendas de 12+ meses.

**Conclusão 5N-T2**: O sales cycle >12 meses combinado com W1+W9 cria risco de runway zero antes do primeiro contrato. O modelo precisa de um plano de bridge: LOIs como proxy de tração para captação antes da receita.

---

## Vieses na Análise Original

### 1. Viés de Confirmação
O YAML foi produzido por "agent-SWOT-specialist" pós-reunião onde o time estava motivado. A lista de Forças (10 itens bem articulados, VVV médio 0.845) é mais polida e detalhada que a lista de Ameaças (VVV médio 0.775). Risco de subestimar adversários e superestimar diferenciais.

**Evidência**: S4, S7, S9 classificados como BELIEF — os três afirmam superioridade sobre concorrentes sem benchmark formal.

### 2. Viés de Âncora
A "condição green-light" no YAML (custo dev ≤ R$150K, pricing ≥ R$5K/mês, OSCIP ativa) foi definida sem análise de mercado comparativa — os valores parecem razoáveis mas não têm base empírica declarada. Uma vez escritos, tornam-se âncoras difíceis de questionar.

### 3. Viés de Autoridade
Várias afirmações estratégicas na análise original derivam de participantes da reunião (Wilton, Gislene) que têm interesse no sucesso do projeto. O "risco de inadimplência 40%" (T1) foi declarado por um dos participantes — não é dado estatístico externo, é estimativa interna tratada como FACT.

### 4. Viés de Disponibilidade
T5 e T6 (fiscalização intensa, caso AIDS) são eventos salientes e memoráveis que podem estar inflando a percepção de risco operacional imediato em detrimento de ameaças menos dramáticas mas mais prováveis (T7: cópia por concorrentes, T9: turnover político).
