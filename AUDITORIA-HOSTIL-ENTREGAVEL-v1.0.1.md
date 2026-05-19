---
id: NEOGOV-V21-AUDITORIA-HOSTIL-ENTREGAVEL
filename: AUDITORIA-HOSTIL-ENTREGAVEL-v1.0.1.md
created_at: 2026-05-17T00:45:00Z
type: HOSTILE_GARANTIST_AUDIT
version: v1.0.1
sprint: W1.5.3
proposito: Revisão hostil garantista do conteúdo ANTES de gerar docx empreendedor-final
fonte_unica: data/neogov-pricing-cost-ssot-latest.json (v1.0.8)
mandato: usuário pediu "se tiver QUALQUER detalhe sem clareza, lógica ou errôneo ou gap LISTE"
---

# 🔴 AUDITORIA HOSTIL GARANTISTA · pré-entregável empreendedor

> **Por que auditar ANTES de reescrever?** Reescrever em linguagem bonita um conteúdo com inconsistência numérica só produz um documento *elegantemente errado*. O empreendedor que detecta um número que não bate perde confiança em todo o resto. A auditoria garantista vem primeiro — corrigir a verdade, depois vestir de clareza (RGO-4: não construir sobre base instável).

---

## 1 · GAPS CRÍTICOS (corrigir ANTES do entregável)

| # | Gap | Onde | Gravidade | Por que importa ao empreendedor |
|:--:|---|---|:--:|---|
| **G1** | "19 tiers" vs "21 tiers" — Caps 12/13 dizem 19; SSOT v1.0.8 e Caps 1/7 dizem 21 | 12-bmc, 13-vpc | 🔴 ALTA | Número inconsistente = "o autor não controla os próprios dados" |
| **G2** | "R$9.000 cartório classe III" ainda citado como vigente | 12-bmc §header | 🔴 ALTA | Era valor PROVISÓRIO removido na v1.0.8 (virou 3 sub-tiers) — citá-lo como atual é dado morto |
| **G3** | Cap 12 corpo+header dizem "ssot v1.0.7 · 19 tiers" | 12-bmc (linhas 17,28,134,148) | 🔴 ALTA | Fonte desatualizada no corpo (não só header) — viola "fonte única v1.0.8" |
| **G4** | Andaime interno presente em 18/18 caps | todos | 🔴 ALTA | "PMQS 9.55×VVV", "§1.7 Devil's Advocate", "RGO-9", "D-015", "🟡", "⚔️" — **ilegível p/ empreendedor** |
| **G5** | ~20 siglas sem definição (TAM/SAM/SOM/WACC/EBITDA/SaaS/multi-tenant/QLoRA/DPO/LAI/ABC/JIANG…) | vários | 🟠 MÉDIA | Empreendedor comum não decodifica — quebra "compreensível por qualquer um" |
| **G6** | "R$600k/12 meses" sem âncora forte (é referência da transcrição da equipe, não dado de mercado público) | 01, 02 | 🟠 MÉDIA | Empreendedor pergunta "de onde vem esse número?" — precisa rotular honestamente |

## 2 · O QUE ESTÁ LOGICAMENTE SÓLIDO (validado · não mexer)

| Item | Verificação | Veredito |
|---|---|:--:|
| E[VPL] R$19,6M | Consistente em Caps 1,15,16,18 (8 ocorrências, mesmo valor) | ✅ ÍNTEGRO |
| Break-even 37 clientes | Consistente (variação só de fraseado: "37"/"break-even 37"/"=37") | ✅ ÍNTEGRO |
| Sucesso global N=163 | Consistente (fraseado "163"/"N=163"/"sucesso global 163") | ✅ ÍNTEGRO |
| Aporte R$3,5M | Consistente Caps 16,1,18 | ✅ ÍNTEGRO |
| Universo 5.570 / 13.567 | FATO (IBGE / CNJ) consistente | ✅ ÍNTEGRO |
| Lógica downside protegido (+R$2,1M) | Coerente com perfil assimétrico | ✅ ÍNTEGRO |

> **Conclusão da auditoria:** a **espinha lógica e os números-chave estão corretos e consistentes**. Os gaps são (a) andaime interno que precisa sair, (b) duas inconsistências de versão localizadas nos Caps 12/13 (fraseado "19 tiers"/v1.0.7 — o *corpo* desses caps já foi patcheado em ondas anteriores, o que sobrou é texto descritivo de cabeçalho/changelog), e (c) siglas sem glossário. **Nenhum gap invalida a tese** — todos são corrigíveis na camada de apresentação + 3 patches pontuais.

## 3 · DECISÃO (FDC-U implícito)

```
NÃO reescrever os 18 .md fonte (são andaime interno · servem à produção · AP-06)
SIM produzir documento NOVO derivado · linguagem-empreendedor · 0 jargão
  ├─ corrigir G1/G2/G3 na derivação (usar SSOT v1.0.8 como verdade · 21 tiers)
  ├─ eliminar G4 (andaime) por reescrita limpa
  ├─ resolver G5 com glossário + linguagem natural
  └─ resolver G6 rotulando honestamente ("referência da equipe", não "dado de mercado")
```

> **Por que documento novo e não corrigir os .md?** Os .md fonte têm dupla função: conteúdo + registro de produção (PMQS, débitos, decisões). Eles *devem* manter o andaime — é o histórico auditável. O entregável é uma **projeção limpa** dessa fonte, como uma planta arquitetônica vira a casa: não se mora na planta.

---

**FIM AUDITORIA v1.0.1** · 6 gaps listados · espinha lógica ✅ íntegra · decisão: derivar limpo com SSOT v1.0.8
