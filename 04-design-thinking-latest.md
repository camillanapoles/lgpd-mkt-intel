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
