# Governance Rules — LGPD Strategic Decision Engine

## Regras derivadas do OMNIBUS v10.0 + MEEST-AE v2.1

---

## R1. VVV com Decay Temporal (MEEST-AE v2.0 §5)

**Regra**: VVV de cada item SNTI decai com o tempo conforme fórmula:
```
Certeza_atualizada = VVV_base × (1 / (1 + λ × meses_desde_atualização))
λ = 0.30 (SaaS = domínio volátil)
```

**Aplicação**: Cada item no JSON deve ter `vvv_updated` (date) e `vvv_decay` (calculado). Score SNTI usa `vvv_decay`, não `vvv` estático.

**Gatilhos**:
- Item com `vvv_decay < 0.5` → FLAG amarelo no card
- Item com `vvv_decay < 0.3` → REMOVER do score até revalidação
- Mês sem atualizar qualquer item → REAVALIAÇÃO OBRIGATÓRIA

---

## R2. Cartas na Mesa — Cada Item é uma Carta (MEEST-AE v2.0 §4)

**Regra**: Cada item SNTI é uma "carta" com estrutura mínima:
- `id` + `description` + `dimensao_sun_tzu`
- `vvv` + `vvv_source` (file:linha) + `vvv_updated` (date)
- `fator` + `polaridade` + `criterios_dinamicos` (min 5)
- `certeza_agregada` + `shelf_life` + `proxima_revisao`

**Aplicação**: Info button (i) do card mostra toda a estrutura da carta.

---

## R3. Sub-Engine por Público-Alvo (MEEST-AE v2.1 §1.1)

**Regra**: Score global NÃO é suficiente. Cada audiência (B2G, B2B, consultor, etc.) tem seu próprio score SNTI com pesos e itens diferenciados.

**Aplicação**: Tab "Arte da Guerra" deve ter toggle global vs por-público. Score recalcula quando troca público.

**Prioridade**: Implementar após Info buttons (P1 do plano FDC-U).

---

## R4. Nenhum Dado sem Fonte Mapeada (VVV §1)

**Regra**: Todo item com VVV > 0 DEVE ter `fonte` com:
- Arquivo ou URL exata
- Data da coleta
- Status: [PESQUISANDO] | [CONCLUÍDO] | [VALIDADO]

**Itens VVV=0.0**: São gaps explícitos. Devem ter `gap_reason` e `action_needed`.

---

## R5. Score Honestos Mesmo se Baixos (MEEST-AE v1.0 P5)

**Regra**: NUNCA inflar VVV para aumentar score. Score baixo = informação honesta = decisão melhor.

**Aplicação**: Se score SNTI < 40 ("RECUAR"), isso é útil. Mostra o que precisa ser resolvido antes de atacar.

---

## R6. Engine Dinâmica Item a Item (Princípio do Xadrez)

**Regra**: Dados de pesquisa = peças estáticas no tabuleiro (cenário atual). Sliders = "e se mover esta peça?" (what-if). ÚNICO dado estático permitido: VVV de pesquisa verificado.

**Proibido**:
- Scores hardcoded no componente
- Lógica de scoring no template
- Valores mágicos sem VVV

---

## R7. Orquestração Reativa (DTP §5)

**Regra**: Cada slider altera o campo de jogo. Após override, reavaliar TODOS os scores (global + dimensões + itens). Não recalcular parcialmente.

**Aplicação**: Quando slider muda, `computeOverrides()` já recalcula tudo. Manter este comportamento.

---

## R8. Continuidade entre Sessões (WAL Omnibus §4)

**Regra**: Estado do projeto persiste em:
- `CLAUDE.md` — visão e mandatos
- `memory/` — contexto entre sessões
- `specs/` — planos de execução
- JSON `strategic-data-unified.json` — single source of truth

**Ao iniciar nova sessão**:
1. Ler `CLAUDE.md` primeiro
2. Ler `memory/MEMORY.md` para contexto
3. Verificar `specs/` para planos pendentes
4. Ler JSON para estado atual dos dados

---

## R9. Validação Antes de Deploy (VVV + Build)

**Regra**: Antes de qualquer push para main:
1. `python3 -c "import json; json.load(open('public/strategic-data-unified.json'))"` — JSON válido
2. `bun run build` — build passa limpo
3. Verificar VVV: nenhum item > 0 sem fonte
4. Score SNTI honesto (não inflado)

---

## R10. Segregação de Responsabilidades (OMNIBUS Architecture)

**Regra**:
- **JSON** = dados + scoring config (VVV, overrides, rules)
- **Vue components** = apresentação + interação
- **App.vue** = orquestração (state, computed, routing)

**Proibido**:
- Lógica de negócio no template
- Dados hardcoded no componente
- Duplicação de fórmulas (App.vue header score vs ArtOfWar score)

---

## Checklist de Manutenção (a cada sessão)

- [ ] `vvv_updated` de cada item: < 30 dias?
- [ ] Build passa limpo?
- [ ] Score SNTI recalcula com sliders?
- [ ] Nenhum componente órfão?
- [ ] JSON válido e sem chaves duplicadas?
- [ ] Deploy ativo no GitHub Pages?
