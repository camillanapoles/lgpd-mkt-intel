---
id: NEOGOV-V21-CAP-04-DESIGN-THINKING
filename: 04-design-thinking.md
created_at: 2026-05-14
type: BP_CHAPTER
sprint: S1.1
parent_doc: BUSINESS-PLAN-FINAL-v2.1
chapter_number: 4
fdcu_score: 9.4
pmqs_target: 9.5
vvv_target: 0.92
abordagem: B_framework_plus_caso_aplicado
tags: [design-thinking, logica-geradora, ideo, empathize, define, ideate, prototype, test]
---

# Capítulo 4 · Design Thinking — A Lógica Geradora do Plano

> "O mercado disse o que construir. Os produtos não foram inventados — foram derivados."

## 4.1 Por que este capítulo abre a estratégia

Toda decisão estratégica deste plano de negócios — quais produtos construir, quais clusters atacar primeiro, em que ordem, com qual narrativa — não nasceu de brainstorming interno nem de imitação de concorrentes. Nasceu de um processo iterativo de **Design Thinking** aplicado às dores reais identificadas em campo.

Este capítulo apresenta esse processo. Sem ele, o restante do plano parece arbitrário. Com ele, cada escolha posterior fica justificada por evidência primária.

A premissa é simples: a NeoGov tem dois ativos raros combinados — `knowledge jurídico LGPD profundo` (Simone e Gislênia, advogadas com domínio B2G) e `capacidade ICT de desenvolvimento` (Camila, automação e IA) [FATO — transcrição reunião 06/05/2026]. Nenhum concorrente combina os dois no mesmo nível [INFERÊNCIA — auditoria competitiva BP v2.0 §3.3]. A pergunta não foi *"o que faremos com esses ativos?"*, foi *"que dor real existe que apenas a combinação desses ativos consegue resolver?"*.

## 4.2 O método: Design Thinking IDEO em 5 fases canônicas

Adotamos a versão IDEO clássica do Design Thinking — `Empathize → Define → Ideate → Prototype → Test` — por três razões operacionais [DECISÃO D-001 registrada em Apêndice B]:

| Razão | Justificativa |
|---|---|
| Coerência com fonte canônica | A lógica de orquestração interna (`inst-lgpd.md` VVV=1.0) já adota IDEO. Reaproveitamento total. |
| Empathize-first é coerente com a operação atual | A NeoGov já opera em campo com prefeituras desde 2024. Os dados primários já existem — basta sistematizar. |
| Iteração linear simplificada | Versões alternativas (d.school 6 fases, Double Diamond) adicionam complexidade sem ganho proporcional no contexto B2G brasileiro. |

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│ EMPATHIZE   │ ──▶ │   DEFINE    │ ──▶ │   IDEATE    │ ──▶ │  PROTOTYPE  │ ──▶ │    TEST     │
│ Dor real?   │     │ POV         │     │ HMW         │     │ Produto     │     │ Validação   │
│ Quem sente? │     │ statement   │     │ statements  │     │ mínimo      │     │ de campo    │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
       │                                                                              │
       └──────────────── iteração contínua ───────────────────────────────────────────┘
