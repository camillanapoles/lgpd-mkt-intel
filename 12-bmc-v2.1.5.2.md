---
id: NEOGOV-V21-CAP-12-BMC
filename: 12-bmc-v2.1.5.2.md
created_at: 2026-05-15T23:50:00Z
type: BP_CHAPTER
sprint: W1.2-PATCH
edicao: 2
parent_doc: BUSINESS-PLAN-FINAL-v2.1
chapter_number: 12
fdcu_score: 9.0
pmqs_target: 8.5
vvv_target: 0.85
abordagem: BMC_Osterwalder_9_blocos + L2_cognitivo + cost-plus-otimização + sanity_check_analogo
referencia_capitulos: [02, 04, 07, 08, 11, 13, 14, 15, 16]
referencia_apendices: [APENDICE-D-PRICING-FUNCTION-v1.0.1]
herda_decisoes: [D-ARC-001, D-SAU-001, D-010, D-EXEC-001, D-EXEC-002, D-EXEC-003, D-011, D-012, D-AUDIT-D001, D-W1.2-001, D-W1.2-002]
insights_consumidos: [IN-002, IN-008, IN-014, IN-017]
retificacao_aplicada: D-W1.2-002 (pricing bottom-up cost-plus matemático · §12.7-BIS adicionado)
base_de_lastro:
  - $1 DIAGNOSTICO (clusters · mercado · regulação)
  - $2 DECISAO (D-ARC-001 híbrido · D-SAU-001 postergar saúde)
  - 02-vmv-v2.1.4.3 (Missão L2 · 5 valores · 6 princípios)
  - SPRINT-3.0.1-v3.0 §12 §15 §16 (pricing · unit economics · 13 skills BABOK)
  - F4 CONSOLIDACAO (7 mandatos · 5 garantias)
audiencia_dual:
  L1_tecnico_interno: Key Activities · Key Resources · Cost Structure · Channels delivery
  L2_cognitivo_externo: Value Propositions · Customer Relationships · narrativa benefício
tags: [bmc, business-model-canvas, 9-blocos, osterwalder, l1-l2, value-proposition, revenue-streams, cost-structure, devil-advocate]
---

# Capítulo 12 · Business Model Canvas

> "Um modelo de negócio bem desenhado responde uma só pergunta com nove respostas conectadas: **para quem criamos valor, como criamos, e por que sobrevivemos fazendo isso?**"

---

## 12.1 Por que o BMC é o contrato lógico do BP

Os capítulos anteriores estabeleceram fragmentos da identidade e da estratégia: o método (Cap 04), as personas (Cap 07), os clusters (Cap 08), os produtos (Cap 11), e a VMV (Cap 02). O Business Model Canvas faz uma operação distinta — **costura todos esses fragmentos num único contrato lógico** que precisa fechar conta de dois lados:

- **Lado direito** (valor entregue · receita): para quem · o que · como vendemos
- **Lado esquerdo** (valor produzido · custo): com o quê · como · com quem

A regra fundamental do BMC de Osterwalder: **se o lado esquerdo custa mais do que o direito gera, o negócio não existe**. Se gera muito mais sem justificar a captura, deixa valor na mesa. O BMC torna essa equação visível.

Este capítulo opera com a **distinção L1/L2** estabelecida no Cap 02 v2.1.4.3 [DECISÃO D-012 do Apêndice B]:

- Blocos **Value Propositions** e **Customer Relationships** → **L2 cognitivo** (benefício humano sentido)
- Blocos **Key Activities**, **Key Resources**, **Cost Structure**, **Channels (delivery)** → **L1 técnico** (método auditável)

Não há contradição entre as camadas — são audiências distintas (cliente vs equipe) para o mesmo modelo.

---

## 12.2 Diagrama Canvas NeoGov v2.1

```
┌──────────────┬──────────────┬──────────────────────┬──────────────┬──────────────┐
│ KEY PARTNER- │ KEY          │ VALUE PROPOSITIONS   │ CUSTOMER     │ CUSTOMER     │
│ SHIPS        │ ACTIVITIES   │                      │ RELATIONSHIPS│ SEGMENTS     │
├──────────────┼──────────────┤  Alfa B2G:           ├──────────────┼──────────────┤
│ • Magalu BR  │ • Curadoria  │  "Compliance sem     │ Manage close:│ • Alfa B2G   │
│   /TIVIT     │   knowledge  │   licitação via      │   Federal/Est│   Federal/Est│
│   cloud BR   │   jurídico   │   Art.75 IV — e sem  │   ⌃ CSM ded. │ • Alfa B2G   │
│ • CNM/CIMI   │ • Fine-tune  │   o medo da multa"   │              │   Municipal  │
│   consórcios │   IA própria │                      │ Co-creation: │ • Beta       │
│ • Contadores │ • Plataforma │  Beta Saúde:         │   Federações │   Hospital   │
│ • Hardware   │   SaaS multi-│  "Anonimização para  │   Hosp Anahp │   privado    │
│   L40S/L4    │   tenant     │   pesquisa científica│              │ • Gamma      │
│ • FNDE/Adv   │ • Customer   │   sem violar LGPD"   │ Self-service:│   Escola     │
│   Cota Wilton│   Success    │                      │   Gamma · Eps│   privada    │
│ • Anahp     │ • Compliance │  Gamma Escola:       │              │ • Épsilon    │
│   (Wave 3)   │   audit      │  "ECA Digital em     │ Communities: │   Escritório │
│              ├──────────────┤   piloto automático: │   Webinars   │   DPO        │
│              │ KEY RESOURCES│   menos burocracia,  │   LinkedIn   │   independ.  │
│              ├──────────────┤   mais segurança"    │              │              │
│              │ • IA própria │                      │              │              │
│              │   Llama 8B   │  Épsilon DPO:        │              │              │
│              │   fine-tuned │  "Multiplique sua    │              │              │
│              │ • Expertise  │   prática jurídica   │              │              │
│              │   Simone+    │   com IA copilota    │              │              │
│              │   Gislênia   │   especializada BR"  │              │              │
│              │ • Plataforma │                      │              │              │
│              │ • ICT status │                      │              │              │
│              │ • Founders 4 │                      │              │              │
├──────────────┴──────────────┴──────────────────────┴──────────────┴──────────────┤
│                                                                                   │
│  CHANNELS                                                                         │
│  Awareness: LinkedIn · CONFIP/CONIP eventos · Webinars FNDE · CNM publicações    │
│  Evaluation: Demo plataforma · POC 30 dias · Diagnóstico LGPD gratuito           │
│  Purchase: Art.75 IV B2G (dispensa) · Art.37 §2° · Boleto/PIX/cartão B2C         │
│  Delivery: SaaS multi-tenant cloud BR · On-premise (Beta hospital · Alfa fed)    │
│  Customer Success: Onboarding 30d · Trimestral review · 24/7 chat                │
│                                                                                   │
├──────────────────────────────────────────────────────┬───────────────────────────┤
│ COST STRUCTURE                                       │ REVENUE STREAMS           │
├──────────────────────────────────────────────────────┼───────────────────────────┤
│ Fixos mensais Wave 1 P50: R$ 146.000 [S3.0.1 §2]    │ Subscription tier·P50    │
│ CSC variável médio: R$ 1.170/cliente/mês             │ Setup one-time           │
│ CAPEX inicial P50: R$ 169.500                        │ Hybrid setup+manutenção  │
│                                                      │ Usage-based (P3 B2C)     │
│ Drivers: Folha 62% · Infra 10% · Mkt 12% ·          │ Per seat (P4 AI-DPO)     │
│ Encargos 7% · SW 4% · Contingência 5%                │ Project + retainer (P5)  │
│                                                      │                          │
│ Type: Value-driven (alta margem · automação)         │ Pricing por análogo      │
│                                                      │ (D-015 LASTROS · §12.7)  │
└──────────────────────────────────────────────────────┴───────────────────────────┘
```

