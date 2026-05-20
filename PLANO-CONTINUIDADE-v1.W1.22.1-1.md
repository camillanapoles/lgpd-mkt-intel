---
id: NEOGOV-V21-PLANO-CONTINUIDADE
filename: PLANO-CONTINUIDADE-v1.W1.22.1-1.md
version: 1.W1.22.1.1
created_at: 2026-05-20T02:35:00Z
type: EXECUTION_PLAN
parent_state: SESSION-STATE-v2.1.22.1.md
hash_entrada: NEOGOV-V21-W1.21.1-AUDITORIA-ENCERRADA-GATE-D24-ABERTO-2026-05-20
hash_saida_esperado: NEOGOV-V21-W1.26-SSOT-v1.0.9-FIXING-PLAN-FECHADO-BP-INVESTIDOR-READY
objetivo_global: "SSOT v1.0.9 canônico + FIXING_PLAN WS-A/B/D fechados + BP v2.1 investidor-ready com VPL defensável"
pre_start_status: PASSOU (7/7 checks · recursion_depth=0 · constitution válida)
---

# 🗺️ PLANO DE CONTINUIDADE · NeoGov BP v2.1
## Horizonte: W1.22.1 → W2.1 · a partir de 2026-05-20

> **Princípio de execução**: cada sprint tem gate de entrada e gate de saída mensuráveis. Nenhuma sprint começa sem gate de entrada passado. Nenhuma sprint fecha sem evidência de funcionamento real (RGO-2).

---

## VISÃO DO CAMINHO CRÍTICO

```
W1.22.1          W1.23.1          W1.24           W1.25           W1.26           W2.1
   │                │                │               │               │               │
[FDC-U D24]  →  [SSOT v1.0.9]  →  [WS-A]  →    [WS-B]  →    [WS-D + Cap15]  →  [Piloto]
Provedor        SSOT fechado     Custo infra    Rateio+Pricing   VPL final       Wave 1
canônico        bloqueio         step-func real  ABC real         investidor      calibra D7/D8
                levanta          MW-1 fecha       MW-2 fecha       ready
```

Paralelos legítimos (não bloqueiam caminho crítico):
```
W1.22.1 → W1.24-paralelo: [WS-C Demanda] · [Apêndice O Arq Técnica] · [D001-NOVO-4 PoC IA]
```

---

## SPRINT W1.22.1 · FDC-U Provedor Cloud (Gate D001-NOVO-24)

**Objetivo**: produzir ata de decisão formal Magalu vs AWS com FDC-U ≥ 9,0 e VVV ≥ 0,95.
**Bloqueia tudo** downstream. Máxima prioridade.

### Gate de ENTRADA W1.22.1
```
✅ SESSION-STATE v2.1.22.1 publicado           (DONE)
✅ AUDITORIA W1.21.1 governante                (DONE)
✅ Dimensionamento simbólico v1.20.1 disponível (DONE — base para calcular ambos)
✅ Scripts infra (build_neogov_infra.py)        (DONE — reutilizar)
✅ Recursion depth = 0                          (DONE)
```

### Tarefas W1.22.1

#### T1 · Cotação simétrica Magalu Cloud BR (atual) 
```
Ação:      web_search "magalu cloud GPU L40S preço 2026" + web_fetch magalu.cloud/calculadora
Entrega:   tabela preços Magalu · mesmo perfil do XLSX AWS (5 produtos × 3 portes)
Critério:  tarifa R$/h GPU + compute + storage + egress confirmada em fonte oficial ≤ 30 dias
Fallback:  se Magalu retirou L40S → flag imediato → D24 decide automaticamente para AWS
```

#### T2 · Tabela comparativa lado-a-lado (mesmo perfil de consumo)
```
Ação:      aplicar tarifas Magalu E AWS no dimensionamento simbólico v1.20.1
           (28 variáveis já mapeadas · só substituir preços unitários)
Entrega:   planilha "Custo_Comparativo_Magalu_vs_AWS_v1.W1.22.1.xlsx"
           → 5 produtos × 3 portes × 2 provedores = 30 células R$/mês
           → delta % por linha
Critério:  aritmética verificável · VVV ≥ 0,95 (fontes rastreáveis por célula)
```

