# FRAMEWORK DE DECOMPOSIÇÃO CRITÉRIOS UNIVERSAL (FDC-U)

## 1. FRAMEWORK SOBRE O CRITÉRIO ORIGINAL

Este FRAMEWORK é uma Metodologia para ordenar e hierarquizar qualquer coisa com base em critérios que são características do objeto, podendo ser positivas ou negativas (inverso), DE FORMA AGONOSTICA E UNIVERSAL/framework para decomposição de qualquer objeto em critérios ponderados, aplicável a: pesquisas, conhecimento, ferramentas de uso, priorizar skills, ou ranquear ferramentas de infraestrutura, etc.

---

## 2. FRAMEWORK AGNÓSTICO — `FDC-U v1.0`

### 2.1 PRINCÍPIO FUNDAMENTAL

> Qualquer objeto `O` pode ser ordenado hierarquicamente se decomposto em atributos mensuráveis `A_i` que impactam um objetivo `G`.

A ordenação emerge da função de utilidade agregada:

```
Score(O) = Σ [ w_i × f_i( A_i(O) ) ]

onde:
  w_i  = peso da dimensão i  (Σw_i = 1.0)
  f_i  = função de transformação (+ direta / - inversa / ~ neutra)
  A_i  = atributo mensurável do objeto
```

---

### 2.2 TAXONOMIA DE FUNÇÕES DE IMPACTO `f_i`

```
┌─────────────────────────────────────────────────────────────┐
│ TIPO     │ SÍMBOLO │ QUANDO USAR           │ FÓRMULA       │
├─────────────────────────────────────────────────────────────┤
│ Positivo │   (+)   │ Mais é melhor         │ f(x) = x      │
│ Negativo │   (-)   │ Menos é melhor        │ f(x) = 10 - x │
│ Ótimo    │   (~)   │ Existe valor ideal    │ f(x)=10-|x-m| │
│ Limiar   │   (>)   │ Mínimo aceitável      │ f(x)=0 se x<t │
│ Logarit. │   (log) │ Retornos decrescentes │ f(x)=log(x+1) │
└─────────────────────────────────────────────────────────────┘
```

---

### 2.3 PROTOCOLO DE DECOMPOSIÇÃO (5 PASSOS)

```
PASSO 1 ➞ DEFINIR O OBJETIVO G
         └─ "Para que estou ordenando estes objetos?"
         
PASSO 2 ➞ LISTAR OBJETOS CANDIDATOS {O₁, O₂, ..., Oₙ}

PASSO 3 ➞ EXTRAIR ATRIBUTOS INTRÍNSECOS A_i
         └─ Pergunta-gatilho: "O que EM [objeto] impacta [objetivo]?"
         
PASSO 4 ➞ ATRIBUIR PESOS w_i E FUNÇÕES f_i
         └─ Restrição: Σw_i = 1.0
         
PASSO 5 ➞ APLICAR REGRAS DE PROFUNDIDADE
         └─ Regra de ouro: se (Irreversibilidade > 7) E (Impacto > 7)
             → análise com profundidade 2×
```

---

## 3. APLICAÇÕES POR DOMÍNIO

### 3.1 PESQUISAS / FONTES DE CONHECIMENTO

```
┌─────────────────────────────────────────────────────────────┐
│ OBJETIVO G: "Qual fonte devo consumir PRIMEIRO?"            │
├─────────────────────────────────────────────────────────────┤
│ Dimensão              │ Peso  │ f_i   │ O que mede?        │
├─────────────────────────────────────────────────────────────┤
│ Recência              │ 0.25  │ (+)   │ Idade da info      │
│ Profundidade técnica  │ 0.25  │ (+)   │ Nível de detalhe   │
│ Credibilidade fonte   │ 0.20  │ (+)   │ Autoridade         │
│ Tempo de leitura      │ 0.15  │ (-)   │ Custo temporal     │
│ Aplicabilidade direta │ 0.15  │ (+)   │ Relevância imediata│
└─────────────────────────────────────────────────────────────┘

➞ REGRA DE OURO: Fonte com ALTA CREDIBILIDADE + ALTA APLICABILIDADE
   → validar citações cruzadas antes de consumir
```

### 3.2 FERRAMENTAS / STACK TECNOLÓGICO

```
┌─────────────────────────────────────────────────────────────┐
│ OBJETIVO G: "Qual ferramenta adotar para o projeto?"        │
├─────────────────────────────────────────────────────────────┤
│ Dimensão              │ Peso  │ f_i   │ O que mede?        │
├─────────────────────────────────────────────────────────────┤
│ Produtividade ganha   │ 0.30  │ (+)   │ Output / hora      │
│ Curva de aprendizado  │ 0.20  │ (-)   │ Tempo até produtivo│
│ Custo (licença/infra) │ 0.15  │ (-)   │ $ mensal           │
│ Comunidade/ecossistema│ 0.15  │ (+)   │ Suporte disponível │
│ Vendor lock-in        │ 0.10  │ (-)   │ Dificuldade saída  │
│ Manutenção longo prazo│ 0.10  │ (-)   │ Custo contínuo     │
└─────────────────────────────────────────────────────────────┘

➞ REGRA DE OURO: Ferramenta com ALTO VENDOR LOCK-IN + ALTO CUSTO
   → análise de migração de saída antes de adoção
```