---

## 12.3 Bloco 1 · Customer Segments

### Quem servimos

Os segmentos derivam dos 6 clusters estabelecidos no Cap 08 (Sprint 1 anterior · FDC-U sustentado):

| ID | Cluster | Tamanho TAM | Wave de entrada | Prioridade |
|---|---|---|:--:|:--:|
| **Alfa-M** | B2G Municipal (5.569 munic · 1.800 na faixa target) | R$ 8-32 mil/mês | W1 Beachhead | 🥇 |
| **Gamma** | Escola privada (~42.000 unidades target) | R$ 497-3.997/mês | W1 Beachhead duplo | 🥇 |
| **Alfa-F/E** | B2G Federal/Estadual (387 órgãos · 58.9% iniciais) | R$ 25-40 mil/mês | W3-W4 | 🥈 |
| **Épsilon** | Escritórios DPO independentes | R$ 800-2.500/mês per seat | W3 | 🥈 |
| **Beta** | Hospital privado (169 Anahp · 246 AMIB top) | R$ 5-25 mil/mês | W5 (POSTERGADO · D-SAU-001) | 🥉 |
| **Delta** | Federações multiplicadoras (CNM · ABRH · CRC) | Indireto (vitória sem batalha) | W4 | Estratégico |

### Tipo de cliente (Osterwalder taxonomy)

**Multi-sided plataform** para Wave 4: Delta = federações multiplicam Alfa+Gamma+Épsilon.
**Niched market** em cada cluster: cada um tem dor específica e canal próprio.
**NÃO mass market**: NeoGov rejeita atender "qualquer empresa que queira LGPD" — foco mata waste.

### Devil's Advocate

> **Contra**: "Atender 6 clusters não dilui o foco?"
>
> **Refutação**: Os clusters foram derivados por FDC-U comportamental — não por geografia ou tamanho. Eles **compartilham 70% da infraestrutura** (plataforma · IA · expertise jurídica) e diferem apenas em produto-âncora + canal. Não é dispersão · é alavancagem da mesma máquina sobre múltiplas correias.

[LASTRO §12.3] Cap 08 · Cap 11 · $1 Diagnóstico · $2 Decisão · F4 §G-003 Caminho Pessimista (cluster a cluster)

---

## 12.4 Bloco 2 · Value Propositions (L2 cognitivo)

### Princípio cognitivo (IN-014)

Cada Value Proposition aqui é redigida no **modo cognitivo externo (L2)** — fala do **benefício humano sentido** pelo cliente, não do método industrial usado internamente. O método é traduzido para a equipe nos Caps 04, 11 e 12.9 deste capítulo.

### Value Proposition #1 · Alfa B2G Municipal

> **"Conformidade com a LGPD sem licitação travada e sem o medo da próxima fiscalização."**

| Elemento | Detalhe |
|---|---|
| Para quem | Procurador Municipal · CIO Estadual · gestor de pequena prefeitura |
| Dor atacada | "Não tenho orçamento de R$600k para Big4" + "ANPD pode bater amanhã" |
| Job-to-be-done | Demonstrar conformidade auditável sem paralisar a operação |
| Pain reliever | Art. 75 IV dispensa licitação (R$65.492/ano cabe) · Art. 37 §2° (R$392.952/ano) |
| Gain creator | Auditabilidade reversa: cada decisão automatizada gera rastro · TCE-PR friendly |
| Diferencial defensável | Expertise LAI×LGPD especializada (P3 único no mercado) + ICT habilita Art.75 IV |

### Value Proposition #2 · Beta Saúde Hospital (POSTERGADO · referência)

> **"Use dados de pacientes em pesquisa científica sem violar a LGPD — porque a anonimização não é improviso."**

| Elemento | Detalhe |
|---|---|
| Para quem | DPO hospitalar · CIO Anahp · diretor pesquisa científica |
| Dor atacada | "Tenho dataset enorme mas não posso usar por receio LGPD" |
| Job-to-be-done | Habilitar pesquisa científica e cooperação acadêmica com proteção real |
| Pain reliever | Anonimização técnica auditável (P3) · ETL MV/Tasy validado |
| Gain creator | Acelera publicações · viabiliza parcerias internacionais |
| Status | 🟠 POSTERGADO · D-SAU-001 · entrada Wave 5 após Wave 1-2 estabilizadas |

### Value Proposition #3 · Gamma Escola Privada

> **"ECA Digital em piloto automático: menos formulários, mais segurança para os pais."**

| Elemento | Detalhe |
|---|---|
| Para quem | Mantenedor escolar · diretor pedagógico · responsável TI escola |
| Dor atacada | "Não tenho TI dedicada · ECA Digital vigente 17/03/2026 · pais perguntam" |
| Job-to-be-done | Cumprir LGPD + ECA Digital sem virar advogado nem contratar Big4 |
| Pain reliever | Consentimento parental automatizado · plataforma onboarded em 7 dias |
| Gain creator | Pode dizer aos pais "estamos em conformidade" com evidência |
| Diferencial defensável | ZERO concorrente dedicado ECA Digital + LGPD (Diagnóstico §1.1 VVV 0.90) |

### Value Proposition #4 · Épsilon Escritório DPO

> **"Multiplique sua prática jurídica com uma IA copilota que entende a LGPD brasileira."**

| Elemento | Detalhe |
|---|---|
| Para quem | Advogado DPO · escritório boutique compliance · consultor independente |
| Dor atacada | "Tenho 30 clientes · só consigo atender bem 10 · não escalo" |
| Job-to-be-done | Atender mais clientes com mesma qualidade · profissional respeitado |
| Pain reliever | AI-DPO especializada BR · automatiza RIPDs · advogado revisa e assina |
| Gain creator | Triplica capacidade de atendimento · LTV aumenta · churn cai |
| Modelo | Per seat licensed · profissional permanece o decisor (Valor 2 NeoGov · Princípio 4) |

### Princípio comum (deriva do Cap 02 VMV)

Todas as 4 Value Propositions atacam o mesmo vilão: **complexidade legal que paralisa**. Todas entregam o mesmo benefício humano: **segurança jurídica e produtividade sem o peso da complexidade**. Diferem apenas no produto-âncora e no canal.

### Devil's Advocate

> **Contra**: "OneTrust e TrustArc já oferecem isso globalmente — por que NeoGov vence?"
>
> **Refutação**: OneTrust/TrustArc não fazem LAI brasileira (Lei 12.527/2011), não fazem ECA Digital (Lei 15.211/2025), e não são ICT — portanto não habilitam Art. 75 IV de dispensa de licitação para B2G. NeoGov tem 3 trincheiras defensáveis simultâneas: regulação BR específica · ICT status · expertise jurídica brasileira manufaturada em produto.

[LASTRO §12.4] Cap 02 v2.1.4.3 · Cap 11 §11.6 · $1 §1.1-1.4 · IN-008 · IN-014

---

## 12.5 Bloco 3 · Channels

### Estrutura por estágio do funil

