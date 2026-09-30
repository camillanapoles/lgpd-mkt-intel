---
id: NEOGOV-V21-SESSION-STATE
filename: SESSION-STATE-v2.1.4.8.md
created_at: 2026-05-14
last_updated: 2026-05-15T16:30:00Z
type: WAL_MASTER_CONTINUITY
status: ACTIVE
parent_session: NEOGOV-V21-AUDIT-FRAMEWORK-2026-05-14
sprint: S3.0.1-v2.0
edicao: DONE_AWAIT_VALIDATION
continuity_hash: NEOGOV-V21-S3.0.1-v2.0-MODELAGEM-PRICING-DONE-AWAIT-VALIDATION
tags: [wal, continuidade, session-state, sprint-3-0-1-v2-done, ba-orchestration]
---

# Session State Master · NeoGov BP v2.1

## Estado da produção · Sprint 3.0.1 v2.0 CONCLUÍDO · aguarda validação

| Item | Valor |
|---|---|
| Versão alvo | BP v2.1 |
| Empresa | NeoGov (ICT privado) |
| Sprint atual | **S3.0.1 v2.0 ENTREGUE** · aguarda aprovação metodologia + validação WTP |
| Próximo sprint | S3.0.2 (validação societária) ou S3.0.3 (WTP entrevistas) |
| Capítulos produzidos | Cap 04 DT (8.74) · Cap 07 Personas (8.02) · Cap 11 Produtos (7.89) · Cap 02 VMV (~8.50) |
| Artefatos críticos | **POP v2.1.1.1 (master) + S3.0.1 v2.0 (pricing bottom-up)** |
| **Hash continuidade** | `NEOGOV-V21-S3.0.1-v2.0-MODELAGEM-PRICING-DONE-AWAIT-VALIDATION` |
| PMQS S3.0.1 v2.0 | 9.21 bruto × 0.78 VVV = **7.18 final** (sobe para 8.01 após GAP02 WTP) |

## Sprint 3.0.1 v2.0 · Highlights metodológicos

| Skill BA-Orchestration aplicada | Resultado |
|---|---|
| `estimation` (PERT 3-point) | Custos fixos P10/P50/P90 detalhados (folha, infra, CAPEX) |
| `decision-analysis` (weighted scoring) | Modelo cobrança vencedor por produto: Tier · Híbrido · Per seat · Projeto |
| `benchmarking` | Comparativo Confidata · Be Compliance · Clio · Harvey · Casetext (legaltech 2026) |
| `risk-analysis` (sensitivity) | Drivers críticos identificados · break-even 50+ clientes Wave 1 |
| `business-model-canvas` | Coerência Revenue ↔ Cost validada |
| `prioritization` (MoSCoW) | 3 tiers por produto · basic/pro/enterprise |

## Output S3.0.1 v2.0 · Pricing Tabela Mestre (cenário P50)

| Produto | Modelo vencedor | Range pricing P50 |
|---|---|---|
| **P1 SaaS Plataforma** | Assinatura tier | R$ 2.800-18.000/mês |
| **P2 Data Discovery** | Híbrido (setup+uso) | Setup R$ 6-35k + R$ 0,12-0,25/doc |
| **P3 LAI/LGPD Anonimização** | Dual (B2G assin · B2C uso) | R$ 7.500-22.000/mês OU R$ 0,12-0,50/doc |
| **P4 AI-DPO Copilot** | Per seat (3 tiers) | R$ 380-850/seat/mês |
| **P5 ETL/Middleware** | Projeto + manutenção | Setup R$ 25-120k + R$ 1.500-6.500/mês |

## Função probabilística de pricing (operacionalizada)

```
P(produto, persona) = max(
    P_custo: custo_unit × (1 + margem_alvo 70-85%),
    P_competitivo: benchmark × 1.10 (diferencial NeoGov),
    P_valor: WTP × 0.75 (captura conservadora)
)
```

## Custos Fixos Mensais NeoGov (Wave 1 · P50)

```
Pró-labores 4 sócios:        R$ 53.000  🟡 lastreado LASTRO-PL-01 a 04
Folha CLT 4 funcionários:    R$ 37.000  ✅ Robert Half 2026
Encargos CLT (Simples ~28%): R$ 10.360
Infraestrutura cloud BR:     R$ 15.300  🟡 LASTRO-01 D003
Software + Operacional:      R$ 6.400   🟢 mercado 2026
Marketing + Vendas Wave 1:   R$ 17.000  🟡 benchmark CAC
Contingência (5%):           R$ 6.950
─────────────────────────────────────
TOTAL FIXO MENSAL P50:       R$ 146.010
```

CAPEX inicial total: R$ 87k-298k (R$ 170k P50)
Break-even: 30-50 clientes ativos no Wave 1

## Lastros estabelecidos (D-015)

| ID | Campo | VVV atual | Sprint destino dado primário |
|---|---|---:|---|
| LASTRO-PL-01 a 04 | Pró-labores 4 sócios | 0.70 | S3.0.2 (decisão societária · 7 dias) |
| LASTRO-FOLHA-CLT | Salários CLT 2026 | 0.95 | ✅ Robert Half + HuntIT validado |
| LASTRO-TRIB-01 | Simples Nacional Anexo III 2026 | 1.00 | ✅ Contabilizei validado |
| LASTRO-01 D003 | Cloud L40S BR | 0.70 | S2.5.3 (cotações reais · 5 dias) |
| LASTRO-02 D003 | Fine-tune QLoRA | 0.85 | S2.5.2 (POC ~R$ 50) |
| LASTRO-CAC-01 | CAC Legaltech 2026 | 0.85 | ✅ PoweredBySearch validado |
| LASTRO-WTP | Willingness to Pay | **0.35** 🔴 | **S3.0.3 (entrevistas Van Westendorp · 15-30 dias)** |

