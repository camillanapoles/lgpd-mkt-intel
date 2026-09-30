---
id: NEOGOV-V21-SPRINT-3.0.1-CUSTO
filename: SPRINT-3.0.1-MODELAGEM-CUSTO-v1.0.md
created_at: 2026-05-15
type: TECHNICAL_DEBT_RESOLUTION
sprint: S3.0.1
edicao: 1
debt_id: D001
parent_sprint: S3.0
purpose: Modelagem bottom-up de custo dos 5 produtos NeoGov com 3 cenários e VVV declarado
vvv_target: 0.85
status: V1_PRODUCED_AWAITING_AUDIT
output_para_subsprint_seguinte: S3.0.2 (Unit Economics)
tags: [debito-D001, modelagem-custo, bottom-up, pricing-base]
---

# Sprint 3.0.1 · Modelagem de Custo Bottom-Up dos 5 Produtos

> **Objetivo:** estimar com rigor o custo real para a NeoGov produzir e operar cada um dos 5 produtos, criando base assertiva para o sub-sprint 3.0.2 (Unit Economics) e 3.0.3 (Pricing).

## 1 · Premissas e fontes primárias

### 1.1 Premissas globais

| Premissa | Valor | Fonte | VVV |
|---|---|---|---:|
| Câmbio USD→BRL | R$ 5,30 / USD | BACEN PTAX maio 2026 (estimativa operacional) | 0.85 |
| Regime tributário NeoGov | Simples Nacional · anexo III | Padrão para ICT pequeno porte · inferência operacional | 0.75 |
| Encargos sobre folha | 8% adicional ao salário bruto (Simples Nacional) | calculadorabrasil.com.br · gov.br Simples 2026 | 0.85 |
| Mês operacional | 22 dias úteis · 176 horas | Padrão CLT Brasil | 0.95 |
| Provisões CLT | 19,44%/mês (férias + 13º + FGTS) | calculadorabrasil.com.br | 0.90 |
| Custo total empregado | 1,28x salário (Simples Nacional + benefícios) | Síntese: 8% encargos + 19,44% provisões + 8% benefícios | 0.80 |

### 1.2 Insumos de mercado validados (web_search 2026-05-15)

**Salários técnicos Brasil 2026** [FATO · Glassdoor + Robert Half + Numerando · VVV 0.85]:

| Cargo | Júnior | Pleno | Sênior | Tech Lead |
|---|---:|---:|---:|---:|
| Desenvolvedor | R$ 3.500 | R$ 7.000 | R$ 12.000 | R$ 20.000 |
| Desenvolvedor IA/ML | R$ 5.000 | R$ 10.000 | R$ 18.000 | R$ 28.000 |
| Custo empresa (×1,28) | R$ 4.480 | R$ 8.960 | R$ 15.360 | R$ 25.600 |
| Custo IA empresa (×1,28) | R$ 6.400 | R$ 12.800 | R$ 23.040 | R$ 35.840 |

**API IA Anthropic Claude 2026** [FATO · platform.claude.com/docs/en/about-claude/pricing · VVV 0.95]:

| Modelo | Input USD/MTok | Output USD/MTok | Input BRL/MTok | Output BRL/MTok |
|---|---:|---:|---:|---:|
| Haiku 4.5 | $1 | $5 | R$ 5,30 | R$ 26,50 |
| Sonnet 4.6 | $3 | $15 | R$ 15,90 | R$ 79,50 |
| Opus 4.7 | $5 | $25 | R$ 26,50 | R$ 132,50 |

- Prompt caching: cache hit a 10% do preço base (90% economia em conteúdo repetido)
- Batch API: 50% desconto para processamento assíncrono <24h
- Estratégia NeoGov: Sonnet 4.6 default · Haiku 4.5 para classificação · Opus 4.7 só casos críticos jurídicos

**Cloud AWS/GCP SaaS multi-tenant** [INFERÊNCIA · benchmark AWS Calculator · VVV 0.70]:

