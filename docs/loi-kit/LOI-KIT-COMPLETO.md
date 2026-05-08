# LOI KIT COMPLETO — Assinatura de 3+ LOIs (GO/NO-GO)
## Guia Passo-a-Passo para Fechamento com Prefeituras e Consorcios

**Data:** Maio 2026
**Responsavel:** Wilton (articulacao) + Gislene (juridico) + Camilla (produto)
**Objetivo:** 3+ LOIs assinadas ate Sprint 3 (22-28/05/2026)
**GO/NO-GO:** Sem 3 LOIs = reavaliar investimento

---

## SUMARIO DOS ENTREGAVEIS

| # | Entregavel | Secao | Status |
|---|-----------|-------|--------|
| 1 | Template LOI pronto para usar | Seção 2 | Template existe em `docs/templates/LOI-LGPD-Prefeituras.md` |
| 2 | Checklist documentos necessarios | Seção 3 | Este documento |
| 3 | Script de abordagem prefeituras | Seção 4 | Este documento |
| 4 | Calculadora ROI municipal | Seção 5 | Este documento |
| 5 | Formulario lead capture | Seção 6 | Este documento |

---

## SECAO 1: CONTEXTO ESTRATEGICO

### Por que 3 LOIs sao o GO/NO-GO

O business plan define que sem validacao de demanda real (LOIs assinadas), nao existe justificativa para investir em MVP. As LOIs provam:

- Prefeituras/consorcios tem **interesse real** (nao apenas verbal)
- O **preco proposto** e aceitavel para o orçamento municipal
- O **enquadramento ICT** (Art. 75, IV) e compreendido pela parte contratante
- Existe **urgencia** (TCE, ANPD, eleicoes)

### Metricas-Chave

| Metrica | Valor | Fonte |
|---------|-------|-------|
| Municipios sem LGPD | 4.011 (72%) | IBGE MUNIC 2024 |
| Limite dispensa licitacao | R$ 65.492/ano | Lei 14.133/2021 Art. 75 II |
| Limite dispensa ICT P&D | R$ 390.000 | Lei 14.133/2021 Art. 75 IV c |
| Ticket medio alvo | R$ 5-15K/ano | Plano de negocios |
| Consorcios mapeados | 5 prioritarios | consorcios_municipais_brasil.json |

### Timeline

```
SEMANA 1 (06-13/05): Preparacao
  [ ] Kit LOI pronto (este documento)
  [ ] Pricing validado por porte de cidade
  [ ] Lista de 30+ leads (prefeituras + consorcios)

SEMANA 2 (14-21/05): Abordagem
  [ ] Contato inicial com top 10 leads
  [ ] Webinar ou apresentacao para consorcios
  [ ] Propostas personalizadas enviadas

SEMANA 3 (22-28/05): Fechamento
  [ ] 3+ LOIs assinadas
  [ ] Pipeline de 10+ leads quentes para Sprint 4
  [ ] Feedback documentado (pricing, features, objeções)
```

---

## SECAO 2: TEMPLATE LOI — REFERENCIA RAPIDA

O template principal esta em:

```
docs/templates/LOI-LGPD-Prefeituras.md
```

### Campos Obrigatorios para Preenchimento

Para cada LOI, preencha os seguintes campos:

