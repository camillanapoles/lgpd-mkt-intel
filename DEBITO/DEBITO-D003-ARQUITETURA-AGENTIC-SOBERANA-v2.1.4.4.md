---
id: NEOGOV-V21-DEBITO-D003-ARQUITETURA
filename: DEBITO-D003-ARQUITETURA-AGENTIC-SOBERANA-v2.1.4.4.md
created_at: 2026-05-15
type: TECHNICAL_DEBT_REGISTRY
status: REGISTERED_BLOCKS_D001
sprint_origem: S3.0.1 v1.0 (gerou contradição detectada pelo usuário)
sprint_destino: S2.5 (NOVO sub-sprint inserido ANTES de S3.0.1-redo)
parent_doc: BUSINESS-PLAN-FINAL-v2.1
purpose: Definir arquitetura técnica de IA soberana e agentic ANTES de modelar custos
priority: CRITICAL · bloqueia D001 (não pode modelar custo de IA sem definir qual IA e onde roda)
relationship_with_D001: D003 deve ser quitado PRIMEIRO · D001 depende de D003
tags: [debito, arquitetura, ia-local, soberania-digital, agentic, lgpd-compliance-interno]
---

# Débito Técnico D003 · Arquitetura Agentic com IA Soberana

> **Identificado em**: Sprint 3.0.1 edição 1 (post-mortem)
> **Severidade**: CRITICAL · bloqueia D001 inteiro (modelagem de custo)
> **Origem**: contradição operacional grave detectada pelo usuário · S3.0.1 v1.0 assumiu APIs IA externas (Anthropic Cloud, OpenAI) para processar dados pessoais e legais de clientes NeoGov
> **Sprint destino**: Sprint 2.5 (NOVO · inserido entre S2.1 e S3.0)

## 1 · Diagnóstico do erro estrutural

A modelagem S3.0.1 v1.0 assumiu uso de APIs cloud externas (Anthropic Claude, OpenAI) para processar:
- Documentos com CPFs, prontuários médicos, dados de menores
- Documentos sigilosos sob LAI
- Atos administrativos públicos com dados pessoais
- Solicitações de titulares LGPD com dados sensíveis

Isso configura **transferência internacional de dados pessoais** sem salvaguardas específicas. Viola:

| Norma | Artigo | Violação |
|---|---|---|
| LGPD | Art. 11 | Dado sensível requer salvaguardas extras (saúde, menores) |
| LGPD | Art. 33-35 | Transferência internacional só com autorização ANPD ou cláusulas-padrão |
| ECA Digital | Lei 15.211/2025 | Proteção reforçada para dados de menores |
| LAI | Lei 12.527/2011 | Documentos sigilosos não podem sair de jurisdição BR |
| Princípio Soberania Digital | Decreto 11.491/2023 | Governo federal exige soberania |
| **Coerência operacional** | — | **Empresa de compliance LGPD não pode violar LGPD** |

**Contradição fatal:** NeoGov vende compliance LGPD mas o produto vendido viola LGPD. Uma única notícia de "NeoGov manda dado de paciente para EUA" mataria a empresa.

## 2 · Decisão arquitetural proposta (validar com Camila)

### 2.1 · Stack técnico recomendado (a confirmar)

| Camada | Proposta principal | Fallback | Justificativa |
|---|---|---|---|
| **Modelo LLM** | Sabiá-4 / Sabiazinho-4 (Maritaca AI) | Llama 3.1 70B (Meta) ou Mixtral 8x22B | Sabiá-4 é BR · treinado em corpus jurídico BR · 128K context · empresa cumpre LGPD declaradamente |
| **Framework agentic** | LangGraph (LangChain) | CrewAI para prototipagem | LangGraph é default para regulated industries · durable execution · checkpoints · auditável |
| **Vector DB (RAG)** | Qdrant on-premise | pgvector (Postgres) | Open-source · pode rodar local · sem dependência externa |
| **Embeddings** | BAAI/bge-m3 (multilingual) on-premise | Sentence-transformers PT-BR | Open weights · pode rodar local |
| **Orquestração** | Kubernetes + Argo Workflows | Docker Compose (pequeno porte) | Padrão SOTA cloud-native |
| **Observability** | LangSmith self-hosted OU Langfuse | OpenTelemetry | Auditabilidade · Valor 5 NeoGov |

### 2.2 · Tier de deploy por persona

A NeoGov não terá UMA arquitetura · terá **3 tiers configuráveis** conforme sensibilidade do cliente:

#### Tier A · Cloud Soberana BR (default escola privada Gamma)

- Provedor: Magalu Cloud OU Locaweb Cloud
- Data center: São Paulo, BR
- Modelo: Sabiá-4 via API Maritaca (já compliance LGPD declarado)
- VPC dedicada por cliente
- **Justificativa:** clientes Gamma (escola privada média) não têm requisito de soberania extrema · cloud BR já basta
- **Custo aproximado:** R$ 800-3.000/cliente/mês (cloud + Maritaca API)

