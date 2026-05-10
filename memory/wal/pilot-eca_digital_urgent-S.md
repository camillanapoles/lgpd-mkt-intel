# PILOT S→Q→I→A — Estágio [S] Socrático
## Item: ceu/eca_digital_urgent
## Timestamp: 2026-05-09T22:42:00-03:00
## Agente: stage-s-pilot
## Modo: read-only — ZERO conclusões — apenas decomposição em primeiros princípios

---

## 1. EPOMETRISMO — "O que eu realmente sei sobre este item?"

### 1.1 Fatos verificáveis sobre Lei 15.211/2025 (ECA Digital)

| # | Fact | Source | Evidence Type |
|---|------|--------|---------------|
| F1 | Lei nº 15.211/2025 foi sancionada em 26/setembro/2025 | DOU 29/09/2025; planalto.gov.br/ccivil_03/_Ato2023-2026/2025/Lei/L15211.htm | Ato normativo federal publicado |
| F2 | Lei é apelidada de "ECA Digital" e altera Estatuto da Criança e do Adolescente (Lei 8.069/1990) | Ementa oficial da Lei 15.211/2025 | Ementa do ato |
| F3 | Lei estabelece deveres para "fornecedores de produtos e serviços de tecnologia da informação" relativos a crianças/adolescentes | Art. 3º Lei 15.211/2025 | Texto legal |
| F4 | Inclui dever de "implementar mecanismos para verificação de idade" (age verification) — Art. 5º | Art. 5º Lei 15.211/2025 | Texto legal |
| F5 | Vacatio legis: lei entra em vigor 12 meses após publicação (≈ 29/09/2026) | Art. final Lei 15.211/2025 | Texto legal |
| F6 | Regulamentação setorial fica a cargo da ANATEL/SENACON/ANPD conforme escopo (a regulamentar) | Lei 15.211/2025 + competência institucional vigente | Texto legal + Lei 12.965/14 (MCI) |
| F7 | Item está classificado na dimensão CEU (Céu — clima/ambiente externo) do framework SNTI | strategic-data-unified.json §snti.dimensions.ceu.items | JSON do projeto |
| F8 | Item carrega `vvv=0.98`, `fator=5`, `polaridade=+1`, `vvv_decay=0.49` no estado atual | strategic-data-unified.json (linha localizada na busca) | JSON do projeto |
| F9 | Justificativa de decay (`vvv_decay_reason`) declara: "narrative-only — pending real S→Q→I→A pipeline execution per OMNIBUS" | strategic-data-unified.json | JSON do projeto |
| F10 | LGPD (Lei 13.709/2018) Art. 14 já exige consentimento específico de pais/responsáveis para tratamento de dados de crianças <12 anos | Lei 13.709/2018 Art. 14 §1º | Texto legal pré-existente |
| F11 | Marco Civil da Internet (Lei 12.965/14) já prevê princípios de proteção, mas não exige age-verification ativa | Lei 12.965/14 Art. 3º, 7º | Texto legal pré-existente |

### 1.2 Fatos verificáveis sobre o produto/contexto SaaS LGPD

| # | Fact | Source | Evidence Type |
|---|------|--------|---------------|
| F12 | Audiences mapeadas no JSON incluem prefeitura, hospital, SaaS_pme, escritorio_juridico, empresa_grande | strategic-data-unified.json §audiences | JSON |
| F13 | Audience "prefeitura" tem dados envolvendo CRAS/CREAS, escolas, saúde infantil — interface com menores | strategic-data-unified.json §audiences.prefeitura.persona | JSON |
| F14 | Audience "hospital" coleta dados de pacientes pediátricos | strategic-data-unified.json §audiences.hospital | JSON |
| F15 | Audience "escritorio_juridico" inclui demandas de família/infância | strategic-data-unified.json §audiences.escritorio_juridico | JSON |

---

## 2. MAIÊUTICA — Premissas ocultas a serem partejadas

### 2.1 Premissas ocultas detectadas no item original