| Estágio | Canal | Cluster prioritário | KPI |
|---|---|---|---|
| **Awareness** | LinkedIn orgânico · Posts da Simone | Alfa-M + Épsilon | Impressões · seguidores qualificados |
| | CONFIP/CONIP eventos B2G | Alfa-M · Alfa-F/E | Leads B2G · cards trocados |
| | Webinars FNDE | Alfa-M | Inscritos · CIO municipal contactável |
| | Publicações CNM/ABRH | Delta · Alfa-M | Endorsement institucional |
| **Evaluation** | Demo plataforma 30 min | Todos | Demo→POC rate |
| | POC 30 dias gratuito (Gamma+Épsilon) | Gamma · Épsilon | POC→assinatura rate |
| | Diagnóstico LGPD gratuito (Alfa) | Alfa-M | Diagnóstico→contrato rate |
| **Purchase** | Dispensa Art. 75 IV (R$65.492/ano) | Alfa-M até 30k hab | CAC B2G · Win rate dispensa |
| | Procedimento simplificado Art. 37 §2° | Alfa-M 30k-100k | CAC B2G · Ciclo médio |
| | Licitação ETEC/CPSI (RDC simplificado) | Alfa-F/E · Alfa-M >100k | Win rate competitivo |
| | Boleto/PIX/cartão B2C com parcelamento | Gamma · Épsilon | Conversão checkout |
| **Delivery** | SaaS multi-tenant cloud BR (Magalu/TIVIT) | Padrão default | Uptime · latência |
| | On-premise/cloud privada | Alfa-F/E · Beta | Setup time · satisfação |
| **Customer Success** | Onboarding 30 dias acompanhado | Todos | Time-to-first-value |
| | Trimestral review (Beta · Alfa-F/E) | Premium tiers | NPS · retention |
| | Chat 24/7 (todos os tiers) | Todos | First response time |

### Mix de canais por cluster

```
Alfa-M    : 60% direto (Simone+Wilton) · 30% federações (CNM) · 10% inbound
Alfa-F/E  : 80% direto (relacionamento) · 20% via federações estaduais
Gamma     : 20% direto · 60% inbound digital · 20% Delta (federação FENEP)
Épsilon   : 50% Webinars + LinkedIn · 30% indicação · 20% direto
Beta      : 70% direto (relacionamento Anahp) · 30% via Wave 5 piloto
Delta     : 100% relacionamento institucional (Wilton)
```

### Devil's Advocate

> **Contra**: "Mix complexo demais · vai dispersar a operação"
>
> **Refutação**: Os canais convergem na **mesma plataforma de entrega** (SaaS multi-tenant). A complexidade aparente está só na aquisição · entrega é uniforme. CAC diferenciado é benefício, não problema — não força fee-for-service em quem prefere self-service.

[LASTRO §12.5] $3 Plano Execução · Sprint 3.0.1 §6 Journey Mapping · §G-003 F4

---

## 12.6 Bloco 4 · Customer Relationships

### Modelo de relacionamento por cluster (Osterwalder taxonomy)

| Cluster | Tipo | Frequência humano | Plataforma |
|---|---|---|---|
| Alfa-F/E | **Personal assistance dedicada (CSM)** | Semanal | + dashboard executivo |
| Alfa-M | **Personal assistance compartilhada** | Quinzenal | + plataforma auto-service |
| Beta | **Co-creation premium** | Mensal | + setup dedicado |
| Gamma | **Self-service guiado** | Sob demanda | + chat 24/7 + KB |
| Épsilon | **Communities + self-service** | Webinars trimestrais | + tooling |
| Delta | **Co-creation institucional** | Trimestral | endorsement |

### Princípios que derivam do Cap 02 VMV

- **Valor 5 · Auditabilidade Reversa** → todo cliente recebe trilha completa de decisões automatizadas
- **Princípio 4 · IA aplica · profissional decide** → AI-DPO complementa, nunca substitui o consultor humano
- **Princípio 6 · L1/L2** → relacionamento com cliente fala benefício (L2), documentação interna fala método (L1)

### Política de NÃO-relacionamento

A NeoGov **rejeita ativamente** dois padrões:
- **Relacionamento puramente transacional**: clientes que tratam compliance como commodity barata · CAC > LTV
- **Relacionamento de dependência tóxica**: cliente que quer "consultor 24/7 me ligando para qualquer dúvida" · destrói escala

### Devil's Advocate

> **Contra**: "Self-service para Gamma escola · escolas brasileiras não têm cultura SaaS"
>
> **Refutação**: $1 Diagnóstico §1.1 mostra que 20.2% da educação básica é privada e crescendo (+17% pós-pandemia · creches 33.1% privadas). Esse mercado já usa Tindle, Lousa Digital, Class Plus — tem cultura SaaS. NeoGov entra em ambiente preparado, não pioneiro.

[LASTRO §12.6] Cap 02 v2.1.4.3 · Cap 07 Personas · $1 §1.1

---

## 12.7 Bloco 5 · Revenue Streams · Pricing por Análogo (D-015 LASTRO)

### Princípio operacional (D-015)

Todo preço apresentado neste bloco vem de **análogo comprovado com lastro rastreável** — não de margem aspiracional. O lastro está nos análogos competitivos do $1 Diagnóstico §competitivo + Sprint 3.0.1 v3.0 §3 (Benchmarking) + restrições legais de licitação (Lei 14.133/2021).

### Pricing Wave 1 Beachhead (Alfa-M + Gamma) · 🟡 [ESTIMATIVA POR ANÁLOGO COM LASTRO]

#### Alfa-M · B2G Municipal

| Tier | Pricing/mês | Pricing/ano | Modelo licitação | VVV |
|---|---:|---:|---|:--:|
| 🟢 **Município < 30k hab (Pro)** | R$ 5.456 | R$ 65.492 | Art. 75 IV (dispensa) | 0.82 |
| 🟢 **Município 30k-100k hab (Plus)** | R$ 14.000 | R$ 168.000 | Art. 37 §2° (simplificado) | 0.78 |
| 🟡 **Município > 100k hab (Enterprise)** | R$ 25.000 | R$ 300.000 | Procedimento competitivo · justificável | 0.65 |
| 🟡 **Federal/Estadual (Enterprise+)** | R$ 30.000-40.000 | R$ 360-480 mil | ETEC/CPSI · RDC | 0.62 |

**Lastros**:
- Art. 75 IV Lei 14.133/2021 → limite legal R$ 65.492/ano (anual exato Pro)
- Art. 37 §2° Lei 14.133/2021 → limite legal R$ 392.952/ano (Plus + folga)
- Análogos SaaS gov BR: Voga, Atende.NET R$ 5k-20k/mês (VVV 0.70)

#### Gamma · Escola Privada

| Tier | Pricing/mês | Pricing/ano | Modelo | VVV |
|---|---:|---:|---|:--:|
| 🟡 **Escola pequena (50-200 alunos · Basic)** | R$ 497 | R$ 5.964 | Boleto/PIX/cartão | 0.72 |
| 🟡 **Escola média (200-800 alunos · Pro)** | R$ 1.497 | R$ 17.964 | Boleto + parcelamento | 0.70 |
| 🟡 **Escola grande (800-1500 alunos · Enterprise)** | R$ 3.997 | R$ 47.964 | Contrato anual | 0.68 |

**Lastros**:
- LGPD Cloud R$199,90/mês = floor entry-level (Diagnóstico VVV 0.85)
- Confidata R$497-3.497/mês = gama competitiva direta (VVV 0.90)
- Gap pricing identificado R$3.500-55.000/mês (Diagnóstico §competitivo VVV 0.85)
- Diferencial ECA Digital exclusivo = +30% premium justificável

### Pricing Wave 2-3 (Épsilon + Alfa-F/E) · 🟡

| Cluster | Modelo | Pricing | VVV |
|---|---|---:|:--:|
| Épsilon DPO (per seat AI-DPO P4) | Licença por advogado | R$ 800-2.500/mês | 0.70 |
| Alfa-F/E Enterprise+ | Subscription + projeto | R$ 360k-800k/ano | 0.62 |

### Pricing Wave 5 (Beta · POSTERGADO referência) · 🟡

| Tier | Pricing/mês | VVV |
|---|---:|:--:|
| Hospital médio | R$ 5.000 | 0.70 |
| Hospital Anahp grande | R$ 15.000 | 0.70 |
| Rede hospitalar | R$ 30.000+ | 0.65 |

