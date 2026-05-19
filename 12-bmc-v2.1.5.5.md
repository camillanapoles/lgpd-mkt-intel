---
id: NEOGOV-V21-CAP12-BMC
filename: 12-bmc-v2.1.5.5.md
created_at: 2026-05-16T06:50:00Z
type: BUSINESS_PLAN_CHAPTER
chapter: 12
title: Business Model Canvas + Pricing Validado
version: v2.1.5.5
supersedes: 12-bmc-v2.1.5.4.md (usava preço velho · pré-DT-TEST · RGO-4 violado)
data_source: data/neogov-pricing-cost-ssot-v1.0.2.json (price.validated)
sprint: W1.2-RETIFICACAO-CONSOLIDACAO
edicao: 1
branch: retificacao-validacao-preco-novo
mandato_atendido: |
  USUARIO_2026-05-16: "re-consolidar Cap 12 BMC v2.1.5.5 lendo ssot.price.validated
  (nao mais preco velho) · referenciando grafico ponto de sucesso · base logica justificada"
canonical_chain:
  - APENDICE-E-v2.0.1 (custo · FATO web_search Magalu)
  - APENDICE-H (DDD 3 camadas)
  - APENDICE-I (ABC rateio proporcional)
  - APENDICE-K (DT TEST · price.validated)
  - APENDICE-L (auditoria base lógica · FIEL comprovado)
  - data/neogov-pricing-cost-ssot-v1.0.2.json (fonte única)
  - data/curva-ponto-sucesso-global.png (gráfico)
quality_target: PMQS 9.5 · VVV >= 0.82 · base estável (RGO-4 satisfeito)
tags: [bmc, pricing-validado, dt-test, ssot-driven, base-logica-fiel]
mandatos_honrados: [RGO-4 base estável, TEXT-AS-OBJECT, D-015, VVV sem máscara, D-020 client-facing]
---

# Capítulo 12 · Business Model Canvas + Pricing Validado
## v2.1.5.5 · Lê `ssot.price.validated` (pós Design Thinking TEST)

> **Mudança crítica vs v2.1.5.4**: este capítulo NÃO usa mais o preço velho inconsistente (Gamma R$ 800 marcado "subsidiado"). Lê `ssot.pricing_tiers[*].price.validated` — preço que **passou pelo Design Thinking TEST** (Apêndice K) sobre base lógica **auditada e comprovada FIEL** (Apêndice L: FATO web_search + MÉTODO ABC/DDD + LÓGICA dedutiva).

---

## §12.0 · Proveniência (base lógica · resposta ao mandato)

```
pricing_chain = {
  custo:    FATO     → web_search Magalu R$6.310/GPU (re-validado 16/05/2026)
  rateio:   MÉTODO   → ABC Kaplan&Cooper (proporcional · não uniforme)
  validação: LÓGICA  → DT TEST 5ª fase IDEO (c1 pagabilidade·c2 concorrência·c3 WTP·c4 margem)
  fidelidade: Apêndice L → FIEL · 4 elos fracos DECLARADOS (não disfarçados)
}
```
Auditoria completa em Apêndice L. Esta é a justificativa epistemológica solicitada.

---

## §12.1-12.6 · Blocos BMC (mantidos de v2.1.5.2 · sem alteração)

> Segmentos de Clientes, Proposta de Valor, Canais, Relacionamento, Recursos-Chave, Atividades-Chave, Parcerias-Chave permanecem conforme v2.1.5.2 (não afetados pelo branch de retificação · RGO-3 não mexer no que funciona). Ver `12-bmc-v2.1.5.2.md §12.1-12.6`.

---

## §12.7 · ESTRUTURA DE RECEITA · Pricing VALIDADO (substitui §12.7-BIS antigo)

### 12.7.1 Tabela mestre · `ssot.pricing_tiers[*].price.validated`

