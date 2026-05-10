# HIQM Rubric — LGPD Strategic Engine

**Version:** 1.0
**Target:** 95% (Qualidade Ouro)
**Source:** `SHUN_TZU-ART_OF_WAR/OMNIBUS_MODULE/HOLISTIC_ITERATIVE_QUALITY_MODULE_v1.0.md`
**Anchored ADW:** `specs/adw-a1f12902-omnibus-meest-ae-orchestration.md` (STEP 2.7)
**Scope:** All Vue components under `presentation-vue/src/components/strategic/`
**Owner:** Engine Quality Gate (HIQM Module)

---

## 1. The 10 HIQM Principles (Constitutional Reference)

Cited verbatim from the HIQM v1.0 source spec, section "Princípios Constitucionais de Qualidade Iterativa":

- **P1 — GARANTIA_EXISTENCIAL:** O processo HIQM nunca termina antes de atingir 95% de qualidade validada.
- **P2 — CHAIN_OF_THOUGHT_OBRIGATÓRIO:** Todo raciocínio deve ser explicitado, documentado e revisável (CE L2/L3).
- **P3 — ITERAÇÃO_SEM_PERDÃO:** Cada ciclo de refinamento deve melhorar objetivamente a métrica de qualidade.
- **P4 — QUALIDADE_QUANTIFICADA:** "Bom" é subjetivo; 95% é objetivo e mensurável via rubricas explícitas.
- **P5 — DOCUMENTAÇÃO_FRACTAL:** Cada fase S→Q→I→A interna possui seu próprio CoT e validação.
- **P6 — ANTI_PREMATURIDADE:** Proibição absoluta de entregar resultado antes da validação final.
- **P7 — RESILIÊNCIA_ITERATIVA:** Falhas em iterações são dados para próximas iterações (anti-fragilidade).
- **P8 — SOBERANIA_DA_QUALIDADE:** HIQM pode rejeitar entregas de outros módulos se abaixo de 95%.
- **P9 — CONTINUIDADE_GARANTIDA:** WAL persiste estado de cada iteração; nenhum progresso é perdido.
- **P10 — EXAUSTIVIDADE_MANDATÓRIA:** "Superficial" é falha constitucional; profundidade é requisito.

---

## 2. Quality Dimensions (Universal, 5 axes per component)

Each strategic component is scored across the same 5 dimensions. Each dimension is rated 0–100%. The component score is the unweighted mean (equal weights — every dimension is necessary, no dimension can compensate the absence of another, per P10).

### D1 — Scoring Dynamism (Engine reactivity)

The component must recompute scores reactively when sliders, overrides, or audience selection change. Static / hardcoded scores are a P6 violation. Anchored in MEEST-AE v1.0 FDC-U and project rule R6/R7 (no hardcoded scores; orchestration reactive).

### D2 — Info Button Presence (P10 exhaustiveness)

Each card or item must expose an `(i)` info affordance that explains the term, shows the source, and surfaces the underlying CNM card (R2). Without it, the component is "superficial" — a direct P10 violation.

### D3 — VVV Visibility (Source + Decay)

Every datum with a VVV score must show: numeric VVV bar, `vvv_decay` (if applicable), `vvv_source` link or file:line, and `vvv_updated` timestamp. Anchored in VVV.md and MEEST-AE v2.0 R1 (decay temporal λ=0.30).

### D4 — Sub-Engine Awareness (Per-audience)

The component must respect the active audience selection (5 personas) when computing or displaying scores. If the component is global-only, it must declare so explicitly via a "global view" badge. Anchored in MEEST-AE v2.1 R3.

### D5 — Mobile / Accessibility

Component must render correctly at ≤375px width, support keyboard navigation (Tab/Enter/Esc on interactive elements), respect `prefers-reduced-motion`, and pass minimum WCAG AA contrast on all text. Anchored in standard A11y baseline + project rule "Mobile responsive" (STEP 2.7 row "Todos").

---

## 3. Per-Component Scoring Matrix

Target ≥95% per cell; component pass ≥95% mean across the 5 dimensions. Scores below reflect the **post-Wave-3 baseline** captured during the W3 review (info button rollout). Components are listed in the order specified by the deliverable.

| Component             | D1 Scoring | D2 Info Btn | D3 VVV | D4 Sub-Engine | D5 Mobile/A11y | Mean   | Status |
|-----------------------|-----------:|------------:|-------:|--------------:|---------------:|-------:|--------|
| ArtOfWar.vue          |       95%  |        95%  |   90%  |          95%  |           90%  |  93%   | ITER-1 |
| FdcuInteractive.vue   |       95%  |        95%  |   85%  |          80%  |           90%  |  89%   | ITER-1 |
| ScenarioSimulator.vue |       95%  |        90%  |   75%  |          85%  |           90%  |  87%   | ITER-1 |
| SwotAnalysis.vue      |       90%  |        95%  |   85%  |          70%  |           90%  |  86%   | ITER-1 |
| MacroAnalysis.vue     |       80%  |        90%  |   80%  |          70%  |           90%  |  82%   | ITER-2 |
| StakeholderMap.vue    |       75%  |        85%  |   80%  |          70%  |           90%  |  80%   | ITER-2 |
| CompetitiveView.vue   |       85%  |        90%  |   80%  |          75%  |           90%  |  84%   | ITER-2 |
| Dashboard5s.vue       |       90%  |        90%  |   80%  |          80%  |           95%  |  87%   | ITER-1 |
| StatusPage.vue        |       95%  |        85%  |   90%  |          70%  |           95%  |  87%   | ITER-1 |
| RoadmapViewer.vue     |       80%  |        85%  |   75%  |          70%  |           90%  |  80%   | ITER-2 |

