# Risk Analysis — Transcrição NeoGov

## Risk Matrix

| Risco | Categoria | Probabilidade | Impacto | Mitigation | Owner | VVV |
|-------|----------|----------------|---------|------------|-------|-----|
| **Prefeitura não ter orçamento/budget** | Comercial | Alta | Alto | Emendas parlamentares; recursos de secretarias (saúde/educação); financiamento FNDE; modelo SaaS com mensalidades reduzidas; subcontratação via OSCIP (sem licitação) | Simone / Wilton | 0.8 |
| **Vazamento de dados sensíveis durante implementação** | Operacional | Média | Crítico | Diagnóstico jurídico prévio; mapeamento completo de fluxos de dados; classificação documental; anonimização imediata de dados físicos; plano de resposta a incidentes | Camila / Simone | 0.7 |
| **ANPD/MP/TCE requisitarem Relatório de Impacto sem estrutura** | Regulatório | Alta | Crítico | Sistema automatizado (LGPD Web) que gera relatórios em tempo real; matrizes de risco preenchidas; inventário de dados sempre atualizado; auditorias preventivas | Simone / Camila | 0.9 |
| **Servidor público causar vazamento (ex: funcionário com rancor)** | Operacional | Média | Crítico | Marca d'água em documentos impressos; log de acesso com identificação; bloqueio imediato de acessos; treinamento de boas práticas; processo disciplinar interno | Camila | 0.7 |
| **Prefeitura fingir conformidade (só política de cookies)** | Regulatório | Alta | Alto | Auditoria profunda de todos os setores; validação de dados físicos e digitais; verificação de controle de acesso; evidências de implementação real; relatórios de maturidade | Simone | 0.8 |
| **Ciclo de vendas B2G excessivamente longo (burocracia)** | Comercial | Alta | Alto | Pitch com valor político ("cidade transparente"); propaganda para prefeito; proposta com emenda já incluída; redução de preço via automação; SaaS auto-vendável | Wilton / Simone | 0.8 |
| **Não conseguir viabilizar economicamente o produto** | Comercial | Média | Crítico | Redução de custo via automação (IA); modelo volume x margem; subcontratação (digitalização); precificação competitiva; validação de viabilidade antes do build | Camila / Wilton | 0.7 |
| **Concorrência (LGPD Tech, TOW, etc.) com preços agressivos** | Competitivo | Alta | Médio | Diferencial: documentos físicos + digitais; OSCIP (sem licitação); specialized em setor público; one-stop-shop (jurídico + tech + segurança); melhor preço via escala | Simone / Wilton | 0.6 |
| **Prefeito priorizar votos em vez de LGPD** | Comercial | Alta | Médio | Posicionar como marketing político ("dados protegidos", "cidade transparente"); uso em campanha; Compliance para evitar processos/inelegibilidade; comparativo com municípios vizinhos | Wilton | 0.6 |
| **Subcontratação falhar (digitalizaçãoanonimização)** | Operacional | Baixa | Alto | Contratos com SLAs rigorosos; fiscalização do processo de execução; certificação de qualidade; backup de fornecedores; cláusulas de indenização | Simone | 0.4 |
| **Desenvolvimento da plataforma (LGPD Web/Drive) atrasar** | Operacional | Média | Alto | MVP em 30-45 dias; desenvolvimento paralelo à captação; reuso de componentes open-source; time técnico dedicado; milestone claros | Camila | 0.7 |
| **Sistema não passar em validação técnica do TI da prefeitura** | Operacional | Média | Médio | Participação de Camila em reuniões técnicas; ISO 27001 compliance; arquitetura robusta; sandbox de demonstração; referências de outros municípios | Camila | 0.5 |
| **Processo manual (corpo-a-corpo) não escalar** | Operacional | Alta | Crítico | Automação via IA (machine learning); dashboard auto-executável; formulários online; webinars em massa; modelo "franchise" com consultores locais | Camila / Wilton | 0.9 |
| **Prefeitura ser autuada durante implementação** | Regulatório | Média | Alto | Priorizar bases legais urgentes; carta de atestado de "em processo"; evidências de progresso; comunicação proativa com ANPD; plano de ação imediato | Simone | 0.7 |
| **Cliente churn (abandono) antes de finalizar projeto** | Comercial | Média | Médio | Contratos com cláusulas de retenção; entregas faseadas com valor perceptível; treinamento de servidores; sucesso do cliente dedicado; KPIs de maturidade visíveis | Wilton / Simone | 0.5 |
| **Dados em nuvem sofrerem ataque/ransomware** | Operacional | Baixa | Crítico | Criptografia E2E; backup offline múltiplo; acesso only com 2FA; monitoramento 24/7; seguro cibernético; redundância geográfica | Camila | 0.5 |
| **Prefeito ser substituído e novo cancelar contrato** | Político | Média | Alto | Contratos plurianuais; cláusulas de indenização; valor entregue até o momento (ativo); marketing com novo prefeito; obrigação legal intransferível | Simone | 0.6 |
| **Nível de maturidade zero em órgãos federais (ex: Ministério da Saúde)** | Regulatório | Média | Médio | Foco inicial em municípios (menor complexidade); depois expandir para estados/união; referências de sucesso municipais; lobbing por legislação mais estrita | Simone | 0.5 |
| **Documentos físicos sem controle (arquivo morto)** | Operacional | Alta | Médio | Diagnóstico de arquivologia; plano de classificação temporalidade; digitalização + destruição física controlada; treinamento de arquivo; LGPD Drive com OCR | Simone / Camila | 0.7 |
| **Não ter time técnico suficiente para escala** | Operacional | Média | Alto | Subcontratação estratégica; parcerias com universidades; trainees/juniors para levantamento; especialistas only em delivery; plataforma auto-vendável | Camila | 0.7 |

