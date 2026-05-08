# TEMPLATE CARTA DE INTENÇÃO (LOI)
## Versão DOCX — Instruções de Formatação

---

### INSTRUÇÕES PARA CONVERSÃO EM DOCX

Este documento contém orientações para formatação em Microsoft Word (.docx). Para gerar o documento final:

1. Copie o conteúdo do arquivo `LOI-LGPD-Prefeituras.md`
2. Cole em editor de texto (Word, Google Docs, LibreOffice)
3. Aplique a formatação conforme tabela abaixo
4. Substitua todos os campos `[CAMPO]` pelas informações reais

---

### TABELA DE FORMATAÇÃO

| Elemento | Fonte | Tamanho | Estilo | Alinhamento |
|----------|-------|---------|--------|-------------|
| **Título principal** | Arial | 16 | Negrito | Centralizado |
| **Subtítulo (h2)** | Arial | 14 | Negrito | Justificado |
| **Cabeçalhos de seção** | Arial | 12 | Negrito | Justificado |
| **Corpo do texto** | Arial | 11 | Normal | Justificado |
| **Tabelas** | Arial | 10 | Normal | Centralizado |
| **Assinaturas** | Arial | 10 | Normal | Centralizado |
| **Rodapé/avisos** | Arial | 8 | Itálico | Centralizado |

---

### ESTRUTURA DO DOCUMENTO DOCX

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                                                                                 │
│  [LOGOTIPO PREFEITURA]                                    [LOGOTIPO CIT AI TECH]│
│                                                                                 │
│                                                                                 │
│                              CARTA DE INTENÇÃO (LOI)                            │
│                                                                                 │
│                     Solução de Conformidade LGPD                                │
│                         para o Setor Público                                   │
│                                                                                 │
│                                                                                 │
│  ─────────────────────────────────────────────────────────────────────────     │
│                                                                                 │
│  DATA: [DATA_ASSINATURA]                                                        │
│  REFERÊNCIA: LOI-[NUMERO_SEQUENCIAL]/LGPD/[ANO]                                │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

### SEÇÃO 1 — CABEÇALHO DE PARTES (DOCX)

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║ 1. PARTES                                                                      ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  CONTRATANTE:                                                                 ║
║                                                                               ║
║  [NOME_DA_PREFEITURA_OU_CONSORCIO], pessoa jurídica de direito público        ║
║  interno, inscrita no CNPJ sob o nº [CNPJ], com sede à [ENDEREÇO_COMPLETO],   ║
║  neste ato representada por [NOME_DO_REPRESENTANTE], [CARGO], portador do     ║
║  CPF nº [CPF], doravante denominada CONTRATANTE.                              ║
║                                                                               ║
║  CONTRATADA:                                                                  ║
║                                                                               ║
║  CIT AI TEC INSTITUTO DE CIÊNCIA E TECNOLOGIA LTDA., pessoa jurídica de       ║
║  direito privado, inscrita no CNPJ sob o nº [CNPJ_CIT], com sede à            ║
║  [ENDEREÇO_COMPLETO_CIT], neste ato representada por                          ║
║  [NOME_DO_REPRESENTANTE_CIT], [CARGO_CIT], portador do CPF nº [CPF_CIT],     ║
║  doravante denominada CONTRATADA.                                             ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

---

### SEÇÃO 8 — BLOCOS DE ASSINATURA (DOCX)

Para formatação em DOCX, utilize a seguinte estrutura para os blocos de assinatura:

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                                                                                 │
│  [CIDADE], [DATA]                                                              │
│                                                                                 │
│                                                                                 │
│  ___________________________                              _____________________ │
│  [NOME_DO_REPRESENTANTE]                                  [NOME_DO_REPRESENTANTE]│
│  [CARGO]                                                  [CARGO_CIT]           │
│  CONTRATANTE: [NOME_DA_PREFEITURA]                        CONTRATADA: CIT AI TECH│
│                                                                                 │
│  CPF: [CPF]                                               CPF: [CPF_CIT]        │
│                                                                                 │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

**No Word:**
1. Insert > Table > 2x1
2. Merge cells para criar colunas separadas
3. Center align texto e linhas de assinatura
4. Usar tabulação para alinhar CPF abaixo do nome

---

### PLACEHOLDERS PARA SUBSTITUIÇÃO

#### Dados da Contratante (Prefeitura/Consórcio)

| Placeholder | Descrição | Exemplo |
|-------------|-----------|---------|
| `[NOME_DA_PREFEITURA_OU_CONSORCIO]` | Nome completo | Prefeitura Municipal de [Cidade] |
| `[CNPJ]` | CNPJ completo | 12.345.678/0001-90 |
| `[ENDEREÇO_COMPLETO]` | Endereço sede | Av. Principal, 123 - Centro - [Cidade]/[UF] |
| `[NOME_DO_REPRESENTANTE]` | Nome do signatário | João da Silva |
| `[CARGO]` | Cargo do signatário | Prefeito Municipal |
| `[CPF]` | CPF do signatário | 123.456.789-00 |
| `[EMAIL_CONTRATANTE]` | E-mail oficial | juridico@cidade.rj.gov.br |

#### Dados da Contratada (CIT AI Tech)

