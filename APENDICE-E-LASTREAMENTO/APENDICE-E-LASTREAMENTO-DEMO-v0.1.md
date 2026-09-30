---
id: NEOGOV-V21-APENDICE-E-DEMO
filename: APENDICE-E-LASTREAMENTO-DEMO-v0.1.md
created_at: 2026-05-15
type: METHODOLOGY_DEMO
status: AWAITING_USER_APPROVAL_OF_FORMAT
purpose: Demonstrar formato de lastreamento de estimativas em 3 exemplos críticos antes de aplicar a todo o BP
parent_decision: D-015 (sistema de lastreamento · a registrar formalmente)
tags: [lastreamento, estimativas, governanca-dados, refatoracao-trivial]
---

# Apêndice E (DEMO) · Lastreamento de Estimativas

> Demonstração com 3 estimativas críticas do Débito D003. Se aprovado o formato, expande para todas as estimativas do BP e vira anexo vivo permanente.

## Convenção de flags visuais

| Flag | Significado | VVV range |
|---|---|---:|
| 🟢 `[FATO]` | Dado primário verificável | 0.90-1.00 |
| 🔵 `[ANÁLOGO]` | Caso similar documentado · empresa comparável | 0.70-0.85 |
| 🟡 `[INFERÊNCIA]` | Derivação lógica · sem análogo direto | 0.55-0.70 |
| 🟠 `[ESTIMATIVA]` | Palpite operacional · valida antes uso comercial | 0.40-0.55 |
| 🔴 `[GAP]` | Vazio · bloqueante para uso comercial | 0.20-0.40 |

---

## EST-001 · Pricing API Maritaca AI · Sabiá-4

```yaml
EST-ID: EST-001-sabia4-pricing
flag: 🔵 ANÁLOGO
valor: R$ 8-15 por MTok input · R$ 25-45 por MTok output (range)
unidade: R$/MTok
fonte_ou_analogo:
  - Análogo 1: Sabiá-3 pricing público Maritaca AI (analisemacro.com.br · ago/2024 · "melhor custo-benefício que GPT-4o")
  - Análogo 2: Maritaca-AI/maritalk-api LangChain integration (github.com · jan/2026)
  - Comparação: Sonnet 4.6 oficial $3/$15 USD-MTok = R$ 16/R$ 80 BRL-MTok
  - Estimativa: Sabiá-4 plausivelmente 30-50% menor que Sonnet por positioning
saneamento:
  acao_1: Consultar tabela oficial em docs.maritaca.ai (link direto API pricing 2026)
  acao_2: Contato comercial Maritaca AI · pedir cotação volume NeoGov
  acao_3: POC pequeno (1000 chamadas reais) · medir custo efetivo
  responsavel: Camila (CTO · acesso técnico) + Wilton (negociação comercial)
  prazo: S2.5.2 (POC Sabiá-4 vs Llama 3.1)
usado_em:
  - DEBITO-D003 §2.1 (decisão modelo principal)
  - SPRINT-3.0.1-redo §3 P1-P4 (componente IA por produto)
  - Tier A arquitetura (custo cloud BR · usa Sabiá-4 via API)
risco_se_errado: alto · IA é 5-15% do custo total · erro 50% afeta margem P3 em 3-5pp
ultima_revisao: 2026-05-15
```

**Por que ANÁLOGO e não ESTIMATIVA:** Sabiá-3 tem pricing público histórico e positioning declarado contra GPT-4o. Inferência defensável que Sabiá-4 segue mesma estratégia comercial (modelo brasileiro · custo competitivo vs Sonnet).

**Por que não FATO ainda:** pricing público Sabiá-4 específico não foi acessado · POC não realizado · contrato volume não negociado.

---

## EST-002 · Custo cloud Tier A (Magalu/Locaweb · cliente Gamma)

```yaml
EST-ID: EST-002-tier-A-cloud-cost
flag: 🔵 ANÁLOGO
valor: R$ 800-3.000 por cliente por mês (range)
unidade: R$/cliente/mês
fonte_ou_analogo:
  - Análogo 1 forte: Sysvale (BA · 11 anos · saúde pública municipal) opera multi-tenant
    sobre Magalu Cloud · "cada município conta com máquina virtual dedicada"
    (magalu.cloud/blog · dez/2025) · perfil similar ao NeoGov Tier A
  - Análogo 2: Locaweb Cloud lançado 2025 declarando 50-70% mais barato que AWS
    (NeoFeed · mar/2026) · 150 clientes em 6 meses
  - Inferência: VM dedicada média Magalu R$ 400-1.500/mês + storage + bandwidth
    + Sabiá-4 API (volume médio) R$ 300-1.000/mês = R$ 700-2.500/mês total
saneamento:
  acao_1: Cotação direta Magalu Cloud para perfil "100 clientes Gamma multi-tenant"
  acao_2: Cotação direta Locaweb Cloud equivalente
  acao_3: POC 1 cliente real (1 escola Gamma) durante 30 dias · medir custo efetivo
  responsavel: Camila (especificação técnica) + Wilton (negociação enterprise)
  prazo: S2.5.3 (validação cloud soberana)
usado_em:
  - DEBITO-D003 §2.2 Tier A (default Gamma escola privada)
  - SPRINT-3.0.1-redo §3 P1 SaaS · linha "cloud"
  - SPRINT-3.0.1-redo §3 P4 AI-DPO · linha "cloud"
  - Cap-11 §pricing P1 + P4
risco_se_errado: médio · cloud é 30-50% do custo P1 · erro 30% afeta margem 8-12pp
ultima_revisao: 2026-05-15
```