| # | Premissa oculta | Onde aparece | Status |
|---|----------------|--------------|--------|
| P1 | "ECA Digital cria urgência REAL" assume que prefeituras já não estão em compliance prévio (LGPD Art. 14) | sqia_trace.socratic + .innovator | NÃO declarada — assume, não prova |
| P2 | "Age verification obrigatório" implica que o ônus cai sobre o cliente da SaaS — pode ser sobre a SaaS-fornecedora | description + explicacao | NÃO declarada — ambiguidade de sujeito de direito |
| P3 | Fator 5 (máximo) assume impacto homogêneo em todas as 5 audiences | fator=5 sem segmentação | NÃO declarada — falta análise per-segmento (R3 GOVERNANCE) |
| P4 | VVV=0.98 trata "existência da lei" e "impacto regulatório" como mesma dimensão verificável | vvv=0.98 + fonte_status=VALIDADO | Conflação — existência (0.98) ≠ impacto (?.??) |
| P5 | "Urgência" assume vacatio legis curto + regulamentação pronta no D-Day | "urgencia municipal" criterio | NÃO declarada — vacatio é 12 meses, regulamentação ANPD/ANATEL atrasada é cenário plausível |
| P6 | shelf_life=12m assume que regulamentação se estabilizará em 1 ano | shelf_life | NÃO declarada — mudança regulatória pode estender |

### 2.2 Verificação de XY-Problem

- **Pergunta declarada (X)**: "ECA Digital cria urgência real para prefeituras?"
- **Pergunta possivelmente real (Y)**: "Como o portfólio do nosso SaaS deve precificar/empacotar o módulo ECA-compliance para as 5 audiences nos próximos 12 meses?"
- **Diagnóstico**: O `description` está formulado como **fato regulatório** (status), mas o uso real do item no engine é **decisão de produto/posicionamento** (ação). Há gap entre formulação e uso.

---

## 3. DIVISÃO — Fragmentação em elementos atômicos

O item `eca_digital_urgent` decompõe-se em 7 sub-elementos não-redutíveis:

```
eca_digital_urgent
├── E1. Existência da lei (binário: existe/não existe)
├── E2. Vigência temporal (data de entrada em vigor)
├── E3. Sujeitos passivos (quem deve cumprir)
├── E4. Obrigação substantiva (age verification — natureza técnica)
├── E5. Regulamentação infralegal (ANPD/ANATEL — pendente)
├── E6. Sanção/enforcement (multa, suspensão — depende de E5)
└── E7. Aplicabilidade ao SaaS (direta vs. indireta — varia por audience)
```

Cada sub-elemento tem nível de certeza distinto:
- E1, E2, E3, E4: HIGH (texto legal publicado)
- E5: LOW (pendente)
- E6: MEDIUM-LOW (depende de E5)
- E7: VARIABLE (depende da arquitetura de cada cliente)

---

## 4. DEFINIÇÃO — Precisão terminológica operacional

| Termo | Definição operacional usada neste pilot |
|-------|----------------------------------------|
| "ECA Digital" | Lei 15.211/2025 que altera Lei 8.069/90 (ECA) inserindo deveres digitais |
| "age verification" | Mecanismo técnico que estima/confirma faixa etária do usuário antes de coletar dado ou liberar acesso (não é definido em detalhe técnico na lei — fica para regulamentação) |
| "urgência" | Função de (proximidade do D-Day vigência) × (tempo necessário para implementação) × (custo do não-compliance) |
| "compliance obrigatório" | Estado em que o sujeito passivo cumpre todos os deveres do Art. 5º Lei 15.211/2025 + regulamentação aplicável |
| "prefeitura" (no contexto deste item) | Órgão público municipal que opera serviços com dados de menores (educação, saúde, assistência social) |
| "VVV" | Verificação Verdade Válida — score 0–1 sobre veracidade da AFIRMAÇÃO no item, NÃO sobre impacto da afirmação no negócio |
| "vvv_decay" | VVV ajustado por (a) decaimento temporal e (b) penalização por origem (narrative-llm vs pipeline-real) |
| "fator" | Peso 1–5 do item dentro da dimensão CEU para o cálculo do score SNTI |
| "polaridade" | +1 (item agrega ao score) / −1 (item subtrai) |
| "dimensão CEU" | Céu — fatores externos (ambiente regulatório, mercado, clima macro) — Sun Tzu cap. I §3 |

