# GOVERNANCE.md — LGPD Strategic Engine
## Regras Derivadas OMNIBUS v10.0 + MEEST-AE v2.1
**Versão**: 1.0  
**Data**: 2026-05-09  
**Autoridade**: CLAUDE.md mandatos + OMNIBUS v10.0 + MEEST-AE v2.1  
**Status**: ATIVO

---

## Propósito

Este documento formaliza as regras de governança do engine estratégico LGPD.
Toda adição de dados, análise ou modificação do JSON deve seguir estas regras.
Violação = dado rejeitado.

---

## R1: VVV com Decay Temporal

```
vvv_decay = vvv × 1/(1 + 0.30 × meses)
```

- Score SNTI usa `vvv_decay`, NÃO `vvv` estático
- λ = 0.30 para SaaS (MEEST-AE v2.0 §Decay Temporal)
- Shelf_life típico: 6 meses para dados regulatórios, 3 meses para dados de mercado
- Revisar na `proxima_revisao` date definida por item

**Aplicação**: Toda vez que o JSON é lido para calcular score, usar vvv_decay, não vvv.

---

## R2: Cartas na Mesa (CNM)

Cada item SNTI = Carta com estrutura obrigatória:

```json
{
  "id": "string",
  "description": "string",
  "dimensao": "DAO|CEU|TERRA|COMANDANTE|METODO",
  "vvv": 0.0,
  "vvv_source": "fonte exata",
  "vvv_updated": "ISO-DATE",
  "fator": "string",
  "polaridade": "positivo|negativo|neutro",
  "criterios_dinamicos": {},
  "certeza_agregada": 0.0,
  "shelf_life": "N meses",
  "proxima_revisao": "ISO-DATE"
}
```

Campos obrigatórios. Item sem esses campos = carta inválida = rejeitado.

---

## R3: Sub-Engine por Público-Alvo

- Cada audiência tem próprio score SNTI com `custom_weights`
- Toggle global vs por-público na UI (App.vue controla)
- Sub-engine usa FDC-U recalibrado para critérios do segmento
- Decay temporal independente por segmento (dados podem ter datas diferentes)

**Aplicação**: ScenarioSimulator deve mostrar score global e score por audiência selecionada.

---

## R4: FDC-U Obrigatório em Toda Decisão

Antes de qualquer fork decisório:
1. Enumerar candidatos
2. Definir dimensões e pesos (Σw = 1.0)
3. Calcular Score(O) = Σ[w_i × f_i(A_i(O))]
4. Ordenar e escolher top-ranked

Proibido: decisão sem FDC-U quando há ≥2 alternativas.

---

## R5: Score Honesto Mesmo se Baixo

- NUNCA inflar VVV para justificar decisão
- Se dado não verificado → vvv < 0.5 (máximo 0.4 para gap/não verificado)
- Score SNTI baixo = realidade do mercado, não falha do sistema
- Regra de ouro: "É melhor score honesto baixo que score inflado alto"

**Violação detectada**: Se vvv > 0.8 sem fonte primária verificável → automático rebaixamento para 0.65.

---

## R6: Engine Dinâmico Item-a-Item

**PROIBIDO**:
- Scores hardcoded no Vue/JSON sem lógica derivada
- Lógica de scoring no template (deve estar em composables)
- Valores mágicos sem VVV
- Cálculo de score fora do ciclo reativo

**Obrigatório**:
- Cada item calcula seu score em tempo real
- Score muda quando slider_overrides mudam
- useVvvDecay composable usado em todos os componentes

---

## R7: Orquestração Reativa

```
slider muda → reavaliar TODOS scores (global + dimensões + itens)
```

- Nenhum score é estático após inicialização
- What-If badge aparece quando slider_overrides ativo
- Dimensão < 60 = CAUTELA alert
- Dimensão < 40 = NÃO ATACAR alert
- Score global recalcula em tempo real, não no mount

---

## R8: Fonte VVV Visível

Cada card DEVE mostrar:
- Barra visual VVV (0-100%)
- Botão "i" que expande fonte exata
- Status: [PESQUISANDO] | [CONCLUIDO] | [VALIDADO]
- vvv_provenance: origem do score (omnibus-pipeline-real | narrative-llm-single-turn)

---

## R9: WAL Obrigatório para Operações OMNIBUS

Toda operação S→Q→I→A DEVE:
1. Criar entry no WAL antes de executar: `[TIMESTAMP] [MODULE] [PHASE] EXEC [hash]`
2. Criar entry após completar: `[TIMESTAMP] [MODULE] [PHASE] COMPLETED quality_cot=X.XX`
3. Arquivo: `.claude/wal/shuntzu-operations.log` (append-only, nunca editar histórico)

---

## R10: Segregação de Responsabilidades

```
JSON = dados (strategic-data-unified.json)
Vue components = apresentação
App.vue = orquestração
composables/ = lógica reativa (useVvvDecay, etc.)
```

Regra: Nenhum dado estratégico vive fora do JSON.
Nenhuma lógica de negócio vive no template .vue.

---

## R11: Quality Threshold Pragmático

