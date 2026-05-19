---
id: NEOGOV-V21-WAL-CONTINUIDADE
filename: WAL-CONTINUIDADE-v1.0.1.md
created_at: 2026-05-16T10:45:00Z
type: CONTINUITY_HANDOFF_DOCUMENT
version: v1.0.1
sprint: W1.3
edicao: 1
proposito: Documento de referência + instrução de como continuar (mandato usuário · ondas de tasks)
fonte_unica: data/neogov-pricing-cost-ssot-latest.json (v1.0.8 · SEMPRE validar antes de consumir)
mandato: WAL contínuo · repetir a cada ação · ondas de tasks seguintes
---

# 📑 WAL · DOCUMENTO DE REFERÊNCIA & CONTINUIDADE
## Ciclo 6 · pós-Cap 16 · onda W1.3

> **Para que serve este documento**: é o handoff que permite retomar o trabalho de onde parou, em qualquer sessão, sem perder contexto. Quem ler isto sabe (a) o que já existe e é verdade, (b) como continuar, (c) o que validar antes.

---

## 1 · DOCUMENTOS DE REFERÊNCIA (fonte da verdade · hierarquia)

| Nível | Documento | Papel | Validar? |
|:--:|---|---|:--:|
| 0 | `/mnt/project/INSTRUCAO-PROTOCOLO-OPERACIONAL-NEOGOV-v2_1_1_2.md` | POP MASTER · sobrescreve conflitos | — |
| 1 | `data/neogov-pricing-cost-ssot-latest.json` (**v1.0.8**) | **FONTE ÚNICA** · 21 tiers · 5 segmentos | ✅ SEMPRE antes de consumir |
| 2 | `content/15-financeiro-latest.md` | DRE/FCD · E[VPL] R$19,6M | lê fonte 1 |
| 2 | `content/16-investimento-latest.md` | Rodada R$3,5M · diluição 15-30% | lê fonte 1 + Cap 15 |
| 3 | `data/dre_fcd-latest.py` · `runway_captacao-latest.py` | LÓGICA rastreável | reproduzível |
| 3 | `content/12-bmc-latest.md` · `13-vpc-latest.md` | BMC/VPC 5 segmentos | lê fonte 1 |

**Regra de ouro do documento de referência**: a fonte 1 (JSON) manda. Qualquer capítulo que divergir dela está errado — o capítulo se ajusta, nunca a fonte se ajusta ao capítulo.

---

## 2 · COMO CONTINUAR A PRÓXIMA ATIVIDADE (instrução operacional)

```
PASSO 1 · PRE-ALWAYS + 5W1H da próxima ação (definida por FDC-U na §5 abaixo)
PASSO 2 · Validar SSOT v1.0.8 ANTES de consumir (python: assert version + tiers + 0 órfãos)
PASSO 3 · Executar a ação (cálculo Python rastreável SE houver número novo)
PASSO 4 · Versionar com edição antecipada (AP-14): {arquivo}-v[N].{SPRINT}.{EDIÇÃO} + -latest
PASSO 5 · present_files + sincronizar -latest
PASSO 6 · Engatar este WAL de novo (recap → validação hostil → débitos → FDC-U → 5W1H)
PASSO 7 · [MANDATO CONTÍNUO] repetir · atuar em ondas de tasks seguintes
```

**Validação da ação atual (Cap 16) por revisão hostil ágil:**

```
PQMS Cap 16: Bruto 9.52 × VVV 0.72 = 6.85 🟡 (honesto · valuation pré-receita puxa)

REVISÃO HOSTIL ÁGIL (3 ataques):
  ⚔️ "Buffer 40% arbitrário" → PROCEDE · marcado D-015 · prática reconhecida ·
     modelar variância seria fora de escopo pré-piloto
  ⚔️ "Haircut valuation é chute" → PROCEDE estrutural · valuation pré-receita É
     negociado · entreguei BANDA não ponto · gerei D001-NOVO-22 (honestidade>precisão)
  ⚔️ "EBITDA≠caixa, vale pior" → VERDADE · declarado §16.1 · buffer absorve parcial ·
     D001-NOVO-20 refina c/ modelo caixa direto
  VEREDITO: Cap 16 ÍNTEGRO · estimativas DECLARADAS · 1 débito novo (D001-NOVO-22)
            Princípio central (dimensionar pela queima não pelo valuation) = sólido
```

---

## 3 · DÉBITOS / PENDÊNCIAS / TASKS (situação não-concluída)