#### T3 · FDC-U formal (8 dimensões)
```
Dimensões obrigatórias:
  D1  Custo total mensal (Wave 1 P75 · 31 clientes · mix real)
  D2  GPU capacity real (tokens/mês por R$ investido)
  D3  Conformidade LGPD/soberania (lei 13.709 · dados em solo BR)
  D4  Disponibilidade SLA (99,9% vs 99,99%)
  D5  Ecossistema BR (suporte PT, parceiros, integrações gov BR)
  D6  Latência real sa-east-1 vs Magalu datacenter BR
  D7  Vendor lock-in / custo de saída
  D8  Roadmap GPU (L40S disponível em 6 meses? A100?)

Pesos declarados ANTES do scoring (não pós-hoc):
  D1 0,25 · D2 0,20 · D3 0,15 · D4 0,10 · D5 0,10 · D6 0,08 · D7 0,07 · D8 0,05

Entrega:   DECISIONS-LOG-FDCU-D24-v1.W1.22.1.md
           com score por dimensão + score total + vencedor declarado + justificativa
Critério:  FDC-U score vencedor ≥ 7,5 · diferença mínima 10% para declarar sem ressalva
           Se diferença < 10%: declarar empate técnico → regra de desempate = D3 (LGPD)
```

#### T4 · Patch SSOT v1.0.8 → metadado de transição
```
Ação:      adicionar campo $meta.pending_upgrade = "D24 · aguarda FDC-U W1.22.1"
           no JSON SSOT v1.0.8 (não altera preços · só metadado)
Entrega:   neogov-pricing-cost-ssot-v1.0.8-PATCH-D24.json
Critério:  JSON válido · preços inalterados · campo novo visível
```

### Gate de SAÍDA W1.22.1
```
[ ] FDC-U score calculado e documentado
[ ] Vencedor declarado (Magalu OU AWS · sem ambiguidade)
[ ] Tabela comparativa verificável (VVV ≥ 0,95)
[ ] DECISIONS-LOG-FDCU-D24 publicado
[ ] D001-NOVO-24 status = FECHADO
→ Se TUDO acima: LIBERAR W1.23.1
→ Se cotação Magalu indisponível: W1.22.1 fecha como "AWS por default" com nota AUDITORIA
```

---

## SPRINT W1.23.1 · SSOT v1.0.9 — Publicação Canônica

**Objetivo**: publicar SSOT v1.0.9 com tarifas do provedor vencedor, ABC drivers recalculados, e todos os 19 tiers repriced.
**Gate de entrada**: W1.22.1 fechado com vencedor declarado.

### Tarefas W1.23.1

#### T1 · Re-cost L1A (12 drivers) com tarifas vencedor
```
Ação:      substituir cada driver do cost_model.layer_1a com tarifa real cotada
           Ex (se AWS): gpu_tokens_ia → g4dn.xlarge 730h × USD 0.6312 × R$5.04 = R$ 2.322
                        compute_k8s  → 4× t3.large 730h × USD 0.09984 × R$5.04 = R$ 1.470
           12 drivers × cotação verificada = Σ L1A novo
Entrega:   Σ L1A v1.0.9 com VVV = 1,0 (cada driver com URL fonte datada)
Critério:  Σ batem com source até R$ 50 de tolerância (margin error admitido)
```

#### T2 · Recalcular CFA (Cost per ABC Weight)
```
Ação:      CFA = Σ L1A / Σ abc_weights (todos os 19 tiers × qtd clientes Wave 1 P75)
           Usar abc_driver_weights do SSOT v1.0.8 (mantidos · não mudam de provedor)
           NOVO: verificar se algum driver weight precisa ajuste pós-DA-03 (P1/P5 sem GPU)
Entrega:   CFA novo em R$/peso · Δ% vs v1.0.8 declarado
Critério:  Wave 1 P75 aritmética fecha: Σ(CFA × abc_weight × N_clientes) ≈ Σ L1A ± 1%
```

