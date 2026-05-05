# DRAFT — Pesquisa de Mercado: Plataforma LGPD / Processamento de Dados

> **Modelo de negócio:** Contabilizei da LGPD — SaaS + consultoria para conformidade e processamento de dados
> **Data:** 2026-05-05
> **Status:** Draft com dados validados via web research

---

## 1. TAM — Tamanho de Mercado

| Métrica | Valor | Fonte |
|---------|-------|-------|
| Mercado cybersecurity Brasil (2025) | USD $3.68-4.61 bi | MarketsandMarkets / Mordor Intelligence |
| Projeção cybersecurity (2030) | USD $6.98 bi | MarketsandMarkets |
| Legaltech América Latina (2025) | USD $1.9 bi | IMARC Group |
| Projeção Legaltech (2034) | USD $4.9 bi | IMARC Group |
| Serviços jurídicos Brasil (2024) | USD $43.5 bi | Grand View Research |
| Projeção serviços jurídicos (2030) | USD $57.4 bi | Grand View Research |
| RegTech & Compliance SaaS Brasil | ~USD $1.2 bi | Ken Research |

**Multa LGPD máxima:** 2% do faturamento anual no Brasil, capped em R$ 50 milhões (~USD $10M) por infração

**SAM estimado (LGPD compliance services):** Subset do RegTech + subset legaltech + subset cybersecurity = **~USD $800M - $1.5 bi** (2025), crescendo 15-20% a.a.

---

## 2. Concorrência — Plataformas LGPD Brasil (Preços Reais)

### 2.1 SaaS Platforms (Brazilian)

| Empresa | Plano Entrada | Plano Topo | Modelo | Destaque |
|---------|--------------|-----------|--------|----------|
| **LGPD Fácil** | R$ 69,60/mês | R$ 398,10/mês | Subscription | Foco PME, documentos prontos |
| **LGPD Tech** | R$ 44,90/mês | R$ 74,90/mês | Subscription | Treinamentos + básico |
| **LGPD Tool** | R$ 349,90/mês | R$ 1.049,90/mês | Per-user | 1-5 usuários |
| **LGPD Check-List** | R$ 299/mês | Sob consulta | Subscription | ROPA/RPID automático |
| **Privacy Guard** | R$ 450/mês | R$ 500/mês (anual R$450) | Subscription | Usuários ilimitados |
| **DPO MAX** | Basic (10 colab) | Premium (300 colab, White Label) | Tiered by size | White Label, App, API |
| **Confidata** | R$ 497/mês | R$ 3.497/mês | Tier + per-user | Único com preços públicos, foco órgãos públicos |
| **LGPD Express** | Starter (AI chat) | Premium (ilimitado) | Tier by interactions | IA LEX, DPO access |

### 2.2 Consultoria / Serviços

| Empresa | Preço | Modelo |
|---------|-------|--------|
| **Rastek Soluções** | R$ 800/mês (12x) | Projeto fixo 3-6 meses |
| **DPO-as-a-Service** (genérico) | R$ 1.200 - R$ 15.000+/mês | Outsourcing DPO |

### 2.3 Players Internacionais

| Empresa | Modelo | Nota |
|---------|--------|------|
| **OneTrust** | Enterprise | Líder global, módulo LGPD dedicado |
| **TrustArc** | Enterprise | Multi-regulatório |
| **iubenda** | Per-site | Consent + policies |
| **Securiti.ai** | Enterprise | AI-driven data discovery |

### 2.4 Gap Identificado

**Nenhum player domina o segmento prefeituras/municipal** com:
- Plataforma acessível (R$ 100-500/mês)
- DPO terceirizado incluído
- Adequação à Lei 14.133/2021 (dispensa de licitação até R$ 65.492/ano)
- Data center no Brasil (Art. 26 §1º LGPD)
- Foco em serviços municipais específicos (ISS, IPTU, e-SUS, education)

**Oportunidade:** Contabilizei-like = self-service + automação + DPO fractionado + pricing prefeitura-friendly

---

## 3. ISO 27001 / ISO 27701 — Valor de Certificação

| Aspecto | Detalhe |
|---------|---------|
| Custo ISO 27001 Brasil | USD $30.000+ (depende tamanho/auditor) |
| ISO 27701 (extensão privacidade) | Adicional sobre 27001 |
| Diferenciação competitiva | Alta — poucos fornecedores LGPD possuem |
| Compatibilidade LGPD | ISO 27701 mapeia diretamente para requisitos LGPD |
| Valor para órgãos públicos | Fundamental em editais e processos seletivos |
| Prazo implantação | 6-12 meses para organização madura |

**Estratégia recomendada:** Buscar ISO 27001 como Phase 2 (pós-MVP), ISO 27701 como Phase 3

---

## 4. Segmento-Alvo: Prefeituras e Serviços Municipais

### 4.1 Dados IBGE 2024 (Perfil dos Municípios Brasileiros)

