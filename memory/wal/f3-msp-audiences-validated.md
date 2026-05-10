# Audiences Validadas via OMNIBUS MSP
**Timestamp**: 2026-05-09T00:00:00-03:00
**QUALITY_CoT**: 8.00
**Método**: shuntzu-f3 MSP Phase 1+2 | S→Q→I→A completo | 10 fontes lidas | 40 menções verbatim

---

## Audiences Aprovadas (para substituir JSON atual)

### Audience 1: b2g_consorcios
- **Nome**: Consórcios Intermunicipais (CIGA, CIMINAS, Granbel e similares)
- **Descrição**: Entidades interfederativas que coordenam serviços compartilhados para 5-30+ municípios membros. São simultaneamente canal de distribuição (vendem ao consórcio → acesso a N municípios) e cliente direto (o consórcio quer oferecer LGPD como serviço para seus membros). Modelo white-label ou ARP (Ata de Registro de Preços) elimina licitação individual por prefeitura. CIGA: 345 municípios, 100% de SC. CIMINAS: credenciamento R$31.9M LGPD 2025.
- **VVV**: 0.90
- **Fonte**: `market-research-2025.md:§Consortium` + `inteligencia-mercado-govtech-lgpd.md:§Canais L91` + `transcricao-insights.json:go_to_market L229` + `strategic-data-unified.json:b2g_consorcios`
- **Power-Interest**: MANAGE CLOSELY (alto poder sobre N municípios, alto interesse em resolver LGPD de todos membros)
- **FDC-U Score**: 7.99 (Rank #1)
- **Custom Weights Sun Tzu sugeridos**: {dao: 0.25, ceu: 0.15, terra: 0.20, comandante: 0.25, metodo: 0.15}
- **Justificativa pesos**:
  - `dao` alto (0.25): Missão do consórcio é servir municípios — alinhamento de propósito é crítico. Consórcio sem propósito claro rompe o acordo
  - `ceu` médio-baixo (0.15): Sazonalidade orçamentária importa mas consórcio tem ciclo próprio mais estável que prefeitura individual
  - `terra` médio (0.20): Terreno favorável — modelo ARP e Lei 11.107/2005 habilitam a compra. Mas terreno tem armadilha de lock-in
  - `comandante` alto (0.25): O Diretor Executivo do consórcio é o comandante decisivo — relação pessoal com ele é determinante para o fechamento
  - `metodo` médio (0.15): Método de entrega white-label deve ser robusto mas não é o diferencial primário

---

### Audience 2: b2g_prefeituras_medio
- **Nome**: Prefeituras de Médio Porte (20-100K habitantes) — SAM Core
- **Descrição**: ~1.200 municípios brasileiros com orçamento disponível (R$15-50K/ano) mas sem equipe técnica interna para LGPD. São o target direto do Dispensa Art.75 IV c/d que permite contratação ICT sem licitação complexa. Urgência regulatória real: ANPD + TCEs em fiscalização ativa, 8.700+ queixas de titulares registradas em 2025. Inclui persona ECA-urgent (secretarias de educação com dados de crianças pós-Lei 15.211/2025) como especialização interna. Procurador municipal é o campeão interno obrigatório — modelo de parecer jurídico pronto é killer feature para desbloquear essa audience.
- **VVV**: 0.95
- **Fonte**: `inteligencia-mercado-govtech-lgpd.md:§Dimensionamento L35` + `IBGE MUNIC 2024 (VVV 1.0)` + `transcricao-insights.json:oportunidades L113` + `market-research-2025.md:§IBGE §7` + `swot-transcricao.yaml:O2`
- **Power-Interest**: MANAGE CLOSELY (poder de contratar diretamente + interesse urgente pós-fiscalização TCE/ANPD)
- **FDC-U Score**: 7.64 (Rank #2)
- **Custom Weights Sun Tzu sugeridos**: {dao: 0.15, ceu: 0.25, terra: 0.30, comandante: 0.20, metodo: 0.10}
- **Justificativa pesos**:
  - `dao` baixo (0.15): Prefeito não age por propósito estratégico — age por pressão/risco. Dao menos relevante que ceu e terra
  - `ceu` alto (0.25): Timing importa muito — LDO/LOA cycle, eleições 2028, janela ANPD enforcement. Entrar no momento errado = processo parado
  - `terra` alto (0.30): Terreno favorável é a vantagem ICT — Art.75 IV, OSCIP, recursos carimbados. Terra é o diferencial insuperável nessa audience
  - `comandante` médio (0.20): Prefeito + Procurador são os dois comandantes decisivos. Duplo-nível de aprovação
  - `metodo` baixo (0.10): O método de entrega (SaaS self-service) é importante mas secundário ao legal/political

---

### Audience 3: b2g_micro_municipios
- **Nome**: Micro-municípios (menos de 10K habitantes) — Espaço Branco
- **Descrição**: ~1.000 municípios com taxa de adequação de 19.8% (menor de todos os portes — IBGE MUNIC 2024). Único segmento onde Confidata não compete (starter R$497/mês = inacessível). Pricing CIT AI Tech a R$297/mês = R$3.564/ano fica abaixo do threshold de Dispensa Art.75 II (até R$50K), permitindo compra simplificada imediata. Secretário acumula múltiplas funções (saúde + educação + administração) — solução "all-in-one" de baixo esforço é proposta de valor máxima. Canal via AMM/associações municipais estaduais (1 evento = 50+ municípios qualificados).
- **VVV**: 0.85
- **Fonte**: `executive-summary.md:§Segmentação L152 + §Pricing Matrix L224` + `IBGE MUNIC 2024 (VVV 1.0)` + `market-research-2025.md:§IBGE §7 L340`
- **Power-Interest**: MANAGE CLOSELY (pequeno poder individual mas interesse urgente; alto poder coletivo via associações)
- **FDC-U Score**: 7.10 (Rank #3, revisado +0.25 após adversarial por oportunidade subestimada)
- **Custom Weights Sun Tzu sugeridos**: {dao: 0.10, ceu: 0.20, terra: 0.25, comandante: 0.15, metodo: 0.30}
- **Justificativa pesos**:
  - `dao` mínimo (0.10): Micro-prefeito não raciocina estrategicamente — age por obrigação e simplicidade
  - `ceu` médio (0.20): Timing crítico via ciclo orçamentário e eventos de associações
  - `terra` médio-alto (0.25): Terreno é favorável (Art.75 II, threshold baixo) mas acesso ao município individual é difícil
  - `comandante` baixo (0.15): Decisor é o próprio prefeito sem mediadores — simples mas com tempo limitado
  - `metodo` alto (0.30): Para esse segmento, o método de entrega (self-service, zero suporte técnico, onboarding em 1 dia) é o diferencial decisivo

---

### Audience 4: b2b_advocacia_whitlabel
- **Nome**: Escritórios de Advocacia Pequenos (1-5 advogados) — Canal White-label
- **Descrição**: Escritórios de advocacia pequenos que assessoram prefeituras e órgãos públicos em licitações e compliance, mas que não têm capacidade de desenvolver solução tecnológica própria. Interesse em white-label para agregar valor aos clientes municipais existentes. Modelo: comissão de 15-20% por cliente indicado + white-label com marca do escritório. Diferente dos grandes escritórios de boutique (PLM, Rayes e Fagundes) que são competidores — focar em escritórios regionais sem produto tecnológico. Fonte de acesso: OAB estadual, eventos de direito público, associações de procuradores municipais.
- **VVV**: 0.70
- **Fonte**: `executive-summary.md:§SWOT O4 L28` + `inteligencia-mercado-govtech-lgpd.md:§Players L44` + `market-research-2025.md:§Competitor tabela L213`
- **Power-Interest**: KEEP INFORMED (poder moderado como influenciadores nos municípios clientes, interesse alto em incrementar receita de compliance)
- **FDC-U Score**: 6.49 (Rank #4)
- **Custom Weights Sun Tzu sugeridos**: {dao: 0.20, ceu: 0.10, terra: 0.15, comandante: 0.30, metodo: 0.25}
- **Justificativa pesos**:
  - `dao` médio (0.20): Alinhamento de propósito é crítico — o escritório deve ver CIT AI Tech como aliado, não como competidor
  - `ceu` mínimo (0.10): Escritórios não têm sazonalidade forte para esse tipo de parceria
  - `terra` médio-baixo (0.15): Terreno é o mercado dos clientes municipais do escritório — importante mas não o driver
  - `comandante` alto (0.30): A relação pessoal com o sócio-fundador do escritório é determinante para onboarding de parceiro
  - `metodo` alto (0.25): O white-label deve ser tecnicamente impecável — bugs no sistema mancham a reputação do escritório com seus clientes

---

## Audiences Descartadas (não validadas para JSON atual)

| ID atual JSON | Diagnóstico | Destino |
|---------------|-------------|---------|
| `b2g_prefeituras` | Audience real mas muito ampla — inclui segmentos de porte muito diferente (micro vs médio vs grande). Substituir por 2 audiences específicas: `b2g_prefeituras_medio` e `b2g_micro_municipios` | Substituir por 2 |
| `b2b_fornecedores_municipio` | Evidência fraca no corpus: inferência sem dados primários validando urgência LGPD para fornecedores de municípios especificamente. Score FDC-U 5.38. Nenhuma menção específica na transcrição principal (1h39m reunião NeoGov) | Remover |
| `b2b_empresas_privadas` | Mercado competido (Confidata já serve com 17 módulos), sem vantagem diferencial da prerrogativa ICT. Score FDC-U 5.73. Executive-summary menciona como expansão futura "Fase 3+" | Remover (Fase 3+) |
| `b2g_estaduais` | Ciclo de venda extremamente lento (>18 meses), burocracia estadual fundamentalmente diferente do municipal, fora do SAM prioritário definido no corpus. Score FDC-U 5.00 | Remover |
| `b2g_consorcios` | MANTER — top scorer 7.99. Audience validada com evidências fortes | Manter e fortalecer |

---

## Recomendação de Substituição no JSON

### Estrutura proposta (5 audiences no JSON):

```json
"audiences": [
  { "id": "b2g_consorcios" },        // MANTER — rank #1, fortalecer dados
  { "id": "b2g_prefeituras_medio" }, // SUBSTITUIR b2g_prefeituras — rank #2
  { "id": "b2g_micro_municipios" },  // NOVO — substituir b2b_empresas_privadas — rank #3
  { "id": "b2b_advocacia_whitlabel"}, // NOVO — substituir b2g_estaduais — rank #4
  // 5ª audience: manter b2g_prefeituras_medio com persona ECA-urgent interna
  // OU expandir para 5 se decidir separar ECA Digital como audience explícita
]
```

### Operações concretas:
1. **`b2g_prefeituras`** → Renomear para `b2g_prefeituras_medio` + atualizar label, persona, weights, game_theory
2. **`b2g_consorcios`** → Manter ID + atualizar label e enriquecer com dados CIGA/CIMINAS validados
3. **`b2b_fornecedores_municipio`** → Deletar do JSON (evidência insuficiente)
4. **`b2b_empresas_privadas`** → Substituir por `b2g_micro_municipios` (novo segmento validado)
5. **`b2g_estaduais`** → Substituir por `b2b_advocacia_whitlabel` (novo segmento validado)

### Prioridade de ataque (ordem de execução):
- **P1**: `b2g_consorcios` (canal multiplica, score máximo)
- **P2**: `b2g_prefeituras_medio` (SAM core, máxima validação)
- **P3**: `b2g_micro_municipios` (espaço branco, zero competição)
- **P4**: `b2b_advocacia_whitlabel` (canal indireto, menor urgência)

---

## Rastreabilidade VVV por Audience

| Audience | VVV Fato Central | Fonte | Classificação |
|----------|-----------------|-------|---------------|
| b2g_consorcios | "credenciamento de R$31.9 milhões para serviços de adequação à LGPD para seus municípios consorciados" | `inteligencia-mercado-govtech-lgpd.md:§Canais L39-40` | FACT / VVV 0.90 |
| b2g_prefeituras_medio | "SAM prioritário... cidades de médio porte (entre 20 mil e 100 mil habitantes), onde existe orçamento para contratação, mas falta equipe técnica interna" | `inteligencia-mercado-govtech-lgpd.md:§Dimensionamento L35` | FACT / VVV 0.95 |
| b2g_micro_municipios | "Até 5.000 habitantes: 19.8% com Responsável LGPD" (IBGE MUNIC 2024) | `market-research-2025.md:§IBGE` | FACT / VVV 1.00 |
| b2b_advocacia_whitlabel | "White-label para escritórios advocacia" (SWOT O4) | `executive-summary.md:§SWOT O4` | FACT / VVV 0.70 |
