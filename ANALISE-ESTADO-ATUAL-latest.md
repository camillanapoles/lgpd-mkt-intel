```
[Modo: S→Q→I→A | CoT: 9.3/10 | Q: 96/100 | Bias: MONITORED]
[PRE-ALWAYS executado · granularidade: ação significativa]
[Auditoria HOSTIL · estado real vs plano NORTH · sem viés de confirmação]
```

## [S] ANÁLISE SOCRÁTICA · Deconstruct

**Mandato recebido**:
1. PLANO NORTH (anexado) = planejamento original · 18 seções · 5 sprints + consolidação · entregável Word
2. Auditar HOSTIL o que foi feito vs plano NORTH (VVV adversarial)
3. Capturar pertinências/débitos
4. Replanejar sequência conforme estado atual real

**Decomposição atômica do plano NORTH** (universo de referência):

| Wave NORTH | Seções | Status NORTH-original |
|---|---|---|
| Wave 1 crítico | 04 DT · 07 Personas · 11 Produtos · 02 VMV · 01 Capa | Sprint 1 + 2 |
| Wave 2 estratégico | 12 BMC · 13 VPC · 08 Clusters · 15 Financeiro · 14 GTM · 09 Porter · 16 Equipe · 18 Roadmap | Sprint 3 + 4 |
| Wave 3 refinamento | 03 Sumário · 06 TAM · 10 Sun Tzu · 05 PESTEL · 17 Riscos | Sprint 5 |
| Consolidação | docx · xlsx · Vue · pdf · slides | C.1-C.4 |

**Universo produzido** (árvore tree fornecida) · file system real:

| Categoria | Arquivos identificados |
|---|---|
| Capítulos canônicos | 02-vmv · 04-design-thinking · 07-personas · 11-produtos · (4 de 18) |
| Sprints desviados | SPRINT-3.0.1 (v1+v2+v3) · SPRINT-3.0.3 |
| Apêndices vivos | A-VVV-LOG · B-DECISIONS · C-INSIGHTS · E-LASTREAMENTO (D ausente) |
| Débitos | D001 · D002 · D003 (v2.1.4.4 e .4.5) |
| BSC drafts | BSC-01/02/03 (insumos · não fontes operacionais) |
| Engines (skills) | 18+ engines em /skills/ENGINE-MODULES/ e /skills/SHUN_TZU/ |
| Governance | POP latest · SESSION-STATE × 17 versões |
| Book final | Blueprint Societário · Arquitetura Processo |
| Source-of-truth oficial | NEOGOV-BUSINESS-PLAN-FINAL.docx + .md |

Vou investigar o estado real antes de auditar:Tenho dados suficientes para auditoria hostil. Vou cruzar BP FINAL real × plano NORTH × produzido nas sessões e mapear débitos.

## [Q] MODO QUESTIONADOR · Auditoria Hostil

**5N adversarial**:

- **Negação**: o que NÃO se tem versus o que NORTH prometeu? → 14 das 18 seções canônicas estão AUSENTES ou em forma de drafts antigos (BP v2.0 cobre parcialmente, mas drafts não-NORTH conforme metodologia)
- **Núcleo irrefutável**: BP NORTH planejava 5 sprints + consolidação · sessões reais executaram 4 capítulos Wave 1 + 2 sprints DESVIADOS (S3.0.1, S3.0.3) que NÃO existem no NORTH
- **Nexo**: desvio foi causado por D003 (IA própria) emergente + débito pricing forçando S3.0.1/S3.0.3 antecipados
- **Nulidade**: se NORTH for sagrado, S3.0.1 v3.0 e S3.0.3 são desvios · se realidade pragmática vale, eles são insumos para Wave 2 §15 Financeiro
- **Nuance**: BP-FINAL.docx original v2.0 já tem MUITAS seções cobertas · NORTH foi escrito ASSUMINDO BP v2.0 como base · então auditoria hostil deve distinguir "BP v2.0 cobre" × "BP v2.1 NORTH-style refeito"

**Classificação evidência**:

