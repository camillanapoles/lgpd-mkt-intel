# PILOT S→Q→I→A — Estágio [Q] Questionador
## Item: ceu/eca_digital_urgent
## Timestamp: 2026-05-09T22:43:30-03:00
## Agente: stage-q-pilot
## Modo: epistemologia crítica — 5N + classificação evidência + 3× Por quê?
## Input: pilot-eca_digital_urgent-S.md

---

## 1. INTERROGAÇÃO SISTÊMICA — 5N

### 1.1 NEGAÇÃO — O que foi omitido na análise S?

| # | Omissão | Implicação |
|---|---------|-----------|
| N1 | Estágio S não verificou se a Lei 15.211/2025 já tem decisões de TRF/STJ aplicando-a — pode haver jurisprudência alterando o sentido literal | Risco de leitura puramente literal |
| N2 | Não foi mapeado se existe MP/Decreto regulamentador já editado entre 09/2025 e 05/2026 (8 meses) | Cenário regulatório pode já ter mudado |
| N3 | Não foi avaliado o custo médio de implementação de age-verification por porte de cliente | Sem isso, "urgência" é abstrata |
| N4 | Não foram listados concorrentes que JÁ vendem módulo ECA-compliance | Sem isso, não há baseline competitivo |
| N5 | Não há análise de capacidade interna (engenharia/produto) de entregar módulo no prazo | Urgência externa sem urgência interna gera planejamento irreal |

### 1.2 NUANCE — Onde estão os graus de liberdade?

| # | Grau de liberdade | Faixa |
|---|-------------------|-------|
| Nu1 | Definição técnica de "verificação de idade" pode variar — auto-declaração, biometria, RG digital, gov.br | Spectrum de R$0 a R$ milhões em CAPEX |
| Nu2 | "Fornecedor" pode ser interpretado restritivamente (só big tech) ou amplamente (qualquer SaaS B2B/B2G) | Define se nosso SaaS é sujeito direto ou indireto |
| Nu3 | Sanção pode variar de advertência a multa de até 10% faturamento (modelo LGPD) | Risco financeiro tem 3 ordens de magnitude |
| Nu4 | Vacatio legis pode ser estendida por MP ou suspensa por liminar | Cronograma não é determinístico |

### 1.3 NÚCLEO — Qual o núcleo duro irrefutável?

**Núcleo duro (sobrevive a qualquer ataque)**:
1. Lei 15.211/2025 EXISTE e foi publicada (F1, F2)
2. Texto legal MENCIONA verificação de idade (F4)
3. Há vacatio legis com data definida (F5)
4. Subset das audiences do SaaS LIDA com dados de menores (F13-F15)

**Tudo o mais é interpretação, projeção ou inferência.**

### 1.4 NEXO — Como conecta com domínios adjacentes?

| Domínio adjacente | Conexão | Força |
|-------------------|---------|-------|
| LGPD Art. 14 (consentimento parental) | Pré-existente, base sobre a qual ECA Digital se estende | FORTE |
| GDPR Art. 8 (idade do consentimento digital) | Modelo internacional já regulamentado — referência para ANPD | MÉDIA |
| COPPA (EUA) | Modelo histórico de age-verification — 25 anos de jurisprudência | MÉDIA |
| Regulamento DSA (UE) | Define obrigações de plataformas — modelo de enforcement | FRACA-MÉDIA |
| Marco Civil Internet | Não exige age-verification, mas fornece base de princípios | FRACA |

### 1.5 NULIDADE — O que torna a análise inválida (Falsificação Popperiana)?

A afirmação central do item ("ECA Digital cria urgência REAL para nosso SaaS") seria **invalidada** se:
- (a) ANPD/ANATEL emitirem regulamentação que isenta SaaS B2B/B2G de implementar age-verification (delegando ao cliente final), OU
- (b) Vacatio legis for prorrogada para >24 meses por MP ou liminar federal, OU
- (c) Custo de implementação cair drasticamente (ex: serviço gov.br gratuito), tornando urgência irrelevante

