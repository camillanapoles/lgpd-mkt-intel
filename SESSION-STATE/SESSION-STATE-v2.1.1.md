---
id: NEOGOV-V21-SESSION-STATE
filename: SESSION-STATE.md
created_at: 2026-05-14
last_updated: 2026-05-14T23:55:00Z
type: WAL_MASTER_CONTINUITY
status: ACTIVE
parent_session: NEOGOV-V21-AUDIT-FRAMEWORK-2026-05-14
continuity_hash: NEOGOV-V21-S1.1-DONE-AWAIT-S1.2
tags: [wal, continuidade, session-state, master]
---

# Session State Master · NeoGov BP v2.1

## Estado da produção

| Item | Valor |
|---|---|
| Versão alvo | BP v2.1 |
| Empresa | NeoGov (ICT privado) |
| Data início produção | 2026-05-14 |
| Sprint atual | Sprint 1.1 fechado · Sprint 1.2 a iniciar |
| Sprints planejados | 5 + Consolidação |
| Sprints concluídos | 1 (S1.1) |
| Anexos vivos | A (12 entradas VVV) · B (5 decisões D-001 a D-005) · C (4 insights IN-001 a IN-004) |
| Capítulos produzidos | content/04-design-thinking.md (PMQS 9.50 × VVV 0.92 = 8.74) |
| Hash continuidade | `NEOGOV-V21-S1.1-DONE-AWAIT-S1.2` |

## Fontes canônicas (hierarquia)

1. `/mnt/user-data/uploads/inst-lgpd.md` — lógica geradora Design Thinking · VVV=1.0
2. `/mnt/user-data/uploads/SESSION-STATE.md` — estado herdado v2.0
3. `/mnt/user-data/uploads/NEOGOV-BUSINESS-PLAN-FINAL.docx/md` — corpo aprovado v2.0
4. `/mnt/user-data/uploads/NEOGOV-DATA-v2.json` — modelo dados estruturado
5. `/mnt/user-data/uploads/transcricao-reuniao-neogov.txt` — fonte primária VVV=1.0

## Anti-padrões absolutos (memória vigente)

- 🚫 Filename pattern `NEOGOV-BP*` ou `CIT-AI-TECH-*` para novos artefatos
- 🚫 Tratar persona como cluster
- 🚫 Reescrever conteúdo aprovado do BP v2.0
- 🚫 Especular sem tag `[INFERÊNCIA]` ou `[ESPECULAÇÃO]`
- 🚫 Fee-for-service como modelo (Camila: "corpo a corpo está ficando passado")
- 🚫 Esquecer Wave 4 Delta = vitória sem batalha Sun Tzu Cap III §3
- 🚫 DT como decoração — DT deve **gerar** o conteúdo
- 🚫 Frameworks ocidentais isolados — sempre dentro da estrutura DT
- 🚫 Editar arquivo sem criar nova edição antecipada (viola mandato versionamento)
- 🚫 Apagar/sobrescrever edições anteriores (histórico é imutável)

## Mandato Versionamento (PROTOCOLO PERMANENTE)

Padrão obrigatório para TODOS os artefatos:

```
{filename}-v2.{SPRINT}.{EDICAO}.{ext}    ← versionado, imutável
{filename}-latest.{ext}                  ← cópia da última edição
```

### Regras operacionais

