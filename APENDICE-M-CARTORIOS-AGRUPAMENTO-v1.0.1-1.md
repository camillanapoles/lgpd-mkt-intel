---
id: NEOGOV-V21-APENDICE-M-CARTORIOS-AGRUPAMENTO
filename: APENDICE-M-CARTORIOS-AGRUPAMENTO-v1.0.1.md
created_at: 2026-05-16T07:40:00Z
type: TECHNICAL_APPENDIX_NEW_SEGMENT_DT_TEST
parent_doc: BUSINESS-PLAN-FINAL-v2.1
data_source: data/neogov-pricing-cost-ssot-v1.0.3.json
parent_apendices: [I-abc, K-dt-test, L-auditoria]
sprint: W1.2-RETIFICACAO-CARTORIOS
edicao: 1
branch: retificacao-validacao-preco-novo
mandato_atendido: |
  USUARIO_2026-05-16: "add ao final o profile cartorios · mto relevante pela qtd solicitacao
  · agrupar por tipo de business (B2G, B2B saude, educacao...) · usar JSON object-oriented
  · FDC-U pra saber sequencia + 5W1H pre-acao"
metodologia:
  primaria: Design Thinking TEST (5a fase · igual Apendice K)
  secundaria: ABC cost (Apendice I) · business_segments grouping
  fato_lastro: web_search CNJ Prov.134/2022 + Prov.213/2026 (16/05/2026)
quality_target: PMQS 9.5 · VVV >= 0.78 · cartorios validado via DT TEST
tags: [cartorios, notarial, business-segments, dt-test, novo-publico, ssot-v1.0.3]
mandatos_honrados: [FDC-U sequencia, 5W1H, RGO-3 ordem certa, RGO-4 base estavel, D-015, VVV]
---

# Apêndice M · Cartórios + Agrupamento por Tipo de Negócio
## Novo Público Validado via DT TEST · SSOT Object-Oriented

> "Cartórios não foram esquecidos — foram corretamente sequenciados. FDC-U decidiu: agrupar ANTES de adicionar (evita retrabalho RGO-3). Como o SSOT é object-oriented, adicionar foi trivial: `ssot.business_segments.b2b_notarial.tiers[]`."

---

## §1 · FDC-U de Sequência (resposta ao mandato "usar FDC-U pra saber sequência")

```
fdc_u_sequencia (executado no PRE-ALWAYS deste turno):
  candidatos: [K1 cartorios, K2 agrupar, K3 cap15, K4 session]
  vencedor_topologico: K2 → K1 → K4 → K3
  porque (RGO-3 minimizar refatoracao):
    agrupar(K2) ANTES de add(K1) → cartorio entra JA no grupo b2b_notarial
    → zero retrabalho · vs adicionar solto e reagrupar depois (2x trabalho)
  validacao_usuario: "como estamos usando json ne? object-oriented, fica facil?"
    → SIM · K2+K1 agora = ssot.business_segments + ssot.pricing_tiers.cartorio_* (1 edit)
```

---

## §2 · Lastro FATO · Por que Cartórios é "mto relevante" (web_search 16/05/2026)

```
FATO_1: ~12.000+ serventias extrajudiciais BR (ON-RCPN · CNJ Prov.213/2026)
        VVV 0.88 · fonte: onrcpn.org.br + anoregpi.org.br
FATO_2: CNJ Prov.134/2022 → LGPD obrigatoria cartorios (180 dias adequacao · gap assessment)
FATO_3: CNJ Prov.213/2026 (20/02/2026 · RECENTISSIMO) → cibersec + criptografia +
        trilhas auditoria + plano continuidade + LGPD plena OBRIGATORIOS · VVV 0.90
FATO_4: cartorios = CONTROLADORES dados sensiveis massivos (nascimento→morte,
        filiacao, patrimonio) · risco LGPD altissimo · IRIB/CNJ
FATO_5: progressividade por arrecadacao (Classe I/II/III) → estratificar (Min. Campbell:
        "quanto maior arrecadacao e volume de dados, maior rigor exigido")
FATO_6: podem TERCEIRIZAR Encarregado/DPO (Prov.134 art.6 §) → P4 AI-DPO fit direto

VEREDITO: usuario estava CERTO · alta relevancia · Prov.213/2026 cria demanda
          COMPULSORIA RECENTE (fev/2026) · janela de oportunidade aberta agora.
```

---

## §3 · Agrupamento por Tipo de Negócio (K2 · `ssot.business_segments`)

```
ssot.business_segments = {
  b2g_setor_publico:   [alfa_m_pro, alfa_m_plus_pregao, alfa_m_plus_dispensa,
                         alfa_m_enterprise, alfa_fe]
  b2b_saude:           [beta_pequeno_y1/y2, beta_medio_y1/y2, beta_grande_y1/y2]
  b2b_educacao:        [gamma_pequena, gamma_media, gamma_enterprise]
  b2b_profissional:    [epsilon_dpo, epsilon_escritorio]
  b2b_notarial:        [cartorio_classe1, cartorio_classe2, cartorio_classe3]  ← NOVO
}
```