```

As cinco subseções a seguir aplicam cada fase ao caso NeoGov, mostrando exatamente que dado entrou, que conclusão saiu, e qual decisão estratégica essa fase produziu.

---

## 4.3 Fase 1 · Empathize — As 4 dores reais identificadas

### O que é a fase

Empathize é o exercício deliberado de **abandonar suposições internas** e mergulhar nas dores reais de quem usa (ou usaria) a solução. Em vez de perguntar *"o que poderíamos vender?"*, perguntamos *"o que faz essas pessoas perderem o sono?"*.

### Como executamos sem entrevistas novas

A NeoGov tem uma vantagem incomum: já opera em campo. A transcrição de reunião interna de 06/05/2026 (VVV=1.0) é o equivalente a uma sessão extensa de etnografia — duas advogadas, uma engenheira e um comercial discutindo sem filtro os obstáculos reais que enfrentam todos os dias [FATO — transcrição]. Somou-se a isso a análise estratégica histórica e os artefatos de iteração (BSC-01/02/03, FDCU-SCORING), produzindo quatro empathy maps consolidados.

Os mapas detalhados estão no Capítulo 7 deste plano. Aqui apresentamos o resumo operacional das quatro dores centrais identificadas:

### As 4 dores universais descobertas

| Persona | Dor central | Gatilho | Ciclo de decisão | VVV |
|---|---|---|---|---|
| Procurador municipal | Responsabilização pessoal por LGPD · improbidade administrativa | Notificação TCE/MP · início de mandato | 4-9 meses | 1.0 [FATO] |
| CIO/Subsecretário estadual ou federal | Conflito LAI × LGPD em sistemas legados heterogêneos | Auditoria CGU/TCU · ANPD priorizou poder público 2026-2027 | 9-18 meses | 0.80 [FACT-T1+INFERÊNCIA] |
| Diretor administrativo hospitalar | Prontuário sensível · sanção até 2% do faturamento | Auditoria operadora · vazamento | 3-6 meses | 0.70 [INFERÊNCIA] |
| Mantenedor/diretor de escola privada | ECA Digital vigente sem TI interna · pai reativo | Notificação · reclamação parental | 1-3 meses | 0.60 [INFERÊNCIA] |

### O insight contraintuitivo

Em sessões de planejamento típicas, faria sentido começar pela dor mais "valiosa" — saúde tem ticket alto, governo federal tem volume. Mas o Empathize revelou algo diferente: **a mesma estrutura de dor aparece em todos os quatro grupos**, com variação apenas nos sistemas integrados (e-Cidade vs. MV/Tasy vs. sistema escolar) e na urgência regulatória.

Esse achado mudou tudo. Em vez de produtos diferentes por segmento, faz sentido **produtos universais que se adaptam ao sistema do cliente**. Foi nesse ponto que a hipótese "industrial, não consultoria" deixou de ser slogan e virou tese operacional [INFERÊNCIA derivada do mapeamento — D-002].

---

## 4.4 Fase 2 · Define — POV Statements por persona

### O que é a fase

Define traduz a empatia bruta em **point-of-view statements** estruturados. A fórmula canônica é: *"`[persona]` precisa de `[necessidade]` porque `[insight surpreendente sobre o por quê]`"*.

O POV não descreve o que vamos vender. Descreve o que a persona precisa, em linguagem que ela mesma usaria. Quem confunde as duas coisas constrói o produto errado.

### Os 4 POVs do plano NeoGov

#### POV 1 · Procurador municipal

> Gestor público municipal precisa de conformidade LGPD contratável sem licitação longa porque teme responsabilização pessoal e busca retorno político visível.

**Insight surpreendente:** a dor não é a multa LGPD (Art. 52 §3° isenta setor público de multa pecuniária — [FATO — Lei 13.709/2018]). A dor é a improbidade administrativa pessoal. Esse achado redireciona o discurso comercial inteiro: não falar de "evitar multa", falar de "blindagem pessoal do gestor".

#### POV 2 · CIO/Subsecretário estadual ou federal

> Gestor de órgão estadual ou federal precisa de solução LGPD que entenda especificidade B2G (LAI, transparência, sistemas legados) porque Big4 cobra mal e soluções genéricas não servem para governo.

**Insight surpreendente:** o que diferencia não é capacidade técnica genérica — é fluência na intersecção LAI×LGPD e familiaridade com sistemas legados governamentais. Isso elimina concorrência Big4 (genérica) e SaaS internacional (sem LAI).

#### POV 3 · Diretor administrativo hospitalar

> Diretor de saúde privada precisa de monitoramento contínuo de dados de pacientes integrado ao sistema existente porque ANPD prioriza saúde 2026-2027 e sanção pode chegar a 2% do faturamento.

**Insight surpreendente:** o cliente já tem MV/Tasy. Vender outro sistema é vender o problema duas vezes. Vender **integração** é vender solução. O switching cost se inverte: cliente que integra não desconecta.

#### POV 4 · Mantenedor/diretor de escola privada

> Mantenedor de escola privada precisa de conformidade ECA Digital + LGPD acessível e autossuficiente porque ECA Digital vigente desde março/2026 e nenhum produto dedicado existe [FATO — Lei 15.211/2025].

**Insight surpreendente:** oceano azul real — zero player com SaaS dedicado a ECA Digital + LGPD educacional combinados [FATO — VVV auditado BP v2.0 §1.3]. Quem chegar primeiro com SaaS dedicado captura o segmento.

### O que a fase Define produziu como decisão estratégica

A redação dos 4 POVs fez emergir uma decisão que estava implícita: **a NeoGov não vende compliance — vende blindagem operacional via knowledge especializado, com discurso comercial específico por persona** [DECISÃO D-003 registrada em Apêndice B].

---

## 4.5 Fase 3 · Ideate — HMW por persona

### O que é a fase

Ideate transforma cada POV em **How Might We statements** (HMW) — perguntas abertas, mas direcionadas, que geram opções de solução. Uma boa HMW é específica o bastante para gerar respostas concretas, mas larga o bastante para permitir alternativas não-óbvias.

### As HMWs que geraram os 5 produtos

| Persona | HMW | Direção de solução |
|---|---|---|
| Procurador municipal | Como **reduzir** o ciclo de contratação de 12 meses para 4-8 semanas? | Art. 75 IV ICT — dispensa direta |
| Procurador municipal | Como **transformar** compliance LGPD em capital político visível? | Dashboard público + relatório TCE-friendly |
| Procurador municipal | Como **servir** 50 municípios com esforço de 1? | Plataforma multi-tenant + consórcios |
| CIO estadual/federal | Como **ser** a única solução B2G que entende LAI+LGPD integrados? | Produto Anonimização LAI/LGPD (exclusivo B2G) |
| CIO estadual/federal | Como **entrar** em estados via ETEC/CPSI sem licitação longa? | Piloto Art. 75 IV → expansão licitação |
| Diretor saúde | Como **integrar** MV/Tasy/Soul MV antes do concorrente? | Produto ETL/Middleware |
| Diretor saúde | Como **gerar** relatório ANPD 72h automaticamente? | AI-DPO Copilot + monitoramento contínuo |
| Mantenedor educação | Como **ser** o primeiro SaaS dedicado ECA Digital antes de março/2026? | Plataforma leve + onboarding self-service |
| Mantenedor educação | Como **servir** 100 escolas com custo de 10? | Multi-tenant + canal FENEP/SINEPE |

### Convergência das HMWs

Quando lidas em conjunto, as nove HMWs convergem para **quatro gargalos operacionais universais** que aparecem em mais de um segmento:

1. **"Onde estão meus dados pessoais?"** — aparece nos 4 segmentos
2. **"Como publicar sem expor?"** — aparece em municipal + estadual/federal (LAI conflict)
3. **"Como atender titulares sem DPO dedicado?"** — aparece em municipal + educação + saúde pequena
4. **"Como integrar sistemas existentes?"** — aparece em saúde + educação + estadual/federal

Os quatro gargalos universais explicam por que **um portfolio compacto de cinco produtos basta para servir todos os segmentos**. Cada produto resolve um gargalo, e a combinação se adapta ao cliente.

---

## 4.6 Fase 4 · Prototype — Os 5 produtos derivados

### O que é a fase

Prototype materializa a solução. No contexto NeoGov, prototipar não significa construir um produto físico de zero — significa **definir o produto mínimo viável que resolve a dor identificada**, baseado nas capacidades existentes da empresa.

### Como os produtos foram derivados (não inventados)

Cada produto resulta da equação `gargalo universal + insumo NeoGov existente = produto IA`:

| # | Produto | Gargalo que resolve | Insumo NeoGov | VVV |
|---|---|---|---|---|
| P1 | Plataforma LGPD SaaS | Compliance básico fragmentado | Metodologia 4 fases validada + dashboard atual | 0.95 [FATO — produto existe] |
| P2 | Data Discovery automatizado ★ICT | "Onde estão meus dados?" | Knowledge Simone (o que é dado sensível) + IA Camila | 0.85 [INFERÊNCIA — derivação direta] |
| P3 | Anonimização LAI/LGPD ★ICT | "Publicar sem expor" (B2G) | Knowledge Simone+Gislênia LAI×LGPD + NLP Camila | 0.90 [FATO — gargalo confirmado em campo] |
| P4 | AI-DPO Copilot ★ICT | "Atender titular sem DPO" | Knowledge Simone treina agente IA | 0.85 [INFERÊNCIA — modelo conhecido em outras indústrias] |
| P5 | ETL/Middleware LGPD | "Integrar sistemas existentes" | Conhecimento e-Cidade/MV/Tasy + conectores Camila | 0.70 [INFERÊNCIA — PoC pendente M4] |

★ICT = produto desenvolvido sob status ICT, registrável via INPI, habilitando Art. 75 IV "d" da Lei 14.133/2021 [FATO — Lei 14.133/2021].

### A lógica de funil natural entre produtos

A ordem em que o cliente adquire os produtos foi descoberta na fase Prototype como sequência natural de valor, não como decisão arbitrária de packaging:

```
Cliente ENTRA por:
  Data Discovery (P2) ──▶ "diagnóstico, baixo risco, alta percepção de valor"
                    │
                    ▼
  AI-DPO Copilot (P4) ──▶ "recorrência mensal, atendimento contínuo"
                    │
                    ▼
  Anonimização LAI (P3) ──▶ "stickiness no workflow diário" (B2G)
                    │
                    ▼
  ETL/Middleware (P5) ──▶ "integração profunda, switching cost máximo"
