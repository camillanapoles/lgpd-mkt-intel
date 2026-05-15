---
id: NEOGOV-V21-DEBITO-D001-PRICING
filename: DEBITO-D001-PRICING-FRAMEWORK-v2.1.3.1.md
created_at: 2026-05-15
type: TECHNICAL_DEBT_REGISTRY
status: REGISTERED_PENDING_EXECUTION
sprint_origem: S1.3 (identificado pós-gate)
sprint_destino: S3.0 (novo sprint inserido)
parent_doc: BUSINESS-PLAN-FINAL-v2.1
purpose: Capturar gap crítico de precificação · executar via modelagem bottom-up
priority: CRITICAL · bloqueia BMC e GTM
tags: [debito, pricing, custo, lucratividade, modelagem-financeira]
---

# Débito Técnico D001 · Framework de Precificação Assertiva

> **Identificado em**: pós-Gate Sprint 1 (Cap 11 §pricing com VVV 0.65)
> **Severidade**: CRITICAL · não-resolução compromete Caps 12, 14, 15
> **Sprint destino**: S3.0 (novo sprint inserido antes do Cap 12 BMC)

## 1 · Diagnóstico do gap

O Capítulo 11 entregou pricing como **inferência top-down** baseada em:
- Tabela Confidata (R$ 497-R$3.497/mês) como referência
- Gap pricing (R$ 3.500-R$ 55.000/mês) como território livre
- Tabela `pricing_est` do DATA-v2.json

**Isso é insuficiente** porque:

1. Não há **modelagem de custo** de produção/operação por produto
2. Não há **margem de lucro alvo** declarada
3. Não há diferenciação clara entre **modelo de cobrança** (assinatura vs API vs usage-based)
4. Não há **CAC + custo de servir** estimado
5. Pricing tem VVV 0.65 — frágil para compor BMC Revenue Streams

## 2 · Framework de Precificação a ser executado (S3.0)

### 2.1 · Modelagem de custo bottom-up por produto

Para cada um dos 5 produtos, estimar:

```yaml
custo_produto:
  
  custos_fixos_alocados:
    desenvolvimento: R$ ? (1x amortizado em X anos)
    manutencao_software: R$ ?/mês alocado
    licencas_terceiros: R$ ?/mês (IDE, infra dev, etc.)
  
  custos_variaveis_por_cliente:
    infra_cloud: R$ ?/cliente/mês
    api_ia:
      tipo: OpenAI | Anthropic | self-hosted | híbrido
      custo_unitario: R$ ?/1k tokens ou /requisição
      uso_estimado: ? unidades/cliente/mês
      custo_total: R$ ?/cliente/mês
    armazenamento: R$ ?/GB-mês × volume estimado
    bandwidth: R$ ?/GB egress × volume
  
  custos_operacionais_alocados:
    suporte_humano: R$ ?/cliente/mês (horas × custo hora)
    onboarding: R$ ? (1x diluído em LTV)
    jurídico_atualização: R$ ?/cliente/mês
  
  custos_aquisicao_CAC:
    canal_direto: R$ ?/cliente
    canal_indireto_consorcio: R$ ?/cliente (comissão FNDE/Wilton)
    marketing: R$ ?/cliente
    
  total_custo_mensal_por_cliente: R$ ?
  total_custo_aquisicao_amortizado: R$ ?/mês (em X meses)
```

### 2.2 · Diferenciação por modelo de cobrança

| Modelo | Aplicação | Cálculo de pricing |
|---|---|---|
| **Assinatura mensal** (P1, P4) | Custo previsível, valor entregue contínuo | `(custo_mensal + CAC_amortizado) × (1 + margem_alvo)` |
| **Projeto + assinatura** (P2, P5) | Setup pesado, depois manutenção | `setup = custo_implantação × (1 + margem_alvo)` + assinatura mensal |
| **Usage-based** (P3) | Custo proporcional ao uso (API IA) | `custo_unitário × volume × (1 + margem_alvo) + custo_fixo_base` |

### 2.3 · Variáveis externas a investigar

| Variável | Como pesquisar | Sprint |
|---|---|---|
| Custo OpenAI/Anthropic API por uso real | Pricing pages + benchmark interno | S3.0 |
| Custo cloud AWS/GCP para serving | AWS Calculator + estimativa volume | S3.0 |
| Salários ramo TI Brasil 2026 | Glassdoor + Catho | S3.0 |
| WTP real por persona (GAP02) | 3-5 entrevistas primárias | S3.0 ou paralelo |
| Pricing concorrentes (Be Compliance, Safetyfyi, GAP05) | Sales call mystery shopping | S3.0 |
| Custo médio para servir cliente B2G via ETEC | Pesquisa PNCP histórico (GAP01) | S3.0 |

### 2.4 · Margem de lucro alvo por produto/segmento

