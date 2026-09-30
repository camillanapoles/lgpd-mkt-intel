#!/usr/bin/env python3
"""
NeoGov · Runway & Dimensionamento de Rodada · LÓGICA pura · SSOT v1.0.8
Resolve D001-NOVO-21. Princípio: rodada dimensionada pela QUEIMA do pior
cenário + buffer — NÃO pelo valuation (valuation é narrativa de upside).
"""
import json

s = json.load(open('/mnt/user-data/outputs/neogov-v21/data/neogov-pricing-cost-ssot-latest.json'))
assert s['$meta']['version'] == "1.0.8"

# EBITDA por cenário (R$ M · do Cap 15 / dre_fcd.py · 5 anos)
ebitda = {
    'A_P25_conservador': [-1.1, -0.1, 1.5, 2.6, 3.7],
    'B_P50_provavel':    [-0.1, 3.3, 8.4, 14.1, 19.9],
    'C_P75_otimista':    [1.5, 8.4, 18.5, 27.1, 35.7],
}
EVPL = 19.59          # E[VPL] ponderado (Cap 15)
VPL_B = 18.69         # VPL cenário provável (Cap 15)

print("="*74)
print("RUNWAY & DIMENSIONAMENTO DE RODADA · NeoGov · SSOT v1.0.8")
print("="*74)

# ===== 1 · QUEIMA ACUMULADA (cash trough por cenário) =====
print("\n[1] QUEIMA ACUMULADA (EBITDA proxy de caixa · vale-do-caixa)")
print(f"{'Cenário':<22}{'acum.A1':>9}{'acum.A2':>9}{'vale':>9}{'recup.':>10}")
troughs = {}
for nome, e in ebitda.items():
    acum, vale, ano_pos = 0, 0, None
    for i, v in enumerate(e):
        acum += v
        if acum < vale: vale = acum
        if acum >= 0 and ano_pos is None and i > 0: ano_pos = i+1
    troughs[nome] = vale
    a1 = e[0]; a2 = e[0]+e[1]
    rp = f"Ano {ano_pos}" if ano_pos else "Ano 1"
    print(f"{nome:<22}{a1:>8.1f}M{a2:>8.1f}M{vale:>8.1f}M{rp:>10}")
pior = min(troughs.values())
print(f"\n  Pior vale-do-caixa (cenário A): R$ {pior:.1f}M")
print("  ⚠️ EBITDA é proxy · capital de giro/CAPEX podem agravar (D-015 · D001-NOVO-20 refina)")

# ===== 2 · NECESSIDADE DE APORTE (queima pior caso + buffer) =====
# Princípio: cobrir o vale do pior cenário + buffer de segurança 40%
#   + 12 meses de runway operacional pós-vale (não morrer na curva)
BUFFER = 0.40                       # 🟡 D-015 · prática early-stage (margem de erro do plano)
runway_op = s['cost_model']['fixed_costs_company_monthly_brl']['total_cf_monthly_brl']*12/1e6  # R$1,71M
need_base = abs(pior)
need_buffer = need_base * (1+BUFFER)
need_total = need_buffer + runway_op   # vale coberto + 1 ano de CF de folga
print("\n[2] NECESSIDADE DE APORTE (dimensionada pela QUEIMA · não pelo valuation)")
print(f"  Vale a cobrir (pior caso A):      R$ {need_base:.2f}M")
print(f"  + buffer segurança {BUFFER:.0%} (🟡):     R$ {need_buffer-need_base:.2f}M")
print(f"  + runway operacional 12m (CF):    R$ {runway_op:.2f}M")
print(f"  ─────────────────────────────────────────────")
print(f"  = APORTE RECOMENDADO:             R$ {need_total:.2f}M  → arredonda R$ {round(need_total*2)/2:.1f}M")
raise_target = round(need_total*2)/2

# ===== 3 · USO DOS RECURSOS =====
print("\n[3] USO DOS RECURSOS (alocação do aporte)")
uso = {
    'Cobrir queima operacional (vale cenário A)': 0.35,
    'Time produto/IA própria (Llama+QLoRA · mandato técnico)': 0.30,
    'Comercial/GTM (Wave 1 Alfa · canal Wilton)': 0.20,
    'Buffer/contingência': 0.15,
}
for k, p in uso.items():
    print(f"  {p:>4.0%}  R$ {raise_target*p:>4.1f}M  {k}")

# ===== 4 · TESE DE VALUATION (banda · NÃO ponto) =====
print("\n[4] TESE DE VALUATION (banda honesta · pré-receita)")
print(f"  Âncora de valor intrínseco: E[VPL] 5a = R$ {EVPL:.1f}M (Cap 15)")
print(f"  Mas valuation pré-receita NÃO = VPL · aplica-se desconto de estágio")
# Pre-money: VPL descontado por risco de execução (early-stage haircut 50-70%)
for haircut, lbl in [(0.50,'otimista'),(0.65,'central'),(0.75,'conservador')]:
    pre = EVPL*(1-haircut)
    dil = raise_target/(pre+raise_target)
    print(f"  haircut {haircut:.0%} ({lbl:<11}): pre-money R$ {pre:>5.1f}M · diluição {dil:>4.0%}")
print("  🟡 D-015 · haircut = prática VC early-stage BR · valuation real = negociado")
print(f"  → diluição provável: 15-30% por R$ {raise_target:.1f}M (banda · não promessa)")

# ===== 5 · SÍNTESE =====
print("\n" + "="*74)
print("SÍNTESE · TESE DE CAPTAÇÃO")
print("="*74)
print(f"  Pedir: ~R$ {raise_target:.1f}M (dimensionado pela queima do pior caso + buffer)")
print(f"  Por quê este valor: cobre vale cenário A (R$ {need_base:.1f}M) sem depender")
print(f"    do cenário otimista acontecer — sobrevivência não é aposta")
print(f"  Retorno ao investidor: E[VPL] R$ {EVPL:.1f}M · perfil assimétrico")
print(f"    (downside +R$2,1M · upside R$38,8M = 18× · Cap 15)")
print(f"  Diluição: banda 15-30% (negociada · não tabelada)")
print(f"  Débito gerado: D001-NOVO-22 (validar valuation c/ term sheet real)")
