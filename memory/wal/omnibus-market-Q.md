# [TRACE-Q] Market Research + FDC-U — Stage Questionador
**Timestamp**: 2026-05-09T00:05:00-03:00
**Pipeline**: OMNIBUS S→Q→I→A | Stage 2 of 4
**Depends on**: omnibus-market-S.md

---

## Evidence Scale por Claim

| Claim | Classificação | Fonte Verificável? | Justificativa |
|-------|--------------|-------------------|---------------|
| 5,570 municípios no Brasil | **FACT** | SIM — IBGE MUNIC 2024 | Dado censitário oficial, data ref. Jul 2024 |
| 72% sem responsável LGPD / 28% com | **FACT** | SIM — IBGE MUNIC 2024 | Pesquisa direta com municípios, metodologia IBGE |
| 4,010 municípios sem LGPD | **FACT** | SIM — derivação direta 5570×0.72 | Cálculo determinístico de dado oficial |
| TAM = R$2.0B+ (yaml) | **SPECULATION** | NÃO — estimativa sem fonte | R$500K/município nunca foi cotado/validado em mercado B2G real |
| TAM = R$2.8M–R$11.1M/ano (md) | **SPECULATION** | NÃO — estimativa sem fonte | R$500–2000/ano por município não tem benchmark verificado |
| SAM = 1,316–1,400 municípios | **INFERENCE** | PARCIAL — Censo 2022 + distribuição | Subtração direta dos extremos (<20K e >100K) do total |
| SAM = R$450M+ | **SPECULATION** | NÃO — estimativa interna | R$300K–500K/município multiplica por SAM sem WTP evidence |
| SOM = 50 mun/ano × 3 anos | **BELIEF** | NÃO — capacidade operacional interna | Baseado em capacidade de equipe não definida, sem benchmark vendas B2G |
| SOM = R$750K/ano (ticket R$15K) | **SPECULATION** | NÃO — "estimativa de mercado consultoria" | Ticket R$15K não evidenciado por nenhuma transação real |
| ARPU R$397/mês | **BELIEF** | NÃO — strategic-data-unified.json interno | Valor arbitrário sem ancoragem em WTP ou benchmark |
| Break-even mês 42 / R$960K funding | **BELIEF** | NÃO — modelo interno não auditado | CAC, LTV, churn não baseados em dados de mercado real |
| LTV:CAC = 6.0 / Payback = 4 meses | **SPECULATION** | NÃO — modelo interno | Payback de 4 meses é extremamente otimista para B2G público |
| MP 1.317/2025 transforma ANPD | **FACT** | SIM — gov.br/anpd + DOU | Medida Provisória publicada, verificável |
| ECA Digital Lei 15.211/2025 | **FACT** | SIM — Planalto + DOU | Lei promulgada, vigência março 2026 |
| BNDES+IDB R$1 bilhão Prodigital | **FACT** | SIM — BNDES + IDB oficiais Jan 2025 | Comunicados oficiais de ambas instituições |
| Lei 14.133/2021 Art.75 IV – R$50K dispensa | **FACT** | SIM — texto de lei federal | Lei aprovada, artigo verificável |
| Confidata preços R$497–R$3.497/mês | **FACT** | SIM — site confidata.com.br | Preços públicos do site |
| NeoGov R$5.275/mês / R$600K | **INFERENCE** | PARCIAL — transcrição interna | Dado de transcrição, não verificado em fonte pública |
| CIGA: 345 municípios / 22M hab | **FACT** | SIM — consorciociga.gov.br | Site oficial do consórcio |
| 8,700+ reclamações titulares 2025 | **INFERENCE** | PARCIAL — ANPD Instagram oficial | Canal oficial mas não publicação formal |
| Serasa: 86% grandes empresas adaptadas | **INFERENCE** | PARCIAL — Serasa (parte interessada) | Empresa cita próprio dado, possível viés |
| Score geral mercado 8.65/10 | **BELIEF** | NÃO — weighted scorecard interno | Pesos não auditados, scores subjetivos |
| Custo data breach R$7.19M | **FACT** | SIM — IBM report (metodologia privada) | IBM Report verificável mas metodologia proprietária |
| ANPD prioridades 2026-2027 | **FACT** | SIM — gov.br/anpd oficial | Mapa publicado oficial |
| Capture rate 0.5%/1.5%/3.5% | **BELIEF** | NÃO — sem benchmark B2G comparável | Taxa de conversão em B2G público municipal sem precedente citado |
| Window 2026-2027 para entrada | **INFERENCE** | PARCIAL — ciclo eleitoral + ANPD | Lógica válida mas quantificação do impacto não evidenciada |
| Cloud Brazil $18.1B → $86.6B 2034 | **INFERENCE** | PARCIAL — IMARC 2025 (firma privada) | Projeção de mercado de research house, não verificável independentemente |

---

## Validação FDC-U

### Verificação de Pesos

- **Pesos somam 1.0**: SIM — soma: 0.30 + 0.25 + 0.20 + 0.15 + 0.10 = **1.00** ✓

### Ortogonalidade das Dimensões

