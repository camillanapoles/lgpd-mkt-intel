---
id: NEOGOV-V21-CAP06-TECNOLOGIA
filename: 06-tecnologia-v1.0.1.md
created_at: 2026-05-16T13:05:00Z
type: BUSINESS_PLAN_CHAPTER
chapter: 6
title: Tecnologia (IA Própria · Mandato Técnico)
version: v1.0.1
data_source: data/neogov-pricing-cost-ssot-v1.0.8.json
sprint: W1.4.3
edicao: 1
branch: retificacao-validacao-preco-novo
canonical_chain: [ssot-v1.0.8, 05-produtos, 16-investimento]
quality_target: PMQS 9.0 · VVV >= 0.76
tags: [tecnologia, ia-propria, llama, qlora, mandato-tecnico, ssot-v1.0.8]
mandatos_honrados: [RGO-9, D-015, AP-14, mandato-IA-propria]
---

# Capítulo 6 · Tecnologia (IA Própria)

> **Por que a IA é mandato, não escolha?** Há uma decisão arquitetural inegociável no projeto: o modelo de IA é **próprio, local, treinado pela equipe** — não API externa (nem mesmo BR como Sabiá/Maritaca). Este capítulo explica *por que* essa restrição existe e o que ela implica.

---

## §6.1 · O mandato técnico (e sua razão)

```
MANDATO: LLM local · próprio · treinado pela equipe
  ❌ NÃO usar API externa (OpenAI, Anthropic, Google)
  ❌ NÃO usar API BR terceira (Sabiá-4 Maritaca)
  ✅ Modelo é OBJETO DE PRODUTO, não dependência
```

**Por que esta restrição é estratégica, não ideológica?**

| Razão | Consequência |
|---|---|
| Dados de conformidade são sensíveis | Não podem trafegar para API terceira (risco LGPD recursivo — a própria empresa de LGPD vazando dados seria fatal) |
| Modelo = ativo proprietário | API terceira = custo variável + dependência + zero moat |
| Especialização > tamanho | Modelo pequeno fine-tuned no domínio LGPD supera GPT genérico na tarefa específica |

> **Insight central**: uma empresa de conformidade LGPD que terceiriza o processamento de dados sensíveis para uma API externa tem um paradoxo fatal no coração do produto. O mandato de IA própria não é preferência técnica — é coerência existencial com o que a empresa vende.

## §6.2 · Stack (decisão arquitetural)

```
Modelo base:    Llama 3.1 8B
Fine-tuning:    QLoRA (eficiente · viável com orçamento early-stage)
Orquestração:   LangGraph
Infra:          Cloud BR (soberania de dados · LGPD)
```

**Por que Llama 3.1 8B e não um modelo maior?** Especialização supera tamanho na tarefa estreita. Um 8B fine-tuned em corpus LGPD/jurídico brasileiro responde melhor *neste domínio* que um modelo gigante generalista — e cabe no orçamento (Cap 16: 30% do aporte = R$1,1M para time produto/IA). Treinar em áreas não-relevantes seria desperdício.

## §6.3 · Risco e mitigação (honesto)

| Risco | Mitigação |
|---|---|
| Fine-tune não performar (R6 Cap 17) | PoC ANTES de prometer a cliente (D001-NOVO-4 · ~870M tokens) |
| Custo de treino subestimado | Cap 15 modela cenários · buffer Cap 16 |

> 🟡 D-015: viabilidade do fine-tune é hipótese a validar (D001-NOVO-4 · PoC vLLM). O capítulo declara isto — não vende IA própria como fato consumado.

---

## §6.4 · PMQS + Devil's Advocate

PMQS Bruto 9.32 × VVV 0.77 = **7.18** 🟡 honesto

> ⚔️ "IA própria é cara/arriscada p/ early-stage" → Procede · é R6 (Cap 17 · médio). Mas a alternativa (API terceira) cria paradoxo existencial (§6.1) — risco maior. Trade-off consciente.
> ⚔️ "Llama 8B pode não bastar" → Hipótese declarada · PoC (D001-NOVO-4) valida antes de comprometer. Não afirmado como certo.

## §6.5 · Backlinks

| Consome / Alimenta |
|---|
| Cap 5 (produtos usam o modelo) · Cap 16 (30% aporte = IA) · Cap 17 (R6) |

---

**FIM Cap 6 v1.0.1** · lê SSOT v1.0.8 · PMQS 7.18 honesto · mandato IA própria fundamentado
