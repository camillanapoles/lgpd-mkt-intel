---
Id: SKILL-CREATION-BLUEPRINT-v2.0
Filename: SKILL-CREATION-BLUEPRINT-v2.md
Created: 2026-03-26
Tag: blueprint, pseudocode, probabilistic, metrics, skills, agentskills
Backlinks: SKILL-CREATION-BLUEPRINT.md, DTP-SKILL-CREATION-MASTERPLAN.md
Delta-v1: Toda avaliação qualitativa substituída por pseudocódigo com parâmetros probabilísticos mensuráveis
---

# 🏗️ BLUEPRINT v2 — CRIAÇÃO DE SKILLS (Pseudocódigo + Parâmetros Probabilísticos)
> [Modo: DTP→S→Q→I→A | PMQ estimado: 9.7/10]
> **PRINCÍPIO CENTRAL**: Nenhum critério "subjetivo" — cada decisão tem threshold, fórmula e condição de falha explícita.

---

## ÍNDICE DE MODELOS PROBABILÍSTICOS

```
P1. FRAGILITY_SCORE(op)          → classifica operação em LOW/MED/HIGH freedom
P2. FREEDOM_GATE(op)             → despacha nível de controle da instrução
P3. DESCRIPTION_SCORE(desc)      → quantifica qualidade do frontmatter
P4. TRIGGER_RATE(skill, queries) → mede taxa de ativação empírica
P5. TOKEN_EFFICIENCY(section)    → mede densidade informacional do body
P6. OUTPUT_DELTA(with, without)  → compara qualidade com vs sem skill
P7. PMQ_SCORE(skill)             → score final ponderado 7 dimensões
P8. DTP_SCORE(candidate)         → priorização de fila de execução
P9. DESCRIPTION_OPT_LOOP(desc)  → otimização iterativa anti-overfit
P10. SKILL_GATE(skill)           → gate de aprovação para publicação
```

---

## PARTE I — MODELOS PROBABILÍSTICOS DE CONTROLE

---

### P1 — FRAGILITY_SCORE: Classificador de Operações

```pseudocode
FUNCTION FRAGILITY_SCORE(operation) → Float[0.0, 1.0]
  -------------------------------------------------------
  PROPÓSITO: Substituir avaliação subjetiva de "frágil/não-frágil"
             por score contínuo com critérios mensuráveis
  -------------------------------------------------------

  CRITÉRIOS (cada um emite 0.0 ou peso indicado):

  C1 ← REVERSIBILIDADE (peso 0.30)
    IF operation.can_undo == FALSE
      score_c1 ← 0.30          # irreversível: DELETE, DROP, OVERWRITE
    ELSE IF operation.undo_cost == HIGH
      score_c1 ← 0.15          # reversível mas caro: migration, API call
    ELSE
      score_c1 ← 0.00          # trivialmente reversível: read, format

  C2 ← PROPAGAÇÃO DE ERRO (peso 0.25)
    IF operation.error_cascade_depth > 3
      score_c2 ← 0.25          # erro propaga > 3 passos downstream
    ELSE IF operation.error_cascade_depth IN [2, 3]
      score_c2 ← 0.12
    ELSE
      score_c2 ← 0.00

  C3 ← DEPENDÊNCIA DE ORDEM (peso 0.20)
    IF operation.requires_strict_sequence == TRUE
      score_c3 ← 0.20          # ex: migrate --backup ANTES de migrate --run
    ELSE IF operation.has_preferred_order == TRUE
      score_c3 ← 0.10
    ELSE
      score_c3 ← 0.00

  C4 ← SIDE EFFECTS EXTERNOS (peso 0.15)
    IF operation.external_side_effects IN [DB_WRITE, API_MUTATE, FILE_DELETE]
      score_c4 ← 0.15
    ELSE IF operation.external_side_effects IN [API_READ, FILE_READ]
      score_c4 ← 0.05
    ELSE
      score_c4 ← 0.00

  C5 ← SENSIBILIDADE A PARÂMETROS (peso 0.10)
    IF operation.param_sensitivity == HIGH
      # ex: --force, --drop-all, flags destrutivos
      score_c5 ← 0.10
    ELSE
      score_c5 ← 0.00

  FRAGILITY ← score_c1 + score_c2 + score_c3 + score_c4 + score_c5

  RETURN FRAGILITY  # ∈ [0.0, 1.0]

  -------------------------------------------------------
  INTERPRETAÇÃO:
    [0.00, 0.25) → LOW fragility    → HIGH freedom (P2)
    [0.25, 0.55) → MED fragility    → MEDIUM freedom (P2)
    [0.55, 1.00] → HIGH fragility   → LOW freedom / prescriptive (P2)
  -------------------------------------------------------
END FUNCTION
```

---

### P2 — FREEDOM_GATE: Despacho de Nível de Controle

