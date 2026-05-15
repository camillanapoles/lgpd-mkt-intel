---
id: NEOGOV-V21-DEBITO-D002-COGNITIVO
filename: DEBITO-D002-AUDITORIA-COGNITIVA-v2.1.4.2.md
created_at: 2026-05-15
type: TECHNICAL_DEBT_REGISTRY
status: REGISTERED_PENDING_EXECUTION
sprint_origem: S2.1 edição 2 (gerado por D-012 + IN-014)
sprint_destino: S5 refinamentos (auditoria final · não bloqueia produção corrente)
parent_doc: BUSINESS-PLAN-FINAL-v2.1
purpose: Auditoria cognitiva retroativa dos capítulos do Sprint 1 (04, 07, 11) aplicando padrão IN-014
priority: MEDIUM · não bloqueia · pode ser feito em S5
tags: [debito, retificacao-cognitiva, marketing, audiencia-externa]
---

# Débito Técnico D002 · Auditoria Cognitiva Retroativa

> **Identificado em**: Sprint 2.1 edição 2 (D-012 + IN-014)
> **Severidade**: MEDIUM · não bloqueia produção corrente, mas degrada PMQS final dos Caps 04/07/11 para audiência externa
> **Sprint destino**: S5 (refinamentos) ou consolidação · pode ser paralelo

## 1 · Diagnóstico do gap

A retificação da Missão (D-012) revelou padrão cognitivo IN-014: termos técnicos sem tradução cognitiva degradam audiência externa. Os capítulos do Sprint 1 (04 DT, 07 Personas, 11 Produtos) foram produzidos antes desta consciência metodológica e podem conter:

1. Termos técnicos sem tradução para benefício humano
2. Frases que sub-valorizam profissionais humanos (advogados, médicos)
3. Marketing implícito de tecnologia em vez de marketing de benefício
4. Falta de identificação clara de "vilão combatido" por capítulo

## 2 · Termos suspeitos a auditar

### Cap 04 · Design Thinking

| Termo atual | Audiência impactada | Tradução cognitiva sugerida |
|---|---|---|
| "knowledge jurídico manufaturado" | Investidor, parceiro institucional | "expertise jurídica aplicada via tecnologia" |
| "manufatura do processo em produto via IA + ICT" | Cliente | "transformamos atendimento jurídico em produto contínuo" |
| "pivô industrial" | Cliente · investidor | "pivô de escala · mesma qualidade, mais clientes" |
| "lógica geradora" | Leitor casual | "método que originou cada decisão deste plano" |
| "knowledge formalizável" | Leitor casual | "conhecimento documentável e treinável" |

### Cap 07 · Personas

| Termo atual | Audiência impactada | Tradução cognitiva sugerida |
|---|---|---|
| "Says/Thinks/Does/Feels" (no header) | Leitor não familiarizado com DT | Preservar mas adicionar nota "elementos canônicos do empathy map" |
| "JTBD statement" | Cliente · investidor | "objetivo final que esta pessoa quer alcançar" |
| "POV statement" | Cliente · investidor | "ponto de vista que captura a dor real" |

### Cap 11 · Produtos

| Termo atual | Audiência impactada | Tradução cognitiva sugerida |
|---|---|---|
| "★ICT" (sigla) | Cliente · investidor | Manter ★ICT mas explicar uma vez = "produto registrado como Instituição de Ciência e Tecnologia, habilita venda direta via dispensa de licitação" |
| "stickiness operacional" | Audiência geral | "produto que se torna indispensável no dia-a-dia" |
| "switching cost máximo" | Audiência geral | "alto custo para o cliente trocar de fornecedor" |
| "manufaturar" (qualquer instância) | Investidor · parceiro | substituir por "compor" ou "automatizar" |

## 3 · Padrão de retificação a aplicar

Para cada termo técnico no texto, aplicar fórmula:

```
[termo técnico] → [benefício humano percebido] sem [vilão concreto]
```

