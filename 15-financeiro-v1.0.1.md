---
id: NEOGOV-V21-CAP15-FINANCEIRO
filename: 15-financeiro-v1.0.1.md
created_at: 2026-05-16T09:45:00Z
type: BUSINESS_PLAN_CHAPTER
chapter: 15
title: Análise Financeira Consolidada (DRE + FCD + Sub-estratificação Classe III)
version: v1.0.1
data_source: data/neogov-pricing-cost-ssot-v1.0.7.json + data/dre_fcd.py + curva v2
parent_chapters: [12-bmc-v2.1.5.6, 13-vpc-v1.0.2]
sprint: W1.3-FINANCEIRO
edicao: 1
branch: retificacao-validacao-preco-novo
absorve_debito: D17 (sub-estratificação Classe III)
mandato_atendido: USUARIO_2026-05-16 "PROSSIGA P5 · Cap 15 Financeiro · WAL contínuo"
canonical_chain: [ssot-v1.0.7, dre_fcd.py, curva_ponto_sucesso_v2.py, APENDICE-N]
quality_target: PMQS 9.5 · VVV >= 0.75 (financeiro tem estimativas declaradas)
tags: [financeiro, dre, fcd, vpl, 3-cenarios, classe-iii-sub, ssot-v1.0.7]
mandatos_honrados: [RGO-9 honestidade, D-015 lastro, TEXT-AS-OBJECT, AP-13 estimativa marcada, AP-14]
---

# Capítulo 15 · Análise Financeira Consolidada
## DRE + FCD · 3 Cenários · Sub-estratificação Classe III

> **Por que este capítulo existe**: os Caps 12/13 definiram *quanto cobrar* e *para quem*. O Cap 15 responde a pergunta que o investidor faz primeiro — *isso dá dinheiro, quando, e quanto vale hoje?* Sem ele, o BP tem preço mas não tem viabilidade demonstrada.

---

## §15.0 · Proveniência (cadeia de fidelidade · Apêndice L)

```
financeiro_chain = {
  receita:    LÓGICA  → curva v2 (price.validated SSOT v1.0.7 · função reproduzível)
  custo_fixo: FATO    → CF R$142.251/mês (folha+infra · Apêndice E web_search)
  margem:     LÓGICA  → ABC (Apêndice I · margem contrib 72% derivada)
  desconto:   🟡 D-015 → 25% (early-stage BR · SELIC+prêmio · D001-NOVO-20 calibra)
  cenários:   🟡 D-015 → ancorados ssot.scenarios (M12/M36 · interpolado)
}
```

**Por que declarar isso primeiro?** Finanças projetadas sempre embutem hipóteses. A diferença entre um plano honesto e um inflado é se as hipóteses estão **rotuladas** ou **escondidas**. Aqui, tudo que é estimativa carrega 🟡 D-015.

---

## §15.1 · Premissas (e por que cada uma)

| Premissa | Valor | Classe | Por que este valor |
|---|---|:--:|---|
| CF anual fixo | R$ 1.707.012 | **FATO** | CF mensal R$142.251 × 12 · folha+infra web_search (Apêndice E) |
| Margem de contribuição | 72% | 🟡 D-015 | Derivada da curva v2 (receita−CSC ABC ponderado mix). Calibra D001-NOVO-8 |
| Taxa de desconto (FCD) | 25% a.a. | 🟡 D-015 | Early-stage BR SaaS = SELIC base + prêmio risco equity. Faixa prática VC BR 20-30%; usei o meio. **Por quê 25%?** Abaixo subvaloriza risco; acima pune projeto saudável. D001-NOVO-20 calibra com captação real |
| Trajetória ARR | ver §15.2 | 🟡 D-015 | Ancorada em `ssot.scenarios` (M12 e M36 são os pontos firmes; anos intermediários interpolados) |