```
=== DADOS DA CONTRATANTE ===
[NOME_DA_PREFEITURA_OU_CONSORCIO]
[CNPJ]
[ENDEREÇO_COMPLETO]
[NOME_DO_REPRESENTANTE]       -- Prefeito ou Diretor-Presidente do consorcio
[CARGO]                       -- Prefeito / Diretor-Presidente
[CPF]
[EMAIL_CONTRATANTE]           -- Email institucional (.gov.br)

=== DADOS DA CONTRATADA (FIXO) ===
CIT AI TEC INSTITUTO DE CIENCIA E TECNOLOGIA LTDA.
[CNPJ_CIT]
[ENDEREÇO_COMPLETO_CIT]
[NOME_DO_REPRESENTANTE_CIT]   -- Wilton
[CARGO_CIT]                   -- Presidente
[CPF_CIT]
[EMAIL_CONTRATADA]            -- comercial@citaitech.com.br

=== TRANSACAO ===
[DATA_ASSINATURA]             -- Data prevista
[NUMERO_SEQUENCIAL]           -- 001, 002, 003...
[ANO]                         -- 2026

=== VALORES (ver Calculadora ROI - Secao 5) ===
[VALOR_SAAS]                  -- Mensal
[VALOR_SAAS_ANUAL]            -- Anual
[VALOR_DPO]                   -- Mensal
[VALOR_DPO_ANUAL]             -- Anual
[VALOR_SETUP]                 -- Taxa unica
[TOTAL_MENSAL]                -- Soma mensal
[TOTAL_ANUAL]                 -- Soma anual

=== PRAZOS ===
[PRAZO_MESES]                 -- 12, 24 ou 36
[DIAS_ONBOARDING]             -- 5 dias
[DIAS_DIAGNOSTICO]            -- 7 dias
[DIAS_POLITICAS]              -- 10 dias
[DIAS_TREINAMENTO]            -- 2 dias
[DATA_GO_LIVE]                -- Data estimada pos-onboarding
[DIAS_EXPERIENCIA]            -- 30 dias
[VALIDADE_MESES]              -- 6 meses

=== OUTROS ===
[PRAZO]                       -- 30 dias (pagamento fatura)
[DESCONTO]                    -- 10 (para pagamento anual)
[CIDADE]                      -- Cidade da contratante
[ESTADO]                      -- UF da contratante
[EMAIL_CONTRATANTE]
[EMAIL_CONTRATADA]
```

### Tabela de Pricing por Porte (para preencher valores)

| Porte | Populacao | SaaS Mensal | DPO Mensal | Setup | Total Mensal | Total Anual |
|-------|-----------|-------------|------------|-------|-------------|-------------|
| Micro | < 10 mil hab | R$ 247 | R$ 150 | R$ 997 | R$ 397 | R$ 4.764 |
| Pequeno | 10-20 mil hab | R$ 347 | R$ 200 | R$ 1.497 | R$ 547 | R$ 6.564 |
| Medio | 20-50 mil hab | R$ 447 | R$ 300 | R$ 1.997 | R$ 747 | R$ 8.964 |
| Medio-Grande | 50-100 mil hab | R$ 647 | R$ 450 | R$ 2.497 | R$ 1.097 | R$ 13.164 |
| Consorcio (por municipio) | Variavel | R$ 167 | R$ 80 | R$ 497 | R$ 247 | R$ 2.964 |

Nota: Todos os valores anuais estao ABAIXO de R$ 65.492 (dispensa Art. 75 II).

---

## SECAO 3: CHECKLIST DE DOCUMENTOS NECESSARIOS

### 3.1 Documentos para Enviar ao Lead (antes da LOI)

- [ ] **Apresentacao Institucional CIT AI Tech** (PDF, 10-15 slides)
  - Quem somos (ICT privado)
  - Solucao DPO-as-a-Service + Plataforma SaaS
  - Diferenciais: Data Discovery, Anonimizacao, DPO incluido
  - Cases/prova de conceito (quando houver)

- [ ] **Proposta Comercial** (PDF)
  - Escopo detalhado dos servicos
  - Precificacao por porte (usar tabela acima)
  - Cronograma de implementacao (30 dias)
  - SLA de atendimento
  - Base legal: Art. 75, IV, "c" e "d" da Lei 14.133/2021

- [ ] **Whitepaper Dispensa de Licitacao ICT** (PDF)
  - Arquivo existente: `docs/whitepaper-dispensa-licitacao-ict-lgpd.md`
  - Fundamentacao juridica Art. 75, IV
  - Enquadramento CIT como ICT
  - Comparativo com licitacao tradicional

- [ ] **Memoria Tecnica da Solucao** (PDF, 2-3 paginas)
  - Arquitetura da plataforma
  - Data center Brasil (Art. 26, par. 1, LGPD)
  - Seguranca e conformidade
  - Integracoes disponiveis

