---
id: NEOGOV-V21-CAP-07-PERSONAS
filename: 07-personas-v2.1.2.1.md
created_at: 2026-05-14
type: BP_CHAPTER
sprint: S1.2
edicao: 1
parent_doc: BUSINESS-PLAN-FINAL-v2.1
chapter_number: 7
fdcu_score: 9.2
pmqs_target: 9.5
vvv_target: 0.85
abordagem: B_fichas_profundas_canvas
referencia_capitulos: [04, 11, 13, 14]
tags: [personas, empathy-map, jtbd, pov, design-thinking, decisores]
---

# Capítulo 7 · Personas — As 4 Pessoas que Decidem a Compra

> "Persona não é segmento. Persona é uma pessoa específica com cargo, dor, gatilho e ciclo próprios."

## 7.1 Por que este capítulo

O Capítulo 4 estabeleceu Design Thinking como lógica geradora. Este capítulo executa a fase **Empathize** com dados primários — produzindo os quatro empathy maps que sustentam toda a estratégia comercial. Cada persona aqui descrita gerará, no Capítulo 13 (Value Proposition Canvas), o mapeamento direto para Pain Relievers e Gain Creators.

A premissa do capítulo é simples: produtos genéricos vendem para "segmentos". Produtos especializados vendem para **decisores específicos**, cada um com motivação própria. A NeoGov vai para o mercado com discurso diferente para cada uma das quatro personas — não com pitch unificado [DECISÃO D-003 herdada · DECISÃO D-006 nesta produção].

## 7.2 Por que 4 personas (e não mais nem menos)

Durante a produção do Capítulo 4, identifiquei que originalmente estavam previstas 5 personas (incluindo "Subsecretário Federal de TIC" separado). A análise revelou que CIO estadual e Subsecretário federal compartilham estrutura de dor — variando apenas o nível governamental e o ciclo de decisão. Consolidá-los em uma persona "Gestor B2G estadual/federal" preserva precisão sem inflacionar artificialmente [INSIGHT IN-001 do Apêndice C · consumido neste sprint].

A redução para 4 personas tem outra virtude: cada persona ocupa uma posição inequívoca no funil estratégico [INFERÊNCIA derivada do mapeamento]:

| # | Persona | Cluster BP | Wave | Posição estratégica |
|---|---|---|---|---|
| 1 | Procurador municipal | Alfa | W1 | Motor de caixa atual |
| 2 | Gestor B2G estadual/federal | Alfa-E/Alfa-F | W2C | Expansão B2G declarada |
| 3 | Diretor administrativo hospitalar | Beta | W2A (gate PoC M4) | Condicional técnico |
| 4 | Mantenedor escolar | Gamma | W2B paralela | Oceano azul crítico |

A regra operacional decorre: **toda decisão comercial deste plano deve ser localizada em ao menos uma dessas quatro personas**. Se uma iniciativa não responde à dor de nenhuma das quatro, ela está fora de escopo.

## 7.3 Como ler cada persona

Cada uma das quatro subseções seguintes apresenta:

1. **Identidade** — cargo, contexto operacional, faixa demográfica
2. **Empathy Map canônico** — Says / Thinks / Does / Feels / Pains / Gains
3. **JTBD statement** — o job-to-be-done na voz da persona
4. **POV statement** — a tradução estruturada da dor
5. **Insight surpreendente** — o achado contraintuitivo que muda o discurso comercial
6. **Mapeamento para produtos** — quais dos 5 produtos NeoGov atacam quais dores

A estrutura é idêntica nas quatro personas — facilitando comparação direta e renderização modular no aplicativo interativo (`<PersonaCard>` Vue).

---

## 7.4 Persona 1 · Procurador Municipal (Cluster Alfa)

### Identidade

