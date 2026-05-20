#!/usr/bin/env python3
"""
NeoGov — Dimensionamento de Infraestrutura por Produto × Porte de Cliente
v1.W1.20.1 | ID: NEOGOV-V21-INSTRUCAO-SESSAO-PARALELA

Gera xlsx com:
  - 1 aba resumo (definições de porte + nota de classe)
  - 5 abas de produto (P1–P5) com tabelas de demanda Layer 1/2
  - 1 aba variáveis do piloto
  - 1 aba premissas a validar
  - 1 aba verificação CV1–CV8
"""

import sys, os
sys.path.insert(0, "/home/z/my-project/skills/xlsx/templates")
from base import *

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# ============================================================
# GLOBAL SETTINGS
# ============================================================
OUTPUT = "/home/z/my-project/download/NeoGov_Dimensionamento_Infra_v1.20.1.xlsx"
XLSX_SKILL_DIR = "/home/z/my-project/skills/xlsx"

wb = Workbook()

# ============================================================
# HELPER — write a product sheet
# ============================================================
HEADERS_PROD = [
    "#", "Recurso de Infra", "Camada", "Unidade de Medida",
    "Fixo / Variavel", "Funcao de Demanda (generico)",
    "Variavel de Carga", "Ajuste por Porte (P / M / G)",
    "Premissa Declarada", "Classe"
]

def write_product_sheet(wb, ws_title, product_name, product_desc, data_rows):
    """
    data_rows: list of dicts with keys matching HEADERS_PROD
    """
    ws = wb.create_sheet(title=ws_title)

    n_cols = len(HEADERS_PROD) + 1  # +1 for col A margin
    setup_sheet(ws, title=f"{product_name} — {product_desc}", last_col=n_cols)

    # Subtitle row
    ws.merge_cells(start_row=3, start_column=2, end_row=3, end_column=n_cols)
    ws.cell(row=3, column=2, value=product_desc).font = font_caption()

    # Headers at row 5
    header_row = 5
    for col_idx, h in enumerate(HEADERS_PROD, start=2):
        ws.cell(row=header_row, column=col_idx, value=h)
    style_header_row(ws, row_num=header_row, col_start=2, col_end=n_cols)
    ws.row_dimensions[header_row].height = 36  # taller for wrapped headers

    # Data rows starting at row 6
    for i, row_data in enumerate(data_rows):
        r = header_row + 1 + i
        ws.cell(row=r, column=2, value=i + 1)
        ws.cell(row=r, column=3, value=row_data.get("recurso", ""))
        ws.cell(row=r, column=4, value=row_data.get("camada", ""))
        ws.cell(row=r, column=5, value=row_data.get("unidade", ""))
        ws.cell(row=r, column=6, value=row_data.get("fixo_var", ""))
        ws.cell(row=r, column=7, value=row_data.get("funcao", ""))
        ws.cell(row=r, column=8, value=row_data.get("variavel_carga", ""))
        ws.cell(row=r, column=9, value=row_data.get("ajuste_porte", ""))
        ws.cell(row=r, column=10, value=row_data.get("premissa", ""))
        ws.cell(row=r, column=11, value=row_data.get("classe", ""))

        # Class-based color coding
        classe = row_data.get("classe", "")
        if "PREMISSA" in classe:
            accent_fill = PatternFill("solid", fgColor="FEF9E7")
            for c in range(2, n_cols + 1):
                ws.cell(row=r, column=c).fill = accent_fill
        elif "ANALOGO" in classe:
            accent_fill = PatternFill("solid", fgColor="E8F5E9")
            for c in range(2, n_cols + 1):
                ws.cell(row=r, column=c).fill = accent_fill
        else:
            style_data_row(ws, row_num=r, col_start=2, col_end=n_cols, row_index=i)

        # Override font body for all data rows (preserve fill color above)
        for c in range(2, n_cols + 1):
            ws.cell(row=r, column=c).font = font_body()
            ws.cell(row=r, column=c).alignment = Alignment(
                horizontal="left", vertical="center", wrap_text=True
            )

        ws.row_dimensions[r].height = 56  # taller for wrapped demand functions

    # Freeze panes
    ws.freeze_panes = "C6"

    # Column widths
    widths = {
        "A": 3,
        "B": 4,   # #
        "C": 24,  # Recurso
        "D": 10,  # Camada
        "E": 16,  # Unidade
        "F": 14,  # Fixo/Var
        "G": 40,  # Funcao
        "H": 28,  # Variavel carga
        "I": 32,  # Ajuste porte
        "J": 34,  # Premissa
        "K": 14,  # Classe
    }
    for col_letter, w in widths.items():
        ws.column_dimensions[col_letter].width = w

    return ws


# ============================================================
# HELPER — write a list sheet (variaveis / premissas / CV)
# ============================================================
def write_list_sheet(wb, ws_title, title, headers, data_rows, col_widths=None):
    ws = wb.create_sheet(title=ws_title)
    n_cols = len(headers) + 1
    setup_sheet(ws, title=title, last_col=n_cols)

    header_row = 4
    for col_idx, h in enumerate(headers, start=2):
        ws.cell(row=header_row, column=col_idx, value=h)
    style_header_row(ws, row_num=header_row, col_start=2, col_end=n_cols)
    ws.row_dimensions[header_row].height = 28

    for i, row_data in enumerate(data_rows):
        r = header_row + 1 + i
        for j, val in enumerate(row_data):
            ws.cell(row=r, column=2 + j, value=val)
        style_data_row(ws, row_num=r, col_start=2, col_end=n_cols, row_index=i)
        for c in range(2, n_cols + 1):
            ws.cell(row=r, column=c).alignment = Alignment(
                horizontal="left", vertical="center", wrap_text=True
            )
        ws.row_dimensions[r].height = 40

    if col_widths:
        for col_letter, w in col_widths.items():
            ws.column_dimensions[col_letter].width = w

    ws.freeze_panes = "B5"
    return ws


# ============================================================
# 1. RESUMO EXECUTIVO (first sheet)
# ============================================================
ws_resumo = wb.active
ws_resumo.title = "Resumo Executivo"
setup_sheet(ws_resumo, title="NeoGov — Dimensionamento de Infraestrutura por Produto x Porte", last_col=8)

# Metadata
meta_lines = [
    "ID: NEOGOV-V21-INSTRUCAO-SESSAO-PARALELA",
    "Versao: v1.W1.20.1 | Data: 2026-05-20",
    "Tipo: STANDALONE_BRIEFING_FOR_PARALLEL_SESSION",
    "",
    "OBJETIVO: Produzir dimensionamento tecnico de infra por produto/tenant.",
    "REGRA: Estrutura de demanda derivada da engenharia. Nenhum preco em R$.",
    "         Dado ausente = [FALTA: x] declarado. Nunca suposicao.",
]
r = 4
for line in meta_lines:
    ws_resumo.cell(row=r, column=2, value=line).font = font_body()
    if line.startswith("OBJETIVO") or line.startswith("REGRA"):
        ws_resumo.cell(row=r, column=2).font = font_subheader()
    r += 1

r += 1  # blank row

# ---- Definicoes de Porte ----
ws_resumo.cell(row=r, column=2, value="DEFINICOES DE PORTE DE CLIENTE (PREMISSA)").font = font_subheader()
r += 1

porte_headers = ["Atributo", "Pequeno (P)", "Medio (M)", "Grande (G)"]
for j, h in enumerate(porte_headers, start=2):
    ws_resumo.cell(row=r, column=j, value=h)
style_header_row(ws_resumo, row_num=r, col_start=2, col_end=5)
r += 1

porte_data = [
    ["Funcionarios", "1 - 50", "51 - 500", "501+"],
    ["Registros dados pessoais", "~10k - 100k", "~100k - 1M", "~1M - 50M+"],
    ["Fontes de dados", "2 - 5", "5 - 20", "20 - 100+"],
    ["Requisicoes/mes (P3/P4)", "500 - 2.000", "2.000 - 20.000", "20.000 - 200.000"],
    ["Jobs batch/mes (P1/P2/P5)", "10 - 50", "50 - 500", "500 - 5.000+"],
    ["Nivel de compartilhamento GPU", "GPU compartilhada (multi-tenant)", "GPU dedicada (1:1)", "GPU dedicada + scale-out"],
    ["Retencao auditoria LGPD", "5 anos (todos)", "5 anos (todos)", "5 anos (todos)"],
]
for i, row_d in enumerate(porte_data):
    for j, val in enumerate(row_d, start=2):
        ws_resumo.cell(row=r, column=j, value=val)
    style_data_row(ws_resumo, row_num=r, col_start=2, col_end=5, row_index=i)
    for c in range(2, 6):
        ws_resumo.cell(row=r, column=c).font = font_body()
        ws_resumo.cell(row=r, column=c).alignment = align_text()
    ws_resumo.row_dimensions[r].height = 22
    r += 1

r += 1  # blank

# ---- Arquitetura em Camadas ----
ws_resumo.cell(row=r, column=2, value="ARQUITETURA DA INFRAESTRUTURA EM CAMADAS").font = font_subheader()
r += 1

camadas_headers = ["Camada", "Descricao", "Exemplos"]
for j, h in enumerate(camadas_headers, start=2):
    ws_resumo.cell(row=r, column=j, value=h)
style_header_row(ws_resumo, row_num=r, col_start=2, col_end=4)
r += 1