- [ ] **Certificado ICT** (copia)
  - Comprovante de qualificacao como ICT
  - Registro no MCTI (quando aplicavel)

### 3.2 Documentos para Solicitar ao Lead

- [ ] **CNPJ da Prefeitura ou Consorcio** (comprovante)
- [ ] **Identificacao do Representante Legal**
  - Nome completo, CPF, cargo
  - Ato de nomeacao ou portaria
- [ ] **Email institucional (.gov.br)** para comunicacoes oficiais
- [ ] **Diagnostico rapido LGPD** (formulario enviado por CIT)
  - Existe responsavel LGPD?
  - Quais sistemas tratam dados pessoais?
  - Recebeu notificacao TCE/ANPD?
  - Orcamento estimado para conformidade

### 3.3 Documentos para Assinatura da LOI

- [ ] LOI preenchida com todos os campos (template da Seção 2)
- [ ] Anexo I: Descricao tecnica da solucao
- [ ] Anexo II: Termo de Referencia minimo
- [ ] Anexo III: SLA proposto
- [ ] Anexo IV: Politica de privacidade CIT AI Tech

### 3.4 Checklist Pos-Assinatura

- [ ] LOI assinada por ambas as partes (2 vias)
- [ ] Copia digital em PDF salva em repositorio
- [ ] Registro no CRM/pipeline de vendas
- [ ] Agendamento de reuniao de onboarding
- [ ] Envio de formulario de diagnostico detalhado
- [ ] Inicio do cronograma de implementacao

---

## SECAO 4: SCRIPTS DE ABORDAGEM

### 4.1 Script Telefonico — Primeiro Contato (Prefeitura)

**Duracao alvo:** 3-5 minutos
**Objetivo:** Agendar reuniao com secretario de administracao ou TI

```
OLA, meu nome e [SEU NOME], da CIT AI Tech. Estou falando com
[SECRETARIO / ASSESSOR]?

(Opa, sim)

Nos somos um Instituto de Ciencia e Tecnologia especializado em
conformidade LGPD para o setor publico. Estamos contatando
prefeituras de [ESTADO] porque identificamos que [NUMERO] municipios
na regiao ainda nao possuem estrutura adequada para a Lei Geral de
Protecao de Dados.

Sei que o Tribunal de Contas tem fiscalizado ativamente esse tema, e
as multas podem chegar a 2% do faturamento -- no caso de prefeituras,
2% da receita corrente, o que pode ser significativo.

Nos oferecemos uma solucao completa: plataforma de conformidade mais
um DPO -- o Encarregado de Dados -- ja incluido no pacote. Tudo isso
por um valor que se enquadra na dispensa de licitacao, entre R$ 300
e R$ 1.000 por mes, dependendo do porte da cidade.

Gostaria de agendar uma reuniao de 30 minutos para apresentar a
solucao? Podemos fazer por videoconferencia.

(O que voces oferecem diferente de outras empresas?)

Nos somos um Instituto de Ciencia e Tecnologia. Isso significa que a
contratacao pode ser feita por dispensa usando o artigo 75, inciso IV,
da Lei de Licitacoes -- sem precisar de processo licitorio complexo.
Alem disso, nosso DPO ja vem incluido no preco, e nossos dados ficam
100% no Brasil, como exige a LGPD.

(Posso agendar para [DATA]?)

Perfeito. Vou enviar um email de confirmacao com o link da reunião
e uma apresentacao resumida. Muito obrigado pelo tempo.
```

### 4.2 Script Telefonico — Primeiro Contato (Consorcio)

**Duracao alvo:** 3-5 minutos
**Objetivo:** Agendar reuniao com Diretor-Presidente ou Diretor Executivo