| Campo | Valor |
|---|---|
| Cargo | Procurador-Geral do Município (ou advogado da PGM) |
| Contexto | Municípios 20k-100k habitantes (faixa onde a metodologia NeoGov já opera) |
| Decisor real | Procurador (não prefeito) [FATO — transcrição reunião] |
| Influenciadores | Secretário de Administração · Controle Interno |
| Aprovador final | Prefeito (via dispensa Art. 75 IV) |

### Empathy Map

**Diz (Says)**
- "Sou obrigado por lei a ter LGPD."
- "Não tenho orçamento, prefiro terceirizar."
- "Preciso ver retorno político nisso."
- "Meu procurador entende isso?"

**Pensa (Thinks)**
- "Não quero ir preso por improbidade."
- "Como isso vai aparecer na imprensa local?"
- "Se TCE me notificar, o que respondo?"
- "Já viram cidade vizinha pagar processo?"

**Faz (Does)**
- Espera notificação TCE/MP ou auditoria para reagir
- Delega execução para TI municipal ou jurídico interno
- Compra via dispensa de licitação (Art. 75 IV) ou emendas parlamentares
- Consulta consórcios intermunicipais para diluir custo

**Sente (Feels)**
- Ansioso com risco pessoal de improbidade
- Aliviado quando vê solução "chave na mão"
- Cético com consultoria cara que entrega papelada
- Pressionado por início de mandato (zerar passivo herdado)

### Pains

| Dor | Severidade | Origem |
|---|---|---|
| Responsabilização pessoal por improbidade administrativa | ALTA | LGPD + Lei de Improbidade |
| Orçamento limitado (R$600k-bloqueio) | ALTA | Realidade fiscal municípios médios |
| Ciclo de licitação tradicional de 12 meses | ALTA | Lei 14.133 caminho convencional |
| Ausência de servidor técnico LGPD interno | MÉDIA | Realidade operacional |
| Conflito LAI × LGPD diário (publicar Diário Oficial) | MÉDIA | Operação de transparência |

### Gains

| Ganho desejado | Importância | Como mensurar |
|---|---|---|
| Tranquilidade jurídica (blindagem pessoal) | ALTA | Ausência de TCE/MP notificações |
| Capital político visível (cidade transparente) | ALTA | Relatório TCE-friendly mensal |
| Custo mensal acessível (< limite Art. 75 IV) | ALTA | R$ orçamento × 12 ≤ R$65.492 |
| Sem licitação longa | ALTA | Contrato em 2-8 semanas |
| Visibilidade de progresso (dashboard) | MÉDIA | Painel para o procurador |

### JTBD (Job-to-Be-Done)

> "Me ajude a **não ser responsabilizado pessoalmente** por violação LGPD — de forma rápida, barata e sem processo licitatório longo."

### POV Statement

> Gestor público municipal **precisa de** conformidade LGPD contratável sem licitação longa **porque** teme responsabilização pessoal e busca retorno político visível.

### Insight Surpreendente · O que muda o discurso comercial

A dor **não é a multa LGPD**. O Art. 52 §3° da LGPD isenta o setor público de multa pecuniária [FATO — Lei 13.709/2018 · AF-004]. A dor é a **responsabilização pessoal por improbidade administrativa** — perda de cargo, inelegibilidade, processo civil pessoal contra o agente público.

**Implicação para a venda:** abandonar discurso "evite multa LGPD". Adotar discurso "blindagem pessoal do gestor + capital político da cidade transparente". Esse pivô discursivo é a diferença entre pitch genérico e pitch que ressoa.

### Mapeamento para os 5 produtos NeoGov

| Produto | Como ataca dores do Procurador |
|---|---|
| P1 Plataforma LGPD SaaS | Dashboard de compliance auditável por TCE — capital político visível |
| P2 Data Discovery automatizado | Resolve "não sei onde estão meus dados" em dias, não meses |
| P3 Anonimização LAI/LGPD ★ | Resolve conflito diário "publicar sem expor" — gargalo invisível mais relevante |
| P4 AI-DPO Copilot | DPO-as-a-service viável para município sem orçamento para DPO humano |
| P5 ETL/Middleware | Conecta e-Cidade · TCE · sistemas municipais — switching cost alto |