| # | Item | Estado | Sev |
|:--:|---|:--:|:--:|
| Cap 16 | Tese investimento | ✅ CONCLUÍDO | — |
| D001-NOVO-21 | Dimensionar rodada | ✅ RESOLVIDO | — |
| **Cap 17** | Riscos (cenário A + D-015 + diluição) | 🔴 pendente · desbloqueado | 🔴 |
| **D001-NOVO-22** | Validar valuation c/ term sheet real | 🟡 novo · pós-captação | 🟡 |
| **§13.5.3-fix** | Cap 13 reflete 3 sub-tiers III | 🟢 cosmético | 🟢 |
| **P2-fix** | Cap 12 §12.12 cita curva v1 | 🟡 leve | 🟡 |
| D001-NOVO-20 | Calibrar WACC/modelo caixa direto | 🟡 depende captação | 🟡 |
| D001-NOVO-19/7/8/6 | L1A SaaS/WTP/ABC/horímetro | 🟡 calibram piloto | 🟡 |

**Onda W1.3 (status)**: P2→P3→P5→D17→Cap16 ✅ · falta Cap 17 para fechar o bloco financeiro-risco. Resíduos cosméticos (§13.5.3, P2-fix) podem ir em onda de limpeza posterior.

---

## 4 · MANDATOS PERMANENTES (lembrar sempre)

```
✅ FONTE ÚNICA = JSON · SEMPRE validar antes de consumir (version+tiers+órfãos)
✅ Versionamento edição antecipada (AP-14) · {arquivo}-v[N].{SPRINT}.{EDIÇÃO} + -latest
✅ Nomenclatura (AP-04) · NUNCA NEOGOV-BP* nem CIT*
✅ RGO-9 honestidade > aparência · PMQS não inflado · estimativas marcadas 🟡 D-015
✅ RGO-4 não construir sobre base instável · RGO-3 ordem certa
✅ Estilo educacional · explicar o PORQUÊ de cada escolha
✅ MANDATO CONTÍNUO · repetir WAL a cada ação · ATUAR EM ONDAS DE TASKS
```

---

## 5 · FDC-U · PRÓXIMA AÇÃO (critério de decisão)

| Dimensão | Peso | Cap 17 | §13.5.3-fix | P2-fix |
|---|:--:|:--:|:--:|:--:|
| Fecha bloco financeiro-risco (onda W1.3) | 0.22 | **10** | 3 | 3 |
| RGO-3 ordem (riscos após estrutura capital) | 0.18 | **9** | 4 | 4 |
| Consome trabalho recém-feito (Cap15/16) | 0.16 | **9** | 5 | 4 |
| Mandato usuário (avançar BP em ondas) | 0.15 | **9** | 4 | 4 |
| RGO-4 base estável | 0.12 | 8 | 7 | 7 |
| Velocidade | 0.09 | 5 | **9** | **8** |
| Honestidade FATO | 0.08 | **9** | 7 | 7 |
| **PONDERADO** | 1.00 | **🥇 8.74** | 4.86 | 4.66 |

**Vencedor: Cap 17 Riscos · 8.74** — fecha a onda W1.3 (bloco financeiro-risco). Consome cenário A (Cap 15) + diluição (Cap 16) + estimativas D-015 acumuladas → matriz de riscos quantificada. RGO-3: riscos vêm *depois* da estrutura de capital (referenciam-na). Resíduos cosméticos vão em onda de limpeza posterior (não bloqueiam).

### 5W1H · Cap 17 (próxima ação)

| | |
|---|---|
| WHAT | Cap 17 Riscos: matriz de riscos quantificada (cenário A, diluição, débitos D-015, fratura interna equipe, dependência sigilo cartório) + mitigações |
| WHY | FDC-U 8.74 · fecha onda W1.3 · consome Cap 15/16 · RGO-3 (riscos após capital) |
| HOW | Inventário riscos × probabilidade × impacto → matriz → mitigação · explicar porquê cada risco importa (educacional) · 🟡 D-015 |
| WHEN | Próxima onda (continuidade automática) |
| WHERE | `content/17-riscos-v1.0.1.md` |
| WHO | AG-0 · validar SSOT v1.0.8 antes |

---

**FIM WAL-CONTINUIDADE v1.0.1** · próxima ação: Cap 17 (FDC-U 8.74) · mandato contínuo ativo · onda W1.3 quase fechada
