---
id: NEOGOV-V21-WAL-CONTINUIDADE
filename: WAL-CONTINUIDADE-v1.0.2.md
created_at: 2026-05-16T11:20:00Z
type: CONTINUITY_HANDOFF_DOCUMENT
version: v1.0.2
supersedes: WAL-CONTINUIDADE-v1.0.1.md (pré-Cap17 · onda W1.3 aberta)
sprint: W1.3
edicao: 2
proposito: Documento referência + como continuar (mandato · ondas de tasks)
fonte_unica: data/neogov-pricing-cost-ssot-latest.json (v1.0.8 · SEMPRE validar)
mandato: WAL contínuo · repetir a cada ação · ondas de tasks
---

# 📑 WAL · DOCUMENTO DE REFERÊNCIA & CONTINUIDADE
## Ciclo 7 · ONDA W1.3 FECHADA · próxima onda W1.4

---

## 1 · DOCUMENTOS DE REFERÊNCIA (fonte da verdade · hierarquia)

| Nível | Documento | Papel | Validar? |
|:--:|---|---|:--:|
| 0 | `/mnt/project/INSTRUCAO-PROTOCOLO-OPERACIONAL-NEOGOV-v2_1_1_2.md` | POP MASTER | — |
| 1 | `data/neogov-pricing-cost-ssot-latest.json` (**v1.0.8**) | **FONTE ÚNICA** · 21 tiers · 5 segmentos | ✅ SEMPRE |
| 2 | `content/15-financeiro-latest.md` | DRE/FCD · E[VPL] R$19,6M | lê fonte 1 |
| 2 | `content/16-investimento-latest.md` | Rodada R$3,5M · diluição 15-30% | lê 1+Cap15 |
| 2 | `content/17-riscos-latest.md` | Matriz 9 riscos · R1 crítico | lê 1+Cap15/16 |
| 2 | `content/12-bmc-latest.md` · `13-vpc-latest.md` | BMC/VPC 5 seg · patches aplicados | lê fonte 1 |
| 3 | `data/dre_fcd-latest.py` · `runway_captacao-latest.py` · `curva_ponto_sucesso-latest.py` | LÓGICA rastreável | reproduzível |

**Regra de ouro**: fonte 1 (JSON) manda. Capítulo que divergir está errado — o capítulo se ajusta.

---

## 2 · COMO CONTINUAR + VALIDAÇÃO HOSTIL (ação atual)

```
PASSO 1 · PRE-ALWAYS + 5W1H da próxima ação (FDC-U §5)
PASSO 2 · Validar SSOT v1.0.8 ANTES de consumir
PASSO 3 · Executar (cálculo Python rastreável SE número novo)
PASSO 4 · Versionar edição antecipada (AP-14) + -latest
PASSO 5 · present_files
PASSO 6 · Engatar WAL (recap → doc-ref+como-continuar c/ validação hostil → débitos → FDC-U → 5W1H)
PASSO 7 · [MANDATO CONTÍNUO] repetir · ATUAR EM ONDAS
```

**Validação hostil ágil — onda W1.3 (Cap 17 + 2 patches):**

```
PQMS Cap 17: Bruto 9.55 × VVV 0.78 = 7.45 🟡 honesto

REVISÃO HOSTIL ÁGIL (3 ataques):
  ⚔️ "Scores P/I subjetivos" → PROCEDE parcial · método (×, faixas) torna
     auditável não arbitrário · D-015
  ⚔️ "Expor R1 afasta investidor" → INVERTE · esconder e ser pego destrói
     credibilidade · honestidade proativa = alavanca (RGO-9)
  ⚔️ "Faltam riscos?" → cobre materiais ao estágio · câmbio/escala pós-Wave1
  PATCHES: §13.5.3-fix (Cap13→3 sub-tiers) + P2-fix (Cap12→curva v2) ·
     cirúrgicos · str_replace · não reescreveram conteúdo aprovado (AP-06)
  VEREDITO: onda W1.3 ÍNTEGRA · R1 sinalizado sem máscara · bloco fechado
```

---

## 3 · DÉBITOS / PENDÊNCIAS / TASKS