Status legend: **GOLD** (≥95%) · **ITER-1** (90–94%, one focused refactor away) · **ITER-2** (80–89%, two focused refactors away) · **ITER-3** (<80%, structural work needed).

---

## 4. How to Measure Each Dimension (PASS criteria)

### D1 — Scoring Dynamism

PASS = changing any slider, override, or audience triggers a Vue reactivity update visible within 1 frame, and no score is read from a literal in the template. Verification: grep for hardcoded numeric scores in the SFC; toggle a slider and confirm a `computed` re-runs.

### D2 — Info Button Presence

PASS = every card-level element renders an `(i)` button that, on click, expands a panel with `description + dimensao + vvv + vvv_source + vvv_updated`. Verification: visual inspection plus DOM count of `[data-info-button]` matches card count.

### D3 — VVV Visibility

PASS = each scored item shows a VVV bar, the decayed value when `vvv_updated` is older than 30 days, and a clickable source. Verification: render a fixture with `vvv_updated = 6 months ago` and confirm the displayed value is lower than `vvv` and the source link resolves.

### D4 — Sub-Engine Awareness

PASS = component reads the active audience from the global toggle and recomputes its own derived values, OR displays a "global view only" badge. Verification: switch audiences and confirm at least one numeric value or filter changes (or the badge is present).

### D5 — Mobile / Accessibility

PASS = component is usable at 375px width with no horizontal scroll, all interactive elements reachable via keyboard, and contrast ratios ≥4.5:1 on body text. Verification: Chrome DevTools device toolbar + Lighthouse a11y score ≥95 + manual Tab traversal.

---

## 5. Iteration Protocol (P1, P3, P6)

When a component scores below 95% on the matrix:

1. **Identify deficit** — record the lowest-scoring dimension and the gap-to-gold (95 − current). This becomes the iteration target.
2. **Refactor** — apply one of the four HIQM refinement strategies from the source spec: `DEEPENING` (add detail), `CORRECTION` (fix defects), `EXPANSION` (add missing dimension coverage), or `OPTIMIZATION` (improve clarity).
3. **Re-measure** — re-score the same dimension using the PASS criteria in section 4. Log the delta in the WAL (`.claude/wal/shuntzu-operations.log`).
4. **Convergence check (P3)** — if the new score is not strictly greater than the previous score, do not increment the iteration counter; escalate the strategy (e.g., `CORRECTION` → `EXPANSION`).
5. **Cap** — maximum 3 attempts per dimension per session. If the third attempt does not converge, mark the component `BLOCKED` and surface a constitutional impossibility note for human review (P6 forbids silent acceptance below 95%).
6. **Certificate** — once mean ≥95% AND every dimension ≥95%, emit a Gold Standard Certificate entry in `memory/shuntzu-engine-state.md` with iteration count and CoT references (P9).

Non-negotiable: the component is **not** considered shippable until the certificate is emitted, regardless of deadline pressure (P6, P8).

---

## 6. Current Baseline (Post-Wave-3 Review Audit)

Captured 2026-05-09 after Wave 3 (info button rollout) and before iteration cycle:

- **Info button coverage before W3 fix:** 5 of 10 components had an `(i)` affordance (ArtOfWar, FdcuInteractive, ScenarioSimulator partial, SwotAnalysis, Dashboard5s). The W3 commit `5ac9f73` extended it to all 10, lifting D2 across the matrix.
- **Score distribution:** most components fall in the **80–95%** band — none currently certified GOLD; none in ITER-3.
- **Strongest dimension across the suite:** D1 Scoring Dynamism (mean 88%) — the engine-driven design pays off here.
- **Weakest dimension across the suite:** D4 Sub-Engine Awareness (mean 76%) — only ArtOfWar and FdcuInteractive consume the per-audience toggle; the rest are global-only and most do not display the "global view" badge.
- **Second weakest:** D3 VVV Visibility (mean 82%) — `vvv_decay` is implemented in JSON but not consistently rendered; sources are shown as text rather than file:line links in StakeholderMap, RoadmapViewer, and ScenarioSimulator.
- **Components closest to GOLD:** ArtOfWar (93%), FdcuInteractive (89%), Dashboard5s (87%), ScenarioSimulator (87%), StatusPage (87%).
- **Components needing two iteration cycles:** MacroAnalysis, StakeholderMap, CompetitiveView, RoadmapViewer (all 80–84%).

Next planned iteration target (highest priority by gap × component impact): **D4 across MacroAnalysis, StakeholderMap, RoadmapViewer** — add the per-audience toggle hookup or the explicit "global view" badge. Expected lift: +10 to +15 points on D4, pushing those three components into ITER-1 band.

---

**Constitutional reminder (P8):** This rubric is sovereign. A component that does not certify GOLD must not be advertised as production-ready in the deployed app, regardless of build status or deploy pipeline state.