#### T3 · Reprice 19 tiers
```
Ação:      para cada tier: Price_novo = CSC_novo ÷ (1 - margem_target)
           CSC_novo = CFA × abc_weight + CSC_L2_marginal + CF_rateado
           Manter margens-target do SSOT v1.0.8 (estratégia comercial não muda)
           Flags: se preço novo > 20% acima do validado → marcar como "revisar pricing"
Entrega:   19 tiers recalculados com price_novo · delta_vs_v1.0.8 · margem real
Critério:  nenhum tier com margem < 0% (exceto Beta Y1 investimento estratégico documentado)
```

#### T4 · Publicar neogov-pricing-cost-ssot-v1.0.9.json
```
Ação:      versionar JSON · atualizar $meta.version · $meta.created_at
           changelog: [D24 fechado · L1A re-cotado · 19 tiers repriced · COR-07 aplicada]
Critério:  JSON válido · VVV global ≥ 0,90 · Apêndice E v2.0.2 publicado junto
```

#### T5 · Apêndice E v2.0.2 (patch mínimo)
```
Ação:      atualizar §3.1 (provedor) · §4.2 (L1A drivers novos) · §A1.2 (lastros novos)
           NÃO reescrever inteiro · patch cirúrgico (regra CLAUDE.md §3)
Entrega:   APENDICE-E-COST-DECOMPOSITION-v2.0.2.md
Critério:  Σ drivers bate com JSON v1.0.9 até R$ 1,00
```

### Gate de SAÍDA W1.23.1
```
[ ] SSOT v1.0.9 JSON publicado · VVV ≥ 0,90
[ ] 19 tiers recalculados · todas as margens positivas ou justificadas
[ ] Apêndice E v2.0.2 publicado
[ ] CFA novo documentado com fórmula verificável
[ ] D001-NOVO-24 status = FECHADO (confirmado segunda vez)
→ Se TUDO: LIBERAR W1.24 (WS-A) + W1.24-paralelo (WS-C)
```

---

## SPRINT W1.24 · WS-A — Custo & Infra (Fecha MW-1 + CD-2)

**Objetivo**: substituir o modelo de custo fixo por função-degrau validada (resolve MW-1).
**Gate de entrada**: SSOT v1.0.9 publicado.

### Tarefas W1.24

#### T1 · Função de escala por recurso (passo a passo)
```
Ação:      para cada recurso L1A: definir a função custo(N_clientes)
           Formato: custo(N) = custo_base_tier + delta_por_tier × floor(N / threshold)
           Ex: GPU compute: 1 g4dn.xlarge por 0-10 clientes P3/P4 médio
                            2× acima de 10 → custo sobe R$ 2.322
           Usar dimensionamento simbólico v1.20.1 (já tem vCPU-h/mês por porte)
Entrega:   tabela de step-functions: 12 drivers × 3 portes × curva de escala
Critério:  cada função tem capacidade máxima declarada + threshold de upgrade declarado
```

#### T2 · Modelar custo real Wave 1 P25/P50/P75
```
Ação:      aplicar funções do T1 ao mix real de clientes W1 P75 (31 clientes declarados)
           Calcular custo infra real para cada percentil
Entrega:   tabela custo real vs custo linear atual (SSOT v1.0.8) por percentil
Critério:  diferença > 15% entre real e linear → atualizar SSOT v1.0.9 com correção
```

#### T3 · Fechar custo órfão CD-2 (R$ 310 kms+postmark)
```
Ação:      mapear kms (R$ 180) e postmark (R$ 130) para produto(s) donos
           Hipótese: kms → todos os produtos (encryption at rest · LGPD)
                     postmark → P4 AI-DPO (notificações chat)
Entrega:   abc_driver_weights atualizados para estes 2 itens em SSOT v1.0.9 patch
Critério:  nenhum driver L1A sem produto dono (fecha CD-2)
```