| Tier | Cliente | Custo cloud/cliente/mês |
|---|---|---:|
| Compartilhado leve | Escola pequena · município < 30k hab | R$ 20 - R$ 60 |
| Dedicado médio | Escola média · município médio · empresa SMB | R$ 100 - R$ 400 |
| Dedicado pesado | Hospital · estado · grande município | R$ 600 - R$ 2.500 |
| Setup integração | ETL com sistema legado (one-shot) | R$ 5.000 - R$ 25.000 |

**CAC SaaS B2B Brasil 2026** [INFERÊNCIA · benchmark setor · VVV 0.65 · gap GAP05]:

| Canal | CAC típico SMB | CAC B2G médio | CAC B2G grande |
|---|---:|---:|---:|
| Inbound orgânico | R$ 800 - R$ 3.000 | R$ 3.000 - R$ 8.000 | R$ 10.000 - R$ 30.000 |
| Canal consórcio/parceria | R$ 1.500 - R$ 5.000 | R$ 5.000 - R$ 15.000 | R$ 15.000 - R$ 40.000 |
| Outbound direto | R$ 3.000 - R$ 8.000 | R$ 8.000 - R$ 25.000 | R$ 25.000 - R$ 80.000 |

---

## 2 · Estrutura de custos (5 componentes universais)

Para cada produto, modelaremos 5 componentes:

```
CUSTO TOTAL POR CLIENTE/MÊS =
    [1] Custos fixos alocados (desenvolvimento amortizado)
  + [2] Custos variáveis por cliente (infra + IA por uso)
  + [3] Custos operacionais (suporte + onboarding + jurídico contínuo)
  + [4] CAC amortizado (custo aquisição diluído na LTV esperada)
  + [5] Overhead administrativo NeoGov
```

### 2.1 Componente [5] · Overhead administrativo NeoGov

Custo fixo da empresa diluído entre todos os clientes ativos. **Cenário M6 (junho 2026 · pós-Wave 1):**

| Item | Custo mensal | Notas |
|---|---:|---|
| Salários core team (4 sócios não-CLT, pró-labore) | R$ 50.000 | Simone+Gislênia+Camila+Wilton · pró-labore R$ 12.500 cada |
| Software/SaaS internos (Notion, GitHub, comunicação) | R$ 3.000 | Estimativa SMB Brasil |
| Contabilidade + jurídico interno | R$ 5.000 | Pequena consultoria |
| Marketing (conteúdo + ads) | R$ 8.000 | Inbound focado |
| Reserva/contingência | R$ 5.000 | 7% sobre total |
| **Total overhead M6** | **R$ 71.000/mês** | |
| Clientes ativos M6 (estimativa) | 30 | 10 Alfa + 15 Gamma + 5 Beta-piloto |
| **Overhead por cliente/mês M6** | **R$ 2.367** | Decresce com escala |

Em escala (M24, 200+ clientes): overhead/cliente → R$ 500-800/mês.

---

## 3 · Modelagem por produto

### P1 · Plataforma LGPD SaaS (assinatura mensal)

**Persona âncora:** Mantenedor escolar (Gamma) · cliente típico: escola privada 200-800 alunos
**Modelo de cobrança:** assinatura mensal · self-service básico + DPO consultivo opcional

| Componente | Low | Mid | High | Memo |
|---|---:|---:|---:|---|
| **[1] Fixos alocados** | R$ 80 | R$ 150 | R$ 250 | Dev plataforma R$ 200k amortizado em 3 anos / 100-500 clientes |
| **[2] Cloud + storage** | R$ 25 | R$ 50 | R$ 120 | Tier compartilhado SaaS multi-tenant |
| **[2] IA (Sonnet base · ~100k tokens/mês)** | R$ 3 | R$ 8 | R$ 25 | Chatbot LGPD básico + RIPD assist |
| **[3] Suporte humano** | R$ 30 | R$ 80 | R$ 200 | Tier self-service: 5min/mês × R$ 90/h pleno |
| **[3] Onboarding amortizado** | R$ 50 | R$ 100 | R$ 200 | R$ 1k onboarding / 18 meses LTV esperada |
| **[3] Manutenção jurídica** | R$ 25 | R$ 50 | R$ 100 | Atualização legal propagada 1:N |
| **[4] CAC amortizado** | R$ 80 | R$ 200 | R$ 500 | R$ 2k-R$ 5k CAC / 18 meses |
| **[5] Overhead alocado** | R$ 100 | R$ 200 | R$ 400 | M6→M24 decrescente |
| **TOTAL custo/cliente/mês** | **R$ 393** | **R$ 838** | **R$ 1.795** | |