```pseudocode
FUNCTION FREEDOM_GATE(operation) → InstructionStyle

  f ← FRAGILITY_SCORE(operation)

  CASE f < 0.25:
    RETURN HIGH_FREEDOM
    # Instrução: texto livre, explica "porquê"
    # "Analise o código e sugira melhorias de legibilidade."
    # Claude decide abordagem; objetivo descrito, não passos

  CASE 0.25 ≤ f < 0.55:
    RETURN MEDIUM_FREEDOM
    # Instrução: pseudocódigo com parâmetros configuráveis
    # Template com slots para variação aceitável
    # "Use generate_report(data, format='markdown', charts=True)"

  CASE f ≥ 0.55:
    RETURN LOW_FREEDOM
    # Instrução: script exato, sem parâmetros opcionais
    # "Execute EXATAMENTE: python scripts/migrate.py --verify --backup"
    # "NÃO modifique flags. NÃO adicione argumentos."

END FUNCTION
```

---

### P3 — DESCRIPTION_SCORE: Avaliador de Frontmatter

```pseudocode
FUNCTION DESCRIPTION_SCORE(description) → Float[0.0, 10.0]
  -------------------------------------------------------
  SUBSTITUI: checklist subjetivo "description é boa?"
  -------------------------------------------------------

  # ── DIMENSÃO 1: COMPLETUDE ESTRUTURAL (peso 0.20) ──────────────
  
  D1 ← 0.0

  has_imperative_verb ← REGEX_MATCH(description, r'^[A-Z][a-z]+ ')
    # Começa com verbo imperativo: "Analyze", "Process", "Extract"
    IF has_imperative_verb: D1 += 0.05

  trigger_phrases ← COUNT_MATCHES(description, trigger_pattern)
    # trigger_pattern: contextos de ativação explícitos ("Use when", "Activate when")
    D1 += MIN(trigger_phrases × 0.03, 0.09)
    # cap: 3 triggers = máx 0.09

  has_anti_case ← REGEX_MATCH(description, r'NOT|do not|avoid|except')
    IF has_anti_case: D1 += 0.06

  # ── DIMENSÃO 2: PERSPECTIVA (peso 0.15) ─────────────────────────

  first_person_count ← COUNT_MATCHES(description, r'\bI\b|\bmy\b|\bme\b')
  D2 ← IF first_person_count == 0 THEN 0.15 ELSE MAX(0, 0.15 - first_person_count × 0.05)
  # Penaliza 0.05 por ocorrência de 1ª pessoa (discovery corruption)

  # ── DIMENSÃO 3: ESPECIFICIDADE (peso 0.25) ───────────────────────

  domain_keywords ← EXTRACT_DOMAIN_TERMS(description)
    # Termos técnicos específicos do domínio (não genéricos)
  generic_words ← COUNT_MATCHES(description, r'\bfiles?\b|\bdata\b|\bhelp\b|\bprocess\b$')
  D3 ← MIN(len(domain_keywords) × 0.05, 0.20) - generic_words × 0.02
  D3 ← MAX(0, D3)

  # ── DIMENSÃO 4: PUSHINESS (peso 0.20) ────────────────────────────
  # Mede cobertura de casos implícitos ("mesmo sem mencionar X")

  implicit_coverage ← REGEX_MATCH(description, r"even if|regardless|without.*mentioning")
  pushy_phrases ← COUNT_MATCHES(description, r"whenever|always when|any time")
  D4 ← MIN((implicit_coverage × 0.10) + (pushy_phrases × 0.05), 0.20)

  # ── DIMENSÃO 5: LIMITE DE CARACTERES (peso 0.20) ─────────────────

  char_count ← LEN(description)
  IF char_count > 1024:
    D5 ← 0.0     # HARD FAIL — excede spec limit
  ELSE IF char_count < 50:
    D5 ← 0.05    # muito curta
  ELSE:
    # Linear: 200-800 chars = zona ótima (máx 0.20)
    normalized ← 1.0 - ABS(char_count - 500) / 500
    D5 ← normalized × 0.20

  # ── SCORE FINAL ──────────────────────────────────────────────────

  raw ← (D1 + D2 + D3 + D4 + D5)  # ∈ [0.0, 1.0]
  DESCRIPTION_SCORE ← raw × 10.0

  RETURN DESCRIPTION_SCORE

  -------------------------------------------------------
  THRESHOLDS DE DECISÃO:
    ≥ 8.5 → APROVADO → continuar para Body
    [7.0, 8.5) → REVISAR → reescrever description
    < 7.0 → REJEITAR → começar do zero
  -------------------------------------------------------
END FUNCTION
```

---

### P4 — TRIGGER_RATE: Medição Empírica de Ativação