```

A Plataforma (P1) é a camada base sobre a qual os outros operam. Cada produto vende o próximo de forma orgânica — Data Discovery revela o problema, AI-DPO ajuda a gerenciar, Anonimização resolve o gargalo operacional diário, ETL torna o cliente permanente.

### O pivô central: de R$600k/12 meses para R$15-50k/4-8 semanas

A fase Prototype produziu a tese central do plano [DECISÃO D-INH-002 herdada + D-004 nova]:

| Dimensão | Modelo antigo (servidor dedicado) | Modelo novo (manufaturado) |
|---|---|---|
| Ticket | R$600.000/contrato | R$15.000-50.000/contrato |
| Duração | 12 meses | 4-8 semanas |
| Equipe | Presencial 1:1 | Plataforma 1:N |
| Escala | Limite humano | Limite computacional |
| Knowledge | Mesma Simone | Mesma Simone, agora treinando agente |

O knowledge não mudou. O processo não mudou. **O que mudou foi a manufatura do processo em produto via IA + ICT**. É essa transformação que justifica o tamanho da oportunidade e a velocidade do go-to-market.

---

## 4.7 Fase 5 · Test — Validação contínua e plano

### O que é a fase

Test fecha o loop. Cada hipótese gerada nas fases anteriores deve ser validada com dados reais antes de escalar. Test não é "lançar e ver" — é experimentação estruturada com critérios pré-definidos.

### Validações já realizadas (consolidadas)

| Hipótese | Método | Resultado | VVV |
|---|---|---|---|
| Mercado público desconforme em massa | Auditoria TCU 1.384/2022 | 76,7% órgãos federais inexpressivos/iniciais | 0.95 [FATO] |
| Educação privada = oceano azul | Auditoria competitiva BP v2.0 | Zero SaaS dedicado encontrado | 0.95 [FATO] |
| Confidata domina entry-level saúde | Análise pricing público | R$497-R$3.497/mês confirmado | 0.95 [FATO] |
| Gap pricing existe | Triangulação Confidata × OneTrust | R$3.500-R$55.000/mês = território aberto | 0.85 [INFERÊNCIA validada] |
| ANPD prioriza poder público | ANPD gov.br Mapa 2026-2027 | Confirmado explicitamente | 0.95 [FATO] |
| Art. 75 IV aplica-se a ICT LGPD | Análise jurídica Gislênia | Aplica-se desde que IP registrado INPI | 0.90 [FATO + dependência] |

### Validações pendentes (gates de risco)

| Hipótese | Método pendente | Sprint relacionado | Risco se falhar |
|---|---|---|---|
| PoC ETL MV/Tasy funciona tecnicamente | Implementação técnica Camila | Wave 2A gate M4 | Reorientar Saúde para outros produtos |
| WTP real por segmento | 3-5 entrevistas primárias por cluster | Antes de pricing final | Ajustar tabela de preços |
| Status real plataforma atual | Levantamento Camila | M1 semana 1 | Cronograma MVP |
| ECA Digital obrigações específicas | Análise legal Simone+Gislênia | Sprint 3 ou pré-Wave 2B | Features do produto Educação |

O Capítulo 17 (Riscos) detalha a estratégia de mitigação. O Capítulo 18 (Roadmap) traz os gates específicos.

### O método como vantagem competitiva

Este capítulo encerra com uma observação operacional: muitas empresas adotam Design Thinking como discurso de marketing. A NeoGov adota como **método de governança contínua**. Toda nova hipótese sobre mercado, produto ou pricing passa pelo mesmo loop: empatia → POV → HMW → protótipo → teste. O plano não é estático — é uma fotografia de um sistema iterativo cujo estado atual é o que está documentado aqui.

A coerência interna entre `método declarado` e `método praticado` é o que torna este plano auditável. O Apêndice C deste documento registra cada insight descoberto durante a própria produção do plano, evidenciando que o método não foi aplicado uma vez no início — foi aplicado em loop até a entrega final.

---

## 4.8 Síntese · O que este capítulo justifica para o restante do plano

Este capítulo justifica três decisões estratégicas que aparecerão em todos os capítulos seguintes [registrado em Apêndice B como D-005]:

1. **Capítulo 7 — Personas:** as 4 personas decisoras com empathy maps detalhados não são segmentação de marketing; são as 4 dores reais que justificam todo o portfolio.
2. **Capítulo 11 — Solução:** os 5 produtos não são feature list; são respostas diretas aos quatro gargalos universais identificados na fase Ideate.
3. **Capítulos 8/12/13 — Clusters/BMC/VPC:** o ranking FDC-U, o Business Model Canvas e o Value Proposition Canvas operam sobre as personas e produtos estabelecidos aqui — não os redefinem.

O método garante que **nenhuma decisão estratégica posterior emerge do nada**. Cada uma rastreia até uma dor real mapeada em campo, fechando o loop entre evidência e estratégia.

---

## Apêndices referenciados neste capítulo

- **Apêndice A · VVV-LOG**: rastreabilidade de cada afirmação factual deste capítulo (12 entradas geradas)
- **Apêndice B · DECISIONS-LOG**: cinco decisões registradas (D-001 a D-005)
- **Apêndice C · INSIGHTS-CARRY**: insights gerados neste sprint que afetam Sprints 1.2 e 1.3



---

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




---

# Capítulo 11 · Solução — Os 5 Produtos Derivados

> "O portfólio não foi inventado. Foi derivado de 4 gargalos universais identificados em campo. Cada produto é um instrumento do pivô industrial."

## 11.1 Por que este capítulo abre a Solução

O Capítulo 4 estabeleceu Design Thinking como lógica geradora. O Capítulo 7 identificou as quatro personas decisoras. Este capítulo é o encontro entre os dois: **cada produto é a resposta concreta a uma dor mapeada nas personas, derivada via fase Prototype do DT** [INSIGHT IN-005 do Apêndice C].

A premissa central já estabelecida no Cap 04 retorna aqui como tese operacional: **"O knowledge não mudou. O processo não mudou. O que mudou foi a manufatura do processo em produto via IA + ICT"** [INSIGHT IN-002 consumido neste sprint]. Cada um dos cinco produtos a seguir é um instrumento desse pivô — não um item solto em catálogo.

## 11.2 A equação que gerou os 5 produtos

A fase Prototype convergiu em uma equação simples para gerar produtos:

```
GARGALO UNIVERSAL  +  INSUMO NEOGOV  ────[IA + ICT]────▶  PRODUTO MANUFATURADO
       (das personas)    (knowledge ou       (capacidade Camila)        (escalável)
                          processo)