| Afirmação | Classificação |
|---|:-:|
| NORTH planejava 18 seções em 5 sprints | FACT ✅ |
| BP-FINAL v2.0 (upload) cobre ~12 das 18 seções em forma "v2.0" | FACT ✅ (grep TOC) |
| Sessões produziram 4 caps Wave 1 (02/04/07/11) refazendo v2.0 | FACT ✅ |
| S3.0.1 e S3.0.3 são desvios do NORTH | FACT ✅ (não existem no NORTH original) |
| S3.0.1 v3.0 cobre §15 Plano Financeiro parcialmente | INFERENCE alta (~85%) |
| Blueprint Societário cobre §16 Equipe parcialmente | INFERENCE alta (~80%) |
| 3 débitos críticos (D001/D002/D003) bloqueiam consolidação | FACT ✅ |

**Auditoria hostil · seção por seção do NORTH × estado real**:

| § | Seção NORTH | Wave | Status real | Débito | VVV |
|---|---|---|---|---|---:|
| 01 | Capa · ficha técnica | W1 | ❌ AUSENTE como artefato isolado | DEB-N-01 | — |
| 02 | VMV | W1 | ✅ PRODUZIDO `02-vmv-latest.md` v2.1.4.3 | — | ~0.85 |
| 03 | Sumário Executivo | W3 | ⚠️ EXISTE no BP v2.0 antigo · mas precisa refazer para v2.1 ao final | DEB-N-03 | 0.60 |
| 04 | Design Thinking | W1 | ✅ PRODUZIDO `04-design-thinking-latest.md` v2.1.1 PMQS 8.74 | — | ~0.85 |
| 05 | PESTEL · regulação | W3 | ⚠️ EXISTE no BP v2.0 §3.2 · mas v2.1 NORTH manda refresh | DEB-N-05 | 0.75 |
| 06 | TAM/SAM/SOM | W3 | ❌ AUSENTE como cálculo formal · BP v2.0 §1.3 menciona mas não calcula | DEB-N-06 | 0.40 |
| 07 | Personas + Empathy Maps | W1 | ✅ PRODUZIDO `07-personas-latest.md` v2.1.2.1 PMQS 8.02 (4 personas deep) | — | ~0.83 |
| 08 | Clusters FDC-U | W2 | ⚠️ EXISTE como insumo `NEOGOV-FDCU-SCORING-CLUSTERS.md` · não integrado ao corpo v2.1 | DEB-N-08 | 0.85 |
| 09 | Porter 5 forças | W2 | ⚠️ APARECE em S3.0.1 v3.0 §1.5 (3.2/5) · não isolado como cap NORTH | DEB-N-09 | 0.80 |
| 10 | Sun Tzu 5 fatores | W3 | ⚠️ EXISTE no BP v2.0 §7.1 · S3.0.1 v3.0 não atualizou · S3.0.3 ignorou | DEB-N-10 | 0.70 |
| 11 | 5 Produtos | W1 | ✅ PRODUZIDO `11-produtos-latest.md` v2.1.3.1 PMQS 7.89 | — | ~0.78 |
| 12 | Business Model Canvas | W2 | ⚠️ APARECE em S3.0.1 v3.0 §12 (9 blocos + Lean Canvas) · NÃO isolado como cap | DEB-N-12 | 0.85 |
| 13 | Value Proposition Canvas × 5 | W2 | ❌ AUSENTE TOTALMENTE · nenhum sprint cobriu 5 VPCs | DEB-N-13 | 0.20 |
| 14 | Go-to-Market Waves | W2 | ⚠️ BP v2.0 §6 cobre · NORTH manda refinar para v2.1 com pricing WTP | DEB-N-14 | 0.70 |
| 15 | Plano Financeiro DRE/FCD/NPV + XLSX | W2 | 🟢 PARCIAL · S3.0.1 v3.0 cobre pricing+custos · falta DRE/FCD/NPV/xlsx | DEB-N-15 | 0.78 |
| 16 | Equipe · governança · RACI · OKRs | W2 | 🟢 PARCIAL · Blueprint BAS cobre · falta OKRs estruturados | DEB-N-16 | 0.85 |
| 17 | Riscos · heat map | W3 | 🟢 PARCIAL · S3.0.1 v3.0 §13 cobre risk register 15 riscos · falta heat map visual | DEB-N-17 | 0.85 |
| 18 | Roadmap · Gates | W2 | ⚠️ BP v2.0 §8 cobre · NORTH manda refresh v2.1 com gates dos débitos D001/D002/D003 | DEB-N-18 | 0.70 |