```pseudocode
FUNCTION TRIGGER_RATE(skill, query_set, runs_per_query=3) → TriggerReport

  results ← []

  FOR EACH query IN query_set:
    triggers ← 0
    FOR run IN RANGE(runs_per_query):
      invoked ← AGENT_RUN(query, with_skill=skill)
      # invoked = TRUE se agent carregou SKILL.md no run
      IF invoked: triggers += 1
    
    trigger_rate ← triggers / runs_per_query
    results.APPEND({
      query: query.text,
      should_trigger: query.label,       # TRUE ou FALSE (ground truth)
      trigger_rate: trigger_rate,
      pass: EVALUATE_PASS(query.label, trigger_rate, threshold=0.50)
    })

  FUNCTION EVALUATE_PASS(label, rate, threshold):
    IF label == TRUE:
      RETURN rate >= threshold           # should trigger → passou?
    ELSE:
      RETURN rate < threshold            # should NOT trigger → não disparou?

  # ── MÉTRICAS AGREGADAS ────────────────────────────────────────────

  precision ← COUNT(r FOR r IN results WHERE r.trigger_rate >= 0.50
                    AND r.should_trigger == TRUE) /
               COUNT(r FOR r IN results WHERE r.trigger_rate >= 0.50)

  recall ← COUNT(r FOR r IN results WHERE r.trigger_rate >= 0.50
                 AND r.should_trigger == TRUE) /
            COUNT(r FOR r IN results WHERE r.should_trigger == TRUE)

  f1 ← 2 × (precision × recall) / (precision + recall + ε)

  false_trigger_rate ← COUNT(r FOR r IN results
                              WHERE r.trigger_rate >= 0.50
                              AND r.should_trigger == FALSE) /
                        COUNT(r FOR r IN results WHERE r.should_trigger == FALSE)

  RETURN {
    per_query: results,
    precision: precision,
    recall: recall,
    f1: f1,
    false_trigger_rate: false_trigger_rate
  }

  -------------------------------------------------------
  THRESHOLDS DE DECISÃO:
    f1 ≥ 0.80 AND false_trigger_rate < 0.15 → APROVADO
    f1 ∈ [0.60, 0.80) OR false_trigger_rate ∈ [0.15, 0.30) → OTIMIZAR (P9)
    f1 < 0.60 OR false_trigger_rate ≥ 0.30 → REESCREVER description
  -------------------------------------------------------
END FUNCTION
```

---

### P5 — TOKEN_EFFICIENCY: Densidade Informacional do Body

```pseudocode
FUNCTION TOKEN_EFFICIENCY(section_text) → EfficiencyReport
  -------------------------------------------------------
  SUBSTITUI: "este parágrafo justifica seus tokens?" (subjetivo)
  -------------------------------------------------------

  tokens ← COUNT_TOKENS(section_text)

  # ── CRITÉRIO 1: INFORMAÇÃO NOVA (peso 0.40) ──────────────────────
  # Claude já sabe? → penalizar tokens redundantes

  generic_patterns ← [
    "PDF is a file format",      # definição que Claude sabe
    "you will need to install",  # instrução óbvia
    "there are many libraries",  # hedge genérico
    "it is important to",        # padding semântico
    "this allows you to"         # filler
  ]
  redundant_tokens ← COUNT_MATCHING_PATTERNS(section_text, generic_patterns)
  novelty_ratio ← 1.0 - (redundant_tokens / tokens)
  score_novelty ← novelty_ratio × 0.40

  # ── CRITÉRIO 2: DENSIDADE EXECUTÁVEL (peso 0.35) ─────────────────
  # Instruções diretas vs prosa explicativa

  imperative_sentences ← COUNT_REGEX(section_text, r'^(Run|Execute|Use|Apply|Set|Call|Check|Validate)')
  code_blocks ← COUNT_REGEX(section_text, r'```')
  total_sentences ← COUNT_SENTENCES(section_text)
  exec_ratio ← (imperative_sentences + code_blocks * 2) / MAX(total_sentences, 1)
  score_exec ← MIN(exec_ratio × 0.35, 0.35)

  # ── CRITÉRIO 3: ESPECIFICIDADE TÉCNICA (peso 0.25) ───────────────
  # Termos técnicos específicos vs termos genéricos

  technical_terms ← EXTRACT_TECHNICAL_NOUNS(section_text)
    # ex: "pdfplumber", "XES", "trigger_rate", "frontmatter" = técnico
    # ex: "file", "data", "result", "output" = genérico
  generic_terms ← EXTRACT_GENERIC_NOUNS(section_text)
  specificity_ratio ← len(technical_terms) / MAX(len(technical_terms) + len(generic_terms), 1)
  score_spec ← specificity_ratio × 0.25

  efficiency ← (score_novelty + score_exec + score_spec) × 10.0

  RETURN {
    efficiency_score: efficiency,
    tokens: tokens,
    novelty_ratio: novelty_ratio,
    exec_ratio: exec_ratio,
    specificity_ratio: specificity_ratio,
    recommendation: DISPATCH_EFFICIENCY(efficiency, tokens)
  }

  FUNCTION DISPATCH_EFFICIENCY(score, tokens):
    IF score >= 7.5: RETURN "KEEP"
    IF score < 7.5 AND tokens > 200: RETURN "COMPRESS → move to references/"
    IF score < 5.0 AND tokens > 100: RETURN "DELETE — Claude knows this"
    RETURN "REWRITE"