```
OLA, meu nome e [SEU NOME], da CIT AI Tech. Estou falando com o(a)
[DIRETOR / ASSESSOR] do [NOME DO CONSORCIO]?

(Sim, em que posso ajudar?)

Nos somos um Instituto de Ciencia e Tecnologia que desenvolveu uma
solucao de conformidade LGPD projetada para consorcios intermunicipais.

Identificamos que o [NOME DO CONSORCIO] atende [NUMERO] municipios
em [ESTADO]. Nossa solucao permite atender todos os municipios
associados com um unico contrato -- e o preco por municipio sai a
partir de R$ 247 por mes, incluindo DPO compartilhado.

Como consorcio, voces podem inclusive revender a solucao com marca
propria, gerando uma nova fonte de receita.

Gostaria de agendar uma conversa de 30 minutos para explorar como
podemos estruturar essa parceria?

(Que base legal sustenta isso?)

Como ICT, usamos o artigo 75, inciso IV, da Nova Lei de Licitacoes.
Isso permite contratacao direta ate R$ 390 mil para pesquisa e
desenvolvimento. Para valores menores, usamos a dispensa por valor
ate R$ 65 mil. Ambos os casos dispensam licitacao completa.

(Vamos agendar para [DATA].)

Otimo. Vou enviar a confirmacao com uma proposta preliminar para
[NOME DO CONSORCIO]. Obrigado.
```

### 4.3 Email de Abordagem — Prefeitura

**Assunto:** Conformidade LGPD para [NOME PREFEITURA] — Dispensa de licitacao ate R$ 390K

```
Prezado(a) [NOME],

Meu nome e [SEU NOME], da CIT AI Tech -- Instituto de Ciencia e
Tecnologia especializado em conformidade LGPD para o setor publico.

MOTIVO DO CONTATO:

Identificamos que [NOME DA PREFEITURA] pode se beneficiar de nossa
solucao de conformidade LGPD. Nosso diferencial:

1. DPO-as-a-Service INCLUSO — Encarregado de Dados dedicado ao
   municipio, sem custo adicional de contratacao
2. Dispensa de licitacao — Como ICT, usamos o Art. 75, IV, da Lei
   14.133/2021, permitindo contratacao simplificada
3. Data 100% Brasil — Conformidade com Art. 26 da LGPD
4. Setup em 30 dias — Diagnostico automatizado, implementacao rapida

INVESTIMENTO:

A partir de R$ [VALOR]/mes, dependendo do porte do municipio.
Valor anual abaixo do limite de dispensa (R$ 65.492), facilitando
a tramitacao.

Gostaria de agendar uma reuniao de 30 minutos para apresentar
a solucao em detalhes?

Atenciosamente,

[SEU NOME]
[CARGO] — CIT AI Tech
[TELEFONE] | [EMAIL]
citaitech.com.br
```

### 4.4 Email de Abordagem — Consorcio

**Assunto:** Parceria LGPD para [NOME CONSORCIO] — R$ 247/municipio/mes

```
Prezado(a) [NOME],

Meu nome e [SEU NOME], da CIT AI Tech. Estou contatando o
[NOME DO CONSORCIO] porque desenvolvemos uma solucao de conformidade
LGPD projetada para consorcios intermunicipais.

O QUE OFERECEMOS:

1. Solucao white-label — O consorcio pode revender com marca propria
2. DPO compartilhado — 1 DPO para cada 10-20 municipios
3. Preco por volume — A partir de R$ 247/municipio/mes para 10+ cidades
4. Contratacao simplificada — ICT com dispensa Art. 75, IV

BENEFICIOS PARA O CONSORCIO:

- Nova fonte de receita (revenda com margem)
- Conformidade LGPD para todos os municipios associados
- Relatorios prontos para TCE/TCU
- Nenhuma infraestrutura necessaria (SaaS)

Gostaria de agendar uma reuniao para discutir como podemos
estruturar essa parceria?

Atenciosamente,

[SEU NOME]
[CARGO] — CIT AI Tech
[TELEFONE] | [EMAIL]
citaitech.com.br
```

### 4.5 WhatsApp — Follow-Up Pos-Reuniao

```
Oi [NOME], sou [SEU NOME] da CIT AI Tech. Obrigado pela reuniao
de [DATA].

Conforme conversamos, segue o link da nossa proposta para
[NOME PREFEITURA/CONSORCIO]:

[LINK PROPOTA]

A LOI esta pronta para assinatura assim que tivermos o OK do
senhor(a). Posso agendar uma chamada rapida para tirar duvidas?

Abs,
[SEU NOME]
```

