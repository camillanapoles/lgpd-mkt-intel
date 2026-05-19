---
id: NEOGOV-V21-REMEDIATION-ENGAGEMENT
filename: NeoGov-REMEDIATION-ENGAGEMENT-v1.W1.10.1.md
version: v1.W1.10.1
created_at: 2026-05-18
type: REMEDIATION_ATTESTATION_ENGAGEMENT
metodologia: padrão Big-4 · ISAE 3000 (attestation) + ISA 450 (remediação)
data_source: Management Letter v1.W1.9.1 (8 achados) + SSOT v1.0.8
mandatos_honrados: [NUNCA CHUTE, RGO-2, cauda-raiz, rastreabilidade]
self_contained: true
---

# ENGAGEMENT DE REMEDIAÇÃO & CERTIFICAÇÃO — NeoGov
## O processo Big-4 do parecer até a certificação assinável

> Você perguntou: contratada com base nos próprios achados, qual o processo,
> quem se envolve, em que ordem, o que fazem por etapa. Este é o desenho formal
> de um *remediation & attestation engagement* (ISAE 3000), mapeado nos 8
> achados reais (MW-1, MW-2, SD-1, SD-2, CD-1 a CD-4).

---

## 0. PRINCÍPIO DE INDEPENDÊNCIA (por que isto se divide em dois contratos)

Padrão Big-4 tem uma regra inegociável: **quem remedia não pode certificar o
próprio trabalho.** Se a firma corrige E atesta, a certificação é nula (conflito
de interesse). Logo o engagement se parte em dois papéis separados:

- **Advisory (remediação):** ajuda a administração a consertar. NÃO assina.
- **Assurance (certificação):** time independente, "muralha chinesa" (ethical
  wall) do advisory, testa o resultado e emite o parecer final.

A administração do NeoGov **é a dona da remediação** — a firma assessora; não
substitui a responsabilidade da gestão (princípio "management's assertion").

---

## 1. QUEM SE ENVOLVE (papéis do engagement)

| Papel | Quem | Responsabilidade |
|---|---|---|
| **Engagement Partner** | Sócio da firma | Assina o parecer final · independência |
| **Engagement Manager** | Gerente sênior | Conduz o dia-a-dia · cronograma |
| **Advisory Lead** | Consultor sênior | Desenha a remediação (NÃO certifica) |
| **Assurance Lead** | Auditor independente | Testa e atesta (muralha vs advisory) |
| **Especialista de Infra/Cloud** | Tech specialist | Cota e valida MW-1 (degraus reais) |
| **Especialista de Custos/ABC** | Cost specialist | Refaz rateio MW-2 |
| **Quality Reviewer (EQCR)** | Sócio 2, externo ao time | Revisão de qualidade independente |
| — lado cliente — | | |
| **Sponsor (CFO/founder)** | NeoGov | Dono das asserções · aprova remediação |
| **Process Owner** | NeoGov eng./fin. | Executa correções · fornece evidência |
| **Comitê de Auditoria** | NeoGov board | Recebe o parecer · governança |

---

## 2. A ORDEM DO PROCESSO (6 fases · ISAE 3000)

A sequência das fases segue a **ordem topológica dos achados** (custo antes de
preço antes de receita antes de VPL — provado no anexo). Não é escolha; é
dependência técnica.

```
FASE 1 Scoping ─► FASE 2 Remediação ─► FASE 3 Readiness
                                            │
FASE 6 Certificação ◄─ FASE 5 Assurance ◄─ FASE 4 Evidência
```

---

### FASE 1 · SCOPING & ENGAGEMENT LETTER (semana 1)

**Quem:** Partner, Manager, Sponsor.
**O que fazem:**
- Carta de contratação define escopo, critérios de certificação, o que será
  atestado e o que será explicitamente excluído (ISAE 3000 exige critérios
  mensuráveis pré-acordados — sem isto não há certificação possível).
- Aceitam os 8 achados do Management Letter como baseline.
- Definem o **critério de aprovação** de cada achado (ex.: MW-1 fecha quando os
  12 recursos têm capacidade+custo cotados de fonte verificável).
- Estabelecem a muralha advisory↔assurance.
**Entregável:** Engagement Letter + matriz de critérios de certificação.

---

### FASE 2 · REMEDIAÇÃO (semanas 2–10) — a maior fase

Conduzida por Advisory + Process Owner do cliente. Ordem **topológica**:

**2A · Fundações (paralelas — sem dependência):**
- CD-3 · unificar SSOT em v1.0.8, corrigir capítulos. *(Process Owner)*
- CD-1 · separar camadas infra/humano no `consumes_drivers`. *(Cost spec.)*
- CD-2 · resolver custo órfão kms+postmark. *(Infra spec.)*
- SD-1 · iniciar coleta de demanda externa (pipeline/LOI). *(Sponsor/comercial)*

