# [TRACE-Q] MSP Universe Mapping — Stage Questionador
**Timestamp**: 2026-05-09T00:00:00-03:00
**Dependência**: f3-msp-universe-S.md (15 segmentos candidatos)

---

## Classificação Epistêmica

| Segmento | Classificação | Evidência (arquivo:seção) | VVV |
|----------|--------------|--------------------------|-----|
| SC-01: Prefeituras 20-100K hab | **FACT** | inteligencia-mercado-govtech-lgpd.md:§Dimensionamento + IBGE MUNIC 2024 + transcricao-insights.json:oportunidades L113 | 0.95 |
| SC-02: Consórcios Intermunicipais | **FACT** | inteligencia-mercado-govtech-lgpd.md:§Canais + market-research-2025.md:§Consortium + strategic-data-unified.json:b2g_consorcios | 0.90 |
| SC-03: Secretarias TI/Administração | **INFERENCE** | co-founder-advisor-municipal-sales.md:§Network L38 (decisor técnico inferido do contexto) | 0.75 |
| SC-04: Administração Estadual | **FACT** | strategic-data-unified.json:b2g_estaduais + MEEST-AE_v2.1.md:§2.3 tabela | 0.65 |
| SC-05: Administração Federal | **SPECULATION** | MEEST-AE_v2.1.md:§2.3 tabela mencionado mas sem evidência no corpus LGPD do projeto | 0.30 |
| SC-06: Fornecedores municipais | **FACT** | strategic-data-unified.json:b2b_fornecedores_municipio (existe no JSON atual) | 0.60 |
| SC-07: PMEs / Empresas privadas | **INFERENCE** | executive-summary.md:§BMC L195 + §SWOT O5 | 0.55 |
| SC-08: Escritórios advocacia | **FACT** | executive-summary.md:§SWOT O4 + inteligencia-mercado-govtech-lgpd.md:§Players L44 | 0.70 |
| SC-09: Procuradorias/Controladorias | **FACT** | inteligencia-mercado-govtech-lgpd.md:§Canais L93 + L98 | 0.70 |
| SC-10: TCU/TCEs | **FACT** | Regulador/influenciador — vários fontes | 0.85 |
| SC-11: Micro-municípios <10K | **FACT** | executive-summary.md:§Segmentação L152 + §Pricing Matrix L224 | 0.80 |
| SC-12: Grandes municípios >100K | **FACT** | market-research-2025.md:§BNDES L136 + executive-summary.md | 0.70 |
| SC-13: Secretarias Educação | **FACT** | market-research-2025.md:§ECA Digital L238 + Lei 15.211/2025 | 0.85 |
| SC-14: Secretarias Saúde | **INFERENCE** | inteligencia-mercado-govtech-lgpd.md:§Tabela L13 (dados sensíveis biometria) | 0.65 |
| SC-15: Associações municípios | **FACT** | transcricao-insights.json:go_to_market + insights-priorizados.yaml | 0.90 |

**Classificações resumidas**: FACT=9, INFERENCE=4, SPECULATION=1

---

## Power-Interest Grid (Posicionamento)

```
                    ALTO INTERESSE (urgência LGPD alta)
                                 │
    KEEP SATISFIED               │      MANAGE CLOSELY (P1 target)
    (Alto poder, baixo interesse │      (Alto poder, alto interesse)
     — satisfazer)               │
                                 │
    TCU/TCEs (reguladores)       │      SC-01: Prefeituras 20-100K ← KEY PLAYER
    SC-12: Grandes >100K         │      SC-02: Consórcios Intermunicipais ← KEY PLAYER
    (têm estrutura própria,      │      SC-11: Micro-municípios <10K ← KEY PLAYER
     menor urgência imediata)    │      SC-13: Secretarias Educação (pós-ECA)
                                 │      SC-09: Procuradorias (influenciadores)
─────────────────────────────────┼─────────────────────────────────────────────
    MONITOR ONLY                 │      KEEP INFORMED
    (Baixo poder, baixo int.)    │      (Baixo poder, alto interesse)
                                 │
    SC-05: Admin. Federal        │      SC-06: Fornecedores municipais
    (ciclo complexo >24 meses)   │      SC-07: PMEs (sem obrigação imediata)
    SC-04: Admin. Estadual       │      SC-08: Escritórios advocacia
    (intermediários, não target) │      SC-14: Secretarias Saúde
    SC-07: PMEs gerais           │      SC-15: Assoc. municípios (canal)
                                 │
                    BAIXO INTERESSE (LGPD não é prioridade)
```

**Quadrante KEY PLAYERS (P1 target)**: SC-01, SC-02, SC-11, SC-13, SC-09
**Quadrante KEEP SATISFIED**: SC-10 (TCU/TCE), SC-12
**Quadrante KEEP INFORMED**: SC-06, SC-08, SC-14
**Quadrante MONITOR ONLY**: SC-04, SC-05, SC-07

---

## 5N — Segmento Crítico 1: Prefeituras 20-100K habitantes (SC-01)

**Por que este segmento é o core?**

1. **Porquê 1** — Porque 72% dos municípios brasileiros não têm estrutura LGPD (IBGE MUNIC 2024, VVV 1.0) e o SAM mais atrativo são as ~1.200 cidades de 20-100K com orçamento disponível mas sem equipe técnica.