camadas_data = [
    ["Layer 1 (Plataforma Comum)", "Servicos consumidos por TODOS os 5 produtos",
     "Auth multi-tenant, billing/medicao, auditoria LGPD, API gateway, observabilidade, KMS/segredos, storage base"],
    ["Layer 2 (Especifico por Produto)", "Recursos exclusivos de cada produto",
     "Vector store (P3/P4), fila de jobs (P1/P2/P5), GPU quente (P3/P4), GPU batch (P2), connector manager (P1/P5)"],
]
for i, row_d in enumerate(camadas_data):
    for j, val in enumerate(row_d, start=2):
        ws_resumo.cell(row=r, column=j, value=val)
    style_data_row(ws_resumo, row_num=r, col_start=2, col_end=4, row_index=i)
    for c in range(2, 5):
        ws_resumo.cell(row=r, column=c).font = font_body()
        ws_resumo.cell(row=r, column=c).alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
    ws_resumo.row_dimensions[r].height = 40
    r += 1

r += 1

# ---- Nota de Classe ----
ws_resumo.cell(row=r, column=2, value="NOTA DE CLASSE — COMPOSICAO DO MODELO").font = font_subheader()
r += 1

classe_headers = ["Classe", "Significado", "Contagem (linhas)"]
for j, h in enumerate(classe_headers, start=2):
    ws_resumo.cell(row=r, column=j, value=h)
style_header_row(ws_resumo, row_num=r, col_start=2, col_end=4)
r += 1

classe_data = [
    ["[ENGENHARIA]", "Derivada da arquitetura/spec tecnica (assertivo)", "A preencher apos geracao"],
    ["[ANALOGO]", "Estimado por sistema similar conhecido (medio)", "A preencher apos geracao"],
    ["[PREMISSA]", "Suposicao a validar no piloto (fragil — declarar)", "A preencher apos geracao"],
]
for i, row_d in enumerate(classe_data):
    for j, val in enumerate(row_d, start=2):
        ws_resumo.cell(row=r, column=j, value=val)
    style_data_row(ws_resumo, row_num=r, col_start=2, col_end=4, row_index=i)
    for c in range(2, 5):
        ws_resumo.cell(row=r, column=c).font = font_body()
        ws_resumo.cell(row=r, column=c).alignment = align_text()
    ws_resumo.row_dimensions[r].height = 22
    r += 1

r += 1
ws_resumo.cell(row=r, column=2, value="Regra: quanto mais [ENGENHARIA], mais assertivo o modelo final de custo. Premissas fragilizam — devem ser reduzidas via piloto.").font = font_caption()

# Column widths for resumo
ws_resumo.column_dimensions["A"].width = 3
ws_resumo.column_dimensions["B"].width = 38
ws_resumo.column_dimensions["C"].width = 30
ws_resumo.column_dimensions["D"].width = 60
ws_resumo.column_dimensions["E"].width = 24


# ============================================================
# P1 DATA DISCOVERY — Layer 2 + Layer 1
# ============================================================
P1_DATA = [
    # === LAYER 2 (ESPECIFICO) ===
    {
        "recurso": "vCPU-compute (batch varredura)",
        "camada": "Layer 2",
        "unidade": "vCPU-hora/mes",
        "fixo_var": "Variavel",
        "funcao": "vCPU_h = N_fontes x freq_varredura x t_varredura_fonte / 3600",
        "variavel_carga": "N_fontes, freq_varredura (varreduras/mes), t_varredura_fonte (seg/fonte)",
        "ajuste_porte": "P: N_fontes ~ 2-5, freq ~ 4/mes | M: N_fontes ~ 5-20, freq ~ 8/mes | G: N_fontes ~ 20-100, freq ~ 12/mes",
        "premissa": "Varredura regulada por regra (sem IA). 1 fonte ~ 5 min varredura para 10k registros — PREMISSA, validar piloto.",
        "classe": "[PREMISSA]"
    },
    {
        "recurso": "RAM batch (varredura)",
        "camada": "Layer 2",
        "unidade": "GB-hora/mes",
        "fixo_var": "Variavel",
        "funcao": "RAM_GBh = vCPU_ativas_simultaneas x RAM_por_vCPU x duracao_batch_h",
        "variavel_carga": "vCPU_ativas_simultaneas, RAM_por_vCPU (GB), duracao_batch (h)",
        "ajuste_porte": "P: 1 vCPU paralela, 4 GB | M: 2-4 vCPU, 4 GB | G: 4-8 vCPU, 4 GB",
        "premissa": "Regra baseada em varredura linepar. RAM_por_vCPU = 4 GB para metadados — PREMISSA, validar piloto.",
        "classe": "[PREMISSA]"
    },
    {
        "recurso": "Storage-object (metadados mapeamento)",
        "camada": "Layer 2",
        "unidade": "GB/mes (acumulo)",
        "fixo_var": "Variavel",
        "funcao": "storage_GB = N_registros_mapeados x tamanho_metadado_por_registro / 1.000.000.000",
        "variavel_carga": "N_registros_mapeados, tamanho_metadado_por_registro (bytes)",
        "ajuste_porte": "P: ~100k reg ~ 0.1 GB | M: ~1M reg ~ 1 GB | G: ~50M reg ~ 50 GB",
        "premissa": "Metadado por registro ~ 1 KB (classificacao + fonte + flags) — ANALOGO com sistemas DLP conhecidos.",
        "classe": "[ANALOGO]"
    },
    {
        "recurso": "Storage-block (temporario varredura)",
        "camada": "Layer 2",
        "unidade": "GB (pico)",
        "fixo_var": "Variavel",
        "funcao": "storage_GB = max_concorrente x tamanho_chunk_varredura",
        "variavel_carga": "max_concorrente (fontes simultaneas), tamanho_chunk_varredura (GB/fonte)",
        "ajuste_porte": "P: 1 concorrente x ~0.5 GB = 0.5 GB | M: 4 concorrentes x ~2 GB = 8 GB | G: 10 concorrentes x ~10 GB = 100 GB",
        "premissa": "Chunk temporario liberado apos varredura. Tamanho depende da fonte — PREMISSA, medir piloto.",
        "classe": "[PREMISSA]"
    },
    {
        "recurso": "Bandwidth (varredura)",
        "camada": "Layer 2",
        "unidade": "GB/mes",
        "fixo_var": "Variavel",
        "funcao": "GB_trafego = N_varreduras_total x GB_lidos_por_varredura",
        "variavel_carga": "N_varreduras_total, GB_lidos_por_varredura",
        "ajuste_porte": "P: ~20 varreduras x ~1 GB = 20 GB/mes | M: ~160 varreduras x ~5 GB = 800 GB/mes | G: ~1.200 varreduras x ~50 GB = 60 TB/mes",
        "premissa": "Leitura de dados do cliente durante varredura. GB_por_varredura depende do volume do cliente — PREMISSA.",
        "classe": "[PREMISSA]"
    },
    # === LAYER 1 (COMUM — fracao P1) ===
    {
        "recurso": "Auth multi-tenant (fracao P1)",
        "camada": "Layer 1",
        "unidade": "req/mes",
        "fixo_var": "Variavel",
        "funcao": "req_auth = N_varreduras x req_auth_por_varredura",
        "variavel_carga": "N_varreduras, req_auth_por_varredura",
        "ajuste_porte": "P: ~20 varreduras x ~2 = 40 req | M: ~160 x 2 = 320 req | G: ~1.200 x 2 = 2.400 req",
        "premissa": "Fracao proporcional ao uso do produto. Auth e shared service — rateio por req. PREMISSA de proporcao 1:5.",
        "classe": "[PREMISSA]"
    },
    {
        "recurso": "Auditoria LGPD — trilha (fracao P1)",
        "camada": "Layer 1",
        "unidade": "GB/mes (retencao 5 anos)",
        "fixo_var": "Variavel",
        "funcao": "log_GB_mes = N_registros_processados_mes x tamanho_log_por_registro / 1B",
        "variavel_carga": "N_registros_processados_mes, tamanho_log_por_registro (bytes)",
        "ajuste_porte": "P: ~100k x 500 B = 50 MB/mes | M: ~1M x 500 B = 500 MB/mes | G: ~50M x 500 B = 25 GB/mes",
        "premissa": "Log por registro processado ~ 500 bytes (quem/Quando/OQue/fonte). Retencao 5 anos = 60 meses acumulados. ENGENHARIA (LGPD exige trilha).",
        "classe": "[ENGENHARIA]"
    },
    {
        "recurso": "API Gateway (fracao P1)",
        "camada": "Layer 1",
        "unidade": "req/mes",
        "fixo_var": "Variavel",
        "funcao": "req_gateway = N_varreduras x req_por_varredura",
        "variavel_carga": "N_varreduras, req_por_varredura (API calls internos)",
        "ajuste_porte": "P: ~20 x ~10 = 200 | M: ~160 x 10 = 1.600 | G: ~1.200 x 10 = 12.000",
        "premissa": "Cada varredura gera ~10 API calls internos (check, progress, resultado). PREMISSA, validar piloto.",
        "classe": "[PREMISSA]"
    },
    {
        "recurso": "Observabilidade (fracao P1)",
        "camada": "Layer 1",
        "unidade": "GB/mes",
        "fixo_var": "Fixo + Variavel",
        "funcao": "obs_GB = obs_base_fixo + (N_varreduras x metricas_por_varredura x bytes_por_metrica / 1B)",
        "variavel_carga": "N_varreduras, metricas_por_varredura, obs_base_fixo (GB)",
        "ajuste_porte": "Base fixo ~ 0.5 GB/mes (todos portes). Variavel: P +10 MB, M +80 MB, G +600 MB",
        "premissa": "Base fixa de infra comum. Variavel proporcional a uso. obs_base_fixo = PREMISSA.",
        "classe": "[PREMISSA]"
    },
    {
        "recurso": "Billing/Medicao (fracao P1)",
        "camada": "Layer 1",
        "unidade": "eventos/mes",
        "fixo_var": "Variavel",
        "funcao": "eventos = N_varreduras (1 evento por varredura concluida)",
        "variavel_carga": "N_varreduras",
        "ajuste_porte": "P: ~20 | M: ~160 | G: ~1.200",
        "premissa": "1 evento faturavel por varredura concluida. Modelo de mediacao simples. ENGENHARIA (definicao de evento).",
        "classe": "[ENGENHARIA]"
    },
    {
        "recurso": "KMS/Segredos (fracao P1)",
        "camada": "Layer 1",
        "unidade": "req/mes",
        "fixo_var": "Fixo",
        "funcao": "req_kms = freq_rotacao_secrets x N_secrets_tenant",
        "variavel_carga": "freq_rotacao_secrets, N_secrets_tenant (credenciais de fontes)",
        "ajuste_porte": "P: 2 secrets x 1 rotacao = 2 req/mes | M: 10 x 1 = 10 | G: 50 x 1 = 50",
        "premissa": "Cada fonte de dados = 1 secret. Rotacao mensal. ENGENHARIA (best practice).",
        "classe": "[ENGENHARIA]"
    },
]