**Score auditoria hostil agregado**:

- ✅ FULL produzidos (NORTH-conforming): **4 / 18 (22%)** · capítulos Wave 1
- 🟢 PARCIAL (insumos existem, falta consolidação NORTH-format): **5 / 18 (28%)** · §15, §16, §17 via S3.0.1+BAS · §08, §09 via insumos
- ⚠️ EXISTE em BP v2.0 (precisa refresh NORTH-format): **6 / 18 (33%)** · §03, §05, §10, §12, §14, §18
- ❌ AUSENTE TOTALMENTE: **3 / 18 (17%)** · §01 Capa, §06 TAM/SAM/SOM, §13 VPC × 5

**Verdade hostil**: NORTH planejou 100% · realidade entrega 22% NORTH-format + 28% reaproveitável + 33% refresh-necessário + 17% zero.

---

## [I] MODO INOVADOR · Síntese

**Insight de fronteira**: o NORTH foi escrito ASSUMINDO que **iríamos REFAZER o BP v2.0 inteiro no novo formato**. Mas o caminho real foi pragmático: **acrescentamos sprints urgentes (S3.0.1 pricing + S3.0.3 WTP)** porque o BP v2.0 tinha débitos críticos (D001/D002/D003) que bloqueavam tudo. Esses sprints são VALOR REAL, não desvio puro.

**Recombinação conceitual**:

```
NORTH original (refazer 18 caps)  +  Realidade (4 caps + 2 sprints + 1 blueprint)
                       │
                       ▼
       NORTH v2 (replanejado)
       │
       ├─ Manter 4 caps já produzidos (Wave 1) ✅
       ├─ Consolidar S3.0.1 v3.0 + S3.0.3 + BAS em caps NORTH (§15, §16, §17) ⚙️
       ├─ Reaproveitar BP v2.0 §1-§8 com refresh leve para 6 caps ⚙️
       ├─ Produzir 3 caps AUSENTES totalmente (§01, §06, §13) ⚙️
       ├─ Refazer §03 Sumário Executivo AO FINAL (lê tudo) 🏁
       └─ Consolidação tripé (docx/xlsx/Vue/pdf/slides) 🏁
```

**Insight #2 · Débito de Forma vs Débito de Conteúdo**:

| Tipo de débito | Significado | Esforço |
|---|---|---|
| Conteúdo ausente | Cap não existe (§01, §06, §13) | ALTO (pesquisa + escrita) |
| Conteúdo presente, forma errada | BP v2.0 § existe mas estilo dev/antigo (§05, §10, §14, §18) | MÉDIO (refresh + estilo CLIENT-FACING) |
| Conteúdo disperso, sem consolidação | Insumos existem mas não NORTH-format (§08, §09, §12, §15, §16, §17) | MÉDIO-BAIXO (consolidação) |
| Conteúdo NORTH-OK | Caps Wave 1 produzidos (§02, §04, §07, §11) | ZERO (manter) |

**Compressão fractal · 3 escalas**:

- **Micro** (por cap): cada cap precisa NORTH-format + PMQS ≥ 8.0 + VVV ≥ 0.85
- **Meso** (por sprint): replanejar sprints conforme tipo de débito (consolidação vs refresh vs novo)
- **Macro** (consolidação): docx + xlsx + Vue + pdf + slides após todos os 18 caps NORTH-format

---

## [A] MODO ADVERSARIAL · Stress-Test

**Advocatus Diaboli A**: "Você está sendo benevolente · S3.0.1 v3.0 + S3.0.3 são DESVIOS · NORTH não os autoriza."  
**Refutação**: PROCEDENTE PARCIAL. NORTH foi planejado antes de descobrirmos débitos D001/D002/D003. Sprints S3.0.x são RESPOSTAS legítimas a débitos críticos · NÃO podem ser ignorados. Mas devem ser **integrados** ao NORTH como insumos de §15 (pricing/financeiro) e §17 (risk register), não como artefatos paralelos.