**Análogo forte:** Sysvale é case quase isomorfo (software para saúde pública municipal · multi-tenant · Magalu Cloud · BR) — é o mesmo padrão técnico que NeoGov adotaria.

---

## EST-003 · CAPEX GPU NVIDIA L40S para Tier B (cloud BR)

```yaml
EST-ID: EST-003-gpu-l40s-capex
flag: 🟡 INFERÊNCIA
valor: R$ 180.000-280.000 por unidade (importada) · OU R$ 8.000-18.000/mês aluguel cloud BR
unidade: R$ (CAPEX) ou R$/mês (OPEX cloud)
fonte_ou_analogo:
  - Análogo fraco: NVIDIA L40S preço internacional ~$8.000-12.000 USD
    (mercado servidores · referência 2025)
  - Câmbio: × 5,30 BRL = R$ 42-64k preço base
  - Importação BR (Imposto + ICMS + logística): tipicamente 3-4x preço base
    = R$ 130-260k posto-Brasil (inferência setor)
  - Alternativa cloud GPU BR: Magalu Cloud GPU on-demand (NVIDIA presente)
    pricing público não acessado · estimar R$ 8-18k/mês baseado em equivalente AWS p4d
saneamento:
  acao_1: Cotação 3 fornecedores BR (Bludata, NTI, Aldo) para L40S
  acao_2: Cotação Magalu Cloud GPU on-demand para L40S
  acao_3: Análise CAPEX vs OPEX (break-even em quantos meses?)
  acao_4: Considerar L40S vs A100 vs H100 (Camila decide custo/performance)
  responsavel: Camila (decisão técnica) + financeiro (CAPEX vs OPEX)
  prazo: S2.5.4 (desenho arquitetura 3-tier · decisão Tier B)
usado_em:
  - DEBITO-D003 §2.2 Tier B (B2G Alfa · cloud BR + GPU dedicada)
  - SPRINT-3.0.1-redo §3 P2 + P3 (componente IA cost via inferência local)
  - Cap-11 §pricing P2 + P3 (margem alvo 80% P3 depende disso)
risco_se_errado: ALTO · GPU é 40-60% do custo recorrente Tier B · erro 30% inviabiliza modelo de negócio
flag_atencao: 🚨 estimativa fraca · POC obrigatório antes de pricing Tier B
ultima_revisao: 2026-05-15
```

**Por que INFERÊNCIA e não ANÁLOGO:** não tenho caso comparável de empresa BR rodando L40S para inferência LLM regulated industry. Cálculo a partir de preço internacional + impostos típicos · defensável mas frágil.

**🚨 alerta:** esta é a estimativa mais fraca do D003 · justifica POC antes de modelar pricing Tier B com confiança.

---

## Resumo das 3 estimativas demo

| EST-ID | Flag | Valor | VVV atual | VVV pós-saneamento | Risco se errado |
|---|:---:|---|---:|---:|---|
| EST-001 Sabiá-4 pricing | 🔵 ANÁLOGO | R$ 8-15/MTok in · R$ 25-45/MTok out | 0.75 | 0.95 | alto |
| EST-002 Tier A cloud | 🔵 ANÁLOGO | R$ 800-3.000/cliente/mês | 0.80 | 0.95 | médio |
| EST-003 GPU L40S CAPEX | 🟡 INFERÊNCIA | R$ 180-280k unidade · R$ 8-18k/mês cloud | 0.60 | 0.90 | ALTO 🚨 |

**Saneamento total estimado para D003 inteiro:** ~25-30 estimativas a documentar · esforço 1-2 sub-sprints · POC obrigatório para Tier B.

---

## Como isso resolve o impasse atual

Sem o sistema, eu travaria esperando Camila validar TUDO antes de prosseguir. Com o sistema:

1. ✅ Executo S2.5 com estimativas honestamente marcadas
2. ✅ Camila valida em paralelo (consulta o backlog de saneamentos)
3. ✅ Cada validação que volta é refatoração cirúrgica (não retrabalho amplo)
4. ✅ Estado do BP é sempre auditável — usuário vê na hora o que é firme

**Honra a:** Valor 1 (Honestidade Epistêmica) + Valor 5 (Auditabilidade Reversa) + RGO-1 (re-avaliar campo) + D-007 (não inflar VVV) + agora D-015 (lastreamento).