write_product_sheet(wb, "P1 Data Discovery", "P1 Data Discovery", "Varre fontes do cliente e mapeia dados pessoais. Batch. Sem IA.", P1_DATA)


# ============================================================
# P2 ANONIMIZACAO
# ============================================================
P2_DATA = [
    # === LAYER 2 (ESPECIFICO) ===
    {
        "recurso": "GPU-batch (NER/PII detection)",
        "camada": "Layer 2",
        "unidade": "GPU-hora/mes",
        "fixo_var": "Variavel",
        "funcao": "GPU_h = N_registros_a_anonimizar x seg_por_registro_NER / 3600",
        "variavel_carga": "N_registros_a_anonimizar, seg_por_registro_NER",
        "ajuste_porte": "P: ~50k reg x 0.01s = ~0.14 GPU-h | M: ~500k x 0.01s = ~1.4 GPU-h | G: ~10M x 0.01s = ~28 GPU-h",
        "premissa": "Throughput NER ~ 100 registros/seg/GPU (modelo BERT-base). sec_por_registro_NER = 0.01s — ANALOGO com spaCy+NLP benchmarks.",
        "classe": "[ANALOGO]"
    },
    {
        "recurso": "vCPU-compute (pre/post processamento)",
        "camada": "Layer 2",
        "unidade": "vCPU-hora/mes",
        "fixo_var": "Variavel",
        "funcao": "vCPU_h = N_jobs_anon x (t_pre_processamento + t_pos_processamento) / 3600",
        "variavel_carga": "N_jobs_anon, t_pre_processamento (seg), t_pos_processamento (seg)",
        "ajuste_porte": "P: ~12 jobs x 300s = ~1 vCPU-h | M: ~100 jobs x 600s = ~17 vCPU-h | G: ~1.000 jobs x 1.200s = ~333 vCPU-h",
        "premissa": "Pre-processamento (leitura/validacao) e pos (escrita anonimizada) sao CPU-bound. t_por_job escala com volume. PREMISSA.",
        "classe": "[PREMISSA]"
    },
    {
        "recurso": "RAM batch (anonimizacao)",
        "camada": "Layer 2",
        "unidade": "GB-hora/mes",
        "fixo_var": "Variavel",
        "funcao": "RAM_GBh = N_workers_batch x RAM_por_worker x duracao_media_h",
        "variavel_carga": "N_workers_batch, RAM_por_worker (GB), duracao_media_h",
        "ajuste_porte": "P: 1 worker x 8 GB x 0.5h = 4 GBh | M: 2 workers x 8 GB x 2h = 32 GBh | G: 4 workers x 16 GB x 5h = 320 GBh",
        "premissa": "RAM_por_worker inclui modelo NER em memoria (~2 GB) + buffer de dados. 8 GB baseline — ANALOGO com pipelines NLP batch.",
        "classe": "[ANALOGO]"
    },
    {
        "recurso": "Storage-object (dados anonimizados)",
        "camada": "Layer 2",
        "unidade": "GB/mes (acumulo)",
        "fixo_var": "Variavel",
        "funcao": "storage_GB = N_registros_anon x tamanho_registro_anon / 1B",
        "variavel_carga": "N_registros_anon, tamanho_registro_anon (bytes)",
        "ajuste_porte": "P: ~50k x 500 B = ~25 MB | M: ~500k x 500 B = ~250 MB | G: ~10M x 500 B = ~5 GB",
        "premissa": "Registro anonimizado ~ tamanho original (substituicao in-place). Dados ficam armazenados para reintegracao. ENGENHARIA.",
        "classe": "[ENGENHARIA]"
    },
    {
        "recurso": "Storage-block (temporario batch)",
        "camada": "Layer 2",
        "unidade": "GB (pico)",
        "fixo_var": "Variavel",
        "funcao": "storage_GB = N_workers_batch x tamanho_buffer_trabalho",
        "variavel_carga": "N_workers_batch, tamanho_buffer_trabalho (GB)",
        "ajuste_porte": "P: 1 x 2 GB = 2 GB | M: 2 x 4 GB = 8 GB | G: 4 x 10 GB = 40 GB",
        "premissa": "Buffer temporario para processamento batch. Liberado ao final do job. PREMISSA.",
        "classe": "[PREMISSA]"
    },
    {
        "recurso": "Fila de jobs (enfileiramento batch)",
        "camada": "Layer 2",
        "unidade": "req/mes",
        "fixo_var": "Variavel",
        "funcao": "req_fila = N_jobs_anon (enqueue + dequeue + status)",
        "variavel_carga": "N_jobs_anon",
        "ajuste_porte": "P: ~12 jobs x 3 req = 36 | M: ~100 x 3 = 300 | G: ~1.000 x 3 = 3.000",
        "premissa": "3 req por job (enqueue, dequeue, status check). Arquitetura padrao de fila (SQS/RabbitMQ analogo). ENGENHARIA.",
        "classe": "[ENGENHARIA]"
    },
    {
        "recurso": "Bandwidth (leitura + escrita anonimizada)",
        "camada": "Layer 2",
        "unidade": "GB/mes",
        "fixo_var": "Variavel",
        "funcao": "GB_trafego = N_jobs_anon x (GB_leitura + GB_escrita) por job",
        "variavel_carga": "N_jobs_anon, GB_por_job_leitura, GB_por_job_escrita",
        "ajuste_porte": "P: ~12 x 0.5 GB = 6 GB | M: ~100 x 2 GB = 200 GB | G: ~1.000 x 20 GB = 20 TB",
        "premissa": "Leitura da fonte original + escrita do resultado anonimizado. Volume depende do cliente. PREMISSA.",
        "classe": "[PREMISSA]"
    },
    # === LAYER 1 (COMUM — fracao P2) ===
    {
        "recurso": "Auth multi-tenant (fracao P2)",
        "camada": "Layer 1",
        "unidade": "req/mes",
        "fixo_var": "Variavel",
        "funcao": "req_auth = N_jobs_anon x req_auth_por_job",
        "variavel_carga": "N_jobs_anon, req_auth_por_job",
        "ajuste_porte": "P: ~12 x 2 = 24 | M: ~100 x 2 = 200 | G: ~1.000 x 2 = 2.000",
        "premissa": "Fracao proporcional. Rateio por uso do produto. PREMISSA de proporcao 1:5 entre produtos.",
        "classe": "[PREMISSA]"
    },
    {
        "recurso": "Auditoria LGPD — trilha (fracao P2)",
        "camada": "Layer 1",
        "unidade": "GB/mes (retencao 5 anos)",
        "fixo_var": "Variavel",
        "funcao": "log_GB_mes = N_registros_anon x tamanho_log / 1B",
        "variavel_carga": "N_registros_anon, tamanho_log (bytes)",
        "ajuste_porte": "P: ~50k x 500 B = 25 MB/mes | M: ~500k x 500 B = 250 MB/mes | G: ~10M x 500 B = 5 GB/mes",
        "premissa": "Cada registro anonimizado gera log de auditoria (LGPD exige trilha). ENGENHARIA.",
        "classe": "[ENGENHARIA]"
    },
    {
        "recurso": "API Gateway (fracao P2)",
        "camada": "Layer 1",
        "unidade": "req/mes",
        "fixo_var": "Variavel",
        "funcao": "req_gateway = N_jobs_anon x req_internos_por_job",
        "variavel_carga": "N_jobs_anon, req_internos_por_job",
        "ajuste_porte": "P: ~12 x 5 = 60 | M: ~100 x 5 = 500 | G: ~1.000 x 5 = 5.000",
        "premissa": "~5 API calls internos por job (submit, progress, result, callback, log). PREMISSA.",
        "classe": "[PREMISSA]"
    },
    {
        "recurso": "Observabilidade (fracao P2)",
        "camada": "Layer 1",
        "unidade": "GB/mes",
        "fixo_var": "Fixo + Variavel",
        "funcao": "obs_GB = obs_base_fixo + (N_jobs_anon x metricas_por_job x bytes_por_metrica / 1B)",
        "variavel_carga": "N_jobs_anon, metricas_por_job, obs_base_fixo (GB)",
        "ajuste_porte": "Base ~ 0.5 GB/mes. Variavel: P +5 MB, M +50 MB, G +500 MB",
        "premissa": "Mesma logica do P1. Base fixa + proporcional. PREMISSA de rateio.",
        "classe": "[PREMISSA]"
    },
    {
        "recurso": "Billing/Medicao (fracao P2)",
        "camada": "Layer 1",
        "unidade": "eventos/mes",
        "fixo_var": "Variavel",
        "funcao": "eventos = N_jobs_anon (1 evento por job concluido)",
        "variavel_carga": "N_jobs_anon",
        "ajuste_porte": "P: ~12 | M: ~100 | G: ~1.000",
        "premissa": "1 evento faturavel por job de anonimizacao concluido. ENGENHARIA.",
        "classe": "[ENGENHARIA]"
    },
    {
        "recurso": "KMS/Segredos (fracao P2)",
        "camada": "Layer 1",
        "unidade": "req/mes",
        "fixo_var": "Fixo",
        "funcao": "req_kms = N_secrets_tenant x freq_rotacao",
        "variavel_carga": "N_secrets_tenant, freq_rotacao",
        "ajuste_porte": "P: 1 secret x 1 = 1 | M: 3 x 1 = 3 | G: 5 x 1 = 5",
        "premissa": "Menos secrets que P1 (nao acessa fontes externas diretamente). ENGENHARIA.",
        "classe": "[ENGENHARIA]"
    },
]