| Indicador | Valor |
|-----------|-------|
| Total municípios Brasil | 5.570 |
| Com responsável LGPD designado | ~28% (~1.559) |
| Sem estrutura LGPD | ~72% (~4.011) |
| População total | 215+ milhões |

### 4.2 Janela de Oportunidade

- **TCEs (Tribunais de Contas)** estão fiscalizando ativamente
- **ANPD** elevada em 2025 — fase de oversight ativo
- **Lei 14.133/2021, Art. 75, II:** Dispensa de licitação até R$ 65.492,11/ano (2026)
- **Orientação Normativa AGU 87/2024:** Parecer jurídico não obrigatório para contratações diretas por valor
- **Prefeituras pioneiras:** Joinville/SC, Congonhas/MG, Suzano/SP, Niterói/RJ — criaram precedentes

### 4.3 Serviços Municipais Típicos (Alto Volume de Dados Pessoais)

- IPTU / Cadastro imobiliário
- ISS / Alvarás
- e-SUS / Saúde pública
- Educação (matrículas, merenda)
- Assistência social (CRAS/CREAS)
- Transporte público
- Protocolo / Ouvidoria

### 4.4 Budget Estimado por Prefeitura

| Porte | População | Budget LGPD/ano estimado |
|-------|-----------|------------------------|
| Pequeno | < 20 mil | R$ 5.000 - 15.000 |
| Médio | 20-100 mil | R$ 15.000 - 50.000 |
| Grande | 100-500 mil | R$ 50.000 - 150.000 |
| Metrópole | > 500 mil | R$ 150.000 - 500.000+ |

**4.011 municípios sem LGPD × R$ 15.000/ano (conservador) = R$ 60M/ano de TAM endereçável imediato**

---

## 5. Modelos de Pricing — Benchmark e Sugestão

### 5.1 Modelos Observados

1. **Subscription tiered** (mais comum): R$ 70 - R$ 3.500/mês
2. **Per-user**: R$ 199-299/usuário adicional
3. **Per-module**: Consent + DPO + Reports separados
4. **Usage-based**: Page views, interações, documentos gerados
5. **DPO-as-a-Service**: R$ 1.200 - R$ 15.000/mês
6. **Projeto fixo**: R$ 800/mês × 12 (R$ 9.600 total)

### 5.2 Pricing Sugerido (Modelo Contabilizei-LGPD)

#### Para Empresas Privadas

| Plano | Preço/mês | Inclui |
|-------|----------|--------|
| **Starter** | R$ 149 | Diagnóstico auto, docs básicos, inventário, treinamentos |
| **Profissional** | R$ 399 | + DPO fractionado (8h/mês), RIPD, gestão incidentes |
| **Enterprise** | R$ 899 | + DPO dedicado, API, white label, suporte 24/7 |

#### Para Prefeituras (Pricing Público)

| Plano | Preço/mês | Inclui |
|-------|----------|--------|
| **Municipal Basic** | R$ 297 | Adequação completa, portal do titular, treinamentos EAD |
| **Municipal Plus** | R$ 597 | + DPO terceirizado, RIPD, relatórios TCE |
| **Municipal Full** | R$ 997 | + Consultoria presencial, ISO 27001 roadmap, API |

**Todos planos municipais abaixo de R$ 65.492/ano (dispensa licitação)**

---

## 6. Roadmap: Zero → MVP → Certificação → Escala

### Phase 0 — Validação (Meses 1-2)
- [ ] Landing page com proposta de valor
- [ ] 50+ entrevistas com secretários de TI de prefeituras
- [ ] 20+ entrevistas com PMEs
- [ ] Validação de willingness-to-pay
- [ ] Definição de ICP (Ideal Customer Profile)

### Phase 1 — MVP (Meses 3-5)
- [ ] Plataforma web (React + Node.js/Python)
- [ ] Módulo 1: Diagnóstico LGPD automatizado (questionário + score)
- [ ] Módulo 2: Inventário de dados (upload + mapeamento)
- [ ] Módulo 3: Gerador de documentos (policies, termos, contratos)
- [ ] Dashboard de conformidade
- [ ] Onboarding self-service
- [ ] Deploy: AWS/GCP com data center em São Paulo (Art. 26 §1º)
- [ ] Beta com 5-10 prefeituras

### Phase 2 — Product-Market Fit (Meses 6-9)
- [ ] Módulo 4: Portal do titular (direitos LGPD)
- [ ] Módulo 5: Gestão de consentimento
- [ ] Módulo 6: Treinamento EAD (Art. 41 III)
- [ ] Relatórios ROPA e RPID automatizados
- [ ] Chat IA para dúvidas LGPD (como LGPD Express)
- [ ] Pricing otimizado com dados reais de uso
- [ ] Meta: 50 clientes ativos

### Phase 3 — DPO & Consultoria (Meses 10-14)
- [ ] DPO-as-a-Service (pool de DPOs fractionados)
- [ ] Gestão de incidentes de segurança
- [ ] Defesas junto à ANPD
- [ ] Relatórios para Tribunais de Contas
- [ ] Integração com sistemas municipais (e-SUS, educacenso)
- [ ] Meta: 150 clientes, R$ 300K MRR