```
quality_threshold_pragmatic = 7.0/10
```

- Derivado do: pilot eca_digital_urgent (QUALITY_CoT = 7.24, vvv_decay = 0.98)
- Abaixo de 7.0 → RETORNAR ao Stage [S] com input refinado
- Acima de 7.0 → aceitar com vvv_provenance = 'omnibus-pipeline-real'
- Referência: HIQM v1.0 §P4 (no premature delivery), WAL 2026-05-09T22:50:07

**Justificativa de relaxamento de 95% HIQM para 7.0/10**:
O pilot provou que QUALITY_CoT = 7.24 → vvv_decay restaurado para 0.98.
Threshold pragmático permite escala (37 items) sem comprometer honestidade VVV.

---

## R12: Pipeline Obrigatório para Novos Dados

Todo dado novo DEVE:
1. Passar por S→Q→I→A completo antes de entrar no JSON
2. Ter entry WAL por stage executado
3. Ter sqia_trace_v2 no item JSON

**Dados narrative-llm-single-turn**:
- vvv_provenance = 'narrative-llm-single-turn'
- vvv_decay degradado automático: multiplicar vvv por 0.70 (penalty -30%)
- Marcar na UI com badge "Não verificado via OMNIBUS"

**Exceção**: Dados de transcrição de reunião (vvv_source = "transcricao") mantêm vvv original
pois são fonte primária (VVV = 1.0 escala CLAUDE.md).

---

## Audit Trail

| Data | Regra | Mudança | Autor |
|------|-------|---------|-------|
| 2026-05-09 | R1-R10 | Criação inicial | CLAUDE.md mandatos |
| 2026-05-09 | R11 | Quality threshold pragmático derivado do pilot | omnibus-orchestrator |
| 2026-05-09 | R12 | Pipeline obrigatório para dados novos | omnibus-orchestrator |

---

*OMNIBUS v10.0 | MEEST-AE v2.1 | VVV validated | 2026-05-09*

---

## R13: Quarentena de Dados Não-OMNIBUS (MANDATO ABSOLUTO)

**Data**: 2026-05-10  
**Origem**: Mandato explícito — sessão 2026-05-10

### Regra

TODO dado de pesquisa que NÃO seguiu pipeline OMNIBUS completo (S→Q→I→A + WAL + sqia_trace_v2):
1. **NÃO pode ser usado** em análises estratégicas
2. **NÃO pode ser referenciado** em prompts de agentes
3. **DEVE ser arquivado** em `archive/non-omnibus-data/`
4. **NÃO pode entrar** no JSON (`strategic-data-unified.json`)

### Dados arquivados (non-OMNIBUS)

```
archive/non-omnibus-data/
  pestle-porter-lgpd.md         — LLM single-turn, sem WAL
  market-research-2025.md       — LLM single-turn, sem WAL
  fdc-u-validation.md           — LLM single-turn, sem WAL
  swot-transcricao.yaml         — LLM single-turn, sem WAL
  bmc-roadmap-cross-check.yaml  — LLM single-turn, sem WAL
  [+ 14 arquivos adicionais]
  omnibus-audiences-*-S.md      — Stage S fabricado sem fonte verificável
```

### Como usar archive (leitura permitida)

Os arquivos em `archive/` podem ser usados APENAS como:
- Input [S] (coleta bruta) para novo pipeline OMNIBUS
- Referência histórica com flag `vvv_provenance=pre-omnibus-archive`

**NUNCA** como resultado final ou dado validado.

### Garantia automática

Agentes DEVEM verificar antes de usar qualquer arquivo de análise:
```bash
# Verificar se arquivo tem provenance OMNIBUS
grep -q "sqia_trace_v2\|omnibus-pipeline-real\|omnibus-retroativo-real" ARQUIVO || echo "QUARENTENA: não usar"
```

---

## R14: Audiences Válidas (pós F3-MSP Universe Mapping)

**Data**: 2026-05-10  
**Método**: shuntzu-f3 MSP Phase 1+2, QUALITY_CoT=8.00, 4 stages S→Q→I→A  
**WAL**: f3-msp-universe-{S,Q,I,A}.md + f3-msp-audiences-validated.md

### Audiences aprovadas via OMNIBUS

| ID | Nome | FDC-U Score | Tipo |
|----|------|------------|------|
| `b2g_consorcios` | Consórcios Intermunicipais | 7.99 | Cliente direto + Canal |
| `b2g_prefeituras_medio` | Prefeituras 20-100K hab | 7.64 | Cliente direto (SAM core) |
| `b2g_micro_municipios` | Micro-municípios <10K hab | 7.10 | Volume, espaço branco |
| `b2b_advocacia_whitlabel` | Escritórios Advocacia | 6.49 | Canal white-label |

### Audiences inválidas (sem evidência OMNIBUS)

- `b2b_fornecedores_municipio` — removida (evidência insuficiente)
- `b2b_empresas_privadas` — substituída
- `b2g_estaduais` — substituída

### Fonte de validação

`memory/wal/f3-msp-audiences-validated.md` — documento autoritativo.
