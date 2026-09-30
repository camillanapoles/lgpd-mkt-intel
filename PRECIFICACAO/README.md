# NeoGov — Arquitetura de Infraestrutura v1.20.1

**ID do Projeto:** NEOGOV-V21-INSTRUCAO-SESSAO-PARALELA
**Data:** 2026-05-20
**Classificacao:** CONFIDENCIAL — Uso Interno

---

## Sumario Executivo

Este pacote contem a arquitetura de infraestrutura completa da plataforma NeoGov, seguindo metodologia tradicional de Engenharia de Requisitos. O trabalho abrange 5 produtos (P1 a P5) x 3 portes de cliente (Pequeno, Medio, Grande), com modelo de duas camadas (Layer 1 comum + Layer 2 especifica por produto).

### Produtos

| ID | Produto | Tipo | GPU |
|----|---------|------|-----|
| P1 | Data Discovery | Batch | Nao |
| P2 | Anonimizacao | Batch (GPU) | Spot/Preemptiva |
| P3 | LAI x LGPD | Interativo | Quente Reservada 24/7 |
| P4 | AI-DPO | Interativo (RAG) | Quente Reservada 24/7 |
| P5 | ETL / Integracao | Batch | Nao |

### Portes de Cliente

| Porte | Funcionarios | Exemplos |
|-------|-------------|----------|
| Pequeno | 1-50 | Pequena prefeitura, escola privada |
| Medio | 51-500 | Municipio medio, hospital privado |
| Grande | 501+ | Estado, orgao federal, rede hospitalar |

---

## Estrutura do Projeto

```
neogov-infra-projeto/
|
|-- NeoGov_Arquitetura_Infra_v1.20.1.docx    # DOCUMENTO PRINCIPAL
|   |-- Capa profissional
|   |-- Secao 1: Engenharia de Requisitos
|   |   |-- 1.1 Requisitos Funcionais (26 RF por produto)
|   |   |-- 1.2 Requisitos Nao-Funcionais (12 RNF)
|   |   |-- 1.3 Matriz de Rastreabilidade (RF x Produto x Persona x Gargalo)
|   |-- Secao 2: Modelo C4 (8 diagramas embutidos)
|   |   |-- 2.1 C4 L1 — Contexto do Sistema
|   |   |-- 2.2 C4 L2 — Layer 1 Global (Shared Services)
|   |   |-- 2.3 C4 L2 — P1 Data Discovery
|   |   |-- 2.4 C4 L2 — P2 Anonimizacao
|   |   |-- 2.5 C4 L2 — P3 LAI x LGPD
|   |   |-- 2.6 C4 L2 — P4 AI-DPO
|   |   |-- 2.7 C4 L2 — P5 ETL / Integracao
|   |   |-- 2.8 C4 L3 — Pipeline de Inferencia GPU
|   |-- Secao 3: Decisoes Arquiteturais (DA-01 a DA-09)
|   |-- Secao 4: Derivacao de Infraestrutura (Layer 1 + Layer 2)
|   |-- Secao 5: Correcoes vs Dimensionamento Anterior (COR-01 a COR-10)
|
|-- NeoGov_Dimensionamento_Infra_v1.20.1.xlsx    # PLANILHA DE DIMENSIONAMENTO
|   |-- Resumo Executivo (porte de cliente, nota de classe)
|   |-- P1 Data Discovery (11 linhas: 5 L2 + 6 L1)
|   |-- P2 Anonimizacao (13 linhas: 7 L2 + 6 L1)
|   |-- P3 LAIxLGPD (12 linhas: 6 L2 + 6 L1)
|   |-- P4 AI-DPO (13 linhas: 7 L2 + 6 L1)
|   |-- P5 ETL-Integracao (12 linhas: 6 L2 + 6 L1)
|   |-- Variaveis do Piloto (28 variaveis)
|   |-- Premissas a Validar (16 premissas)
|   |-- Verificacao CV (CV1-CV8 todas PASS)
|
|-- c4-diagramas/                            # DIAGRAMAS C4 (PNG individuais)
|   |-- C4-L1-System-Context.png              # Contexto do sistema (4 personas + ext)
|   |-- C4-L2-Layer1-Global.png              # Layer 1: Shared Services
|   |-- C4-L2-P1-DataDiscovery.png           # P1: Varredura batch, sem IA
|   |-- C4-L2-P2-Anonimizacao.png            # P2: GPU batch, job queue
|   |-- C4-L2-P3-LAixLGPD.png               # P3: GPU quente reservada
|   |-- C4-L2-P4-AI-DPO.png                  # P4: GPU quente reservada + RAG
|   |-- C4-L2-P5-ETL-Integracao.png         # P5: Batch, sem IA
|   |-- C4-L3-GPU-Inference.png              # Pipeline inferencia P3/P4
|
|-- scripts/                                  # SCRIPTS GERADORES
|   |-- gen_c4_diagrams.py                   # Gerador dos 8 diagramas C4 (Playwright)
|   |-- gen_docx_arq.py                      # Gerador do DOCX de arquitetura
|   |-- build_neogov_infra.py                # Gerador do XLSX de dimensionamento
|
|-- briefing/                                 # BRIEFING DE REFERENCIA
|   |-- BP-Cap04-Design-Thinking-e-Cap07-Personas.md
|
|-- README.md                                 # ESTE ARQUIVO
```

