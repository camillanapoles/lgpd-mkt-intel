---
name: ETL como Middleware — Modelo de Produto
description: Usuario definiu ETL/API do sistema NeoGov funciona como middleware. Muda modelo cobranca: infra + integracao = custo recorrente com stickiness e usage-based pricing justificado.
type: project
originSessionId: 0900217c-7777-46b2-91c6-8a8692be686a
---
# ETL como Middleware — Modelo de Produto

## Conceito
NeoGov NAO e apenas SaaS de compliance. E um **middleware de dados LGPD** que:
1. Conecta aos sistemas do cliente (ERP, prontuario, sistema escolar)
2. Extrai dados pessoais via API/ETL
3. Processa, classifica e monitora continuamente
4. Gera relatorios, alertas, RIPD automatico, incidentes

## Implicacao Estrategica
- **Stickiness alta:** cliente integrado nao sai (switching cost)
- **Custo recorrente real:** ETL continuo consome infra NeoGov
- **Pricing natural:** usage-based (registros processados, APIs, armazenamento)
- **Moat:** integracao com sistemas especificos por cluster = fosso competitivo
  - Beta: MV/Tasy/Soul MV (prontuarios hospitalares)
  - Gamma: sistemas escolares (diario, matricula, comunicacao pais)
  - Alfa: sistemas municipais (e-cidade, TCE)

## Camadas de Cobranca

| Camada | O que cobra | Modelo |
|---|---|---|
| **Plataforma base** | Dashboard, RIPD, DSAR | Assinatura mensal |
| **Middleware/ETL** | Volume dados processados, APIs | Usage-based |
| **Integracao** | Conexao sistemas cliente | Setup fee |
| **Consultoria** | Implantacao, DPO-as-a-Service | Projeto/hora |
| **Suporte** | SLA, treinamento | Assinatura add-on |

## Middleware > SaaS puro
- SaaS puro = commodity (OneTrust, LGPD Cloud)
- Middleware com ETL = **infraestrutura critica** do cliente
- Dados fluem continuamente = dependencia real
- Switching cost muito maior

**Why:** Usuario enfatizou ETL/API e o modelo de produto central, nao acessorio.
**How to apply:** BSC-02 trata portfolio como camadas (plataforma + middleware + servico). ETL/middleware e produto defensavel principal.
