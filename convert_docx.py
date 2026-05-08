#!/usr/bin/env python3
"""Convert DOCX files to Markdown with heading styles and table support."""

import sys
from pathlib import Path
from docx import Document

OUTPUT_DIR = Path("/home/cnmfs/ICT/PROTOTYPE/LAYER/LGPD")

FILES = [
    (
        "/home/cnmfs/ICT/PROTOTYPE/LAYER/LGPD/drive-files/LGPD/DIVISÃO DE FUNÇÕES E CRONOGRAMA.docx",
        "divisao-funcoes-cronograma.md",
    ),
    (
        "/home/cnmfs/ICT/PROTOTYPE/LAYER/LGPD/drive-files/LGPD/Inteligência de Mercado GovTech LGPD.docx",
        "inteligencia-mercado-govtech-lgpd.md",
    ),
    (
        "/home/cnmfs/ICT/PROTOTYPE/LAYER/LGPD/drive-files/LGPD/PLANO DE NEGÓCIOS: CIT AI TECH – GOVTECH & LGPD.docx",
        "plano-negocios-cit-ai-tech.md",
    ),
]


def extract_table(table):
    """Convert a python-docx Table to a markdown table string."""
    rows = []
    for row in table.rows:
        cells = []
        for cell in row.cells:
            text = cell.text.strip().replace("\n", " ").replace("|", "\\|")
            cells.append(text)
        rows.append(cells)

    if not rows:
        return ""

    # Calculate column widths (just use max content length for alignment)
    num_cols = max(len(r) for r in rows)
    # Pad rows to same length
    for r in rows:
        while len(r) < num_cols:
            r.append("")

    lines = []
    # Header row
    lines.append("| " + " | ".join(rows[0]) + " |")
    # Separator
    lines.append("| " + " | ".join(["---"] * num_cols) + " |")
    # Data rows
    for row in rows[1:]:
        lines.append("| " + " | ".join(row) + " |")

    return "\n".join(lines)


def run_bold_italic(paragraph):
    """Extract runs with **bold** and *italic* formatting."""
    parts = []
    for run in paragraph.runs:
        text = run.text
        if not text:
            continue
        bold = run.bold
        italic = run.italic
        if bold and italic:
            parts.append(f"***{text}***")
        elif bold:
            parts.append(f"**{text}**")
        elif italic:
            parts.append(f"*{text}*")
        else:
            parts.append(text)
    return "".join(parts) if parts else paragraph.text


def convert_docx_to_md(docx_path: str) -> str:
    """Convert a single DOCX file to Markdown string."""
    doc = Document(docx_path)
    md_lines = []

    # Build an ordered list of (type, element) where type is 'para' or 'table'
    # based on document body order
    from docx.oxml.ns import qn

    body = doc.element.body
    para_map = {p._element: p for p in doc.paragraphs}
    table_map = {t._element: t for t in doc.tables}

    for child in body:
        if child.tag == qn("w:p"):
            para = para_map.get(child)
            if para is None:
                continue
            style_name = para.style.name if para.style else ""

            # Detect heading level
            if style_name.startswith("Heading"):
                try:
                    level = int(style_name.split()[-1])
                except ValueError:
                    level = 1
                prefix = "#" * level
                text = run_bold_italic(para).strip()
                md_lines.append(f"{prefix} {text}")
            elif style_name == "Title":
                text = run_bold_italic(para).strip()
                md_lines.append(f"# {text}")
            elif style_name == "Subtitle":
                text = run_bold_italic(para).strip()
                md_lines.append(f"## {text}")
            elif style_name.startswith("List"):
                text = run_bold_italic(para).strip()
                md_lines.append(f"- {text}")
            elif style_name.startswith("TOC"):
                # Skip table of contents entries
                continue
            else:
                text = run_bold_italic(para).strip()
                if text:
                    md_lines.append(text)
                else:
                    md_lines.append("")

        elif child.tag == qn("w:tbl"):
            table = table_map.get(child)
            if table:
                md_lines.append("")
                md_lines.append(extract_table(table))
                md_lines.append("")

    # Clean up excessive blank lines
    result = "\n".join(md_lines)
    while "\n\n\n" in result:
        result = result.replace("\n\n\n", "\n\n")
    return result.strip() + "\n"


def main():
    for docx_path, md_name in FILES:
        print(f"\n{'='*70}")
        print(f"Converting: {docx_path}")
        print(f"        ->: {OUTPUT_DIR / md_name}")
        print(f"{'='*70}\n")

        md_content = convert_docx_to_md(docx_path)
        out_path = OUTPUT_DIR / md_name
        out_path.write_text(md_content, encoding="utf-8")

        print(md_content)
        print(f"\n[OK] Written {len(md_content)} chars to {out_path}")

    print(f"\n{'='*70}")
    print("FILES CREATED:")
    print(f"{'='*70}")
    for _, md_name in FILES:
        p = OUTPUT_DIR / md_name
        size = p.stat().st_size
        print(f"  {p}  ({size:,} bytes)")


if __name__ == "__main__":
    main()