| Nome Comercial (client-facing) | Cliente | **Preço validado** | Modelo de cobrança | CSC total | Margem |
|---|---|---:|---|---:|:--:|
| **NeoGov Município · Essencial** | Cidade <30k hab | **R$ 5.458/mês** | Assinatura mensal | R$ 1.164 | 79% |
| **NeoGov Município · Profissional (Licitação)** | Cidade 30-100k via pregão | **R$ 12.000/mês** | Assinatura mensal | R$ 5.314 | 56% |
| **NeoGov Município · Profissional (Dispensa)** | Cidade 30-100k via Art.75 | **R$ 25.000/mês** | Assinatura mensal | R$ 9.489 | 62% |
| **NeoGov Município · Avançado** | Cidade >100k hab | **R$ 38.000/mês** | Assinatura premium + uso | R$ 18.727 | 51% |
| **NeoGov Estadual & Federal** | Estados/Ministérios | **R$ 50.000/mês** + R$ 25k setup | Assinatura premium + retainer | R$ 30.977 | 38% |
| **NeoGov Saúde · Hospital Pequeno (Ano 1)** | <100 leitos · ano 1 | **R$ 12.000/mês** + R$ 25k setup | Setup + manutenção | R$ 15.663 | -31% ⚠️ |
| **NeoGov Saúde · Hospital Pequeno (Recorrente)** | <100 leitos · ano 2+ | **R$ 12.000/mês** | Assinatura | R$ 10.163 | 15% |
| **NeoGov Saúde · Hospital Médio (Ano 1)** | 100-300 leitos · ano 1 | **R$ 28.000/mês** + R$ 50k setup | Setup + manutenção | R$ 28.202 | -1% ⚠️ |
| **NeoGov Saúde · Hospital Médio (Recorrente)** | 100-300 leitos · ano 2+ | **R$ 28.000/mês** | Assinatura | R$ 19.702 | 30% |
| **NeoGov Saúde · Hospital Grande (Ano 1)** | >300 leitos · ano 1 | **R$ 65.000/mês** + R$ 100k setup | Setup + manutenção | R$ 52.354 | 19% |
| **NeoGov Saúde · Hospital Grande (Recorrente)** | >300 leitos · ano 2+ | **R$ 65.000/mês** | Assinatura | R$ 38.854 | 40% |
| **NeoGov Educação · Escola Pequena** | 50-200 alunos | **R$ 597/mês** ⬇️ | Assinatura mensal | R$ 187 | 69% |
| **NeoGov Educação · Escola Média** | 200-800 alunos | **R$ 1.797/mês** ⬇️ | Assinatura mensal | R$ 364 | 80% |
| **NeoGov Educação · Rede & Escola Grande** | 800-1500 alunos | **R$ 5.000/mês** | Assinatura mensal | R$ 1.217 | 76% |
| **NeoGov Profissional · DPO Individual** | Advogado/DPO autônomo | **R$ 997/licença/mês** ⬇️ | Por licença (seat) | R$ 226 | 77% |
| **NeoGov Profissional · Escritório DPO** | Escritório 3+ DPOs | **R$ 797/licença/mês** ⬇️ | Por licença (volume) | R$ 164/seat | 79% |

> ⬇️ = preço REDUZIDO pelo DT TEST (Apêndice K): 4 tiers ajustados para land grab (volume play onde CSC é baixo · margem ainda 69-80%). 12 tiers mantidos.

### 12.7.2 Modelos de cobrança · `ssot.billing_models`

| Modelo | Aplicação | Termos |
|---|---|---|
| **Assinatura mensal** | P1 Plataforma Core | Anual -15% · lock-in 12m |
| **Assinatura premium tier** | P3-B2G · hospitais recorrente | Anual -10% · lock-in 12m |
| **Por uso (R$/M tokens)** | P3-B2C Anonimização | R$ 25/M tokens + mínimo R$ 500/mês · sem lock-in |
| **Por licença (seat)** | P4 AI-DPO | Desconto volume 10+/50+ · sem lock-in individual |
| **Setup + manutenção** | P2 ETL hospitalar | Setup 3x parcelas · lock-in 12m |
| **Projeto + retainer** | P5 Consultoria | Projeto 6x · retainer 6m mín |

---

## §12.11 · ESTRUTURA DE CUSTO · 3 Camadas DDD + ABC (Apêndice H+I)