### 3.3 DECISÕES DE ARQUITETURA / DESIGN

```
┌─────────────────────────────────────────────────────────────┐
│ OBJETIVO G: "Qual padrão/arquitetura implementar?"          │
├─────────────────────────────────────────────────────────────┤
│ Dimensão              │ Peso  │ f_i   │ O que mede?        │
├─────────────────────────────────────────────────────────────┤
│ Escalabilidade        │ 0.25  │ (+)   │ Crescimento futuro │
│ Complexidade cognitiva│ 0.20  │ (-)   │ Carga mental dev   │
│ Custo de mudança      │ 0.20  │ (-)   │ Refactor necessário│
│ Performance           │ 0.15  │ (+)   │ Latência/throughput│
│ Testabilidade         │ 0.10  │ (+)   │ Facilidade testes  │
│ Observabilidade       │ 0.10  │ (+)   │ Debug/monitoramento│
└─────────────────────────────────────────────────────────────┘

➞ REGRA DE OURO: Decisão com ALTO CUSTO DE MUDANÇA + ALTA ESCALABILIDADE
   → protótipo de stress-test + plano de rollback obrigatório
```

### 3.4 TAREFAS / WORKFLOW (generalização do original)

```
┌─────────────────────────────────────────────────────────────┐
│ OBJETIVO G: "Qual tarefa executar AGORA?"                   │
├─────────────────────────────────────────────────────────────┤
│ Dimensão              │ Peso  │ f_i   │ O que mede?        │
├─────────────────────────────────────────────────────────────┤
│ Valor entregue        │ 0.30  │ (+)   │ Impacto no objetivo│
│ Custo execução        │ 0.20  │ (-)   │ Esforço necessário │
│ Risco se adiado       │ 0.20  │ (+)   │ Degradação temporal│
│ Bloqueio downstream   │ 0.15  │ (+)   │ Dependências       │
│ Irreversibilidade     │ 0.15  │ (+)   │ Custo do erro      │
└─────────────────────────────────────────────────────────────┘

➞ REGRA DE OURO: IRREVERSÍVEL + ALTO IMPACTO = análise 2× profunda
```

---

## 4. METODOLOGIA DE EXTRAÇÃO DE ATRIBUTOS

### 4.1 PERGUNTAS-GATILHO POR CATEGORIA

```
┌─────────────────────────────────────────────────────────────┐
│ CATEGORIA DO OBJETO  │ PERGUNTAS DE DECOMPOSIÇÃO            │
├─────────────────────────────────────────────────────────────┤
│ CONHECIMENTO         │ • Quão recente? Quão profundo?       │
│                      │ • Quão aplicável? Quão confiável?    │
│                      │ • Quanto tempo para absorver?        │
├─────────────────────────────────────────────────────────────┤
│ FERRAMENTA           │ • Quanto ganho de produtividade?     │
│                      │ • Quanto custa aprender/manter?      │
│                      │ • Quão difícil é trocar depois?      │
├─────────────────────────────────────────────────────────────┤
│ DECISÃO/ARQUITETURA  │ • Quão caro é mudar depois?          │
│                      │ • Quanto escala? Quão complexo?      │
│                      │ • Quão fácil de testar/monitorar?    │
├─────────────────────────────────────────────────────────────┤
│ PESSOA/CANDIDATO     │ • Quanto valor entrega?              │
│                      │ • Quanto custa integrar?             │
│                      │ • Quem mais depende dele?            │
├─────────────────────────────────────────────────────────────┤
│ INVESTIMENTO/RECURSO │ • Retorno esperado?                  │
│                      │ • Risco de perda?                    │
│                      │ • Liquidez (quão rápido converte)?   │
└─────────────────────────────────────────────────────────────┘
```

---

## 5. TEMPLATE UNIVERSAL REUTILIZÁVEL

```markdown
# MATRIZ DE IMPACTO — [OBJETIVO G]

## Objetivo
[Definir claramente para que estou ordenando]

## Objetos candidatos
- O₁: [descrição]
- O₂: [descrição]
- ...

## Dimensões de impacto

| Dimensão | Peso | f_i | Score O₁ | Score O₂ | ... |
|----------|------|-----|----------|----------|-----|
| [A₁]     | 0.xx | (+) |          |          |     |
| [A₂]     | 0.xx | (-) |          |          |     |
| ...      |      |     |          |          |     |

## Fórmula
Score(Oₙ) = Σ (peso_i × f_i(A_i(Oₙ)))

## Regras de profundidade
- Se [dimensão X] > 7 E [dimensão Y] > 7 → análise 2×
- Se [dimensão Z] < [limiar] → descarte imediato

## Resultado
| Rank | Objeto | Score | Justificativa |
|------|--------|-------|---------------|
| 1    |        |       |               |
| 2    |        |       |               |
```

---

## 6. SÍNTESE — O QUE TORNA ISTO UNIVERSAL

| Aspecto | Como se generaliza	 |
|------|--------|
| Objeto | Qualquer entidade mensurável	 |
| Atributos | Características intrínsecas que impactam `G`	 |
| Função `f_i` | Direta (+), inversa (-), ótima (), limiar (>)	 |
| Peso `w_i` | Reflete prioridade do contexto	 |
| Regra de ouro | Identifica casos que exigem análise extra	 |
| Score | Ordenação numérica objetiva |	

---