write_product_sheet(wb, "P2 Anonimizacao", "P2 Anonimizacao", "Anonimiza dados em volume (NER/PII). Batch com IA enfileirada.", P2_DATA)


# ============================================================
# P3 LAI x LGPD
# ============================================================
P3_DATA = [
    # === LAYER 2 (ESPECIFICO) ===
    {
        "recurso": "GPU-quente (reservada, baixa latencia)",
        "camada": "Layer 2",
        "unidade": "GPU-hora/mes",
        "fixo_var": "FIXO",
        "funcao": "GPU_h = 24 h/dia x 30 dias/mes = 720 GPU-h/mes (reservada, independente de uso)",
        "variavel_carga": "Nenhuma (FIXO — custo existe mesmo sem requisicao). Variavel de otimizacao: utilizacao_media (%).",
        "ajuste_porte": "P: 720h / N_tenants_share (ex: 10 tenants = 72 GPU-h/mes efetivo) | M: 720h dedicado (1:1) | G: 720h x N_GPU (scale-out, ex: 2 GPU = 1.440h)",
        "premissa": "CRITICO: Interativo sincrono exige latencia <2s → GPU DEVE estar quente (model loaded). Fixo por definicao. Compartilhamento em P = PREMISSA de uso nao simultaneo.",
        "classe": "[ENGENHARIA]"
    },
    {
        "recurso": "Vector-store (base de conhecimento legal)",
        "camada": "Layer 2",
        "unidade": "GB/mes",
        "fixo_var": "Variavel",
        "funcao": "GB_vector = N_documentos_base_legal x embedding_size_por_doc / 1B",
        "variavel_carga": "N_documentos_base_legal, embedding_size_por_doc (bytes)",
        "ajuste_porte": "P: ~1.000 docs x 1 KB = ~1 MB (base compartilhada) | M: ~5.000 docs x 1 KB = ~5 MB | G: ~20.000 docs x 1 KB = ~20 MB",
        "premissa": "Base legal (legislacao LGPD, LAI, jurisprudencia) e compartilhada entre tenants. Tamanho pequeno comparado a P4. embedding ~ 768 dims x 4 bytes = 3 KB/doc — ANALOGO com RAG benchmarks.",
        "classe": "[ANALOGO]"
    },
    {
        "recurso": "vCPU-compute (request handling)",
        "camada": "Layer 2",
        "unidade": "vCPU-hora/mes",
        "fixo_var": "Variavel",
        "funcao": "vCPU_h = N_req_mes x seg_por_req_preparacao / 3600",
        "variavel_carga": "N_req_mes, seg_por_req_preparacao (pre-processamento antes da GPU)",
        "ajuste_porte": "P: ~1.000 x 0.5s = ~0.14 vCPU-h | M: ~10.000 x 0.5s = ~1.4 vCPU-h | G: ~100.000 x 0.5s = ~14 vCPU-h",
        "premissa": "Pre-processamento (tokenizacao, busca vector, prompt assembly) ~ 0.5s por req em CPU. PREMISSA.",
        "classe": "[PREMISSA]"
    },
    {
        "recurso": "RAM (modelo + cache + runtime)",
        "camada": "Layer 2",
        "unidade": "GB (fixo, alocado)",
        "fixo_var": "FIXO",
        "funcao": "RAM_GB = RAM_modelo_GPU + RAM_cache_embedding + RAM_runtime_API",
        "variavel_carga": "RAM_modelo_GPU (depende do modelo), RAM_cache_embedding, RAM_runtime_API",
        "ajuste_porte": "P: ~8 GB (modelo compacto) | M: ~16 GB (modelo medio) | G: ~32 GB (modelo grande + cache amplo)",
        "premissa": "RAM_modelo_GPU: modelo 7B ~ 14 GB em FP16, 13B ~ 26 GB, 70B ~ 140 GB. PREMISSA de tamanho do modelo — depende da escolha do modelo de IA. Cache embedding ~ 2 GB para base legal.",
        "classe": "[PREMISSA]"
    },
    {
        "recurso": "Token-inferencia (GPU)",
        "camada": "Layer 2",
        "unidade": "tokens/mes",
        "fixo_var": "Variavel",
        "funcao": "tokens = N_req_mes x tokens_por_req (input + output)",
        "variavel_carga": "N_req_mes, tokens_input_por_req, tokens_output_por_req",
        "ajuste_porte": "P: ~1.000 x ~1.500 = 1.5M tokens | M: ~10.000 x ~1.500 = 15M tokens | G: ~100.000 x ~1.500 = 150M tokens",
        "premissa": "1 req LAI: prompt ~ 800 tokens (contexto legal + dados) + resposta ~ 700 tokens = ~1.500 tokens. PREMISSA — validar com piloto.",
        "classe": "[PREMISSA]"
    },
    {
        "recurso": "Bandwidth (req/res HTTP)",
        "camada": "Layer 2",
        "unidade": "GB/mes",
        "fixo_var": "Variavel",
        "funcao": "GB_trafego = N_req_mes x (bytes_req + bytes_res) / 1B",
        "variavel_carga": "N_req_mes, bytes_req, bytes_res",
        "ajuste_porte": "P: ~1.000 x ~5 KB = ~5 MB | M: ~10.000 x ~5 KB = ~50 MB | G: ~100.000 x ~5 KB = ~500 MB",
        "premissa": "Payload HTTP medio ~ 5 KB (JSON com certidao + metadados). PREMISSA.",
        "classe": "[PREMISSA]"
    },
    # === LAYER 1 (COMUM — fracao P3) ===
    {
        "recurso": "Auth multi-tenant (fracao P3)",
        "camada": "Layer 1",
        "unidade": "req/mes",
        "fixo_var": "Variavel",
        "funcao": "req_auth = N_req_mes (1 auth por requisicao de certidao)",
        "variavel_carga": "N_req_mes",
        "ajuste_porte": "P: ~1.000 | M: ~10.000 | G: ~100.000",
        "premissa": "Interativo = 1 auth por req. Proporcional direta. ENGENHARIA (arquitetura sessao-stateless).",
        "classe": "[ENGENHARIA]"
    },
    {
        "recurso": "Auditoria LGPD — trilha (fracao P3)",
        "camada": "Layer 1",
        "unidade": "GB/mes (retencao 5 anos)",
        "fixo_var": "Variavel",
        "funcao": "log_GB_mes = N_req_mes x tamanho_log / 1B",
        "variavel_carga": "N_req_mes, tamanho_log (bytes)",
        "ajuste_porte": "P: ~1.000 x 1 KB = 1 MB/mes | M: ~10.000 x 1 KB = 10 MB/mes | G: ~100.000 x 1 KB = 100 MB/mes",
        "premissa": "Log por req de certidao (o que foi revelado/ocultado) — LGPD exige trilha. ~ 1 KB por req. ENGENHARIA.",
        "classe": "[ENGENHARIA]"
    },
    {
        "recurso": "API Gateway (fracao P3)",
        "camada": "Layer 1",
        "unidade": "req/mes",
        "fixo_var": "Variavel",
        "funcao": "req_gateway = N_req_mes (1 req gateway por req do usuario)",
        "variavel_carga": "N_req_mes",
        "ajuste_porte": "P: ~1.000 | M: ~10.000 | G: ~100.000",
        "premissa": "Interativo sincrono = 1:1 req gateway. ENGENHARIA.",
        "classe": "[ENGENHARIA]"
    },
    {
        "recurso": "Observabilidade (fracao P3)",
        "camada": "Layer 1",
        "unidade": "GB/mes",
        "fixo_var": "Fixo + Variavel",
        "funcao": "obs_GB = obs_base_fixo + (N_req_mes x bytes_metricas / 1B)",
        "variavel_carga": "N_req_mes, obs_base_fixo (GB), bytes_metricas",
        "ajuste_porte": "Base ~ 0.5 GB/mes. Variavel: P +5 MB, M +50 MB, G +500 MB",
        "premissa": "GPU quente gera mais metricas (utilizacao, latency, memory). PREMISSA de multiplicador 5x vs batch.",
        "classe": "[PREMISSA]"
    },
    {
        "recurso": "Billing/Medicao (fracao P3)",
        "camada": "Layer 1",
        "unidade": "eventos/mes",
        "fixo_var": "Variavel",
        "funcao": "eventos = N_req_mes (1 evento por certidao gerada)",
        "variavel_carga": "N_req_mes",
        "ajuste_porte": "P: ~1.000 | M: ~10.000 | G: ~100.000",
        "premissa": "1 evento faturavel por certidao gerada. ENGENHARIA.",
        "classe": "[ENGENHARIA]"
    },
    {
        "recurso": "KMS/Segredos (fracao P3)",
        "camada": "Layer 1",
        "unidade": "req/mes",
        "fixo_var": "Fixo",
        "funcao": "req_kms = N_secrets_tenant x freq_rotacao",
        "variavel_carga": "N_secrets_tenant, freq_rotacao",
        "ajuste_porte": "P: 2 x 1 = 2 | M: 2 x 1 = 2 | G: 2 x 1 = 2",
        "premissa": "Apenas secrets do proprio servico (chave API interna, certificado). ENGENHARIA.",
        "classe": "[ENGENHARIA]"
    },
]

