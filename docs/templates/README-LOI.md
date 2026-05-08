# Templates de Letter of Intent (LOI) — Solução LGPD para Prefeituras

Diretório de templates de Carta de Intenção para contratação de soluções LGPD pelo setor público, em conformidade com a Lei 14.133/2021 e Marco Legal de CT&I.

---

## Arquivos Disponíveis

| Arquivo | Descrição | Quando Usar |
|---------|-----------|-------------|
| `LOI-LGPD-Prefeituras.md` | Template principal em Markdown | Uso geral, visualização rápida |
| `LOI-LGPD-Prefeituras-DOCX-PLACEHOLDER.md` | Instruções para formatação DOCX | Geração de documento Word final |
| `README-LOI.md` | Este arquivo | Referência e documentação |

---

## Estrutura do LOI

O template segue uma estrutura jurídica clara e acessível, organizada em 9 seções:

1. **Partes** — Identificação completa da Contratante (prefeitura/consórcio) e Contratada (CIT AI Tech)
2. **Objeto** — Descrição da solução DPO-as-a-Service e plataforma SaaS LGPD
3. **Valor Estimado** — Estrutura de precificação com valores compatíveis com dispensa de licitação (Art. 75, II)
4. **Prazo** — Vigência pretendida e cronograma de implementação
5. **Confidencialidade** — Obrigações de sigilo e conformidade com LGPD (Art. 26 §1º)
6. **Não-Obrigatoriedade** — Cláusula expressa de natureza não-vinculativa do LOI
7. **Disposições Gerais** — Comunicações, foro e mecanismos de aceitação
8. **Assinaturas** — Blocos para assinatura dos representantes legais
9. **Anexos** — Documentos complementares (TR, SLA, política de privacidade)

---

## Pontos-Chave do Template

### Base Legal Regulatória

O LOI fundamenta a contratação nas seguintes prerrogativas de ICT:

- **Art. 75, IV, "c" da Lei 14.133/2021** — Dispensa para P&D até R$390.000,00
- **Art. 75, IV, "d" da Lei 14.133/2021** — Dispensa para licenciamento de criação protegida
- **Encomenda Tecnológica (ETEC)** — Para desenvolvimento inovador
- **CPSI** — Contrato Público para Solução Inovadora (Marco das Startups)

### Compatibilidade com Dispensa por Valor

O valor anual estimado situa-se abaixo de R$65.492,00, permitindo:

- Tramitação simplificada
- Sales cycle reduzido
- Menor burocracia para prefeituras pequenas e médias

### Foco em Diferenciais Competitivos

O LOI destaca:

- Data 100% Brasil (Art. 26 §1º LGPD)
- DPO fractionado incluído
- Setup em 30 dias (não meses)
- Relatórios prontos para TCE/TCU
- Templates específicos (IPTU, e-SUS, educação)

---

## Como Usar

### 1. Para Visualização Rápida

Abra `LOI-LGPD-Prefeituras.md` em qualquer visualizador de Markdown:

```bash
# Linux/macOS
cat LOI-LGPD-Prefeituras.md

# Ou abra em VS Code, GitHub, etc.
```

### 2. Para Edição e Personalização

Substitua todos os campos `[CAMPO]` pelas informações reais:

#### Dados Mínimos Obrigatórios

```markdown
# Contratante
[NOME_DA_PREFEITURA_OU_CONSORCIO]
[CNPJ]
[ENDEREÇO_COMPLETO]
[NOME_DO_REPRESENTANTE]
[CARGO]
[CPF]
[EMAIL_CONTRATANTE]

# Contratada (CIT AI Tech)
[CNPJ_CIT]
[ENDEREÇO_COMPLETO_CIT]
[NOME_DO_REPRESENTANTE_CIT]
[CARGO_CIT]
[CPF_CIT]
[EMAIL_CONTRATADA]

# Transação
[DATA_ASSINATURA]
[NUMERO_SEQUENCIAL]
[ANO]
[VALOR_SAAS], [VALOR_DPO], [VALOR_SETUP]
[TOTAL_MENSAL], [TOTAL_ANUAL]
[PRAZO_MESES]
[DATA_GO_LIVE]
[VALIDADE_MESES]
[CIDADE], [ESTADO]
```