## Fila DTP REORDENADA pós-S3.0.1 v2.0

```
🥇 PRÓXIMO · Sprint S3.0.2 · Validação Societária (paralelo S2.5)
   ├─ Reunião 4 sócios + contador
   ├─ Definir pró-labores reais (LASTRO-PL-01 a 04)
   ├─ Confirmar CNAE + Anexo Simples (Fator R ≥ 32%)
   └─ Output: tabela definitiva salários · refatorar §2.2 S3.0.1
   Prazo: 7 dias úteis

🥈 Sprint S2.5 · Quitar D003 v2 (arquitetura IA)
   ├─ S2.5.1 → Stack com Camila CTO
   ├─ S2.5.2 → POC fine-tune (~R$ 50)
   ├─ S2.5.3 → Cotações cloud BR (LASTRO-01 → ✅)
   ├─ S2.5.4 → Arquitetura 3-tier final
   └─ S2.5.5 → Cap 11 §arquitetura
   Prazo: 10-15 dias úteis

🥉 Sprint S3.0.3 · Validação WTP (CRÍTICO destrava VVV)
   ├─ 15-20 entrevistas Van Westendorp por cluster
   ├─ Refinar pricing §10 S3.0.1
   └─ Output: ranges WTP-validated (VVV 0.78 → 0.85+)
   Prazo: 15-30 dias úteis

🔢 Sprint S3.0.4 · APENDICE-D-MODELO-CUSTO-PRICING.xlsx
   └─ Planilha viva 9 abas · só após LASTROS resolvidos

🔢 Sprint S3.0.5 · Retificar Cap 11 §pricing
   └─ Substituir VVV 0.65 → VVV 0.85+

🔢 Sprint S5.0.5 · Quitar D002 (MEDIUM) auditoria cognitiva
```

## Débitos Técnicos · Status atualizado

| ID | Status | Próxima ação |
|---|---|---|
| **D003 v2** | 🔴 CRITICAL · ATIVO | Disparar S2.5 (Camila CTO + POC + cotações) |
| **D001** (pricing) | 🟡 MITIGADO · S3.0.1 v2.0 entregou metodologia | Validar S3.0.2 + S3.0.3 para quitar |
| **D002** (cognitivo) | 🟡 MEDIUM · aguardando | S5.0.5 |
| **D-014** (metodológico) | ✅ INCORPORADO em POP §1 | Permanente |
| **D-015** (estimativa-lastreada) | ✅ INCORPORADO em POP §7 + aplicado em S3.0.1 v2.0 | Permanente |

## Decisões emergentes deste Sprint

| ID novo | Conteúdo |
|---|---|
| **D-016** (a registrar) | Aplicar BA-Orchestration BABOK v3 como pacote orquestrado em sprints analíticos (estimation + decision-analysis + benchmarking + risk-analysis + BMC + prioritization) |
| **D-017** (a registrar) | Modelos de cobrança vencedores via weighted scoring: P1 Tier · P2 Híbrido · P3 Dual · P4 Per seat · P5 Projeto+manutenção |
| **D-018** (a registrar) | Função probabilística de pricing operacionalizada: P = max(P_custo, P_competitivo, P_valor) com cenários P10/P50/P90 |

## Insights emergentes deste Sprint

| ID novo | Conteúdo |
|---|---|
| **IN-015** | Break-even crítico Wave 1 = 50+ clientes ativos (curva economia de escala) |
| **IN-016** | Fator R amarra modelo de custo ao de receita (folha ≥ 32% receita) — pricing assertivo deve assegurar isso |
| **IN-017** | LTV/CAC absurdamente altos (135-245:1) sinalizam CAC subestimado ou churn assumido baixo · validar WTP é ESSENCIAL |
| **IN-018** | Stack BA-Orchestration BABOK v3 é a forma correta de fazer análise estratégica densa (skills aplicadas em sequência, não isoladas) |

## Cadeia de hashes (atualizada)

| Hash | Sprint | Status |
|---|---|---|
| ... (anterior · mantidas) | ... | ... |
| `NEOGOV-V21-S3.0.1-INVALIDADO+D003-V2+POP-v2.1.1.1-PUBLICADO-AWAIT-S2.5-OR-COMBO` | POP-pub | SUPERSEDED |
| `NEOGOV-V21-S3.0.1-v2.0-MODELAGEM-PRICING-DONE-AWAIT-VALIDATION` | S3.0.1-v2 | **ATIVO** |

## Próxima ação imediata

```
Aguardar input do usuário sobre:

(A) Aprovar metodologia BA-Orchestration aplicada em S3.0.1 v2.0?
(B) Aprovar ranges de pricing P10/P50/P90 propostos?
(C) Decidir ordem dos próximos sprints:
    - S3.0.2 (societária) + S2.5 (D003) em paralelo
    - S3.0.3 (WTP) imediato (destrava VVV mais rápido)
    - S2.5 antes (resolver D003 first)
(D) Pular para S3.0.4 xlsx com lastros atuais (rápido mas com 🟡 amarelos)?

OU: outras correções/adições solicitadas pelo usuário
```

---

**Sprint 3.0.1 v2.0 entregue** · 6 skills BA-Orchestration aplicadas · POP v2.1.1.1 honrado · D003-v2 honrado · D-015 honrado em 6 lastros.