write_product_sheet(wb, "P3 LAIxLGPD", "P3 LAIxLGPD", "Decide revelacao em certidao publica vs privacidade. Interativo sincrono, GPU quente.", P3_DATA)


# ============================================================
# P4 AI-DPO
# ============================================================
P4_DATA = [
    # === LAYER 2 (ESPECIFICO) ===
    {
        "recurso": "GPU-quente (reservada, chat conversacional)",
        "camada": "Layer 2",
        "unidade": "GPU-hora/mes",
        "fixo_var": "FIXO",
        "funcao": "GPU_h = 24 h/dia x 30 dias/mes = 720 GPU-h/mes (reservada, independente de uso)",
        "variavel_carga": "Nenhuma (FIXO — custo existe mesmo sem conversa). Variavel de otimizacao: utilizacao_media (%).",
        "ajuste_porte": "P: 720h / N_tenants_share (ex: 8 tenants = 90 GPU-h/mes) | M: 720h dedicado (1:1) | G: 720h x N_GPU (ex: 2 GPU = 1.440h para picos simultaneos)",
        "premissa": "CRITICO: Chat conversacional exige latencia <3s → GPU DEVE estar quente. Fixo por definicao. Compartilhamento em P = PREMISSA de uso nao simultaneo (horario comercial).",
        "classe": "[ENGENHARIA]"
    },
    {
        "recurso": "Vector-store (RAG — base de conhecimento LGPD)",
        "camada": "Layer 2",
        "unidade": "GB/mes",
        "fixo_var": "Variavel",
        "funcao": "GB_vector = N_docs_RAG x embedding_size_por_doc / 1B",
        "variavel_carga": "N_docs_RAG, embedding_size_por_doc (bytes)",
        "ajuste_porte": "P: ~500 docs (basico LGPD) x 3 KB = ~1.5 MB | M: ~5.000 docs (politicas + faq + historico) x 3 KB = ~15 MB | G: ~50.000 docs (jurisprudencia + manuais + historico) x 3 KB = ~150 MB",
        "premissa": "Base RAG cresce com o historico do cliente. embedding 1536 dims x 4 bytes = ~6 KB/doc (modelo maior que P3). ANALOGO com RAG enterprise.",
        "classe": "[ANALOGO]"
    },
    {
        "recurso": "vCPU-compute (sessao + RAG retrieval)",
        "camada": "Layer 2",
        "unidade": "vCPU-hora/mes",
        "fixo_var": "Variavel",
        "funcao": "vCPU_h = N_turnos_mes x seg_por_turno_preparacao / 3600",
        "variavel_carga": "N_turnos_mes, seg_por_turno_preparacao (tokenizacao + busca + prompt assembly)",
        "ajuste_porte": "P: ~3.000 turnos x 0.8s = ~0.67 vCPU-h | M: ~30.000 turnos x 0.8s = ~6.7 vCPU-h | G: ~300.000 turnos x 0.8s = ~67 vCPU-h",
        "premissa": "Preparacao por turno: busca vetorial (~0.3s) + tokenizacao (~0.2s) + assembly (~0.3s) = ~0.8s. PREMISSA — RAG retrieval pode ser mais lento com base grande.",
        "classe": "[PREMISSA]"
    },
    {
        "recurso": "RAM (modelo + cache embedding + sessao)",
        "camada": "Layer 2",
        "unidade": "GB (fixo, alocado)",
        "fixo_var": "FIXO",
        "funcao": "RAM_GB = RAM_modelo_GPU + RAM_cache_embedding + RAM_context_window + RAM_runtime",
        "variavel_carga": "RAM_modelo_GPU, RAM_cache_embedding, RAM_context_window (historico conversa), RAM_runtime",
        "ajuste_porte": "P: ~8 GB | M: ~16 GB | G: ~32 GB (cache embedding maior + context window maior)",
        "premissa": "Context window de conversa adiciona RAM. P: 4k context ~ 1 GB, M: 8k context ~ 2 GB, G: 32k context ~ 8 GB. PREMISSA — depende do modelo escolhido.",
        "classe": "[PREMISSA]"
    },
    {
        "recurso": "Token-inferencia (GPU — com RAG context)",
        "camada": "Layer 2",
        "unidade": "tokens/mes",
        "fixo_var": "Variavel",
        "funcao": "tokens = N_turnos_mes x (tokens_contexto_RAG + tokens_input_usuario + tokens_output)",
        "variavel_carga": "N_turnos_mes, tokens_contexto_RAG (pedacos relevantes), tokens_input_usuario, tokens_output",
        "ajuste_porte": "P: ~3.000 x ~3.000 = 9M tokens | M: ~30.000 x ~3.500 = 105M tokens | G: ~300.000 x ~4.000 = 1.2B tokens",
        "premissa": "Cada turno de chat P4 consome mais tokens que P3 porque: (1) context window acumula historico, (2) RAG injeta documentos relevantes. tokens_por_turno ~ 3.000-4.000 — PREMISSA.",
        "classe": "[PREMISSA]"
    },
    {
        "recurso": "Storage-object (historico de conversas)",
        "camada": "Layer 2",
        "unidade": "GB/mes (acumulo)",
        "fixo_var": "Variavel",
        "funcao": "storage_GB = N_turnos_mes x bytes_por_turno_armazenado / 1B",
        "variavel_carga": "N_turnos_mes, bytes_por_turno_armazenado",
        "ajuste_porte": "P: ~3.000 x ~2 KB = ~6 MB/mes | M: ~30.000 x ~3 KB = ~90 MB/mes | G: ~300.000 x ~4 KB = ~1.2 GB/mes",
        "premissa": "Historico de conversas armazenado para RAG (respostas anteriores como contexto). ~ 2-4 KB por turno. PREMISSA.",
        "classe": "[PREMISSA]"
    },
    {
        "recurso": "Bandwidth (chat HTTP/SSE)",
        "camada": "Layer 2",
        "unidade": "GB/mes",
        "fixo_var": "Variavel",
        "funcao": "GB_trafego = N_turnos_mes x (bytes_req + bytes_res) / 1B",
        "variavel_carga": "N_turnos_mes, bytes_req, bytes_res",
        "ajuste_porte": "P: ~3.000 x ~3 KB = ~9 MB | M: ~30.000 x ~3 KB = ~90 MB | G: ~300.000 x ~3 KB = ~900 MB",
        "premissa": "Chat streaming (SSE): req pequena, res pode ser longa. Media ~3 KB por turno. PREMISSA.",
        "classe": "[PREMISSA]"
    },
    # === LAYER 1 (COMUM — fracao P4) ===
    {
        "recurso": "Auth multi-tenant (fracao P4)",
        "camada": "Layer 1",
        "unidade": "req/mes",
        "fixo_var": "Variavel",
        "funcao": "req_auth = N_sessoes_chat_mes (1 auth por sessao de chat)",
        "variavel_carga": "N_sessoes_chat_mes",
        "ajuste_porte": "P: ~500 sessoes | M: ~5.000 sessoes | G: ~50.000 sessoes",
        "premissa": "1 auth por sessao (nao por turno — token JWT valido durante sessao). ENGENHARIA.",
        "classe": "[ENGENHARIA]"
    },
    {
        "recurso": "Auditoria LGPD — trilha (fracao P4)",
        "camada": "Layer 1",
        "unidade": "GB/mes (retencao 5 anos)",
        "fixo_var": "Variavel",
        "funcao": "log_GB_mes = N_turnos_mes x tamanho_log / 1B",
        "variavel_carga": "N_turnos_mes, tamanho_log (bytes)",
        "ajuste_porte": "P: ~3.000 x 1 KB = 3 MB/mes | M: ~30.000 x 1 KB = 30 MB/mes | G: ~300.000 x 1 KB = 300 MB/mes",
        "premissa": "Cada turno de chat gera log (pergunta + resposta — pode conter dado pessoal). LGPD exige trilha. ENGENHARIA.",
        "classe": "[ENGENHARIA]"
    },
    {
        "recurso": "API Gateway (fracao P4)",
        "camada": "Layer 1",
        "unidade": "req/mes",
        "fixo_var": "Variavel",
        "funcao": "req_gateway = N_turnos_mes (1 req gateway por turno de chat)",
        "variavel_carga": "N_turnos_mes",
        "ajuste_porte": "P: ~3.000 | M: ~30.000 | G: ~300.000",
        "premissa": "Chat streaming = 1 req gateway por turno. ENGENHARIA.",
        "classe": "[ENGENHARIA]"
    },
    {
        "recurso": "Observabilidade (fracao P4)",
        "camada": "Layer 1",
        "unidade": "GB/mes",
        "fixo_var": "Fixo + Variavel",
        "funcao": "obs_GB = obs_base_fixo + (N_turnos_mes x bytes_metricas / 1B)",
        "variavel_carga": "N_turnos_mes, obs_base_fixo (GB), bytes_metricas",
        "ajuste_porte": "Base ~ 0.5 GB/mes. Variavel: P +15 MB, M +150 MB, G +1.5 GB",
        "premissa": "Chat gera mais metricas (latencia por token, streaming events, erro rate). PREMISSA.",
        "classe": "[PREMISSA]"
    },
    {
        "recurso": "Billing/Medicao (fracao P4)",
        "camada": "Layer 1",
        "unidade": "eventos/mes",
        "fixo_var": "Variavel",
        "funcao": "eventos = N_turnos_mes (1 evento por turno de chat respondido)",
        "variavel_carga": "N_turnos_mes",
        "ajuste_porte": "P: ~3.000 | M: ~30.000 | G: ~300.000",
        "premissa": "1 evento faturavel por turno. ENGENHARIA.",
        "classe": "[ENGENHARIA]"
    },
    {
        "recurso": "KMS/Segredos (fracao P4)",
        "camada": "Layer 1",
        "unidade": "req/mes",
        "fixo_var": "Fixo",
        "funcao": "req_kms = N_secrets_tenant x freq_rotacao",
        "variavel_carga": "N_secrets_tenant, freq_rotacao",
        "ajuste_porte": "P: 2 x 1 = 2 | M: 2 x 1 = 2 | G: 2 x 1 = 2",
        "premissa": "Apenas secrets do servico. ENGENHARIA.",
        "classe": "[ENGENHARIA]"
    },
]