---

## Metodologia

### Fluxo de Trabalho

O projeto seguiu a sequencia metodologica tradicional de Engenharia de Requisitos:

1. **Levantamento de Requisitos** — Analise do briefing NEOGOV-V21, capitulos do Business Plan (Design Thinking + Personas) e mapeamento de 4 personas com dores, gatilhos e ciclos de decisao.

2. **Engenharia de Requisitos** — Formalizacao de 26 Requisitos Funcionais (RF) e 12 Requisitos Nao-Funcionais (RNF), com prioridades, classes tecnicas e metricas de sucesso.

3. **Arquitetura de Sistema (C4)** — Modelagem hierarquica em 4 niveis: Contexto do Sistema (L1), Containers por camada (L2), Componentes criticos (L3). 8 diagramas produzidos.

4. **Decisoes Arquiteturais** — Registro de 9 decisoes arquiteturais (DA-01 a DA-09) documentando escolhas como GPU quente vs batch, vector store compartilhado, e soberania de dados.

5. **Derivacao de Infraestrutura** — Mapeamento de requisitos para recursos de infra, separados em Layer 1 (comum, rateio proporcional) e Layer 2 (especifico por produto).

6. **Dimensionamento** — Tabelas de demanda com funcoes por recurso x porte, classificacao [ENGENHARIA]/[ANALOGO]/[PREMISSA], e verificacao CV1-CV8.

### Classes de Estimativa

| Classe | Definicao | Percentual |
|--------|-----------|------------|
| [ENGENHARIA] | Derivado diretamente da arquitetura C4 | 40% |
| [ANALOGO] | Baseado em sistema similar conhecido | 8% |
| [PREMISSA] | Assuncao a ser validada no piloto | 50% |

### Verificacao CV (todos PASS)

| CV | Descricao | Status |
|----|-----------|--------|
| CV1 | Todo recurso tem Classe de Estimativa | PASS |
| CV2 | Sem valores em R$ | PASS |
| CV3 | Layer 1 rateada por uso | PASS |
| CV4 | GPU aparece apenas onde a arquitetura indica | PASS |
| CV5 | P1 e P5 sem GPU | PASS |
| CV6 | P3 e P4 com GPU quente reservada | PASS |
| CV7 | P2 com GPU batch sob demanda | PASS |
| CV8 | Toda premissa classificada por criticidade | PASS |

---

## Decisoes Arquiteturais (DA-01 a DA-09)