| Par de Dimensões | Overlap? | Problema |
|------------------|----------|---------|
| Impacto ↔ Urgência | **SIM — OVERLAP CRÍTICO** | "Impacto alto" frequentemente implica "urgência alta". Ex: LOIs_Assinadas recebe 10/10 em ambos sem critério diferenciador. Correlação estimada: r ≈ 0.7-0.85 |
| Impacto ↔ Risco | **SIM — OVERLAP MODERADO** | Itens de alto impacto tendem a ter alto risco. Ex: LOIs tem risco 9 e impacto 10 — ambos baseados na ausência de resultado |
| Esforço ↔ Risco | **OVERLAP LEVE** | Itens de alto esforço frequentemente têm maior risco de não conclusão |
| VVV ↔ demais | **NÃO** | VVV mede epistemologia (qualidade da fonte), não magnitude estratégica. Ortogonal ✓ |
| Urgência ↔ Risco | **OVERLAP MODERADO** | Alta urgência implica risco de atraso. Distinção não está operacionalizada |

**Diagnóstico ortogonalidade**: Impacto e Urgência são as dimensões com maior correlação interna. Peso combinado = 0.55 (55% do score total), amplificando potencialmente o mesmo sinal.

### Funções de Impacto por Dimensão

| Dimensão | Função Declarada | Correto? | Observação |
|----------|-----------------|----------|------------|
| Impacto | Direta (+) | ✓ | Mais impacto = melhor |
| Urgência | Direta (+) | ✓ | Mais urgência = melhor prioridade |
| VVV | Direta (+) | ✓ | Mais evidência = melhor |
| Esforço | Inversa (−) | ✓ | Mas implementação usa f(x)=x sem inversão explícita; score = w × A_esforço, onde A_esforço=1 (baixo) é melhor |
| Risco | Inversa (−) | ✓ | Mesma questão: score = w × A_risco, onde A_risco=1 seria melhor (baixo risco) |

**Problema de implementação**: Para Esforço e Risco a função inversa deveria ser f(x) = 10 - x (conforme FDC-U spec). Verificando com Consorcios_Map: Esforço=4 → pontuação = 0.15 × 4 = 0.60 (mas se inversa correta: 0.15 × (10-4) = 0.90). O relatório parece usar diretamente o valor sem inversão. **Bug de implementação detectado** — todos os scores com Esforço e Risco invertidos estão subestimados para itens de baixo esforço/risco.

**Exemplo**: LOIs_Assinadas Esforço=1 (fácil). Score atual = 0.15 × 1 = 0.15. Com inversão correta: 0.15 × (10-1) = 1.35. Diferença de 0.15 → 1.35 para este item.

### Problema de Escala VVV

VVV está em escala 0-1, demais dimensões em 0-10. Efeito:
- VVV máximo: 0.20 × 1.0 = 0.20 (peso efetivo 2% do score máximo de 10)
- Impacto máximo: 0.30 × 10 = 3.0 (peso efetivo 30%)
- VVV efetivamente pesa apenas 2% em vez de 20% declarado

**Conclusão**: FDC-U como implementado na fdc-u-validation.md tem 2 bugs: (1) VVV subescalado 10×, (2) funções inversas não invertidas para Esforço e Risco.

---

## Âncora Bias

**DETECTADO — âncora: NeoGov R$600K/ano**

Evidência:
- NeoGov aparece como único benchmark de preço B2G real (R$5.275/mês ≈ R$63.3K/ano)
- O TAM de R$2.0B+ no yaml usa R$500K/município — provavelmente âncora no NeoGov expandida
- O ARPU de R$397/mês parece ser um "desconto percebido" sobre Confidata starter (R$497/mês)
- Break-even de R$960K pode ter sido calibrado para parecer abaixo de funding seed típico (~$500K–$1M)

**Âncora secundária detectada: Confidata R$497/mês** — ARPU de R$397/mês posiciona produto como 20% mais barato sem evidência de diferencial que justifique essa ancoragem de preço.

---

## Questões Abertas (Gaps para Pesquisa Primária Real)

1. **WTP Municipal Real**: Quanto municípios de 20-100K pagam por serviços de TI/compliance? Dado ausente — nenhum orçamento real citado.
2. **TAM Monetizado**: Qual é o ticket médio real praticado no mercado B2G LGPD? Os dois documentos divergem em 3 ordens de magnitude (R$15K/ano vs R$2B+/TAM).
3. **Ciclo de Vendas B2G**: Quanto tempo leva um ciclo de venda municipal (licitação ou dispensa)? Dado ausente — afeta diretamente o payback de 4 meses.
4. **Churn Público**: Qual é a taxa de churn em contratos B2G SaaS? Zero citado — improvável.
5. **Capacidade BNDES Prodigital para LGPD**: O programa financia soluções SaaS ou apenas infraestrutura? Limite mínimo US$2M sugere escopo maior.
6. **Validação Parecer Jurídico Art.75 IV**: A dispensa licitação se aplica de fato a SaaS LGPD? VVV 0.5 — crítico para o modelo de go-to-market.
7. **ICT Prerrogativas**: Quais são exatamente as prerrogativas de ICT que a empresa possui? Citadas como diferencial mas não detalhadas.
8. **LOI Pipeline**: Quantas conversas ativas com municípios existem hoje? Zero LOIs assinadas mas sem pipeline qualificado citado.
9. **Consortium Commercial Model**: CIGA e CIMINAS cobrariam fee por canal? Modelo comercial não especificado.
10. **ANPD Municipal Enforcement**: Há algum processo aberto contra município por LGPD em 2025-2026? Dado ausente — sem multas confirmadas ainda.