#### Tier B · Cloud Soberana BR + Modelo Open-Source On-Premise (default B2G Alfa)

- Cloud: Magalu/TIVIT (camada operacional)
- Modelo: Llama 3.1 70B fine-tunado com knowledge LGPD/LAI rodando em GPU NVIDIA L40S em cloud BR
- VPC dedicada + criptografia em repouso e trânsito
- **Justificativa:** B2G exige declarar onde os dados são processados · controle total sobre modelo
- **Custo aproximado:** R$ 2.500-8.000/cliente/mês (cloud + GPU dedicada compartilhada)

#### Tier C · On-Premise No Cliente (default Saúde Beta + B2G Federal sensível)

- Hardware: cliente fornece (hospital tem datacenter) OU NeoGov instala
- Modelo: Llama 3.1 70B ou Sabiá-4 licenciado on-premise (Maritaca oferece)
- Inferência: GPU NVIDIA L40S no datacenter cliente
- Atualização: NeoGov mantém modelo + knowledge base via VPN
- **Justificativa:** dado nunca sai do cliente · máxima soberania
- **Custo aproximado:** setup R$ 80-300k + manutenção R$ 3-15k/mês

### 2.3 · Arquitetura agentic proposta (multi-agent specialization)

```
                    ┌─────────────────────────────┐
                    │   ORQUESTRADOR LangGraph    │
                    │   (state + routing)         │
                    └──────────┬──────────────────┘
                               │
                ┌──────────────┼──────────────┬──────────────┐
                │              │              │              │
                ▼              ▼              ▼              ▼
        ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐
        │ Agent 1  │   │ Agent 2  │   │ Agent 3  │   │ Agent 4  │
        │ Data     │   │ Anonimi- │   │ AI-DPO   │   │ Compliance│
        │ Discovery│   │ zação    │   │ Copilot  │   │ Auditor   │
        │ (P2)     │   │ (P3)     │   │ (P4)     │   │ (P1+P4)   │
        └────┬─────┘   └────┬─────┘   └────┬─────┘   └────┬─────┘
             │              │              │              │
             └──────────────┴──────────────┴──────────────┘
                            │
                            ▼
              ┌─────────────────────────────┐
              │   KNOWLEDGE BASE NeoGov      │
              │   (RAG via Qdrant)           │
              │   - Knowledge Simone/Gislênia│
              │   - Jurisprudência LGPD/LAI  │
              │   - Templates produtos       │
              └─────────────────────────────┘
                            │
                            ▼
              ┌─────────────────────────────┐
              │   HUMAN ESCALATION          │
              │   - Edge cases jurídicos    │
              │   - Casos sensíveis         │
              └─────────────────────────────┘
```

### 2.4 · Por que multi-agent especializado vs modelo único

| Aspecto | Modelo único (Sonnet 4.6) | Multi-agent especializado |
|---|---|---|
| Custo inferência | Alto (modelo grande para tudo) | Baixo (modelo pequeno por tarefa) |
| Latência | Alta | Baixa (paralelização) |
| Auditabilidade | Difícil rastrear decisão específica | Cada agente loggable separadamente |
| Knowledge específico | Genérico no contexto | Embarcado via RAG por agente |
| Substituição modelo | Afeta tudo | Pode trocar agente por agente |
| Conformidade LGPD | Mais difícil isolar dado sensível | Cada agente com escopo isolado |
| Custo de evolução | Re-treinar modelo grande | Atualizar 1 agente isoladamente |

**Veredicto:** multi-agent especializado é a arquitetura SOTA 2026 para regulated industries.

## 3 · Inserção no roadmap

O roadmap precisa ser ajustado:

```
═══════════════════════════════════════════════════
🛑 BLOQUEIOS CONSTITUCIONAIS · resolver antes de prosseguir
═══════════════════════════════════════════════════

🥇 S2.5 · NOVO · Quitar D003 (CRITICAL · bloqueia D001)
   ├─ S2.5.1 → Validar stack técnico com Camila
   ├─ S2.5.2 → Decisão Sabiá-4 vs Llama 3.1 (POC pequeno)
   ├─ S2.5.3 → Validar Magalu/TIVIT/Locaweb (custo + soberania declarada)
   ├─ S2.5.4 → Desenhar arquitetura 3-tier (A, B, C)
   ├─ S2.5.5 → Cap 11 §arquitetura · adicionar seção arquitetura técnica
   Gate 2.5 · D003 quitado

🥈 S3.0 · Quitar D001 (CRITICAL · agora com arquitetura definida)
   ├─ S3.0.1-redo → Modelagem custo bottom-up COM IA SOBERANA
   ├─ S3.0.2 → Unit economics
   ├─ S3.0.3 → Pricing assertivo
   ├─ S3.0.4 → APENDICE-D xlsx
   └─ S3.0.5 → Retificar Cap 11 §pricing
   Gate 3.0 · D001 quitado

🥉 S5.0.5 · Quitar D002 (MEDIUM)
   └─ Auditoria cognitiva Caps 04/07/11
   Gate 5.0.5 · D002 quitado

═══════════════════════════════════════════════════
✅ PORTÃO ABERTO · plano principal retoma
═══════════════════════════════════════════════════
SPRINT 2.2 (Cap 01) → SPRINT 3.1 (BMC) → ...
```