**2B · MW-1 (raiz — bloqueia tudo):**
- Especialista de infra levanta arquitetura real produto→recurso.
- Cotação formal dos 10 recursos sem capacidade (CSV já entregue como input).
- Substitui custo-fixo por step-function com degraus reais.
- *Critério de fechamento:* 12/12 recursos com capacidade+custo de fonte
  verificável (cotação de fornecedor, não estimativa).

**2C · MW-2 (depende de 2B):**
- Cost specialist refatora o rateio para LER `consumes_drivers` completo.
- Reconstrói margem por produto com perfil técnico real.
- *Critério:* rateio usa 12/12 drivers; P1 e P4 deixam de compartilhar régua.

**2D · SD-2 (depende de 2B+2C — exige operação real):**
- Piloto Wave1 mede margem e intensidade de uso reais (não análogo).
- *Critério:* margem deixa de ser estimativa, vira medição.

**Entregável:** dossiê de remediação por achado, cada um com evidência de
correção e critério de fechamento atendido.

---

### FASE 3 · READINESS ASSESSMENT (semana 11)

**Quem:** Advisory faz auto-revisão ANTES de entregar ao Assurance.
**O que fazem:** simulam a auditoria de certificação internamente — encontram e
fecham gaps antes do time independente olhar (padrão Big-4: nunca entregar ao
assurance sem readiness; reduz reprovação). Equivale ao seu Quality Gate.
**Entregável:** Readiness Report — verde/amarelo por achado. Amarelo volta à
Fase 2.

---

### FASE 4 · MONTAGEM DA EVIDÊNCIA (semana 12)

**Quem:** Process Owner do cliente entrega; Assurance recebe.
**O que fazem:** cada asserção da administração ("MW-1 está corrigido") vem
acompanhada de evidência testável: cotações assinadas, SSOT versionado, output
do piloto, decision logs. Sem evidência, a asserção não é testável → não
certificável (RGO-2: nada é "done" sem evidência real).
**Entregável:** Evidence Pack indexado por achado.

---

### FASE 5 · ASSURANCE / TESTES INDEPENDENTES (semanas 13–15)

**Quem:** Assurance Lead — **independente**, primeira vez que toca o material.
**O que fazem:** não confiam na palavra do advisory. Re-testam:
- recalculam o custo-step com as cotações (reproduzem, não conferem);
- re-rodam o rateio refatorado e validam que lê 12/12;
- testam a margem do piloto contra a evidência bruta;
- amostragem adversarial (tentam quebrar, padrão hostile audit).
Achado que não passa → **exceção**, volta à Fase 2 (re-trabalho).
**Entregável:** Working Papers + lista de exceções (idealmente vazia).

---

### FASE 6 · CERTIFICAÇÃO (semana 16)

**Quem:** Engagement Partner assina; EQCR (sócio independente) revisa antes.
**O que fazem:**
- EQCR faz revisão de qualidade independente (exigência regulatória Big-4).
- Partner emite o parecer conforme o resultado:
  - **Certificação limpa** — se todos os achados fecharam e VPL recalculado tem
    base. (equivale a "unqualified opinion")
  - **Certificação com ressalva** — se achados menores residuais, declarados.
  - **Recusa** — se MW-1/MW-2 não fecharam: NÃO se certifica. Honestidade > selo.
- Só aqui o VPL recalculado passa a ser **decisão-grade**.
**Entregável:** Certificação final assinada + Management Letter de follow-up
(deficiências residuais a monitorar).

---

## 3. O QUE A CERTIFICAÇÃO **NÃO** É (limite honesto, padrão Big-4)

- Não garante que o plano terá sucesso — atesta que os números têm lastro.
- Não substitui o piloto — atesta que a margem foi medida, não que será mantida.
- Tem data de validade — muda o SSOT, a certificação expira.
- Certifica processo e evidência, não o futuro.

---

## 4. CRONOGRAMA-RESUMO

| Fase | Semanas | Dono | Gate de saída |
|---|---|---|---|
| 1 Scoping | 1 | Partner+Sponsor | Critérios acordados |
| 2 Remediação | 2–10 | Advisory+Cliente | 8 achados fechados |
| 3 Readiness | 11 | Advisory | Tudo verde |
| 4 Evidência | 12 | Cliente | Evidence Pack |
| 5 Assurance | 13–15 | Assurance indep. | Zero exceções |
| 6 Certificação | 16 | Partner+EQCR | Parecer assinado |

~16 semanas. O caminho crítico é MW-1→MW-2→SD-2 (custo→rateio→piloto): nada
acelera isso porque o piloto exige operação real.

---

## 5. CONCLUSÃO

O processo que emerge não é "consertar e carimbar". É a separação formal entre
**quem corrige** (advisory, não assina) e **quem atesta** (assurance independente),
com a remediação na ordem topológica dos achados, evidência testável em cada
porta, e a recusa explícita de certificar se as deficiências materiais não
fecharem. A certificação final só existe se a base existir — exatamente o
princípio que orientou toda esta auditoria desde a primeira mensagem.
