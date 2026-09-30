# 🔧 RETIFICAÇÃO DO PLANO — Continuidade e VVV agora explícitos

**Você apontou 2 gaps críticos antes de eu disparar Sprint 1.** Vou retificar o plano antes de executar.

---

## FASE 0 — Clarificação Socrática dos gaps apontados

### Gap 1: Continuidade inter-sessões/inter-sprints

**O que você está pedindo:**
- Como **garantir que informação relevante** descoberta no Sprint 1 chegue ao Sprint 5 sem perda?
- Cada sprint deve ter **output explícito** que alimenta o próximo (não conhecimento implícito perdido)
- Mecanismo formal de **passagem de bastão** entre sprints

### Gap 2: VVV como anexo incremental paralelo

**O que você está pedindo:**
- Documento **separado e incremental** que registra cada validação VVV
- **Cresce a cada sprint** (não refeito do zero)
- Ao final, **incorporado ao BP** como apêndice/anexo de auditoria
- Permite ao leitor do BP ver a **rastreabilidade** de cada afirmação

**Estes 2 gaps são interdependentes**: o documento VVV paralelo É um dos canais de continuidade.

---

## FASE 1 — Arquitetura de Continuidade (resposta ao Gap 1)


### 1. Padrão de versionamento mandatório

```
{filename}-v2.{SPRINT}.{EDICAO}.{ext}
```

### Componentes

| Componente | Regra |
|---|---|
| `v2` | Versão maior do BP (não muda durante v2.x) |
| `SPRINT` | Sprint atual (1.1, 1.2, 1.3, 2.1, ...) |
| `EDICAO` | Contador incremental dentro do sprint, começa em 1 |
| `latest` | Symlink/cópia que SEMPRE aponta para a edição mais recente |

### Regra crítica

> **A edição seguinte é criada ANTES de receber edits.** Cria-se primeiro `{file}-v2.1.1.{SPRINT}.2.md` (vazio ou copy do .1), recebe edits nele, e ATUALIZA `{file}-latest.md`.

Isso garante:
- **Histórico imutável** — toda edição anterior preservada
- **Rastreabilidade** — qualquer leitor pega `-latest.md` e tem garantia da versão mais recente
- **Reversibilidade** — qualquer edição anterior recuperável
- **Atomicidade** — sem corrida de race condition entre edits

---

### 2. As 4 camadas de artefatos vivos

```
╔════════════════════════════════════════════════════════════════╗
║  CAMADA 1 · SESSION-STATE.md (WAL master)                      ║
║  └─ Estado vivo · atualizado a CADA fim de sprint              ║
║  └─ hash_continuidade rastreável                                ║
║                                                                  ║
║  CAMADA 2 · NEOGOV-v21-VVV-LOG.md (anexo VVV incremental)      ║
║  └─ Cresce a cada validação                                     ║
║  └─ Vira Apêndice A do BP final                                 ║
║                                                                  ║
║  CAMADA 3 · NEOGOV-v21-DECISIONS-LOG.md (decisões + ratio)     ║
║  └─ Toda decisão de produção registrada                         ║
║  └─ Vira Apêndice B do BP final                                 ║
║                                                                  ║
║  CAMADA 4 · NEOGOV-v21-INSIGHTS-CARRY.md (insights de campo)    ║
║  └─ Descobertas Sprint N que ajustam Sprint N+1                 ║
║  └─ Vira nota técnica integrada                                 ║
╚════════════════════════════════════════════════════════════════╝
```

### Como cada sprint OBRIGATORIAMENTE atualiza as 4 camadas

```
Sprint N executa
    │
    ├─→ produz capítulo {NN-nome}.md
    │
    ├─→ INCREMENTA VVV-LOG (toda afirmação validada)
    │
    ├─→ INCREMENTA DECISIONS-LOG (toda decisão tomada)
    │
    ├─→ INCREMENTA INSIGHTS-CARRY (descobertas que afetam próximos)
    │
    └─→ ATUALIZA SESSION-STATE (hash + status + próximo)
            │
            ▼
        GATE de aprovação
            │
            ▼
    Sprint N+1 LÊ as 4 camadas ANTES de começar
```

**Princípio de ouro:** *Nenhum sprint começa sem ler as 4 camadas atualizadas. Nenhum sprint termina sem incrementar as 4 camadas.*

---

## FASE 2 — Estrutura dos Anexos Incrementais (resposta ao Gap 2)

### Anexo A — VVV-LOG (rastreabilidade)

Schema operacional:

```yaml
afirmacao_id: AF-001
secao: cap_04_design_thinking
texto_resumido: "76,7% órgãos federais em grau inexpressivo LGPD"
classificacao: FACT
fonte_primaria: TCU Acórdão 1.384/2022
fonte_secundaria: Auditoria TCU 2024 (Rede Integrar)
verificada_em: 2026-05-14
vvv_score: 0.95
validador: HIQM_audit
ultima_revisao_sprint: S1.1
status: VÁLIDO
```

Cada capítulo escrito **gera N entradas no VVV-LOG**. O log cresce monotonicamente — nunca diminui, só refina.

### Anexo B — DECISIONS-LOG (rationale)

Schema:

```yaml
decisao_id: D-001
sprint: S1.1
data: 2026-05-14
contexto: "Capítulo 04 — escolha do framework de descrição DT"
opcoes_consideradas:
  - "IDEO 5 fases (Empathize→Test) — escolhido"
  - "d.school 6 fases (com Discover) — rejeitado"
  - "Double Diamond — rejeitado"
escolha: "IDEO 5 fases canônicas"
rationale: "inst-lgpd.md já adota IDEO; coerência com fonte VVV=1.0"
impacto_proximos_sprints: "Personas e Produtos devem seguir mesmo modelo"
revisivel: false
```

### Anexo C — INSIGHTS-CARRY (descobertas)

Schema:

```yaml
insight_id: IN-001
sprint_origem: S1.1
sprint_destino: S1.2
tipo: ADJUSTMENT | CONFIRMATION | CONTRADICTION | NEW_DATA
descoberta: "Durante mapeamento das 5 fases DT, identifiquei que a transcrição
            confirma 4 personas distintas (não 5). Quinta persona 'Gov Federal'
            é projeção do alvo declarado, não dor mapeada."
acao_em_sprint_destino: "Sprint S1.2 produz 4 empathy maps (não 5).
                        Gov Federal entra em projeção, marcado [INFERÊNCIA]"
impacto_vvv: "Ajusta vvv_global em -0.02 (transparência)"
incorporado_no_bp: true
```

---

## FASE 3 — Output retificado do Plano Mestre v2.1

### Estrutura completa de saída (atualizada)

```
/mnt/user-data/outputs/neogov-v21/
│
├── BUSINESS-PLAN-FINAL-v2.1.docx          ← entregável principal (Word)
├── BUSINESS-PLAN-FINAL-v2.1.md            ← fonte de verdade
├── BUSINESS-PLAN-FINAL-v2.1.pdf           ← versão assinada
│
├── anexos/
│   ├── APENDICE-A-VVV-LOG.md              ← rastreabilidade VVV incremental
│   ├── APENDICE-B-DECISIONS-LOG.md        ← rationale de decisões
│   ├── APENDICE-C-INSIGHTS-CARRY.md       ← descobertas inter-sprint
│   ├── APENDICE-D-MODELO-FINANCEIRO.xlsx  ← DRE/FCD/NPV/IRR
│   ├── APENDICE-E-EMPATHY-MAPS.pdf        ← 4 mapas detalhados
│   └── APENDICE-F-FONTES-EXTERNAS.md      ← bibliografia
│
├── continuity/
│   ├── SESSION-STATE.md                   ← WAL master vivo
│   └── HASH-CHAIN.md                      ← cadeia de hashes inter-sprint
│
├── content/                                ← capítulos MD fonte
│   ├── 01-capa-ficha.md
│   ├── 02-vmv.md
│   ├── 03-sumario-executivo.md
│   ├── 04-design-thinking.md              ← Sprint 1.1
│   ├── 05-pestel.md
│   ├── 06-mercado-tam.md
│   ├── 07-personas.md                     ← Sprint 1.2
│   ├── 08-clusters-fdcu.md
│   ├── 09-porter.md
│   ├── 10-suntzu.md
│   ├── 11-produtos.md                     ← Sprint 1.3
│   ├── 12-bmc.md
│   ├── 13-vpc.md
│   ├── 14-gtm-waves.md
│   ├── 15-financeiro.md
│   ├── 16-equipe-governanca.md
│   ├── 17-riscos.md
│   └── 18-roadmap.md
│
├── data/                                    ← data layer único
│   ├── personas.json
│   ├── produtos.json
│   ├── clusters.json
│   └── tokens.json
│
└── app/                                     ← Vue 3 App interativo
    └── ... (estrutura Vue completa)
```

---

## FASE 4 — Protocolo de Continuidade Operacional

### Template de fim-de-sprint (obrigatório)

Toda vez que fechar um sprint, executo este checklist:

```yaml
end_of_sprint_checklist:
  
  - [ ] Capítulo .md salvo em content/{NN-nome}.md
  - [ ] PMQS calculado e ≥ 9.5 (documentado em DECISIONS-LOG)
  - [ ] Afirmações novas adicionadas ao VVV-LOG com classificação
  - [ ] Decisões tomadas registradas no DECISIONS-LOG com rationale
  - [ ] Insights/descobertas registrados no INSIGHTS-CARRY
  - [ ] SESSION-STATE.md atualizado com:
      └─ hash_continuidade novo
      └─ status do sprint
      └─ próximo sprint identificado
      └─ pré-requisitos do próximo sprint resolvidos
  - [ ] Render preview docx (verificar que renderiza bem em Word)
  - [ ] Gate de aprovação com usuário
```

### Template de início-de-sprint (obrigatório)

```yaml
start_of_sprint_protocol:
  
  - [ ] Ler SESSION-STATE.md (estado atual)
  - [ ] Ler INSIGHTS-CARRY com sprint_destino == sprint_atual
  - [ ] Ler VVV-LOG (afirmações já validadas a reaproveitar)
  - [ ] Ler DECISIONS-LOG (decisões prévias que constrangem este sprint)
  - [ ] Confirmar fontes canônicas ainda válidas (inst-lgpd, BP-FINAL, DATA-v2)
  - [ ] Dispatch DTP: enumerar tarefas atomicas deste sprint
  - [ ] PIER: gerar abordagens, selecionar, executar
```

---

## FASE 5 — Garantia adicional: estrutura DOCX final

### Como os anexos chegam ao Word final

```
BUSINESS-PLAN-FINAL-v2.1.docx
│
├── CORPO PRINCIPAL (capítulos 01-18)
│   ↑ produzido nos Sprints 1-5
│
└── APÊNDICES (montados automaticamente no Sprint Consolidação)
    │
    ├── A. Rastreabilidade VVV  ← APENDICE-A-VVV-LOG.md incorporado
    ├── B. Decisões e Rationale ← APENDICE-B-DECISIONS-LOG.md incorporado
    ├── C. Notas de Iteração    ← APENDICE-C-INSIGHTS-CARRY.md incorporado
    ├── D. Modelo Financeiro     ← XLSX referenciado + sumário
    ├── E. Empathy Maps Visuais  ← imagens PDF embedded
    └── F. Bibliografia          ← APENDICE-F-FONTES-EXTERNAS.md
```

**Princípio**: o leitor do BP pode **auditar qualquer afirmação** consultando o Apêndice A (VVV-LOG), entender **qualquer decisão** consultando o Apêndice B (DECISIONS-LOG), e ver as **descobertas do processo** no Apêndice C (INSIGHTS-CARRY).

Isso transforma o BP de "documento estático" em **artefato auditável** — o que para uma empresa de compliance é coerência absoluta com o produto vendido.

---

## FASE 6 — Inicializando os 4 documentos de continuidade

Vou criar agora os arquivos esqueleto dos 4 anexos para que o Sprint 1 já comece preenchendo-os:Estrutura limpa. Agora crio os 4 documentos de continuidade com seus esqueletos:Os 4 documentos de continuidade estão inicializados. Vou apresentá-los e visualizar como o sistema funciona:Os 4 artefatos de continuidade estão entregues. Agora um diagrama do fluxo de informação:## ✅ Plano Retificado — Resumo do que mudou

| Antes | Depois |
|---|---|
| Continuidade implícita (memória + SESSION-STATE) | **4 documentos vivos** com schemas operacionais |
| VVV mencionado como score, mas sem rastro | **Apêndice A incremental** com 1 entrada por afirmação |
| Decisões tomadas sem registro formal | **Apêndice B append-only** com rationale |
| Insights de sprint perdidos no chat | **Apêndice C** garantia inter-sprint |
| BP final = só conteúdo | **BP final = conteúdo + 6 apêndices auditáveis (A-F)** |

**Princípio operacional vigente:**
- 🔒 Nenhum sprint inicia sem ler os 4 documentos vivos
- 🔒 Nenhum sprint termina sem incrementar os 4 documentos vivos  
- 🔒 Hash de continuidade comprovável a cada gate
- 🔒 Anexos A-C viram apêndices do BP final no Word

---

## 🎯 Pergunta operacional antes de disparar Sprint 1.1

Você já confirmou "sim, dispara Sprint 1 agora" antes. Mas como **adicionei a infraestrutura de continuidade**, quero confirmar:Aguardo confirmação para disparar Sprint 1.1.