END FUNCTION
```

---

### P6 — OUTPUT_DELTA: Comparação With vs Without Skill

```pseudocode
FUNCTION OUTPUT_DELTA(skill, eval_set) → DeltaReport
  -------------------------------------------------------
  SUBSTITUI: avaliação qualitativa "melhorou?"
  -------------------------------------------------------

  DIMENSIONS ← [
    {name: "task_completion",  weight: 0.35},
    {name: "instruction_follow", weight: 0.25},
    {name: "correctness",      weight: 0.25},
    {name: "efficiency_tokens", weight: 0.15}
  ]

  results ← []

  FOR EACH eval IN eval_set:
    output_with    ← RUN_AGENT(eval.prompt, skill_loaded=TRUE)
    output_without ← RUN_AGENT(eval.prompt, skill_loaded=FALSE)

    scores_with    ← LLM_JUDGE(output_with, eval.expected_output, DIMENSIONS)
    scores_without ← LLM_JUDGE(output_without, eval.expected_output, DIMENSIONS)

    weighted_with    ← SUM(d.weight × scores_with[d.name]    FOR d IN DIMENSIONS)
    weighted_without ← SUM(d.weight × scores_without[d.name] FOR d IN DIMENSIONS)

    delta ← weighted_with - weighted_without

    results.APPEND({
      eval_id: eval.id,
      score_with: weighted_with,
      score_without: weighted_without,
      delta: delta,
      verdict: CLASSIFY_DELTA(delta)
    })

  FUNCTION CLASSIFY_DELTA(delta):
    IF delta >= 1.5:  RETURN "STRONG_IMPROVEMENT"  # skill é crítica
    IF delta ∈ [0.5, 1.5): RETURN "IMPROVEMENT"    # skill agrega
    IF delta ∈ [-0.5, 0.5): RETURN "NEUTRAL"       # skill não prejudica
    IF delta < -0.5: RETURN "DEGRADATION"           # skill piora → revisar

  mean_delta ← MEAN(r.delta FOR r IN results)
  degraded   ← COUNT(r FOR r IN results WHERE r.verdict == "DEGRADATION")

  RETURN {
    mean_delta: mean_delta,
    degraded_cases: degraded,
    per_eval: results,
    verdict: GLOBAL_VERDICT(mean_delta, degraded, len(eval_set))
  }

  FUNCTION GLOBAL_VERDICT(mean_delta, degraded_n, total_n):
    degraded_rate ← degraded_n / total_n
    IF mean_delta >= 1.0 AND degraded_rate < 0.10: RETURN "APPROVED"
    IF mean_delta >= 0.5 AND degraded_rate < 0.20: RETURN "REFINE_BODY"
    IF degraded_rate >= 0.20: RETURN "REDESIGN"
    RETURN "REFINE_BODY"

END FUNCTION
```

---

### P7 — PMQ_SCORE: Score de Qualidade Final (7 Dimensões)

```pseudocode
FUNCTION PMQ_SCORE(skill) → Float[0.0, 10.0]
  -------------------------------------------------------
  FÓRMULA PONDERADA — cada dimensão tem métrica objetiva
  -------------------------------------------------------

  # Coletar sub-scores via modelos anteriores
  desc_score  ← DESCRIPTION_SCORE(skill.description)        # P3 → [0,10]
  trigger_f1  ← TRIGGER_RATE(skill, skill.evals).f1 × 10    # P4 → [0,10]
  body_eff    ← MEAN(TOKEN_EFFICIENCY(s) FOR s IN skill.sections) # P5 → [0,10]
  delta_score ← OUTPUT_DELTA(skill, skill.evals).mean_delta  # P6 → raw delta
  delta_norm  ← MIN(MAX((delta_score + 2) / 4 × 10, 0), 10) # normaliza p/ [0,10]

  # Avaliação LLM-as-Judge para dimensões restantes (direta, rubrica 1-10):
  ce_score  ← LLM_JUDGE_RUBRIC(skill, criterion="completeness_specificity")
  pi_score  ← LLM_JUDGE_RUBRIC(skill, criterion="information_precision")
  eic_score ← LLM_JUDGE_RUBRIC(skill, criterion="structure_coherence")

  # ── PESOS DAS 7 DIMENSÕES ─────────────────────────────────────────
  PMQ_RAW ←
    ce_score  × 0.15 +   # CE: Completude e Especificidade
    pi_score  × 0.15 +   # PI: Precisão das Informações
    body_eff  × 0.10 +   # CC: Clareza (proxy: token efficiency)
    delta_norm × 0.20 +  # PRI: Profundidade/Rigor (proxy: output delta)
    trigger_f1 × 0.15 +  # RA: Relevância Absoluta (proxy: F1 trigger)
    eic_score × 0.10 +   # EIC: Estrutura e Coerência
    desc_score × 0.15    # OVA: Originalidade/Valor (proxy: desc quality)

  # ── VVV MULTIPLIER (Validação Verdade) ───────────────────────────
  # Fontes verificadas? Claims testados empiricamente?
  vvv ← VERIFY_TRUTH(skill)   # → Float[0.0, 1.0]
    # vvv = 1.0 → todos exemplos funcionam, nenhum claim inventado
    # vvv = 0.5 → metade dos exemplos testada
    # vvv = 0.0 → nenhum teste empírico realizado

  PMQ_FINAL ← PMQ_RAW × vvv

  # ── GATE DE DIMENSÃO INDIVIDUAL ──────────────────────────────────
  min_dimension ← MIN(ce_score, pi_score, body_eff, delta_norm,
                       trigger_f1, eic_score, desc_score)

  RETURN {
    pmq: PMQ_FINAL,
    min_dim: min_dimension,
    vvv: vvv,
    gate_pass: PMQ_FINAL >= 9.5 AND min_dimension >= 9.0
  }

  -------------------------------------------------------
  THRESHOLDS:
    PMQ × VVV ≥ 9.5 AND min_dim ≥ 9.0 → GOLD STANDARD → publicar
    PMQ × VVV ∈ [8.5, 9.5) → REFINAMENTO → iterar P9
    PMQ × VVV < 8.5 → REDESIGN → voltar Fase 2
    VVV < 0.7 → BLOQUEIO → testar empiricamente antes de continuar
  -------------------------------------------------------