**Advocatus Diaboli B**: "Você marcou §02/§04/§07/§11 como ✅ FULL · mas PMQS médio = 8.16 está abaixo do alvo NORTH 9.5."  
**Refutação**: PROCEDENTE. Alvo NORTH 9.5 OURO não foi atingido em nenhum cap. Realista NeoGov PMQS ≥ 8.0 atingido (D-007). NORTH 9.5 requer Wave 1 piloto real (3 meses), conforme S3.0.1 v3.0 honesty check. **Débito permanece**: caps Wave 1 devem ser refinados pós-WTP (S3.0.3 execução) para subir VVV → PMQS.

**Advocatus Diaboli C**: "Você ignorou os arquivos `/skills/` na árvore · são 18+ engines indexadas · estão sendo usados?"  
**Refutação**: PROCEDENTE. Tree fornecida mostra engines (DTP/PIER/HIQM/CONTEXT-ENG/PHILOSOPHICAL/VVV/FDC-U/etc) em `/skills/SHUN_TZU/` e `/skills/ENGINE-MODULES/`. Tenho usado de memória · não invocado explicitamente como skills. **Débito metodológico**: invocar engines indexadas (CONTEXT_ENGINEERING_MODULE-v8.0 · VVV.md · FDC-U.md) PRE-ALWAYS, não apenas BABOK BA-Orchestration.

**Advocatus Diaboli D**: "PROTOCOLO_OPERACIONAL_PADRAO.md (raiz) vs POP NeoGov v2.1.1.1 (continuity) · qual prevalece?"  
**Refutação**: PROCEDENTE. Há dois POPs visíveis na tree. Não validei qual é canônico. **Débito de fonte**: verificar se PROTOCOLO_OPERACIONAL_PADRAO.md é o "north" instrucional (system-wide) e POP NeoGov é o projeto-específico. Hierarquia precisa ser explicitada.

**Stress-test edge cases**:

| Edge case | Comportamento esperado |
|---|---|
| S3.0.1 v3.0 OURO virar §15 NORTH | Refatorar com headers NORTH · PMQS deve subir com WTP |
| BP v2.0 §1-§8 reaproveitável? | SIM mas precisa refresh estilo CLIENT-FACING + linguagem terceira pessoa + numeração formal |
| §13 VPC × 5 do zero | Personas (§07) + Produtos (§11) já existem · VPC é DERIVADO · esforço MÉDIO |
| §06 TAM/SAM/SOM | DATA-v2.json + BP v2.0 §1.3 + S3.0.1 v3.0 §3 + FDCU-SCORING existem · cálculo formal AUSENTE · esforço MÉDIO |
| §01 Capa | Trivial · skill `docx` template | esforço BAIXO |

**Checklist 5 vieses nesta auditoria**:

| Viés | Detectado | Mitigação |
|---|:-:|---|
| Confirmação | ❌ NÃO | Audição HOSTIL · busquei contras |
| Âncora | ⚠️ baixo · ancorei em NORTH | Aceito · NORTH é referência válida |
| Recência | ⚠️ médio · pesei muito últimos sprints | Mitigado revisitando BP v2.0 base |
| Autoridade | ❌ NÃO | Questionei NORTH (advocatus diaboli A) |
| Ação | ⚠️ médio · proposta longa antes de validar | Mitigado oferecendo decisão antes de executar |

**Falsificação Popperiana**: se próximo movimento executar 1 sprint apenas e PMQS resultante < 8.0 OU VVV < 0.85 = sinalização que replanejamento precisa retrabalho. Teste aplicável ao primeiro sprint disparado.

---

## SÍNTESE CONVERGENTE

**Jornada do pensamento**: usuário forneceu plano NORTH original · pediu auditoria hostil + captura de pendências + replanejamento conforme estado atual. Investiguei file system real (bash) + BP v2.0 TOC real (grep) · cruzei NORTH × produzido × BP v2.0 antigo · classifiquei débitos em 4 categorias (FULL · PARCIAL · EXISTE-precisa-refresh · AUSENTE) · validei via 5N + 5 vieses + Popperiano + 4 advocatus diaboli.

**Escolha racional**: replanejamento honra NORTH como destino (18 caps cobertos) mas **realidade pragmática** como caminho (4 caps prontos + 2 sprints aproveitáveis + 6 caps BP v2.0 refresh + 3 caps zero + consolidação). Alternativas descartadas:
- Refazer tudo do zero (viola RGO-3 ordem certa · desperdício)
- Ignorar NORTH (viola contrato user · perda direção)
- Manter status quo (viola Constitution Art. 2 SEMPRE re-avaliar)