### Gatilhos de compra (sales triggers)

1. Notificação TCE ou MP por LGPD/LAI
2. Início de mandato (zerar passivos LGPD herdados)
3. Vazamento em município vizinho (efeito demonstração)
4. Auditoria TCU expandida 2024 via Rede Integrar
5. Demanda popular por transparência pós-eleição

### Ciclo e canal

| Atributo | Valor |
|---|---|
| Ciclo de decisão | 4-9 meses (Art. 75 IV reduz para 2-8 semanas) |
| Canal primário | Consórcios intermunicipais (1 contrato → N municípios) |
| Canal secundário | FNDE · emendas parlamentares (Wilton) |
| Ticket médio estimado | R$ 8.000-15.000/mês [INFERÊNCIA — pricing entry-level + Art. 75 IV] |

---

## 7.5 Persona 2 · Gestor B2G Estadual/Federal (Cluster Alfa-E/Alfa-F)

### Identidade

| Campo | Valor |
|---|---|
| Cargo | CIO de Secretaria Estadual ou Subsecretário Federal de TIC |
| Contexto | Órgãos com múltiplos sistemas legados heterogêneos |
| Decisor real | CIO + Procurador Geral do Estado (PGE) |
| Influenciadores | Secretário/Ministro · Controladoria · DPO institucional |
| Aprovador final | Governador/Ministro via ETEC ou licitação |

### Empathy Map

**Diz (Says)**
- "TCU já nos auditou em LGPD."
- "Precisamos de sistema integrado — não mais um silo."
- "Temos sistemas legados de décadas."
- "Big4 cobre caro e não entende governo."

**Pensa (Thinks)**
- "Temos volume muito maior que prefeitura — risco proporcionalmente maior."
- "ANPD vai priorizar o setor público em 2026-2027."
- "Serpro/Dataprev podem ser preferíveis politicamente."
- "Boutiques rasas não escalam para nossa complexidade."

**Faz (Does)**
- Licitações via ETEC ou CPSI (caminhos rápidos)
- Contratos maiores e mais complexos que municipais
- Coordena múltiplas secretarias com sistemas distintos
- Engaja TCU/CGU em discussões prévias para validar abordagem

**Sente (Feels)**
- Pressionado por TCU (76,7% órgãos federais inexpressivos) [AF-003]
- Frustrado com soluções genéricas sem foco B2G
- Desconfortável com vendor lock-in de fornecedor único
- Motivado pela janela ANPD 2026-2027 [AF-005]

### Pains

| Dor | Severidade | Origem |
|---|---|---|
| Sistemas legados heterogêneos sem integração | ALTA | Décadas de TI fragmentada |
| Múltiplas regulações simultâneas (LAI + LGPD + transparência + ECA) | ALTA | Complexidade jurídica B2G |
| Big4 caro · boutique raso | ALTA | Mercado polarizado |
| Ciclo de licitação tradicional 9-18 meses | ALTA | Lei 14.133 |
| Concorrência interna com Serpro/Dataprev | MÉDIA | Política institucional |

### Gains

| Ganho desejado | Importância | Como mensurar |
|---|---|---|
| Solução B2G integrada (LAI+LGPD+ECA) | ALTA | Cobertura legislativa documentada |
| Data discovery automático em massa | ALTA | Horas economizadas vs entrevistas |
| Anonimização LAI/LGPD automática | ALTA | % documentos públicos tarjados |
| AI-DPO que escala para volume estadual | ALTA | Atendimentos titular automatizados |
| Conformidade TCU comprovável | ALTA | Relatório TCU-ready trimestral |

### JTBD

> "Me ajude a **provar conformidade LGPD para o TCU e ANPD** sem contratar Big4 e sem sistemas genéricos que não entendem governo."