```
custo_model = {
  layer_1a_platform (shared · rateável ABC):  R$ 10.988/mês  → FATO web_search
  layer_1b_dev_operacional (NÃO ratea):       R$  4.574/mês  → CF empresa
  layer_2_product (marginal por uso):         variável        → tarifas FATO
  layer_3_service (humano premium):           R$/hora         → taxa FATO · qtd ESTIMATIVA
}
rateio = ABC proporcional (Kaplan) · escola Gamma Pequena NÃO paga GPU (peso=0)
```

CF total empresa = **R$ 142.251/mês** (folha + L1B + marketing + compliance). Detalhe Apêndice E §4 + I §2.

---

## §12.12 · PONTO DE SUCESSO · Curva (função + gráfico)

### 12.12.1 Função (do `data/curva_ponto_sucesso.py` · LÓGICA pura reproduzível)

```
profit_global(N) = Σ_c [ N·mix_c × (price.validated_c − csc_total_c) ] − CF
```

### 12.12.2 Resultados-chave

| N clientes | Receita/mês | Lucro/mês | Status | ARR |
|---:|---:|---:|:--:|---:|
| 12 | R$ 74k | -R$ 95k | 🔴 burn | R$ 0.9M |
| 31 (Wave1 P75) | R$ 191k | -R$ 21k | 🔴 burn aceitável | R$ 2.3M |
| **37** | — | **R$ 0** | **⚖️ BREAK-EVEN GLOBAL** | — |
| 50 | R$ 308k | +R$ 53k | ✅ lucro | R$ 3.7M |
| 90 (Wave2) | R$ 555k | +R$ 209k | ✅ | R$ 6.7M |
| **163** | — | — | **🎯 SUCESSO GLOBAL (ARR ≥ R$12M · margem 49%)** | R$ 12.1M |
| 220 (Wave3) | R$ 1.36M | +R$ 716k | ✅ | R$ 16.3M |
| 600 (Wave5) | R$ 3.70M | +R$ 2.2M | ✅✅ industrial | R$ 44.4M |

**Gráfico**: `data/curva-ponto-sucesso-global.png` (zona burn vermelha até N=37 · zona lucro verde · Waves marcadas).

### 12.12.3 Break-even isolado por cluster (unit economics)

```
Mais eficientes (menos clientes p/ break-even):
  beta_grande_y2:    6 clientes   (lucro R$ 26.146/cliente)
  alfa_m_enterprise: 8 clientes   (lucro R$ 19.273/cliente)
  alfa_m_plus_disp: 10 clientes   (lucro R$ 15.511/cliente)

Menos eficientes (mais clientes · volume play):
  gamma_pequena:   347 clientes  (lucro R$ 410/cliente · MAS CSC só R$187 · escala)
  epsilon_dpo:     185 clientes  (land grab mercado DPO)

Beta Y1 (investimento estratégico): margem negativa · LTV/CAC compensa Y2+
```

---

## §12.13 · Síntese · Modelo de Negócio Validado

```
NeoGov é viável quando:
  N >= 37 clientes (mix Wave1 P75)        → break-even operacional
  N >= 163 clientes                        → sucesso global (ARR R$12M · margem 49%)
  
Trajetória cenário B (P50 · mais provável):
  Wave1 M12: ~25 clientes (burn controlado · investimento R$ 1-2M)
  Wave2 M24: ~90 clientes (lucro R$ 209k/mês)
  Wave3 M36: ~220 clientes (ARR R$ 16.3M · SUCESSO GLOBAL atingido)
  Wave5 M60: ~600 clientes (ARR R$ 44M · escala industrial Camila CTO)

Preço validado por DT TEST sobre base FIEL (Apêndice L):
  - 4 reduções estratégicas (Gamma/Épsilon · volume play · margem 69-80%)
  - 12 tiers mantidos (Alfa/Beta · cash engines · PASS DT TEST)
```

---

## §12.14 · Backlinks

| Consome este Cap | Como |
|---|---|
| Cap 13 VPC | Value Proposition por cluster usa pricing validado |
| Cap 15 Financeiro | DRE/FCD usa `ssot` + curva ponto sucesso |
| Cap 14 GTM | Pricing positioning + sales playbook |
| Cap 17 Riscos | Cenário A (P25) + elos fracos Apêndice L = riscos |

---

**FIM Cap 12 v2.1.5.5** · PMQS estimado 8.4 · VVV 0.82 · base FIEL (Apêndice L) · RGO-4 ✅