| ID | Decisao | Impacto |
|----|---------|---------|
| DA-01 | GPU quente reservada 24/7 para P3 e P4 | Custo fixo elevado, mas SLA de latencia garantido |
| DA-02 | GPU spot/preemptiva para P2 | Custo variavel, tolerancia a cold start |
| DA-03 | Cloud BR exclusivamente (RNF-01) | Sem API externa, modelos proprios |
| DA-04 | Multi-tenancy por schema PostgreSQL | Isolamento logico sem hardware dedicado |
| DA-05 | API Gateway centralizado (Layer 1) | Ponto unico de entrada, rate limiting, auth |
| DA-06 | Vector Store compartilhado P3/P4 | Redundancia de infra para mesmos embeddings |
| DA-07 | Retencao de audit logs: 5 anos imutavel | Requisito LGPD Art. 46 |
| DA-08 | Job Queue (RabbitMQ) para batch P1/P2/P5 | Desacoplamento e resiliencia |
| DA-09 | Conector Manager generico para P1/P5 | Abstracao sobre multiplos sistemas legados |

---

## Correcoes Aplicadas vs Dimensionamento Anterior

Foram identificadas 10 correcoes (COR-01 a COR-10) entre o dimensionamento inicial e a arquitetura validada, incluindo:

- **COR-01**: P2 deve usar GPU batch (spot), nao GPU quente
- **COR-02**: Vector Store deve ser contabilizado separadamente para P3 e P4
- **COR-03**: P1 e P5 nao devem ter linha de GPU (confirmacao arquitetural)
- **COR-04**: GPU quente P3/P4 requer armazenamento de modelo em VRAM
- **COR-05**: Retencao de 5 anos para audit logs (necessita storage dedicado)
- E mais 5 correcoes menores detalhadas no DOCX Secao 5.

---

## Premissas Criticas a Validar no Piloto

| # | Premissa | Criticidade |
|---|----------|-------------|
| PR-01 | Modelo NER BERT-base pt-BR e suficiente para P2 | CRITICA |
| PR-02 | Modelo LLM 7B e suficiente para P4 (qualidade de resposta) | CRITICA |
| PR-03 | Modelo de decisao P3 atinge >90% acuracia com fine-tune | CRITICA |
| PR-04 | Volume medio de documentos P2 por tenant e < 1.000/mes | ALTA |
| PR-05 | Uso simultaneo P4 por tenant e < 5 sessoes concorrentes | ALTA |
| PR-06 | Conector e-Cidade pode ser implementado em < 2 semanas | ALTA |

---

## Requisitos Nao-Funcionais Transversais

| RNF | Descricao | Metrica |
|-----|-----------|---------|
| RNF-01 | Soberania de Dados | 100% em cloud BR, 0 APIs externas |
| RNF-02 | Multi-tenancy | Zero vazamento cross-tenant |
| RNF-03 | Latencia P3 | P95 < 2s |
| RNF-04 | Latencia P4 | TTFT P95 < 3s |
| RNF-05 | Retencao Auditoria | 5 anos imutavel |
| RNF-06 | GPU Quente | Modelo loaded 24/7, cold start = 0 |
| RNF-09 | SLA Disponibilidade | Uptime >= 99.5% mensal |
| RNF-12 | IA Propria Local | 0 dependencias de API externa |

---

## Tecnologias Referenciadas

| Camada | Tecnologia |
|--------|------------|
| API Gateway | Kong / AWS API Gateway |
| Auth | OAuth2 / OIDC / JWT (Keycloak) |
| Banco Relacional | PostgreSQL (multi-tenant por schema) |
| Object Storage | S3-compatible (MinIO / cloud BR) |
| Vector Store | Milvus / Qdrant |
| GPU Batch | NVIDIA T4/A10G spot instances |
| GPU Quente | NVIDIA A10G/T4 reservadas 24/7 |
| Job Queue | RabbitMQ / SQS |
| Orquestracao | Celery / Apache Airflow |
| NER Model | BERT-base pt-BR (fine-tuned) |
| LLM | 7B参数 (fine-tuned LGPD) |
| Observabilidade | Prometheus + Grafana + ELK |
| KMS | HashiCorp Vault |

---

*Gerado em 2026-05-20 | NeoGov ICT — LGPD Compliance + AI*