### 4.6 Tratamento de Objecoes

| Objecao | Resposta |
|---------|----------|
| "Nao temos orcamento" | "O valor se enquadra na dispensa de licitacao. Nao precisa de processo licitorio, basta uma justificativa de contratacao direta. O custo mensal e menor que o salario de um estagiio." |
| "Ja temos alguem fazendo isso" | "Nos complementamos. Nosso DPO e compartilhado e nossa plataforma automatiza o que seria feito manualmente. Posso mostrar como agregamos valor sem substituir o que ja funciona." |
| "Precisamos de licitacao" | "Como somos ICT, a contratacao pode ser feita por dispensa (Art. 75, IV). Vou enviar o whitepaper juridico que fundamenta isso." |
| "Prefiro esperar" | "O TCE de [ESTADO] esta fiscalizando ativamente. Prefeituras sem DPO nomeado podem ser notificadas. A janela e agora." |
| "Confidata ja nos atende" | "Confidata e uma otima plataforma de documentacao. Nos complementamos com Data Discovery automatizado, Anonimizacao LAI e DPO incluido. Posso preparar uma analise comparativa." |
| "Quem garante que voces entregam?" | "Oferecemos 30 dias de experiencia. Se nao atender, sem custo. Alem disso, somos ICT registrado -- temos obrigatoriedade de entrega pela Lei de Inovacao." |

---

## SECAO 5: CALCULADORA ROI MUNICIPAL

### 5.1 Custo da Nao-Conformidade (Risco)

| Risco | Valor Estimado | Probabilidade | Custo Esperado/Ano |
|-------|---------------|---------------|-------------------|
| Multa ANPD (minima) | R$ 5.000 | 15% | R$ 750 |
| Multa ANPD (moderada) | R$ 50.000 | 5% | R$ 2.500 |
| Multa ANPD (grave) | R$ 500.000 | 1% | R$ 5.000 |
| Notificacao TCE | R$ 10.000 (custo atendimento) | 20% | R$ 2.000 |
| Processo MP/ANPD (defesa) | R$ 30.000 (advogado) | 5% | R$ 1.500 |
| Reputacao/midia | R$ 20.000 (comunicacao) | 3% | R$ 600 |
| **CUSTO ESPERADO TOTAL DO RISCO** | | | **R$ 12.350/ano** |

### 5.2 Comparativo: CIT vs Alternativas

| Solucao | Custo Anual | DPO Incluido? | Tempo Setup | Dispensa Licitacao? |
|---------|-------------|---------------|-------------|---------------------|
| **CIT AI Tech (Micro)** | R$ 4.764 | Sim | 30 dias | Sim (ICT) |
| **CIT AI Tech (Pequeno)** | R$ 6.564 | Sim | 30 dias | Sim (ICT) |
| **CIT AI Tech (Medio)** | R$ 8.964 | Sim | 30 dias | Sim (ICT) |
| **CIT AI Tech (Consorcio)** | R$ 2.964/mun | Sim | 30 dias | Sim (ICT) |
| Confidata Starter | R$ 5.964 | Nao | Meses | Sim (Art. 75 II) |
| Confidata Profissional | R$ 17.964 | Nao | Meses | Sim (Art. 75 II) |
| DPO dedicado (mercado) | R$ 60.000-120.000 | Sim | N/A | N/A |
| Consultoria LGPD | R$ 30.000-80.000 | Nao | 6-12 meses | Depende |

### 5.3 ROI por Porte de Municipio

#### Municipio MICRO (< 10 mil hab)

```
Investimento CIT:           R$ 4.764/ano
Custo risco evitado:        R$ 12.350/ano (estimativa)
DPO proprio (alternativa):  R$ 60.000/ano (impossivel)
Consultoria (alternativa):  R$ 30.000/ano

Economia vs consultoria:    R$ 25.236/ano
Economia vs DPO proprio:    R$ 55.236/ano
ROI vs risco:               159% (risco evitado / investimento)
Payback:                    4,6 meses
```

#### Municipio PEQUENO (10-20 mil hab)