```

Aplicando aos 4 gargalos universais identificados no Cap 04 §4.5:

| Gargalo universal | Insumo NeoGov | Transformação IA+ICT | Produto |
|---|---|---|---|
| "Onde estão meus dados pessoais?" | Knowledge jurídico Simone (classifica dado sensível) | Agente IA varredor | **P2 · Data Discovery** |
| "Como publicar sem expor?" (B2G) | Expertise LAI×LGPD (Simone + Gislênia) | Algoritmo NLP de tarjamento | **P3 · Anonimização LAI/LGPD** |
| "Como atender titulares sem DPO?" | Knowledge LGPD profundo (Simone) | Agente IA conversacional treinado | **P4 · AI-DPO Copilot** |
| "Como integrar sistemas existentes?" | Conhecimento e-Cidade/MV/Tasy/escolar | Conectores via API | **P5 · ETL/Middleware** |

E um quinto produto, **P1 · Plataforma SaaS**, é a camada base sobre a qual os outros operam — herdada da operação atual e evoluída para multi-tenant. Total: **5 produtos**, alinhados à decisão D-INH-002 do BP v2.0.

## 11.3 Estrutura uniforme de apresentação

Cada uma das cinco subseções seguintes apresenta o produto em estrutura idêntica:

1. **Equação derivativa** (gargalo + insumo → produto)
2. **O que é em uma frase**
3. **Persona-âncora primária** + adaptação por persona secundária
4. **Como se adapta por sistema integrado** (quando aplicável)
5. **Modelo de receita** + pricing por segmento
6. **Status ICT e INPI**
7. **Quando o cliente entra por ele** (posição no funil)

Estrutura uniforme facilita comparação entre produtos e permite o reaproveitamento como componente `<ProdutoCard>` no aplicativo interativo Vue.

---

## 11.4 Produto P1 · Plataforma LGPD SaaS

### Equação derivativa

```
Metodologia 4 fases validada em campo  +  Dashboard atual  →  SaaS multi-tenant
```

### O que é

Plataforma SaaS multi-tenant que centraliza compliance LGPD — dashboard + RIPD + DSAR + mapeamento de dados — substituindo o modelo presencial "1 consultor por cliente" por modelo "1 plataforma para todos".

### Persona-âncora primária

**Mantenedor escolar (Gamma)** — versão leve self-service [INSIGHT IN-005 do Apêndice C].

A escola privada não tem DPO, não tem TI dedicada, não tem orçamento para consultoria. Precisa de uma plataforma simples que ela mesma opere [AF-026]. P1 é o produto-âncora dela.

### Adaptação por persona secundária

| Persona | Como P1 atende |
|---|---|
| Procurador municipal (Alfa) | Dashboard de compliance auditável por TCE — capital político visível |
| Gestor B2G estadual/federal | Camada base auditável por TCU + integração com sistemas legados |
| Diretor saúde hospitalar | Dashboard centralizando dados pós-integração ETL (P5) |

### Modelo de receita

Assinatura mensal por organização.

### Pricing estimado por segmento

| Segmento | Faixa | Racional |
|---|---|---|
| Educação privada (versão leve) | R$ 500-1.200/mês | Tier acessível pós-pandemia |
| Setor público municipal | R$ 800-3.000/mês | Compatível com Art. 75 IV (R$65.492 anual) |
| Setor público estadual/federal | R$ 3.000-10.000/mês | Volume governamental |
| Saúde privada | R$ 2.000-5.000/mês | Add-on a P5 ETL |

VVV pricing: 0.65 — depende de validação WTP (GAP02) [DECISÃO D-INH-002 herdada].

### Status ICT e INPI

| Atributo | Estado |
|---|---|
| Status atual | Existe operacionalmente, evolução para multi-tenant pendente |
| Pré-requisito | GAP04 (status real plataforma · Camila levanta M1) |
| INPI | Não obrigatório para P1 (não é produto IA pura, é evolução de SaaS existente) |

### Posição no funil

Em segmentos onde NeoGov não tem ETL implantado (Educação Gamma fase 1), P1 é o **produto de entrada**. Em segmentos com integração (Saúde, Municipal), P1 é a **camada base** sobre a qual outros produtos operam.

---

## 11.5 Produto P2 · Data Discovery Automatizado ★ICT

### Equação derivativa

```
Knowledge jurídico Simone (o que é dado sensível)  +  Agente IA varredor (Camila)  →  Inventário automatizado
```

### O que é

Agente IA que varre bancos SQL/NoSQL, arquivos e e-mails do cliente identificando automaticamente dados pessoais — classificando-os como comum, sensível ou de menor. Substitui semanas de entrevistas manuais por dias de varredura.

### Persona-âncora primária

**Procurador municipal (Alfa) E Gestor B2G estadual/federal (Alfa-E/F)** — produto-âncora compartilhado pelas duas personas de setor público.

Razão: ambas têm o mesmo gargalo universal — "não sei onde estão meus dados" — e operam em sistemas legados heterogêneos. Diferença está em volume (estadual/federal tem 10x mais dados) e ciclo (estadual mais lento).

### Adaptação por persona secundária

| Persona | Como P2 atende |
|---|---|
| Diretor saúde hospitalar | Inventário inicial em sistemas MV/Tasy + sistemas RH/ouvidoria/faturamento (que MV não cobre) [AF-021] |
| Mantenedor escolar | Diagnóstico inicial sem entrevistas presenciais — relatório auto-explicativo |

### Adaptação por sistema integrado

| Sistema | Conector |
|---|---|
| PostgreSQL, MySQL, Oracle, MongoDB | Padrão SQL/NoSQL |
| Arquivos (PDF, DOCX, XLSX) | Parser + NLP |
| Sistemas municipais (e-Cidade, Betha, Fiorilli) | Conector específico |
| Sistemas hospitalares (MV, Tasy, Soul MV) | Conector específico (após PoC M4) |

### Modelo de receita

Projeto (setup inicial) + assinatura de monitoramento contínuo.

### Pricing estimado por segmento

| Segmento | Setup | Assinatura |
|---|---|---|
| Setor público municipal | R$ 5-15k | R$ 1-3k/mês |
| Setor público estadual/federal | R$ 30-80k | R$ 5-15k/mês |
| Saúde privada | R$ 20-50k | R$ 3-8k/mês |
| Educação privada (versão simplificada) | R$ 2-5k | R$ 500-1.500/mês |

VVV pricing: 0.65 — depende de validação WTP (GAP02).

### Status ICT e INPI

| Atributo | Estado |
|---|---|
| Status | Produto novo (NEW_ICT) — desenvolvimento Camila |
| INPI | **Obrigatório antes de venda B2G** (Art. 75 IV "d") [DECISÃO D-INH-007] |
| Risco | R2 — INPI não registrado (mitigação em curso) |

### Posição no funil

**Produto de entrada universal** [confirmado em Cap 04 §4.6]. Cliente entra por Data Discovery porque tem baixo risco percebido (diagnóstico não-invasivo) e alta percepção de valor imediata (revela problema antes invisível). Após P2, cliente naturalmente migra para P4 e P3.

---

## 11.6 Produto P3 · Anonimização Inteligente LAI/LGPD ★ICT

### Equação derivativa

```
Expertise LAI × LGPD (Simone + Gislênia)  +  Algoritmo NLP de tarjamento (Camila)  →  Tarjamento automático
```

### O que é

IA que identifica e tarja automaticamente dados pessoais em PDFs, Diários Oficiais, atos administrativos e documentos públicos antes da publicação via Lei de Acesso à Informação. Resolve o conflito legal diário entre **obrigação de publicar (LAI)** e **proibição de expor dados pessoais (LGPD)**.

### Por que este é o produto-âncora B2G universal

P3 é o **diferencial competitivo central** da NeoGov para todo o setor público [INSIGHT IN-006 do Apêndice C consumido neste sprint]:

1. **Único produto exclusivo B2G** — saúde privada e educação privada não têm LAI, não precisam disso. P3 é só para governo.
2. **Único produto onde ninguém entende o problema** — Big4 sabe LGPD mas não LAI brasileira. SaaS internacional não tem LAI nem como conceito.
3. **Gargalo diário** — todo município, estado e órgão federal publica diariamente. Hoje é feito à mão ou não é feito.
4. **Habilitado por Acórdão TCE-PR 1153/2025** — referência jurisprudencial que valida abordagem.

P3 é a razão principal pela qual NeoGov vence Big4 e OneTrust no setor público brasileiro. Sem P3, NeoGov é mais um SaaS LGPD. Com P3, é **a única solução B2G completa**.

### Persona-âncora primária

**Procurador municipal (Alfa) E Gestor B2G estadual/federal (Alfa-E/F)** — produto-âncora compartilhado por ambas as personas B2G.

### Adaptação por persona secundária

P3 **não se adapta** para Beta (saúde privada) e Gamma (educação privada). Esses segmentos não têm LAI. Confirmado em Cap 07 §7.6 e §7.7 — P3 não consta dos mapeamentos persona × produto desses dois.

### Adaptação por volume

| Tamanho do órgão | Customização |
|---|---|
| Município pequeno (publicações semanais) | Versão batch (processa fila uma vez/dia) |
| Município médio/grande (publicações diárias) | Versão real-time (API call por documento) |
| Estado/Federal (volume massivo) | Versão enterprise (auto-scaling + dashboards de auditoria) |

### Modelo de receita

Usage-based (por documento processado/mês).

### Pricing estimado

| Segmento | Faixa |
|---|---|
| Setor público municipal | R$ 1.000-4.000/mês |
| Setor público estadual | R$ 5.000-15.000/mês |
| Setor público federal | R$ 10.000-30.000/mês |

VVV pricing: 0.70 — validar via PNCP (GAP01).

### Status ICT e INPI

| Atributo | Estado |
|---|---|
| Status | Produto novo (NEW_ICT) — desenvolvimento Camila |
| INPI | **Obrigatório** — base do diferencial competitivo |
| Exclusividade | **Exclusivo B2G** [confirmado em DATA-v2.json] |

### Posição no funil

P3 é o produto que cria **stickiness operacional** em clientes B2G. Após implantado, faz parte do fluxo diário do órgão (toda publicação passa por ele). Switching cost elevado.

---

## 11.7 Produto P4 · AI-DPO Copilot ★ICT

### Equação derivativa

```
Knowledge LGPD profundo (Simone) + Conhecimento ECA Digital + LAI  +  Agente IA conversacional treinado (Camila)
→  DPO-as-a-Service escalável
```

### O que é

Agente IA treinado em LGPD + LAI + ECA Digital que opera como copiloto do Encarregado de Dados — responde a pedidos de titulares, redige relatórios de impacto à proteção de dados (RIPDs), apoia ouvidoria e guia DPOs humanos. Substitui o modelo "1 especialista por cliente" pelo modelo "1 especialista treina o agente, agente atende 10x mais clientes".

### Persona-âncora primária

**Mantenedor escolar (Gamma)** — não tem DPO próprio, não tem orçamento para contratá-lo. AI-DPO é a única forma viável de cumprir LGPD em escola pequena/média [AF-026].

### Adaptação por persona secundária

| Persona | Como P4 atende |
|---|---|
| Procurador municipal | DPO-as-a-service para município sem orçamento DPO humano |
| Gestor B2G estadual/federal | Reduz carga de DPO humano sobrecarregado em volume estadual [AF-005] |
| Diretor saúde hospitalar | Atendimento titular automático em 72h conforme SLA ANPD |

### Adaptação por base de conhecimento

| Versão | Treinado em |
|---|---|
| Versão municipal | LGPD + LAI + foco em prefeituras |
| Versão estadual/federal | LGPD + LAI + Lei 14.133 + transparência ativa + sistemas legados |
| Versão saúde | LGPD + dados sensíveis + ANS + ANVISA + prontuário eletrônico |
| Versão educação | LGPD + ECA Digital + consentimento parental + dados de menor |

### Modelo de receita

Assinatura mensal por organização (com tier por volume de atendimentos).

### Pricing estimado por segmento

| Segmento | Faixa |
|---|---|
| Educação privada | R$ 800-2.000/mês |
| Setor público municipal | R$ 1.500-5.000/mês |
| Setor público estadual/federal | R$ 5.000-15.000/mês |
| Saúde privada | R$ 3.000-10.000/mês |

VVV pricing: 0.65 — validar WTP (GAP02).

### Status ICT e INPI

| Atributo | Estado |
|---|---|
| Status | Produto novo (NEW_ICT) — desenvolvimento Camila |
| INPI | Obrigatório (algoritmo + base de conhecimento jurídico = IP) |
| Diferencial | Treinado em LGPD + LAI + ECA Digital brasileiros — não é OpenAI genérico |

### Posição no funil

P4 é o **produto recorrente** do funil — entra após P2 (Data Discovery) que revelou o problema. Cliente assina P4 porque precisa de gestão contínua, não diagnóstico isolado.

---

## 11.8 Produto P5 · ETL/Middleware LGPD

### Equação derivativa

```
Conhecimento dos sistemas do cliente (e-Cidade, MV/Tasy, Class, etc.)  +  Conectores via API (Camila)
→  Monitoramento contínuo automático
```

### O que é

Middleware que se conecta via API nativa aos sistemas existentes do cliente e monitora dados pessoais continuamente — gera alertas, atualiza RIPDs automaticamente, notifica incidentes em tempo real. **Não substitui** o sistema do cliente — integra-se a ele.

### Persona-âncora primária

**Diretor administrativo hospitalar (Beta)** — o cliente já tem MV/Tasy e não vai substituí-lo. P5 é o único caminho para entrar em saúde sem competir contra o sistema instalado [INSIGHT IN-006 + AF-022].

### Adaptação por persona secundária

| Persona | Como P5 atende |
|---|---|
| Procurador municipal | Integração com e-Cidade · TCE · sistemas municipais (alto switching cost após implantação) |
| Mantenedor escolar | Integração com sistema escolar (Class, Phonexao, Sponte) — fase 2 do funil |
| Gestor B2G estadual/federal | Integração com sistemas legados (SEI, SIAFI) — alta complexidade técnica |

### Adaptação por sistema integrado (gold do mapeamento)

| Segmento | Sistemas suportados |
|---|---|
| Setor público municipal | e-Cidade · TCE · Betha · Fiorilli · sistemas municipais |
| Saúde privada | MV · Tasy · Soul MV (gate PoC M4) |
| Educação privada | Class · Phonexao · Opyun · Sponte · Wpensar |
| Setor público estadual/federal | SEI · SIAFI · sistemas legados específicos |

### Modelo de receita

Setup (one-time) + assinatura usage-based (por registros processados/mês).

### Pricing estimado

| Segmento | Setup | Assinatura |
|---|---|---|
| Setor público municipal | R$ 10-30k | R$ 1-3k/mês |
| Saúde privada | R$ 30-60k | R$ 5-8k/mês |
| Educação privada | R$ 5-15k | R$ 800-2.000/mês |
| Setor público estadual/federal | R$ 50-150k | R$ 8-25k/mês |

VVV pricing: 0.55 — depende totalmente de PoC M4 (GAP03) [RISCO R4].

### Status ICT e INPI

| Atributo | Estado |
|---|---|
| Status | Produto novo (NEW_ICT) — desenvolvimento Camila |
| INPI | Conectores específicos podem ser registrados |
| Gate crítico | **PoC ETL MV/Tasy obrigatório em M4 antes de escalar Saúde** [D-INH-005] |
| VVV | 0.70 — menor do portfólio por dependência técnica não validada |

### Posição no funil

P5 é o produto que cria **switching cost máximo**. Uma vez integrado nos sistemas do cliente, sair custaria refazer conectores customizados. É o produto que transforma cliente em recorrente permanente.

---

## 11.9 Matriz de Síntese · Persona × Produto-Âncora × Adaptação

| Produto | Persona-âncora | Adapta para | Diferencial competitivo |
|---|---|---|---|
| **P1 Plataforma SaaS** | Mantenedor escolar (Gamma) | Procurador · Gestor B2G · Diretor saúde | Camada base universal |
| **P2 Data Discovery** ★ICT | Procurador + Gestor B2G | Diretor saúde · Mantenedor | Substitui entrevistas manuais |
| **P3 Anonimização LAI/LGPD** ★ICT | Procurador + Gestor B2G | (não adapta — exclusivo B2G) | **Único produto LAI×LGPD do mercado** |
| **P4 AI-DPO Copilot** ★ICT | Mantenedor escolar | Procurador · Gestor B2G · Diretor saúde | Treinado em legislação BR (vs OpenAI genérico) |
| **P5 ETL/Middleware** | Diretor saúde hospitalar | Procurador · Mantenedor · Gestor B2G | Switching cost máximo (integração API) |

## 11.10 Sequência de venda · Funil natural entre produtos

A ordem em que o cliente adquire produtos foi descoberta na fase Prototype como sequência natural de valor (já apresentada em Cap 04 §4.6):

```
CLIENTE ENTRA POR:
  P2 Data Discovery  ──▶  diagnóstico baixo risco, alta percepção de valor
         │
         ▼
  P4 AI-DPO Copilot  ──▶  recorrência mensal, atendimento contínuo
         │
         ▼
  P3 Anonimização LAI  ──▶  stickiness no workflow diário (apenas B2G)
         │
         ▼
  P5 ETL/Middleware  ──▶  integração profunda, switching cost máximo