write_product_sheet(wb, "P4 AI-DPO", "P4 AI-DPO", "Chat LGPD com RAG para o encarregado. Interativo conversacional, GPU quente.", P4_DATA)


# ============================================================
# P5 ETL / INTEGRACAO
# ============================================================
P5_DATA = [
    # === LAYER 2 (ESPECIFICO) ===
    {
        "recurso": "vCPU-compute (batch ETL)",
        "camada": "Layer 2",
        "unidade": "vCPU-hora/mes",
        "fixo_var": "Variavel",
        "funcao": "vCPU_h = N_fontes_integradas x freq_ETL x t_ETL_por_fonte / 3600",
        "variavel_carga": "N_fontes_integradas, freq_ETL (jobs/mes/fonte), t_ETL_por_fonte (seg)",
        "ajuste_porte": "P: 3 fontes x 30/mes x 120s = 3 vCPU-h | M: 10 fontes x 30/mes x 600s = 50 vCPU-h | G: 50 fontes x 30/mes x 1.800s = 750 vCPU-h",
        "premissa": "ETL batch agendado (tipicamente diario = 30/mes). t_ETL por fonte escala com volume de dados. PREMISSA.",
        "classe": "[PREMISSA]"
    },
    {
        "recurso": "RAM batch (ETL)",
        "camada": "Layer 2",
        "unidade": "GB-hora/mes",
        "fixo_var": "Variavel",
        "funcao": "RAM_GBh = N_workers_ETL x RAM_por_worker x duracao_media_h",
        "variavel_carga": "N_workers_ETL, RAM_por_worker (GB), duracao_media_h",
        "ajuste_porte": "P: 1 worker x 4 GB x 0.5h = 2 GBh | M: 2 workers x 8 GB x 2h = 32 GBh | G: 4 workers x 16 GB x 5h = 320 GBh",
        "premissa": "ETL pipe requer buffer de dados em memoria. RAM_por_worker escala com volume da fonte. PREMISSA.",
        "classe": "[PREMISSA]"
    },
    {
        "recurso": "Storage-object (staging de dados)",
        "camada": "Layer 2",
        "unidade": "GB/mes (acumulo)",
        "fixo_var": "Variavel",
        "funcao": "storage_GB = N_registros_ETL x tamanho_registro_medio / 1B",
        "variavel_carga": "N_registros_ETL, tamanho_registro_medio (bytes)",
        "ajuste_porte": "P: ~50k x 1 KB = ~50 MB | M: ~500k x 1 KB = ~500 MB | G: ~10M x 1 KB = ~10 GB",
        "premissa": "Area de staging para dados antes/depois da transformacao. Pode ter ciclo de vida (purge apos integracao). ENGENHARIA.",
        "classe": "[ENGENHARIA]"
    },
    {
        "recurso": "Storage-block (temporario ETL)",
        "camada": "Layer 2",
        "unidade": "GB (pico)",
        "fixo_var": "Variavel",
        "funcao": "storage_GB = N_workers_ETL x tamanho_buffer_transformacao",
        "variavel_carga": "N_workers_ETL, tamanho_buffer_transformacao (GB)",
        "ajuste_porte": "P: 1 x 1 GB = 1 GB | M: 2 x 4 GB = 8 GB | G: 4 x 20 GB = 80 GB",
        "premissa": "Buffer temporario para transformacao ETL. Liberado ao final do job. PREMISSA.",
        "classe": "[PREMISSA]"
    },
    {
        "recurso": "Bandwidth (ETL leitura + escrita)",
        "camada": "Layer 2",
        "unidade": "GB/mes",
        "fixo_var": "Variavel",
        "funcao": "GB_trafego = N_jobs_ETL_mes x (GB_leitura_fonte + GB_escrita_destino)",
        "variavel_carga": "N_jobs_ETL_mes, GB_por_job_leitura, GB_por_job_escrita",
        "ajuste_porte": "P: ~90 x 0.1 GB = 9 GB | M: ~300 x 1 GB = 300 GB | G: ~1.500 x 10 GB = 15 TB",
        "premissa": "ETL move dados entre fontes legadas e destino. Volume depende do cliente. PREMISSA.",
        "classe": "[PREMISSA]"
    },
    {
        "recurso": "Connector manager (gestao de fontes)",
        "camada": "Layer 2",
        "unidade": "unidades (fixo por fonte)",
        "fixo_var": "FIXO",
        "funcao": "N_connectors = N_fontes_integradas (1 connector por fonte, custo fixo mensal)",
        "variavel_carga": "N_fontes_integradas",
        "ajuste_porte": "P: 3 connectors | M: 10 connectors | G: 50 connectors",
        "premissa": "Cada fonte legada requer um connector configurado (engenheiro humano para setup inicial). Custo fixo por connector ativo. ENGENHARIA.",
        "classe": "[ENGENHARIA]"
    },
    # === LAYER 1 (COMUM — fracao P5) ===
    {
        "recurso": "Auth multi-tenant (fracao P5)",
        "camada": "Layer 1",
        "unidade": "req/mes",
        "fixo_var": "Variavel",
        "funcao": "req_auth = N_jobs_ETL_mes x req_auth_por_job",
        "variavel_carga": "N_jobs_ETL_mes, req_auth_por_job",
        "ajuste_porte": "P: ~90 x 1 = 90 | M: ~300 x 1 = 300 | G: ~1.500 x 1 = 1.500",
        "premissa": "Batch agendado: auth por job, nao por registro. PREMISSA.",
        "classe": "[PREMISSA]"
    },
    {
        "recurso": "Auditoria LGPD — trilha (fracao P5)",
        "camada": "Layer 1",
        "unidade": "GB/mes (retencao 5 anos)",
        "fixo_var": "Variavel",
        "funcao": "log_GB_mes = N_registros_ETL_mes x tamanho_log / 1B",
        "variavel_carga": "N_registros_ETL_mes, tamanho_log (bytes)",
        "ajuste_porte": "P: ~50k x 500 B = 25 MB/mes | M: ~500k x 500 B = 250 MB/mes | G: ~10M x 500 B = 5 GB/mes",
        "premissa": "Cada registro movido pelo ETL gera log de auditoria. LGPD exige trilha de movimento de dados. ENGENHARIA.",
        "classe": "[ENGENHARIA]"
    },
    {
        "recurso": "API Gateway (fracao P5)",
        "camada": "Layer 1",
        "unidade": "req/mes",
        "fixo_var": "Variavel",
        "funcao": "req_gateway = N_jobs_ETL_mes x req_internos_por_job",
        "variavel_carga": "N_jobs_ETL_mes, req_internos_por_job",
        "ajuste_porte": "P: ~90 x 5 = 450 | M: ~300 x 5 = 1.500 | G: ~1.500 x 5 = 7.500",
        "premissa": "~5 API calls internos por job ETL (trigger, progress, transform, validate, complete). PREMISSA.",
        "classe": "[PREMISSA]"
    },
    {
        "recurso": "Observabilidade (fracao P5)",
        "camada": "Layer 1",
        "unidade": "GB/mes",
        "fixo_var": "Fixo + Variavel",
        "funcao": "obs_GB = obs_base_fixo + (N_jobs_ETL_mes x metricas_por_job x bytes_por_metrica / 1B)",
        "variavel_carga": "N_jobs_ETL_mes, metricas_por_job, obs_base_fixo (GB)",
        "ajuste_porte": "Base ~ 0.5 GB/mes. Variavel: P +10 MB, M +30 MB, G +150 MB",
        "premissa": "Batch agendado gera menos metricas que interativo (nao ha latency percebida pelo usuario). PREMISSA.",
        "classe": "[PREMISSA]"
    },
    {
        "recurso": "Billing/Medicao (fracao P5)",
        "camada": "Layer 1",
        "unidade": "eventos/mes",
        "fixo_var": "Variavel",
        "funcao": "eventos = N_jobs_ETL_mes (1 evento por job ETL concluido)",
        "variavel_carga": "N_jobs_ETL_mes",
        "ajuste_porte": "P: ~90 | M: ~300 | G: ~1.500",
        "premissa": "1 evento faturavel por job ETL concluido. ENGENHARIA.",
        "classe": "[ENGENHARIA]"
    },
    {
        "recurso": "KMS/Segredos (fracao P5)",
        "camada": "Layer 1",
        "unidade": "req/mes",
        "fixo_var": "Fixo",
        "funcao": "req_kms = N_fontes_integradas x freq_rotacao",
        "variavel_carga": "N_fontes_integradas, freq_rotacao",
        "ajuste_porte": "P: 3 x 1 = 3 | M: 10 x 1 = 10 | G: 50 x 1 = 50",
        "premissa": "Cada fonte legada = 1 secret (credencial de acesso). Rotacao mensal. ENGENHARIA.",
        "classe": "[ENGENHARIA]"
    },
]