**Notas P1:**
- VVV componentes: 0.80 (média ponderada)
- Sensibilidade alta a CAC e onboarding em fase inicial
- Em escala (M18+), custo Mid cai para ~R$ 500-600/cliente/mês

---

### P2 · Data Discovery ★ICT (projeto + assinatura)

**Persona âncora:** Procurador municipal + Gestor B2G estadual/federal (Alfa-A, Alfa-E/F)
**Modelo de cobrança:** Setup projeto (one-shot) + assinatura monitoramento mensal

#### P2a · Setup do projeto (one-shot)

Discovery completo dos dados pessoais nos sistemas legados do cliente.

| Componente | Low | Mid | High | Memo |
|---|---:|---:|---:|---|
| **Trabalho humano** | R$ 8.000 | R$ 15.000 | R$ 35.000 | 80-300h pleno+sênior, depende do escopo |
| **IA varredura inicial (~5M tokens Sonnet)** | R$ 80 | R$ 250 | R$ 800 | Scan documentos + estruturação |
| **Cloud spike** | R$ 200 | R$ 800 | R$ 3.000 | Storage + processamento concentrado |
| **Jurídico Simone+Gislênia (validação)** | R$ 1.500 | R$ 4.000 | R$ 12.000 | Revisão final, parecer formal |
| **CAC alocado ao setup** | R$ 2.000 | R$ 5.000 | R$ 15.000 | B2G ciclo longo |
| **TOTAL setup** | **R$ 11.780** | **R$ 25.050** | **R$ 65.800** | |

#### P2b · Assinatura mensal monitoramento

| Componente | Low | Mid | High | Memo |
|---|---:|---:|---:|---|
| **Cloud monitoring** | R$ 50 | R$ 150 | R$ 600 | |
| **IA scan delta mensal (~500k tokens)** | R$ 8 | R$ 20 | R$ 60 | |
| **Suporte humano** | R$ 80 | R$ 200 | R$ 600 | |
| **Manutenção + atualização** | R$ 50 | R$ 150 | R$ 400 | |
| **Overhead alocado** | R$ 150 | R$ 300 | R$ 700 | |
| **TOTAL recorrente/mês** | **R$ 338** | **R$ 820** | **R$ 2.360** | |

**Notas P2:**
- VVV: 0.75 (componentes humanos têm variação alta)
- ★ICT: amortização adicional do INPI (R$ 5k registro / 10 anos vida útil patente)
- Status ICT permite Art. 75 IV (dispensa de licitação)

---

### P3 · Anonimização LAI/LGPD ★ICT (usage-based)

**Persona âncora:** Procurador + Gestor B2G (publicação obrigatória LAI)
**Modelo de cobrança:** Tier fixo (base) + usage-based por documento processado

#### P3a · Tier fixo base mensal

| Componente | Low | Mid | High | Memo |
|---|---:|---:|---:|---|
| **Plataforma base + auth** | R$ 80 | R$ 150 | R$ 300 | Acesso ao sistema · multi-tenant |
| **Cloud baseline** | R$ 50 | R$ 120 | R$ 300 | Idle infrastructure |
| **Manutenção jurídica LAI×LGPD** | R$ 100 | R$ 200 | R$ 500 | Atualização legal contínua (V2-knowledge ativo) |
| **Overhead alocado** | R$ 150 | R$ 300 | R$ 600 | |
| **Subtotal tier base** | **R$ 380** | **R$ 770** | **R$ 1.700** | |

#### P3b · Usage por documento anonimizado

Custo NeoGov para processar 1 documento típico (10-50 páginas):