Nenhuma das 3 condições é impossível. **A afirmação é falsificável → científica → válida para análise.**

---

## 2. ESCALA DE EVIDÊNCIA — Classificação de cada claim do Estágio S

| # | Claim do Estágio S | Classificação | Justificativa |
|---|--------------------|---------------|---------------|
| C1 | Lei 15.211/2025 existe (F1) | **FACT** | Ato normativo publicado em DOU |
| C2 | Lei altera ECA (F2) | **FACT** | Ementa oficial |
| C3 | Lei estabelece deveres para fornecedores TI (F3) | **FACT** | Texto legal Art. 3º |
| C4 | Lei exige age verification (F4) | **FACT** | Texto legal Art. 5º |
| C5 | Vacatio é 12 meses (F5) | **FACT** | Texto legal artigo final |
| C6 | Regulamentação ANPD/ANATEL pendente (F6) | **INFERENCE** | Inferido de competência institucional + ausência de dec. publicado em fonte oficial conhecida no recorte temporal |
| C7 | "ECA Digital cria urgência real para prefeituras" | **INFERENCE** + **SPECULATION** parcial | Fato (lei existe) + inferência (afeta dados de menores) + especulação (urgência alta sem regulamentação publicada) |
| C8 | "Prefeituras com dados de menores precisam compliance imediato" | **SPECULATION** | "Imediato" é exagero — vacatio dá 12m; depende de regulamentação |
| C9 | "Peso 5 (máximo)" justificado pela lei | **BELIEF** | Não há critério objetivo declarado para fator=5 vs fator=4 — é juízo de valor |
| C10 | "Impacto homogêneo em 5 audiences" (premissa P3) | **BELIEF** | Não há análise per-segmento — assumido como crença |
| C11 | "VVV=0.98 captura corretamente o item" | **BELIEF** | VVV foi atribuído por LLM em narrativa, não por pipeline real (vide vvv_decay_reason) |
| C12 | "shelf_life=12m é apropriado" | **SPECULATION** | Não há base empírica — chute fundamentado |

**Contagem de labels (mandato ≥5):** FACT=5, INFERENCE=2, SPECULATION=3, BELIEF=4, **TOTAL=14 ocorrências.**

---

## 3. QUESTIONAMENTO RECURSIVO — 3× "Por quê?"

### 3.1 Conclusão "ECA Digital = urgência alta para nosso SaaS"

```
Por quê? (1) → Porque a lei exige age verification e nossas audiences (prefeitura/hospital/escritorio_juridico)
                lidam com dados de menores
   Por quê? (2) → Porque o modelo de negócio do SaaS é vender módulos LGPD-compliance,
                   e ECA Digital expande superfície de obrigações
      Por quê? (3) → Porque clientes (notadamente prefeituras) demandam que o SaaS
                      "resolva o problema regulatório", não apenas armazene dados
                      → REVELAÇÃO: a urgência é COMERCIAL (preempção competitiva)
                        mais do que JURÍDICA (vacatio dá 12m)
```

**Insight**: A urgência real é **competitiva** (quem chega primeiro com módulo ECA captura mercado), não regulatória strict-sense.

### 3.2 Conclusão "Fator=5 é apropriado"

```
Por quê? (1) → Porque é uma lei federal nova com impacto direto
   Por quê? (2) → Porque envolve menores (categoria sensível na LGPD)
      Por quê? (3) → Porque gera responsabilidade civil/administrativa elevada
                      → REVELAÇÃO: a justificativa é coerente, MAS fator=5 deveria ser
                        condicionado à exposição da audience específica.
                        SaaS_pme genérico que não atende menores teria fator=2-3,
                        não 5. Fator=5 monolítico viola R3 (sub-engine por audience).
```

**Insight**: Fator deve ser per-audience, não global.

### 3.3 Conclusão "VVV=0.98 reflete a verdade"