### POV Statement

> Gestor de órgão estadual ou federal **precisa de** solução LGPD que entenda especificidade B2G (LAI, transparência, sistemas legados) **porque** Big4 cobra mal e soluções genéricas não servem para governo.

### Insight Surpreendente · O que muda o discurso comercial

O que diferencia **não é capacidade técnica genérica** — é fluência na intersecção **LAI × LGPD** e familiaridade com sistemas legados governamentais. Concorrentes Big4 sabem auditoria mas não automação. SaaS internacionais (OneTrust, TrustArc) sabem produto mas não LAI brasileira [INFERÊNCIA — VVV-GAP-RESEARCH].

**Implicação para a venda:** o pitch para essa persona é **"somos a única solução que entende LAI brasileira + LGPD + automação no mesmo produto"**. Esse posicionamento elimina simultaneamente Big4 (genérica) e SaaS internacional (sem LAI). Diferenciação inequívoca.

### Mapeamento para os 5 produtos NeoGov

| Produto | Como ataca dores do Gestor B2G |
|---|---|
| P3 Anonimização LAI/LGPD ★ | **Produto-âncora** · resolve conflito LAI×LGPD em volume estadual |
| P2 Data Discovery automatizado | Inventário em sistemas legados heterogêneos |
| P4 AI-DPO Copilot | Atendimento titular em volume governamental |
| P5 ETL/Middleware | Integração com sistemas legados (SEI, SIAFI, etc.) |
| P1 Plataforma LGPD SaaS | Camada base auditável por TCU |

### Gatilhos de compra

1. Auditoria CGU ou TCU (TCU Acórdão 1.384/2022 e auditoria 2024)
2. Início de gestão (zerar passivos)
3. ANPD Mapa 2026-2027 priorizando poder público [AF-005]
4. ECA Digital vigente afetando secretarias de educação estadual
5. Vazamento em outro órgão (efeito demonstração)

### Ciclo e canal

| Atributo | Valor |
|---|---|
| Ciclo de decisão | 9-18 meses tradicional · 3-6 meses via ETEC/CPSI |
| Canal primário | ETEC (piloto Art. 75 IV) → licitação expansão |
| Canal secundário | Articulação política via FNDE/Wilton |
| Ticket médio estimado | R$ 30.000-80.000/mês [INFERÊNCIA — gap pricing R$3.5k-R$55k] |

---

## 7.6 Persona 3 · Diretor Administrativo Hospitalar (Cluster Beta)

### Identidade

| Campo | Valor |
|---|---|
| Cargo | Diretor Administrativo · Diretor Técnico Médico |
| Contexto | Hospitais privados médios/grandes (50-500 leitos) · planos saúde |
| Decisor real | Dir. Administrativo + DPO institucional + Comitê Dir. Médica |
| Influenciadores | Compliance · Jurídico · TI |
| Aprovador final | Conselho ou Diretor Geral |

### Empathy Map

**Diz (Says)**
- "Prontuário é nosso ativo mais sensível."
- "ANVISA + ANS + LGPD ao mesmo tempo é demais."
- "Meu sistema MV/Tasy já tem API — preciso de alguém que saiba usar."
- "Confidata já me ligou — qual a sua diferença?"

**Pensa (Thinks)**
- "Vazamento aqui não é só multa — é processo civil + crime."
- "ANS pode descredenciar contrato com operadora."
- "ANPD priorizou saúde em 2026-2027 — vão chegar aqui."
- "Comprar sistema novo sobre MV é redundância."

**Faz (Does)**
- Contratos B2B diretos com fornecedores
- Decisão em comitê (Dir. Médica + DPO + TI)
- Ciclo 45-90 dias de decisão
- Avalia integração técnica antes de pricing

**Sente (Feels)**
- Alto risco reputacional permanente
- Urgente por ANPD priorização saúde 2026-2027
- Sobrecarregado por múltiplas regulações
- Cético com solução que não integre MV/Tasy nativamente

