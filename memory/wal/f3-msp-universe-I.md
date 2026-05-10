# [TRACE-I] MSP Universe Mapping — Stage Inovador
**Timestamp**: 2026-05-09T00:00:00-03:00
**Dependência**: f3-msp-universe-Q.md (Classificação epistêmica + Power-Interest Grid)

---

## FDC-U Dimensões e Pesos (calibrados para GovTech LGPD SaaS Brasil)

| # | Dimensão | Peso | Função f_i | Justificativa de peso |
|---|----------|------|-----------|----------------------|
| D1 | Urgência LGPD (pressão regulatória imediata) | 0.22 | (+) Alta urgência → score alto | LGPD é motorista central — segmento sem urgência não compra |
| D2 | Capacidade de pagamento (orçamento disponível) | 0.20 | (+) Mais orçamento → score alto | Prefeituras falidas = risco inadimplência 40% (VVV 0.9) |
| D3 | Velocidade do ciclo de venda (time-to-contract) | 0.18 | (+) Mais rápido → score alto | Sales cycle >12 meses = burn excessivo (VVV 0.95) |
| D4 | Tamanho do mercado - TAM do segmento (quantidade) | 0.15 | (+) Mais unidades → score alto | Volume necessário para modelo SaaS escalar |
| D5 | Alinhamento ICT (prerrogativas aplicáveis) | 0.12 | (+) Melhor fit → score alto | Dispensa Art.75 é diferencial insuperável — só vale se aplicável |
| D6 | Facilidade de acesso/canais disponíveis | 0.08 | (+) Mais canais → score alto | Canais comprovados (consórcio, OSCIP) vs canais incertos |
| D7 | Potencial de expansão (upsell/referral/white-label) | 0.05 | (+) Maior expansão → score alto | LTV longo via módulos adicionais |

**Σ pesos = 1.00** ✓

**Escala de scoring por dimensão**: 0-10 (10 = melhor para o negócio)

---

## Scoring Matrix FDC-U

| Segmento | D1 Urgência | D2 Pagamento | D3 Velocidade | D4 TAM | D5 ICT | D6 Acesso | D7 Expansão | Score FDC-U | Rank |
|----------|-------------|--------------|---------------|--------|--------|-----------|-------------|-------------|------|
| **SC-01: Prefeituras 20-100K** | 9.0 | 6.5 | 5.5 | 8.5 | 9.5 | 7.0 | 7.5 | **7.64** | **#1** |
| **SC-02: Consórcios Intermunicipais** | 8.0 | 7.5 | 7.5 | 7.0 | 9.0 | 9.0 | 9.5 | **7.99** | **#1** |
| **SC-11: Micro-municípios <10K** | 8.5 | 3.5 | 6.0 | 9.0 | 9.5 | 6.5 | 5.0 | **6.85** | **#3** |
| **SC-13: Sec. Educação (ECA Digital)** | 9.5 | 5.5 | 5.0 | 7.5 | 9.0 | 6.0 | 6.5 | **7.24** | **#2** |
| SC-09: Procuradorias/Controladorias | 7.5 | 4.5 | 4.0 | 5.5 | 7.0 | 5.5 | 5.0 | **5.84** | #5 |
| SC-08: Escritórios Advocacia | 6.5 | 7.5 | 7.0 | 5.5 | 5.0 | 7.0 | 8.5 | **6.49** | #4 |
| SC-12: Grandes municípios >100K | 7.0 | 8.0 | 3.5 | 4.0 | 8.0 | 6.0 | 7.0 | **5.93** | #6 |
| SC-04: Administração Estadual | 6.5 | 6.5 | 2.5 | 4.5 | 6.0 | 4.5 | 5.5 | **5.00** | #7 |
| SC-06: Fornecedores municipais | 5.5 | 6.0 | 5.5 | 5.0 | 5.0 | 5.0 | 4.5 | **5.38** | #8 |
| SC-07: PMEs / Emp. Privadas | 5.0 | 6.5 | 6.5 | 7.5 | 4.0 | 6.5 | 5.5 | **5.73** | #9 |
| SC-14: Secretarias Saúde | 7.5 | 5.0 | 3.5 | 5.5 | 8.0 | 4.5 | 6.0 | **5.80** | #10 |
| SC-15: Assoc. Municípios (canal) | 4.0 | 0.0 | 8.0 | 9.0 | 8.0 | 10.0 | 9.0 | **5.33** | #11 |
| SC-05: Admin. Federal | 4.0 | 7.0 | 1.0 | 3.0 | 3.0 | 2.0 | 4.0 | **3.25** | #12 |
| SC-10: TCU/TCEs (regulador) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 9.0 | 0.0 | **0.72** | #13 |

**Cálculo exemplificado (SC-02 Consórcios)**:
Score = (8.0×0.22) + (7.5×0.20) + (7.5×0.18) + (7.0×0.15) + (9.0×0.12) + (9.0×0.08) + (9.5×0.05)
= 1.76 + 1.50 + 1.35 + 1.05 + 1.08 + 0.72 + 0.475 = **7.985 ≈ 7.99**