2. **Porquê 2** — Porque municípios <10K não têm orçamento suficiente e municípios >100K já têm estrutura própria (Abismo Digital por porte é documentado — VVV 0.95).

3. **Porquê 3** — Porque esses municípios são o target exato do Dispensa Art.75 IV da Lei 14.133/2021 que permite contratação ICT sem licitação até R$390K+, removendo a principal barreira de vendas B2G (VVV 0.95).

4. **Porquê 4** — Porque a fiscalização ativa de ANPD + TCEs criou urgência regulatória forçada nesse segmento: "Prefeitos só se movem com processo/inelegibilidade" (transcricao-insights.json:L159, VVV 0.85) — e essa urgência agora existe.

5. **Porquê 5** — Porque o budget estimado de R$15-50K/ano (insights-priorizados.yaml + transcricao-insights.json) é viável se o pricing for calibrado (VVV 0.7), enquanto as soluções atuais (NeoGov R$600K, Confidata R$497-3.497/mês) são inacessíveis para esse segmento.

**Nulidade (falsificação)**: Se as prefeituras 20-100K não tiverem orçamento disponível mesmo com pressão regulatória (risco: "A maioria das prefeituras estão falidas" — VVV 0.9), o segmento perde atratividade. Mitigação: uso de recursos carimbados FNDE, emendas parlamentares, e OSCIP como canal.

---

## 5N — Segmento Crítico 2: Consórcios Intermunicipais (SC-02)

**Por que consórcios são alavanca estratégica?**

1. **Porquê 1** — Porque vender para 1 consórcio = acesso a 5-30+ municípios simultaneamente, resolvendo o gargalo do sales cycle 1-a-1 de 12 meses (VVV 0.95 sales cycle B2G).

2. **Porquê 2** — Porque consórcios já têm modelo de compra centralizada validado (CIGA: 345 municípios, CIMINAS: R$31.9M credenciamento LGPD 2025 — VVV 0.9), eliminando incerteza de canal.

3. **Porquê 3** — Porque o modelo white-label para consórcios (R$197/mês/município) cria lock-in e receita recorrente multi-cliente via único ponto de contato (strategic-data-unified.json:b2g_consorcios).

4. **Porquê 4** — Porque consórcios intermunicipais podem contratar via Ata de Registro de Preços, habilitando "carona" de dezenas de prefeituras sem licitação individual (inteligencia-mercado-govtech-lgpd.md:§Canais, VVV 0.9).

5. **Porquê 5** — Porque o consórcio como cliente resolve simultaneamente o problema de inadimplência individual das prefeituras (a inadimplência do consórcio é coletivizada e mais difícil) — risco mitigado estruturalmente.

**Nulidade**: Se os grandes consórcios (CIGA, CIMINAS) decidirem desenvolver solução própria de LGPD internamente, o canal fecha. Probabilidade baixa dado custo de desenvolvimento.

---

## 5N — Segmento Crítico 3: Micro-municípios <10K habitantes (SC-11)

**Por que micro-municípios são oportunidade real?**

1. **Porquê 1** — Porque são ~1.000 municípios com taxa de adequação de apenas 19.8% (IBGE MUNIC 2024, VVV 1.0) — maior concentração de desconformidade.

2. **Porquê 2** — Porque são o único segmento onde Confidata não compete (preço mínimo R$497/mês está acima do orçamento) — espaço branco real (executive-summary.md:§Pricing Matrix, VVV 0.9).

3. **Porquê 3** — Porque a Lei 14.133/2021 Art.75 II permite dispensa até R$50K para aquisições simples, e o pricing de R$297/mês = R$3.564/ano está bem abaixo desse threshold — compra simplificada (VVV 0.98).

4. **Porquê 4** — Porque micro-municípios têm secretários que acumulam múltiplas funções, sem equipe técnica — o produto self-service "sem dor de cabeça" é perfeitamente posicionado para esse perfil.

5. **Porquê 5** — Porque mesmo com LTV menor (R$297/mês = R$3.564/ano), o CAC é muito baixo via consórcio/associação (1 evento AMM = 20+ municípios), tornando o unit economics viável.

**Nulidade**: Se os micro-municípios não tiverem capacidade operacional de implementar nem a solução mais simples (servidor público sem qualquer TI), o segmento precisa de modelo freemium + suporte intensivo que aumenta CAC.

---

## Síntese das Questões Abertas Críticas

1. **Distinção SC-03 vs SC-01**: Secretarias de TI são decisores internos das prefeituras, não segmento separado — colapsar em SC-01.
2. **SC-06 (fornecedores municipais) carece de evidência de dor urgente** — mencionado no JSON atual mas sem fundamentação na transcrição ou pesquisa primária. Flag: INFERENCE fraca.
3. **SC-07 (PMEs)**: Mencionado no BMC mas sem pesquisa de campo validando disposição de compra para LGPD nesse segmento no corpus disponível. Evidência apenas por analogia (Confidata serve esse mercado).
4. **SC-13 (ECA Digital)**: Nova lei forçando urgência — segmento real mas falta evidência de disposição de pagamento específica para secretarias de educação municipal.