> **Lição pedagógica**: a taxa de desconto é a premissa que mais distorce um FCD. Um plano que usa 10% (taxa de renda fixa) infla o VPL artificialmente. 25% reconhece que uma startup pré-receita é mais arriscada que um título público — é honestidade financeira, não pessimismo.

---

## §15.2 · DRE Projetado · 3 Cenários (R$ milhões · 5 anos)

**Por que 3 cenários e não 1 número?** Um único número projetado é uma ficção de precisão. Três cenários (P25/P50/P75) comunicam a **distribuição de resultados possíveis** — o investidor decide com base no range, não num ponto.

### Cenário A · P25 Conservador (prob. 25%)

| | Ano 1 | Ano 2 | Ano 3 | Ano 4 | Ano 5 |
|---|---:|---:|---:|---:|---:|
| Receita (ARR) | 0,9 | 2,2 | 4,5 | 6,0 | 7,5 |
| **EBITDA** | **-1,1** | **-0,1** | **+1,5** | **+2,6** | **+3,7** |

> Mesmo no cenário ruim, o EBITDA vira positivo no **Ano 3**. Isso importa: significa que o pior caso ainda é um negócio que se sustenta — só demora mais.

### Cenário B · P50 Provável (prob. 50%)

| | Ano 1 | Ano 2 | Ano 3 | Ano 4 | Ano 5 |
|---|---:|---:|---:|---:|---:|
| Receita (ARR) | 2,3 | 7,0 | 14,0 | 22,0 | 30,0 |
| **EBITDA** | **-0,1** | **+3,3** | **+8,4** | **+14,1** | **+19,9** |

> O cenário central: EBITDA quase neutro no Ano 1, forte tração a partir do Ano 2. É a trajetória que a curva v2 sustenta (sucesso global N=163 ≈ Ano 3).

### Cenário C · P75 Otimista (prob. 25%)

| | Ano 1 | Ano 2 | Ano 3 | Ano 4 | Ano 5 |
|---|---:|---:|---:|---:|---:|
| Receita (ARR) | 4,5 | 14,0 | 28,0 | 40,0 | 52,0 |
| **EBITDA** | **+1,5** | **+8,4** | **+18,5** | **+27,1** | **+35,7** |

> EBITDA positivo já no Ano 1. Escala industrial (a tese da Camila CTO) materializada.

---

## §15.3 · FCD · Valor Presente Líquido (desconto 25%)

**Por que trazer a valor presente?** R$ 30M no Ano 5 não vale R$ 30M hoje — vale menos, porque (a) há risco de não acontecer e (b) dinheiro hoje rende. O FCD traduz o futuro incerto em um número comparável hoje.

| Cenário | VPL 5 anos | × Probabilidade | Contribuição |
|---|---:|:--:|---:|
| A · P25 conservador | R$ 2,14M | 0,25 | R$ 0,53M |
| B · P50 provável | R$ 18,69M | 0,50 | R$ 9,34M |
| C · P75 otimista | R$ 38,84M | 0,25 | R$ 9,71M |
| **🎯 E[VPL] esperado ponderado** | | | **R$ 19,59M** |

> **Como ler isto**: o valor esperado (média ponderada pela probabilidade) é **R$ 19,6M**. Note a assimetria: o cenário ruim (A) ainda dá VPL **positivo** (R$ 2,1M) — o downside é limitado. O upside (C) é 18× o downside. Esse perfil risco-retorno (downside protegido, upside grande) é exatamente o que torna o negócio investível.

---

## §15.4 · Sub-estratificação Classe III (resolve débito D17)

**Por que isto estava errado antes?** O Apêndice N expôs: tratar Classe III (arrecadação >R$1M/ano, com casos até R$143M) como **tier único de R$9.000** era o mesmo erro do "hospital único" — agrupar realidades 100× diferentes num preço só. D17 exigia corrigir.