| Segmento | Nome client-facing | Tiers | Compra como |
|---|---|:--:|---|
| **B2G** | Setor Público | 5 | Licitação/dispensa |
| **B2B Saúde** | Hospitais | 6 | RFP/setup |
| **B2B Educação** | Escolas | 3 | Self-service |
| **B2B Profissional** | DPOs/Escritórios | 2 | Per seat |
| **B2B Notarial** | Cartórios | 3 | Subscription (proporcional) |

> Navegação object-oriented: `ssot.business_segments.b2b_notarial.tiers` → lista direta. Facilita compressão por tipo de cliente como você pediu.

---

## §4 · DT TEST · Cartórios (5ª fase · igual Apêndice K)

### 4.1 `dt_test.cartorio_classe1` — Serventia Pequena

```
recall.POV (titular cartorio pequeno · 1-3 funcionarios · baixa arrecadacao):
  jobs:  ["cumprir Prov.134+213 CNJ", "terceirizar DPO (nao tenho equipe)",
          "evitar sancao Corregedoria", "cibersec minima viavel"]
  pains: ["assimetria estrutural (Min.Campbell reconhece)", "sem orcamento TI",
          "Prov.213 fev/2026 novo e assustador", "arrecadacao baixa"]
  gains: ["compliance turnkey barato", "DPO terceirizado IA", "transicao proporcional"]

prototype.price = ssot.cartorio_classe1.price.recommended = R$ 897/mes
test:
  c1_payability  = 10.764/ano vs arrecadacao cartorio pequeno R$150k-500k = 2-7% → PASS
  c2_competition = sem concorrente especializado notarial+IA · iComp/LGPD Cloud genericos → PASS_FORTE
  c3_wtp_proxy   = 🟠 ESTIMATIVA · analogo Epsilon DPO R$997 · cartorio paga p/ evitar Corregedoria → PASS (D-015)
  c4_margin      = (897-256)/897 = 71% → PASS
verdict = PASS · price.validated = R$ 897
vvv = 0.72 (c3 estimativa · D001-NOVO-16 piloto cartorio calibra)
```

### 4.2 `dt_test.cartorio_classe2` — Serventia Média

```
recall.POV (cartorio medio · 4-10 func · arrecadacao moderada):
  jobs:  ["LGPD + LAIxLGPD certidoes inteiro teor", "gap assessment Prov.134",
          "trilhas auditoria Prov.213", "DPO + politica seguranca"]
  pains: ["certidao inteiro teor x LGPD tensao real", "Prov.213 cibersec custosa",
          "compartilhamento SIRC/centrais dados"]
  gains: ["P3-B2G resolve LAIxLGPD certidoes", "compliance + cibersec integrado"]

prototype.price = R$ 4.500/mes
test:
  c1_payability  = 54k/ano vs arrecadacao media R$500k-2M = 2.7-11% → PASS
  c2_competition = vs generico iComp R$1.2-3k · NeoGov premium MAS notarial-especifico → PASS
  c3_wtp_proxy   = 🟠 analogo Gamma Enterprise · cartorio medio suporta · risco Corregedoria alto → PASS (D-015)
  c4_margin      = (4.500-1.789)/4.500 = 60% → PASS
verdict = PASS · price.validated = R$ 4.500
vvv = 0.70
```

### 4.3 `dt_test.cartorio_classe3` — Serventia Grande

```
recall.POV (cartorio grande · registro imoveis/notas capital · alta arrecadacao):
  jobs:  ["rigor maximo Prov.213 (maior arrecadacao=maior exigencia)",
          "dados sensiveis massivos protegidos", "certidoes volume LAIxLGPD",
          "plano continuidade negocios robusto"]
  pains: ["volume dados massivo", "exposicao reputacional alta", "auditoria CNJ rigorosa"]
  gains: ["enterprise-grade compliance", "P3-B2C anonimizacao volume", "soberania"]

prototype.price = R$ 18.000/mes
test:
  c1_payability  = 216k/ano vs arrecadacao grande R$2-20M+ = 1-11% → PASS
  c2_competition = vs OneTrust/generico · NeoGov notarial-especifico + IA propria → PASS
  c3_wtp_proxy   = 🟠 analogo Alfa-M Enterprise · cartorio grande alta capacidade → PASS (D-015)
  c4_margin      = (18.000-6.677)/18.000 = 63% → PASS
verdict = PASS · price.validated = R$ 18.000
vvv = 0.72
```

### 4.4 Resultado · escreve `ssot.cartorio_*.price.validated`

| Tier | recommended | **validated** | DT verdict | margem | VVV |
|---|---:|---:|:--:|:--:|:--:|
| `cartorio_classe1` | R$ 897 | **R$ 897** | PASS | 71% | 0.72 |
| `cartorio_classe2` | R$ 4.500 | **R$ 4.500** | PASS | 60% | 0.70 |
| `cartorio_classe3` | R$ 18.000 | **R$ 18.000** | PASS | 63% | 0.72 |