**VVM (Valor de Viabilidade Média):** 0.67 (risco moderado-alto, mitigável com execution rigorosa)

---

## Red Flags (Validar ANTES)

1. **[CRÍTICO] Viabilidade econômica NÃO está validada** — Precisa saber custo de desenvolvimento (LGPD Web/Drive) X preço de venda X margem. Se R$5k/mês com custo R$3k, margem 40% pode ser baixa para escalar. (linhas 1391-1397, 1564-1573)

2. **[CRÍTICO] Prefeituras estão falidas** — "A maioria das prefeituras estão falidas, estão sem dinheiro, por causa do mal uso do dinheiro público." (linhas 889-892) Preciso validar se funding via emendas/secretarias é realista ou só exceção.

3. **[CRÍTICO] Processo 100% manual (corpo-a-corpo)** — "O método é bem-venda corpo a corpo. Tem casos políticos, isso mesmo." (linhas 1631-1634) Se não automatizar, não escala. Preciso confirmar que Camila pode entregar MVP em 30-45 dias e qual prioridade.

4. **[ALTO] Concorrência existe e é forte** — LGPD Tech, TOW, Confidata já estão no mercado. Diferencial ("documentos físicos + digitais") precisa ser validado com prospects: é real ou só nice-to-have?

5. **[ALTO] Prefeitos não priorizam LGPD** — Comparação com lixo: "menos de 1,5% das prefeituras no Brasil tem aterro sanitário." (linha 862) Prefeito só se move se tiver (a) Processo/inelegibilidade, (b) Marketing/votos, ou (c) Orçamento sobrando. Pitch precisa atacar os três.

6. **[ALTO] Time técnico NÃO está dimensionado** — Pergunta "quanto tempo a gente precisa para desenvolver LGPD Web, LGPD Drive?" foi feita mas NÃO respondida. (linhas 1228-1247) Sem isso, não dá pra validar custo/margem.

7. **[ALTO] Subcontratação é estratégia-chave mas não está mapeada** — "A gente pega o contrato por um preço e compra por outro." (linha 608) Quem são os 3 fornecedores de digitalização? Qual é a spread real? O que acontece se falhar?

8. **[MÉDIO] OSCIP/Instituto não está estruturado** — "A Lei Nacional das OSCIP, ela fala justamente isso. O instituto que tem a qualificação de OSCIP, a grande questão que você acabou de falar, ele faz e somente faz a gestão dos recursos." (linhas 656-661) Preciso validar se instituto JÁ tem qualificação ou é plano.

9. **[MÉDIO] Produto não está definido (escopo aberto)** — Discussão sobre "duas ferramentas, dois sistemas, mas uma plataforma integrada" (linhas 1668-1669) sem clareza de MVP. Preciso de product spec before build.