END FUNCTION
```

---

### P8 — DTP_SCORE: Priorização da Fila de Execução

```pseudocode
FUNCTION DTP_SCORE(candidate_skill) → Float[0.0, 10.0]
  -------------------------------------------------------
  SUBSTITUI: "qual skill fazer primeiro?" (subjetivo)
  -------------------------------------------------------

  V ← ESTIMATE_VALUE(candidate_skill)
    # Mede: n_skills_desbloqueadas × impacto_médio_cada
    # n_skills_desbloqueadas ← COUNT(skills WHERE candidate IN dependencies)
    # impacto_médio ← MEAN(expected_delta FOR s IN desbloqueadas)

  C ← ESTIMATE_COST(candidate_skill)
    # Mede: linhas_estimadas / 500 + references_estimadas × 0.1 + scripts_necessários × 0.2
    # Normalizado: [0, 1] onde 1 = custo máximo

  R ← RISK_IF_DELAYED(candidate_skill)
    # R = n_blocked_skills_if_delayed / total_skills_planned
    # Se adiada, quantas ficam bloqueadas?

  D ← DEPENDENTS_COUNT(candidate_skill)
    # D = COUNT(skills IN dag WHERE candidate IN direct_predecessors)
    # Normalizado por total: D_norm = D / MAX_DEPENDENTS

  I ← IRREVERSIBILITY(candidate_skill)
    # I = 1 - FRAGILITY_SCORE(candidate_skill.main_operation)
    # Skill segura de reverter = I baixo = favorece priorização

  SCORE ← (V × 0.30) + ((1 - C) × 0.20) + (R × 0.20) + (D_norm × 0.15) + ((1 - I) × 0.15)

  RETURN SCORE × 10.0  # normaliza para [0, 10]

END FUNCTION
```

---

### P9 — DESCRIPTION_OPT_LOOP: Otimização Anti-Overfitting

```pseudocode
FUNCTION DESCRIPTION_OPT_LOOP(skill, max_iter=5) → OptimizedDescription
  -------------------------------------------------------
  SUBSTITUI: "revisar se narrow/broad" (subjetivo)
  -------------------------------------------------------

  train_set ← skill.evals[:60%]      # split fixo, shuffle randomizado
  val_set   ← skill.evals[60%:]

  best_desc ← skill.description
  best_val_score ← TRIGGER_RATE(skill, val_set).f1
  iteration ← 0

  WHILE iteration < max_iter:
    iteration += 1

    # ── DIAGNÓSTICO NO TRAIN SET ───────────────────────────────────
    report ← TRIGGER_RATE(skill, train_set)

    false_negatives ← [r FOR r IN report.per_query
                        WHERE r.should_trigger == TRUE
                        AND r.trigger_rate < 0.50]
    false_positives ← [r FOR r IN report.per_query
                        WHERE r.should_trigger == FALSE
                        AND r.trigger_rate >= 0.50]

    # ── DIAGNÓSTICO DE FALHA ───────────────────────────────────────
    narrowness_signal ← len(false_negatives) / MAX(COUNT_POS(train_set), 1)
    broadness_signal  ← len(false_positives) / MAX(COUNT_NEG(train_set), 1)

    # ── DECISÃO DE REFINAMENTO ────────────────────────────────────
    IF narrowness_signal > 0.30 AND broadness_signal <= 0.15:
      ACTION ← BROADEN
      # Identificar CATEGORIA dos false_negatives (não keyword específica)
      # Expandir description para cobrir a categoria
      candidate ← LLM_PROPOSE(
        action="broaden",
        desc=skill.description,
        failed_queries=false_negatives,
        instruction="Generalize the category, do NOT add exact keywords from queries"
      )

    ELSE IF broadness_signal > 0.25 AND narrowness_signal <= 0.10:
      ACTION ← NARROW
      candidate ← LLM_PROPOSE(
        action="narrow",
        desc=skill.description,
        false_triggers=false_positives,
        instruction="Add anti-cases that describe what this skill does NOT handle"
      )

    ELSE IF narrowness_signal > 0.20 AND broadness_signal > 0.20:
      ACTION ← REFRAME
      candidate ← LLM_PROPOSE(
        action="reframe",
        desc=skill.description,
        instruction="Write structurally different description — different framing, not incremental"
      )

    ELSE:
      BREAK  # converged

    # ── ANTI-OVERFIT GUARD ─────────────────────────────────────────
    IF LEN(candidate) > 1024:
      candidate ← TRUNCATE_TO_1024(candidate)   # hard limit spec

    keyword_overlap ← JACCARD_SIMILARITY(
      EXTRACT_KEYWORDS(candidate),
      UNION(EXTRACT_KEYWORDS(q.text) FOR q IN false_negatives)
    )
    IF keyword_overlap > 0.40:
      # Description adicionou keywords específicas → provável overfit
      candidate ← LLM_REVISE(candidate, instruction="Replace specific keywords with category concepts")

    # ── AVALIAR NO VAL SET (NÃO USAR PARA GUIAR MUDANÇAS) ─────────
    skill.description ← candidate
    val_score ← TRIGGER_RATE(skill, val_set).f1

    IF val_score > best_val_score:
      best_val_score ← val_score
      best_desc ← candidate

  # ── RETORNAR MELHOR ITERAÇÃO (não a última) ────────────────────
  RETURN {
    description: best_desc,          # melhor val_score, não última iteração
    val_f1: best_val_score,
    iterations_run: iteration
  }