Exemplos aplicados:
- "IA + ICT" → "tecnologia avançada com proteção jurídica" sem "complexidade legal"
- "knowledge manufaturado" → "expertise legal aplicada continuamente" sem "dependência de 1 consultor"
- "switching cost" → "valor que cresce com o tempo" sem "custo de trocar fornecedor"

## 4 · Execução proposta (Sprint S5 ou consolidação)

### Opção A · Auditoria pontual (recomendada)
Não reescrever capítulos inteiros. Aplicar substituições cirúrgicas:
- 10-15 substituições por capítulo
- Manter estrutura e tabelas
- Cada substituição registra entrada VVV-LOG nova
- Tempo estimado: 1 sub-sprint S5.0.5

### Opção B · Reescrita parcial das seções de abertura
Reescrever só as seções §X.1 ("Por que este capítulo") com tom cognitivo retificado. Manter tabelas e conteúdo técnico.

### Opção C · Acompanhar Sumário Executivo (Cap 03)
O Sumário Executivo (S5.3) é escrito por último e lê todos os capítulos. Pode "absorver" a retificação cognitiva no nível mais visível externamente, deixando capítulos internos com o tom técnico atual.

**Recomendação:** Opção A + Opção C combinadas. Substituições cirúrgicas nos Caps 04/07/11 + Sumário Executivo com tom cognitivo retificado.

## 5 · Entregáveis de S5.0.5 (sub-sprint auditoria cognitiva)

1. **`content/04-design-thinking-v2.5.x.md`** — retificação cognitiva pontual
2. **`content/07-personas-v2.5.x.md`** — retificação cognitiva pontual
3. **`content/11-produtos-v2.5.x.md`** — retificação cognitiva pontual + traduções de siglas
4. **Anexos atualizados** A/B/C com retificações registradas

## 6 · Anti-padrões a evitar na auditoria

- 🚫 Reescrever conteúdo aprovado (D-INH não pode ser revogado)
- 🚫 Perder rigor metodológico em nome de "linguagem fácil"
- 🚫 Sobrecarregar texto com glossário inline (criar §Glossário no Cap 01 Capa)
- 🚫 Mudar termos técnicos onde audiência é técnica (programadores no Cap 11 técnico)
- 🚫 Inflar PMQS retroativamente — registrar nova edição com retificação, não substituir versão fechada

## 7 · Quando NÃO aplicar IN-014

Audiências internas (equipe, comitê técnico) toleram terminologia precisa. Aplicação de IN-014 é primariamente para:
- Audiência externa (cliente, investidor, parceiro institucional)
- Material de marketing (Cap 14 GTM)
- Sumário Executivo (Cap 03 · leitura externa)
- Visão e Missão (Cap 02 · já aplicado)

## 8 · VVV alvo pós-S5.0.5

| Métrica | VVV atual | VVV alvo pós-D002 |
|---|---:|---:|
| Caps 04/07/11 clareza audiência externa | 0.85 | 0.90+ |
| PMQS final Sprint 1 (médio) | 8.22 | 8.45+ |
| Coerência com Cap 02 v2.1.4.2 retificado | 0.75 | 0.95 |

## 9 · Registro nos anexos vivos

Este débito gera referência cruzada nos 3 anexos:

- **APENDICE-A-VVV-LOG**: notação "FLAG-D002" em afirmações suspeitas (não SUPERSEDED ainda)
- **APENDICE-B-DECISIONS-LOG**: D-013 (futura) será "Execução D002 · auditoria cognitiva aplicada"
- **APENDICE-C-INSIGHTS-CARRY**: IN-014 referencia este débito como execução prevista

## 10 · Conexão com Plano Maior

D002 é o segundo débito técnico registrado (após D001 · Pricing). Padrão emergente:
- **D001 (S3.0)** — débito de precisão técnica (modelagem bottom-up)
- **D002 (S5.0.5)** — débito de precisão cognitiva (tradução para audiência)

Ambos são **resultados naturais do método PIER**: PMQS auditado revela gaps que não eram visíveis na geração inicial. Esta é a manifestação prática do Valor 5 (Auditabilidade Reversa) operando no próprio processo de produção do BP.