1. **Criar EDICAO+1 ANTES de editar** — toda edição cria arquivo novo, não sobrescreve
2. **Atualizar `-latest.{ext}`** — sempre cópia idêntica da última edição
3. **Edições anteriores ficam no histórico** — nunca apagar
4. **Aplica-se a content/, anexos/, continuity/, data/**

### Exemplos práticos

```
Sprint 1.1 primeira escrita do Cap 04:
  → criar: 04-design-thinking-v2.1.1.md
  → atualizar: 04-design-thinking-latest.md (cópia da v2.1.1)

Sprint 1.1 recebe ajuste durante mesmo sprint:
  → criar: 04-design-thinking-v2.1.2.md (antecipado, vazio ou copy da v2.1.1)
  → editar v2.1.2 com mudanças
  → atualizar: 04-design-thinking-latest.md (cópia da v2.1.2)

Sprint 1.2 referencia Cap 04:
  → sempre lê: 04-design-thinking-latest.md
  → garantia: tem a versão mais recente
```

## Fila DTP (sprints planejados)

```
SPRINT 1 · núcleo gerador (Wave 1 crítica)
├─ S1.1 → content/04-design-thinking.md  ★ próximo
├─ S1.2 → content/07-personas.md
├─ S1.3 → content/11-produtos.md
└─ GATE 1

SPRINT 2 · identidade e abertura
├─ S2.1 → content/02-vmv.md
├─ S2.2 → content/01-capa-ficha.md
└─ GATE 2

SPRINT 3 · análise estratégica de profundidade
├─ S3.1 → content/12-bmc.md
├─ S3.2 → content/13-vpc.md
├─ S3.3 → content/09-porter.md
└─ GATE 3

SPRINT 4 · camada operacional
├─ S4.1 → content/16-equipe-governanca.md
├─ S4.2 → content/15-financeiro.md (+ XLSX anexo)
├─ S4.3 → content/14-gtm-waves.md
└─ GATE 4

SPRINT 5 · refinamentos
├─ S5.1 → content/08-clusters-fdcu.md
├─ S5.2 → content/{05,06,10,17,18}.md
├─ S5.3 → content/03-sumario-executivo.md (lê tudo, escreve por último)
└─ GATE 5

CONSOLIDAÇÃO
├─ C.1 → BUSINESS-PLAN-FINAL-v2.1.docx
├─ C.2 → APENDICE-D-MODELO-FINANCEIRO.xlsx
├─ C.3 → Vue App + GitHub Actions
├─ C.4 → PDF + slides executive summary
└─ GATE FINAL
```

## Definition of Done (por sprint)

- [ ] Capítulo MD salvo em `content/{NN-nome}.md`
- [ ] PMQS ≥ 9.5 documentado em DECISIONS-LOG
- [ ] Afirmações adicionadas ao VVV-LOG com classificação
- [ ] Decisões adicionadas ao DECISIONS-LOG com rationale
- [ ] Insights adicionados ao INSIGHTS-CARRY (se houver)
- [ ] Hash continuidade atualizado neste arquivo
- [ ] Render preview docx validado (renderiza bem em Word)
- [ ] Gate aprovação usuário

## Checklist start-of-sprint

- [ ] Ler `SESSION-STATE.md` (este arquivo)
- [ ] Ler `INSIGHTS-CARRY` com `sprint_destino == sprint_atual`
- [ ] Ler `VVV-LOG` (afirmações já validadas)
- [ ] Ler `DECISIONS-LOG` (decisões que constrangem este sprint)
- [ ] Confirmar fontes canônicas ainda válidas
- [ ] Dispatch DTP enumerando tarefas
- [ ] PIER (gerar abordagens, selecionar, executar)

## Cadeia de hashes (continuidade comprovável)

| Hash | Sprint | Data | Status |
|---|---|---|---|
| `NEOGOV-V21-S0-INIT-AWAIT-S1.1` | S0 | 2026-05-14 | FECHADO |
| `NEOGOV-V21-S1.1-DONE-AWAIT-S1.2` | S1.1 | 2026-05-14 | ATIVO |

## Próximas 3 ações imediatas

1. **Gate aprovação Sprint 1.1** — usuário valida Cap 04 + anexos atualizados
2. **Sprint 1.2**: produzir `content/07-personas.md` (FDC-U 9.2) consumindo IN-001 e IN-003
3. **Sprint 1.3**: produzir `content/11-produtos.md` (FDC-U 9.0) consumindo IN-002 e IN-004

---

## Glossário de termos canônicos

| Sigla | Significado |
|---|---|
| VVV | Validation · Verification · Veracity |
| PMQS | Production · Maturity · Quality · Score (≥ 9.5 alvo) |
| FDC-U | Framework Decisional de Cluster (13 dimensões) |
| DT | Design Thinking (5 fases canônicas IDEO) |
| DTP | Decision Topology Protocol (orquestrador) |
| MO | Modus Operandi (executor tático) |
| CM | Check-Mate (protocolo de correção) |
| HIQM | Holistic Iterative Quality Module (auditor consciente) |
| BMC | Business Model Canvas (Osterwalder 9 blocos) |
| VPC | Value Proposition Canvas (Osterwalder 2 lados) |