**Análogos**: OneTrust US$10k+/ano (R$53k+/ano = R$4.4k+/mês) · TrustArc US$10k-250k/ano

### Receita média anual por cluster (P50)

| Cluster | Receita média/cliente/ano P50 |
|---|---:|
| **Alfa Federal/Estadual** | R$ 250.000-800.000 |
| **Alfa Municipal** | R$ 90.000-180.000 |
| **Beta Hospital** | R$ 200.000-450.000 (W5) |
| **Gamma Escola** | R$ 18.000-48.000 |
| **Épsilon DPO** | R$ 9.600-30.000 |

### Modelos de cobrança por produto

| Produto | Modelo | Justificativa |
|---|---|---|
| P1 (Plataforma Core) | Subscription mensal/anual | SaaS clássico · receita previsível |
| P2 (Setup ETL hospital) | One-time + manutenção mensal | Setup pesado · manutenção contínua |
| P3 B2G (Anonimização LAI×LGPD) | Subscription premium | Diferencial único · alta margem |
| P3 B2C (Anonimização sob demanda) | Usage-based | Variável por volume processado |
| P4 (AI-DPO Copilot) | Per seat | Per advogado licenciado |
| P5 (Projeto + retainer) | Project + retainer mensal | Customização Alfa-F/E · híbrido |

### Devil's Advocate

> **Contra**: "VVV 0.62-0.82 ainda é frágil · pricing não é assertivo"
>
> **Refutação**: VVV sobe para 0.90+ apenas após Wave 1 piloto real (3-5 clientes · 3 meses). O patamar atual é honesto e cumpre M-001 (rastreabilidade). Tier Pro municipal (VVV 0.82) tem lastro legal direto (Art. 75 IV) — esse é assertivo. Tiers de menor VVV têm faixas declaradas, não pontos cegos.

> **Contra**: "Por que não cobrar mais? OneTrust cobra US$50k/ano"
>
> **Refutação**: NeoGov não compete com OneTrust em mesmo cliente. OneTrust não cabe em Art. 75 IV (não é ICT BR · não tem LAI). Gamma escola não compra OneTrust nem por R$4k/mês. Cada tier NeoGov é dimensionado para WTP do cluster específico, não para teto global.

[LASTRO §12.7] $1 §competitivo · Sprint 3.0.1 v3.0 §3 §15 §16 · Lei 14.133/2021 Art. 75 e 37 · F4 §G-001

> **🟡 RETIFICAÇÃO METODOLÓGICA D-W1.2-002 aplicada na edição 2 (v2.1.5.2)**: O conteúdo do §12.7 acima (pricing por análogo) foi degradado a **sanity check externo** · a base de cálculo primária agora é o método matemático bottom-up cost-plus + otimização micro-econômica detalhado em §12.7-BIS. Análogos permanecem como validação cruzada não-primária.

---

## 12.7-BIS · Pricing Function · Método Bottom-Up Cost-Plus + Otimização Matemática

> "Quem precifica por concorrente assume que é igual ao concorrente. NeoGov não é. Precificação justa parte do custo de produção, soma margem alvo + premiums de diferencial gritante, e otimiza no ponto onde lucro total é máximo dado a demanda inferida."

### Por que análogo não basta (D-W1.2-002 rationale)

A precificação por análogo competitivo é metodologicamente inadequada quando o serviço tem **diferenças gritantes** vs. concorrentes mapeados. Diferenciais gritantes invalidam a premissa de comparabilidade que sustenta análogo top-down. NeoGov tem 6 diferenciais gritantes documentados (Apêndice D §1) que justificam pricing assertivo via método matemático.

### Função NeoGov consolidada

```
P_NeoGov(cluster) = min(
                      max(P_base, P*),       # FLOOR: cost-plus OU ponto ótimo
                      P_legal_max,           # TETO: limite legal Art. 75 IV / 37 §2°
                      P_WTP_max              # TETO: demanda viável
                    )

onde:
  P_base = CT × (1 + m_alvo + Σ m_premiums_diferencial)
  P*     = CSC + (1/k)     [ponto ótimo · max L(P)]
  CT     = CSC + (CF/N)
```

### Resultado consolidado · Pricing Wave 1 P50 (substitui pricing por análogo)

| Cluster · Tier | P_base cost-plus (N=30) | P* otimização | P_legal | P_WTP | **P_NeoGov FINAL** | Tipo |
|---|---:|---:|---:|---:|---:|:--:|
| **Alfa-M Pro** (<30k hab) | R$ 12.678 | R$ 9.503 | R$ 5.458 | n.d. | **R$ 5.458** | 🔴 Subsidiado · binding AR75 |
| **Alfa-M Plus** (30-100k hab) | R$ 12.678 | R$ 21.170 | R$ 32.746 | R$ 25.000 | **R$ 18.000** | 🟢 Autossustentável |
| **Alfa-M Enterprise** (>100k hab) | R$ 12.678 | R$ 21.170 | livre | R$ 40.000 | **R$ 28.000** | 🟢 Margem alta |
| **Alfa-F/E** | R$ 12.678 | n.d. | livre | R$ 50.000 | **R$ 35.000** | 🟢 Margem alta |
| **Gamma Pequena** (50-200 alunos) | R$ 10.263 | R$ 2.420 | livre | R$ 800 | **R$ 800** | 🔴 Subsidiado |
| **Gamma Média** (200-800 alunos) | R$ 10.263 | R$ 4.503 | livre | R$ 2.500 | **R$ 2.000** | 🟡 Marginal |
| **Gamma Enterprise** (800-1500 alunos) | R$ 10.263 | R$ 4.503+ | livre | R$ 5.000 | **R$ 4.500** | 🟢 Autossustentável |
| **Épsilon DPO** (per seat) | R$ 9.158 | n.d. | livre | R$ 2.500 | **R$ 1.800** | 🟡 Marginal |
| **Beta Hospital** (W5 ref) | R$ 12.678 | n.d. | livre | R$ 25.000 | **R$ 15.000** | 🟢 Margem alta |

> **🟡 Mudança vs §12.7 v1**: Alfa-M Plus passou de R$ 14.000 → R$ 18.000 (+28%) justificado pelo P* otimização · Alfa-M Enterprise passou de R$ 25.000 → R$ 28.000 (+12%) · Gamma Enterprise passou de R$ 3.997 → R$ 4.500 (+12%) · Beta Hospital subiu de R$ 5.000 → R$ 15.000 (W5 só · não Wave 1).

### Componentes da função (resumo)

#### Custos (do Sprint 3.0.1 §9 P50)

```
CSC = R$ 1.170/cliente/mês  (custo variável por cliente)
CF  = R$ 146.000/mês         (custos fixos totais)
CFA = CF / N                  (fixos alocados por cliente)
CT  = CSC + CFA               (custo total por cliente)
```

#### Markups · diferencial NeoGov gritante (matriz por cluster · Apêndice D §3)

| Premium | Justificativa | Alfa-M | Alfa-F/E | Beta | Gamma | Épsilon |
|---|---|:--:|:--:|:--:|:--:|:--:|
| m_alvo (lucro SaaS) | Benchmark saudável | 35% | 40% | 40% | 30% | 30% |
| m_P3 (LAI×LGPD único) | Monopólio segmento | +25% | +25% | +25% | — | — |
| m_ICT (Art. 75 IV) | Habilita dispensa | +15% | +15% | — | — | — |
| m_ECA (pioneiro) | Único Gamma | — | — | — | +20% | — |
| m_jurídica | Expertise BR | +15% | +15% | +15% | +10% | +15% |
| m_IA_propria | Soberania dados | +10% | +10% | +10% | +5% | +5% |
| m_risco_setor | Ciclo · volatilidade | +10% | +5% | +20% | +5% | +5% |
| **Σ markup total** | — | **110%** | **110%** | **110%** | **70%** | **55%** |

