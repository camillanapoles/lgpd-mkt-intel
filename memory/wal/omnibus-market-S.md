# [TRACE-S] Market Research + FDC-U — Stage Socrático
**Timestamp**: 2026-05-09T00:00:00-03:00
**Pipeline**: OMNIBUS S→Q→I→A | Stage 1 of 4
**Inputs**: market-research-2025.md, fdc-u-validation.md, market-sizing.yaml

---

## Market Sizing Extraído

| Métrica | Valor | Fonte Declarada | Tipo (Primária/Estimativa) |
|---------|-------|-----------------|--------------------------|
| TAM — municipal universe | 5,570 municípios | IBGE MUNIC 2024 | Primária (dado oficial) |
| TAM — sem LGPD | 4,010 municípios (72%) | IBGE MUNIC 2024 | Primária (dado oficial) |
| TAM — monetizado (yaml) | R$ 2.0B+ | Estimativa interna (R$500K/mun) | Estimativa LLM |
| TAM — monetizado (md) | R$ 2.8M–R$11.1M/ano | Estimativa interna (R$500–2000/ano) | Estimativa LLM |
| SAM — municípios 20-100K | 1,316–1,400 municípios | IBGE Censo 2022 + distribuição estimada | Estimativa (derivada de primária) |
| SAM — monetizado (yaml) | R$ 450M+ | Estimativa interna (R$300K–500K/mun) | Estimativa LLM |
| SAM — monetizado (md) | R$ 2M–R$8M/ano | Estimativa interna | Estimativa LLM |
| SOM — municípios alvo | 50/ano × 3 anos = 150 | Estimativa de capacidade operacional | Estimativa LLM |
| SOM — monetizado (yaml) | R$ 750K/ano / R$ 2.25M total | Ticket médio R$15K × 50 mun | Estimativa LLM |
| SOM — monetizado (md) | R$ 700K–R$2.8M/ano | Estimativa interna | Estimativa LLM |
| BNDES+IDB Prodigital | R$ 1 bilhão (US$180M) | IDB + BNDES comunicados oficiais Jan 2025 | Primária |
| Custo data breach Brasil | R$ 7.19M | IBM Cost of Data Breach 2024 | Estimativa (pesquisa privada) |
| Penalidade ANPD máxima | R$ 50M / 2% receita | Lei LGPD Art.52 | Primária (lei) |
| ARPU target | R$397/mês | strategic-data-unified.json | Estimativa interna |
| Break-even | 350 clientes / MRR R$139K / mês 42 | strategic-data-unified.json | Estimativa interna |
| Funding requerido | R$ 960K | strategic-data-unified.json | Estimativa interna |
| LTV:CAC | 6.0 | strategic-data-unified.json | Estimativa interna |
| Payback | 4 meses | strategic-data-unified.json | Estimativa interna |

**Nota crítica — Conflito interno TAM:** O market-sizing.yaml usa ticket médio R$500K/município (adequação completa) → TAM R$2.0B+. O market-research-2025.md usa ticket R$500–2000/ANO (SaaS) → TAM R$2.8M–R$11.1M. Diferença de 3 ordens de magnitude. Este conflito é a maior inconsistência do market sizing.

---

## FDC-U Atual (Extraído de fdc-u-validation.md)

- **Número de itens validados**: 5 (Top 5 Critical Priorities) + 5 Quick Wins = 10 itens
- **Dimensões com pesos declarados**:

| Dimensão | Peso | Função |
|----------|------|--------|
| Impacto | 0.30 | Direta (+) — maior é melhor |
| Urgência | 0.25 | Direta (+) — maior é melhor |
| VVV | 0.20 | Direta (+) — maior é melhor |
| Esforço | 0.15 | Inversa (−) — menor é melhor |
| Risco | 0.10 | Inversa (−) — menor é melhor |

- **Pesos somam**: 0.30 + 0.25 + 0.20 + 0.15 + 0.10 = **1.00** ✓
- **Escala**: Impacto, Urgência, Esforço, Risco em 0-10; VVV em 0-1 (escala diferente!)

**Problema de escala detectado**: VVV está em escala 0-1 enquanto as demais dimensões estão em 0-10. O cálculo usa `w_VVV × f_VVV(A_VVV)` com `A_VVV ∈ [0,1]` em vez de `[0,10]`. Isso comprime artificialmente a pontuação VVV por fator 10.