#### T4 · Apêndice E v2.0.2 → v2.0.3 (step-functions)
```
Ação:      adicionar seção §5 "Modelo de Escala" com as funções do T1
Critério:  MW-1 Management Letter marcado como FECHADO com evidência
```

### Gate de SAÍDA W1.24
```
[ ] Step-functions de todos os 12 drivers L1A documentadas
[ ] Custo real Wave 1 P75 calculado e comparado
[ ] CD-2 fechado (drivers kms/postmark com dono declarado)
[ ] MW-1 Management Letter finding = FECHADO com evidência
[ ] Apêndice E v2.0.3 publicado
→ Se TUDO: LIBERAR W1.25 (WS-B)
```

---

## SPRINT W1.24-PARALELO · Trabalhos não bloqueados por D24

Estas sprints correm **em paralelo** com W1.24 (não dependem do provedor).

### WS-C · Demanda & Mercado (fecha SD-1)
```
T1: Re-validar TAM/SAM com fonte ≤ 6 meses (web_search IBGE + ANATEL + CNJ 2026)
T2: Modelar curva S de adoção Wave 1→5 com referência (SaaS B2G BR comparáveis)
T3: Substituir extrapolação linear >M36 por S-curve com parâmetros declarados
T4: Atualizar Cap 03 (Mercado) com curva nova · nota de pressupostos visível
Critério:  SD-1 Management Letter = FECHADO
```

### Apêndice O · Arquitetura Técnica (valor não bloqueado)
```
T1: Formalizar NeoGov_Arquitetura_Infra_v1.20.1.docx como Apêndice O do BP
T2: Incorporar 8 diagramas C4 em Cap 11 (Tecnologia) com nota de provedor
    "diagramas agnósticos · instâncias específicas dependem de SSOT v1.0.9"
T3: Publicar APENDICE-O-ARQUITETURA-TECNICA-v1.0.md
Critério:  Cap 11 referencia Apêndice O · diagramas embarcados
```

### D001-NOVO-4 · PoC IA própria (Llama vs Sabiá)
```
T1: Levantar custo Sabiá-3 (Maritaca AI · preço API BR 2026)
T2: Levantar custo Llama 3.1 8B auto-hospedado no provedor vencedor
T3: FDC-U make vs buy: build (self-host) vs buy (API externa)
    Dimensões: custo/token · latência · controle · compliance LGPD · lock-in
T4: Registrar decisão em DECISIONS-LOG
Critério:  D001-NOVO-4 fechado · COR-07 (tipo instância GPU) atualizado se necessário
```

---

## SPRINT W1.25 · WS-B — Rateio & Pricing (Fecha MW-2)

**Objetivo**: refazer o rateio ABC sobre SSOT v1.0.9 e revisar os 19 tiers com preços de mercado.
**Gate de entrada**: W1.24 (WS-A) fechado.

### Tarefas W1.25

#### T1 · Validar pesos ABC com dados reais de uso (ou manter com flag)
```
Ação:      verificar se abc_driver_weights do SSOT v1.0.8 ainda são defensáveis
           com a nova arquitetura v1.20.1 (DA-01..09 mudaram alguns perfis)
           Se pesos mudam > 20% → refazer Apêndice I v1.0.2
           Se pesos mantêm dentro de 20% → flag D001-NOVO-8 para calibração piloto
Critério:  pesos declarados como [ENGENHARIA] ou [PREMISSA] (nunca silencioso)
```

#### T2 · Reprice final com custo real (step-func aplicada)
```
Ação:      para cada tier: Price_final = f(CSC_real_step_func) ÷ (1 - margem_target)
           Onde CSC_real veio de WS-A step-functions (T1 do W1.24)
Entrega:   19 tiers com price_final · margem real · delta vs price_validated v1.0.8
           Highlight: tiers onde margem mudou > 5pp
Critério:  nenhum tier com margem negativa não justificada
           Alfa-M Pro ainda ≥ 70% margem (produto âncora)
           Beta-Pequeno Y1 pode manter margem negativa estratégica SE documentada
```