```
Investimento CIT:           R$ 6.564/ano
Custo risco evitado:        R$ 12.350/ano
DPO proprio (alternativa):  R$ 60.000/ano
Consultoria (alternativa):  R$ 40.000/ano

Economia vs consultoria:    R$ 33.436/ano
Economia vs DPO proprio:    R$ 53.436/ano
ROI vs risco:               88%
Payback:                    6,4 meses
```

#### Municipio MEDIO (20-50 mil hab)

```
Investimento CIT:           R$ 8.964/ano
Custo risco evitado:        R$ 12.350/ano
DPO proprio (alternativa):  R$ 84.000/ano
Consultoria (alternativa):  R$ 50.000/ano

Economia vs consultoria:    R$ 41.036/ano
Economia vs DPO proprio:    R$ 75.036/ano
ROI vs risco:               38%
Payback:                    8,7 meses
```

#### Consorcio (por municipio, 10+ municipios)

```
Investimento CIT:           R$ 2.964/municipio/ano
Custo risco evitado:        R$ 12.350/municipio/ano
DPO proprio (alternativa):  R$ 60.000/municipio/ano

Economia vs DPO proprio:    R$ 57.036/municipio/ano
ROI vs risco:               317%
Payback:                    2,9 meses
```

### 5.4 Argumento de Venda Baseado em ROI

**Para prefeituras:**

> "O investimento anual e de R$ [VALOR]. So o custo de contratar um
> DPO no mercado seria R$ 5.000-10.000 por mes. Nos incluimos o DPO
> por uma fracao desse valor. Alem disso, o custo de uma notificacao
> do TCE ou multa da ANPD pode ser dezenas de vezes maior que o
> investimento anual na nossa solucao."

**Para consorcios:**

> "Para cada municipio associado, o custo e de apenas R$ 2.964 por
> ano. Isso e menos de R$ 250 por mes por municipio. O consorcio
> pode revender a R$ 400-500 por municipio e gerar margem de 50-70%
> sobre a diferenca."

---

## SECAO 6: FORMULARIO DE LEAD CAPTURE

### 6.1 Formulario Web — Campos Recomendados

Para implementacao em Google Forms, Typeform, ou formulario no site:

