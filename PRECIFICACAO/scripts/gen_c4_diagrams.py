#!/usr/bin/env python3
"""
NeoGov — Gerador de Diagramas C4 (Arquitetura de Infraestrutura)
v1.0 | Gera diagramas C4 Level 1/2/3 via Playwright + CSS puro
Saída: 8 PNGs em /home/z/my-project/download/c4/
"""

import os, json
from playwright.sync_api import sync_playwright

OUT_DIR = "/home/z/my-project/download/c4"
os.makedirs(OUT_DIR, exist_ok=True)

# ============================================================
# C4 CSS TEMPLATE (embedded)
# ============================================================
C4_CSS = """
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: 'Segoe UI', Arial, sans-serif; background: #fff; padding: 24px; }
.diagram { position: relative; }
/* C4 Color Scheme */
.c4-person { background: #08427B; color: #fff; border: 2px solid #073B6F; }
.c4-system { background: #1168BD; color: #fff; border: 2px solid #0E5FA4; }
.c4-external { background: #999; color: #fff; border: 2px solid #7A7A7A; }
.c4-container { background: #438DD5; color: #fff; border: 2px solid #3872B0; }
.c4-container-app { background: #438DD5; color: #fff; border: 2px solid #3872B0; }
.c4-container-db { background: #438DD5; color: #fff; border: 2px solid #3872B0; }
.c4-component { background: #85BBF0; color: #333; border: 2px solid #6C9BD2; }
.c4-boundary { border: 2px dashed #999; background: rgba(68,141,213,0.03); }
.box {
  position: absolute; border-radius: 6px; display: flex; flex-direction: column;
  align-items: center; justify-content: center; text-align: center; padding: 6px 8px;
  z-index: 2; line-height: 1.3;
}
.box .label { font-size: 12px; font-weight: 600; }
.box .tech { font-size: 9px; opacity: 0.75; margin-top: 2px; }
.box .desc { font-size: 9px; opacity: 0.7; margin-top: 1px; }
.boundary {
  position: absolute; border-radius: 10px; z-index: 1;
}
.boundary-label {
  position: absolute; top: -12px; left: 14px; background: #fff; padding: 0 6px;
  font-size: 13px; font-weight: 700; color: #555; z-index: 3;
}
.svg-lines { position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 1; pointer-events: none; }
.conn-label { font-size: 9px; fill: #555; font-family: 'Segoe UI', Arial, sans-serif; }
.page-title { font-size: 16px; font-weight: 700; color: #333; margin-bottom: 4px; }
.page-sub { font-size: 11px; color: #888; margin-bottom: 14px; }
.legend { position: absolute; bottom: 8px; right: 8px; display: flex; gap: 12px; z-index: 5; }
.legend-item { display: flex; align-items: center; gap: 4px; font-size: 9px; color: #666; }
.legend-box { width: 14px; height: 10px; border-radius: 2px; border: 1px solid #999; }
"""


def make_arrow_svg(connections, W, H):
    """Generate SVG with arrow connections."""
    lines = []
    lines.append(f'<svg class="svg-lines" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">')
    lines.append('<defs>')
    lines.append('<marker id="arrowhead" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">')
    lines.append('<path d="M 0 0 L 10 5 L 0 10 z" fill="#888"/>')
    lines.append('</marker>')
    lines.append('</defs>')
    for c in connections:
        x1, y1, x2, y2 = c["x1"], c["y1"], c["x2"], c["y2"]
        label = c.get("label", "")
        lx = (x1 + x2) / 2
        ly = (y1 + y2) / 2 - 6
        lines.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#888" stroke-width="1.5" marker-end="url(#arrowhead)"/>')
        if label:
            lines.append(f'<text x="{lx}" y="{ly}" text-anchor="middle" class="conn-label">{label}</text>')
    lines.append('</svg>')
    return "\n".join(lines)