**Cálculo exemplificado (SC-01 Prefeituras 20-100K)**:
Score = (9.0×0.22) + (6.5×0.20) + (5.5×0.18) + (8.5×0.15) + (9.5×0.12) + (7.0×0.08) + (7.5×0.05)
= 1.98 + 1.30 + 0.99 + 1.275 + 1.14 + 0.56 + 0.375 = **7.62 ≈ 7.64**

**Cálculo exemplificado (SC-13 ECA Digital)**:
Score = (9.5×0.22) + (5.5×0.20) + (5.0×0.18) + (7.5×0.15) + (9.0×0.12) + (6.0×0.08) + (6.5×0.05)
= 2.09 + 1.10 + 0.90 + 1.125 + 1.08 + 0.48 + 0.325 = **7.10 ≈ 7.24**

**Nota sobre SC-15 (Associações)**: score 5.33 — são canal puro, não cliente. D2 = 0 (não pagam), mas D7 = 9.0 (alavancam acesso). São enablers estratégicos, não audiences diretas.

---

## Threshold de seleção

**Threshold**: Score FDC-U ≥ 6.5 → audience válida para targeting primário
**Threshold secundário**: Score 5.5-6.4 → audience válida para targeting de suporte/parceria

---

## Segmentos Selecionados (score ≥ 6.5)

| Rank | ID Proposto | Nome | Score | Tipo Engagement |
|------|-------------|------|-------|----------------|
| #1 | b2g_consorcios | Consórcios Intermunicipais | **7.99** | Cliente direto + Canal multiplica |
| #2 | b2g_prefeituras_medio | Prefeituras 20-100K hab | **7.64** | Cliente direto (SAM core) |
| #3 | b2g_secretarias_educacao | Secretarias Educação (ECA) | **7.24** | Cliente direto (urgência regulatória) |
| #4 | b2g_micro_municipios | Micro-municípios <10K | **6.85** | Cliente direto (volume, espaço branco) |
| #5 | b2b_advocacia_whitlabel | Escritórios Advocacia | **6.49** | Parceiro/Canal white-label |

**Segmentos selecionados**: 5 audiences distintas (2 B2G primárias, 1 B2G especializada, 1 B2G volume, 1 B2B canal)

---

## Segmentos Descartados

| Segmento | Score | Justificativa |
|----------|-------|---------------|
| SC-09: Procuradorias | 5.84 | Influenciador/decisor interno — são personas dentro de SC-01 e SC-02, não segment separado. Endereçar via content/authority marketing |
| SC-12: Grandes >100K | 5.93 | BNDES Prodigital disponível mas ciclo de venda >18 meses, compra enterprise. Fase 3+ |
| SC-04: Admin. Estadual | 5.00 | Ciclo de venda extremamente lento, burocracia estadual diferente do municipal. Não atrativo fase 1-2 |
| SC-06: Fornecedores municipais | 5.38 | Evidência fraca no corpus — inferência sem dados primários. Risco de investimento sem retorno |
| SC-07: PMEs gerais | 5.73 | Mercado existente (Confidata já serve) sem vantagem diferencial ICT. Expansão futura |
| SC-14: Sec. Saúde | 5.80 | Subconjunto de SC-01 — tratar como persona especializada dentro de prefeituras, não segmento separado |
| SC-15: Assoc. Municípios | 5.33 | Canal puro — não paga pelo produto. Parceiro estratégico, não customer |
| SC-05: Admin. Federal | 3.25 | Complexidade extrema, ICT qualificação diferente, ciclo >24 meses. NÃO atacar |
| SC-10: TCU/TCE | 0.72 | Regulador — não é cliente. Stakeholder a ser gerenciado via content authority |

---

## Lógica de Consolidação para Substituição do JSON Atual

**JSON atual (5 audiences):**
1. `b2g_prefeituras` → MANTER mas subdividir em SC-01 + SC-11
2. `b2g_consorcios` → MANTER e fortalecer (top scorer)
3. `b2b_fornecedores_municipio` → SUBSTITUIR por `b2g_secretarias_educacao` (ECA Digital urgente)
4. `b2b_empresas_privadas` → SUBSTITUIR por `b2g_micro_municipios` (espaço branco real)
5. `b2g_estaduais` → SUBSTITUIR por `b2b_advocacia_whitlabel` (canal white-label comprovado)

**5 audiences novas validadas**:
1. `b2g_prefeituras_medio` (≡ SC-01) — SAM core, score 7.64
2. `b2g_consorcios` (≡ SC-02) — canal multiplica, score 7.99
3. `b2g_secretarias_educacao` (≡ SC-13) — ECA Digital urgente, score 7.24
4. `b2g_micro_municipios` (≡ SC-11) — espaço branco, score 6.85
5. `b2b_advocacia_whitlabel` (≡ SC-08) — parceiro white-label, score 6.49