10. **[MÉDIO] Sales cycle B2G pode ser >12 meses** — Exemplo RJ: "o prefeito queria que aumentasse o valor da proposta" (linha 1503) indica processo lento. Preciso validar métricas reais de conversion (proposal → close).

---

## GAPS de Conhecimento

| Gap | Por que importa | Como validar |
|-----|-----------------|--------------|
| **Custo de desenvolvimento da plataforma** | Sem isso, não consigo precificar, calcular ROI, ou levantar funding | Camila precisa entregar orçamento detalhado (dev, infra, manutenção) com cronograma |
| **Taxa de conversão real (proposal → close)** | Permite estimar runway, sizing de time de vendas, volume de leads necessário | Simone compartilhar histórico: quantas propostas enviadas X quantas fechadas, com ticket médio |
| **Custo de subcontratação (digitalização)** | Spread entre "preço que cobra cliente" e "preço que paga fornecedor" é parte da margem | Wilton getting 3 quotes de fornecedores de digitalizaçãoanonimização |
| **Qualificação OSCIP está ativa?** | Se não, não existe "sem licitação" — edge competevio disappears | Verificar status no governo federal; senão, plano B (licitação ou convênio) |
| **Maturidade LGPD de municípios-alvo** | Se estão "no estágio zero", projeto é mais longo (educação + implementação) | Survey com 10 prefeitos de pequeno/médio porte para validar awareness |
| **Feature set real vs. nice-to-have** | Escopo aberto vira scope creep forever; precisa de MVP | Definir product spec com feature matrix: must-have vs. phase 2 |
| **Referências de sucesso (case studies)** | Sem prova social, adoption é mais lenta | Conseguir 3 prefeituras que aceitam ser beta testers (talvez com desconto) |
| **Competitive positioning real** | Se concorrentes já fazem "docs físicos", diferencial desaparece | Análise aprofundada de LGPD Tech, TOW, Confidata (features, pricing, cases) |
| **Regulamentação ANPD 2025-2026** | Agenda regulatória pode mudar urgency | Estudar roadmap ANPD; entrevistar especialista para validar timing |
| **Unit economics (LTV:CAC)** | Sem isso, não dá pra escalar com VC ou growth equity | Modelo financeiro com churn, LTV, CAC, payback period |

---

## VVV (Validação de Viabilidade)

### Score médio por risco: **0.67 / 1.0**

**Interpretação:**
- Riscos regulatórios são mais altos (0.8-0.9) mas **mitigáveis** com produto bem-executado
- Riscos comerciais são altos (0.6-0.8) mas **endereçáveis** com pricing correto e pitch político
- Riscos operacionais são médios (0.5-0.7) e **dependem de execution** (time técnico + MVP)
- Viabilidade **existe** se (e somente se) (a) custo de desenvolvimento for <=R$150k, (b) pricing >=R$5k/mês, (c) time técnico entrega em 45 dias

### Recomendação Imediata:

**ANTES de qualquer desenvolvimento:**
1. Camila: entregar orçamento de desenvolvimento com 80% de confidence
2. Wilton: levantar 3 quotes de fornecedores de digitalização (spread real)
3. Simone: validar qualificação OSCIP do instituto E histórico de conversão
4. Todos: definir product spec MVP (features must-have vs. phase 2)

**Se** (custo dev <= R$150k) **E** (pricing >= R$5k/mês) **E** (OSCIP ativa) → **Green light**
**Senão** → Pivot ou rethink model.

---

### Fontes de Linha (amostra)

- Linhas 889-892: prefeituras falidas, mal uso dinheiro público
- Linhas 1228-1247: gap de informação sobre tempo de desenvolvimento
- Linhas 1391-1397: discussão sobre custo de serviço (R$5k - R$3k = R$2k lucro)
- Linhas 1631-1634: "método é bem-venda corpo a corpo"
- Linhas 608-624: estratégia de subcontratação (compra por X, vende por Y)
- Linhas 656-661: OSCIP e gestão de recursos
- Linhas 112-119: caso real de vazamento (funcionário público com AIDS publicado na internet)
- Linhas 26-27: fiscalização ANPD/MP/TCE começou em 2022