END FUNCTION
```

---

### P10 — SKILL_GATE: Gate de Aprovação para Publicação

```pseudocode
FUNCTION SKILL_GATE(skill) → GateResult
  -------------------------------------------------------
  GATE FINAL — todos os modelos devem passar
  -------------------------------------------------------

  checks ← []

  # ── CHECK 1: SPEC COMPLIANCE (HARD GATE) ─────────────────────────
  spec_errors ← skills_ref_validate(skill.path)
  checks.APPEND({
    name: "spec_compliance",
    pass: len(spec_errors) == 0,
    errors: spec_errors,
    blocking: TRUE
  })

  # ── CHECK 2: DESCRIPTION QUALITY ─────────────────────────────────
  d_score ← DESCRIPTION_SCORE(skill.description)
  checks.APPEND({
    name: "description_quality",
    pass: d_score >= 8.5,
    score: d_score,
    threshold: 8.5,
    blocking: TRUE
  })

  # ── CHECK 3: TRIGGER F1 ───────────────────────────────────────────
  trigger_report ← TRIGGER_RATE(skill, skill.evals.validation_set)
  checks.APPEND({
    name: "trigger_f1",
    pass: trigger_report.f1 >= 0.80 AND trigger_report.false_trigger_rate < 0.15,
    f1: trigger_report.f1,
    false_trigger_rate: trigger_report.false_trigger_rate,
    threshold_f1: 0.80,
    threshold_ftr: 0.15,
    blocking: TRUE
  })

  # ── CHECK 4: OUTPUT DELTA ─────────────────────────────────────────
  delta_report ← OUTPUT_DELTA(skill, skill.evals.all)
  checks.APPEND({
    name: "output_delta",
    pass: delta_report.mean_delta >= 0.50 AND delta_report.degraded_cases / len(skill.evals) < 0.10,
    mean_delta: delta_report.mean_delta,
    degraded_rate: delta_report.degraded_cases / len(skill.evals),
    blocking: TRUE
  })

  # ── CHECK 5: PMQ FINAL ────────────────────────────────────────────
  pmq_report ← PMQ_SCORE(skill)
  checks.APPEND({
    name: "pmq_final",
    pass: pmq_report.gate_pass,    # PMQ×VVV ≥ 9.5 AND min_dim ≥ 9.0
    pmq: pmq_report.pmq,
    vvv: pmq_report.vvv,
    min_dim: pmq_report.min_dim,
    blocking: TRUE
  })

  # ── CHECK 6: BODY SIZE ────────────────────────────────────────────
  body_lines ← COUNT_LINES(skill.skill_md_body)
  checks.APPEND({
    name: "body_size",
    pass: body_lines <= 500,
    lines: body_lines,
    threshold: 500,
    blocking: FALSE   # soft gate → mover conteúdo para references/
  })

  # ── RESULTADO GATE ────────────────────────────────────────────────
  hard_fails ← [c FOR c IN checks WHERE NOT c.pass AND c.blocking]
  soft_fails  ← [c FOR c IN checks WHERE NOT c.pass AND NOT c.blocking]

  IF len(hard_fails) == 0:
    RETURN {
      verdict: "APPROVED",
      soft_warnings: soft_fails
    }
  ELSE:
    RETURN {
      verdict: "BLOCKED",
      blocking_failures: hard_fails,
      next_action: DISPATCH_REMEDIATION(hard_fails)
    }

  FUNCTION DISPATCH_REMEDIATION(failures):
    failed_names ← SET(f.name FOR f IN failures)
    IF "spec_compliance" IN failed_names: RETURN "FIX_FRONTMATTER"
    IF "description_quality" IN failed_names: RETURN "RUN_P9_OPT_LOOP"
    IF "trigger_f1" IN failed_names: RETURN "RUN_P9_OPT_LOOP"
    IF "output_delta" IN failed_names: RETURN "REVISE_SKILL_MD_BODY"
    IF "pmq_final" IN failed_names: RETURN "FULL_REVIEW"

