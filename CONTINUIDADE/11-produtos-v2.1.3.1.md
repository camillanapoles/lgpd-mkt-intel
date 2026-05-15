---
id: NEOGOV-V21-CAP-11-PRODUTOS
filename: 11-produtos-v2.1.3.1.md
created_at: 2026-05-14
type: BP_CHAPTER
sprint: S1.3
edicao: 1
parent_doc: BUSINESS-PLAN-FINAL-v2.1
chapter_number: 11
fdcu_score: 9.0
pmqs_target: 8.0
vvv_target: 0.85
abordagem: B_fichas_profundas_matriz_sequencia
referencia_capitulos: [04, 07, 12, 13, 14]
insights_consumidos: [IN-002, IN-004, IN-005, IN-006]
tags: [produtos, solucao, pivo-industrial, ict, ia, ai-dpo, anonimizacao, data-discovery, etl]
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