### 3. Para Geração de DOCX

Siga as instruções em `LOI-LGPD-Prefeituras-DOCX-PLACEHOLDER.md`:

1. Copie o conteúdo do template principal
2. Cole em Microsoft Word/Google Docs/LibreOffice
3. Aplique formatação conforme tabela
4. Substitua placeholders
5. Insira logotipos
6. Salve como `.docx` e `.pdf`

### 4. Para Automação (Python)

Exemplo de script para geração automatizada:

```python
#!/usr/bin/env python3
"""
Gerador automático de LOI LGPD para prefeituras
"""

from docx import Document
from docx.shared import Pt, Inches
from datetime import date
import json

def gerar_loi(dados_cliente):
    """Gera documento LOI personalizado"""

    doc = Document()

    # Título
    title = doc.add_heading('CARTA DE INTENÇÃO (LOI)', 0)
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER

    # Subtítulo
    subtitle = doc.add_paragraph(
        'Solução de Conformidade LGPD para o Setor Público'
    )
    subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
    subtitle.runs[0].italic = True

    # Data e referência
    doc.add_paragraph(f'DATA: {dados_cliente["data_assinatura"]}')
    doc.add_paragraph(
        f'REFERÊNCIA: LOI-{dados_cliente["numero"]}/LGPD/{dados_cliente["ano"]}'
    )

    # ... continuação conforme template

    # Salvar
    arquivo = f'LOI-LGPD-{dados_cliente["prefeitura"]}-{date.today()}.docx'
    doc.save(arquivo)
    return arquivo

# Exemplo de uso
dados = {
    "prefeitura": "Prefeitura Municipal de Exemplo",
    "cnpj": "12.345.678/0001-90",
    "data_assinatura": "08 de maio de 2026",
    "numero": "001",
    "ano": "2026",
    # ... outros campos
}

arquivo_gerado = gerar_loi(dados)
print(f"LOI gerado: {arquivo_gerado}")
```

---

## Checklist de Validação

Antes de enviar o LOI para assinatura:

```
[ ] Todos os campos [CAMPO] foram substituídos
[ ] CNPJs e CPFs foram validados
[ ] Endereços estão completos
[ ] Valores monetários em formato brasileiro
[ ] Datas por extenso
[ ] Nomes completos (sem abreviações)
[ ] Cargos conforme estatutos sociais
[ ] E-mails institucionais verificados
[ ] Número de referência único
[ ] Foro correto (localidade da Contratante)
[ ] Logotipos em alta resolução (DOCX)
[ ] Revisão jurídica concluída
[ ] Versão PDF salva para registro
```

---

## Controle de Versões

| Versão | Data | Alterações | Autor |
|--------|------|------------|-------|
| 1.0 | 08/05/2026 | Criação inicial | CIT AI Tech |

---

## Notas Importantes

1. **Natureza Jurídica:** Este LOI é NÃO-VINCULATIVO, exceto quanto a confidencialidade e disposições expressamente obrigatórias.

2. **Contrato Definitivo:** A efetiva contratação dependerá de instrumento posterior com Termo de Referência completo, SLAs e cláusulas de responsabilidade.

3. **Conformidade LGPD:** A CONTRATADA compromete-se a armazenar dados em data center no Brasil (Art. 26 §1º).

4. **Base Legal ICT:** O LOI demonstra compreensão das prerrogativas de ICT para contratação simplificada.

---

## Suporte

Para dúvidas sobre o uso destes templates:

- **E-mail:** juridico@citaitech.com.br
- **Documentação:** Ver `/docs/legal/` para referências adicionais

---

*Última atualização: 08 de maio de 2026*
