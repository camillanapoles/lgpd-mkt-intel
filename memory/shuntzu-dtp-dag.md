---
type: shuntzu-dtp-dag
version: 1.0.0
last_updated: 2026-05-09T22:35:00-03:00
reference_rule: ~/.claude/rules/shuntzu-continuity.md
reference_omnibus: SHUN_TZU-ART_OF_WAR/OMNIBUS/DTP-VECTOR.md
---

# DTP DAG — Decision Tree Persistence

Decision DAG per OMNIBUS DTP-VECTOR. Tracks resolved + pending decision nodes. Restored on session resume per continuity §"Cross-Session Continuity".

## Node Schema

```
{ id, phase, type, status, depends_on, output_artifact, timestamp }
```

Status values: PENDING | IN_PROGRESS | RESOLVED | BLOCKED | SKIPPED

---

## Resolved Nodes

### ADW-a1f12902 — INFRA_BOOT_SEQ
- **id**: ADW-a1f12902
- **phase**: BOOT
- **type**: bootstrap
- **status**: RESOLVED (COMPLETE)
- **depends_on**: []
- **output_artifact**: `.claude/wal/shuntzu-operations.log` + `memory/shuntzu-*.md`
- **timestamp**: 2026-05-09T22:35:00-03:00
- **notes**: Continuity infrastructure created per shuntzu-continuity rule mandate

---

## Pending Nodes

### Phase 1 — Foundation (presentation/data integrity)

#### NODE-P1A — Continuity Infrastructure
- **status**: RESOLVED (this session)
- **depends_on**: []
- **output**: WAL + 3 memory files

#### NODE-P1B — Info Button (W3) per card
- **status**: RESOLVED (commit 5ac9f73 "feat: W3 — Info button expandivel em todos componentes")
- **depends_on**: NODE-P1A
- **output**: Info button on every component

#### NODE-P1C — VVV audit against transcripts
- **status**: PENDING
- **depends_on**: NODE-P1A
- **target**: raise lois_zero, conversao_zero, custo_dev_unknown from gaps to 0.85+
- **output**: updated `vvv_source` + `vvv_updated` per card
- **success_criteria**: GOVERNANCE.md R5 — "Score honesto mesmo se baixo"

### Phase 2 — Sub-Engine + Reactivity

#### NODE-P2A — Sub-Engine per audience (R3)
- **status**: RESOLVED (commit 530d575 "feat: Wave 2 — FdcuInteractive JSON props, Status Page, Sub-Engine toggle")
- **depends_on**: NODE-P1A
- **output**: 5 audiences with custom_weights, toggle global ↔ per-public

#### NODE-P2B — Status Page [PESQUISANDO]/[CONCLUIDO]
- **status**: RESOLVED (commit 530d575)
- **depends_on**: NODE-P1A
- **output**: per-item research status

#### NODE-P2C — Slider reactivity verification (R7)
- **status**: PENDING
- **depends_on**: NODE-P2A
- **target**: any slider change triggers full re-eval (global + per-dim + per-item)
- **success_criteria**: GOVERNANCE.md R7 "Orquestracao reativa"

### Phase 3 — Validation + Quality

#### NODE-P3A — E2E tests per tab
- **status**: PENDING
- **depends_on**: NODE-P2C
- **target**: each Vue tab has Playwright/Vitest E2E
- **success_criteria**: CLAUDE.md "Pending Requirements"

#### NODE-P3B — Build clean + GitHub Pages live
- **status**: ONGOING (verified each push)
- **depends_on**: NODE-P3A
- **target**: `bun run build` passes, deploy at https://camillanapoles.github.io/lgpd-mkt-intel/

#### NODE-P3C — VVV provenance file:linha (R1)
- **status**: PENDING
- **depends_on**: NODE-P1C
- **target**: each SNTI item has `fonte` with `file:linha` precision
- **target_score**: avg VVV 0.93 → 0.97

---

## Phase Tracking

| Phase | Total Nodes | Resolved | Pending | Blocked |
|-------|-------------|----------|---------|---------|
| BOOT | 1 | 1 | 0 | 0 |
| 1 (Foundation) | 3 | 2 | 1 | 0 |
| 2 (Sub-Engine) | 3 | 2 | 1 | 0 |
| 3 (Validation) | 3 | 0 | 3 (1 ongoing) | 0 |
| **Total** | **10** | **5** | **5** | **0** |

## Dependency Graph (text DAG)

```
ADW-a1f12902 (BOOT)
    └── P1A (RESOLVED)
            ├── P1B (RESOLVED)
            ├── P1C (PENDING) ──┐
            └── P2A (RESOLVED) ──┐
                    └── P2B (RESOLVED)
                    └── P2C (PENDING)
                            └── P3A (PENDING)
                                    └── P3B (ONGOING)
                                            └── P3C (PENDING) ←── P1C
```

## Resume Protocol

On context loss, agent must:
1. Read this file
2. Verify all RESOLVED nodes still have their output artifacts
3. Pick next PENDING node whose `depends_on` are all RESOLVED
4. Append WAL entry before executing

## Anti-Drift

- Never mark RESOLVED without artifact verification
- Never skip PENDING with unmet dependencies
- BLOCKED status requires `blocker_reason` field — escalate to user
