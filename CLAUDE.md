# Vinicio Project Guidelines

## Purpose

This document defines the working guidelines for building and evolving an interactive strategic planning presentation. The goal is to create a GitHub Pages-published experience that supports business decision-making with structured analysis, clear visual presentation, and incremental improvements.

## Expected Deliverable

Create an interactive page published on GitHub Pages (preferred stack can be Vue if that is the chosen implementation). The page should help users review and discuss strategic planning scenarios during meetings and decision processes.

The experience should cover:

- current scenario analysis,
- opportunities and barriers,
- SWOT analysis,
- strategic planning synthesis,
- business model canvas aligned with the strategic plan,
- market roadmap derived from the strategic plan and canvas.

## Working Approach

Use a coordinated multi-agent workflow with parallel execution where possible. Keep work incremental and avoid radical changes when improving existing outputs.

Maintain a single structured source of truth for shared inputs and outputs, preferably in a single JSON-based format that other agents can consume consistently.

Recommended specialist roles include:

- business analysis,
- research,
- planning,
- UX/UI,
- review,
- validation.

## Analysis Requirements

When source material includes a transcript, use it as the starting point for the analysis:

1. Capture the current scenario described in the transcript.
2. Extract likely insights and strategic signals from the transcript.
3. Produce a structured SWOT for the current scenario.
4. Translate findings into strategic, methodological, and market-oriented recommendations.

## Validation Rules

Every adjustment must have a clear methodological and strategic justification grounded in:

- market context,
- business rationale,
- benchmarking,
- stakeholder relevance.

If a change cannot be justified, it should not be approved.

All important information must be:

- verifiable,
- traceable,
- mapped to a single authoritative source.

If sources diverge, analyze which source is more reliable before proceeding.

## Contributor Rules

Before creating new documentation, verify whether equivalent documentation already exists.

Before starting any task, verify its current state:

- completed,
- in progress,
- incremental update,
- new.

## Quality Standard

Final outputs should be robust, reviewed, and validated for consistency, strategic coherence, and usability.