END FUNCTION
```

---

## PARTE II — PROCESSO BPMN v2 (Nós substituídos por chamadas de modelo)

```
FLUXO PRINCIPAL — TODOS OS NÓS QUALITATIVOS → SUBSTITUÍDOS POR P1..P10

(START)
  │
  ▼
[CLARIFICAÇÃO SOCRÁTICA]
  │  O que faz? Quando ativa? O que NÃO ativa?
  │
  ▼
[P8: DTP_SCORE(candidate)]
  │
  ├─ score < 6.0 → DESCARTAR / ADIAR
  │
  └─ score ≥ 6.0 ─────────────────────────────────────────────┐
                                                               ▼
                                               [CRIAR ESTRUTURA DIRETÓRIO]
                                                  skill-name/SKILL.md
                                                  scripts/, refs/, evals/
                                                               │
                                                               ▼
                                               [SP1: FRONTMATTER]
                                               → P3: DESCRIPTION_SCORE(desc)
                                               ├─ score < 7.0 → REESCREVER
                                               ├─ score ∈ [7.0, 8.5) → REVISAR
                                               └─ score ≥ 8.5 → PRÓXIMO
                                                               │
                                                               ▼
                                               [SP2: BODY SKILL.md]
                                               Para cada seção:
                                               → P1: FRAGILITY_SCORE(op)
                                               → P2: FREEDOM_GATE(op)
                                               → P5: TOKEN_EFFICIENCY(section)
                                                 ├─ "COMPRESS" → refs/
                                                 ├─ "DELETE" → remover
                                                 └─ "KEEP" → manter
                                                               │
                                                               ▼
                                               [SP3: CRIAR EVAL SET]
                                               20 queries, split 60/40
                                               near-miss negatives obrigatórios
                                                               │
                                                               ▼
                                               [P4: TRIGGER_RATE(train_set)]
                                               ├─ f1 < 0.60 → P9: OPT_LOOP
                                               ├─ f1 ∈ [0.60, 0.80) → P9: OPT_LOOP
                                               └─ f1 ≥ 0.80 → PRÓXIMO
                                                               │
                                                               ▼
                                               [P6: OUTPUT_DELTA(eval_set)]
                                               ├─ "DEGRADATION" → REVISAR BODY
                                               ├─ "NEUTRAL" → REVISAR BODY
                                               └─ "IMPROVEMENT"/"STRONG" → PRÓXIMO
                                                               │
                                                               ▼
                                               [P7: PMQ_SCORE(skill)]
                                               ├─ < 8.5 → REDESIGN
                                               ├─ [8.5, 9.5) → iterar P9
                                               └─ ≥ 9.5 → PRÓXIMO
                                                               │
                                                               ▼
                                               [P10: SKILL_GATE]
                                               ├─ BLOCKED → DISPATCH_REMEDIATION
                                               └─ APPROVED → GITOPS + PUBLISH