## 4 · Anti-padrões a evitar (lição S3.0.1 v1.0)

- 🚫 **Modelar custo sem definir arquitetura** (erro origem deste débito)
- 🚫 **Assumir API externa para dado sensível** (viola LGPD)
- 🚫 **Modelo único genérico para tudo** (perde escala via especialização)
- 🚫 **Cloud não-soberana para B2G** (viola Decreto 11.491/2023)
- 🚫 **Decisão arquitetural sem validar com CTO (Camila)** (viola estrutura de governança NeoGov)
- 🚫 **Pricing antes de arquitetura** (D001 espera D003)

## 5 · Validação com a equipe NeoGov

**Pendente · GAP-CAMILA-01:** Camila (CTO) tem preferências técnicas que devem orientar S2.5?
- Já existe stack tecnológico em uso na NeoGov?
- Camila tem experiência com qual framework agentic?
- Há orçamento CAPEX para investir em GPU dedicada (Tier B)?
- Qual o status real do MVP atual da plataforma? (gap GAP04 antigo)

**A validar com a equipe antes de S2.5.4 (desenho final 3-tier):**
- Simone+Gislênia: arquitetura proposta satisfaz parecer jurídico LGPD/LAI/ECA?
- Wilton: clientes B2G têm exigência específica de cloud (Serpro? AWS Brasil? On-premise?)?

## 6 · Entregáveis do S2.5

1. **`content/11-produtos-v2.5.x.md`** — Adicionar §arquitetura técnica
2. **`continuity/ARQUITETURA-TECNICA-NEOGOV-v1.0.md`** — Documento técnico
3. **POC pequeno Sabiá-4** — validar que modelo BR atende tarefas LGPD
4. **Matriz custo arquitetura 3-tier** — base para S3.0.1-redo
5. **Decisão framework agentic** — LangGraph default ou CrewAI prototipagem?

## 7 · Impacto cruzado nos artefatos existentes

| Artefato | Impacto | Ação |
|---|---|---|
| Cap 11 §11.4-11.8 (produtos) | NÃO menciona arquitetura técnica | Adicionar §arquitetura nova |
| Cap 02 VMV §2.4 (missão) | Diz "aplicação de tecnologia avançada" | OK · não precisa ajuste |
| Cap 04 DT | OK · não especifica stack | OK |
| Cap 07 Personas | OK | OK |
| Cap 17 Riscos (BP v2.0) | Faltava risco "violar LGPD com IA externa" | Adicionar risco R-IA |
| S3.0.1 v1.0 | **TODO INVALIDADO** | Marcar SUPERSEDED |

## 8 · VVV consolidado pós-D003

| Componente | VVV atual | VVV alvo pós-D003 |
|---|---:|---:|
| Stack IA proposto | 0.65 | 0.90 (validado por POC + Camila) |
| Cloud soberana | 0.70 | 0.90 (validado por contrato) |
| Framework agentic | 0.75 | 0.90 (validado por POC) |
| Compliance LGPD interno | 0.30 ❌ | 0.95 ✅ |
| Custo IA bottom-up | 0.50 (invalidado) | 0.85 (após D003 + S3.0.1-redo) |

## 9 · Conexão com Plano Maior

Padrão emergente de débitos:
- **D001 (S3.0)** — débito de precisão técnica de custo
- **D002 (S5.0.5)** — débito de precisão cognitiva
- **D003 (S2.5)** — débito de coerência operacional (compliance interno)

D003 é o mais grave porque ataca a **integridade ontológica do produto** — não basta o produto entregar compliance, ele precisa SER compliance.

Lição metodológica: **PIER aplicado rigorosamente captura erros estruturais antes que se propaguem**. Este débito provou o valor do método (D-007 honestidade epistêmica + RGO-1 re-avaliar campo).

## 10 · Hash de continuidade

| Hash atual (antes deste débito) | Hash próximo |
|---|---|
| `NEOGOV-V21-S3.0.1-MODELAGEM-CUSTO-AWAIT-S3.0.2` | `NEOGOV-V21-S3.0.1-INVALIDADO+D003-CRITICAL-AWAIT-S2.5` |