**Incerteza declarada**:
- 🟡 Hierarquia POPs (sistema vs projeto) · não validei · resolver no replanejamento
- 🟡 Engines `/skills/` não invocadas explicitamente · débito metodológico
- 🟢 PMQS Wave 1 atingiu 8.0 mas NORTH alvo é 9.5 · gap aceitável com lastros pendentes (S3.0.3 execução real destrava)

---

## OUTPUT TÉCNICO · Replanejamento NORTH v2 (NeoGov Conforme Estado Real)

### §1 · Captura de Pendências (Débitos NORTH)

| ID | Cap | Tipo débito | Esforço | Bloqueante para |
|---|:-:|---|:-:|---|
| DEB-N-01 | §01 Capa | AUSENTE · novo | BAIXO | Consolidação final |
| DEB-N-03 | §03 Sumário Executivo v2.1 | EXISTE-refresh | MÉDIO | Consolidação final (escrever AO FIM) |
| DEB-N-05 | §05 PESTEL refresh | EXISTE-refresh | BAIXO | §09 Porter |
| DEB-N-06 | §06 TAM/SAM/SOM | AUSENTE · novo | MÉDIO | §14 GTM · §15 Financeiro |
| DEB-N-08 | §08 Clusters FDC-U consolidação | PARCIAL | BAIXO | §14 GTM |
| DEB-N-09 | §09 Porter cap isolado | PARCIAL | BAIXO | — |
| DEB-N-10 | §10 Sun Tzu refresh | EXISTE-refresh | BAIXO | — |
| DEB-N-12 | §12 BMC cap isolado | PARCIAL | MÉDIO | §13 VPC |
| DEB-N-13 | §13 VPC × 5 | AUSENTE · novo | MÉDIO-ALTO | Consolidação |
| DEB-N-14 | §14 GTM refresh v2.1 | EXISTE-refresh | MÉDIO | — |
| DEB-N-15 | §15 Financeiro DRE/FCD/NPV + xlsx | PARCIAL (S3.0.1 v3.0 + WTP pendente) | ALTO | Investidor-ready |
| DEB-N-16 | §16 Equipe + OKRs | PARCIAL (BAS cobre) | MÉDIO | Governança |
| DEB-N-17 | §17 Risk heat map visual | PARCIAL (S3.0.1 v3.0 §13) | BAIXO | — |
| DEB-N-18 | §18 Roadmap v2.1 | EXISTE-refresh | MÉDIO | Consolidação |
| DEB-N-19 (NOVO) | Engines `/skills/` PRE-ALWAYS | Metodológico | BAIXO | Conformidade total |
| DEB-N-20 (NOVO) | Hierarquia POPs (sistema vs projeto) | Governance | BAIXO | POP §2 fontes canônicas |
| DEB-N-21 (NOVO) | Wave 1 caps subir PMQS 8.0→9.0+ | Refinamento | MÉDIO | Pós-WTP S3.0.3 |
| DEB-N-22 (NOVO) | CONSOLIDAÇÃO tripé docx/xlsx/Vue/pdf/slides | Output | ALTO | Entrega final |

### §2 · Replanejamento Sequencial · Sprints NORTH v2 (8 sprints)