| Componente | Por doc Low | Por doc Mid | Por doc High | Memo |
|---|---:|---:|---:|---|
| **IA Sonnet 4.6 (~15k tokens médio)** | R$ 0,40 | R$ 0,80 | R$ 2,00 | Análise + classificação + tarjamento sugerido |
| **IA Opus 4.7 (casos críticos · 5% volume)** | R$ 0,30 | R$ 0,80 | R$ 3,00 | Decisão complexa LAI×LGPD intersect |
| **Cloud processamento** | R$ 0,20 | R$ 0,50 | R$ 2,00 | OCR + storage + bandwidth |
| **Revisão humana amostral (10% docs)** | R$ 1,50 | R$ 4,00 | R$ 15,00 | Pleno jurídico revisa 1 a cada 10 |
| **CAC amortizado por doc (LTV 5k docs)** | R$ 0,40 | R$ 1,00 | R$ 3,00 | CAC R$ 2k-15k diluído |
| **TOTAL custo por documento** | **R$ 2,80** | **R$ 7,10** | **R$ 25,00** | |

**Notas P3:**
- VVV: 0.70 (volume × ticket têm sensibilidade alta · GAP02 WTP crítico)
- ★ICT: diferencial competitivo único · justifica margem alvo 80% (vs 60-65% outros produtos)
- Volume médio cliente B2G: 200-800 docs/mês · alto pode chegar a 5.000/mês

---

### P4 · AI-DPO Copilot ★ICT (assinatura mensal)

**Persona âncora:** Mantenedor escolar + Procurador municipal + Diretor saúde pequena
**Modelo de cobrança:** Assinatura mensal · tier por volume de solicitações de titulares

| Componente | Low | Mid | High | Memo |
|---|---:|---:|---:|---|
| **[1] Fixos alocados** | R$ 120 | R$ 250 | R$ 500 | Dev IA mais caro · R$ 350k / 3 anos / 100-300 clientes |
| **[2] Cloud + storage** | R$ 80 | R$ 180 | R$ 500 | Tier dedicado · armazenamento de logs |
| **[2] IA (Sonnet ~500k tokens/mês + Haiku classificação)** | R$ 20 | R$ 60 | R$ 200 | Chatbot DPO contínuo |
| **[3] Suporte humano** | R$ 80 | R$ 200 | R$ 500 | Tickets escalados |
| **[3] Onboarding amortizado** | R$ 150 | R$ 300 | R$ 700 | R$ 3k-R$ 8k onboarding / 18 meses |
| **[3] Manutenção jurídica** | R$ 80 | R$ 200 | R$ 500 | Knowledge base evolui semanal |
| **[4] CAC amortizado** | R$ 150 | R$ 400 | R$ 1.200 | R$ 3k-R$ 20k CAC / 18 meses |
| **[5] Overhead alocado** | R$ 150 | R$ 300 | R$ 600 | |
| **TOTAL custo/cliente/mês** | **R$ 830** | **R$ 1.890** | **R$ 4.700** | |

**Notas P4:**
- VVV: 0.75
- ★ICT: encapsula knowledge Simone+Gislênia treinado · registrável INPI
- Suporte humano cresce não-linearmente com volume titulares · monitorar

---

### P5 · ETL/Middleware (setup pesado + assinatura)

**Persona âncora:** Diretor saúde (hospital) · sistemas MV/Tasy/Soul MV
**Modelo de cobrança:** Setup pesado (one-shot) + assinatura operação + manutenção

#### P5a · Setup integração (one-shot)

Integração com sistema legado · escopo varia drasticamente.

| Componente | Low | Mid | High | Memo |
|---|---:|---:|---:|---|
| **Trabalho humano integração** | R$ 25.000 | R$ 80.000 | R$ 250.000 | Sênior+Tech Lead 250-1500h |
| **Discovery sistema cliente** | R$ 5.000 | R$ 15.000 | R$ 40.000 | Estudo MV/Tasy específico |
| **Cloud setup** | R$ 2.000 | R$ 8.000 | R$ 25.000 | Infraestrutura dedicada |
| **Validação jurídica** | R$ 3.000 | R$ 10.000 | R$ 25.000 | Simone valida conformidade ETL |
| **CAC alocado** | R$ 5.000 | R$ 15.000 | R$ 50.000 | Ciclo longo saúde |
| **PoC risco** | R$ 5.000 | R$ 15.000 | R$ 40.000 | Reserva para retrabalho M4 Gate |
| **TOTAL setup** | **R$ 45.000** | **R$ 143.000** | **R$ 430.000** | |

