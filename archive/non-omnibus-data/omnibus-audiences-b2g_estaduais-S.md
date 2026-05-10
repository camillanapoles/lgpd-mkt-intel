# [TRACE-S] Audience: b2g_estaduais
**Timestamp**: 2026-05-09T18:00:00-03:00

## Custom Weights Extraídos
| Dimensão Sun Tzu | Peso |
|------------------|------|
| DAO (Moral / Alinhamento estratégico) | 0.20 |
| CÉU (Timing / Janela regulatória) | 0.15 |
| TERRA (Posição competitiva) | 0.25 |
| COMANDANTE (Liderança / Articulação política) | 0.25 |
| MÉTODO (Disciplina / Execução) | 0.15 |

**Rationale do JSON**: B2G estaduais pondera COMANDANTE + TERRA — nível estadual exige liderança com influência política e posição competitiva frente a players estabelecidos.

## Fatos sobre Segmento
| Fato | Fonte | VVV Estimado |
|------|-------|-------------|
| 27 estados + DF no Brasil; cada um com ~20-100 órgãos/autarquias | IBGE | 0.90 |
| LGPD Art.41 + Lei 14.133 com limites maiores para licitação estadual | Texto legal | 0.95 |
| Processo licitatório estadual: 3-12 meses para contratação de software | Prática de mercado | 0.75 |
| NeoGov e Confidata já têm penetração em nível estadual | Transcricão + pesquisa | 0.75 |
| Ticket: R$2.000-5.000/mês (JSON persona) para plataforma enterprise | JSON data | 0.75 |
| Decisor: Diretor de TI + Procurador Jurídico (dupla aprovação) | JSON persona | 0.80 |
| Volume de dados: milhares de servidores, décadas de dados acumulados | Inferência de estrutura pública | 0.70 |
| Lei de Acesso à Informação (LAI) + LGPD cria sobreposição complexa | Juridico inferido | 0.80 |
| Estratégia JSON: atacar SOMENTE após consolidar municipal (phase 3+) | JSON sun_tzu_strategy | 0.90 |
| Exposição midiática estadual é maior: vazamento vira notícia regional | Inferência comunicação | 0.70 |

## Pain Points Únicos
1. **Volume de dados insustentável para processo manual**: Órgão estadual tem dados de centenas de milhares de cidadãos (IPVA, saúde, educação). Inventário de dados e mapeamento de fluxos é impossível manualmente — precisa de automação real (Data Discovery).
2. **Dupla conformidade LAI + LGPD cria contradição operacional**: LAI exige transparência; LGPD exige proteção. Como publicar dados de servidores no Portal de Transparência sem violar LGPD? Empresa que não entende essa sobreposição não serve ao órgão estadual.
3. **Processo de licitação inviabiliza agility**: Para contratar um SaaS de R$3K/mês, o órgão estadual precisa fazer pregão eletrônico (3-6 meses). Uma startup sem track record e sem capacidade de vencer licitação estadual não consegue entrar.
4. **Lock-in de players estabelecidos**: NeoGov e Confidata já têm contratos estaduais. Órgão que já usa qualquer sistema deles tende a contratar compliance na mesma plataforma para evitar integração. Barreira de entrada técnica real.
5. **Fiscalização TCE estadual específica para cada estado**: Cada TCE tem interpretação própria sobre o que é "compliance LGPD adequado". Empresa tem que conhecer jurisprudência de cada tribunal — custo de personalização altíssimo para startup.