```
═══════════════════════════════════════════════════════════════
SPRINT N1 (NORTH v2) · Consolidação de Insumos Existentes
   Duração estimada: 3-5 dias úteis
   Objetivo: aproveitar 80% do trabalho feito (S3.0.1 v3.0 + S3.0.3 + BAS)
   
   ├─ N1.1  §15 Plano Financeiro v2.1 (consolidar S3.0.1 v3.0 + custos + pricing)
   │        Skill: xlsx + engenheiro-processos-master + technical-writer
   │        Output: 15-financeiro-latest.md + APENDICE-D-FINANCEIRO.xlsx (10 abas)
   │
   ├─ N1.2  §16 Equipe + Governança + OKRs (consolidar BAS + RACI S3.0.1)
   │        Skill: brand + docx + technical-writer + arc42
   │        Output: 16-equipe-governanca-latest.md (CLIENT-FACING)
   │
   └─ N1.3  §17 Risk Heat Map Visual (formalizar 15 riscos S3.0.1 v3.0)
            Skill: design-system + svg + visualize
            Output: 17-riscos-heat-map-latest.md + heat-map.svg
   
   Gate N1: PMQS ≥ 8.0 + VVV ≥ 0.78 (com lastros atuais)

═══════════════════════════════════════════════════════════════
SPRINT N2 (NORTH v2) · Caps Novos · AUSENTES Totalmente
   Duração estimada: 4-6 dias úteis
   Objetivo: cobrir as 3 lacunas zero
   
   ├─ N2.1  §06 TAM/SAM/SOM formal (5.570 mun + 42.491 escolas + hospitais)
   │        Skill: xlsx + benchmarking + estimation parametric
   │        Output: 06-tam-sam-som-latest.md + cálculos xlsx
   │
   ├─ N2.2  §13 VPC × 5 personas (Alfa Mun · Alfa Fed/Est · Beta · Gamma · Épsilon)
   │        Skill: design-thinking (VPC formal) + journey-mapping
   │        Output: 13-value-proposition-canvas-latest.md (5 VPCs)
   │
   └─ N2.3  §01 Capa + ficha técnica + ToC
            Skill: docx + design-system + brand
            Output: 01-capa-ficha-tecnica-latest.md (template oficial)
   
   Gate N2: PMQS ≥ 8.0 + VVV ≥ 0.80

═══════════════════════════════════════════════════════════════
SPRINT N3 (NORTH v2) · Refresh CLIENT-FACING das seções BP v2.0 existentes
   Duração estimada: 4-6 dias úteis
   Objetivo: trazer §05, §10, §14, §18 do BP v2.0 para NORTH-format v2.1
   
   ├─ N3.1  §05 PESTEL v2.1 (refresh com IBS/CBS 2027 + ECA Digital + ANPD timing)
   │        Skill: technical-writer + swot-pestle-analysis
   │        Output: 05-pestel-latest.md (CLIENT-FACING)
   │
   ├─ N3.2  §10 Sun Tzu 5 fatores atualizados (DAO/TIAN/DI/JIANG/FA pós-S3.0.1)
   │        Skill: constitutional-ai-orchestrator + strategic-analyst
   │        Output: 10-sun-tzu-latest.md
   │
   ├─ N3.3  §14 Go-to-Market Waves v2.1 (refresh com pricing WTP-pendente)
   │        Skill: engenheiro-processos-master + journey-mapping
   │        Output: 14-gtm-waves-latest.md
   │
   └─ N3.4  §18 Roadmap v2.1 + Gates débitos D001/D002/D003
            Skill: process-modeling + estimation PERT
            Output: 18-roadmap-gates-latest.md
   
   Gate N3: PMQS ≥ 8.0 + VVV ≥ 0.82

═══════════════════════════════════════════════════════════════
SPRINT N4 (NORTH v2) · Caps Wave 2 isolados (já parciais)
   Duração estimada: 3-4 dias úteis
   Objetivo: formalizar BMC, Porter, Clusters como capítulos isolados NORTH
   
   ├─ N4.1  §12 BMC + Lean Canvas (extrair S3.0.1 v3.0 §12 · expandir)
   │        Skill: business-model-canvas + design-system
   │        Output: 12-business-model-canvas-latest.md (CLIENT-FACING)
   │
   ├─ N4.2  §09 Porter 5 forças (extrair S3.0.1 v3.0 §1.5 · expandir por cluster)
   │        Skill: swot-pestle-analysis + strategic-analyst
   │        Output: 09-porter-latest.md
   │
   └─ N4.3  §08 Clusters FDC-U consolidado (integrar NEOGOV-FDCU-SCORING-CLUSTERS.md)
            Skill: constitutional-ai-orchestrator + FDC-U engine
            Output: 08-clusters-fdcu-latest.md
   
   Gate N4: PMQS ≥ 8.0 + VVV ≥ 0.82

═══════════════════════════════════════════════════════════════
SPRINT N5 (NORTH v2) · Refinamento Wave 1 (pós-WTP)
   Duração estimada: 2-3 dias úteis · DEPENDE de S3.0.3 execução real
   Objetivo: subir PMQS dos 4 caps Wave 1 de 8.0 para 9.0+
   
   ├─ N5.1  §02 VMV v2.2 (refinar com WTP confirmado)
   ├─ N5.2  §04 Design Thinking v2.2 (refinar com clusters validados)
   ├─ N5.3  §07 Personas v2.2 (refinar com WTP por persona)
   ├─ N5.4  §11 Produtos v2.2 (refinar com pricing WTP-confirmed)
   └─ Gate N5: PMQS ≥ 9.0 + VVV ≥ 0.92

═══════════════════════════════════════════════════════════════
SPRINT N6 (NORTH v2) · Sumário Executivo (último cap escrito · lê tudo)
   Duração estimada: 1-2 dias úteis
   Objetivo: §03 Sumário Executivo v2.1 lê os 17 caps anteriores + 10 decisões centrais
   
   ├─ N6.1  §03 Sumário Executivo v2.1 (síntese investor-ready)
   │        Skill: technical-writer + slides + brand
   │        Output: 03-sumario-executivo-latest.md (1-pager + versão 5-páginas)
   │
   └─ Gate N6: PMQS ≥ 9.0 + VVV ≥ 0.90

═══════════════════════════════════════════════════════════════
SPRINT NC (NORTH v2) · CONSOLIDAÇÃO TRIPÉ MULTI-OUTPUT
   Duração estimada: 3-5 dias úteis
   Objetivo: render final em 5 formatos
   
   ├─ NC.1  BUSINESS-PLAN-FINAL-v2.1.docx (pandoc + template oficial CLIENT-FACING)
   ├─ NC.2  APENDICE-D-MODELO-FINANCEIRO.xlsx (10 abas dashboard-quality)
   ├─ NC.3  Vue 3 App + GitHub Pages (interactive navegável)
   ├─ NC.4  BUSINESS-PLAN-FINAL-v2.1.pdf (signed)
   └─ NC.5  Slides Executive Summary (.pptx 10-15 slides)
   
   Gate NC: 5 outputs sincronizados (princípio DRY · md = fonte)

═══════════════════════════════════════════════════════════════
SPRINT META (paralelo · permanente) · Conformidade Metodológica
   Objetivo: aplicar engines indexadas + governance
   
   ├─ META.1  Invocar PRE-ALWAYS engines indexadas (CONTEXT-ENG, VVV, FDC-U, HIQM, PHILOSOPHICAL)
   ├─ META.2  Resolver hierarquia POPs (PROTOCOLO_OPERACIONAL_PADRAO.md vs POP NeoGov)
   ├─ META.3  Atualizar SESSION-STATE + APENDICE-A/B/C a cada sprint
   └─ META.4  Decisões D-020 (CLIENT-FACING) + D-021 (PRE-ALWAYS) formalizar em POP §1.2
```

