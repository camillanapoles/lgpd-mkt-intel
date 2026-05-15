---
id: NEOGOV-V21-SUPERSEDED-MARKER-S3.0.1
filename: SUPERSEDED-S3.0.1-MODELAGEM-CUSTO-v1.0.md
created_at: 2026-05-15
type: SUPERSEDED_MARKER
status: SUPERSEDED_ACTIVE
parent_artifact: SPRINT-3.0.1-MODELAGEM-CUSTO-v1.0.md
reason: Erro estrutural · violação operacional grave
supersedes_action: NÃO USAR este artefato como input para qualquer sub-sprint
detected_by: usuário · iteração crítica pós-entrega S3.0.1
honra_valor: V1 Honestidade Epistêmica + D-007 (declarar erros sem mascarar)
honra_regra: RGO-1 (campo mudou · re-avaliar) + RGO-4 (não construir sobre base instável)
---

# 🛑 ARTEFATO SUPERSEDED · S3.0.1 v1.0 Modelagem de Custo

## Por que está marcado como SUPERSEDED

O artefato `SPRINT-3.0.1-MODELAGEM-CUSTO-v1.0.md` (PMQS 6.75) assumiu uso de APIs IA cloud externas (Anthropic Claude, OpenAI) para processar dados pessoais e legais de clientes da NeoGov.

Isso configura **transferência internacional de dados pessoais** sem salvaguardas adequadas, violando:

- LGPD Art. 11 (dado sensível)
- LGPD Art. 33-35 (transferência internacional)
- ECA Digital Lei 15.211/2025 (dados de menores)
- LAI Lei 12.527/2011 (documento sigiloso)
- Princípio Soberania Digital · Decreto 11.491/2023
- **Coerência operacional**: empresa de compliance LGPD não pode violar LGPD

Contradição fatal: NeoGov vende compliance LGPD mas o produto vendido violaria LGPD.

## O que fazer

1. **NÃO consumir** este artefato como input para qualquer sub-sprint
2. **NÃO referenciar** valores específicos (R$ 5,30/MTok Sonnet etc.)
3. **CONSIDERAR APENAS estrutura metodológica preservável:**
   - Framework de 5 componentes de custo (válido)
   - Premissas globais salários/encargos BR (válido)
   - Estrutura 3 cenários low/mid/high (válido)
   - Salários BR 2026 dados (válido)
   - Cloud SaaS benchmarks (parcialmente válido · refinar com cloud soberana BR)

## O que substituirá

Após D003 quitado (Sprint 2.5), o **Sprint 3.0.1-redo** produzirá nova modelagem com:
- Stack técnico definido em D003 (Sabiá-4 / Llama 3.1 / LangGraph / Cloud BR)
- 3 tiers de deploy (Magalu/Locaweb · GPU cloud BR · on-premise)
- Custos compatíveis com arquitetura agentic real

## Referências cruzadas

- Débito gerador: `DEBITO-D003-ARQUITETURA-AGENTIC-SOBERANA-v2.1.4.4.md`
- Hash continuidade pré-erro: `NEOGOV-V21-S3.0.1-MODELAGEM-CUSTO-AWAIT-S3.0.2`
- Hash continuidade pós-erro: `NEOGOV-V21-S3.0.1-INVALIDADO+D003-CRITICAL-AWAIT-S2.5`

## Decisão emergente

D-014 · Modelagem de custo NÃO pode ser feita antes de definir arquitetura técnica (decisão metodológica permanente · adicionar à governança NeoGov).