def render_diagram(title, subtitle, W, H, boxes, connections, boundaries, filename):
    """Render a C4 diagram as PNG using Playwright."""
    # Build HTML
    html_boxes = ""
    for b in boxes:
        cls = b.get("cls", "c4-container")
        html_boxes += f'''<div class="box {cls}" style="left:{b['x']}px;top:{b['y']}px;width:{b['w']}px;height:{b['h']}px;">
      <span class="label">{b['label']}</span>
      {f'<span class="tech">{b["tech"]}</span>' if "tech" in b else ""}
      {f'<span class="desc">{b["desc"]}</span>' if "desc" in b else ""}
    </div>\n'''

    html_bounds = ""
    for b in boundaries:
        html_bounds += f'''<div class="boundary c4-boundary" style="left:{b['x']}px;top:{b['y']}px;width:{b['w']}px;height:{b['h']}px;">
      <span class="boundary-label">{b['label']}</span>
    </div>\n'''

    svg = make_arrow_svg(connections, W, H)

    html = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><style>{C4_CSS}</style></head>
<body>
<div class="page-title">{title}</div>
<div class="page-sub">{subtitle}</div>
<div class="diagram" style="width:{W}px;height:{H}px;">
{svg}
{html_bounds}
{html_boxes}
</div>
</body></html>"""

    # Render
    html_path = f"/tmp/c4_{filename}.html"
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)

    with sync_playwright() as p:
        browser = p.chromium.launch(args=["--no-sandbox"])
        page = browser.new_page(viewport={"width": W + 48, "height": H + 80})
        page.goto(f"file://{html_path}")
        page.wait_for_timeout(500)
        out_path = os.path.join(OUT_DIR, filename)
        page.screenshot(path=out_path, full_page=True)
        browser.close()

    os.remove(html_path)
    print(f"  [OK] {filename}")


# ============================================================
# D1: C4 Level 1 — System Context
# ============================================================
def diagram_L1_context():
    W, H = 1300, 780
    boxes = [
        {"cls": "c4-person", "label": "Procurador\nMunicipal", "x": 40, "y": 40, "w": 130, "h": 70},
        {"cls": "c4-person", "label": "CIO Estadual\n/ Federal", "x": 40, "y": 200, "w": 130, "h": 70},
        {"cls": "c4-person", "label": "Dir. Administrativo\nHospitalar", "x": 40, "y": 380, "w": 130, "h": 70},
        {"cls": "c4-person", "label": "Mantenedor\nEscola Privada", "x": 40, "y": 560, "w": 130, "h": 70},
        # NeoGov Platform
        {"cls": "c4-system", "label": "NeoGov Platform\n(LGPD Compliance + IA)", "desc": "Multi-tenant SaaS", "x": 440, "y": 240, "w": 220, "h": 120},
        # External systems
        {"cls": "c4-external", "label": "e-Cidade", "x": 920, "y": 40, "w": 120, "h": 55},
        {"cls": "c4-external", "label": "MV / Tasy", "x": 920, "y": 120, "w": 120, "h": 55},
        {"cls": "c4-external", "label": "SEI / SIAFI", "x": 920, "y": 200, "w": 120, "h": 55},
        {"cls": "c4-external", "label": "Class / Phonexao", "x": 920, "y": 280, "w": 120, "h": 55},
        {"cls": "c4-external", "label": "ANPD Portal", "x": 920, "y": 380, "w": 120, "h": 55},
        {"cls": "c4-external", "label": "TCE / CGU", "x": 920, "y": 460, "w": 120, "h": 55},
        {"cls": "c4-external", "label": "Cloud BR\n(Soberania)", "desc": "GPU + Compute", "x": 920, "y": 560, "w": 120, "h": 65},
        # Regulations
        {"cls": "c4-external", "label": "LGPD", "x": 1100, "y": 40, "w": 80, "h": 40},
        {"cls": "c4-external", "label": "LAI", "x": 1100, "y": 100, "w": 80, "h": 40},
        {"cls": "c4-external", "label": "ECA Digital", "x": 1100, "y": 160, "w": 80, "h": 40},
    ]
    connections = [
        {"x1": 170, "y1": 75, "x2": 440, "y2": 270, "label": "Usa P3 (LAI)"},
        {"x1": 170, "y1": 235, "x2": 440, "y2": 290, "label": "Usa P2, P3, P5"},
        {"x1": 170, "y1": 415, "x2": 440, "y2": 320, "label": "Usa P4, P5"},
        {"x1": 170, "y1": 595, "x2": 440, "y2": 340, "label": "Usa P1, P4"},
        {"x1": 660, "y1": 280, "x2": 920, "y2": 67, "label": "P1 varre"},
        {"x1": 660, "y1": 300, "x2": 920, "y2": 147, "label": "P5 integra"},
        {"x1": 660, "y1": 320, "x2": 920, "y2": 227, "label": "P5 integra"},
        {"x1": 660, "y1": 340, "x2": 920, "y2": 307, "label": "P5 integra"},
        {"x1": 660, "y1": 310, "x2": 920, "y2": 407, "label": "Relatorio"},
        {"x1": 660, "y1": 300, "x2": 920, "y2": 487, "label": "Comprovacao"},
        {"x1": 660, "y1": 340, "x2": 920, "y2": 592, "label": "GPU / Compute"},
    ]
    render_diagram(
        "C4 Level 1 — System Context",
        "NeoGov Platform no contexto de atores, sistemas externos e regulacoes",
        W, H, boxes, connections, [],
        "C4-L1-System-Context.png"
    )


# ============================================================
# D2: C4 Level 2 — Global Platform Layer (Layer 1)
# ============================================================
def diagram_L2_layer1():
    W, H = 1300, 700
    boxes = [
        # Tenant boundary
        {"cls": "c4-container", "label": "API Gateway", "tech": "Kong / AWS API GW", "x": 30, "y": 60, "w": 180, "h": 70},
        {"cls": "c4-container", "label": "Auth Service", "tech": "OAuth2 / OIDC / JWT", "x": 30, "y": 160, "w": 180, "h": 70},
        {"cls": "c4-container", "label": "Billing / Medicao", "tech": "Metering + Events", "x": 30, "y": 260, "w": 180, "h": 70},
        {"cls": "c4-container", "label": "Audit Trail LGPD", "tech": "Retencao 5 anos", "x": 30, "y": 370, "w": 180, "h": 70},
        {"cls": "c4-container", "label": "Observabilidade", "tech": "Metrics + Logs + Traces", "x": 30, "y": 470, "w": 180, "h": 70},
        {"cls": "c4-container", "label": "KMS / Segredos", "tech": "HashiCorp Vault", "x": 30, "y": 570, "w": 180, "h": 70},
        # Storage
        {"cls": "c4-container-db", "label": "Object Storage", "tech": "S3-compatible", "x": 310, "y": 160, "w": 170, "h": 70},
        {"cls": "c4-container-db", "label": "Block Storage", "tech": "EBS / NVMe", "x": 310, "y": 270, "w": 170, "h": 70},
        {"cls": "c4-container-db", "label": "Relational DB", "tech": "PostgreSQL", "x": 310, "y": 380, "w": 170, "h": 70},
        {"cls": "c4-container-db", "label": "Log Storage", "tech": "Elasticsearch", "x": 310, "y": 490, "w": 170, "h": 70},
        # Products consuming (right side)
        {"cls": "c4-system", "label": "P1\nData Discovery", "x": 680, "y": 30, "w": 110, "h": 70},
        {"cls": "c4-system", "label": "P2\nAnonimizacao", "x": 680, "y": 120, "w": 110, "h": 70},
        {"cls": "c4-system", "label": "P3\nLAI x LGPD", "x": 680, "y": 210, "w": 110, "h": 70},
        {"cls": "c4-system", "label": "P4\nAI-DPO", "x": 680, "y": 300, "w": 110, "h": 70},
        {"cls": "c4-system", "label": "P5\nETL / Integracao", "x": 680, "y": 390, "w": 110, "h": 70},
        # Consumer label
        {"cls": "c4-component", "label": "Todos os 5 produtos\nconsomem estes servicos", "desc": "Rateio proporcional ao uso", "x": 560, "y": 540, "w": 240, "h": 60},
    ]
    connections = [
        {"x1": 210, "y1": 95, "x2": 680, "y2": 65, "label": "Route"},
        {"x1": 210, "y1": 195, "x2": 680, "y2": 155, "label": "Auth"},
        {"x1": 210, "y1": 295, "x2": 680, "y2": 245, "label": "Bill"},
        {"x1": 210, "y1": 405, "x2": 680, "y2": 335, "label": "Audit"},
        {"x1": 210, "y1": 505, "x2": 680, "y2": 355, "label": "Metrics"},
        {"x1": 210, "y1": 605, "x2": 680, "y2": 425, "label": "Secrets"},
        # Storage connections
        {"x1": 210, "y1": 95, "x2": 310, "y2": 195, "label": ""},
        {"x1": 210, "y1": 405, "x2": 310, "y2": 415, "label": "Logs"},
        {"x1": 210, "y1": 505, "x2": 310, "y2": 525, "label": "Index"},
    ]
    boundaries = [
        {"label": "Layer 1 — Plataforma Comum (Shared Services)", "x": 15, "y": 20, "w": 490, "h": 640},
        {"label": "Layer 2 — Produtos (Consumers)", "x": 555, "y": 10, "w": 260, "h": 450},
    ]
    render_diagram(
        "C4 Level 2 — Global Platform Layer (Layer 1)",
        "Servicos compartilhados consumidos por todos os 5 produtos",
        W, H, boxes, connections, boundaries,
        "C4-L2-Layer1-Global.png"
    )


# ============================================================
# D3: C4 Level 2 — P1 Data Discovery
# ============================================================
def diagram_L2_P1():
    W, H = 1200, 650
    boxes = [
        {"cls": "c4-container", "label": "Scanner Engine", "tech": "Python / Rule-based", "desc": "Varredura batch de fontes", "x": 350, "y": 80, "w": 200, "h": 90},
        {"cls": "c4-container", "label": "Classification\nRules Engine", "tech": "Regex + NLP Light", "desc": "Sem IA", "x": 350, "y": 210, "w": 200, "h": 90},
        {"cls": "c4-container", "label": "Metadata Store", "tech": "PostgreSQL", "x": 350, "y": 340, "w": 200, "h": 70},
        {"cls": "c4-container", "label": "Report Generator", "tech": "PDF / Dashboard", "x": 350, "y": 450, "w": 200, "h": 70},
        {"cls": "c4-container", "label": "Scheduler", "tech": "Cron / Event-driven", "x": 50, "y": 80, "w": 160, "h": 70},
        {"cls": "c4-container", "label": "Connector Mgr", "tech": "Source adapters", "x": 50, "y": 200, "w": 160, "h": 70},
        {"cls": "c4-container-db", "label": "Temp Storage\n(Varredura)", "tech": "S3-compatible", "x": 750, "y": 80, "w": 160, "h": 70},
        {"cls": "c4-container-db", "label": "Object Storage\n(Metadados)", "tech": "S3-compatible", "x": 750, "y": 210, "w": 160, "h": 70},
        # Layer 1
        {"cls": "c4-component", "label": "Layer 1", "desc": "Auth + Billing + Audit\nGateway + KMS + Obs", "x": 750, "y": 380, "w": 160, "h": 80},
    ]
    connections = [
        {"x1": 210, "y1": 115, "x2": 350, "y2": 115, "label": "Trigger"},
        {"x1": 210, "y1": 235, "x2": 350, "y2": 160, "label": "Config sources"},
        {"x1": 450, "y1": 170, "x2": 450, "y2": 210, "label": "Scan results"},
        {"x1": 450, "y1": 300, "x2": 450, "y2": 340, "label": "Save metadata"},
        {"x1": 450, "y1": 410, "x2": 450, "y2": 450, "label": "Generate"},
        {"x1": 550, "y1": 115, "x2": 750, "y2": 115, "label": "Temp data"},
        {"x1": 550, "y1": 375, "x2": 750, "y2": 245, "label": "Persist"},
        {"x1": 550, "y1": 125, "x2": 750, "y2": 420, "label": "L1 services"},
    ]
    boundaries = [
        {"label": "P1 Data Discovery — Layer 2 (Especifico)", "x": 25, "y": 30, "w": 610, "h": 530},
    ]
    render_diagram(
        "C4 Level 2 — P1 Data Discovery",
        "Varredura batch de fontes, classificacao por regra (sem IA), mapeamento de dados pessoais",
        W, H, boxes, connections, boundaries,
        "C4-L2-P1-DataDiscovery.png"
    )


# ============================================================
# D4: C4 Level 2 — P2 Anonimizacao
# ============================================================
def diagram_L2_P2():
    W, H = 1200, 650
    boxes = [
        {"cls": "c4-container", "label": "NER / PII Engine", "tech": "BERT-base + spaCy", "desc": "GPU Batch", "x": 350, "y": 80, "w": 200, "h": 90},
        {"cls": "c4-container", "label": "Pre-Processor", "tech": "Read + Validate", "x": 80, "y": 80, "w": 170, "h": 70},
        {"cls": "c4-container", "label": "Post-Processor", "tech": "Write Anonymized", "x": 80, "y": 200, "w": 170, "h": 70},
        {"cls": "c4-container", "label": "Job Queue", "tech": "SQS / RabbitMQ", "x": 80, "y": 330, "w": 170, "h": 70},
        {"cls": "c4-container", "label": "Job Orchestrator", "tech": "Celery / Airflow", "x": 350, "y": 220, "w": 200, "h": 70},
        {"cls": "c4-container-db", "label": "Anonymized Data", "tech": "S3-compatible", "x": 750, "y": 80, "w": 160, "h": 70},
        {"cls": "c4-container-db", "label": "Temp Buffer", "tech": "Block Storage", "x": 750, "y": 200, "w": 160, "h": 70},
        {"cls": "c4-component", "label": "GPU Batch", "desc": "Spot / Reserved", "x": 600, "y": 80, "w": 120, "h": 60},
        {"cls": "c4-component", "label": "Layer 1", "desc": "Auth + Billing + Audit\nGateway + KMS + Obs", "x": 750, "y": 370, "w": 160, "h": 80},
    ]
    connections = [
        {"x1": 250, "y1": 115, "x2": 350, "y2": 105, "label": "Feed"},
        {"x1": 250, "y1": 235, "x2": 350, "y2": 245, "label": "Write back"},
        {"x1": 250, "y1": 365, "x2": 350, "y2": 255, "label": "Enqueue/Dequeue"},
        {"x1": 450, "y1": 170, "x2": 600, "y2": 110, "label": "GPU call"},
        {"x1": 450, "y1": 290, "x2": 450, "y2": 330, "label": "Schedule"},
        {"x1": 550, "y1": 125, "x2": 750, "y2": 115, "label": "Store"},
        {"x1": 550, "y1": 255, "x2": 750, "y2": 235, "label": "Buffer"},
        {"x1": 550, "y1": 130, "x2": 750, "y2": 410, "label": "L1 services"},
    ]
    boundaries = [
        {"label": "P2 Anonimizacao — Layer 2 (Especifico)", "x": 25, "y": 30, "w": 740, "h": 400},
    ]
    render_diagram(
        "C4 Level 2 — P2 Anonimizacao",
        "Anonimizacao batch com GPU (NER/PII), job queue, pre/post processamento",
        W, H, boxes, connections, boundaries,
        "C4-L2-P2-Anonimizacao.png"
    )


# ============================================================
# D5: C4 Level 2 — P3 LAI x LGPD
# ============================================================
def diagram_L2_P3():
    W, H = 1200, 650
    boxes = [
        {"cls": "c4-container", "label": "Certificate Engine", "tech": "FastAPI / Sync", "desc": "Interativo, baixa latencia", "x": 350, "y": 80, "w": 200, "h": 90},
        {"cls": "c4-container", "label": "Legal Rules Engine", "tech": "LAI + LGPD rules", "x": 350, "y": 220, "w": 200, "h": 70},
        {"cls": "c4-container-db", "label": "Vector Store", "tech": "Milvus / Qdrant", "desc": "Base legal compartilhada", "x": 100, "y": 80, "w": 170, "h": 80},
        {"cls": "c4-container-db", "label": "Certificate DB", "tech": "PostgreSQL", "x": 100, "y": 210, "w": 170, "h": 70},
        {"cls": "c4-component", "label": "GPU Quente (RESERVADA)", "desc": "Model loaded 24/7\n< 2s latencia", "x": 650, "y": 80, "w": 180, "h": 80},
        {"cls": "c4-container", "label": "Context Manager", "tech": "Prompt assembly", "x": 650, "y": 220, "w": 180, "h": 70},
        {"cls": "c4-component", "label": "Layer 1", "desc": "Auth + Billing + Audit\nGateway + KMS + Obs", "x": 650, "y": 380, "w": 180, "h": 80},
    ]
    connections = [
        {"x1": 270, "y1": 120, "x2": 350, "y2": 115, "label": "RAG retrieve"},
        {"x1": 270, "y1": 245, "x2": 350, "y2": 255, "label": "Legal context"},
        {"x1": 450, "y1": 170, "x2": 650, "y2": 120, "label": "Inference"},
        {"x1": 650, "y1": 255, "x2": 550, "y2": 255, "label": "Rules"},
        {"x1": 450, "y1": 130, "x2": 650, "y2": 420, "label": "L1 services"},
    ]
    boundaries = [
        {"label": "P3 LAI x LGPD — Layer 2 (Especifico)", "x": 25, "y": 30, "w": 870, "h": 340},
    ]
    render_diagram(
        "C4 Level 2 — P3 LAI x LGPD",
        "Decisao de revelacao em certidao publica. Interativo sincrono. GPU quente RESERVADA.",
        W, H, boxes, connections, boundaries,
        "C4-L2-P3-LAixLGPD.png"
    )


# ============================================================
# D6: C4 Level 2 — P4 AI-DPO
# ============================================================
def diagram_L2_P4():
    W, H = 1200, 650
    boxes = [
        {"cls": "c4-container", "label": "Chat Service", "tech": "WebSocket / SSE", "desc": "Conversacional", "x": 350, "y": 80, "w": 200, "h": 90},
        {"cls": "c4-container", "label": "Session Manager", "tech": "Redis / In-memory", "x": 100, "y": 80, "w": 170, "h": 70},
        {"cls": "c4-container", "label": "RAG Retriever", "tech": "Embedding search", "x": 100, "y": 210, "w": 170, "h": 70},
        {"cls": "c4-container-db", "label": "Vector Store", "tech": "Milvus / Qdrant", "desc": "RAG: docs LGPD + historico", "x": 100, "y": 340, "w": 170, "h": 70},
        {"cls": "c4-container-db", "label": "Chat History", "tech": "PostgreSQL", "x": 350, "y": 220, "w": 200, "h": 70},
        {"cls": "c4-component", "label": "GPU Quente (RESERVADA)", "desc": "Model loaded 24/7\n< 3s latencia", "x": 650, "y": 80, "w": 180, "h": 80},
        {"cls": "c4-container", "label": "Prompt Builder", "tech": "RAG + History + System", "x": 650, "y": 220, "w": 180, "h": 70},
        {"cls": "c4-component", "label": "Layer 1", "desc": "Auth + Billing + Audit\nGateway + KMS + Obs", "x": 650, "y": 380, "w": 180, "h": 80},
    ]
    connections = [
        {"x1": 270, "y1": 115, "x2": 350, "y2": 115, "label": "Session state"},
        {"x1": 270, "y1": 245, "x2": 350, "y2": 140, "label": "RAG docs"},
        {"x1": 270, "y1": 375, "x2": 270, "y2": 280, "label": "Embed + search"},
        {"x1": 450, "y1": 170, "x2": 650, "y2": 120, "label": "Inference"},
        {"x1": 550, "y1": 255, "x2": 650, "y2": 255, "label": "Context"},
        {"x1": 450, "y1": 130, "x2": 650, "y2": 420, "label": "L1 services"},
    ]
    boundaries = [
        {"label": "P4 AI-DPO — Layer 2 (Especifico)", "x": 25, "y": 30, "w": 870, "h": 340},
    ]
    render_diagram(
        "C4 Level 2 — P4 AI-DPO",
        "Chat LGPD com RAG. Conversacional. GPU quente RESERVADA. Sessao + historico.",
        W, H, boxes, connections, boundaries,
        "C4-L2-P4-AI-DPO.png"
    )


# ============================================================
# D7: C4 Level 2 — P5 ETL / Integracao
# ============================================================
def diagram_L2_P5():
    W, H = 1200, 650
    boxes = [
        {"cls": "c4-container", "label": "ETL Pipeline", "tech": "Apache Airflow / custom", "x": 350, "y": 80, "w": 200, "h": 90},
        {"cls": "c4-container", "label": "Job Scheduler", "tech": "Cron / Event-driven", "x": 80, "y": 80, "w": 170, "h": 70},
        {"cls": "c4-container", "label": "Connector Manager", "tech": "e-Cidade / MV / Tasy / Class", "desc": "Requer engenheiro p/ setup", "x": 80, "y": 210, "w": 170, "h": 80},
        {"cls": "c4-container-db", "label": "Staging Area", "tech": "S3-compatible", "x": 80, "y": 350, "w": 170, "h": 70},
        {"cls": "c4-container-db", "label": "Temp Buffer", "tech": "Block Storage", "x": 350, "y": 220, "w": 200, "h": 70},
        {"cls": "c4-container", "label": "Data Validator", "tech": "Schema + Integrity", "x": 350, "y": 340, "w": 200, "h": 70},
        {"cls": "c4-component", "label": "Layer 1", "desc": "Auth + Billing + Audit\nGateway + KMS + Obs", "x": 700, "y": 200, "w": 160, "h": 80},
    ]
    connections = [
        {"x1": 250, "y1": 115, "x2": 350, "y2": 115, "label": "Trigger"},
        {"x1": 250, "y1": 250, "x2": 350, "y2": 140, "label": "Source config"},
        {"x1": 250, "y1": 385, "x2": 350, "y2": 255, "label": "Read/Write"},
        {"x1": 450, "y1": 170, "x2": 450, "y2": 220, "label": "Buffer"},
        {"x1": 450, "y1": 290, "x2": 450, "y2": 340, "label": "Validate"},
        {"x1": 550, "y1": 130, "x2": 700, "y2": 240, "label": "L1 services"},
    ]
    boundaries = [
        {"label": "P5 ETL / Integracao — Layer 2 (Especifico) — SEM IA", "x": 25, "y": 30, "w": 590, "h": 420},
    ]
    render_diagram(
        "C4 Level 2 — P5 ETL / Integracao",
        "Integra sistemas legados. Batch agendado. Sem IA. Requer engenheiro p/ setup novo conector.",
        W, H, boxes, connections, boundaries,
        "C4-L2-P5-ETL-Integracao.png"
    )


# ============================================================
# D8: C4 Level 3 — GPU Inference Pipeline (P3 / P4)
# ============================================================
def diagram_L3_inference():
    W, H = 1200, 520
    boxes = [
        {"cls": "c4-component", "label": "HTTP Request", "desc": "GET/POST or SSE", "x": 20, "y": 180, "w": 120, "h": 60},
        {"cls": "c4-component", "label": "Auth + Rate\nLimit", "desc": "Layer 1", "x": 170, "y": 180, "w": 100, "h": 60},
        {"cls": "c4-component", "label": "Tokenizer", "desc": "Input tokenization", "x": 300, "y": 180, "w": 100, "h": 60},
        {"cls": "c4-component", "label": "RAG Retriever", "desc": "Vector search\n+ Top-K docs", "x": 300, "y": 60, "w": 100, "h": 60},
        {"cls": "c4-component", "label": "Prompt\nAssembly", "desc": "System + RAG +\nHistory + User", "x": 430, "y": 120, "w": 100, "h": 60},
        {"cls": "c4-component", "label": "GPU Inference", "desc": "Model forward pass\n(loaded in VRAM)", "x": 570, "y": 120, "w": 120, "h": 80},
        {"cls": "c4-component", "label": "Output\nDecoder", "desc": "Token stream", "x": 720, "y": 120, "w": 100, "h": 60},
        {"cls": "c4-component", "label": "Response\nFormatter", "desc": "JSON / SSE stream", "x": 850, "y": 180, "w": 100, "h": 60},
        {"cls": "c4-component", "label": "Audit Logger", "desc": "LGPD trail", "x": 850, "y": 60, "w": 100, "h": 60},
        {"cls": "c4-component", "label": "Billing\nEvent", "desc": "Count tokens", "x": 1000, "y": 180, "w": 100, "h": 60},
        # GPU Memory
        {"cls": "c4-container-db", "label": "GPU VRAM (Reservado)", "desc": "Model weights + KV Cache + Context", "x": 560, "y": 310, "w": 140, "h": 70},
        # Vector Store
        {"cls": "c4-container-db", "label": "Vector Store", "desc": "Embeddings", "x": 170, "y": 60, "w": 100, "h": 60},
    ]
    connections = [
        {"x1": 140, "y1": 210, "x2": 170, "y2": 210, "label": ""},
        {"x1": 270, "y1": 210, "x2": 300, "y2": 210, "label": ""},
        {"x1": 350, "y1": 180, "x2": 400, "y2": 150, "label": ""},
        {"x1": 220, "y1": 90, "x2": 300, "y2": 90, "label": "Search"},
        {"x1": 350, "y1": 120, "x2": 400, "y2": 135, "label": "Docs"},
        {"x1": 530, "y1": 150, "x2": 570, "y2": 150, "label": ""},
        {"x1": 690, "y1": 150, "x2": 720, "y2": 150, "label": ""},
        {"x1": 820, "y1": 150, "x2": 850, "y2": 200, "label": ""},
        {"x1": 820, "y1": 140, "x2": 850, "y2": 90, "label": "Log"},
        {"x1": 950, "y1": 210, "x2": 1000, "y2": 210, "label": ""},
        {"x1": 630, "y1": 200, "x2": 630, "y2": 310, "label": "VRAM"},
    ]
    boundaries = [
        {"label": "Pipeline de Inferencia GPU — P3 / P4 (Componentes)", "x": 8, "y": 20, "w": 1110, "h": 380},
    ]
    render_diagram(
        "C4 Level 3 — Pipeline de Inferencia GPU (P3 / P4)",
        "Fluxo sincrono de requisicao: Auth -> Tokenize -> RAG -> Prompt -> GPU -> Stream -> Audit -> Bill",
        W, H, boxes, connections, boundaries,
        "C4-L3-GPU-Inference.png"
    )


# ============================================================
# MAIN
# ============================================================
if __name__ == "__main__":
    print("Gerando diagramas C4 NeoGov...")
    print("=" * 50)
    diagram_L1_context()
    diagram_L2_layer1()
    diagram_L2_P1()
    diagram_L2_P2()
    diagram_L2_P3()
    diagram_L2_P4()
    diagram_L2_P5()
    diagram_L3_inference()
    print("=" * 50)
    print(f"8 diagramas gerados em {OUT_DIR}/")
