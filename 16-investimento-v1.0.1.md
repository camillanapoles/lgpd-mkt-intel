---
id: NEOGOV-V21-CAP16-INVESTIMENTO
filename: 16-investimento-v1.0.1.md
created_at: 2026-05-16T10:30:00Z
type: BUSINESS_PLAN_CHAPTER
chapter: 16
title: Tese de Investimento (Dimensionamento de Rodada + Valuation)
version: v1.0.1
data_source: data/neogov-pricing-cost-ssot-v1.0.8.json + data/runway_captacao.py + Cap 15
parent_chapters: [15-financeiro-v1.0.1]
sprint: W1.3-INVESTIMENTO
edicao: 1
branch: retificacao-validacao-preco-novo
resolve_debito: D001-NOVO-21 (dimensionar rodada)
gera_debito: D001-NOVO-22 (validar valuation c/ term sheet real)
mandato_atendido: USUARIO_2026-05-16 "Cap 16 · WAL contínuo · ondas de tasks"
canonical_chain: [ssot-v1.0.8, runway_captacao.py, 15-financeiro-v1.0.1, dre_fcd.py]
quality_target: PMQS 9.5 · VVV >= 0.72 (valuation pré-receita = estimativa declarada)
tags: [investimento, captacao, runway, valuation, diluicao, ssot-v1.0.8]
mandatos_honrados: [RGO-9 honestidade, D-015 lastro, AP-14 edição antecipada, estilo-educacional]
---

# Capítulo 16 · Tese de Investimento
## Dimensionamento de Rodada + Valuation

> **Por que este capítulo existe**: o Cap 15 provou que o negócio *vale* algo (E[VPL] R$19,6M). O Cap 16 responde a pergunta operacional do fundador e do investidor: *quanto capital, para quê, e a que custo de diluição?*

---

## §16.0 · O princípio que estrutura tudo (insight central)

```
ERRO COMUM:   "VPL é R$19,6M → posso levantar muito"  (dimensiona pelo upside)
PRINCÍPIO:    "Quanto preciso para sobreviver mesmo no pior caso?"  (dimensiona pela queima)
```

**Por que isto importa?** São duas perguntas distintas que iniciantes fundem:

| Pergunta | Responde a | Dirigida por |
|---|---|---|
| *"De quanto preciso?"* | Tamanho da rodada | Queima do **pior** cenário + buffer |
| *"Quanto vale?"* | Diluição/equity | Valuation (negociado) |

Dimensionar pela queima protege a empresa: ela sobrevive **mesmo se o cenário otimista não acontecer**. Dimensionar pelo valuation é apostar a sobrevivência no melhor caso — fragilidade fatal.

---

## §16.1 · Queima acumulada (o "vale do caixa")

**Por que olhar o acumulado, não o ano isolado?** Caixa é estoque, não fluxo. Um ano de EBITDA -R$0,1M parece trivial, mas se o ano anterior já queimou R$1,1M, o **acumulado** (-R$1,2M) é o que esvazia a conta. O ponto mais fundo desse acumulado é o "vale do caixa" — o mínimo que o aporte precisa cobrir.

| Cenário | Acum. Ano 1 | Acum. Ano 2 | **Vale do caixa** | Recuperação |
|---|---:|---:|---:|:--:|
| A · P25 conservador | -R$ 1,1M | -R$ 1,2M | **-R$ 1,2M** | Ano 3 |
| B · P50 provável | -R$ 0,1M | +R$ 3,2M | **-R$ 0,1M** | Ano 2 |
| C · P75 otimista | +R$ 1,5M | +R$ 9,9M | **R$ 0,0M** | Ano 2 |

> O pior vale (cenário A) é **-R$1,2M**. É este número — não o VPL — que dimensiona a rodada.
> ⚠️ 🟡 D-015: EBITDA é *proxy* de caixa. Capital de giro e CAPEX podem agravar o vale. D001-NOVO-20 refina com modelo de fluxo de caixa direto.

---

## §16.2 · Dimensionamento do aporte

**Por que três componentes e não só o vale?** Cobrir exatamente o vale (-R$1,2M) deixaria a empresa com saldo zero no fundo do poço — qualquer desvio mata. Um dimensionamento prudente soma três camadas:

| Componente | Valor | Por que |
|---|---:|---|
| Vale a cobrir (pior caso A) | R$ 1,20M | Sobrevivência mínima sem apostar no upside |
| + Buffer de segurança 40% 🟡 | R$ 0,48M | Margem de erro do plano (estimativas têm desvio) |
| + Runway operacional 12 m (CF) | R$ 1,71M | Não morrer na curva: 1 ano de fôlego pós-vale |
| **= Aporte recomendado** | **≈ R$ 3,5M** | |

> 🟡 D-015: buffer 40% = prática early-stage (não há fórmula; é margem de erro reconhecida). O valor arredonda para **R$ 3,5M** — número que cobre o cenário A com folga sem inflar diluição desnecessariamente.