| Produto | Persona | Margem mínima | Margem alvo | Justificativa |
|---|---|---:|---:|---|
| P1 Plataforma | Gamma (edu) | 50% | 65% | Tier acessível, escala via SaaS multi-tenant |
| P1 Plataforma | Alfa (municipal) | 55% | 70% | Volume + canal consórcio |
| P2 Data Discovery | Alfa-E/F (B2G) | 60% | 75% | Knowledge intensivo, ICT premium |
| P3 Anonimização | Alfa, Alfa-E/F | 65% | 80% | **Diferencial competitivo único · maior margem** |
| P4 AI-DPO | Gamma | 45% | 60% | Volume + suporte automatizado |
| P4 AI-DPO | Alfa, Beta | 55% | 70% | Customização média |
| P5 ETL | Beta (saúde) | 50% | 65% | Setup alto compensa margem operacional |

Valores propostos como hipótese de trabalho — a confirmar com modelagem de custo real.

### 2.5 · Análise de unit economics

Para cada combo (produto × persona) calcular:

```
LTV (Lifetime Value) = ticket_mensal × duração_média_contrato × margem_bruta
CAC (Customer Acquisition Cost) = custo_aquisição_estimado
LTV/CAC ratio = LTV / CAC
Payback period = CAC / (ticket_mensal × margem_bruta)

Alvo SaaS saudável:
  LTV/CAC ≥ 3
  Payback ≤ 12 meses (B2G permite 18-24)
```

## 3 · Inserção no roadmap · Sprint 3.0 (NOVO)

A re-ordenação da fila DTP fica:

```
SPRINT 1 · núcleo gerador ✅ CONCLUÍDO
  S1.1 04 DT · S1.2 07 Personas · S1.3 11 Produtos

SPRINT 2 · identidade e abertura
  S2.1 02 VMV · S2.2 01 Capa-ficha

SPRINT 3.0 · MODELAGEM DE PRECIFICAÇÃO  ← NOVO · resolve este débito
  S3.0.1 → Modelagem custo bottom-up · 5 produtos
  S3.0.2 → Unit economics + WTP estimado
  S3.0.3 → Pricing final + margem
  S3.0.4 → APENDICE-D-MODELO-CUSTO.xlsx (planilha viva)
  S3.0.5 → Retificar Cap 11 §pricing com valores assertivos
  Gate 3.0

SPRINT 3.1 · Cap 12 BMC (com inputs do S3.0)
SPRINT 3.2 · Cap 13 VPC
SPRINT 3.3 · Cap 09 Porter

SPRINT 4 · operacional
  S4.1 16 Equipe · S4.2 15 Financeiro · S4.3 14 GTM
```

## 4 · Entregáveis do Sprint 3.0

1. **`content/15-financeiro-base-v2.x.y.md`** — modelagem de custo + pricing assertivo
2. **`APENDICE-D-MODELO-CUSTO-v2.x.y.xlsx`** — planilha Excel viva com:
   - Aba "Premissas" (todas as variáveis editáveis)
   - Aba "Custo P1" a "Custo P5" (modelagem detalhada por produto)
   - Aba "Unit Economics" (LTV/CAC/Payback)
   - Aba "Pricing Final" (tabela consolidada)
   - Aba "Sensibilidade" (análise what-if)
3. **`content/11-produtos-v2.3.0.X.md`** — retificação do §pricing com valores assertivos
4. **Anexos atualizados** A/B/C com novas afirmações VVV (passando de inferência para fato modelado)

## 5 · Anti-padrões a evitar

- 🚫 Pricing top-down (cópia de concorrente) sem modelagem própria de custo
- 🚫 Margem palpitada sem cálculo bottom-up
- 🚫 Mesmo pricing para personas diferentes (Procurador municipal e Gov federal têm WTP diferente)
- 🚫 Esquecer custo de API IA por uso (P3 é usage-based — custo escala com volume)
- 🚫 Ignorar CAC diferenciado por canal (consórcio = comissão maior; outbound = mais caro)
- 🚫 Margem uniforme entre produtos (P3 é diferencial único = margem maior justificada)

## 6 · VVV alvo pós-Sprint 3.0

| Tipo de afirmação | VVV atual | VVV alvo pós-S3.0 |
|---|---:|---:|
| Pricing por produto | 0.65 | 0.85+ |
| Margem de lucro | (não declarado) | 0.80+ |
| Unit economics | (não declarado) | 0.85+ |
| WTP por persona | 0.50 (GAP02) | 0.85+ (entrevistas) |
| Cap 11 pricing global | 0.65 | 0.85+ |
| **PMQS Cap 11 retificado** | 7.89 | **8.50+** |

## 7 · Registro nos anexos vivos

Este débito gera entradas nos 3 anexos:

- **APENDICE-B-DECISIONS-LOG**: D-010 · Inserção Sprint 3.0 modelagem precificação
- **APENDICE-C-INSIGHTS-CARRY**: IN-011 · Pricing top-down é insuficiente · S3.0 obrigatório antes do BMC
- **SESSION-STATE**: hash atualizado para `NEOGOV-V21-S1.3-DONE+DEBT-D001-AWAIT-S2.1`

A nomenclatura do hash reflete o débito identificado — não bloqueia Sprint 2.1 (que não depende de pricing), mas marca claramente o gap.