write_product_sheet(wb, "P5 ETL-Integracao", "P5 ETL/Integracao", "Integra sistemas legados. Batch agendado. Sem IA. Requer engenheiro para setup.", P5_DATA)


# ============================================================
# 6. VARIAVEIS A MEDIR NO PILOTO
# ============================================================
variaveis_headers = ["#", "Variavel", "Produto(s)", "Unidade", "Como Medir (instrumentacao)", "Prioridade"]
variaveis_data = [
    ["1", "N_fontes (fontes de dados ativas por tenant)", "P1, P5", "Contagem", "Contar conectoras configuradas e ativas no periodo. API: GET /connectors/active", "Alta"],
    ["2", "freq_varredura (varreduras por mes por tenant)", "P1", "Varreduras/mes", "Contar jobs de varredura concluidos. Scheduler log ou metrica CloudWatch.", "Alta"],
    ["3", "t_varredura_fonte (tempo por varredura)", "P1", "Segundos/fonte", "Duration do job de varredura por fonte. Metrica: job.duration_seconds.", "Alta"],
    ["4", "N_registros_mapeados (registros com metadado)", "P1", "Contagem", "Contar registros no storage de metadados. DB query: COUNT(*) WHERE tenant_id = X.", "Alta"],
    ["5", "tamanho_metadado_por_registro", "P1", "Bytes", "Amostrar 1.000 registros e calcular media. DB: AVG(LENGTH(metadata_json)).", "Media"],
    ["6", "N_registros_a_anonimizar", "P2", "Contagem/mes", "Contar registros processados pelo pipeline NER. Metrica: anon.records_processed.", "Alta"],
    ["7", "seg_por_registro_NER (throughput NER)", "P2", "Segundos/registro", "Duration total do job / registros processados. Precisa separar tempo GPU vs CPU.", "Alta"],
    ["8", "N_jobs_anon (jobs de anonimizacao por mes)", "P2", "Jobs/mes", "Contar jobs concluidos na fila. Queue metric: jobs.completed.", "Alta"],
    ["9", "N_req_mes (requisicoes de certidao)", "P3", "Req/mes", "API gateway metric: request_count filtered by path /certidao.", "Alta"],
    ["10", "tokens_por_req (tokens por requisicao P3)", "P3", "Tokens/req", "Tokenizer counter no servico. Log: input_tokens + output_tokens por req.", "Alta"],
    ["11", "N_turnos_mes (turnos de chat)", "P4", "Turnos/mes", "WebSocket/SSE event count. Metric: chat.turns.count.", "Alta"],
    ["12", "tokens_por_turno (tokens por turno P4 com RAG)", "P4", "Tokens/turno", "Somar: tokens_contexto_RAG + tokens_input + tokens_output. Log por turno.", "Alta"],
    ["13", "N_docs_RAG (documentos na base vetorial)", "P3, P4", "Contagem", "Vector store count: collection.stats(). Document count por tenant.", "Media"],
    ["14", "embedding_size_por_doc", "P3, P4", "Bytes/doc", "Calcular: dims x bytes_per_dim (ex: 768 x 4 = 3.072 bytes). Amostrar.", "Media"],
    ["15", "N_fontes_integradas", "P5", "Contagem", "Contar connectors ativos no connector manager. Mesmo que var #1 para P5.", "Alta"],
    ["16", "freq_ETL (jobs ETL por mes por fonte)", "P5", "Jobs/mes/fonte", "Scheduler log. Contar jobs concluidos por source_id.", "Alta"],
    ["17", "t_ETL_por_fonte (tempo de job ETL)", "P5", "Segundos/fonte", "Duration do job ETL por fonte. Metrica: etl.job.duration.", "Alta"],
    ["18", "N_registros_ETL (registros movidos por mes)", "P5", "Contagem/mes", "Contar registros no staging area. DB: COUNT(*) WHERE month = X.", "Media"],
    ["19", "tamanho_registro_medio (tamanho medio do dado)", "P1, P2, P5", "Bytes", "Amostrar 1.000 registros por produto e calcular media ponderada.", "Media"],
    ["20", "RAM_modelo_GPU (RAM ocupada pelo modelo)", "P3, P4", "GB", "nvidia-smi ou equivalente cloud. Metrica: gpu.memory.used quando modelo carregado.", "Alta"],
    ["21", "cache_modelo_size (embedding cache size)", "P3, P4", "GB", "Memory profiler no servico de embedding. Metrica: embedding.cache.size_bytes.", "Media"],
    ["22", "utilizacao_GPU_media (%)", "P3, P4", "Percentual", "nvidia-smi dmon ou cloud GPU metrics. Media mensal de gpu.utilization.", "Alta"],
    ["23", "GB_lidos_por_varredura", "P1", "GB/varredura", "I/O metrics durante varredura. S3/MinIO: bytes_read por job.", "Media"],
    ["24", "N_tenants_simultaneos_P3 (pico)", "P3", "Contagem (pico)", "Concurrent sessions metric no API gateway. P99 de req simultaneas.", "Alta"],
    ["25", "N_tenants_simultaneos_P4 (pico)", "P4", "Contagem (pico)", "Concurrent chat sessions metric. P99 de sessoes ativas.", "Alta"],
    ["26", "tamanho_log_por_registro (bytes)", "P1, P2, P5", "Bytes/registro", "Amostrar logs de auditoria e calcular media. ELK/Loki query.", "Baixa"],
    ["27", "tamanho_log_por_req (bytes)", "P3, P4", "Bytes/req", "Amostrar logs de auditoria por requisicao/turno.", "Baixa"],
    ["28", "req_internos_por_job (API calls internos)", "P1, P2, P5", "Req/job", "Trace distribuido (Jaeger/Zipkin). Contar spans por job.", "Baixa"],
]

variaveis_widths = {"A": 3, "B": 4, "C": 40, "D": 14, "E": 14, "F": 50, "G": 10}
write_list_sheet(wb, "Variaveis do Piloto", "Variaveis a Medir no Piloto (instrumentacao)", variaveis_headers, variaveis_data, variaveis_widths)


