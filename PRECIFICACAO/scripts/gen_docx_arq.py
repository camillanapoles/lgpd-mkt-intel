#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NeoGov — Arquitetura de Infraestrutura v1.20.1
Gerador de documento DOCX profissional.
"""

import os
from docx import Document
from docx.shared import Inches, Pt, Cm, Emu, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.section import WD_ORIENT
from docx.oxml.ns import qn, nsdecls
from docx.oxml import parse_xml
import datetime

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
DARK_BLUE = RGBColor(0x1B, 0x2A, 0x4A)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
LIGHT_GRAY = RGBColor(0xF2, 0xF2, 0xF2)
MEDIUM_GRAY = RGBColor(0xCC, 0xCC, 0xCC)
ACCENT_BLUE = RGBColor(0x2C, 0x5F, 0x8A)
DARK_BLUE_HEX = "1B2A4A"
LIGHT_BLUE_HEX = "E8EEF4"
BORDER_COLOR = "B0B0B0"

OUTPUT_PATH = "/home/z/my-project/download/NeoGov_Arquitetura_Infra_v1.20.1.docx"
C4_DIR = "/home/z/my-project/download/c4"

# ─── HELPER FUNCTIONS ────────────────────────────────────────────────────────

def set_cell_shading(cell, color_hex):
    """Set background shading for a table cell."""
    shading = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shading)


def set_cell_border(cell, **kwargs):
    """Set cell borders. kwargs: top, bottom, left, right with dict of sz, color, val."""
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcBorders = parse_xml(f'<w:tcBorders {nsdecls("w")}></w:tcBorders>')
    for edge, attrs in kwargs.items():
        element = parse_xml(
            f'<w:{edge} {nsdecls("w")} w:val="{attrs.get("val", "single")}" '
            f'w:sz="{attrs.get("sz", "4")}" w:space="0" '
            f'w:color="{attrs.get("color", BORDER_COLOR)}"/>'
        )
        tcBorders.append(element)
    tcPr.append(tcBorders)


def format_table(table, header_color=DARK_BLUE_HEX):
    """Apply professional formatting to a table."""
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    # Style borders
    tbl = table._tbl
    tblPr = tbl.tblPr if tbl.tblPr is not None else parse_xml(f'<w:tblPr {nsdecls("w")}/>') 
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'  <w:top w:val="single" w:sz="4" w:space="0" w:color="{BORDER_COLOR}"/>'
        f'  <w:left w:val="single" w:sz="4" w:space="0" w:color="{BORDER_COLOR}"/>'
        f'  <w:bottom w:val="single" w:sz="4" w:space="0" w:color="{BORDER_COLOR}"/>'
        f'  <w:right w:val="single" w:sz="4" w:space="0" w:color="{BORDER_COLOR}"/>'
        f'  <w:insideH w:val="single" w:sz="4" w:space="0" w:color="{BORDER_COLOR}"/>'
        f'  <w:insideV w:val="single" w:sz="4" w:space="0" w:color="{BORDER_COLOR}"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)

    # Format header row
    if len(table.rows) > 0:
        for cell in table.rows[0].cells:
            set_cell_shading(cell, header_color)
            for paragraph in cell.paragraphs:
                paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
                for run in paragraph.runs:
                    run.font.color.rgb = WHITE
                    run.font.bold = True
                    run.font.size = Pt(10)
                    run.font.name = "Calibri"

    # Format data rows
    for i, row in enumerate(table.rows[1:], 1):
        bg = LIGHT_BLUE_HEX if i % 2 == 0 else "FFFFFF"
        for cell in row.cells:
            set_cell_shading(cell, bg)
            for paragraph in cell.paragraphs:
                for run in paragraph.runs:
                    run.font.size = Pt(9.5)
                    run.font.name = "Calibri"


def add_styled_heading(doc, text, level=1):
    """Add a heading with custom dark blue styling."""
    heading = doc.add_heading(text, level=level)
    for run in heading.runs:
        run.font.color.rgb = DARK_BLUE
        run.font.name = "Calibri"
    return heading


def add_body_text(doc, text, bold=False, italic=False, alignment=WD_ALIGN_PARAGRAPH.JUSTIFY):
    """Add a body paragraph with standard formatting."""
    p = doc.add_paragraph()
    p.alignment = alignment
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.line_spacing = Pt(15)
    run = p.add_run(text)
    run.font.size = Pt(11)
    run.font.name = "Calibri"
    run.font.bold = bold
    run.font.italic = italic
    return p


def add_bullet(doc, text, level=0):
    """Add a bullet point."""
    p = doc.add_paragraph(style='List Bullet')
    p.clear()
    run = p.add_run(text)
    run.font.size = Pt(10.5)
    run.font.name = "Calibri"
    p.paragraph_format.space_after = Pt(3)
    if level > 0:
        p.paragraph_format.left_indent = Cm(1.5 * level)
    return p


def set_page_margins(section, top=2.0, bottom=2.0, left=2.5, right=2.5):
    """Set page margins in cm."""
    section.top_margin = Cm(top)
    section.bottom_margin = Cm(bottom)
    section.left_margin = Cm(left)
    section.right_margin = Cm(right)


def add_footer_page_number(section):
    """Add page number to footer."""
    footer = section.footer
    footer.is_linked_to_previous = False
    p = footer.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    run = p.add_run("NeoGov — Arquitetura de Infraestrutura v1.20.1  |  Página ")
    run.font.size = Pt(8)
    run.font.color.rgb = RGBColor(0x66, 0x66, 0x66)
    run.font.name = "Calibri"
    
    # Add page number field
    fldChar1 = parse_xml(f'<w:fldChar {nsdecls("w")} w:fldCharType="begin"/>')
    run1 = p.add_run()
    run1._r.append(fldChar1)
    
    instrText = parse_xml(f'<w:instrText {nsdecls("w")} xml:space="preserve"> PAGE </w:instrText>')
    run2 = p.add_run()
    run2._r.append(instrText)
    
    fldChar2 = parse_xml(f'<w:fldChar {nsdecls("w")} w:fldCharType="end"/>')
    run3 = p.add_run()
    run3._r.append(fldChar2)
    
    for r in [run1, run2, run3]:
        r.font.size = Pt(8)
        r.font.color.rgb = RGBColor(0x66, 0x66, 0x66)


def add_c4_image(doc, filename, caption, description_paragraphs):
    """Add a C4 diagram image with caption and description."""
    img_path = os.path.join(C4_DIR, filename)
    
    if os.path.exists(img_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p_img.add_run()
        run.add_picture(img_path, width=Cm(16))
    
    # Caption
    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_cap = p_cap.add_run(caption)
    run_cap.font.size = Pt(10)
    run_cap.font.bold = True
    run_cap.font.color.rgb = DARK_BLUE
    run_cap.font.name = "Calibri"
    run_cap.font.italic = True
    
    doc.add_paragraph()  # spacer
    
    # Description paragraphs
    for desc_text in description_paragraphs:
        add_body_text(doc, desc_text)
    
    doc.add_paragraph()  # spacer


def add_horizontal_line(doc):
    """Add a thin horizontal line."""
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    pPr = p._p.get_or_add_pPr()
    pBdr = parse_xml(
        f'<w:pBdr {nsdecls("w")}>'
        f'  <w:bottom w:val="single" w:sz="6" w:space="1" w:color="{DARK_BLUE_HEX}"/>'
        f'</w:pBdr>'
    )
    pPr.append(pBdr)


# ─── COVER PAGE ──────────────────────────────────────────────────────────────

def create_cover_page(doc):
    """Create a professional cover page with dark background."""
    section = doc.sections[0]
    
    # Add a full-page table to simulate dark background
    # We'll use a 1-cell table that covers the page
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    
    cell = table.cell(0, 0)
    set_cell_shading(cell, DARK_BLUE_HEX)
    
    # Remove table borders for clean look
    tbl = table._tbl
    tblPr = tbl.tblPr if tbl.tblPr is not None else parse_xml(f'<w:tblPr {nsdecls("w")}/>') 
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'  <w:top w:val="none" w:sz="0" w:space="0" w:color="auto"/>'
        f'  <w:left w:val="none" w:sz="0" w:space="0" w:color="auto"/>'
        f'  <w:bottom w:val="none" w:sz="0" w:space="0" w:color="auto"/>'
        f'  <w:right w:val="none" w:sz="0" w:space="0" w:color="auto"/>'
        f'  <w:insideH w:val="none" w:sz="0" w:space="0" w:color="auto"/>'
        f'  <w:insideV w:val="none" w:sz="0" w:space="0" w:color="auto"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)
    
    # Set cell width to full page
    tc = cell._tc
    tcW = parse_xml(f'<w:tcW {nsdecls("w")} w:w="5000" w:type="pct"/>')
    tc.get_or_add_tcPr().append(tcW)
    
    # Clear default paragraph
    cell.paragraphs[0].clear()
    
    # Spacing at top
    for _ in range(4):
        p_spacer = cell.add_paragraph()
        p_spacer.paragraph_format.space_after = Pt(0)
        p_spacer.paragraph_format.space_before = Pt(0)
    
    # Main title
    p_title = cell.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_after = Pt(8)
    run_t = p_title.add_run("NeoGov")
    run_t.font.size = Pt(44)
    run_t.font.bold = True
    run_t.font.color.rgb = WHITE
    run_t.font.name = "Calibri"
    
    # Subtitle line
    p_sub = cell.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_after = Pt(6)
    run_s = p_sub.add_run("——")
    run_s.font.size = Pt(20)
    run_s.font.color.rgb = RGBColor(0x6B, 0x8C, 0xBE)
    run_s.font.name = "Calibri"
    
    # Subtitle
    p_sub2 = cell.add_paragraph()
    p_sub2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub2.paragraph_format.space_after = Pt(24)
    run_s2 = p_sub2.add_run("Arquitetura de Infraestrutura")
    run_s2.font.size = Pt(28)
    run_s2.font.color.rgb = RGBColor(0xCC, 0xDD, 0xEE)
    run_s2.font.name = "Calibri"
    
    # Description
    p_desc = cell.add_paragraph()
    p_desc.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_desc.paragraph_format.space_after = Pt(6)
    run_d = p_desc.add_run("Engenharia de Requisitos + Modelo C4 + Derivacao de Infraestrutura")
    run_d.font.size = Pt(14)
    run_d.font.color.rgb = RGBColor(0x99, 0xAA, 0xBB)
    run_d.font.name = "Calibri"
    run_d.font.italic = True
    
    # Spacer
    for _ in range(4):
        p_spacer = cell.add_paragraph()
        p_spacer.paragraph_format.space_after = Pt(0)
    
    # Version info
    p_ver = cell.add_paragraph()
    p_ver.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_ver.paragraph_format.space_after = Pt(4)
    run_v = p_ver.add_run("v1.20.1  |  Data: 2026-05-20")
    run_v.font.size = Pt(12)
    run_v.font.color.rgb = RGBColor(0x88, 0x99, 0xAA)
    run_v.font.name = "Calibri"
    
    # ID
    p_id = cell.add_paragraph()
    p_id.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_id.paragraph_format.space_after = Pt(4)
    run_i = p_id.add_run("NEOGOV-V21-INSTRUCAO-SESSAO-PARALELA")
    run_i.font.size = Pt(10)
    run_i.font.color.rgb = RGBColor(0x77, 0x88, 0x99)
    run_i.font.name = "Calibri"
    run_i.font.italic = True
    
    # Classification
    p_class = cell.add_paragraph()
    p_class.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_class.paragraph_format.space_after = Pt(0)
    run_c = p_class.add_run("CONFIDENCIAL — Uso Interno")
    run_c.font.size = Pt(9)
    run_c.font.color.rgb = RGBColor(0x66, 0x77, 0x88)
    run_c.font.name = "Calibri"
    run_c.font.small_caps = True
    
    # Page break after cover
    doc.add_page_break()


# ─── SECTION 1: ENGENHARIA DE REQUISITOS ─────────────────────────────────────

def create_section_1(doc):
    """Section 1 — Engenharia de Requisitos."""
    
    add_styled_heading(doc, "1. Engenharia de Requisitos", level=1)
    add_horizontal_line(doc)
    
    add_body_text(doc, (
        "Esta secao apresenta a engenharia de requisitos completa da plataforma NeoGov, "
        "organizada em tres dimensoes complementares: (i) requisitos funcionais detalhados por produto, "
        "que definem o que o sistema deve fazer; (ii) requisitos nao-funcionais que estabelecem "
        "qualidades, restricoes e metricas de sucesso; e (iii) a matriz de rastreabilidade que "
        "conecta cada requisito ao produto, persona responsavel e possiveis gargalos tecnicos. "
        "A abordagem segue as melhores praticas de Engenharia de Requisitos (SOMMERVILLE, 2011) "
        "adaptada ao contexto de plataformas governamentais multi-tenant com capacidades de IA."
    ))
    add_body_text(doc, (
        "A plataforma NeoGov e composta por cinco produtos principais, cada um com escopo e "
        "caracteristicas tecnicas distintas. O P1 (Data Discovery) e o P5 (ETL/Integracao) operam "
        "exclusivamente com logica deterministica, sem dependencia de GPU. O P2 (Anonimizacao) "
        "utiliza IA em modo batch assincrono. Ja o P3 (LAIxLGPD) e o P4 (AI-DPO) exigem GPU "
        "quente reservada para atender requisito de latencia interativa. Essa classificacao e "
        "fundamental para a derivacao de infraestrutura apresentada na Secao 4."
    ))
    
    # ── 1.1 Requisitos Funcionais ──
    add_styled_heading(doc, "1.1 Requisitos Funcionais por Produto", level=2)
    
    add_body_text(doc, (
        "A tabela a seguir consolida todos os requisitos funcionais identificados para os cinco "
        "produtos da plataforma NeoGov. Cada requisito possui um identificador unico (RF-P{N}-{NN}), "
        "esta vinculado a um produto especifico, possui uma descricao detalhada do comportamento "
        "esperado, uma prioridade (Critica, Alta, Media) e uma classe de requisito que indica sua "
        "natureza tecnica (IA, batch, interativo, legado, etc.). A prioridade foi definida com base "
        "no impacto operacional e nos riscos regulatórios de LGPD associados a cada funcionalidade."
    ))
    
    # Data for functional requirements
    rf_data = [
        # P1 — Data Discovery
        ["RF-P1-01", "P1 — Data Discovery", "Varredura batch de fontes de dados institucionais para identificacao de schemas, tabelas, colunas e tipos de dados", "Critica", "Batch"],
        ["RF-P1-02", "P1 — Data Discovery", "Classificacao de dados por regras pre-definidas (sem IA): identificacao heuristicas de PII (CPF, CNPJ, nome, email, telefone)", "Critica", "Regra"],
        ["RF-P1-03", "P1 — Data Discovery", "Mapeamento de dados pessoais: cruzamento automatico de colunas identificadas com catalogo de tipos PII da LGPD (Art. 5)", "Alta", "Regra"],
        ["RF-P1-04", "P1 — Data Discovery", "Relatorio de inventario de dados pessoais: geracao de documento com lista completa de bases, colunas e classificacao", "Alta", "Relatorio"],
        ["RF-P1-05", "P1 — Data Discovery", "Conectores multi-fonte (PostgreSQL, MySQL, SQL Server, Oracle, S3, arquivos CSV/JSON) para ingestao de metadados", "Critica", "Conector"],
        # P2 — Anonimizacao
        ["RF-P2-01", "P2 — Anonimizacao", "Detecao de PII/NER utilizando modelos de IA (NER) em modo batch: identificacao de entidades nomeadas em textos livres", "Critica", "IA-Batch"],
        ["RF-P2-02", "P2 — Anonimizacao", "Job queue para processamento assincrono de lotes de documentos: enfileiramento, priorizacao e retry automatico", "Critica", "Fila"],
        ["RF-P2-03", "P2 — Anonimizacao", "Pre-processamento de documentos: normalizacao de encoding, limpeza, extracao de texto de PDFs e imagens (OCR)", "Alta", "Pipeline"],
        ["RF-P2-04", "P2 — Anonimizacao", "Pos-processamento e validacao de anonimizacao: verificacao de que nenhum dado pessoal permaneceu exposto apos tratamento", "Critica", "Validacao"],
        ["RF-P2-05", "P2 — Anonimizacao", "Tecnicas de anonimizacao aplicaveis: mascaramento, generalizacao, supressao, pseudonimizacao conforme Art. 12 da LGPD", "Alta", "Regra"],
        # P3 — LAIxLGPD
        ["RF-P3-01", "P3 — LAIxLGPD", "Decisao automatizada de revelacao ou nao de informacao pessoal em certidoes LAI, com base legal fundamentada", "Critica", "IA-Interativo"],
        ["RF-P3-02", "P3 — LAIxLGPD", "Interface interativa sincrona com latencia inferior a 2 segundos (tempo de resposta total, incluindo inferencia)", "Critica", "Performance"],
        ["RF-P3-03", "P3 — LAIxLGPD", "GPU quente reservada 24/7 com modelo de IA carregado em memoria para garantir latencia previsivel", "Critica", "Infra"],
        ["RF-P3-04", "P3 — LAIxLGPD", "Inclusao de base legal (fundamentacao juridica) na certidao gerada, referenciando artigos da LGPD e LAI aplicaveis", "Alta", "Regra"],
        ["RF-P3-05", "P3 — LAIxLGPD", "Registro de auditoria de cada decisao: entrada, saida, base legal aplicada e justificativa da IA para revisao futura", "Critica", "Auditoria"],
        # P4 — AI-DPO
        ["RF-P4-01", "P4 — AI-DPO", "Interface de chat conversacional para atendimento ao Encarregado de Dados (DPO) com historico de sessao", "Critica", "IA-Interativo"],
        ["RF-P4-02", "P4 — AI-DPO", "RAG (Retrieval-Augmented Generation) com base de conhecimento LGPD: indexacao de legislacao, orientacoes e precedentes", "Critica", "IA-RAG"],
        ["RF-P4-03", "P4 — AI-DPO", "Gerenciamento de sessao e historico: contexto persistente por usuario com possibilidade de retomar conversas anteriores", "Alta", "Sessao"],
        ["RF-P4-04", "P4 — AI-DPO", "GPU quente reservada 24/7 com modelo de linguagem carregado para respostas em tempo real", "Critica", "Infra"],
        ["RF-P4-05", "P4 — AI-DPO", "Streaming de resposta: entrega progressiva do conteudo gerado para melhoria da experiencia do usuario", "Alta", "Streaming"],
        ["RF-P4-06", "P4 — AI-DPO", "Base de conhecimento atualizavel: carga incremental de novos documentos legislativos e orientacoes sem reindexacao total", "Media", "RAG"],
        # P5 — ETL/Integracao
        ["RF-P5-01", "P5 — ETL/Integracao", "Conectores para sistemas legados governamentais: e-Cidade, MV/Sistemas Tasy, SEI, SIAFI e Class (Câmara)", "Critica", "Conector"],
        ["RF-P5-02", "P5 — ETL/Integracao", "Processamento batch agendado de ETL: extracao, transformacao e carga de dados com cron configuravel por tenant", "Critica", "Batch"],
        ["RF-P5-03", "P5 — ETL/Integracao", "Validacao de dados durante carga: verificacao de integridade referencial, tipos de dados e restricoes de dominio", "Alta", "Validacao"],
        ["RF-P5-04", "P5 — ETL/Integracao", "Connector Manager: interface para cadastro e gerenciamento de conexoes com fontes de dados externas", "Alta", "Conector"],
        ["RF-P5-05", "P5 — ETL/Integracao", "SEM IA neste produto: processamento puramente deterministico, sem dependencia de GPU ou modelos de machine learning", "Critica", "Sem-IA"],
    ]
    
    table1 = doc.add_table(rows=1 + len(rf_data), cols=5)
    table1.autofit = True
    
    # Headers
    headers1 = ["ID", "Produto", "Requisito Funcional", "Prioridade", "Classe"]
    for j, h in enumerate(headers1):
        cell = table1.rows[0].cells[j]
        cell.text = h
    
    # Data
    for i, row_data in enumerate(rf_data):
        for j, val in enumerate(row_data):
            cell = table1.rows[i + 1].cells[j]
            cell.text = val
    
    format_table(table1)
    
    # Set column widths
    widths1 = [Cm(2.0), Cm(3.2), Cm(8.5), Cm(1.8), Cm(2.0)]
    for row in table1.rows:
        for idx, width in enumerate(widths1):
            row.cells[idx].width = width
    
    doc.add_paragraph()
    
    # ── 1.2 Requisitos Nao-Funcionais ──
    add_styled_heading(doc, "1.2 Requisitos Nao-Funcionais", level=2)
    
    add_body_text(doc, (
        "Os requisitos nao-funcionais (RNFs) definem as qualidades transversais e restricoes "
        "tecnologicas da plataforma NeoGov. Diferentemente dos requisitos funcionais, que descrevem "
        "comportamentos especificos, os RNFs estabelecem atributos de qualidade como desempenho, "
        "seguranca, escalabilidade e conformidade regulatória. Estes requisitos sao especialmente "
        "criticos em contextos governamentais, onde a soberania de dados, a conformidade com LGPD e "
        "a disponibilidade do servico impactam diretamente a prestacao de servicos publicos ao cidadao."
    ))
    add_body_text(doc, (
        "Destaca-se o RNF-01 (Soberania de Dados), que impoe que toda a infraestrutura esteja "
        "localizada em nuvem brasileira, sem chamadas a APIs externas como OpenAI ou Anthropic. "
        "Esta restricao e um mandato do cliente e tem impacto profundo na arquitetura, exigindo "
        "modelos de IA proprios hospedados localmente. Os RNFs de latencia (03 e 04) diferenciam "
        "os produtos interativos (P3 e P4) dos produtos batch (P1 e P2), determinando a estrategia "
        "de GPU: quente reservada para interativo e sob demanda (spot) para batch."
    ))
    
    rnf_data = [
        ["RNF-01", "Soberania de Dados", "Toda infraestrutura em cloud BR (OVH BR, Locaweb, AWS BR). Sem API externa (OpenAI, Anthropic). IA propria e local.", "TODOS", "100% dados em BR; 0 chamadas externas"],
        ["RNF-02", "Multi-tenancy", "Isolamento logico de dados por tenant (orgao). Cada orgao visualiza apenas seus proprios dados e configuracoes.", "TODOS", "Zero vazamento cross-tenant em testes"],
        ["RNF-03", "Latencia (P3)", "Resposta interativa sincrona inferior a 2 segundos para decisao de revelacao em certidao LAI.", "P3", "P95 < 2s; P99 < 3s"],
        ["RNF-04", "Latencia (P4)", "Primeiro token de resposta do chat em menos de 3 segundos; streaming subsequente continuo.", "P4", "TTFT P95 < 3s"],
        ["RNF-05", "Retencao de Auditoria", "Logs de auditoria LGPD (Art. 46) mantidos por no minimo 5 anos em storage imutavel.", "TODOS", "100% logs recuperaveis em 5 anos"],
        ["RNF-06", "GPU Quente Reservada", "Instancia GPU dedicada 24/7 com modelo carregado em memoria (warm model) para P3 e P4.", "P3, P4", "Modelo loaded; cold start = 0"],
        ["RNF-07", "GPU Batch sob Demanda", "Instancias GPU spot/preemptive para processamento batch do P2, escalando conforme fila.", "P2", "Tempo de fila < 15 min (P95)"],
        ["RNF-08", "Escalabilidade Horizontal", "Capacidade de escalar recursos por tenant individualmente conforme demanda.", "TODOS", "Novo tenant provisionado em < 4h"],
        ["RNF-09", "Disponibilidade (SLA)", "Disponibilidade minima de 99.5% (uptime mensal), excluindo janelas de manutencao agendada.", "TODOS", "Uptime >= 99.5% mensal"],
        ["RNF-10", "Conformidade LGPD Art. 46", "Medidas tecnicas e administrativas de seguranca: criptografia em transito e repouso, controle de acesso, logs.", "TODOS", "Audit pass; 0 vulnerabilidades criticas"],
        ["RNF-11", "Integracao Legados", "Conectores nativos com e-Cidade, MV/Tasy, SEI, SIAFI e Class para ingestao de dados institucionais.", "P5", "Conector funcional por sistema"],
        ["RNF-12", "IA Propria Local", "Modelos de IA executados inteiramente em infraestrutura propria, sem chamadas a servicos de terceiros.", "P2, P3, P4", "0 dependencias de API externa"],
    ]
    
    table2 = doc.add_table(rows=1 + len(rnf_data), cols=5)
    table2.autofit = True
    
    headers2 = ["ID", "Categoria", "Requisito", "Produto(s)", "Metrica de Sucesso"]
    for j, h in enumerate(headers2):
        table2.rows[0].cells[j].text = h
    
    for i, row_data in enumerate(rnf_data):
        for j, val in enumerate(row_data):
            table2.rows[i + 1].cells[j].text = val
    
    format_table(table2)
    
    widths2 = [Cm(1.8), Cm(2.5), Cm(6.5), Cm(1.8), Cm(4.0)]
    for row in table2.rows:
        for idx, width in enumerate(widths2):
            row.cells[idx].width = width
    
    doc.add_paragraph()
    
    # ── 1.3 Matriz de Rastreabilidade ──
    add_styled_heading(doc, "1.3 Matriz de Rastreabilidade", level=2)
    
    add_body_text(doc, (
        "A matriz de rastreabilidade abaixo conecta cada requisito funcional ao seu produto, "
        "a persona primaria responsavel e o gargalo tecnico identificado. Esta matriz e fundamental "
        "para garantir que todos os requisitos sao cobertos pela arquitetura proposta e que os "
        "gargalos sao tratados de forma explicita nas decisoes arquiteturais. A identificacao "
        "previa de gargalos permite priorizar investimentos em infraestrutura e mitigar riscos "
        "tecnicos antes da implementacao."
    ))
    add_body_text(doc, (
        "As personas mapeadas incluem: DPO (Encarregado de Dados Pessoais) — usuario principal do "
        "P4 e beneficiario do P3; Eng. de Dados — responsavel por configurar conectores e jobs "
        "no P1 e P5; Operador LGPD — usuario que aciona processos de anonimizacao no P2; e "
        "Solicitante LAI — cidadao ou servidor que solicita certidao via P3. Os gargalos sao "
        "classificados como: GPU (dependencia de hardware de aceleracao), Conector (complexidade "
        "de integracao com sistema legado), Fila (limitacao de throughput de processamento batch), "
        "e Modelo (dependencia de modelo de IA treinado e atualizado)."
    ))
    
    trace_data = [
        ["RF-P1-01", "P1 — Data Discovery", "Eng. de Dados", "Conector (multi-fonte)", "Varredura requer conectores estaveis"],
        ["RF-P1-02", "P1 — Data Discovery", "Eng. de Dados", "Regra (heuristica)", "Regras de classificacao pre-definidas"],
        ["RF-P1-03", "P1 — Data Discovery", "DPO", "Catalogo PII", "Catalogo abrangente de tipos de dados pessoais"],
        ["RF-P1-04", "P1 — Data Discovery", "DPO", "Nenhum", "Relatorio gerado a partir de metadados coletados"],
        ["RF-P1-05", "P1 — Data Discovery", "Eng. de Dados", "Conector (legado)", "Drivers e protocolos variados por sistema"],
        ["RF-P2-01", "P2 — Anonimizacao", "Operador LGPD", "GPU + Modelo NER", "Modelo NER precisa e atualizado"],
        ["RF-P2-02", "P2 — Anonimizacao", "Operador LGPD", "Fila (throughput)", "Dimensionamento da fila para picos de demanda"],
        ["RF-P2-03", "P2 — Anonimizacao", "Operador LGPD", "Pipeline (OCR)", "Qualidade do OCR em documentos escaneados"],
        ["RF-P2-04", "P2 — Anonimizacao", "Operador LGPD", "Validacao (regras)", "Cobertura das regras de validacao pos-anonimizacao"],
        ["RF-P2-05", "P2 — Anonimizacao", "DPO", "Modelo (tecnicas)", "Selecao adequada da tecnica por tipo de dado"],
        ["RF-P3-01", "P3 — LAIxLGPD", "Solicitante LAI", "GPU + Modelo IA", "Modelo treinado com decisoes juridicas"],
        ["RF-P3-02", "P3 — LAIxLGPD", "Solicitante LAI", "GPU (latencia)", "GPU quente e carregada para < 2s"],
        ["RF-P3-03", "P3 — LAIxLGPD", "DPO", "GPU (custo fixo)", "Custo 24/7 de GPU reservada"],
        ["RF-P3-04", "P3 — LAIxLGPD", "Solicitante LAI", "Base Legal", "Base juridica atualizada e indexada"],
        ["RF-P3-05", "P3 — LAIxLGPD", "DPO / Auditor", "Storage", "Armazenamento de logs por 5 anos"],
        ["RF-P4-01", "P4 — AI-DPO", "DPO", "GPU + Modelo LLM", "Modelo LLM treinado em LGPD/legislacao"],
        ["RF-P4-02", "P4 — AI-DPO", "DPO", "Vector Store", "Indexacao eficiente da base de conhecimento"],
        ["RF-P4-03", "P4 — AI-DPO", "DPO", "Sessao (estado)", "Gerenciamento de contexto por usuario"],
        ["RF-P4-04", "P4 — AI-DPO", "DPO", "GPU (custo fixo)", "Custo 24/7 de GPU reservada para chat"],
        ["RF-P4-05", "P4 — AI-DPO", "DPO", "Streaming (latencia)", "Infraestrutura de streaming estavel"],
        ["RF-P4-06", "P4 — AI-DPO", "Eng. de Dados", "Vector Store", "Carga incremental sem downtime"],
        ["RF-P5-01", "P5 — ETL/Integracao", "Eng. de Dados", "Conector (legado)", "APIs/BDs de sistemas legados nem sempre documentados"],
        ["RF-P5-02", "P5 — ETL/Integracao", "Eng. de Dados", "Fila (cron)", "Agendamento confiavel e tolerante a falhas"],
        ["RF-P5-03", "P5 — ETL/Integracao", "Eng. de Dados", "Validacao", "Regras de integridade por sistema fonte"],
        ["RF-P5-04", "P5 — ETL/Integracao", "Eng. de Dados", "Conector (config)", "Complexidade de configuracao por instancia"],
        ["RF-P5-05", "P5 — ETL/Integracao", "Arquiteto", "Nenhum (sem-IA)", "Sem dependencia de GPU confirmado"],
    ]
    
    table3 = doc.add_table(rows=1 + len(trace_data), cols=5)
    table3.autofit = True
    
    headers3 = ["Requisito", "Produto", "Persona", "Gargalo", "Observacao"]
    for j, h in enumerate(headers3):
        table3.rows[0].cells[j].text = h
    
    for i, row_data in enumerate(trace_data):
        for j, val in enumerate(row_data):
            table3.rows[i + 1].cells[j].text = val
    
    format_table(table3)
    
    widths3 = [Cm(2.0), Cm(3.0), Cm(2.5), Cm(3.0), Cm(6.5)]
    for row in table3.rows:
        for idx, width in enumerate(widths3):
            row.cells[idx].width = width
    
    doc.add_page_break()


# ─── SECTION 2: MODELO C4 ────────────────────────────────────────────────────

def create_section_2(doc):
    """Section 2 — Arquitetura de Sistema: Modelo C4."""
    
    add_styled_heading(doc, "2. Arquitetura de Sistema — Modelo C4", level=1)
    add_horizontal_line(doc)
    
    add_body_text(doc, (
        "Esta secao apresenta a arquitetura do sistema NeoGov utilizando o modelo C4 (Context, "
        "Containers, Components, Code). O modelo C4 e uma abordagem hierarquica para visualizacao "
        "de arquitetura de software que permite diferentes niveis de abstracao, desde a visao "
        "macro do sistema em seu ambiente ate os detalhes de componentes internos. Foram produzidos "
        "oito diagramas: um de contexto do sistema (Level 1), seis de containers por produto e camada "
        "global (Level 2), e um detalhamento do pipeline de inferencia GPU (Level 3)."
    ))
    add_body_text(doc, (
        "Cada diagrama e acompanhado de uma descricao narrativa que explica: (i) o que o diagrama "
        "representa; (ii) as decisoes arquiteturais visuais mais relevantes; e (iii) quais requisitos "
        "funcionais e nao-funcionais sao enderecados pela arquitetura ilustrada. Esta abordagem garante "
        "que a arquitetura e tracável ate os requisitos, facilitando validacoes e auditorias."
    ))
    
    # C4-L1-System-Context
    add_styled_heading(doc, "2.1 C4 Level 1 — Contexto do Sistema", level=2)
    add_c4_image(doc, "C4-L1-System-Context.png",
        "Figura 1 — C4 Level 1: Contexto do Sistema NeoGov",
        [
            "O diagrama de contexto apresenta o sistema NeoGov como um todo, inserido em seu ecossistema "
            "de atores externos. Os atores mapeados incluem: o Cidadao/Solicitante LAI (que acessa certidoes "
            "via P3), o DPO/Encarregado (usuario principal do P4 e supervisao geral), o Engenheiro de Dados "
            "(operador de P1 e P5), e o Operador LGPD (responsavel por P2). O sistema interage com fontes "
            "de dados institucionais (banco de dados, sistemas legados, documentos) e com o arcabouco "
            "regulatório (LGPD, LAI, Portarias).",
            
            "A principal decisao arquitetural visivel neste nivel e a segmentacao em cinco produtos independentes "
            "(P1 a P5), cada um com interface propria mas compartilhando uma camada de infraestrutura comum. "
            "O sistema como um todo opera em cloud brasileira (RNF-01), sem dependencia de APIs externas "
            "(RNF-12), garantindo soberania de dados. A separacao clara entre produtos batch (P1, P2, P5) e "
            "produtos interativos (P3, P4) ja e visivel neste nivel de abstracao.",
            
            "Os requisitos enderecados neste diagrama incluem: RNF-01 (soberania de dados em cloud BR), "
            "RNF-02 (multi-tenancy — o sistema atende multiplos orgaos), RNF-09 (disponibilidade 99.5% "
            "do sistema como um todo) e RNF-11 (integracao com sistemas legados). A visao de contexto "
            "tambem estabelece que o NeoGov nao e um sistema isolado, mas parte de um ecossistema maior "
            "de governanca digital publica."
        ]
    )
    
    # C4-L2-Layer1-Global
    add_styled_heading(doc, "2.2 C4 Level 2 — Camada Global (Layer 1)", level=2)
    add_c4_image(doc, "C4-L2-Layer1-Global.png",
        "Figura 2 — C4 Level 2: Camada Global — Recursos Compartilhados",
        [
            "O diagrama da camada global detalha os recursos de infraestrutura compartilhados por todos "
            "os cinco produtos da plataforma. Esta camada inclui: API Gateway (ponto de entrada unificado "
            "com autenticacao e rate limiting), Identity Provider (IdP) para gestao de identidades e "
            "multi-tenancy, banco de dados relacional multi-tenant (PostgreSQL com schema por tenant), "
            "storage de objetos (S3-compatible) para documentos e arquivos, e o servico de fila de jobs "
            "(RabbitMQ/Redis) utilizado pelos produtos batch.",
            
            "A decisao arquitetural mais relevante nesta camada e a separacao explicita entre recursos "
            "compartilhados (Layer 1) e recursos especificos por produto (Layer 2). Os recursos "
            "compartilhados sao dimensionados para atender a capacidade agregada de todos os tenants e "
            "produtos, enquanto os recursos especificos sao escalados conforme a demanda individual de "
            "cada produto. Esta separacao facilita o dimensionamento, o monitoramento e a escalabilidade "
            "independente.",
            
            "Os requisitos enderecados incluem: RNF-02 (multi-tenancy com isolacao logico — implementado "
            "via schemas separados no PostgreSQL e namespaces no storage), RNF-05 (retencao de auditoria — "
            "logs armazenados no storage de objetos com lifecycle policy de 5 anos), RNF-08 (escalabilidade "
            "horizontal — API Gateway e IdP podem ser escalados independentemente), e RNF-09 (disponibilidade "
            "— recursos compartilhados com alta disponibilidade e failover automático)."
        ]
    )
    
    # C4-L2-P1
    add_styled_heading(doc, "2.3 C4 Level 2 — P1 Data Discovery", level=2)
    add_c4_image(doc, "C4-L2-P1-DataDiscovery.png",
        "Figura 3 — C4 Level 2: P1 — Data Discovery",
        [
            "O diagrama do P1 Data Discovery apresenta os containers que compoem este produto: o "
            "Discovery Service (servico principal de varredura), o Connector Manager (gestao de "
            "conectores com fontes de dados), o Rule Engine (motor de classificacao por regras heuristicas), "
            "o Inventory Report Generator (gerador de relatorios de inventario) e o Metadata Store "
            "(armazenamento de metadados coletados).",
            
            "A decisao arquitetural mais relevante neste produto e a ausencia total de componentes de IA. "
            "Conforme RF-P1-02 e RF-P5-05, a classificacao de dados no P1 utiliza exclusivamente regras "
            "pre-definidas (heurísticas de PII baseadas em padroes de CPF, CNPJ, email, etc.), sem "
            "necessidade de GPU. Esta decisao simplifica significativamente a infraestrutura do P1, "
            "reduzindo custo e complexidade. O Connector Manager atua como camada de abstracao sobre "
            "multiplos drivers de banco de dados e conectores de arquivo (RF-P1-05).",
            
            "Os requisitos enderecados incluem: RF-P1-01 a RF-P1-05 (todos os requisitos funcionais do P1), "
            "RNF-11 (conectores multi-fonte), e indiretamente RNF-08 (escalabilidade — o Discovery Service "
            "pode ser escalado horizontalmente para varreduras paralelas). A arquitetura batch com job queue "
            "endereca DA-08, permitindo varreduras agendadas sem impactar outros produtos."
        ]
    )
    
    # C4-L2-P2
    add_styled_heading(doc, "2.4 C4 Level 2 — P2 Anonimizacao", level=2)
    add_c4_image(doc, "C4-L2-P2-Anonimizacao.png",
        "Figura 4 — C4 Level 2: P2 — Anonimizacao",
        [
            "O diagrama do P2 Anonimizacao detalha o pipeline de processamento de documentos para "
            "anonimizacao de dados pessoais. Os containers incluem: o Anonymization Service (orquestrador "
            "do pipeline), o NER Model (modelo de reconhecimento de entidades nomeadas executado em GPU), "
            "o Pre-processor (normalizacao e extracao de texto), o Post-processor (aplicacao de tecnicas "
            "de anonimizacao e validacao), o Job Queue (fila de processamento) e o Anonymized Store "
            "(armazenamento de documentos anonimizados).",
            
            "A decisao arquitetural critica deste produto e a utilizacao de GPU batch sob demanda (DA-02, "
            "RNF-07) em vez de GPU quente reservada. Como o processamento de anonimizacao e assincrono "
            "(RF-P2-02), o sistema tolera tempo de fila sem impactar a experiencia do usuario. As instancias "
            "GPU spot/preemptive sao mais economicas, sendo ativadas conforme a profundidade da fila de jobs. "
            "O Job Queue garante resiliencia com retry automatico em caso de falha da instancia spot.",
            
            "Os requisitos enderecados incluem: RF-P2-01 a RF-P2-05 (todos os requisitos funcionais do P2), "
            "RNF-07 (GPU batch sob demanda), RNF-12 (IA propria local — modelo NER executado na infraestrutura "
            "propria, sem chamadas externas), e RNF-05 (retencao de auditoria — logs de cada job de anonimizacao "
            "armazenados por 5 anos). A arquitetura endereca tambem RF-P2-04 (validacao pos-anonimizacao) "
            "atraves do componente Post-processor dedicado."
        ]
    )
    
    # C4-L2-P3
    add_styled_heading(doc, "2.5 C4 Level 2 — P3 LAI x LGPD", level=2)
    add_c4_image(doc, "C4-L2-P3-LAixLGPD.png",
        "Figura 5 — C4 Level 2: P3 — LAI x LGPD",
        [
            "O diagrama do P3 LAIxLGPD apresenta a arquitetura do servico de decisao automatizada para "
            "certidoes LAI. Os containers incluem: o LAI Service (servico principal de certificacao), "
            "o Legal Reasoning Model (modelo de IA para decisao de revelacao), o Vector Store (base "
            "vetorial de base legal indexada), o Certificate Generator (gerador de certidoes formatadas) "
            "e o Audit Log (registro de decisoes para conformidade).",
            
            "A decisao arquitetural mais critica deste produto e a GPU quente reservada 24/7 (DA-01, "
            "RF-P3-03, RNF-06). O requisito de latencia inferior a 2 segundos (RF-P3-02, RNF-03) exige "
            "que o modelo de IA esteja permanentemente carregado em memoria de video (VRAM), eliminando "
            "qualquer cold start. O custo fixo da GPU reservada e justificado pelo SLA de latencia "
            "interativa e pela natureza sincrona do atendimento ao solicitante. O Vector Store compartilhado "
            "(DA-06) armazena a base legal indexada, utilizada via RAG para fundamentar cada decisao.",
            
            "Os requisitos enderecados incluem: RF-P3-01 a RF-P3-05 (todos os requisitos funcionais do P3), "
            "RNF-03 (latencia < 2s), RNF-06 (GPU quente reservada), RNF-05 (retencao de auditoria — "
            "cada decisao e registrada com entrada, saida e base legal aplicada), RNF-10 (conformidade "
            "LGPD Art. 46 — medidas tecnicas de seguranca), e RNF-12 (IA propria local). A arquitetura "
            "tambem endereca DA-07 (retencao de logs por 5 anos) atraves do Audit Log dedicado."
        ]
    )
    
    # C4-L2-P4
    add_styled_heading(doc, "2.6 C4 Level 2 — P4 AI-DPO", level=2)
    add_c4_image(doc, "C4-L2-P4-AI-DPO.png",
        "Figura 6 — C4 Level 2: P4 — AI-DPO",
        [
            "O diagrama do P4 AI-DPO detalha a arquitetura do assistente conversacional para o "
            "Encarregado de Dados. Os containers incluem: o Chat Service (servico de chat com gestao "
            "de sessao), o LLM (Large Language Model executado em GPU), o RAG Pipeline (pipeline de "
            "retrieval-augmented generation), o Vector Store (base vetorial de conhecimento LGPD por "
            "tenant), o Session Manager (gerenciador de historico e contexto) e o Streaming Gateway "
            "(gateway de streaming de resposta).",
            
            "Assim como o P3, o P4 requer GPU quente reservada 24/7 (DA-01, RF-P4-04, RNF-06) para "
            "atender o requisito de latencia (RF-P4-05, RNF-04 — primeiro token < 3s). A decisao "
            "arquitetural diferencial do P4 e o Vector Store separado por tenant (DA-06), diferente "
            "do P3 que utiliza um Vector Store compartilhado. Esta separacao garante que cada orgao "
            "(tenant) possui sua propria base de conhecimento LGPD customizada, sem contaminacao "
            "cross-tenant. O RAG Pipeline combina recuperacao vetorial com o contexto da sessao para "
            "gerar respostas contextualizadas e precisas.",
            
            "Os requisitos enderecados incluem: RF-P4-01 a RF-P4-06 (todos os requisitos funcionais "
            "do P4), RNF-04 (latencia < 3s), RNF-06 (GPU quente reservada), RNF-12 (IA propria local), "
            "RNF-02 (multi-tenancy — Vector Store e sessoes isoladas por tenant), e RNF-05 (retencao "
            "de historico de conversas por 5 anos). O Streaming Gateway endereca RF-P4-05 (streaming "
            "de resposta) e o Session Manager endereca RF-P4-03 (gestao de sessao e historico)."
        ]
    )
    
    # C4-L2-P5
    add_styled_heading(doc, "2.7 C4 Level 2 — P5 ETL / Integracao", level=2)
    add_c4_image(doc, "C4-L2-P5-ETL-Integracao.png",
        "Figura 7 — C4 Level 2: P5 — ETL / Integracao",
        [
            "O diagrama do P5 ETL/Integracao apresenta a arquitetura de integracao com sistemas "
            "legados governamentais. Os containers incluem: o ETL Service (orquestrador de pipelines "
            "de extracao, transformacao e carga), o Connector Manager (gestao de conectores para "
            "e-Cidade, MV/Tasy, SEI, SIAFI e Class), o Data Validator (validador de integridade "
            "de dados), o Job Scheduler (agendador de jobs batch) e o Staging Area (area temporaria "
            "de preparacao de dados).",
            
            "A decisao arquitetural mais relevante deste produto e a confirmacao de que nao ha "
            "nenhum componente de IA (DA-03, RF-P5-05). O P5 opera exclusivamente com logica "
            "deterministica: extracao via conectores, transformacao por regras configuraveis e "
            "carga com validacao de integridade. O Connector Manager (DA-09) e configurado manualmente "
            "por engenheiro de dados para cada instancia de sistema legado, dada a variabilidade de "
            "APIs, schemas e protocolos encontrados nos diferentes orgaos.",
            
            "Os requisitos enderecados incluem: RF-P5-01 a RF-P5-05 (todos os requisitos funcionais "
            "do P5), RNF-11 (integracao com e-Cidade, MV/Tasy, SEI, SIAFI e Class), e DA-08 (job queue "
            "para batch agendado). O Data Validator endereca RF-P5-03 (validacao de dados durante carga). "
            "A arquitetura sem IA confirma DA-03 e elimina a necessidade de qualquer recurso de GPU "
            "para este produto, mantendo a infraestrutura otimizada em custo."
        ]
    )
    
    # C4-L3-GPU-Inference
    add_styled_heading(doc, "2.8 C4 Level 3 — Pipeline de Inferencia GPU", level=2)
    add_c4_image(doc, "C4-L3-GPU-Inference.png",
        "Figura 8 — C4 Level 3: Pipeline de Inferencia GPU — Detalhamento de Componentes",
        [
            "O diagrama Level 3 detalha o pipeline interno de inferencia GPU, compartilhado conceitualmente "
            "pelos produtos P2, P3 e P4 (embora com configuracoes distintas). Os componentes incluem: "
            "API Inference Server (servidor de inferencia — vLLM/TGI), Model Loader (carregador de modelos "
            "em VRAM), Request Router (roteador de requisicoes — batch vs. interativo), Tokenizer "
            "(tokenizacao de entrada), Inference Engine (motor de inferencia propriamente dito), "
            "Post-processor (pos-processamento de saida) e Monitoring (metricas de latencia e utilizacao).",
            
            "A decisao arquitetural mais significativa neste nivel e a dualidade do Request Router, "
            "que direciona requisicoes para dois modos de operacao distintos: (i) modo interativo para "
            "P3 e P4, com GPU quente reservada e prioridade maxima de latencia; e (ii) modo batch para "
            "P2, com GPU spot sob demanda e processamento por lotes. Esta dualidade permite otimizar "
            "o custo de GPU: os produtos interativos pagam pelo custo fixo da reserva, enquanto o "
            "produto batch se beneficia do custo variavel das instancias spot. O Model Loader garante "
            "que o modelo esta sempre em VRAM para os servicos interativos, eliminando cold starts.",
            
            "Os requisitos enderecados incluem: RNF-03 (latencia < 2s para P3 — garantida pelo "
            "modelo loaded e roteamento prioritario), RNF-04 (latencia < 3s para P4 — garantida pelo "
            "mesmo mecanismo), RNF-06 (GPU quente reservada — implementada via instancia dedicada 24/7), "
            "RNF-07 (GPU batch sob demanda — implementada via instancias spot escaladas pelo Request "
            "Router), e RNF-12 (IA propria local — todo o pipeline executa em infraestrutura propria, "
            "sem dependencia de APIs externas). O componente Monitoring endereca a visibilidade "
            "operacional necessaria para o cumprimento dos SLAs de latencia."
        ]
    )
    
    doc.add_page_break()


# ─── SECTION 3: DECISOES ARQUITETURAIS ───────────────────────────────────────

def create_section_3(doc):
    """Section 3 — Decisoes Arquiteturais."""
    
    add_styled_heading(doc, "3. Decisoes Arquiteturais", level=1)
    add_horizontal_line(doc)
    
    add_body_text(doc, (
        "Esta secao documenta as decisoes arquiteturais fundamentais que nortearam o design da "
        "plataforma NeoGov. Cada decisao e classificada conforme a taxonomia ADR (Architecture "
        "Decision Records) e inclui: identificacao unica (DA-NN), descricao da decisao, justificativa "
        "tecnic ou de negocio, impacto esperado na infraestrutura, e a classe da decisao (ENGENHARIA, "
        "FATO, ANALOGO, PREMISSA). A classe indica o grau de incerteza e reversibilidade da decisao:"
    ))
    
    add_bullet(doc, "ENGENHARIA: Decisao tecnica fundamentada em requisitos funcionais e nao-funcionais claros. Alta confianca.")
    add_bullet(doc, "FATO: Restricao imposta pelo cliente ou pelo contexto (ex: mandato regulatorio). Nao negociavel.")
    add_bullet(doc, "ANALOGO: Decisao por analogia com solucoes similares em outros projetos. Confianca media.")
    add_bullet(doc, "PREMISSA: Assuncao que precisa ser validada durante o piloto. Confianca baixa a media.")
    
    add_body_text(doc, (
        "A classificacao das decisoes permite priorizar esforcos de validacao: premissas devem ser "
        "testadas o mais cedo possivel no piloto, enquanto fatos e decisoes de engenharia possuem "
        "maior estabilidade. As decisoes de engenharia com impacto em custo de infraestrutura (DA-01, "
        "DA-02) devem ser revisadas periodicamente conforme a evolucao dos precos de GPU em cloud BR."
    ))
    
    da_data = [
        [
            "DA-01",
            "GPU quente reservada 24/7 para P3 e P4",
            "O requisito de latencia interativa (< 2s para P3, < 3s para P4) exige que o modelo de IA "
            "esteja permanentemente carregado em VRAM. Qualquer cold start (carregamento sob demanda) "
            "introduz latencia de 30-120s, inviabilizando o SLA. A reserva 24/7 elimina cold starts "
            "e garante latencia previsivel e consistente.",
            "Custo fixo mensal significativo (instancia GPU dedicada). Necessidade de monitorar "
            "utilizacao para otimizar tipo de instancia. Possibilidade de compartilhar a mesma GPU "
            "entre P3 e P4 se a VRAM for suficiente para ambos os modelos simultaneamente.",
            "ENGENHARIA"
        ],
        [
            "DA-02",
            "GPU batch sob demanda (spot) para P2",
            "O processamento de anonimizacao (P2) e assincrono e tolera enfileiramento. O operador LGPD "
            "submete lotes de documentos e recebe o resultado quando o processamento conclui, sem "
            "exigencia de latencia imediata. Instancias spot/preemptive reduzem custo em ate 70% "
            "comparado a instancias reservadas, com tradeoff de possivel preempcao.",
            "Custo variavel proporcional ao volume de processamento. Job queue com retry automatico "
            "para tratar preempcoes de instancia spot. Tempo de fila pode aumentar em periodos de "
            "escassez de GPUs spot na regiao.",
            "ENGENHARIA"
        ],
        [
            "DA-03",
            "P1 e P5 operam sem GPU (sem IA)",
            "Os requisitos funcionais de P1 (RF-P1-02: classificacao por regra) e P5 (RF-P5-05: SEM IA) "
            "confirmam explicitamente que estes produtos nao utilizam modelos de IA. A classificacao "
            "no P1 e baseada em regras heuristicas, e o P5 e puramente deterministico (ETL). Portanto, "
            "nenhum recurso de GPU e necessario para estes produtos.",
            "Reducao significativa de custo de infraestrutura (aproximadamente 60% da plataforma opera "
            "sem GPU). Simplificacao operacional e de monitoramento. Os containers do P1 e P5 podem "
            "executar em instancias CPU comuns, escalando horizontalmente conforme demanda.",
            "ENGENHARIA"
        ],
        [
            "DA-04",
            "Cloud BR para soberania de dados",
            "Mandato explicito do cliente: toda a infraestrutura deve estar localizada em data centers "
            "no Brasil. Esta restricao e derivada de requisitos legais de LGPD (Art. 33 — transferencia "
            "internacional de dados) e de politicas de soberania digital do orgao contratante. "
            "Provedores elegiveis incluem OVH Cloud BR, Locaweb, AWS sa-east-1, Azure Brazil South.",
            "Selecao limitada de provedores e SKUs (instancias GPU podem ser mais caras ou limitadas "
            "em cloud BR). Latencia intra-cloud pode ser superior a regioes nos EUA. Necessidade de "
            "avaliar disponibilidade de instancias GPU com VRAM suficiente (A100/H100) na regiao escolhida.",
            "FATO"
        ],
        [
            "DA-05",
            "Multi-tenancy com isolamento logico",
            "A plataforma atende multiplos orgaos (tenants) a partir de uma unica implantacao. O "
            "isolamento logico (schemas separados no PostgreSQL, namespaces no storage, chaves de "
            "criptografia por tenant) oferece equilibrio entre escalabilidade e custo, evitando "
            "a complexidade e custo de isolamento fisico (instancias separadas por tenant).",
            "Risco teorico de vazamento cross-tenant por bugs na camada de aplicacao. Necessidade de "
            "testes rigorosos de isolamento. Escalabilidade depende de otimizacao de queries multi-tenant. "
            "Migracao para isolamento fisico pode ser necessaria se algum orgao exigir certificação especifica.",
            "ANALOGO"
        ],
        [
            "DA-06",
            "Vector store compartilhado (P3) + separado por tenant (P4)",
            "O P3 (LAIxLGPD) acessa uma base legal padronizada (legislacao LGPD/LAI) que e igual para "
            "todos os tenants — justificando um Vector Store compartilhado. O P4 (AI-DPO) requer "
            "base de conhecimento customizada por orgao (normas internas, orientacoes especificas) — "
            "justificando Vector Store separado por tenant para evitar contaminacao de contexto.",
            "Complexidade adicional na gestao de dois padroes de Vector Store. O Vector Store "
            "compartilhado do P3 requer mecanismo de versionamento para atualizacoes da base legal. "
            "O Vector Store por tenant do P4 pode ter custo de armazenamento significativo com muitos tenants.",
            "PREMISSA"
        ],
        [
            "DA-07",
            "Retencao de auditoria LGPD por 5 anos",
            "O Art. 46 da LGPD exige medidas tecnicas e administrativas de seguranca. A retencao "
            "de logs de auditoria por 5 anos e uma interpretacao conservadora desta exigencia, "
            "alinhada com boas praticas de governanca digital e com o prazo prescricional de acoes "
            "judiciais na esfera administrativa federal.",
            "Custo de storage de logs cresce linearmente ao longo do tempo. Necessidade de politica "
            "de lifecycle (exclusao automatica apos 5 anos). Indexacao de logs para pesquisa eficiente "
            "em periodos longos. Impacto na escolha do storage (deve suportar retention policies).",
            "ENGENHARIA"
        ],
        [
            "DA-08",
            "Job queue para processamento batch (P1, P2, P5)",
            "Os produtos batch (P1, P2, P5) compartilham o padrao de processamento assincrono: "
            "tarefas sao enfileiradas, processadas por workers e o resultado e armazenado para "
            "consulta posterior. Um job queue centralizado (RabbitMQ/Redis) com priorizacao por "
            "produto e tenant permite gerenciar a carga de forma eficiente e resiliente.",
            "Ponto unico de falha se o job queue nao tiver alta disponibilidade. Necessidade de "
            "monitoramento de profundidade de fila e tempo de processamento. Dead letter queue para "
            "jobs que falham repetidamente. Escalonamento horizontal de workers conforme demanda.",
            "ENGENHARIA"
        ],
        [
            "DA-09",
            "Connector manager com setup manual por engenheiro",
            "A diversidade de sistemas legados (e-Cidade, MV/Tasy, SEI, SIAFI, Class) com APIs, "
            "schemas e protocolos variados nao permite automacao completa do setup de conectores. "
            "Cada instancia de sistema legado pode ter versoes diferentes, customizações locais e "
            "configuracoes especificas que exigem intervencao manual de um engenheiro de dados.",
            "Tempo de onboarding de novos tenants e fontes de dados e maior (depende de disponibilidade "
            "de engenheiro). Necessidade de documentacao detalhada para cada conector configurado. "
            "Possibilidade de criar um catalogo de templates de conectores para acelerar setups futuros.",
            "ENGENHARIA"
        ],
    ]
    
    table = doc.add_table(rows=1 + len(da_data), cols=5)
    table.autofit = True
    
    headers = ["ID", "Decisao", "Justificativa", "Impacto", "Classe"]
    for j, h in enumerate(headers):
        table.rows[0].cells[j].text = h
    
    for i, row_data in enumerate(da_data):
        for j, val in enumerate(row_data):
            table.rows[i + 1].cells[j].text = val
    
    format_table(table)
    
    widths = [Cm(1.5), Cm(3.5), Cm(5.0), Cm(4.0), Cm(2.0)]
    for row in table.rows:
        for idx, width in enumerate(widths):
            row.cells[idx].width = width
    
    doc.add_page_break()


# ─── SECTION 4: DERIVACAO DE INFRAESTRUTURA ──────────────────────────────────

def create_section_4(doc):
    """Section 4 — Derivacao de Infraestrutura."""
    
    add_styled_heading(doc, "4. Derivacao de Infraestrutura a partir da Arquitetura", level=1)
    add_horizontal_line(doc)
    
    add_body_text(doc, (
        "Esta secao apresenta a derivacao dos recursos de infraestrutura a partir da arquitetura C4 "
        "e das decisoes arquiteturais documentadas. A abordagem segue o principio de tracabilidade: "
        "cada recurso de infraestrutura e justificado por um ou mais requisitos ou decisoes "
        "arquiteturais. A infraestrutura e organizada em duas camadas: Layer 1 (recursos compartilhados "
        "por todos os produtos) e Layer 2 (recursos especificos por produto). Esta separacao permite "
        "dimensionamento independente e otimizacao de custos."
    ))
    add_body_text(doc, (
        "A derivacao utiliza a classificacao de recursos como Fixo (custo constante mensal, provisionado "
        "permanentemente) ou Variavel (custo proporcional ao uso, escalado conforme demanda). Recursos "
        "fixos sao justificados por requisitos de latencia ou disponibilidade, enquanto recursos "
        "variaveis sao justificados por workloads batch tolerantes a enfileiramento. Esta classificacao "
        "e fundamental para o modelo de custos apresentado na planilha de dimensionamento complementar."
    ))
    
    # ── 4.1 Layer 1 ──
    add_styled_heading(doc, "4.1 Layer 1 — Recursos Compartilhados", level=2)
    
    add_body_text(doc, (
        "A tabela abaixo lista todos os recursos de infraestrutura compartilhados entre os cinco "
        "produtos da plataforma. Estes recursos formam a base da plataforma e devem ser dimensionados "
        "para a capacidade agregada de todos os tenants ativos. A classe de cada recurso indica sua "
        "natureza (Fixo ou Variavel) e o grau de incerteza na estimativa."
    ))
    
    layer1_data = [
        ["API Gateway", "Fixo", "Ponto de entrada unificado com autenticacao (JWT), rate limiting e roteamento para os cinco produtos. Necessidade de alta disponibilidade (RNF-09).", "Infra"],
        ["Identity Provider (IdP)", "Fixo", "Gestao de identidades multi-tenant com SSO, RBAC e provisionamento por orgao. Integracao com LDAP/AD dos orgaos.", "Infra"],
        ["PostgreSQL Multi-tenant", "Fixo", "Banco de dados relacional com schema separado por tenant. Armazena metadados, configuracoes, usuarios, audit logs. HA com failover.", "Dados"],
        ["Object Storage (S3)", "Fixo", "Storage de documentos, arquivos anonimizados, relatorios, modelos de IA e backups. Lifecycle policy para retencao de 5 anos (DA-07).", "Dados"],
        ["Redis Cache", "Fixo", "Cache de sessao (P3, P4), cache de metadados (P1), rate limiting e filas de alta velocidade. Cluster com replicacao.", "Cache"],
        ["RabbitMQ / Job Queue", "Fixo", "Fila de processamento batch para P1, P2 e P5 (DA-08). Suporte a priorizacao, retry e dead letter queue. HA com mirroring.", "Fila"],
        ["Prometheus + Grafana", "Fixo", "Monitoramento centralizado: metricas de latencia (RNF-03, RNF-04), utilizacao de GPU, profundidade de filas e saude dos servicos.", "Observabilidade"],
        ["ELK Stack / Loki", "Fixo", "Central de logs agregados para debugging, auditoria (RNF-05) e analise de incidentes. Retention policy de 5 anos.", "Observabilidade"],
        ["Vault / KMS", "Fixo", "Gestao de secrets, chaves de criptografia por tenant e certificates. Encriptacao em transito (TLS) e repouso (AES-256) — RNF-10.", "Seguranca"],
        ["Kubernetes Cluster", "Fixo", "Orquestracao de containers para todos os servicos. Autoscaling horizontal (RNF-08), self-healing e rolling updates.", "Infra"],
        ["CDN / Load Balancer", "Fixo", "Distribuicao de carga para servicos web, assets estaticos e cache de borda. Necessario para disponibilidade (RNF-09).", "Infra"],
    ]
    
    table1 = doc.add_table(rows=1 + len(layer1_data), cols=4)
    table1.autofit = True
    
    headers1 = ["Recurso", "Tipo", "Justificativa", "Classe"]
    for j, h in enumerate(headers1):
        table1.rows[0].cells[j].text = h
    
    for i, row_data in enumerate(layer1_data):
        for j, val in enumerate(row_data):
            table1.rows[i + 1].cells[j].text = val
    
    format_table(table1)
    
    widths1 = [Cm(3.5), Cm(1.5), Cm(9.0), Cm(2.0)]
    for row in table1.rows:
        for idx, width in enumerate(widths1):
            row.cells[idx].width = width
    
    doc.add_paragraph()
    
    # ── 4.2 Layer 2 ──
    add_styled_heading(doc, "4.2 Layer 2 — Recursos por Produto", level=2)
    
    add_body_text(doc, (
        "A tabela abaixo detalha os recursos de infraestrutura especificos de cada produto. "
        "Estes recursos sao escalados de forma independente, permitindo que cada produto cresca "
        "conforme sua demanda sem impactar os demais. A classificacao Fixo/Variavel e derivada "
        "diretamente das decisoes arquiteturais e dos requisitos de latencia de cada produto."
    ))
    
    layer2_data = [
        # P1
        ["P1 — Data Discovery", "Discovery Service (CPU)", "Variavel", "Servico de varredura batch. Escala horizontalmente conforme numero de fontes e tenants. Sem GPU (DA-03).", "Compute"],
        ["P1 — Data Discovery", "Rule Engine (CPU)", "Fixo", "Motor de classificacao por regras heuristicas. CPU dedicada para processamento deterministico (RF-P1-02).", "Compute"],
        ["P1 — Data Discovery", "Metadata Store (DB)", "Fixo", "Armazenamento de metadados coletados. Extensao do PostgreSQL multi-tenant com tabelas especificas do P1.", "Dados"],
        ["P1 — Data Discovery", "Connector Manager", "Fixo", "Servico de gestao de conectores multi-fonte (RF-P1-05). Setup manual por engenheiro (DA-09).", "Infra"],
        # P2
        ["P2 — Anonimizacao", "Anonymization Service", "Variavel", "Orquestrador do pipeline de anonimizacao. Escala conforme volume de documentos na fila.", "Compute"],
        ["P2 — Anonimizacao", "GPU Batch (Spot)", "Variavel", "Instancias GPU spot para inferencia NER (DA-02, RNF-07). Escala conforme profundidade da fila de jobs.", "GPU"],
        ["P2 — Anonimizacao", "Anonymized Store", "Fixo", "Storage de documentos anonimizados. Ciclo de vida: armazenamento temporario + arquivamento longo prazo.", "Dados"],
        ["P2 — Anonimizacao", "NER Model Storage", "Fixo", "Armazenamento dos artefatos do modelo NER (pesos, tokenizer, configuracao). Versionamento por modelo.", "Modelo"],
        # P3
        ["P3 — LAIxLGPD", "LAI Service (CPU)", "Fixo", "Servico de certificacao com logica de negocio e integracao com o modelo de IA.", "Compute"],
        ["P3 — LAIxLGPD", "GPU Quente Reservada (A100)", "Fixo", "GPU dedicada 24/7 com modelo loaded (DA-01, RF-P3-03, RNF-06). A100 40GB ou superior para modelo legal.", "GPU"],
        ["P3 — LAIxLGPD", "Vector Store (Base Legal)", "Fixo", "Base vetorial compartilhada de legislacao LGPD/LAI (DA-06). Indexada e atualizada periodicamente.", "Dados"],
        ["P3 — LAIxLGPD", "Audit Log Store", "Fixo", "Registro imutavel de decisoes para auditoria (RF-P3-05, DA-07). Retencao minima de 5 anos.", "Dados"],
        # P4
        ["P4 — AI-DPO", "Chat Service (CPU)", "Fixo", "Servico de chat com gestao de sessao, streaming e integracao com RAG Pipeline.", "Compute"],
        ["P4 — AI-DPO", "GPU Quente Reservada (A100)", "Fixo", "GPU dedicada 24/7 com LLM loaded (DA-01, RF-P4-04, RNF-06). A100 80GB preferencial para modelo grande.", "GPU"],
        ["P4 — AI-DPO", "Vector Store (por Tenant)", "Fixo", "Base vetorial isolada por tenant com conhecimento LGPD customizado (DA-06). Custo cresce com tenants.", "Dados"],
        ["P4 — AI-DPO", "Session Store (Redis)", "Fixo", "Armazenamento de sessoes e historico de conversas (RF-P4-03). TTL configuravel com backup periodico.", "Cache"],
        # P5
        ["P5 — ETL/Integracao", "ETL Service (CPU)", "Variavel", "Orquestrador de pipelines ETL batch. Escala conforme numero de jobs agendados e volume de dados.", "Compute"],
        ["P5 — ETL/Integracao", "Job Scheduler", "Fixo", "Agendador de jobs batch com cron configuravel por tenant (RF-P5-02). Integracao com RabbitMQ (DA-08).", "Fila"],
        ["P5 — ETL/Integracao", "Staging Area", "Fixo", "Area temporaria de preparacao de dados antes da carga final. Limpeza automatica pos-processamento.", "Dados"],
        ["P5 — ETL/Integracao", "Connector Manager (P5)", "Fixo", "Gestao de conectores para sistemas legados (RF-P5-01, DA-09). Configuracao manual por engenheiro.", "Infra"],
    ]
    
    table2 = doc.add_table(rows=1 + len(layer2_data), cols=5)
    table2.autofit = True
    
    headers2 = ["Produto", "Recurso", "Tipo (F/V)", "Justificativa", "Classe"]
    for j, h in enumerate(headers2):
        table2.rows[0].cells[j].text = h
    
    for i, row_data in enumerate(layer2_data):
        for j, val in enumerate(row_data):
            table2.rows[i + 1].cells[j].text = val
    
    format_table(table2)
    
    widths2 = [Cm(3.0), Cm(3.5), Cm(1.5), Cm(6.5), Cm(1.5)]
    for row in table2.rows:
        for idx, width in enumerate(widths2):
            row.cells[idx].width = width
    
    doc.add_paragraph()
    
    # ── 4.3 Validacoes Cruzadas ──
    add_styled_heading(doc, "4.3 Validacoes Cruzadas", level=2)
    
    add_body_text(doc, (
        "As validacoes cruzadas verificam a coerencia entre a arquitetura proposta, as decisoes "
        "arquiteturais e os requisitos originais. Estas validacoes sao essenciais para identificar "
        "contradicoes ou inconsistencias antes da fase de implementacao. As tres validacoes principais "
        "sao apresentadas abaixo:"
    ))
    
    add_body_text(doc, "Validacao 1: P1 e P5 NAO possuem GPU", bold=True)
    add_body_text(doc, (
        "Coerencia verificada: os requisitos funcionais RF-P1-02 (classificacao por regra sem IA) e "
        "RF-P5-05 (SEM IA) confirmam explicitamente que P1 e P5 nao utilizam inteligencia artificial. "
        "A decisao arquitetural DA-03 formaliza esta restricao. Na derivacao de infraestrutura, nenhum "
        "recurso GPU foi alocado para P1 ou P5. Todos os seus containers executam exclusivamente em "
        "instancias CPU, reduzindo significativamente o custo total da plataforma. Esta validacao "
        "confirma que aproximadamente 40% dos produtos (2 de 5) operam sem dependencia de GPU."
    ))
    
    add_body_text(doc, "Validacao 2: P3 e P4 possuem GPU quente FIXA", bold=True)
    add_body_text(doc, (
        "Coerencia verificada: os requisitos RF-P3-03 e RF-P4-04 exigem GPU quente reservada 24/7, "
        "e os RNF-03 e RNF-04 estabelecem latencias maximas de 2s e 3s, respectivamente. A decisao "
        "arquitetural DA-01 justifica a reserva permanente de GPU para eliminar cold starts. Na "
        "derivacao de infraestrutura, tanto P3 quanto P4 possuem recursos GPU classificados como "
        "'Fixo', com instancia A100 dedicada. O custo fixo e justificado pelo SLA de latencia "
        "interativa. Uma possivel otimizacao futura seria compartilhar uma unica GPU A100 80GB "
        "entre P3 e P4, se a VRAM for suficiente para carregar ambos os modelos simultaneamente — "
        "isto requer validacao em piloto."
    ))
    
    add_body_text(doc, "Validacao 3: P2 possui GPU batch VARIABLE", bold=True)
    add_body_text(doc, (
        "Coerencia verificada: o requisito RF-P2-02 (job queue) e o RNF-07 (GPU batch sob demanda) "
        "confirmam que o processamento de anonimizacao e assincrono e tolera enfileiramento. A decisao "
        "arquitetural DA-02 formaliza a escolha de instancias spot/preemptive para P2. Na derivacao "
        "de infraestrutura, o recurso GPU do P2 e classificado como 'Variavel', escalando conforme "
        "a profundidade da fila de jobs. O custo variavel e significativamente menor que o fixo, "
        "mas o tradeoff e a possibilidade de preempcao (requer retry automatico no job queue). "
        "Esta validacao confirma que a estrategia de GPU do P2 e ortogonal e complementar a dos "
        "produtos interativos."
    ))
    
    doc.add_page_break()


# ─── SECTION 5: CORRECOES E AJUSTES ──────────────────────────────────────────

def create_section_5(doc):
    """Section 5 — Correcoes e Ajustes vs Dimensionamento Anterior."""
    
    add_styled_heading(doc, "5. Correcoes e Ajustes vs Dimensionamento Anterior", level=1)
    add_horizontal_line(doc)
    
    add_body_text(doc, (
        "Esta secao apresenta as correcoes e ajustes identificados durante a analise arquitetural "
        "em relacao ao dimensionamento de infraestrutura anterior (planilha de dimensionamento v1.20.1). "
        "A analise comparativa entre a engenharia de requisitos, o modelo C4 e o dimensionamento "
        "anterior revelou discrepancias que precisam ser corrigidas para garantir a coerencia do "
        "projeto. Cada item e classificado quanto ao tipo de correcao e a acao requerida."
    ))
    add_body_text(doc, (
        "As discrepancias foram categorizadas em tres niveis de criticidade: (i) Correcao Imediata — "
        "inconsistencia que deve ser resolvida antes da implementacao; (ii) Validacao em Piloto — "
        "premissa que precisa ser testada durante a fase piloto antes de confirmar o dimensionamento; "
        "e (iii) Ajuste Futuro — melhoria identificada que pode ser adiada para iteracoes futuras "
        "sem impacto na viabilidade do projeto."
    ))
    
    corrections_data = [
        [
            "COR-01",
            "GPU alocada para P1 no dimensionamento anterior",
            "A planilha anterior incluia custo de GPU para P1 (Data Discovery). Apos analise dos "
            "requisitos funcionais (RF-P1-02: classificacao por regra, sem IA) e da decisao DA-03, "
            "foi confirmado que P1 nao necessita de GPU. O custo de GPU do P1 foi removido.",
            "Correcao Imediata",
            "Removido recurso GPU de P1 na planilha. Economia estimada de 15-20% no custo mensal de GPU."
        ],
        [
            "COR-02",
            "GPU alocada para P5 no dimensionamento anterior",
            "Similar ao COR-01, a planilha anterior incluia GPU para P5 (ETL/Integracao). O requisito "
            "RF-P5-05 (SEM IA) e a decisao DA-03 confirmam a ausencia de dependencia de GPU para P5. "
            "O custo foi removido.",
            "Correcao Imediata",
            "Removido recurso GPU de P5. Economia estimada adicional de 10-15% no custo mensal."
        ],
        [
            "COR-03",
            "GPU do P2 classificada como Fixa em vez de Variavel",
            "A planilha anterior classificava a GPU do P2 como custo fixo mensal. Apos analise do "
            "RNF-07 (GPU batch sob demanda) e DA-02, foi reclassificada como Variavel, refletindo "
            "o uso de instancias spot que escalam conforme demanda.",
            "Correcao Imediata",
            "Reclassificado GPU P2 de Fixo para Variavel. Custo agora proporcional ao volume de jobs."
        ],
        [
            "COR-04",
            "Ausencia de Vector Store no dimensionamento anterior",
            "O dimensionamento anterior nao incluia custo de Vector Store para P3 e P4. A analise "
            "arquitetural (DA-06, RF-P4-02) identificou a necessidade de bases vetoriais para RAG. "
            "Estimativa de custo adicionada.",
            "Correcao Imediata",
            "Adicionado Vector Store compartilhado (P3) e por tenant (P4). Custo varia com numero de tenants."
        ],
        [
            "COR-05",
            "Retencao de logs configurada para 2 anos (deveria ser 5)",
            "A planilha anterior configurava retention policy de 2 anos para logs de auditoria. O "
            "DA-07 e o RNF-05 estabelecem retencao minima de 5 anos conforme Art. 46 da LGPD.",
            "Correcao Imediata",
            "Ajustado retention policy para 5 anos. Impacto no custo de storage de logs (+150% estimado)."
        ],
        [
            "COR-06",
            "GPU compartilhada entre P3 e P4 (premissa nao validada)",
            "A planilha anterior assumia que P3 e P4 poderiam compartilhar uma unica GPU A100 80GB. "
            "Esta premissa depende da VRAM combinada dos modelos caber em uma unica instancia, "
            "o que precisa ser validado em piloto com os modelos reais.",
            "Validacao em Piloto",
            "Piloto deve medir VRAM utilizada por cada modelo simultaneamente. Se nao couber, "
            "provisionar GPU separada para cada produto (custo +100%)."
        ],
        [
            "COR-07",
            "Tipo de instancia GPU nao especificado para P3/P4",
            "O dimensionamento anterior nao especificava o tipo exato de instancia GPU. A analise "
            "arquitetural indica necessidade de A100 (40GB para P3, 80GB preferencial para P4) "
            "para acomodar os modelos de IA com margem de seguranca.",
            "Validacao em Piloto",
            "Piloto deve testar com A100 40GB e 80GB para determinar o SKU otimo por produto. "
            "Disponibilidade em cloud BR deve ser verificada."
        ],
        [
            "COR-08",
            "Custo de Connector Manager nao incluido no dimensionamento",
            "A analise arquitetural identificou o Connector Manager como componente distinto para "
            "P1 e P5 (DA-09), com custo de manutencao e configuracao manual por engenheiro. Este "
            "custo operacional nao estava refletido na planilha.",
            "Ajuste Futuro",
            "Adicionar estimativa de horas de engenharia para configuracao de conectores por tenant. "
            "Pode ser modelado como custo de setup (capex) + manutencao (opex)."
        ],
        [
            "COR-09",
            "Monitoramento e observabilidade subestimados",
            "O dimensionamento anterior alocava recursos minimos para monitoramento. A arquitetura C4 "
            "requer stack completa (Prometheus + Grafana + ELK) com retention de 5 anos, implicando "
            "custo significativo de storage e compute para os servicos de observabilidade.",
            "Ajuste Futuro",
            "Revisar dimensionamento de storage para logs e metricas. Considerar tiered storage "
            "(hot/warm/cold) para otimizar custo de retencao de 5 anos."
        ],
        [
            "COR-10",
            "Cenario de disaster recovery nao abordado",
            "A planilha anterior contemplava apenas o cenario de operacao normal. A arquitetura "
            "arquitetural sugere necessidade de DR (replicacao cross-region ou backup offsite) "
            "para atender RNF-09 (99.5% disponibilidade) em caso de falha regional.",
            "Validacao em Piloto",
            "Piloto deve definir estrategia de DR: active-passive com replica em regiao secundaria "
            "ou backup periodico em storage externo. Impacto significativo no custo total."
        ],
    ]
    
    table = doc.add_table(rows=1 + len(corrections_data), cols=5)
    table.autofit = True
    
    headers = ["ID", "Discrepancia Identificada", "Descricao e Analise", "Acao Requerida", "Impacto Estimado"]
    for j, h in enumerate(headers):
        table.rows[0].cells[j].text = h
    
    for i, row_data in enumerate(corrections_data):
        for j, val in enumerate(row_data):
            table.rows[i + 1].cells[j].text = val
    
    format_table(table)
    
    widths = [Cm(1.5), Cm(3.0), Cm(5.0), Cm(2.5), Cm(4.5)]
    for row in table.rows:
        for idx, width in enumerate(widths):
            row.cells[idx].width = width
    
    doc.add_paragraph()
    
    # Summary
    add_styled_heading(doc, "5.1 Resumo das Correcoes", level=2)
    
    add_body_text(doc, (
        "Em resumo, a analise arquitetural identificou 10 discrepancias entre o dimensionamento "
        "anterior e a arquitetura proposta. Destas, 5 requerem correcao imediata (COR-01 a COR-05), "
        "3 necessitam de validacao durante o piloto (COR-06, COR-07, COR-10), e 2 podem ser "
        "ajustadas em iteracoes futuras (COR-08, COR-09). As correcoes imediatas resultam em "
        "reducao de custo de GPU (remocao de P1 e P5) compensada pela adicao de Vector Store "
        "e aumento da retencao de logs. O saldo liquido depende dos custos reais dos provedores "
        "de cloud BR, a serem confirmados durante o piloto."
    ))
    add_body_text(doc, (
        "O impacto mais significativo nas correcoes imediatas e a realocacao de recursos de GPU: "
        "a remocao de GPU de P1 e P5 reduz o custo de GPU em aproximadamente 25-35%, enquanto a "
        "reclassificacao de GPU do P2 de Fixo para Variavel introduz incerteza no custo mensal "
        "(depende do volume de processamento). A adicao de Vector Store e o aumento da retencao "
        "de logs representam custos adicionais que devem ser orçados. Recomenda-se que o piloto "
        "inclua medicao precisa de todos os recursos para calibrar o modelo de custos final."
    ))


# ─── MAIN ─────────────────────────────────────────────────────────────────────

def main():
    print("Criando documento NeoGov — Arquitetura de Infraestrutura v1.20.1...")
    
    doc = Document()
    
    # Configure default style
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Calibri'
    font.size = Pt(11)
    
    # Configure heading styles
    for level in range(1, 4):
        h_style = doc.styles[f'Heading {level}']
        h_style.font.name = 'Calibri'
        h_style.font.color.rgb = DARK_BLUE
    
    # Configure page margins
    set_page_margins(doc.sections[0])
    add_footer_page_number(doc.sections[0])
    
    # Build document sections
    create_cover_page(doc)
    create_section_1(doc)
    create_section_2(doc)
    create_section_3(doc)
    create_section_4(doc)
    create_section_5(doc)
    
    # Save
    doc.save(OUTPUT_PATH)
    print(f"Documento salvo com sucesso: {OUTPUT_PATH}")
    print(f"Tamanho do arquivo: {os.path.getsize(OUTPUT_PATH) / 1024:.1f} KB")


if __name__ == "__main__":
    main()