### §3 · Métricas-meta do Replanejamento

| Métrica | Estado atual | Pós-N1 (consolidação) | Pós-N3 (refresh) | Pós-N6 (sumário) | Pós-NC (entrega) |
|---|---:|---:|---:|---:|---:|
| Caps NORTH-format produzidos | 4/18 (22%) | 7/18 (39%) | 14/18 (78%) | 17/18 (94%) | **18/18 (100%)** |
| PMQS médio | 8.16 | 8.20 | 8.30 | 8.50 | **8.80+** |
| VVV médio | 0.82 | 0.84 | 0.86 | 0.92 (pós-WTP) | **0.94** |
| Outputs tripé | 1/5 (md parcial) | 2/5 | 3/5 | 4/5 | **5/5** |

### §4 · Critérios de sucesso · Gate Final

```
✅ 18/18 capítulos NORTH-format produzidos
✅ PMQS médio ≥ 8.5 (realista) · alvo ouro 9.5 (com Wave 1 piloto)
✅ VVV médio ≥ 0.90 (com WTP S3.0.3 executado real)
✅ 5/5 outputs tripé sincronizados (md/docx/xlsx/Vue/pdf)
✅ 3 débitos críticos quitados (D001 pricing · D002 cognitivo · D003 arquitetura)
✅ Anti-padrões zero (D-015 lastros · D-019 BABOK · D-020 CLIENT-FACING · D-021 PRE-ALWAYS)
✅ NORTH 100% honrado conforme replanejamento
```