```
=== DADOS DO MUNICIPIO/CONSORCIO ===

Campo: tipo_entidade
Tipo:  Selecao unica
Opcoes: [Prefeitura, Consorcio Intermunicipal, Orgao Estadual, Outro]
Obrigatorio: Sim

Campo: nome_entidade
Tipo:  Texto curto
Placeholder: "Ex: Prefeitura Municipal de Sao Jose dos Campos"
Obrigatorio: Sim

Campo: estado
Tipo:  Selecao unica
Opcoes: [AC, AL, AM, AP, BA, CE, DF, ES, GO, MA, MG, MS, MT, PA,
         PB, PE, PI, PR, RJ, RN, RO, RR, RS, SC, SE, SP, TO]
Obrigatorio: Sim

Campo: populacao_estimada
Tipo:  Selecao unica
Opcoes: [Ate 5 mil, 5-10 mil, 10-20 mil, 20-50 mil, 50-100 mil,
         100-500 mil, Acima de 500 mil]
Obrigatorio: Sim

=== DADOS DO CONTATO ===

Campo: nome_completo
Tipo:  Texto curto
Obrigatorio: Sim

Campo: cargo
Tipo:  Texto curto
Placeholder: "Ex: Secretario de Administracao, Diretor de TI"
Obrigatorio: Sim

Campo: email_institucional
Tipo:  Email
Placeholder: "Ex: secretaria@prefeitura.gov.br"
Obrigatorio: Sim

Campo: telefone
Tipo:  Telefone
Obrigatorio: Sim

=== DIAGNOSTICO LGPD ===

Campo: possui_dpo
Tipo:  Selecao unica
Opcoes: [Sim, ja nomeamos um DPO,
         Nao, mas estamos em processo,
         Nao possuimos DPO,
         Nao sei o que e DPO]
Obrigatorio: Sim

Campo: status_lgpd
Tipo:  Selecao unica
Opcoes: [Nao iniciamos a implementacao,
         Iniciamos mas nao concluímos,
         Implementamos parcialmente,
         Estamos em conformidade,
         Nao sabemos o status]
Obrigatorio: Sim

Campo: recebeu_notificacao
Tipo:  Selecao multipla
Opcoes: [Nao recebemos,
         Notificacao TCE/TCM,
         Notificacao ANPD,
         Requerimento MP,
         Acao judicial]
Obrigatorio: Sim

Campo: sistemas_dados_pessoais
Tipo:  Selecao multipla
Opcoes: [Sistema tributario (IPTU/ISS),
         Sistema de saude (e-SUS),
         Sistema educacional,
         Portal de transparencia,
         Ouvidoria,
         Recursos humanos (servidores),
         Assistencia social (CAD/CadUnico),
         Outros]
Obrigatorio: Sim

=== INTERESSE ===

Campo: interesse_principal
Tipo:  Selecao unica
Opcoes: [Conformidade completa LGPD,
         DPO-as-a-Service,
         Diagnostico/auditoria inicial,
         Anonimizacao de documentos,
         Conformidade TCE/TCU,
         Todos os acima]
Obrigatorio: Sim

Campo: orcamento_estimado
Tipo:  Selecao unica
Opcoes: [Ate R$ 3.000/ano,
         R$ 3.000-6.000/ano,
         R$ 6.000-12.000/ano,
         R$ 12.000-30.000/ano,
         R$ 30.000-65.000/ano,
         Acima de R$ 65.000/ano,
         Nao temos orcamento definido]
Obrigatorio: Nao

Campo: urgencia
Tipo:  Selecao unica
Opcoes: [Imediata (ate 30 dias),
         Curto prazo (1-3 meses),
         Medio prazo (3-6 meses),
         Explorando opcoes]
Obrigatorio: Sim

Campo: como_conheceu
Tipo:  Selecao unica
Opcoes: [Busca Google,
         Indicacao de outro municipio,
         Webinar/evento,
         Consorcio intermunicipal,
         Redes sociais,
         Outro]
Obrigatorio: Nao

Campo: observacoes
Tipo:  Texto longo
Placeholder: "Informacoes adicionais, duvidas, ou contexto especifico"
Obrigatorio: Nao
```

### 6.2 Classificacao de Leads (Scoring)

| Criterio | Pontos | Peso |
|----------|--------|------|
| Possui urgencia imediata ou curto prazo | +30 | Alto |
| Recebeu notificacao TCE/ANPD/MP | +25 | Alto |
| Nao possui DPO | +20 | Medio |
| Populacao 20-100K (ticket medio maior) | +15 | Medio |
| Orcamento definido acima de R$ 6K/ano | +15 | Medio |
| Consorcio (volume) | +10 | Baixo |
| Nao iniciou LGPD (urgencia) | +10 | Baixo |
| Email institucional (.gov.br) | +5 | Baixo |

**Classificacao:**
- **Quente (70+ pontos):** Abordagem telefonica em 24h + proposta personalizada
- **Morno (40-69 pontos):** Email de abordagem + convite webinar
- **Frio (< 40 pontos):** Email de nurturing + adicao a lista de contatos

---

## SECAO 7: ALVOS PRIORITARIOS — TOP 5 CONSORCIOS

Baseado em `consorcios_municipais_brasil.json`:

| # | Consorcio | Estado | Municipios | Contato | Potencial |
|---|-----------|--------|------------|---------|-----------|
| 1 | **CIGA** | SC | 345 | ciga@ciga.sc.gov.br / (48) 3321-5300 | MASSIVO — 345 municipios, ja atua em TI |
| 2 | **COPIRN** | RN | 158 | copirn@copirn.org.br / (84) 98895-8827 | ALTO — 158 municipios, multifinalitario |
| 3 | **CIMAMS** | MG | 150 | Site: cimams.mg.gov.br | ALTO — 150 municipios, 22 unidades |
| 4 | **CONIAPE** | PE | 44 | administrativo@consorcioconiape.pe.gov.br | MEDIO — 44 municipios, compras compartilhadas |
| 5 | **CIMINAS** | MG | 29 | Site: ciminas.mg.gov.br | MEDIO — orcamento R$31.9M, bom caso de referencia |