| Sub-faixa | Preço/mês | CSC | Margem | % de Classe III |
|---|---:|---:|:--:|:--:|
| **III-A** (arrecad. R$1-3M/ano) | R$ 5.000 | R$ 1.217 | 76% | ~55% |
| **III-B** (arrecad. R$3-10M/ano) | R$ 15.000 | R$ 6.677 | 55% | ~35% |
| **III-C** (arrecad. >R$10M · custom) | R$ 30.000+ | R$ 18.727 | 38% | ~10% |

> 🟡 D-015: as sub-faixas são análogas (distribuição log-típica de arrecadação). **Por que isto é melhor que o R$9.000 único?** Porque captura valor proporcional: o 9º RI Rio (R$71,9M/semestre) pagando R$9.000 era subprecificação grosseira; agora cai em III-C custom. D001-NOVO-17 calibra com o dado real (sigiloso · acesso restrito Justiça Aberta).

**Substitui** `ssot.cartorio_classe3` provisório → atualizar SSOT (próximo ciclo).

---

## §15.5 · Síntese Financeira

```
Break-even operacional:  37 clientes (curva v2 · Wave1 mix)
Sucesso global:          163 clientes · ARR R$12M · margem op 49%
E[VPL] 5 anos:           R$ 19,59M (ponderado)
Cenário provável (B):    VPL R$ 18,69M · EBITDA+ a partir Ano 2
Downside (A):            VPL +R$2,14M (positivo · risco limitado)
Uplift cartório W3-5:    +R$312k/mês (cenário separado · 🟡 2% TAM)
```

> **A história que os números contam**: NeoGov precisa de ~37 clientes para parar de queimar caixa e ~163 para ser um sucesso pleno. No cenário provável, isso acontece até o Ano 3, gerando um negócio que vale ~R$19M hoje. O risco existe (Ano 1 queima caixa), mas é limitado — mesmo o cenário ruim retorna capital.

---

## §15.6 · Auto-avaliação PMQS + Devil's Advocate

| Critério | Peso | Score |
|---|:--:|:--:|
| CE Completude | 15% | 9.4 |
| PI Precisão | 15% | 9.6 |
| CC Clareza | 10% | 9.6 |
| PRI Profundidade | 20% | 9.5 |
| RA Relevância | 15% | 9.7 |
| EIC Estrutura | 10% | 9.4 |
| OVA Originalidade | 15% | 9.3 |

**PMQS Bruto** = 9.50 · **VVV** = 0.76 (cenários/desconto = estimativa declarada) · **PMQS Final = 7.22** 🟡 (honesto · sobe pós D001-NOVO-7/20 piloto)

> ⚔️ **Devil's advocate 1**: "Margem 72% é otimista." → Procede como risco. Deriva da curva v2 (ABC). Mas a margem inclui clusters de baixo CSC (Gamma/Épsilon CSC <R$500). É ponderada pelo mix, não arbitrária. D001-NOVO-8 calibra.
> ⚔️ **2**: "Trajetória ARR Ano1→5 é interpolada." → Verdade. Pontos firmes = M12/M36 (ssot.scenarios). Anos 2/4/5 interpolados · marcado D-015. Não fabricado — ancorado.
> ⚔️ **3**: "FCD ignora necessidade de capital de giro / aporte." → Procede. Este cap mostra VPL operacional. Necessidade de aporte (queima Ano 1 ≈ R$1,1M cenário A) deve virar **D001-NOVO-21** (dimensionar rodada). Honestamente registrado.

---

## §15.7 · Backlinks

| Consome | Como |
|---|---|
| Cap 16 Investimento | E[VPL] R$19,6M + queima Ano1 → dimensionar rodada (D001-NOVO-21) |
| Cap 17 Riscos | Cenário A + estimativas D-015 = riscos quantificados |
| Pitch investidor | E[VPL] + perfil risco assimétrico |

---

**FIM Cap 15 v1.0.1** · DRE+FCD+ClasseIII · lê SSOT v1.0.7 · D17 absorvido · PMQS 7.22 honesto · novos débitos D001-NOVO-20/21