#### P5b · Assinatura mensal operação

| Componente | Low | Mid | High | Memo |
|---|---:|---:|---:|---|
| **Cloud operacional contínuo** | R$ 500 | R$ 2.000 | R$ 8.000 | Pipelines 24/7 |
| **Monitoramento + alerting** | R$ 200 | R$ 600 | R$ 1.800 | |
| **Suporte humano dedicado** | R$ 500 | R$ 1.500 | R$ 5.000 | SLA contratual |
| **Manutenção (mudanças legado)** | R$ 300 | R$ 1.000 | R$ 3.000 | MV atualiza · NeoGov adapta |
| **Overhead alocado** | R$ 400 | R$ 800 | R$ 2.000 | |
| **TOTAL recorrente/mês** | **R$ 1.900** | **R$ 5.900** | **R$ 19.800** | |

**Notas P5:**
- VVV: 0.65 (gap GAP03 PoC pendente · setup pode ter surpresas)
- Risco R4 BP v2.0: integração pode não funcionar tecnicamente em alguns sistemas
- Margem reduzida vs outros produtos por causa do suporte humano dedicado

---

## 4 · Tabela síntese · custo mid por produto

| Produto | Modelo | Setup mid | Recorrente mid | Margem alvo* |
|---|---|---:|---:|---:|
| P1 Plataforma SaaS | Assinatura | — | R$ 838/mês | 65% |
| P2 Data Discovery ★ICT | Projeto + Sub | R$ 25.050 | R$ 820/mês | 75% |
| P3 Anonimização ★ICT | Tier + Usage | R$ 770/mês tier + R$ 7,10/doc | — | 80% |
| P4 AI-DPO ★ICT | Assinatura | — | R$ 1.890/mês | 60% |
| P5 ETL/Middleware | Setup + Sub | R$ 143.000 | R$ 5.900/mês | 50% |

*Margem alvo do BP v2.1 §11 retificado (a ser confirmada no sub-sprint S3.0.3)

---

## 5 · Pricing derivado (preview · refinado em S3.0.3)

Aplicando margem alvo sobre custo mid:

| Produto | Custo mid | Margem alvo | Pricing derivado |
|---|---:|---:|---|
| P1 SaaS | R$ 838/mês | 65% | ≈ R$ 2.395/mês (tier médio) |
| P2 Setup | R$ 25.050 | 75% | ≈ R$ 100.200 (setup médio) |
| P2 Sub | R$ 820/mês | 75% | ≈ R$ 3.280/mês |
| P3 Tier base | R$ 770/mês | 80% | ≈ R$ 3.850/mês |
| P3 Doc | R$ 7,10/doc | 80% | ≈ R$ 35,50/doc |
| P4 AI-DPO | R$ 1.890/mês | 60% | ≈ R$ 4.725/mês |
| P5 Setup | R$ 143.000 | 50% | ≈ R$ 286.000 (setup médio) |
| P5 Sub | R$ 5.900/mês | 50% | ≈ R$ 11.800/mês |

**Alerta crítico:** pricing derivado P5 ≈ R$ 286k setup está ALÉM do que dispensa Art. 75 IV (R$ 65.492/2025). Implica: P5 não cabe via dispensa direta · obriga licitação OU divisão em fases · refinar em S3.0.3.

**Validação preliminar vs ranges do BP v2.1 §11:**
- P1 BP v2.1: R$ 500-10.000/mês → derivado mid R$ 2.395 ✅ dentro range
- P3 BP v2.1: R$ 1.000-30.000/mês → derivado mid R$ 3.850 + usage ✅ dentro range
- P4 BP v2.1: R$ 800-15.000/mês → derivado mid R$ 4.725 ✅ dentro range
- P5 BP v2.1: setup R$ 10-150k → mid R$ 286k ❌ ALÉM do range · REFINAR

---

## 6 · Componentes de incerteza e VVV consolidado