### Pains

| Dor | Severidade | Origem |
|---|---|---|
| Dado sensível (prontuário) · sanção 2% faturamento | ALTA | LGPD Art. 52 |
| Concorrentes Confidata/Be Compliance já atuam no setor | ALTA | Mercado competitivo |
| ANPD prioriza saúde 2026-2027 | ALTA | Política regulatória |
| Risco descredenciamento ANS por vazamento | ALTA | Compliance operadora |
| Sistema MV/Tasy não cobre LGPD transversal | MÉDIA | HIS cobre HIS, não RH/ouvidoria/faturamento |

### Gains

| Ganho desejado | Importância | Como mensurar |
|---|---|---|
| ETL integrado MV/Tasy/Soul MV | ALTA | Conector funcional + dados fluindo |
| Monitoramento contínuo de dados sensíveis | ALTA | Alertas em tempo real |
| DPO automatizado (resposta titular 72h) | ALTA | SLA ANPD cumprido |
| Switching cost alto (proteção investimento) | MÉDIA | Integração profunda |
| Conformidade ANS comprovável | MÉDIA | Relatório auditoria operadora |

### JTBD

> "Me ajude a **monitorar dados de pacientes continuamente** e responder ANPD em 72h sem depender de processo manual."

### POV Statement

> Diretor de saúde privada **precisa de** monitoramento contínuo de dados de pacientes integrado ao sistema existente **porque** ANPD prioriza saúde 2026-2027 e sanção pode chegar a 2% do faturamento.

### Insight Surpreendente · O que muda o discurso comercial

O cliente **já tem MV/Tasy**. Vender outro sistema é vender o problema duas vezes (treinamento + redundância). **Vender integração é vender solução** [INFERÊNCIA · BP v2.0 §6.3]. O switching cost se inverte: cliente que integra não desconecta — porque desconectar significaria refazer conectores customizados.

**Implicação para a venda:** o produto-âncora para essa persona não é a plataforma SaaS — é o **P5 ETL/Middleware**. O discurso é "deixe seu MV/Tasy como está · nós conectamos no que ele tem". Esse posicionamento é o oposto do pitch de Confidata e Be Compliance, que vendem dashboard substituto.

**Risco operacional declarado:** este pitch depende do PoC ETL funcionar tecnicamente. Wave 2A é condicional ao gate M4 [DECISÃO D-INH-005 herdada · risco R4 mapeado em Cap 17].

### Mapeamento para os 5 produtos NeoGov

| Produto | Como ataca dores do Diretor Saúde |
|---|---|
| P5 ETL/Middleware | **Produto-âncora** · integração MV/Tasy/Soul MV |
| P4 AI-DPO Copilot | Atendimento titular automático 72h |
| P2 Data Discovery automatizado | Inventário inicial de dados sensíveis |
| P1 Plataforma LGPD SaaS | Dashboard auditável por operadora/ANS |
| P3 Anonimização LAI/LGPD | Pouco relevante (saúde privada não tem LAI) |

### Gatilhos de compra

1. Auditoria operadora plano de saúde
2. Sanção ANPD em hospital concorrente
3. Vazamento próprio (incidente prévio)
4. Mudança Diretor Administrativo (zerar passivos)
5. ANS notificação compliance LGPD

### Ciclo e canal

| Atributo | Valor |
|---|---|
| Ciclo de decisão | 3-6 meses (comitê multidisciplinar) |
| Canal primário | ANAHP (associação hospitais privados) · parceria MV/Tasy |
| Canal secundário | Eventos HIMSS Brasil · CONIB |
| Ticket médio estimado | R$ 15.000-50.000/mês [INFERÊNCIA — saúde com ticket alto] |

---

## 7.7 Persona 4 · Mantenedor/Diretor de Escola Privada (Cluster Gamma)

### Identidade

