# [TRACE-S] Audience: b2g_prefeituras
**Timestamp**: 2026-05-09T18:00:00-03:00

## Custom Weights Extraídos
| Dimensão Sun Tzu | Peso |
|------------------|------|
| DAO (Moral / Alinhamento estratégico) | 0.15 |
| CÉU (Timing / Janela regulatória) | 0.20 |
| TERRA (Posição competitiva) | 0.30 |
| COMANDANTE (Liderança / Articulação) | 0.20 |
| MÉTODO (Disciplina / Execução) | 0.15 |

**Rationale do JSON**: B2G prefeituras pondera TERRA (posição) mais — contrato municipal depende de posição competitiva.

## Fatos sobre Segmento
| Fato | Fonte | VVV Estimado |
|------|-------|-------------|
| 5.570 municípios brasileiros, maioria sem estrutura LGPD | IBGE 2023 / ANPD relatório | 0.85 |
| Lei 14.133/2021 Art.75 IV: dispensa licitação até R$50K | Texto legal (fato) | 1.00 |
| LGPD Art.41 exige DPO obrigatório para órgãos públicos | LGPD texto (fato) | 1.00 |
| Multa ANPD até 2% do faturamento (teto R$50M) | LGPD Art.52 | 0.95 |
| TAM estimado: ~4.000 pequenos municípios (<100K hab) sem fornecedor LGPD | Inferência IBGE + ANPD | 0.60 |
| Ciclo de compra: 15-45 dias via dispensa de licitação (<R$50K) | Lei 14.133 Art.75 + prática | 0.80 |
| Orçamento SaaS: R$297-397/mes (conforme JSON persona) | JSON validated data | 0.75 |
| Canais: CNM, FNP (Frente Nacional de Prefeitos), consorcios, TCE | JSON + knowledge | 0.75 |
| Decisor: Secretário de Administração ou Prefeito diretamente | Transcricão reunião + prática | 0.80 |
| Nenhum player nacional focus em micro-municípios LGPD | Análise competitiva inferida | 0.55 |

## Pain Points Únicos
1. **Não sabe por onde começar com LGPD**: Gestor público sem conhecimento técnico, sem equipe privacy, percebe LGPD como coisa de "empresa grande". A obrigação legal existe mas não há orientação acessível para prefeitura de 15K habitantes.
2. **Orçamento extremamente limitado**: Prefeitura pequena tem verbas engessadas. Mesmo R$500/mês pode ser barreira se não couber no orçamento de TI (frequentemente inexistente como linha separada).
3. **Medo de autuação TCE/TCU + ANPD simultâneo**: Dupla exposição — irregularidade administrativa E multa de proteção de dados. Paralisa decisão por medo de consequências em qualquer direção.
4. **Processo de contratação percebido como complexo**: Mesmo com dispensa de licitação disponível, gestores públicos têm medo de contestação posterior. A simplicidade do Art.75 IV não é suficientemente conhecida.
5. **Sem parceiro de confiança local**: Decisões de TI em municípios pequenos dependem muito de indicação de pares (outros prefeitos) ou de organismos como TCE/CNM — não de vendas diretas.
