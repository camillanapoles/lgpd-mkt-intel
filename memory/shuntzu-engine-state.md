---
type: shuntzu-engine-state
version: 1.0.0
last_updated: 2026-05-09T22:35:00-03:00
reference_rule: ~/.claude/rules/shuntzu-continuity.md
data_source: presentation-vue/public/strategic-data-unified.json
---

# Shun Tzu Engine State

Live snapshot of OMNIBUS/MEEST-AE engine pipeline. Restored on session resume per continuity §"Cross-Session Continuity".

## Pipeline Position (S→Q→I→A)

| Field | Value |
|-------|-------|
| current_phase | IDLE |
| last_completed | A (Adversarial) — for items already validated in JSON |
| next_action | Awaiting user/orchestrator trigger |
| pending_items | none in active queue |

Stages:
- **S** (Socratic) — question generation
- **Q** (Questioner) — evidence gathering
- **I** (Innovator) — synthesis + scoring
- **A** (Adversarial) — challenge + finalization

Per-item S→Q→I→A trace lives inline in `strategic-data-unified.json` under `snti.dimensions.<dim>.items[].sqia_trace`.

## FDC-U Dimension Scores (Current Snapshot)

Source: `strategic-data-unified.json` § `snti.dimensions`. Weights per OMNIBUS FDC-U section.

| Dimension | Weight | Item Count | VVV Avg (raw) | Status |
|-----------|--------|-----------|---------------|--------|
| dao (Moral & Alinhamento) | 0.20 | 6 | 0.73 | ACTIVE |
| ceu (Tempo & Macro) | 0.20 | 7 | 0.91 | ACTIVE |
| terra (Terreno & Mercado) | 0.20 | 10 | 0.85 | ACTIVE |
| comandante (Lideranca) | 0.20 | 7 | 0.75 | ACTIVE |
| metodo (Disciplina & Execucao) | 0.20 | 8 | 0.55 | ACTIVE — DEGRADED (lois_zero, conversao_zero) |

Weighted Score (raw VVV, no decay): see App.vue computed `globalScoreSnti`.

## VVV Decay State (R1)

Formula: `vvv_decay = vvv × 1/(1 + 0.30 × meses)` (SaaS λ=0.30).

- All 38 cards have `vvv_updated` field; `vvv_decay` recomputed at load time
- Last bulk update: 2026-05-09 (see CNM cards file)
- Stale-check threshold: 6 months → flagged for revalidation per Anti-Drift Rules

## MEEST-AE Persona/Segment Context (R3 Sub-Engine)

5 audiences with custom_weights — each has its own SNTI score:

| Audience | Slug | Weight Profile | Score Status |
|----------|------|----------------|--------------|
| Prefeituras | prefeituras | terra-heavy | computed |
| Consorcios | consorcios | dao+terra | computed |
| TCEs | tces | ceu+metodo | computed |
| TCU | tcu | ceu+comandante | computed |
| ANPD | anpd | ceu+metodo | computed |

## Pending DTP DAG Decisions

See: `memory/shuntzu-dtp-dag.md` for full DAG.

Quick summary:
- **Resolved**: 1 node (ADW-a1f12902 INFRA_BOOT)
- **Pending**: Phase 1 (W3 info button complete), Phase 2 (sub-engine toggle complete), Phase 3 (E2E tests, VVV audit)

## Boot Order Status (per shuntzu-continuity §Module Priority Chain)

1. CE — READY (rules + memory loaded)
2. Planner — READY (S→Q→I→A pipeline IDLE)
3. WOE — READY (DAG file initialized)
4. IIM — READY (awaiting input)
5. E — READY (gated by IIM trigger)

## Resume Protocol

On context loss, agent must:
1. Read this file FIRST
2. Reconcile pipeline phase with WAL last entry
3. Reload CNM cards for VVV decay revalidation
4. Replay any UNCOMMITTED node from DAG