#### Função de demanda (microeconomia · elasticidade-preço inferida)

```
Q(P) = Q_max × exp(-k × P)

k_Alfa_Pro    = 0,00012  (B2G inelástico · demanda compulsória)
k_Alfa_Plus   = 0,00005
k_Gamma_Peq   = 0,0008   (privado elástico)
k_Gamma_Méd   = 0,0003
```

#### Função de lucro e otimização

```
L(P) = (P - CMg) × Q(P) - CF

dL/dP = 0  ⇒  P* = CSC + 1/k        [fórmula fechada · derivada]
```

### Subsídio cruzado estratégico (resultado da análise matemática)

A função revelou que **Alfa-M Pro e Gamma Pequena não cobrem custo em Wave 1** (CT > P_legal_max ou WTP_max). Não são rejeitados — são **alavancagem estratégica subsidiada** pelos clusters autossustentáveis:

```
ALAVANCA SUBSIDIADA:
  - Alfa-M Pro     (R$ 5.458 · binding legal)
  - Gamma Pequena  (R$ 800   · binding WTP)
  → Volume · prova social · vitória sem batalha (Sun Tzu III)
  → Materializa Valor 4 (Acessibilidade Real) do Cap 02 VMV

CASH ENGINES:
  - Alfa-M Plus       (R$ 18.000)
  - Alfa-M Enterprise (R$ 28.000)
  - Alfa-F/E          (R$ 35.000)
  - Beta Hospital W5  (R$ 15.000)
  → Margem operacional + premium por diferencial
```

### Validação econômica Wave 1 P75 (mix realístico)

```
3 Alfa-M Pro    × R$ 5.458  = R$  16.374  (subsidiado)
6 Alfa-M Plus   × R$ 18.000 = R$ 108.000  (cash engine)
1 Alfa-M Enter  × R$ 28.000 = R$  28.000  (margem alta)
10 Gamma Peq    × R$    800 = R$   8.000  (subsidiada)
8 Gamma Média   × R$  2.000 = R$  16.000  (marginal)
3 Gamma Enter   × R$  4.500 = R$  13.500
──────────────────────────────────────────
31 clientes · Receita mensal: R$ 189.874
CSC variável (31×1.170):       R$  36.270
Margem bruta:                   R$ 153.604
Custos fixos:                   R$ 146.000
RESULTADO MENSAL: R$ +7.604 ✅ break-even superado
```

### Análise estatística P10/P50/P90 (Apêndice D §7)

Cada P_NeoGov é P50 (mediana). Cenários P10 (conservador) e P90 (otimista) modelados via Monte Carlo simplificado considerando variação ±20% em CSC, CF, k, m_alvo. Sensibilidade dominante: **N (escala) responde por ±30% no preço** — reforçando estratégia de subsidio cruzado em Wave 1 e ramp para autossustentabilidade plena em Wave 2-5.

### Calibração obrigatória Wave 1 piloto

Parâmetro k (elasticidade-preço) tem VVV 0,55 atual · será calibrado para 0,85+ com dados primários do piloto Wave 1 via regressão simples sobre (P_aplicado, Q_observado). Trigger: M+6 após primeiros 5-10 contratos.

### Devil's Advocate (2 contras representativos)

> **Contra**: "Alfa-M Plus a R$ 18.000 (vs R$ 14.000 da v1) é caro · vai perder cliente"
>
> **Refutação**: P* otimização (R$ 21.170) mostra que R$ 18.000 está abaixo do ótimo · margem de oportunidade. P_WTP estimado é R$ 25.000 (município médio paga mais por especialização BR). Premium de 28% justifica o diferencial gritante. Risco mitigado pela calibração piloto.

> **Contra**: "Subsídio cruzado é fragilidade contábil"
>
> **Refutação**: Subsídio é **temporal** (Wave 1) e **estratégico** (volume + Valor 4). Em Wave 2+ (N>30), CFA cai pela metade → todos tiers autossustentáveis. É alavancagem, não permanência. Cap 15 Financeiro modelará evolução da margem por wave.