---

## 5. TRACE-S (formato canônico OMNIBUS)

```text
[TRACE-S] Primeiros princípios identificados:
  - 11 fatos verificáveis sobre Lei 15.211/2025 e contexto LGPD (F1-F11)
  - 4 fatos sobre audiences afetadas (F12-F15)
  - 7 sub-elementos atômicos (E1-E7) com níveis distintos de certeza
[TRACE-S] Premissas ocultas questionadas:
  - 6 premissas não-declaradas detectadas (P1-P6)
  - Conflação principal: existência da lei (alta certeza) vs impacto sobre SaaS (baixa-média certeza)
  - XY-Problem: item formulado como fato regulatório, usado como decisão de produto
[TRACE-S] Definições operacionais:
  - 10 termos definidos sem ambiguidade (ECA Digital, age verification, urgência, compliance,
    prefeitura, VVV, vvv_decay, fator, polaridade, dimensão CEU)
[TRACE-S] Status: complete — sem conclusões, apenas decomposição
```

---

## 6. Cited-Facts List (consolidado para uso pelo Estágio Q)

```yaml
facts:
  - id: F1
    claim: "Lei 15.211/2025 sancionada em 26/09/2025"
    source: "DOU 29/09/2025; planalto.gov.br"
  - id: F2
    claim: "Lei altera ECA (Lei 8.069/1990)"
    source: "Ementa Lei 15.211/2025"
  - id: F3
    claim: "Estabelece deveres para fornecedores de TI relativos a crianças/adolescentes"
    source: "Art. 3º Lei 15.211/2025"
  - id: F4
    claim: "Exige mecanismos de verificação de idade"
    source: "Art. 5º Lei 15.211/2025"
  - id: F5
    claim: "Vacatio legis 12 meses (≈ vigência 29/09/2026)"
    source: "Artigo final Lei 15.211/2025"
  - id: F6
    claim: "Regulamentação infralegal pendente (ANPD/ANATEL/SENACON)"
    source: "Lei 15.211/2025 + competências institucionais Lei 13.709/18 + Lei 12.965/14"
  - id: F7
    claim: "Item classificado em CEU.items"
    source: "strategic-data-unified.json"
  - id: F8
    claim: "VVV=0.98 fator=5 polaridade=+1 vvv_decay=0.49 no estado atual"
    source: "strategic-data-unified.json"
  - id: F9
    claim: "vvv_decay_reason indica que pipeline real ainda não foi rodado"
    source: "strategic-data-unified.json"
  - id: F10
    claim: "LGPD Art. 14 §1º já exige consentimento parental para <12 anos"
    source: "Lei 13.709/2018"
  - id: F11
    claim: "MCI não exige age-verification ativa"
    source: "Lei 12.965/2014"
  - id: F12
    claim: "5 audiences mapeadas: prefeitura/hospital/SaaS_pme/escritorio_juridico/empresa_grande"
    source: "strategic-data-unified.json §audiences"
  - id: F13-F15
    claim: "Subset das audiences interage com dados de menores (prefeitura/hospital/escritorio_juridico)"
    source: "strategic-data-unified.json §audiences.*.persona"
hidden_premises:
  - P1: "Não-compliance prévio assumido"
  - P2: "Sujeito passivo: cliente vs SaaS — ambiguidade"
  - P3: "Impacto homogêneo nas 5 audiences"
  - P4: "Existência ≡ impacto na mesma métrica VVV"
  - P5: "Vacatio + regulamentação prontos no D-Day"
  - P6: "Estabilização regulatória em 12m"
atomic_elements: [E1, E2, E3, E4, E5, E6, E7]
xy_problem_detected: true
```

---

## Status final do Estágio S
- Decomposição: COMPLETE
- Conclusões geradas: ZERO (mandato cumprido)
- Próximo estágio: [Q] Questionador deve receber esta lista de fatos + premissas + sub-elementos