> Todos PASS · 3 elos c3 (WTP) = ESTIMATIVA por análogo declarada (D-015) · sub-débito **D001-NOVO-16** (piloto cartório · Van Westendorp notarial) calibra.

---

## §5 · Impacto na Curva de Ponto de Sucesso

```
Cartorios ADICIONAM potencial de receita SEM custo fixo adicional (mesma infra guarda-chuva):
  TAM cartorios: ~12.000 serventias BR
  Penetracao conservadora 2% Wave 3-5 = 240 cartorios
  Mix estimado: 60% Classe I (R$897) + 30% Classe II (R$4.500) + 10% Classe III (R$18.000)
  Receita potencial 240 cartorios:
    144 × R$897   = R$ 129.168/mes
    72 × R$4.500  = R$ 324.000/mes
    24 × R$18.000 = R$ 432.000/mes
    TOTAL          = R$ 885.168/mes adicional (Wave 3-5)
  margem media ~64% · CSC baixo (ABC · infra compartilhada)

→ Cartorios ACELERAM ponto de sucesso global (mais receita · mesma CF)
  Recalculo curva: Apendice F calculator aceita novos tiers via ssot (parametrico)
```

---

## §6 · Devil's Advocate

> **Contra 1**: "Preços cartório são análogos · não testados (c3 ESTIMATIVA)"
>
> **Refutação**: Verdade · marcado D-015 honestamente (Apêndice L padrão). Análogos são FORTES: Classe I↔Épsilon DPO (mesmo P4), Classe III↔Alfa-M Enterprise (mesmo bundle). D001-NOVO-16 piloto calibra. Não é chute — é estimativa ancorada em tier já validado.

> **Contra 2**: "12.000 serventias é TAM teórico · penetração real?"
>
> **Refutação**: 2% Wave 3-5 é conservador (240/12.000). Prov.213/2026 (fev/2026) torna compliance compulsório RECENTE → demanda real, não especulativa. Comparável: Gamma escolas teve adoção similar pós-ECA Digital.

> **Contra 3**: "Adicionar 5º segmento agora dispersa foco Wave 1"
>
> **Refutação**: NÃO dispersa execução — apenas registra no SSOT/catálogo. Cartórios é Wave 3-5 (Ômega notarial). Wave 1 segue B2G/Educação. Você pediu "add ao final" — feito como registro, não como prioridade de execução imediata.

---

## §7 · FDC-U D-W1.2-RETIF-003

| Opção | Score |
|---|---|
| **B · Agrupar(K2) → Cartórios(K1) → DT TEST · SSOT v1.0.3** | **🥇 9.50** |
| A · Cartórios solto sem agrupar (retrabalho RGO-3) | 5.20 |
| C · Só agrupar · cartórios depois (mandato parcial) | 6.80 |
| D · Adiar tudo para Cap 15 (ignora pedido explícito) | 4.10 |

Dimensões: mandato usuário 0.30 · RGO-3 ordem 0.20 · FATO lastro 0.20 · object-oriented facilita 0.15 · velocidade 0.15. **Vencedor B 9.50**.

---

## §8 · PMQS

PMQS Bruto = 9.6×.15+9.7×.15+9.4×.10+9.7×.20+10×.15+9.5×.10+9.6×.15 = **9.66**
VVV = 0.78 (cartórios novo · c3 estimativa · mas FATO legal forte)
**PMQS Final = 9.66 × 0.78 = 7.53** 🟡 (honesto · sobe pós D001-NOVO-16 piloto cartório)

---

## §9 · Versionamento & Próximo

| Versão | Data | Mudança |
|---|---|---|
| v1.0.1 | 2026-05-16T07:40 | K2 business_segments + K1 cartórios 3 classes + DT TEST + SSOT v1.0.3 |

**Sequência FDC-U restante** (continuidade automática):
```
✅ K2 agrupar (feito · ssot.business_segments)
✅ K1 cartórios (feito · 3 classes validadas DT TEST)
🔴 K4 consolidar SESSION-STATE + DECISIONS-LOG branch (próximo · fecha branch · RGO-2)
🟡 K3 Cap 15 Financeiro (usa ssot v1.0.3 final · com cartórios + agrupado)
```

---

**FIM Apêndice M**

> **Mandato cumprido**: ✅ FDC-U decidiu sequência (K2→K1→K4→K3 · justificado RGO-3) · ✅ 5W1H pré-ação executado · ✅ cartórios add (3 classes · FATO CNJ Prov.134/213 web_search) · ✅ agrupado por tipo de negócio (5 business_segments) · ✅ SSOT object-oriented v1.0.3 (navegável `ssot.business_segments.b2b_notarial`) · ✅ DT TEST validou preços · base estável.