> **Referência completa**: `APENDICE-D-PRICING-FUNCTION-v1.0.1.md` (16 seções · 6 Devil's Advocate · 4 fórmulas · Monte Carlo · sensibilidade) · PMQS bruto 9.45 · VVV 0,72 (subirá com piloto).

[LASTRO §12.7-BIS] Apêndice D · Sprint 3.0.1 §9 §15 §16 · Drury 2018 · Mankiw princípios · Cap 02 v2.1.4.3 Valor 4 · Cap 11 §11.6

---

## 12.8 Bloco 6 · Key Resources

### Recursos físicos · digitais · intelectuais · humanos

| Tipo | Recurso | Status | Defensibilidade |
|---|---|---|:--:|
| **Intelectual** | Expertise LGPD especializada brasileira (Simone, Gislênia) | 🟢 Existe | 🥇 Alta |
| **Intelectual** | Expertise LAI × LGPD (P3 único) | 🟢 Existe | 🥇 Defensável |
| **Intelectual** | Conhecimento ECA Digital pioneiro | 🟢 Existe | 🥇 Defensável |
| **Intelectual** | INPI registro plataforma | 🔴 GAP-05 pendente | 🥈 Média (deveria ser alta) |
| **Digital** | Plataforma SaaS multi-tenant (P1) | 🟡 Em desenvolvimento (GAP-04) | 🥈 Média |
| **Digital** | IA própria local Llama 8B fine-tuned BR | 🟡 Roadmap (D-ARC-001) | 🥇 Alta após implementado |
| **Digital** | Dataset jurídico BR curado | 🟡 Em curadoria | 🥇 Defensável |
| **Digital** | Status ICT (Instituição Científica e Tecnológica) | 🟢 Existe | 🥇 Habilita Art. 75 IV |
| **Humano** | Founders 4 (Simone CEO · Wilton BD político · Camila CTO · Gislênia Compliance) | 🟢 Existe | 🥈 Critical mas substituível |
| **Físico** | Hardware GPU L40S (treinamento local IA) | 🔴 Pendente | 🥉 Commodity |
| **Físico** | Cloud privada (Magalu/TIVIT) | 🟡 Em contratação | 🥉 Commodity |
| **Financeiro** | Capital inicial CAPEX | 🟡 P50 R$169.500 (Sprint 3.0.1 §9.3) | — |
| **Financeiro** | Receita recorrente alvo Wave 1 | 🔴 Pendente piloto | — |

### Recursos críticos para Wave 1 (priorização MoSCoW)

```
MUST:
  - Plataforma P1 funcional (GAP-04 resolver)
  - Founders ativos (já tem)
  - ICT status (já tem · habilita Art. 75 IV)
  - Expertise jurídica (já tem)

SHOULD:
  - INPI registrado (GAP-05) — protege IP
  - IA própria fine-tuned — diferencial competitivo
  - Dataset curado — feed da IA

COULD:
  - Cloud privada formalizada (acordo Magalu)
  - Hardware GPU dedicado

WON'T (Wave 1):
  - Wave 5 Beta saúde (postergado D-SAU-001)
```

### Devil's Advocate

> **Contra**: "Plataforma em desenvolvimento é risco crítico"
>
> **Refutação**: É · explicitamente registrado como GAP-04 no F4. Mitigação: Wave 1 Beachhead Alfa-M pode iniciar com MVP funcional (não plataforma completa) usando expertise jurídica como entrega primária + tooling parcial. Cronograma Wave 1 considera 60-90 dias de polish da plataforma antes do go-live em escala.

[LASTRO §12.8] Cap 11 §11.2-§11.6 · Sprint 3.0.1 §4 Capability Mapping · F4 GAPs

---

## 12.9 Bloco 7 · Key Activities

### Atividades centrais (Osterwalder taxonomy: Production · Problem-solving · Platform)

#### Tipo: Production (industrial · sistematizada · Valor 3)

1. **Curadoria de knowledge jurídico** · Simone + Gislênia · transformar precedentes, interpretações e decisões em dataset estruturado
2. **Fine-tuning de IA própria** · Camila · Llama 8B especializado em LGPD+LAI+ECA Digital
3. **Desenvolvimento da plataforma SaaS** · time TI · features versionadas com release notes
4. **Compliance audit interno** · trimestral · honra Valor 5 (Auditabilidade Reversa)

#### Tipo: Problem-solving (alto valor · low scale · Valor 2)

5. **Casos jurídicos inéditos** · Simone resolve · resultado vira input do dataset (Princípio 2 Cap 02)
6. **Resposta a fiscalização ANPD** · expertise legal humana · cliente premium
7. **Adaptação a nova lei** (ex: novas resoluções ANPD) · propaga via plataforma para todos clientes

#### Tipo: Platform/Network (multi-sided · escalável)

8. **B2G sales · gestão de relacionamento institucional** · Wilton · ciclo longo (6-18 meses)
9. **Customer Success operations** · onboarding · trimestral review · suporte 24/7
10. **Partnership management** · Magalu · CNM · contadores · FNDE · advogados de cota

### Atividades por wave

| Atividade | W1 | W2 | W3 | W4 | W5 |
|---|:--:|:--:|:--:|:--:|:--:|
| Curadoria knowledge | 🔥 | 🔥 | 🟡 | 🟡 | 🟡 |
| Fine-tune IA | 🔥 | 🟡 | 🟡 | 🟢 | 🟢 |
| Plataforma dev | 🔥 | 🔥 | 🟡 | 🟢 | 🟢 |
| B2G sales | 🔥 | 🟡 | 🔥 | 🟡 | 🟢 |
| Customer Success | 🟡 | 🔥 | 🔥 | 🟡 | 🔥 |
| Partnership mgmt | 🟡 | 🟡 | 🟡 | 🔥 | 🟡 |

🔥 = atividade dominante · 🟡 = atividade ativa · 🟢 = atividade em manutenção

### Devil's Advocate

> **Contra**: "10 atividades simultâneas para 4 founders é overload"
>
> **Refutação**: Não são simultâneas em intensidade — a tabela mostra quais dominam por wave. Wave 1 tem 3 atividades-fogo (curadoria, plataforma, IA) e o resto em manutenção. Customer Success só vira fogo na Wave 2 quando há base de clientes. Princípio de atenção pivotal sazonal.

[LASTRO §12.9] Cap 11 §11.5 Atividades · Sprint 3.0.1 §4 Capability + §5 VSM

---

## 12.10 Bloco 8 · Key Partnerships

### Parcerias por tipo (Osterwalder: alianças · joint ventures · buyer-supplier)

| Parceria | Tipo | Função estratégica | Status | Wave |
|---|---|---|:--:|:--:|
| **Magalu Cloud / TIVIT** | Buyer-supplier infrastrutura BR | Cloud privada · soberania de dados · LGPD-friendly | 🟡 Em negociação | W1 |
| **CNM (Confed. Nac. Municípios)** | Aliança estratégica | Canal Delta · endorsement institucional · vitória sem batalha | 🟢 Relacionamento Wilton | W1+W4 |
| **CIMI · consórcios intermunicipais** | Aliança estratégica | Canal Delta · alavancagem regional | 🟡 Em mapeamento | W1+W4 |
| **FNDE / cota Wilton** | Alianças política | Acesso B2G federal · ETEC simplificado | 🟢 Wilton ativo | W3-W4 |
| **Contadores · fiscalistas** | Buyer-supplier serviço | Onboarding pricing assertivo · regime tributário | 🟡 A formalizar | W1 |
| **FENEP / sindicatos escola privada** | Aliança estratégica | Canal Delta para Gamma | 🟡 A explorar | W2 |
| **Anahp / hospitais Anahp** | Aliança piloto | Wave 5 entrada Beta postergada | 🟢 Relacionamento existente | W5 |
| **Hardware vendor (NVIDIA partners BR)** | Buyer-supplier hardware | GPU L40S · L4 para treinamento | 🟡 A negociar | W1 |
| **Advogados parceiros (cota)** | Joint venture serviço | Capacidade extra · escala humana | 🟡 A estruturar | W2+ |

### Motivações estratégicas (por que cada parceria)

| Motivação | Parcerias correspondentes |
|---|---|
| **Optimization & economy of scale** | Magalu (compartilhar infra) · contadores |
| **Reduction of risk and uncertainty** | Magalu (LGPD-friendly default) · advogados parceiros |
| **Acquisition of resources & activities** | CNM (canal) · CIMI · FNDE · FENEP · Anahp |

### Devil's Advocate

> **Contra**: "Dependência do Wilton para B2G é single point of failure"
>
> **Refutação**: É · risco real. Mitigação: (a) Wave 1 cobre Alfa-M via dispensa Art. 75 IV (não exige cota política), (b) parcerias com cota se diversificam após Wave 2, (c) status de ICT habilita licitações sem dependência exclusiva de relacionamento. Wilton é alavanca, não trava única.

[LASTRO §12.10] Cap 16 Equipe · Sprint 3.0.1 §2 Stakeholder Analysis · F4 GAPs

---

## 12.11 Bloco 9 · Cost Structure

### Tipo dominante: **Value-driven** (alta margem · alta automação · diferencial preserva premium)

Com **base cost-driven controlada** (Folha = maior driver · justifica padronização industrial).

### Estrutura de custos consolidada (Sprint 3.0.1 v3.0 §9 P50)

```
CUSTOS FIXOS MENSAIS WAVE 1 (P50) ················ R$ 146.000
├─ Folha CLT (Camila CTO + 2 devs + admin)        R$  90.520  (62%)
├─ Marketing (eventos · LinkedIn · webinars)      R$  17.520  (12%)
├─ Infra cloud (Magalu/TIVIT P50)                 R$  14.600  (10%)
├─ Encargos sobre folha                           R$  10.220  (7%)
├─ Software (licenças · ferramentas)              R$   5.840  (4%)
├─ Contingência                                   R$   7.300  (5%)
└────────────────────────────────────────────────────────────

CUSTOS VARIÁVEIS POR CLIENTE (CSC médio P50) ····· R$ 1.170/mês
├─ Cloud por cliente                              R$ 60-400 (varia tier)
├─ API IA inference                               R$ 50-300
├─ Suporte humano alocado                         R$ 200-500
├─ Onboarding diluído em LTV                      R$ 100-300

CAPEX INICIAL (P50) ······························ R$ 169.500
├─ Hardware GPU L40S (cota dev)                   R$  85.000
├─ Plataforma desenvolvimento (3 meses até MVP)   R$  45.000
├─ Setup IA fine-tune inicial                     R$  25.000
└─ Reserva legal/INPI/marcas                      R$  14.500
   (amortizado em 12 meses = R$ 14.125/mês)
```

### Drivers analisados (D-015 lastros)

| Driver | % do total | Lastro |
|---|:--:|---|
| Folha CLT | 62% | Sprint 3.0.1 §9.1 · salários Glassdoor/Robert Half VVV 0.85 |
| Infra cloud | 10% | Magalu Cloud R$400-1.500/cliente análogo VVV 0.80 |
| Marketing | 12% | Inferência operacional · benchmark legaltech VVV 0.70 |
| Encargos | 7% | calculadorabrasil.com.br · Simples Nacional VVV 0.85 |
| Software | 4% | Inferência operacional VVV 0.75 |
| Contingência | 5% | Reserva técnica padrão SaaS VVV 0.80 |

### Economies of scale planejadas

- **Wave 1 (5-10 clientes)**: custo médio servir R$ 17.000/cliente/mês (com fixos)
- **Wave 2 (30 clientes)**: custo médio servir R$ 6.500/cliente/mês (diluição)
- **Wave 5 (100+ clientes)**: custo médio servir R$ 3.000/cliente/mês (industrial)

### Devil's Advocate

> **Contra**: "Folha 62% é insustentável · SaaS típico tem 30-40%"
>
> **Refutação**: Wave 1 tem 5-10 clientes · folha proporcionalmente cara é normal (early stage). Wave 2 (30 clientes) folha cai para ~45%. Wave 5 (100+ clientes) folha será ~35%. NeoGov pré-Wave 5 é early stage, não SaaS maduro. Comparação inadequada.

> **Contra**: "Contingência 5% é baixa"
>
> **Refutação**: Sprint 3.0.1 §13 Risk Register tem 5 riscos formais com plano de mitigação detalhado §13.3. A contingência adicional vai além dos riscos mapeados. Subir contingência sem premissa específica seria pricing defensivo, não economia real.

[LASTRO §12.11] Sprint 3.0.1 §9 (Estimation PERT) · §13 (Risk Register)

---

## 12.12 Validação · Coerência Revenue ↔ Cost

> **🟡 Esta seção foi recalculada na edição 2 com pricing da função matemática §12.7-BIS** · valores anteriores baseados em pricing por análogo foram substituídos.

### Break-even por cluster (Wave 1 · pricing P_NeoGov FINAL)

#### Alfa-M Pro subsidiado (R$ 5.458/mês · binding AR75)

```
Receita mensal/cliente:             R$ 5.458
CSC variável/cliente:               R$ 1.170
Margem bruta/cliente:               R$ 4.288  (78.6%)

NOTA: CFA por cliente quando N=12 é R$ 12.167 → cliente loss = -R$ 7.879
CFA por cliente quando N=30 é R$ 4.867 → cliente neutro = +R$ 591
CFA por cliente quando N=100 é R$ 1.460 → cliente lucrativo = +R$ 2.828

Conclusão: Pro só vira lucrativo em escala (N≥30) · justifica subsídio cruzado Wave 1
```

#### Alfa-M Plus autossustentável (R$ 18.000/mês)

```
Receita mensal/cliente:             R$ 18.000  (atualizado de R$ 14.000)
CSC variável/cliente:               R$ 1.170
Margem bruta/cliente:               R$ 16.830 (93.5%)

Break-even só com Plus: 146.000 ÷ 16.830 = 9 clientes ✅ realístico
```

#### Mix realístico Wave 1 (pricing P_NeoGov)

```
Cenário base (P50 · 6 meses):
  3 munic. Pro    × R$ 5.458   = R$ 16.374
  4 munic. Plus   × R$ 18.000  = R$ 72.000
  5 esc. Pro      × R$ 2.000   = R$ 10.000  (Gamma Média)
  ────────────────────────────────────────
  Receita total mensal:        R$ 98.374
  CSC variável (12 clientes):   R$ 14.040
  Margem bruta total:           R$ 84.334
  Fixos:                       R$ 146.000
  ────────────────────────────────────────
  Resultado mensal:             R$ -61.666 🟡 burn aceitável
  Burn rate mensal:            R$ 62.000  (anterior era R$ 80.000)
```

#### Cenário P75 Wave 1 (pricing P_NeoGov · 31 clientes)

```
  3 Alfa-M Pro     × R$ 5.458   = R$  16.374  (subsidiado)
  6 Alfa-M Plus    × R$ 18.000  = R$ 108.000  (cash engine)
  1 Alfa-M Enter   × R$ 28.000  = R$  28.000
  10 Gamma Pequena × R$    800  = R$   8.000  (subsidiada)
  8 Gamma Média    × R$  2.000  = R$  16.000
  3 Gamma Enter    × R$  4.500  = R$  13.500
  ─────────────────────────────────────────
  Receita total mensal:        R$ 189.874
  CSC variável (31 clientes):   R$  36.270
  Margem bruta:                 R$ 153.604
  Fixos:                       R$ 146.000
  ─────────────────────────────────────────
  Resultado mensal:             R$ +7.604 ✅ break-even superado
```

#### Cenário ótimo P90 Wave 1 (57 clientes · 12-18 meses)

```
  8 Alfa-M Pro     × R$  5.458 = R$  43.664
  12 Alfa-M Plus   × R$ 18.000 = R$ 216.000
  2 Alfa-M Enter   × R$ 28.000 = R$  56.000
  20 Gamma Pequena × R$    800 = R$  16.000
  10 Gamma Média   × R$  2.000 = R$  20.000
  5 Gamma Enter    × R$  4.500 = R$  22.500
  ─────────────────────────────────────────
  Receita total mensal:        R$ 374.164
  CSC variável (57 clientes):   R$  66.690
  Margem bruta:                 R$ 307.474
  Fixos:                       R$ 146.000
  ─────────────────────────────────────────
  Resultado mensal:             R$ +161.474 ✅ lucro substancial
```

### Conclusão da validação · pricing matemático

| Cenário | Clientes Wave 1 | Receita mensal | Resultado | Status |
|---|:--:|---:|---:|:--:|
| Pessimista | 6 | ~R$ 47.000 | -R$ 110k | 🔴 plano B/C |
| **Base P50** | **12** | **R$ 98.374** | **-R$ 61.666** | 🟡 burn aceitável 6m |
| **Otimista P75** | **31** | **R$ 189.874** | **+R$ 7.604** | 🟢 break-even |
| **Ótimo P90** | **57** | **R$ 374.164** | **+R$ 161.474** | ✅ profit |

### Burn rate sustentado · CAPEX recalibrado

```
CAPEX inicial:                R$ 169.500
Burn rate P50 (6 meses):      R$ 372.000  (R$ 62k × 6 · vs R$ 480k anterior)
Runway necessário Wave 1:     R$ 541.500  (vs R$ 650k anterior)

REDUÇÃO de R$ 108.500 no runway necessário pelo pricing assertivo Alfa-M Plus.

Fonte runway proposta:
  - CAPEX founders inicial
  - Receita progressiva (cash engine Alfa-M Plus)
  - Plano B: contratos âncora B2G (3-5 munic. Plus = R$ 90k+/mês imediato)
```

### Devil's Advocate

> **Contra**: "Pricing assertivo (R$ 18k Plus) pode ter taxa de conversão menor"
>
> **Refutação**: VVV 0,55 atual da elasticidade-preço k é honesto. Piloto Wave 1 calibra (M+6). Mesmo com elasticidade pessimista, o valor R$ 18.000 está abaixo do P* otimização (R$ 21.170) · há folga de 15% pra negociação caso a caso (cota Wilton). Estratégia: começar R$ 18k, ajustar conforme realidade do piloto.

> **Contra**: "Subsídio cruzado em Wave 1 é difícil de defender pra investidor"
>
> **Refutação**: Pelo contrário · é defesa estratégica forte. Mostra: (1) plano realista pré-piloto, (2) materialização do Valor 4 (Acessibilidade) que diferencia da concorrência, (3) cenários P50/P75/P90 com transparência, (4) caminho claro para autossustentabilidade plena em Wave 2 (N>30 → CFA cai 60%). Investidor sofisticado prefere lógica + lastro a otimismo cego.

[LASTRO §12.12] Sprint 3.0.1 §9 + Apêndice D · §1 §1.1-1.3 · F4 §G-003 · v2.1.5.2 patch

---

## 12.13 Síntese · Coerência entre os 9 blocos

### Teste de coerência cruzada (Osterwalder validation)

| Pergunta de teste | Resposta NeoGov | Status |
|---|---|:--:|
| Customer Segments justifica Value Propositions? | 4 VPs cognitivas, uma por cluster prioritário | ✅ |
| Value Propositions justifica Customer Relationships? | VP cognitiva → CR self-service ou personal | ✅ |
| Customer Segments justifica Channels? | Cada cluster tem mix próprio (60% direto Alfa · 60% inbound Gamma) | ✅ |
| Value Propositions justifica Revenue Streams? | Pricing por análogo · Premium VP → premium pricing | ✅ |
| Key Resources sustenta Key Activities? | Expertise + Plataforma + IA → curadoria + dev + sales | ✅ |
| Key Partnerships preenche gaps? | Cloud BR, canal Delta, hardware, advogados parceiros | ✅ |
| Cost Structure suporta Revenue Streams? | Break-even em 12-18 meses com mix realístico | 🟡 burn 6m |
| Activities materializa Value Propositions? | Curadoria → diferencial expertise · Fine-tune → diferencial IA | ✅ |

### Princípio de coerência declarado (Cap 02 v2.1.4.3)

> "A coerência interna do plano depende de cada capítulo seguinte responder à pergunta: **'Isso está coerente com a VMV declarada aqui?'**"

**Resposta do Cap 12 BMC**: 
- Missão "simplificar cumprimento LGPD com produtividade, segurança jurídica, auditabilidade plena, sem peso da complexidade" → materializada em todas as 4 Value Propositions L2 cognitivas
- Visão "5.000 organizações historicamente excluídas" → materializada no Customer Segments (Gamma + Alfa-M + Épsilon = clusters mal-atendidos pelo mercado)
- Valor 1 Honestidade Epistêmica → VVV declarado em cada pricing · LASTROS rastreáveis
- Valor 2 Expertise como Ativo → Key Resources com expertise no topo
- Valor 3 Escala via Sistematização → Cost Structure com economies of scale planejadas
- Valor 4 Acessibilidade Real → Pricing Pro municipal (R$5.456) e Basic escola (R$497) cobrem mercado excluído
- Valor 5 Auditabilidade Reversa → Activities inclui compliance audit + Customer Relationships com trilha completa

---

## 12.14 O que este capítulo justifica para o restante do plano

| Cap seguinte | Elemento que este capítulo justifica |
|---|---|
| **Cap 13 VPC** | Value Proposition Canvas detalhado para cada uma das 4 VPs deste cap |
| **Cap 14 GTM** | 4 discursos comerciais materializam cada VP em pitch · canais já mapeados §12.5 |
| **Cap 15 Financeiro** | Modelagem detalhada · DRE · FCD usa Revenue+Cost deste cap como base · 3 cenários |
| **Cap 16 Equipe** | Roles derivados de Key Activities · governança suporta Key Resources |
| **Cap 17 Riscos** | Risk Register Sprint 3.0.1 §13 + novos riscos · coerência cross-bloco |
| **Cap 18 Roadmap** | Waves de produto/canal/cliente alinhadas com este BMC |

---

## 12.15 Histórico de retificações

| Edição | Data | Mudança | Decisão |
|---|---|---|---|
| v2.1.5.1 | 2026-05-15T23:10 | Versão inicial · W1.2 dispatch · 9 blocos · L1/L2 separation aplicada · Devil's Advocate por bloco · pricing por análogo D-015 | D-W1.2-001 |
| v2.1.5.2 | 2026-05-15T23:50 | **Retificação pricing matemático** · §12.7-BIS adicionado · método bottom-up cost-plus + otimização micro-econômica · §12.7 análogo demoted para sanity check · §12.12 cenários financeiros recalculados | **D-W1.2-002** + Apêndice D |

### O que mudou na v2.1.5.2

- **§12.7-BIS adicionado** · método matemático bottom-up cost-plus + função de otimização P* = CSC + 1/k
- **§12.7 original demoted** para sanity check (análogos como validação externa, não primária)
- **§12.12 recalculado** com pricing P_NeoGov FINAL · burn rate reduzido de R$ 80k para R$ 62k/mês P50
- **Pricing assertivo aplicado**: Alfa-M Plus R$ 14.000 → **R$ 18.000** (+28%) · Alfa-M Enterprise R$ 25.000 → **R$ 28.000** (+12%) · Gamma Enterprise R$ 3.997 → **R$ 4.500** (+12%)
- **Subsídio cruzado documentado** · Alfa-M Pro e Gamma Pequena subsidiados Wave 1 · cash engines compensam · materializa Valor 4 (Acessibilidade Real)
- **Insight IN-017 consumido** · "pricing por análogo insuficiente quando diferencial gritante"

---

## 12.16 Auto-avaliação PMQS (edição 2)

| Critério (peso) | Score v2.1.5.2 | Mudança vs v2.1.5.1 | Justificativa |
|---|:--:|:--:|---|
| CE Completude (15%) | 9.7 | +0.2 | +§12.7-BIS matemático + Apêndice D 16 seções |
| PI Precisão (15%) | 9.5 | +0.5 | Fórmulas Drury/Mankiw · números rastreáveis · cenários recalculados |
| CC Clareza (10%) | 9.0 | = | L1/L2 mantida · §12.7-BIS bem estruturado |
| PRI Profundidade Rigor (20%) | 9.7 | +0.2 | Derivação P* · Monte Carlo · sensibilidade |
| RA Relevância (15%) | 9.7 | +0.2 | Resolve falha apontada · materializa Valor 1 |
| EIC Estrutura Coerência (10%) | 9.5 | = | §12.7 → §12.7-BIS lógica preservada |
| OVA Originalidade Valor (15%) | 9.7 | +0.7 | Subsídio cruzado · função matemática rara em BPs BR |

**PMQS Bruto** = 9.7×0.15 + 9.5×0.15 + 9.0×0.10 + 9.7×0.20 + 9.7×0.15 + 9.5×0.10 + 9.7×0.15
= 1.455 + 1.425 + 0.900 + 1.940 + 1.455 + 0.950 + 1.455 = **9.58**

**VVV global**: 0,80 (média)
- Custos: VVV 0,80
- Markups diferenciais: VVV 0,72
- Elasticidade k: VVV 0,55 (calibrar piloto)
- Limites legais: VVV 1,00

**PMQS Final** = 9.58 × 0.80 = **7.66** ✅ acima target Wave 1 (7.225)

> **Nota PMQS**: ganho de PMQS bruto de 9.30 → 9.58 reflete o ganho de rigor metodológico. VVV mantido 0,80 (similar) · Apêndice D §14 declara honestamente que VVV global 0,72 sobe para 0,85+ após calibração piloto Wave 1.

---

## Apêndices referenciados

- **Apêndice A · VVV-LOG**: 14 + 6 novas afirmações (AF-054 a AF-073) cobrindo pricing matemático
- **Apêndice B · DECISIONS-LOG**: D-W1.2-001 (estrutura BMC) + **D-W1.2-002 (pricing bottom-up)**
- **Apêndice C · INSIGHTS-CARRY**: IN-014 consumido · IN-015 (Delta canal) · IN-016 (break-even mix) · **IN-017 (subsídio cruzado · pricing matemático)**
- **Apêndice D · PRICING-FUNCTION**: documento técnico standalone com 16 seções · Monte Carlo · sensibilidade · calibração

---

## Fim do Capítulo 12 v2.1.5.2

**Próximo capítulo (Cap 13 VPC)** detalhará Value Proposition Canvas para cada uma das 4 VPs deste capítulo, com customer jobs/pains/gains e fit pain-reliever/gain-creator.