```
Por quê? (1) → Porque a lei existe, é pública, é verificável
   Por quê? (2) → Porque foi marcado como "VALIDADO" no fonte_status
      Por quê? (3) → Porque LLM em narrativa gerou esse score baseado na clareza textual
                      → REVELAÇÃO: VVV=0.98 mede VERDADE do enunciado descritivo
                        ("ECA Digital existe e exige age verification") → CORRETO.
                        Mas o item COMUNICA "urgência" — e essa parte tem VVV mais baixo
                        (~0.55-0.65, conforme C7-C8 acima).
                        Há CONFLAÇÃO entre VVV-da-existência e VVV-da-urgência.
```

**Insight**: VVV agregado mascara dois VVVs distintos.

---

## 4. FALÁCIAS POTENCIAIS DETECTADAS

| # | Falácia | Onde aparece |
|---|---------|--------------|
| Fl1 | Apelo à autoridade | "Lei federal publicada" → assumir alto impacto sem avaliar regulamentação |
| Fl2 | Falsa equivalência | Existência da lei tratada como equivalente a urgência operacional |
| Fl3 | Generalização apressada | Fator=5 aplicado a 5 audiences sem segmentação |
| Fl4 | Falácia da recência | Lei nova → assumida como mais impactante que LGPD/MCI consolidadas |
| Fl5 | Petição de princípio | "Urgência" usada como justificativa de "urgência" no encadeamento sqia_trace original |

---

## 5. QUESTÕES ABERTAS CRÍTICAS (input para Estágio I)

| # | Questão aberta | Por que importa |
|---|---------------|-----------------|
| Q-O1 | Qual o custo médio de implementar age-verification adequada por audience? | Define ROI do módulo |
| Q-O2 | Existe regulamentação ANPD/ANATEL específica entre 09/2025 e 05/2026? | Define obrigações concretas |
| Q-O3 | Quais concorrentes já anunciaram módulo ECA-compliance? | Define janela competitiva |
| Q-O4 | Qual a posição do SaaS na cadeia de responsabilidade (operador vs controlador)? | Define exposição direta |
| Q-O5 | Há jurisprudência aplicando a lei mesmo antes da vigência (ex: tutela antecipada)? | Define risco antecipado |
| Q-O6 | Quanto custa NÃO ter o módulo (perda de oportunidade comercial)? | Define urgência comercial |

---

## 6. TRACE-Q (formato canônico OMNIBUS)

```text
[TRACE-Q] Classificação epistemológica:
  - 14 claims classificadas: 5 FACT, 2 INFERENCE, 3 SPECULATION, 4 BELIEF
  - Núcleo duro irrefutável: 4 claims (existência da lei, menção age verification, vacatio, audiences afetadas)
  - Resto é interpretação ou projeção

[TRACE-Q] Falácias potenciais detectadas:
  - 5 falácias mapeadas (autoridade, falsa equivalência, generalização, recência, petição de princípio)
  - Principal: conflação entre VVV-da-existência (alto, justificado) e VVV-da-urgência (médio, não comprovado)

[TRACE-Q] Questões abertas críticas:
  - 6 questões abertas que o Estágio I deve endereçar via síntese

[TRACE-Q] Falsificação Popperiana:
  - Análise é falsificável (3 condições de invalidação identificadas) → científica

[TRACE-Q] Recursão "Por quê?" 3x revelou:
  - (a) Urgência real é COMERCIAL, não regulatória
  - (b) Fator deve ser per-audience (R3 GOVERNANCE)
  - (c) VVV agregado mascara 2 VVVs distintos (existência ≠ urgência)
```

---

## Status final do Estágio Q
- 5N completas: SIM
- ≥5 ocorrências de FACT|INFERENCE|SPECULATION|BELIEF: SIM (14 ocorrências)
- 3× "Por quê?" em ≥3 conclusões: SIM (3 conclusões aprofundadas)
- Falsificabilidade verificada: SIM (científica)
- Próximo estágio: [I] Inovador deve sintetizar via analogias + FDC-U + escalas