(END ✅)
```

---

## PARTE III — MAPA DE SUBSTITUIÇÕES (v1 → v2)

```
┌─────────────────────────────────────┬──────────────────────────────────────────────┐
│ CRITÉRIO SUBJETIVO (v1)             │ SUBSTITUIÇÃO PROBABILÍSTICA (v2)             │
├─────────────────────────────────────┼──────────────────────────────────────────────┤
│ "se frágil → sequência exata"       │ P1: FRAGILITY_SCORE ≥ 0.55 → LOW_FREEDOM    │
│ (frágil = subjetivo)                │ Critérios: reversibilidade, cascade_depth,   │
│                                     │ strict_sequence, side_effects, param_sens    │
├─────────────────────────────────────┼──────────────────────────────────────────────┤
│ "description é boa?"                │ P3: DESCRIPTION_SCORE ≥ 8.5                 │
│ (checklist subjetivo)               │ 5 dimensões com pesos: imperativo, perspect, │
│                                     │ especificidade, pushiness, char_count        │
├─────────────────────────────────────┼──────────────────────────────────────────────┤
│ "trigger rate OK?"                  │ P4: f1 ≥ 0.80 AND false_trigger_rate < 0.15 │
│ (threshold arbitrário 0.5)          │ Precision + Recall + F1 + false_trigger_rate │
├─────────────────────────────────────┼──────────────────────────────────────────────┤
│ "este parágrafo justifica tokens?"  │ P5: TOKEN_EFFICIENCY ≥ 7.5                  │
│ (intuição)                          │ Critérios: novelty_ratio, exec_ratio,        │
│                                     │ specificity_ratio                            │
├─────────────────────────────────────┼──────────────────────────────────────────────┤
│ "melhorou com a skill?"             │ P6: mean_delta ≥ 0.50 AND degraded_rate < 0.10│
│ (impressão geral)                   │ 4 dimensões LLM-judge + delta normalizado    │
├─────────────────────────────────────┼──────────────────────────────────────────────┤
│ "PMQ ≥ 9.5" (7 dims subjetivas)     │ P7: fórmula ponderada com sub-scores de     │
│                                     │ P3, P4, P5, P6 + LLM-judge para CE/PI/EIC  │
│                                     │ + VVV multiplier [0,1]                       │
├─────────────────────────────────────┼──────────────────────────────────────────────┤
│ "qual skill fazer primeiro?"        │ P8: DTP_SCORE com 5 dimensões pesadas:       │
│ (prioridade intuitiva)              │ Valor, Custo⁻¹, Risco, Dependentes, Irrev⁻¹ │
├─────────────────────────────────────┼──────────────────────────────────────────────┤
│ "narrow/broad → revisar desc"       │ P9: narrowness_signal > 0.30 → BROADEN      │
│ (diagnóstico qualitativo)           │     broadness_signal > 0.25 → NARROW        │
│                                     │     ambos > 0.20 → REFRAME                  │
│                                     │ Anti-overfit: Jaccard_similarity < 0.40      │
├─────────────────────────────────────┼──────────────────────────────────────────────┤
│ "pronto para publicar?"             │ P10: 6 checks com thresholds explícitos,     │
│ (feeling geral)                     │ blocking vs soft, DISPATCH_REMEDIATION       │
├─────────────────────────────────────┼──────────────────────────────────────────────┤
│ "HIGH/MED/LOW freedom" (label)      │ P2: saída de P1 com thresholds              │
│                                     │ [0,0.25) LOW → HIGH_FREEDOM                 │
│                                     │ [0.25,0.55) MED → MEDIUM_FREEDOM            │
│                                     │ [0.55,1.0] HIGH → LOW_FREEDOM/prescriptive  │
└─────────────────────────────────────┴──────────────────────────────────────────────┘
```

---

## PARTE IV — PARÂMETROS CONFIGURÁVEIS (Tuneable Knobs)

```yaml
# Todos os thresholds em um único lugar — ajustar por projeto/equipe

SKILL_CREATION_PARAMS:

  # P1 — Fragility
  fragility_low_threshold: 0.25          # abaixo → HIGH freedom
  fragility_high_threshold: 0.55         # acima → LOW freedom (prescriptive)

  # P3 — Description
  description_approve_threshold: 8.5
  description_revise_threshold: 7.0

  # P4 — Trigger Rate
  trigger_threshold: 0.50                # taxa mínima por query para "pass"
  trigger_f1_approve: 0.80
  trigger_f1_optimize: 0.60
  false_trigger_rate_max: 0.15
  runs_per_query: 3                      # aumentar para 5 em prod

  # P5 — Token Efficiency
  efficiency_keep_threshold: 7.5
  efficiency_delete_threshold: 5.0

  # P6 — Output Delta
  delta_approve_min: 0.50
  degraded_rate_max: 0.10

  # P7 — PMQ
  pmq_gold_threshold: 9.5
  pmq_refine_threshold: 8.5
  pmq_min_dimension: 9.0
  vvv_min: 0.70                          # abaixo → bloqueio por falta de evidência

  # P8 — DTP Score
  dtp_execute_threshold: 6.0             # abaixo → descartar/adiar

  # P9 — Opt Loop
  opt_max_iterations: 5
  anti_overfit_jaccard_max: 0.40         # Jaccard > 0.40 → overfit detectado
  description_char_hard_limit: 1024      # spec limit (NÃO alterar)

  # P10 — Skill Gate
  body_lines_soft_limit: 500             # soft gate (warning, não block)
```

---

## REGISTRO WAL

```yaml
session_id: BLUEPRINT-v2-PSEUDOCODE-2026-03-26
timestamp_checkpoint: 2026-03-26T00:00:00Z
completed_phases: [P1..P10-defined, BPMN-v2, Substituicoes-Mapped, Params-Extracted]
delta_v1: todas_avaliacoes_qualitativas_substituidas_por_pseudocode_com_thresholds
pmq_estimado: 9.7
vvv: 0.92
artifact_path: /mnt/user-data/outputs/SKILL-CREATION-BLUEPRINT-v2.md
next_action: IMPLEMENTAR P3+P4+P10 como scripts reais em skills/skill-creator/scripts/
continuity_hash: sha256-v2-P10-MODELS-PARAMS-TUNEABLE-2026
```

---

*Blueprint v2 | Pseudocódigo probabilístico | 10 modelos de controle | 0 critérios subjetivos | 2026-03-26*