#### T3 · Fechar MW-2 Management Letter
```
Ação:      substituir rateio 1/5 uniforme (XLSX exploratório) por ABC Apêndice I v1.0.2
           Produzir evidência: P4 AI-DPO paga mais L1 que P1 (correto · tem GPU)
                               Gamma paga menos L1 que Alfa (correto · sem GPU)
Critério:  MW-2 = FECHADO com evidência numérica da diferenciação
```

### Gate de SAÍDA W1.25
```
[ ] 19 tiers com price_final calculado sobre custo real
[ ] Apêndice I v1.0.2 publicado (ou flag D001-NOVO-8 declarado)
[ ] MW-2 = FECHADO com evidência
[ ] SSOT v1.0.9 atualizado com prices finais (v1.0.9-patch ou v1.1.0)
→ Se TUDO: LIBERAR W1.26 (WS-D + Cap 15)
```

---

## SPRINT W1.26 · WS-D + Cap 15 — Piloto & VPL Final

**Objetivo**: fechar SD-2 (margem validada), recalcular VPL defensável, BP investidor-ready.
**Gate de entrada**: W1.25 (WS-B) fechado.

### Tarefas W1.26

#### T1 · Fechar SD-2 (margem 72% sem origem)
```
Ação:      derivar margem média real de mercado dos tiers repriced de W1.25
           Calcular margem blend ponderada pelo mix W1 P75
           Documentar como FATO (não mais 72% flutuante)
Entrega:   margem blend declarada com decomposição por cluster
Critério:  SD-2 Management Letter = FECHADO
```

#### T2 · Recalcular DRE 3 cenários (P25/P50/P75)
```
Ação:      atualizar 15-financeiro com:
           - Receita: preços finais W1.25 × mix W1 P75
           - CSC: step-functions W1.24 aplicadas por percentil
           - Custos fixos: R$ 152.977 (Apêndice E v2.0.3)
Entrega:   DRE P25/P50/P75 atualizada · comparativa com versão anterior
Critério:  todos os inputs rastreáveis ao SSOT v1.0.9 ou Apêndice E v2.0.3
```

#### T3 · Recalcular VPL
```
Ação:      FCD com WACC 25% (conservador · D001-NOVO-20 atualiza pós-captação)
           3 cenários × 5 anos
           Substituir extrapolação linear por S-curve de WS-C
Entrega:   VPL P25/P50/P75 · E[VPL] · intervalo de confiança declarado
Critério:  VPL não é ponto · é intervalo [P25, P75] com P50 como referência
           Opinião auditoria: "DEFENSÁVEL" (vs anterior: "adversa")
```

#### T4 · Atualizar Cap 15 + CATÁLOGO-MESTRE v1.0.3
```
Ação:      patch Cap 15 com novos números (cirúrgico · não reescrever)
           Atualizar CATALOGO: PMQS, VVV, débitos fechados
Critério:  18/18 capítulos ainda coerentes com SSOT v1.0.9
```

### Gate de SAÍDA W1.26 = Gate BP INVESTIDOR-READY
```
[ ] SD-1 fechado (curva S demanda)
[ ] SD-2 fechado (margem blend documentada)
[ ] MW-1 fechado (step-functions infra)
[ ] MW-2 fechado (ABC rateio)
[ ] VPL defensável publicado (intervalo · não ponto)
[ ] Cap 15 atualizado
[ ] CATÁLOGO-MESTRE v1.0.3 publicado
[ ] Management Letter W1.9.1: 4/8 findings fechados (MW-1, MW-2, SD-1, SD-2)
→ BP v2.1 STATUS: INVESTIDOR-READY (com ressalvas declaradas: D7, D8, D20, D22)
```

---

## SPRINT W2.1 · Piloto Wave 1 — Calibração Real

**Início**: após BP investidor-ready (pós W1.26) **OU** em paralelo (lançar pilotos comerciais sem esperar W1.26 fechar).
**Objetivo**: calibrar D001-NOVO-7 (WTP real) e D001-NOVO-8 (pesos ABC reais) com dados de clientes.