**Exemplo LOIs_Assinadas**: VVV=0.0 → pontuação = 0.20 × 0.0 = 0.0. Se VVV fosse normalizado para 0-10 (0.0 → 0), resultado seria igual. Mas para VVV=0.8 (Consorcios_Map): pontuação = 0.20 × 0.8 = 0.16 (vs potencial máximo de 0.20 × 10 = 2.0 se escala fosse 0-10). **A dimensão VVV está subponderada efetivamente em 10×**.

---

## Mapa Fonte → Tipo

| Dado | Fonte | Tipo |
|------|-------|------|
| 5,570 municípios brasileiros | IBGE MUNIC 2024 (oficial) | Primária |
| 28% têm responsável LGPD / 72% sem | IBGE MUNIC 2024 (oficial) | Primária |
| 4,010 municípios sem LGPD | Derivação direta de IBGE | Primária derivada |
| 1,316–1,400 municípios 20-100K | IBGE Censo 2022 + estimativa distribuição | Estimativa baseada em primária |
| ANPD transformada (MP 1.317/2025) | gov.br/anpd oficial | Primária |
| ECA Digital Lei 15.211/2025 | Planalto / Diário Oficial | Primária |
| Sanções ANPD 2023-2024 | Confidata (com refs oficiais) | Secundária (VVV 0.9) |
| BNDES+IDB R$1 bilhão | BNDES + IDB comunicados oficiais | Primária |
| TAM R$2.0B+ | Estimativa interna (R$500K/mun) | Estimativa LLM — sem evidência |
| TAM R$2.8M–R$11.1M/ano | Estimativa interna (R$500–2000/ano) | Estimativa LLM — sem evidência |
| SAM R$450M+ | Estimativa interna (R$300K–500K/mun) | Estimativa LLM — sem evidência |
| ARPU R$397/mês | strategic-data-unified.json | Estimativa interna não verificada |
| Break-even mês 42, R$960K | strategic-data-unified.json | Estimativa interna não verificada |
| LTV:CAC 6.0 / Payback 4 meses | strategic-data-unified.json | Estimativa interna não verificada |
| Custo data breach R$7.19M | IBM Cost of Data Breach 2024 | Pesquisa privada (VVV 0.90) |
| R$15K ticket médio SOM | "Estimativa baseada em mercado consultoria" | Estimativa sem fonte primária |
| Preço consultoria R$5K–R$20K | Pesquisa mercado consultoria LGPD 2024 | Secundária (não citada) |
| NeoGov R$5.275/mês / R$600K total | strategic-data-unified.json (transcrição) | Benchmark não verificado externamente |
| Confidata preços R$497–R$3.497/mês | Site oficial Confidata | Primária |
| CIGA: 345 municípios, 22M hab | CIGA oficial site | Primária |
| Market score geral 8.65/10 | strategic-data-unified.json (interno) | Estimativa interna |

---

## Premissas Implícitas no Market Research

1. **Premissa de preço**: Ticket médio R$500–2000/ano (SaaS) é viável para municípios de 20-100K que têm "limited IT capacity" — sem validação de disposição a pagar (WTP).
2. **Premissa de conversão**: Capture rates 0.5%/1.5%/3.5% sobre SAM são assumidas sem benchmark de mercado B2G comparável.
3. **Premissa de ticket alternativo**: market-sizing.yaml assume R$500K/município (1 a 2 ordens de magnitude maior) — sugere confusão entre modelo consultoria e modelo SaaS.
4. **Premissa de consortium**: CIGA (345 municípios) e CIMINAS como canais imediatos — sem validação de interesse de parceria ou modelo comercial.
5. **Premissa de enforcement**: Aceleração ANPD aumenta demanda — sem quantificar elasticidade de demanda a enforcement.
6. **Premissa de substituição**: Municípios atualmente sem LGPD não têm alternativa gratuita aceitável — mas compliance mínima pode ser feita internamente.
7. **Premissa BNDES**: R$1 bilhão Prodigital pode financiar soluções SaaS LGPD — mas limite por projeto US$2-40M sugere escopo muito maior que solução municipal isolada.
8. **Premissa de barreira**: LOI = validação de mercado — mas LOI ≠ contrato assinado nem pagamento confirmado.
9. **Premissa competitiva**: Confidata "too expensive" para pequenos municípios — sem comparação direta de custo total de adequação vs preço SaaS.
10. **Premissa ICT**: Prerrogativas legais ICT (Art.75 IV) como diferencial — validade jurídica pendente (Parecer_Juridico VVV 0.5).