P1 Plataforma SaaS é a CAMADA BASE sobre a qual os outros operam.
```

Cada produto vende o próximo. Data Discovery revela o problema → AI-DPO ajuda a gerenciar → Anonimização (em B2G) resolve gargalo operacional → ETL torna o cliente permanente.

## 11.11 Pivô industrial · Tabela comparativa

A tese central do plano — **"industrial, não consultoria"** [INSIGHT IN-002 consumido neste sprint] — é materializada nos cinco produtos:

| Dimensão | Modelo antigo (1:1 consultoria) | Modelo novo (1:N produto) |
|---|---|---|
| Ticket | R$ 600.000/contrato | R$ 15.000-50.000/contrato |
| Duração contratual | 12 meses | 4-8 semanas implantação + recorrência |
| Equipe necessária | Presencial dedicada 1 consultor por cliente | Plataforma multi-tenant + agente IA |
| Escala | Limite humano (10-15 clientes/ano) | Limite computacional (100+ clientes/ano) |
| Knowledge | Mesma Simone | Mesma Simone — treinando o agente |
| Receita | Linear (não escala) | Recorrente + usage-based |
| Switching cost | Baixo (cliente pode trocar de consultor) | Alto (integração + workflow embutido) |
| Diferencial | Knowledge jurídico | Knowledge jurídico **+** automação **+** integração |

## 11.12 Validações pendentes (gates de risco) · Síntese

| Produto | Validação pendente | Gate | Risco se falhar |
|---|---|---|---|
| P1 Plataforma | Status real atual (GAP04) | M1 sem 1 | Cronograma MVP atrasa |
| P2-P3-P4 | Registro INPI | Antes de venda B2G | Art. 75 IV "d" bloqueado |
| Todos | WTP real por segmento (GAP02) | Antes de pricing final | Ajuste tabela preços |
| P3 | Texto ECA Digital específico (GAP07) | Antes de Wave 2B | Features específicas |
| P5 | PoC MV/Tasy funciona (GAP03) | M4 Saúde gate | Reorienta Wave 2A |
| P2/P3/P4 | Scores Gov estadual/federal (GAP01) | Antes Wave 2C | Ajuste pricing/abordagem |

Cap 17 (Riscos) detalha mitigação. Cap 18 (Roadmap) traz gates específicos.

## 11.13 O que este capítulo justifica para o restante do plano

Este capítulo justifica três grupos de decisões estratégicas que aparecerão em capítulos seguintes:

1. **Capítulo 12 — Business Model Canvas:** os 5 produtos definem Value Propositions, Revenue Streams e Key Activities. BMC é a operacionalização dos produtos como modelo de negócio.

2. **Capítulo 13 — Value Proposition Canvas:** cada VPC ancora em (persona-âncora × produto-âncora). 4 VPCs × 5 produtos = mapeamento explícito de Pain Relievers e Gain Creators.

3. **Capítulo 14 — Go-to-Market:** a sequência de venda §11.10 define o playbook comercial. Cada wave (W1, W2A, W2B, W2C) usa subset de produtos por persona.

A coerência do plano depende de **cada produto rastrear até a fase Prototype do Cap 04 + uma persona do Cap 07**. Nenhum produto aparece "do nada" — todos foram derivados.

---

## Apêndices referenciados neste capítulo

- **Apêndice A · VVV-LOG**: 14 novas afirmações geradas (AF-029 a AF-042)
- **Apêndice B · DECISIONS-LOG**: 1 decisão registrada (D-009: estrutura B fichas profundas)
- **Apêndice C · INSIGHTS-CARRY**: 4 insights consumidos (IN-002, IN-004, IN-005, IN-006) · novos para Sprint 2 e 3