| Produto | VVV componentes | Maior incerteza | Gap externo |
|---|---:|---|---|
| P1 SaaS | 0.80 | CAC real (orgânico vs paid) | GAP02 WTP |
| P2 Data Discovery | 0.75 | Horas trabalho humano (escopo cliente) | GAP02 WTP |
| P3 Anonimização | 0.70 | Volume docs/mês por cliente | GAP02 WTP + GAP07 ECA digital |
| P4 AI-DPO | 0.75 | Volume tickets titulares | GAP02 WTP |
| P5 ETL/Middleware | 0.65 | Setup horas (surpresas técnicas) | GAP03 PoC saúde |
| **VVV médio S3.0.1** | **0.73** | | |

VVV alvo era 0.85. **Lacuna 0.12** indica que sub-sprints seguintes precisam reduzir incerteza via:
- S3.0.2: validar com 3-5 entrevistas WTP (GAP02)
- S3.0.3: pesquisar concorrentes Be Compliance + Safetyfyi (GAP05)
- Pré-Wave 2A: executar PoC ETL (GAP03)

---

## 7 · Entregáveis do S3.0.1

- ✅ Este documento (modelagem v1 com 5 produtos × 5 componentes × 3 cenários)
- ✅ Premissas declaradas com fontes
- ✅ Validação contra ranges do BP v2.1 (1 inconsistência detectada em P5)
- ✅ VVV declarado por produto e gap consolidado
- ⏭️ Para S3.0.2: aplicar Unit Economics (LTV/CAC/Payback) sobre estes custos
- ⏭️ Para S3.0.3: pricing assertivo com margem alvo confirmada
- ⏭️ Para S3.0.4: converter este documento em APENDICE-D-MODELO-CUSTO.xlsx editável
- ⏭️ Para S3.0.5: retificar Cap 11 §pricing com valores assertivos

---

## 8 · Decisões emergentes neste sub-sprint

### D-013 (emergente) · Estratégia de modelo de IA por produto

| Produto | Modelo IA principal | Modelo IA fallback | Por quê |
|---|---|---|---|
| P1 SaaS | Haiku 4.5 | Sonnet 4.6 | Volume alto · classificação simples |
| P2 Data Discovery | Sonnet 4.6 | Opus 4.7 | Análise rica de documentos |
| P3 Anonimização | Sonnet 4.6 (95%) + Opus 4.7 (5%) | — | Decisão LAI×LGPD complexa em casos críticos |
| P4 AI-DPO | Sonnet 4.6 | Haiku 4.5 (classificação) | Cobertura conversacional ampla |
| P5 ETL | Haiku 4.5 (classificação de campo) | — | Pipeline ETL não precisa raciocínio profundo |

Estratégia de **modelo certo para tarefa certa** = otimização de 30-60% no custo de IA vs uso uniforme de Sonnet.

### IN-015 (emergente) · P5 ETL fura limite Art. 75 IV · necessita estrutura comercial específica

Setup P5 mid R$ 286k > limite R$ 65.492 (Art. 75 IV 2025). Implica:
- **Opção A:** Dividir P5 em fases (PoC R$ 60k + ampliações via licitação)
- **Opção B:** Vender P5 só para clientes via licitação tradicional (não dispensa)
- **Opção C:** Reformular P5 com escopo menor que caiba na dispensa
- Decisão pendente → S3.0.3 ou S4.3 GTM

---

## 9 · Próximo sub-sprint · S3.0.2 Unit Economics

Inputs prontos para S3.0.2:
- ✓ Custo mensal por produto (low/mid/high)
- ✓ Custo aquisição (CAC) estimado por canal
- ✓ Duração esperada de cliente (LTV horizon · 18 meses padrão · 36 meses B2G)

S3.0.2 calculará:
- LTV (ticket × duração × margem bruta)
- LTV/CAC ratio (alvo ≥ 3 SaaS saudável · ≥ 5 B2G)
- Payback period (alvo ≤ 12m SMB · ≤ 24m B2G)
- Sensibilidade aos parâmetros

---

## Hash de continuidade

| Hash atual | Hash próximo |
|---|---|
| `NEOGOV-V21-S2.1-RETIFICADO+DEBT-D001-D002-BLOQUEANTES-AWAIT-RESOLUCAO` | `NEOGOV-V21-S3.0.1-MODELAGEM-CUSTO-AWAIT-S3.0.2` |