| Placeholder | Descrição | Exemplo |
|-------------|-----------|---------|
| `[CNPJ_CIT]` | CNPJ da CONTRATADA | 00.000.000/0001-00 |
| `[ENDEREÇO_COMPLETO_CIT]` | Endereço sede | Rua da Inovação, 456 - São Paulo/SP |
| `[NOME_DO_REPRESENTANTE_CIT]` | Nome do signatário | Maria Santos |
| `[CARGO_CIT]` | Cargo do signatário | Diretora de Operações |
| `[CPF_CIT]` | CPF do signatário | 987.654.321-00 |
| `[EMAIL_CONTRATADA]` | E-mail comercial | contato@citaitech.com.br |

#### Dados da Transação

| Placeholder | Descrição | Exemplo |
|-------------|-----------|---------|
| `[DATA_ASSINATURA]` | Data de assinatura | 08 de maio de 2026 |
| `[NUMERO_SEQUENCIAL]` | Número do LOI | 001 |
| `[ANO]` | Ano do LOI | 2026 |
| `[VALOR_SAAS]` | Valor mensal plataforma | 997,00 |
| `[VALOR_SAAS_ANUAL]` | Valor anual plataforma | 11.964,00 |
| `[VALOR_DPO]` | Valor mensal DPO | 1.500,00 |
| `[VALOR_DPO_ANUAL]` | Valor anual DPO | 18.000,00 |
| `[VALOR_SETUP]` | Taxa de implementação | 5.000,00 |
| `[TOTAL_MENSAL]` | Total mensal | 2.497,00 |
| `[TOTAL_ANUAL]` | Total anual | 29.964,00 |
| `[DESCONTO]` | Desconto pagamento anual | 15 |
| `[PRAZO]` | Dias para pagamento | 30 |
| `[PRAZO_MESES]` | Vigência contrato | 12 |
| `[DIAS_ONBOARDING]` | Dias onboarding | 15 |
| `[DIAS_DIAGNOSTICO]` | Dias diagnóstico | 30 |
| `[DIAS_POLITICAS]` | Dias políticas | 45 |
| `[DIAS_TREINAMENTO]` | Dias treinamento | 5 |
| `[DATA_GO_LIVE]` | Data go-live | 01/08/2026 |
| `[DIAS_EXPERIENCIA]` | Dias experiência | 30 |
| `[VALIDADE_MESES]` | Validade LOI | 6 |
| `[CIDADE]` | Cidade foro | [Nome da Cidade] |
| `[ESTADO]` | Estado foro | RJ |

---

### VERIFICAÇÃO FINAL ANTES DE GERAR DOCX

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│  CHECKLIST — ANTES DE GERAR DOCUMENTO FINAL                                   │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│  [ ] Todos os campos [CAMPO] foram substituídos                                │
│  [ ] CNPJs e CPFs foram validados                                              │
│  [ ] Endereços estão completos e corretos                                      │
│  [ ] Valores monetários estão em formato brasileiro (R$ X.XXX,XX)              │
│  [ ] Datas estão em formato por extenso (ex: 08 de maio de 2026)               │
│  [ ] Nomes dos representantes estão completos (sem abreviações)                │
│  [ ] Cargos correspondem aos estatutos/contratos sociais                      │
│  [ ] E-mails institucionais foram verificados                                  │
│  [ ] Número de referência foi gerado corretamente                              │
│  [ ] Foro foi definido conforme localidade da Contratante                     │
│  [ ] Logotipos foram inseridos em alta resolução                               │
│  [ ] Documento foi revisado por assessoria jurídica                            │
│  [ ] Versão final foi salva em formato PDF para registro                       │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

### NOTAS DE CONVERSÃO AUTOMATIZADA

Para geração automatizada de DOCX via Python:

```python
# Exemplo de código para conversão
from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

doc = Document()

# Título
title = doc.add_heading('CARTA DE INTENÇÃO (LOI)', 0)
title.alignment = WD_ALIGN_PARAGRAPH.CENTER

# Subtítulo
subtitle = doc.add_paragraph('Solução de Conformidade LGPD para o Setor Público')
subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
subtitle.runs[0].italic = True

# Data e referência
doc.add_paragraph(f'DATA: {data_assinatura}')
doc.add_paragraph(f'REFERÊNCIA: LOI-{numero}/LGPD/{ano}')

# ... continuação do documento

# Salvar
doc.save(f'LOI-LGPD-{prefeitura}-{data}.docx')
```

---

### VERSÕES DO DOCUMENTO

Recomenda-se manter controle de versões:

| Arquivo | Formato | Uso |
|---------|---------|-----|
| `LOI-LGPD-Prefeituras.md` | Markdown | Template editável |
| `LOI-LGPD-Prefeituras-DOCX-PLACEHOLDER.md` | Markdown | Instruções DOCX |
| `LOI-LGPD-[PREFEITURA]-[DATA].docx` | DOCX | Versão final para assinatura |
| `LOI-LGPD-[PREFEITURA]-[DATA].pdf` | PDF | Versão assinada/registrada |

---

*Documento preparado por: CIT AI Tech — Departamento Jurídico*
*Versão: 1.0 — Data: Maio 2026*