---

## §16.3 · Uso dos recursos

**Por que esta alocação?** O capital deve atacar os gargalos que destravam as próximas ondas (waves), não diluir-se em tudo:

| % | Valor | Destino | Por que |
|:--:|---:|---|---|
| 35% | R$ 1,2M | Cobrir queima operacional (vale A) | Sobrevivência — prioridade zero |
| 30% | R$ 1,1M | Time produto/IA própria (Llama+QLoRA) | Mandato técnico: o modelo é objeto-de-produto, não API terceira |
| 20% | R$ 0,7M | Comercial/GTM (Wave 1 Alfa · canal Wilton) | Wave 1 é o motor de caixa que paga as próximas |
| 15% | R$ 0,5M | Buffer/contingência | Antifragilidade |

> A lógica segue a trilha de waves: o aporte financia até a Wave 1 (Alfa) gerar caixa, que então paga a Wave 2 — cada onda financia a seguinte (princípio do roadmap).

---

## §16.4 · Tese de valuation (banda, não ponto)

**Por que uma banda e não um número?** Valuation pré-receita é negociação, não cálculo. Dar um número único finge precisão que não existe. O honesto é ancorar no valor intrínseco (E[VPL]) e aplicar o *desconto de estágio* que todo investidor early-stage aplica:

| Haircut de estágio | Pre-money | Diluição por R$ 3,5M |
|:--:|---:|:--:|
| 50% (otimista) | R$ 9,8M | ~26% |
| 65% (central) | R$ 6,9M | ~34% |
| 75% (conservador) | R$ 4,9M | ~42% |

> 🟡 D-015: o haircut reflete prática VC early-stage BR (risco de execução pré-receita). **Por que descontar o VPL?** Porque R$19,6M é o valor *se a execução der certo*; o investidor entra *antes* dessa prova, então paga menos pelo risco. Banda-alvo de negociação: **diluição 15-30%** por R$ 3,5M (number a fechar em term sheet). Gera D001-NOVO-22 (validar com term sheet real).

---

## §16.5 · Síntese da tese

```
PEDIR:        ~R$ 3,5M  (dimensionado pela queima do pior caso + buffer + runway)
POR QUÊ:      cobre o vale do cenário A (R$1,2M) sem depender do otimismo
RETORNO:      E[VPL] R$19,6M · perfil assimétrico (downside +R$2,1M / upside R$38,8M = 18×)
DILUIÇÃO:     banda 15-30% (negociada · não tabelada)
USO:          35% sobrevivência · 30% IA própria · 20% GTM Wave1 · 15% buffer
```

> **A história para o investidor**: "Peço R$3,5M não porque sonho grande, mas porque é o que garante a empresa sobreviver mesmo no cenário ruim e ainda ter 12 meses de fôlego. Se o cenário provável (B) se confirmar, isso vira um negócio que vale ~R$19M — com a particularidade de que mesmo o pior caso devolve capital. Você arrisca pouco no piso e ganha muito no teto."

---

## §16.6 · Auto-avaliação PMQS + Devil's Advocate

| Critério | Peso | Score |
|---|:--:|:--:|
| CE | 15% | 9.4 | PI | 15% | 9.5 | CC | 10% | 9.7 |
| PRI | 20% | 9.5 | RA | 15% | 9.7 | EIC | 10% | 9.5 | OVA | 15% | 9.4 |

**PMQS Bruto** = 9.52 · **VVV** = 0.72 (valuation pré-receita = estimativa estrutural) · **Final = 6.85** 🟡 (honesto · valuation puxa · sobe pós term sheet D001-NOVO-22)

> ⚔️ **1**: "Buffer 40% é arbitrário." → Procede. Não há fórmula para margem-de-erro-do-plano. 40% é prática reconhecida, marcado D-015. Alternativa seria modelar variância — fora de escopo pré-piloto.
> ⚔️ **2**: "Haircut de valuation é chute." → Procede como estrutural. Valuation pré-receita É negociado, não calculável. Por isso entrego **banda**, não ponto, e gero D001-NOVO-22. Honestidade > falsa precisão (RGO-9).
> ⚔️ **3**: "EBITDA≠caixa, o vale pode ser pior." → Verdade e declarado em §16.1. D001-NOVO-20 (modelo de caixa direto) refina. O buffer 40% existe parcialmente para absorver isso.

---

## §16.7 · Backlinks

| Consome | Como |
|---|---|
| Cap 15 Financeiro | E[VPL], DRE, queima por cenário |
| Cap 17 Riscos | rodada/diluição → risco de captação + cenário A |
| Pitch investidor | tese R$3,5M + perfil assimétrico + uso dos recursos |

---

**FIM Cap 16 v1.0.1** · D001-NOVO-21 RESOLVIDO · lê SSOT v1.0.8 · PMQS 6.85 honesto · gera D001-NOVO-22