| # | Item | Estado | Sev |
|:--:|---|:--:|:--:|
| Cap 17 | Riscos | ✅ CONCLUÍDO | — |
| §13.5.3-fix | Cap13 3 sub-tiers | ✅ RESOLVIDO | — |
| P2-fix | Cap12 curva v2 | ✅ RESOLVIDO | — |
| **ONDA W1.3** | Bloco financeiro-risco | ✅ **FECHADA** | — |
| **Onda W1.4** | Consolidação tripé (docx/md/Vue) + pitch | 🔴 próxima onda | 🔴 |
| D001-NOVO-22 | Validar valuation term sheet | 🟡 pós-captação | 🟡 |
| D001-NOVO-20 | Calibrar WACC/caixa direto | 🟡 depende captação | 🟡 |
| D001-NOVO-19/7/8/6/4 | L1A/WTP/ABC/horímetro/PoC IA | 🟡 calibram piloto | 🟡 |
| D001-NOVO-16/18 | Arrecadação cartório (sigilosa) | 🟢 mitigado (faixa FATO) | 🟢 |

**Ondas concluídas**: W1.2 (pricing-audit) · **W1.3 (financeiro-risco · P2→P3→P5→D17→Cap16→Cap17 ✅)**
**Próxima onda W1.4**: consolidar BP completo (capítulos avulsos → tripé multi-output) + pitch investidor.

---

## 4 · MANDATOS PERMANENTES

```
✅ FONTE ÚNICA = JSON v1.0.8 · SEMPRE validar antes de consumir
✅ Versionamento edição antecipada (AP-14) + -latest
✅ Nomenclatura (AP-04) · NUNCA NEOGOV-BP*/CIT*
✅ RGO-9 honestidade>aparência · PMQS não inflado · 🟡 D-015 marcado
✅ RGO-4 base estável · RGO-3 ordem certa · AP-06 não reescrever aprovado
✅ Estilo educacional · explicar o PORQUÊ
✅ MANDATO CONTÍNUO · WAL a cada ação · ATUAR EM ONDAS
```

---

## 5 · FDC-U · PRÓXIMA AÇÃO (onda W1.4)

| Dimensão | Peso | Consolidar BP | Pitch | D-debt piloto |
|---|:--:|:--:|:--:|:--:|
| Mandato usuário (tripé multi-output) | 0.22 | **10** | 6 | 2 |
| Entregável final do BP | 0.20 | **10** | 7 | 2 |
| RGO-3 (consolidar antes de pitch) | 0.16 | **9** | 5 | 4 |
| Consome onda W1.3 fechada | 0.15 | **9** | 8 | 3 |
| Valor para stakeholder | 0.13 | 8 | **9** | 4 |
| Velocidade | 0.08 | 5 | 6 | **8** |
| RGO-4 base estável | 0.06 | 9 | 7 | 6 |
| **PONDERADO** | 1.00 | **🥇 9.06** | 6.72 | 3.16 |

**Vencedor: Consolidar BP · 9.06** — onda W1.3 fechada significa que os capítulos 12-17 estão íntegros sobre SSOT v1.0.8. Mandato do usuário = tripé multi-output (docx técnico + md fonte + Vue.js interativo). Consolidar ANTES do pitch (RGO-3: pitch deriva do BP consolidado, não o inverso).

### 5W1H · Onda W1.4 (próxima)

| | |
|---|---|
| WHAT | Consolidar BP: índice mestre dos capítulos + verificação de consistência cruzada (todos lendo SSOT v1.0.8) → preparar tripé docx/md/Vue |
| WHY | FDC-U 9.06 · mandato tripé multi-output · onda W1.3 entregou os capítulos · RGO-3 |
| HOW | Catálogo mestre + matriz de consistência (cap × versão × fonte) → identificar gaps de capítulos faltantes (1-11, 14, 18) → plano de consolidação |
| WHEN | Próxima onda |
| WHERE | `continuity/CATALOGO-MESTRE-v1.0.1.md` + plano tripé |
| WHO | AG-0 · validar SSOT v1.0.8 antes |

---

**FIM WAL-CONTINUIDADE v1.0.2** · onda W1.3 FECHADA · próxima: onda W1.4 consolidação (FDC-U 9.06) · mandato contínuo ativo
