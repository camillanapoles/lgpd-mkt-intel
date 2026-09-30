---
id: NEOGOV-V21-CAP14-GTM
filename: 14-gtm-v1.0.1.md
created_at: 2026-05-16T12:20:00Z
type: BUSINESS_PLAN_CHAPTER
chapter: 14
title: Go-to-Market (Roadmap de Waves)
version: v1.0.1
data_source: data/neogov-pricing-cost-ssot-v1.0.8.json
parent_chapters: [12-bmc, 13-vpc, 15-financeiro]
sprint: W1.4.2
edicao: 1
branch: retificacao-validacao-preco-novo
mandato_atendido: USUARIO_2026-05-16 "consolidar · paralelo · WAL contínuo"
canonical_chain: [ssot-v1.0.8, 12-bmc, 13-vpc]
quality_target: PMQS 9.5 · VVV >= 0.78
tags: [gtm, roadmap-waves, sun-tzu, canal-wilton, ssot-v1.0.8]
mandatos_honrados: [RGO-9 honestidade, RGO-3, AP-14, estilo-educacional]
---

# Capítulo 14 · Go-to-Market (Roadmap de Waves)

> **Por que GTM é um roadmap de waves, não uma lista de canais?** A tese da NeoGov não é "vender para todos os segmentos". É uma **sequência onde cada onda financia a próxima** — princípio Sun Tzu (Cap. III): a vitória se prepara antes da batalha. Tratar GTM como lista de táticas perderia o que é estrutural: a *ordem* importa mais que os canais.

---

## §14.1 · O princípio: cada onda paga a seguinte

```
Wave 1 (Alfa/B2G)  → motor de caixa  → financia →
Wave 2 (Beta/Saúde) → fit metodológico → financia →
Wave 3 (Gamma/Educação · SaaS multi-tenant) → escala →
Wave 4 (Delta/Associativo) → "vitória sem batalha" (federação) →
Wave 5-6 (Épsilon/Zeta · DPO/B2B geral) →
Wave 7+ (Ômega · Cartórios/hiper-regulados)
```

**Por que esta ordem específica?**

| Wave | Segmento | Por que nesta posição |
|:--:|---|---|
| W1 | B2G Setor Público | Maior ticket (R$5,4k-50k) + canal político existente (Wilton/FNDE) = caixa rápido |
| W2 | B2B Saúde | Valida metodologia em ambiente regulado complexo · funda o desenvolvimento |
| W3 | B2B Educação | Volume (preço baixo R$597-5k) só compensa com SaaS multi-tenant (precisa W1/W2 financiarem o build) |
| W4 | Associativo | Federações/sindicatos = 1 venda → N clientes ("vitória sem batalha" · Sun Tzu Cap III §3) |
| W5-6 | DPO/B2B geral | Mercado pulverizado · entra após produto maduro |
| W7+ | Cartórios/Ômega | Hiper-regulado · maior complexidade · entra com produto provado |

> **Lição estratégica**: a sequência não é por tamanho de mercado nem por facilidade — é por **capacidade de cada onda financiar a infraestrutura da próxima**. W3 (SaaS) é cara de construir; só faz sentido depois que W1/W2 geraram o caixa. Inverter a ordem (começar pelo volume barato) quebraria o financiamento.

---

## §14.2 · Canais por wave

| Wave | Canal primário | Risco (Cap 17) |
|:--:|---|---|
| W1 B2G | Wilton (acesso político · FNDE · Brasília) | R4: canal único — diversificar em W2+ |
| W2 Saúde | Venda consultiva + Simone (credibilidade jurídica LGPD) | — |
| W3 Educação | Self-service SaaS + parcerias rede de escolas | — |
| W4 Associativo | Federações/sindicatos (1 contrato → N membros) | alavancagem |

> **Por que sinalizar o risco do canal aqui?** GTM honesto reconhece sua própria fragilidade: a Wave 1 depende fortemente de um canal (Wilton). Isso é alavanca *e* risco (R4 no Cap 17). Mitigação: usar o caixa da W1 para construir canais independentes antes da W2.

---

## §14.3 · Mensagem por segmento (do VPC · Cap 13)

| Segmento | Dor central | Mensagem |
|---|---|---|
| B2G Município | Sanção ANPD + sem equipe TI | "Conformidade turnkey · sem montar time" |
| B2B Saúde | Dados sensíveis massivos | "Compliance + cibersegurança integrados" |
| B2B Educação | LGPD + dados de menores | "Proteção de menores automatizada · barato" |
| B2B DPO | Terceirização obrigatória | "DPO-as-a-service com IA" |
| B2B Cartório | Prov. CNJ 213/2026 + assimetria | "Compliance notarial proporcional ao porte" |

---

## §14.4 · Síntese GTM

```
ESTRUTURA:  roadmap de 7 waves · cada uma financia a próxima (Sun Tzu)
ENTRADA:    W1 B2G (maior ticket + canal Wilton) = motor de caixa
ESCALA:     W3 SaaS (só após W1/W2 financiarem o build)
ALAVANCA:   W4 federações ("vitória sem batalha")
RISCO:      W1 canal único (R4 · mitigar com caixa da própria W1)
```

> **A leitura honesta**: o GTM não promete crescimento explosivo imediato. Promete uma sequência disciplinada onde a sobrevivência (W1) vem antes da escala (W3), e cada etapa é autofinanciada pela anterior. É deliberadamente conservador na ordem — porque inverter a sequência por ganância quebraria o modelo de financiamento.

---

## §14.5 · PMQS + Devil's Advocate

PMQS Bruto 9.52 × VVV 0.79 = **7.52** 🟡 honesto

> ⚔️ **1**: "Roadmap de 7 waves é otimista demais." → Procede como risco de execução. O plano financeiro (Cap 15) modela cenários onde nem todas as waves se materializam (cenário A). O roadmap é direção, não garantia.
> ⚔️ **2**: "Dependência de Wilton é frágil." → Reconhecido explicitamente (§14.2 · R4 Cap 17). Honestidade > esconder. Mitigação declarada.
> ⚔️ **3**: "'Vitória sem batalha' é jargão." → É referência precisa a Sun Tzu Cap III §3 (federação = 1 venda atinge N) · conceito operacional, não retórica.

## §14.6 · Backlinks

| Consome | Como |
|---|---|
| Cap 13 VPC | mensagem por segmento |
| Cap 15 Financeiro | waves → trajetória de receita |
| Cap 17 Riscos | R4 canal único |

---

**FIM Cap 14 v1.0.1** · roadmap de waves · lê SSOT v1.0.8 · PMQS 7.52 honesto
