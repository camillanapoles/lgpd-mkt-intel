---
id: NEOGOV-V21-CAP17-RISCOS
filename: 17-riscos-v1.0.1.md
created_at: 2026-05-16T11:00:00Z
type: BUSINESS_PLAN_CHAPTER
chapter: 17
title: Matriz de Riscos Quantificada + Mitigações
version: v1.0.1
data_source: data/neogov-pricing-cost-ssot-v1.0.8.json + Cap 15/16 + memória equipe
parent_chapters: [15-financeiro-v1.0.1, 16-investimento-v1.0.1]
sprint: W1.3-RISCOS
edicao: 1
branch: retificacao-validacao-preco-novo
fecha_onda: W1.3 (bloco financeiro-risco)
mandato_atendido: USUARIO_2026-05-16 "multi task by wave · Cap 17 · WAL contínuo"
canonical_chain: [ssot-v1.0.8, 15-financeiro, 16-investimento]
quality_target: PMQS 9.5 · VVV >= 0.78
tags: [riscos, matriz, mitigacao, jian-fratura-equipe, ssot-v1.0.8]
mandatos_honrados: [RGO-9 honestidade brutal, D-015, AP-14, estilo-educacional]
---

# Capítulo 17 · Matriz de Riscos Quantificada

> **Por que este capítulo fecha o bloco**: Caps 15/16 mostraram o que o negócio *pode render* e *quanto custa começar*. O Cap 17 responde à pergunta que o investidor cético faz por último: *o que pode dar errado, e o que vocês fazem a respeito?* Um BP sem riscos honestos não é otimista — é ingênuo, e investidores experientes descartam.

---

## §17.0 · Como os riscos são pontuados (método)

```
Score = Probabilidade (1-5) × Impacto (1-5)
  Score ≥ 15 → 🔴 CRÍTICO   (atacar antes de captar)
  Score 9-14 → 🟠 ALTO      (mitigação ativa no plano)
  Score < 9  → 🟡 MÉDIO     (monitorar)
```

**Por que multiplicar e não somar?** Um risco improvável mas catastrófico (impacto 5, prob 1 → 5) e um risco provável mas trivial (prob 5, impacto 1 → 5) recebem o mesmo score — e isso é correto. A multiplicação captura que **risco é a interação** entre quão provável e quão grave, não a soma. Um risco só é crítico quando *ambos* são altos.

---

## §17.1 · Matriz consolidada (9 riscos · ordenada por score)

| ID | Risco | P | I | Score | Nível |
|:--:|---|:--:|:--:|:--:|:--:|
| **R1** | Fratura interna equipe (JIANG=5 · não resolvida) | 4 | 5 | **20** | 🔴 CRÍTICO |
| R3 | Estimativas D-015 erradas (WTP/ABC/WACC) | 3 | 4 | 12 | 🟠 ALTO |
| R4 | Dependência canal único (Wilton/político FNDE) | 3 | 4 | 12 | 🟠 ALTO |
| R2 | Cenário A se materializa (queima R$1,2M) | 3 | 3 | 9 | 🟠 ALTO |
| R5 | Arrecadação cartório sigilosa (preço impreciso) | 3 | 3 | 9 | 🟠 ALTO |
| R7 | Diluição > 30% (valuation fraco) | 3 | 3 | 9 | 🟠 ALTO |
| R6 | IA própria não performar (Llama+QLoRA) | 2 | 4 | 8 | 🟡 MÉDIO |
| R8 | Concorrente entra notarial+IA antes | 2 | 3 | 6 | 🟡 MÉDIO |
| R9 | Mudança regulatória LGPD/CNJ | 2 | 3 | 6 | 🟡 MÉDIO |

```
1 crítico · 5 altos · 3 médios
```

---

## §17.2 · R1 · O risco dominante (e por que o BP não pode resolvê-lo)

**Fratura interna da equipe — score 20, o maior do projeto.**

> ⭐ **Insight desconfortável (RGO-9)**: este não é um risco de mercado, produto ou finanças — é risco de **gente**. Nenhum modelo financeiro, por melhor que seja, sobrevive a sócios em conflito. E o BP **não pode resolvê-lo** — só pode sinalizá-lo honestamente. Esconder R1 para o plano parecer mais limpo seria a desonestidade mais perigosa possível, porque é o risco que mais mata startups.