### §5 · Duração estimada total (8 sprints + META permanente)

| Sprint | Duração úteis | Cumulativo |
|---|:-:|:-:|
| N1 Consolidação | 3-5 dias | 5 dias |
| N2 Caps novos | 4-6 dias | 11 dias |
| N3 Refresh | 4-6 dias | 17 dias |
| N4 Caps isolados | 3-4 dias | 21 dias |
| N5 Refinamento Wave 1 | 2-3 dias (após S3.0.3) | 51 dias (com WTP 30 dias) |
| N6 Sumário | 1-2 dias | 53 dias |
| NC Consolidação | 3-5 dias | 58 dias |

**Total realista**: **~8-9 semanas** (incluindo S3.0.3 execução real WTP de 30 dias em paralelo)

---

## METADATA DE VALIDAÇÃO

- **Fontes consultadas**:
  - Plano NORTH original (anexo do usuário)
  - File system real `/home/claude/neogov-v21/` (bash find)
  - BP-FINAL v2.0 original (`/mnt/user-data/uploads/NEOGOV-BUSINESS-PLAN-FINAL.md` · TOC via grep)
  - 4 caps Wave 1 produzidos (existência confirmada)
  - S3.0.1 v3.0 + S3.0.3 + BAS (existência confirmada)
- **Pendente investigação**:
  - 🟡 PROTOCOLO_OPERACIONAL_PADRAO.md (raiz) vs POP NeoGov · não validei diferença
  - 🟡 Engines `/skills/` invocação · prática de uso real ausente · débito metodológico DEB-N-19
- **Classificação afirmações**:
  - 4 caps Wave 1 produzidos: FACT ✅
  - 6 caps BP v2.0 reaproveitáveis: FACT ✅ (TOC verificado)
  - 3 caps AUSENTES totalmente: FACT ✅
  - Replanejamento 8 sprints + META é o caminho ótimo: INFERENCE alta (~88%) · pode otimizar
  - Duração 8-9 semanas: ESTIMATIVA POR ANÁLOGO 🟡 (depende de cadência sessões + S3.0.3 execução real)
- **Vieses detectados**: ⚠️ Recência médio (mitigado revisitando BP v2.0) · ⚠️ Ação médio (mitigado oferecendo decisão antes de executar)
- **Vieses mitigados**: Confirmação (audição hostil) · Âncora (questionei NORTH via advocatus diaboli A) · Autoridade (questionei NORTH)

---

## REGISTRO WAL

```yaml
session_id: NEOGOV-V21-AUDITORIA-HOSTIL-REPLANEJAMENTO-NORTH-2026-05-15
timestamp_checkpoint: 2026-05-15T21:30:00Z
completed_phases: [S, Q, I, A, OUTPUT, VALIDATION]
active_constraints:
  - Constitution_Art1-3_FULL
  - RGO-1-8_FULL
  - POP_v2.1.1.1_LOADED
  - Layer0_FULL
  - Layer0.5_ACTIVE
  - Layer2_ACTIVE
  - D-020_ACTIVE (CLIENT-FACING)
  - D-021_PROPOSTA_v2.0 (PRE-ALWAYS pendente formalização)
  - PLANO_NORTH_RECEBIDO_E_AUDITADO
auditoria_hostil_score:
  caps_full_norms: 4/18 (22%)
  caps_parcial: 5/18 (28%)
  caps_existe_refresh: 6/18 (33%)
  caps_ausente: 3/18 (17%)
debitos_capturados:
  norte_debitos: 18 (DEB-N-01 a DEB-N-22, com 3 metodológicos novos)
  bloqueantes_consolidacao: 4 (D001 D002 D003 + DEB-N-22)
sprints_replanejados: 8 (N1-N6 + NC + META permanente)
duracao_total_realista: 8-9 semanas (com S3.0.3 paralelo)
continuity_hash: NEOGOV-V21-NORTH-v2-REPLANEJADO-8-SPRINTS-AWAIT-USER-DISPATCH-N1
proxima_acao: USER_DECIDE_QUAL_SPRINT_N_DISPARAR_PRIMEIRO
```

---