| Campo | Valor |
|---|---|
| Cargo | Mantenedor · Diretor de Escola Privada |
| Contexto | Escolas privadas pequenas/médias (50-1500 alunos) sem TI dedicada |
| Decisor real | Mantenedor (decisão solo) · Diretor (operação) |
| Influenciadores | Coordenação pedagógica · Coordenador financeiro |
| Aprovador final | Mantenedor (rápido) |

### Empathy Map

**Diz (Says)**
- "ECA Digital · fui notificado que preciso me adequar."
- "Não tenho DPO · não tenho orçamento para um."
- "Sou pequeno · não vou ser fiscalizado, né?"
- "Mensalidade está apertada pós-pandemia."

**Pensa (Thinks)**
- "Pai descobre vazamento de dado do filho = caos reputacional."
- "Como vou pagar isso com mensalidade baixa?"
- "Concorrente que se adequar primeiro ganha vantagem competitiva."
- "Preciso de algo que eu mesmo opere · sem TI."

**Faz (Does)**
- Decisão solo, rápida (sem comitê)
- Ciclo 15-45 dias
- Prefere self-service (sem dependência de consultor)
- Avalia indicação de outros mantenedores (FENEP/SINEPE)

**Sente (Feels)**
- Urgência real (ECA Digital vigente mar/2026) [AF-006]
- Preocupado e sem saber por onde começar
- Pressionado por reclamação de pai (efeito disparador)
- Esperançoso por solução acessível e simples

### Pains

| Dor | Severidade | Origem |
|---|---|---|
| Nenhum SaaS dedicado existe [AF-007] | ALTA | Oceano azul confirmado |
| ECA Digital vigente · prazo curto | ALTA | Lei 15.211/2025 |
| Preço sensível pós-pandemia | ALTA | Realidade financeira escolar |
| Sem TI interna para implantar | ALTA | Realidade operacional |
| Reação parental imprevisível a vazamento | ALTA | Risco reputacional |

### Gains

| Ganho desejado | Importância | Como mensurar |
|---|---|---|
| Consentimento parental automático (ECA Digital) | ALTA | Fluxo digital funcionando |
| Tier acessível R$ 500-800/mês | ALTA | Pricing dentro da faixa |
| Onboarding em < 1 semana | ALTA | Time-to-value |
| Vantagem competitiva (escola pioneira) | MÉDIA | Marketing "ECA Digital compliant" |
| Solução self-service · sem consultor | MÉDIA | Manual + chat IA |

### JTBD

> "Me ajude a **cumprir ECA Digital e LGPD para dados de alunos** sem precisar de TI, sem custo alto, sem complicação."

### POV Statement

> Mantenedor de escola privada **precisa de** conformidade ECA Digital + LGPD acessível e autossuficiente **porque** ECA Digital vigente desde março/2026 e nenhum produto dedicado existe.

### Insight Surpreendente · O que muda o discurso comercial

**Oceano azul real**: zero player com SaaS dedicado a ECA Digital + LGPD educacional combinados [AF-007 confirmado em BP v2.0]. Quem chegar primeiro com produto dedicado **captura o segmento** antes de qualquer concorrente reagir.

**Implicação para a venda:** o discurso para essa persona é o **oposto** dos outros três. As outras três personas são "tenho um problema reconhecido — resolva". O Mantenedor é "**você nem sabe ainda que isso é problema · eu sou o único que está dizendo + tem a solução**". Pitch educativo, não persuasivo.

**Risco operacional:** janela de oceano azul depende de chegar antes do Big4 ou de competidor SaaS reagir. Cap 17 Risco R5 mapeia esta condição.

### Mapeamento para os 5 produtos NeoGov

| Produto | Como ataca dores do Mantenedor |
|---|---|
| P1 Plataforma LGPD SaaS | **Produto-âncora** · versão leve para escola · self-service |
| P4 AI-DPO Copilot | Atendimento pai/mãe automatizado |
| P2 Data Discovery automatizado | Diagnóstico inicial sem entrevistas presenciais |
| P5 ETL/Middleware | Integração com sistema escolar (Class, Phonexao, etc.) — fase 2 |
| P3 Anonimização LAI/LGPD | Não aplicável (escola privada não tem LAI) |