**Por que P=4, I=5?** A fratura já é observável (memória da reunião · JIANG=5). Impacto 5 porque dissolução societária em estágio pré-receita é terminal — não há produto a salvar. **Mitigação**: acordo de sócios formal + governança definida **antes** de captar (investidor due-diligence vai expor isto de qualquer forma; melhor resolver proativamente).

---

## §17.3 · Riscos ALTOS (mitigação por design)

**Por que vários já estão parcialmente mitigados?** Boa parte do trabalho dos Caps 15/16 foi *projetar contra* estes riscos:

| ID | Risco | Mitigação | Já mitigado? |
|:--:|---|---|:--:|
| R3 | Estimativas D-015 | Piloto Wave1 calibra WTP/ABC/WACC antes de escalar | Parcial (marcadas, não cegas) |
| R4 | Canal único Wilton | Diversificar canais Wave2+ · Wave1 não 100% dependente | A executar |
| R2 | Cenário A queima | Rodada R$3,5M **já dimensionada** p/ cobrir A (Cap 16) | ✅ Por design |
| R5 | Cartório sigilo | Faixa-classe FATO é teto público · piloto valida WTP | Parcial |
| R7 | Diluição >30% | BATNA = bootstrap via Wave1 Alfa (cash engine) | ✅ Alavancagem negocial |

> **Lição pedagógica**: R2 e R7 mostram que um bom plano *embute* mitigações na estrutura. Dimensionar a rodada pela queima do pior caso (Cap 16) **é** a mitigação de R2. Ter o Wave1 Alfa como motor de caixa **é** a mitigação de R7 (poder dizer "não preciso fechar a qualquer custo"). Mitigação não é uma seção separada — é arquitetura.

---

## §17.4 · Riscos MÉDIOS (monitorar)

| ID | Mitigação |
|:--:|---|
| R6 IA própria | PoC fine-tune **antes** de prometer a cliente (D001-NOVO-4) — não vender o que não foi provado |
| R8 Concorrente | Velocidade Wave1 + lock-in via integração profunda |
| R9 Regulatório | Produto configurável (absorve mudança normativa) · Simone monitora CNJ/ANPD |

---

## §17.5 · Síntese de riscos

```
RISCO DOMINANTE:  R1 fratura equipe (20) — resolver ANTES de captar · BP só sinaliza
JÁ MITIGADOS:     R2 (rodada cobre queima) · R7 (BATNA bootstrap) — por design Cap16
CALIBRAM-SE:      R3/R5 via piloto Wave1 (estimativas → fatos)
PERFIL GERAL:     1 crítico humano · maioria mitigável por execução disciplinada
```

> **A leitura honesta para o investidor**: "O modelo financeiro é sólido e o downside é protegido. O maior risco não está na planilha — está na mesa de sócios. Estamos sinalizando isso porque preferimos um investidor que entra com os olhos abertos a um que descobre depois. Os demais riscos ou já estão mitigados por design (rodada cobre o pior caso) ou se resolvem com a disciplina de execução do piloto."

---

## §17.6 · PMQS + Devil's Advocate

PMQS Bruto 9.55 · VVV 0.78 (riscos qualitativos · scores P/I = julgamento estruturado D-015) · **Final 7.45** 🟡 honesto

> ⚔️ **1**: "Scores P/I são subjetivos." → Procede parcialmente. P/I em risco é sempre julgamento; o método (multiplicação, faixas) o torna *estruturado e auditável*, não arbitrário. Declarado D-015.
> ⚔️ **2**: "Expor R1 afasta investidor." → Inverte-se: esconder R1 e ser pego na due-diligence destrói credibilidade total. Honestidade proativa é alavanca, não fraqueza (RGO-9).
> ⚔️ **3**: "Faltam riscos (câmbio, tech debt)?" → Possível. Lista cobre os materiais ao estágio. Riscos de escala (câmbio em infra cloud) entram em revisão pós-Wave1 — fora de escopo pré-piloto.

---

## §17.7 · Backlinks

| Consome | Como |
|---|---|
| Cap 16 Investimento | rodada/BATNA = mitigação R2/R7 |
| Cap 15 Financeiro | cenário A = R2 |
| Pitch investidor | matriz + R1 sinalizado honestamente |

---

**FIM Cap 17 v1.0.1** · FECHA onda W1.3 · lê SSOT v1.0.8 · PMQS 7.45 honesto · R1 sinalizado sem máscara