### Estrategia por Consorcio

**CIGA (prioridade maxima):**
- Ja atua em gestao tributaria e sistemas para municipios
- 345 municipios = potencial de R$ 85.000/mes (a R$ 247/municipio)
- Foco: Apresentar como modulo adicional ao portfólio CIGA
- Contato inicial: email + ligacao + proposta de white-label

**COPIRN:**
- 158 municipios com saude e saneamento (dados sensiveis)
- Potencial: R$ 39.000/mes
- Foco: Conformidade em saude (dados sensiveis LGPD)

**CIMAMS:**
- 150 municipios em MG, 22 unidades descentralizadas
- Potencial: R$ 37.000/mes
- Foco: Atendimento juridico ja existe — complementar com LGPD

---

## SECAO 8: TRACKER DE LOIs

### Modelo de Acompanhamento

| # | Entidade | Contato | Porte | Data Contato | Data Reuniao | Proposta Enviada | LOI Assinada | Valor Anual | Status |
|---|----------|---------|-------|-------------|-------------|-----------------|-------------|-------------|--------|
| 1 | | | | | | | | | Lead |
| 2 | | | | | | | | | Lead |
| 3 | | | | | | | | | Lead |
| 4 | | | | | | | | | Lead |
| 5 | | | | | | | | | Lead |

### Status Possíveis

- **Lead** — Contato identificado, sem abordagem
- **Abordado** — Primeiro contato realizado
- **Reuniao agendada** — Data marcada
- **Reuniao realizada** — Apresentacao feita
- **Proposta enviada** — Proposta formal + LOI
- **Negociacao** — Discussao de termos
- **LOI assinada** — GO
- **Recusado** — Motivo registrado

---

## SECAO 9: CRITERIO GO/NO-GO

### Aprovado (GO) quando:

```
[ ] 3+ LOIs assinadas com prefeituras ou consorcios
[ ] Pelo menos 1 LOI com consorcio (escala)
[ ] Ticket medio validado entre R$ 3.000-15.000/ano
[ ] Enquadramento ICT compreendido pela contratante
[ ] Feedback documentado sobre pricing e features
[ ] Pipeline de 5+ leads adicionais identificados
```

### Reavaliar (CONDITIONAL GO) quando:

```
[ ] 1-2 LOIs assinadas
[ ] Pipeline forte (10+ leads em negociacao)
[ ] Feedback positivo mas cycle longo
```

### Abortar (NO-GO) quando:

```
[ ] 0 LOIs apos 30 dias de abordagem ativa
[ ] Objecao recorrente: "nao temos orcamento" (>80% dos leads)
[ ] Pricing rejeitado consistentemente
[ ] Enquadramento ICT contestado pela maioria
```

---

## ARQUIVOS RELACIONADOS

| Arquivo | Localizacao | Uso |
|---------|------------|-----|
| Template LOI | `docs/templates/LOI-LGPD-Prefeituras.md` | Base do documento |
| Instrucoes DOCX | `docs/templates/LOI-LGPD-Prefeituras-DOCX-PLACEHOLDER.md` | Geracao Word |
| Whitepaper dispensa | `docs/whitepaper-dispensa-licitacao-ict-lgpd.md` | Suporte juridico |
| Checklist INPI | `docs/INPI_CHECKLIST_REGISTRO_SOFTWARE_IA.md` | Registro IP |
| Consorcios | `consorcios_municipais_brasil.json` | Dados de contato |
| Business Plan | `BUSINESS-PLAN.md` | Contexto financeiro |
| Battle card | `battle-card-confidata.md` | Argumentos vs Confidata |
| Estrategia diff. | `estrategia-diferenciacao-confidata.md` | Roteiros de venda |
| Planejamento | `strategic-planning.json` | Decisoes e roadmap |

---

*Documento preparado por: CIT AI Tech — Maio 2026*
*Versao: 1.0 — Data: 08/05/2026*
*Proxima revisao: 15/05/2026 (apos Sprint 2)*