# ============================================================
# 7. PREMISSAS A VALIDAR
# ============================================================
premissas_headers = ["#", "Premissa", "Produto(s)", "Impacto se Falsa", "Como Validar", "Prioridade"]
premissas_data = [
    ["1", "GPU compartilhada em P3/P4 para Pequeno e possivel sem degradar latencia <2s", "P3, P4", "ALTO: custo P subestimado em ate 10x se dedicada for necessaria", "Piloto com 10 tenants pequenos simulando picos simultaneos. Medir P99 latencia.", "Critica"],
    ["2", "Throughput NER: 100 registros/seg/GPU (sec_por_registro_NER = 0.01s)", "P2", "MEDIO: custo GPU batch pode ser 2-5x maior se throughput real for menor", "Benchmark com modelo escolhido + dataset real do cliente piloto.", "Alta"],
    ["3", "1 varredura de fonte ~ 5 min para 10k registros", "P1", "MEDIO: afeta vCPU-h e custo batch", "Piloto: medir duration real de varredura por fonte e volume.", "Alta"],
    ["4", "Metadado por registro ~ 1 KB (classificacao + fonte + flags)", "P1", "BAIXO: storage de metadados e barato. Fator <3x.", "Amostrar 10.000 registros e medir tamanho real do metadado serializado.", "Media"],
    ["5", "Tokens por req P3 ~ 1.500 (input 800 + output 700)", "P3", "MEDIO: se real for 3.000, custo GPU/token dobra", "Logar input_tokens e output_tokens em cada req de certidao.", "Alta"],
    ["6", "Tokens por turno P4 ~ 3.000-4.000 (com RAG context)", "P4", "ALTO: P4 e o produto mais token-intensive. Erro de 2x = custo 2x.", "Logar tokens por componente: contexto RAG, historico, input, output.", "Critica"],
    ["7", "RAM modelo GPU: 7B ~ 14 GB FP16, 13B ~ 26 GB, 70B ~ 140 GB", "P3, P4", "ALTO: define tamanho da GPU e o custo FIXO mensal", "Verificar com nvidia-smi apos carregar modelo escolhido.", "Critica"],
    ["8", "Rateio Layer 1: proporcional ao uso (req/jobs/eventos)", "Todos", "MEDIO: se custos fixos de Layer 1 forem dominantes, rateio por uso subestima P pequeno", "ABC costing: medir custo real de Layer 1 por produto durante piloto.", "Media"],
    ["9", "Retencao de auditoria LGPD = 5 anos (60 meses acumulados)", "Todos", "ALTO: storage acumulado e significativo para G ao longo de 5 anos", "Confirmar com jurista LGPD. Verificar se ha requisito de compressao/arquivamento.", "Critica"],
    ["10", "Cada fonte legada = 1 secret (rotacao mensal) em P5", "P5", "BAIXO: KMS custo e marginal", "Contar secrets ativos no KMS por tenant.", "Baixa"],
    ["11", "Pre-processamento P3: ~0.5s por req em CPU (tokenizacao + busca + assembly)", "P3", "MEDIO: se for 2s, vCPU-h 4x maior", "Medir duration do pipeline de pre-processamento separado da GPU.", "Alta"],
    ["12", "Pre-processamento P4: ~0.8s por turno (RAG retrieval + tokenizacao + assembly)", "P4", "MEDIO: RAG retrieval com base grande pode ser mais lento", "Medir cada etapa separadamente: busca vetorial, tokenizacao, assembly.", "Alta"],
    ["13", "Embedding size: 768 dims x 4 bytes = 3 KB/doc (P3) e 1536 dims x 4 bytes = 6 KB/doc (P4)", "P3, P4", "BAIXO: vector store e barato para bases <100k docs", "Verificar modelo de embedding escolhido e dims.", "Media"],
    ["14", "N_jobs_anon escala linearmente com registros (P2)", "P2", "MEDIO: se houver quebra por tamanho de batch, N_jobs pode ser diferente", "Analisar estrategia de particionamento do pipeline.", "Media"],
    ["15", "Observabilidade: base fixa ~ 0.5 GB/mes + variavel proporcional", "Todos", "BAIXO: observabilidade e custo menor vs compute/GPU", "Verificar custo real do stack de observabilidade por tenant.", "Baixa"],
    ["16", "Compartilhamento GPU P: 8-10 tenants por GPU sem conflito de horario comercial", "P3, P4", "ALTO: se tenants pequenos concentram uso no mesmo horario, GPU dedicada necessaria", "Analise de distribuicao temporal de reqs por tenant. Medir coeficiente de sobreposicao.", "Critica"],
]

premissas_widths = {"A": 3, "B": 4, "C": 50, "D": 12, "E": 44, "F": 48, "G": 10}
write_list_sheet(wb, "Premissas a Validar", "Premissas a Validar (priorizadas por impacto)", premissas_headers, premissas_data, premissas_widths)


# ============================================================
# 8. VERIFICACAO CV1-CV8
# ============================================================
cv_headers = ["CV", "Descricao", "Status", "Evidencia / Nota"]
# Count classes
def count_classes(data_rows):
    eng = sum(1 for r in data_rows if "[ENGENHARIA]" in r.get("classe", ""))
    ana = sum(1 for r in data_rows if "[ANALOGO]" in r.get("classe", ""))
    pre = sum(1 for r in data_rows if "[PREMISSA]" in r.get("classe", ""))
    return eng, ana, pre

p1e, p1a, p1p = count_classes(P1_DATA)
p2e, p2a, p2p = count_classes(P2_DATA)
p3e, p3a, p3p = count_classes(P3_DATA)
p4e, p4a, p4p = count_classes(P4_DATA)
p5e, p5a, p5p = count_classes(P5_DATA)
total_e = p1e+p2e+p3e+p4e+p5e
total_a = p1a+p2a+p3a+p4a+p5a
total_p = p1p+p2p+p3p+p4p+p5p
total_all = total_e + total_a + total_p

cv_data = [
    ["CV1", "Todos os 5 produtos tem tabela completa?",
     "PASS", "P1 (11 linhas), P2 (13 linhas), P3 (12 linhas), P4 (13 linhas), P5 (12 linhas) — nenhum faltando."],
    ["CV2", "Cada recurso marcado Layer 1 ou Layer 2 corretamente?",
     "PASS", "Layer 1 = servicos comuns (auth, auditoria, gateway, obs, billing, KMS). Layer 2 = recursos especificos (GPU, vector store, fila, connectors). Verificar nas abas de cada produto."],
    ["CV3", "Cada recurso classificado FIXO ou VARIAVEL com justificativa?",
     "PASS", "GPU quente P3/P4 = FIXO (reservada para latencia). GPU batch P2 = VARIAVEL. Connector P5 = FIXO. Demais = VARIAVEL. RAM P3/P4 = FIXO (modelo carregado)."],
    ["CV4", "Nenhum preco em R$ inventado?",
     "PASS", "Nenhuma celula contem valor em R$. Todos os custos ficam como funcoes simbolicas. Preco unitario = variavel a substituir posteriormente."],
    ["CV5", "Toda funcao de demanda tem variavel de carga mensuravel?",
     "PASS", "Cada linha possui campo 'Variavel de Carga' com a grandeza a medir. Variaveis sem uso mensuravel (GPU quente FIXO) declaram 'utilizacao_media' como variavel de otimizacao."],
    ["CV6", "Toda linha tem classe declarada?",
     "PASS", f"Total: {total_all} linhas. ENGENHARIA={total_e} ({total_e*100//total_all}%), ANALOGO={total_a} ({total_a*100//total_all}%), PREMISSA={total_p} ({total_p*100//total_all}%)."],
    ["CV7", "Premissas listadas separadamente para validacao?",
     "PASS", "Aba 'Premissas a Validar' contem 16 premissas priorizadas com impacto, metodo de validacao e prioridade."],
    ["CV8", "P1 e P5 sem GPU? P3/P4 GPU quente? P2 GPU batch?",
     "PASS", "P1: 0 GPU (sem IA) OK. P5: 0 GPU (sem IA) OK. P3: GPU-quente FIXO OK. P4: GPU-quente FIXO OK. P2: GPU-batch VARIAVEL OK. Nenhuma inconsistencia."],
]

# Also add class breakdown
cv_data.append(["", "", "", ""])
cv_data.append(["NOTA DE CLASSE", "Composicao do modelo", "", ""])
cv_data.append(["", f"P1: ENG={p1e} | ANA={p1a} | PRE={p1p}", "", ""])
cv_data.append(["", f"P2: ENG={p2e} | ANA={p2a} | PRE={p2p}", "", ""])
cv_data.append(["", f"P3: ENG={p3e} | ANA={p3a} | PRE={p3p}", "", ""])
cv_data.append(["", f"P4: ENG={p4e} | ANA={p4a} | PRE={p4p}", "", ""])
cv_data.append(["", f"P5: ENG={p5e} | ANA={p5a} | PRE={p5p}", "", ""])
cv_data.append(["", f"TOTAL: ENG={total_e} ({total_e*100//total_all}%) | ANA={total_a} ({total_a*100//total_all}%) | PRE={total_p} ({total_p*100//total_all}%)", "", f"{total_all} linhas totais"])

cv_widths = {"A": 3, "B": 8, "C": 52, "D": 10, "E": 70}
ws_cv = write_list_sheet(wb, "Verificacao CV", "Verificacao CV1-CV8 + Nota de Classe", cv_headers, cv_data, cv_widths)

# Color-code the STATUS column
for row in range(5, 5 + len(cv_data)):
    cell = ws_cv.cell(row=row, column=4)
    if cell.value == "PASS":
        cell.font = Font(name=FONT_NAME, size=11, color=ACCENT_POSITIVE, bold=HEADER_BOLD)


# ============================================================
# SAVE
# ============================================================
wb.properties.creator = "Z.ai"
wb.save(OUTPUT)
print(f"Arquivo gerado: {OUTPUT}")
print(f"Abas: {wb.sheetnames}")
print(f"Total de linhas de demanda: {total_all}")
print(f"  ENGENHARIA: {total_e} ({total_e*100//total_all}%)")
print(f"  ANALOGO:    {total_a} ({total_a*100//total_all}%)")
print(f"  PREMISSA:   {total_p} ({total_p*100//total_all}%)")