### Estrutura
```
T1: 5 municípios Alfa pequenos (contratos piloto gratuitos 90 dias)
    → medir uso real P1/P3 · coletar feedback WTP · Van Westendorp 25 entrevistas
T2: 3 hospitais Beta pequenos (PoC 60 dias)
    → medir uso real P2/P4 · validar GPU compartilhamento (COR-06)
T3: 10 escolas Gamma (acesso básico gratuito)
    → validar CSC mínimo real · confirmar P1-only sem GPU
T4: Telemetria → calibrar abc_driver_weights reais → SSOT v1.1.0
```

### Critérios W2.1
```
[ ] 25 entrevistas WTP completadas → D001-NOVO-7 fechado
[ ] Telemetria real ≥ 60 dias → D001-NOVO-8 fechado ou refinado
[ ] GPU multi-tenant validada ou refutada → COR-06 fechado
[ ] SSOT v1.1.0 publicado com pesos reais
```

---

## RESUMO EXECUTIVO DO PLANO

```
Sprint      Foco                    Gate         Fecha débito(s)
─────────────────────────────────────────────────────────────────
W1.22.1     FDC-U Provedor          D24 fechado  D24
W1.23.1     SSOT v1.0.9             JSON pub.    COR-07
W1.24       WS-A Infra step-func    MW-1 fechado MW-1, CD-2
W1.24‑par   WS-C + Apêndice O + D4  paralelos    SD-1, D4
W1.25       WS-B Rateio + Pricing   MW-2 fechado MW-2
W1.26       VPL + Cap 15            BP inv-ready SD-1, SD-2
W2.1        Piloto Wave 1           SSOT v1.1.0  D7, D8
─────────────────────────────────────────────────────────────────
TOTAL ML findings fechados em W1.26:  4/8 (MW-1, MW-2, SD-1, SD-2)
Restantes declarados como "fechar com piloto": CD-4, D7, D8
Restantes pós-captação: D20, D22 (valuation)
```

---

## MATRIZ DE RISCO DO PLANO

| Risco | Impacto | Prob | Mitigação |
|---|---|---|---|
| Magalu retirou L40S do catálogo | D24 decide automaticamente para AWS | média | verificar T1 W1.22.1 primeiro |
| Preço AWS muito acima do SSOT v1.0.8 | repricing forçado · margens caem | média | step-functions W1.24 mostram real |
| Pesos ABC mudam > 20% com novas DAs | Apêndice I v1.0.2 completo | baixa | flag D001-NOVO-8 contém o risco |
| Margem Alfa-M Pro cai < 70% | repricing urgente ou novo tier | baixa | gate W1.25 T2 detecta antes |
| W1.22.1 > 1 sprint (cotação demora) | atraso cascata | média | iniciar WS-C paralelo para não perder velocidade |
| Piloto W2.1 sem clientes reais | D7/D8 ficam como premissas | alta | Wilton inicia pipeline comercial em paralelo agora |

---

## PRÓXIMA AÇÃO IMEDIATA (agora · sem esperar)

```
┌─────────────────────────────────────────────────────────────────┐
│  AÇÃO IMEDIATA: Iniciar W1.22.1 · T1                           │
│                                                                  │
│  web_search "magalu cloud GPU L40S preço mai 2026"              │
│  + web_fetch magalu.cloud/calculadora                            │
│  → Se L40S disponível: seguir FDC-U 8 dimensões               │
│  → Se L40S indisponível: D24 fecha para AWS automaticamente     │
│     + SSOT v1.0.9 usa tarifas XLSX v1.20.1 (já cotadas)        │
│     + pula direto para W1.23.1 T1                               │
└─────────────────────────────────────────────────────────────────┘
```

---

**FIM PLANO-CONTINUIDADE-v1.W1.22.1-1**

hash_saida: NEOGOV-V21-W1.22.1-PLANO-PUBLICADO-PRONTO-PARA-EXECUCAO-2026-05-20