### Phase 4 — Certificação & Expansão (Meses 15-20)
- [ ] Obtenção ISO 27001
- [ ] Início processo ISO 27701
- [ ] White Label para escritórios de advocacia/consultoria
- [ ] API pública para integração
- [ ] Marketplace de templates por setor (saúde, educação, financeiro)
- [ ] Meta: 500 clientes, R$ 1M MRR

### Phase 5 — Nacional & SaaS Scale (Meses 21-30)
- [ ] ISO 27701 obtida
- [ ] Certificação como certificadora nacional (se viável)
- [ ] Expansão para empresas privadas (todos os portes)
- [ ] Parcerias com associações de municípios
- [ ] Features AI: auto-classificação de dados, risk scoring preditivo
- [ ] Meta: 2.000+ clientes, R$ 3M+ MRR, break-even

---

## 7. Sugestões de Valor / Diferenciação

### 7.1 Para Prefeituras
1. **Única plataforma abaixo da dispensa de licitação** com DPO incluído
2. **Data 100% no Brasil** (compliance Art. 26 §1º)
3. **Templates para serviços municipais** (IPTU, e-SUS, education, CRAS)
4. **Relatórios prontos para TCE/TCM** (fiscalização)
5. **Setup em dias, não meses** (self-service + onboarding guiado)

### 7.2 Para Empresas Privadas
1. **Modelo Contabilizei:** self-service + automação + suporte humano quando necessário
2. **Pricing transparente** (poucos fazem — Confidata é exceção)
3. **DPO fractionado** (compartilhado entre clientes = custo menor)
4. **IA para automação** de diagnósticos, documentos, relatórios
5. **Certificação ISO** como diferencial de confiança

### 7.3 Mostras de Proposta de Valor

```
"Se sua prefeitura tem 50.000 habitantes, você processa dados de 100% deles.
 Um único incidente pode gerar multa de até R$ 50 milhões.
 Nossa plataforma adequa sua prefeitura em 30 dias por menos que um salário mínimo/mês."
```

---

## 8. Stack Tecnológico Sugerido

| Camada | Tecnologia | Razão |
|--------|-----------|-------|
| Frontend | React + TailwindCSS | Componentes interativos, SPA |
| Backend | Node.js (Fastify) ou Python (FastAPI) | API REST, performance |
| Database | PostgreSQL | Dados estruturados, ROPA |
| Auth | Keycloak ou Auth0 | SSO/SAML (requisito TCU) |
| Storage | S3-compatible (MinIO) | Documentos, evidências |
| AI | OpenAI / Claude API | Chat LGPD, geração docs |
| Deploy | AWS São Paulo (sa-east-1) | Art. 26 §1º LGPD |
| CI/CD | GitHub Actions | Automatização |
| Infra | Terraform / Docker | IaC, reprodutibilidade |

---

## 9. Fontes Validadas

| # | Fonte | URL | Dado |
|---|-------|-----|------|
| 1 | IBGE — Perfil Municípios 2024 | lgpd2u.com.br | 28% prefeituras com LGPD |
| 2 | MarketsandMarkets | marketsandmarkets.com | Cybersecurity BR $4.61B |
| 3 | IMARC Group | imarcgroup.com | Legaltech LatAm $1.9B |
| 4 | Grand View Research | grandviewresearch.com | Legal services BR $43.5B |
| 5 | Ken Research | kenresearch.com | RegTech BR ~$1.2B |
| 6 | Confidata (preços) | confidata.com.br/precos | R$497-R$3.497/mês |
| 7 | LGPD Fácil (preços) | lgpdfacil.com/planos | R$69.60-R$398.10/mês |
| 8 | Privacy Guard (preços) | lp.privacyguard.com.br | R$450-500/mês |
| 9 | LGPD Tool (preços) | lgpdtool.com.br | R$349.90-R$1.049.90/mês |
| 10 | DPO MAX | dpomax.com.br/precos | Tiered by org size |
| 11 | LGPD Express | lgpdexpress.com.br/planos | Starter-Premium tiers |
| 12 | ANPD | gov.br/anpd | Fiscalização ativa 2025 |
| 13 | Contabilizei (modelo) | businessmodelcanvastemplate.com | Referência modelo negócio |
| 14 | TopCertifier ISO 27001 | iso-certification-brazil.com | Custo ISO BR |
| 15 | Lei 14.133/2021 | gov.br | Dispensa licitação R$65.492 |

---

## 10. Próximos Passos

1. **Validar ICP:** Entrevistar 20+ secretários de TI de prefeituras
2. **Testar pricing:** Apresentar tabela de preços a 30+ potenciais clientes
3. **Iniciar MVP:** Focar no diagnóstico automatizado (maior apelo self-service)
4. **Parcerias:** Associar com associações de municípios (FNP, FNP-MA)
5. **Legal:** Estruturar contratos dentro da Lei 14.133/2021