### Gatilhos de compra

1. ECA Digital vigente março/2026 (gatilho temporal forte)
2. Notificação ou reclamação de pai sobre dados do filho
3. Concorrente escola anunciar adequação (efeito demonstração)
4. Início de ano letivo (compras de software)
5. FENEP/SINEPE recomendar fornecedor

### Ciclo e canal

| Atributo | Valor |
|---|---|
| Ciclo de decisão | 1-3 meses (decisão solo do mantenedor) |
| Canal primário | FENEP/SINEPE (federações educação privada) |
| Canal secundário | Eventos pedagógicos · indicação par |
| Ticket médio estimado | R$ 500-1.200/mês [INFERÊNCIA — tier acessível] |

---

## 7.8 Síntese comparativa · As 4 personas em uma tabela

| Dimensão | Procurador Municipal | Gestor B2G E/F | Diretor Saúde | Mantenedor Escolar |
|---|---|---|---|---|
| **Cluster** | Alfa | Alfa-E/F | Beta | Gamma |
| **Wave** | W1 motor caixa | W2C declarado | W2A condicional | W2B paralela |
| **Decisor real** | Procurador | CIO + PGE | Comitê Dir.+DPO | Mantenedor solo |
| **Ciclo decisão** | 4-9 meses | 9-18 meses (3-6 via ETEC) | 3-6 meses | 1-3 meses |
| **Ticket estimado** | R$ 8-15k/mês | R$ 30-80k/mês | R$ 15-50k/mês | R$ 0,5-1,2k/mês |
| **Dor central** | Improbidade pessoal | LAI×LGPD legados | Prontuário + ANS | ECA Digital sem TI |
| **Produto-âncora** | P3 Anonimização | P3 Anonimização | P5 ETL | P1 Plataforma leve |
| **Insight discursivo** | "Blindagem pessoal" | "Único que entende B2G" | "Integramos, não substituímos" | "Pioneirismo competitivo" |
| **VVV global** | 1.0 [FATO] | 0.80 [INFERÊNCIA dominante] | 0.70 [INFERÊNCIA] | 0.60 [INFERÊNCIA] |
| **Validação pendente** | Já operando · validar pricing | PNCP estaduais/federais (GAP01) | PoC ETL M4 (GAP03) | WTP entrevistas (GAP02) |

## 7.9 O que este capítulo justifica para o restante do plano

Este capítulo justifica três grupos de decisões estratégicas que aparecerão em capítulos seguintes:

1. **Capítulo 11 — Solução · Produtos:** o mapeamento "persona × produto-âncora" mostra que cada produto tem usuário específico. Não há produto "para todos" — há produtos universais com **persona-âncora prioritária**.

2. **Capítulo 13 — Value Proposition Canvas:** as quatro personas serão os pontos de partida para construir Pain Relievers e Gain Creators específicos. Cada VPC ancora em uma persona deste capítulo.

3. **Capítulo 14 — Go-to-Market:** quatro estratégias comerciais distintas (canal, ciclo, ticket, discurso) para as quatro personas. Não um único playbook.

A coerência do plano depende de **toda decisão posterior rastrear até pelo menos uma dessas quatro personas**. Se uma iniciativa não responde à dor mapeada aqui, ela está fora de escopo.

---

## Apêndices referenciados neste capítulo

- **Apêndice A · VVV-LOG**: 16 novas afirmações geradas neste sprint (AF-013 a AF-028)
- **Apêndice B · DECISIONS-LOG**: 1 decisão registrada (D-006: estrutura B fichas profundas)
- **Apêndice C · INSIGHTS-CARRY**: insights consumidos (IN-001, IN-003) · novos para próximo sprint
