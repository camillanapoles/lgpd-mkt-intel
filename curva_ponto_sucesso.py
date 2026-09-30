#!/usr/bin/env python3
"""
NeoGov · Curva Ponto de Sucesso (Lucro) · por Cliente + Global
Fonte única: data/neogov-pricing-cost-ssot-latest.json (price.validated do DT TEST)
Object-oriented: tudo navegável por ssot[...] path
Saída: gráficos PNG + tabela break-even
"""
import json
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

SSOT_PATH = '/mnt/user-data/outputs/neogov-v21/data/neogov-pricing-cost-ssot-latest.json'
OUT_DIR = '/mnt/user-data/outputs/neogov-v21/data'

with open(SSOT_PATH) as f:
    ssot = json.load(f)

tiers = ssot['pricing_tiers']
CF = ssot['cost_model']['fixed_costs_company_monthly_brl']['total_cf_monthly_brl']  # 142.251
L1A = ssot['cost_model']['layer_1a_platform_shared_customer_serving']['total_monthly_brl']  # 10.988
mix = ssot['mix_wave1_p75']

# ============================================================
# FUNÇÃO 1 · LUCRO POR CLIENTE (unit economics por tier)
#   profit_per_client(tier) = price.validated - cost.csc_total
# ============================================================
def profit_per_client(tier_key):
    t = tiers[tier_key]
    price = t['price']['validated']
    csc = t['cost']['csc_total']
    return price - csc, price, csc

# ============================================================
# FUNÇÃO 2 · BREAK-EVEN POR CLUSTER ISOLADO
#   N_be(tier) = CF / margem_unitaria(tier)
# ============================================================
def break_even_isolated(tier_key):
    margin, _, _ = profit_per_client(tier_key)
    if margin <= 0:
        return float('inf')
    return math.ceil(CF / margin)

# ============================================================
# FUNÇÃO 3 · PONTO DE SUCESSO GLOBAL (mix · N clientes escalado)
#   profit_global(N, mix) = Σ(N_c · (price_c - csc_c)) - CF
#   Escala o mix Wave1 P75 proporcionalmente
# ============================================================
mix_tiers = {k: v for k, v in mix.items()
             if k in tiers and isinstance(v, (int, float)) and not k.startswith('_')}
mix_total = sum(mix_tiers.values())  # 31

def profit_global(N):
    """Lucro global para N clientes mantendo proporção do mix Wave1 P75"""
    scale = N / mix_total
    revenue = 0.0
    csc_var = 0.0
    for tk, qty in mix_tiers.items():
        n_c = qty * scale
        price = tiers[tk]['price']['validated']
        csc = tiers[tk]['cost']['csc_total']
        revenue += n_c * price
        csc_var += n_c * csc
    profit = revenue - csc_var - CF
    return profit, revenue, csc_var

def break_even_global():
    """N onde profit_global = 0 (busca incremental)"""
    for N in range(1, 2000):
        p, _, _ = profit_global(N)
        if p >= 0:
            return N
    return None

# ============================================================
# RELATÓRIO TEXTUAL
# ============================================================
print("=" * 78)
print("NEOGOV · CURVA PONTO DE SUCESSO (LUCRO) · price.validated DT TEST")
print("=" * 78)
print(f"\nCF (custo fixo mensal empresa): R$ {CF:,.0f}")
print(f"L1A (platform shared rateável): R$ {L1A:,.0f}")
print(f"Mix Wave1 P75 referência: {mix_total} clientes\n")

print("─" * 78)
print("FUNÇÃO 1+2 · LUCRO POR CLIENTE & BREAK-EVEN ISOLADO POR CLUSTER")
print("─" * 78)
print(f"{'tier (ssot path)':<24}{'price':>9}{'csc':>9}{'lucro/cli':>11}{'N break-even':>14}")
rows = []
for tk in tiers:
    if tk.startswith('_'):
        continue
    margin, price, csc = profit_per_client(tk)
    nbe = break_even_isolated(tk)
    nbe_s = '∞' if nbe == float('inf') else str(nbe)
    print(f"{tk:<24}{price:>9,.0f}{csc:>9,.0f}{margin:>11,.0f}{nbe_s:>14}")
    rows.append((tk, price, csc, margin, nbe))

print("\n" + "─" * 78)
print("FUNÇÃO 3 · PONTO DE SUCESSO GLOBAL (mix Wave1 P75 escalado)")
print("─" * 78)
nbe_global = break_even_global()
print(f"\n  N break-even GLOBAL (mix Wave1 P75): {nbe_global} clientes")
for N in [12, 25, 31, 50, 90, 220, 600]:
    p, r, c = profit_global(N)
    status = "✅ LUCRO" if p >= 0 else "🔴 burn "
    arr = (r) * 12
    print(f"  N={N:>4} clientes → receita R$ {r:>11,.0f}/mês · lucro R$ {p:>12,.0f}/mês {status} · ARR R$ {arr:>13,.0f}")

# Ponto de sucesso global (4 condições · ARR >= 12M)
print("\n  PONTO DE SUCESSO GLOBAL (ARR >= R$ 12M · condição primária):")
for N in range(1, 2000):
    p, r, c = profit_global(N)
    if r * 12 >= 12_000_000:
        margin_op = p / r if r > 0 else 0
        print(f"    N = {N} clientes → ARR R$ {r*12:,.0f} · margem op {margin_op*100:.0f}% "
              f"{'✅ atinge sucesso' if margin_op >= 0.25 else '🟡 ARR ok · margem<25%'}")
        break

# ============================================================
# GRÁFICO 1 · LUCRO POR CLIENTE (barh por tier)
# ============================================================
fig, ax = plt.subplots(figsize=(11, 7))
rows_sorted = sorted([r for r in rows], key=lambda x: x[3])
labels = [r[0].replace('_', ' ') for r in rows_sorted]
margins = [r[3] for r in rows_sorted]
colors = ['#d64545' if m < 0 else '#3a8a3a' if m > 5000 else '#d4a017' for m in margins]
bars = ax.barh(labels, margins, color=colors, edgecolor='#222', linewidth=0.5)
ax.axvline(0, color='#222', linewidth=1)
ax.set_xlabel('Lucro por cliente / mês (R$) — price.validated DT TEST', fontsize=11)
ax.set_title('NeoGov · Lucro Unitário por Cluster·Tier (Apêndice K validado)',
             fontsize=13, fontweight='bold')
ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'R$ {x:,.0f}'))
for b, m in zip(bars, margins):
    ax.text(m + (800 if m >= 0 else -800), b.get_y() + b.get_height()/2,
            f'R$ {m:,.0f}', va='center', ha='left' if m >= 0 else 'right', fontsize=8)
ax.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.savefig(f'{OUT_DIR}/curva-lucro-por-cliente.png', dpi=130, bbox_inches='tight')
plt.close()

# ============================================================
# GRÁFICO 2 · CURVA PONTO DE SUCESSO GLOBAL (lucro vs N clientes)
# ============================================================
fig, ax = plt.subplots(figsize=(11, 7))
N_range = list(range(1, 250))
profits = [profit_global(N)[0] for N in N_range]
revenues = [profit_global(N)[1] for N in N_range]

ax.plot(N_range, profits, color='#2c5f8a', linewidth=2.5, label='Lucro global / mês')
ax.fill_between(N_range, profits, 0, where=[p >= 0 for p in profits],
                color='#3a8a3a', alpha=0.15, label='Zona de lucro')
ax.fill_between(N_range, profits, 0, where=[p < 0 for p in profits],
                color='#d64545', alpha=0.15, label='Zona de burn')
ax.axhline(0, color='#222', linewidth=1)
ax.axvline(nbe_global, color='#d4a017', linestyle='--', linewidth=2,
           label=f'Break-even global · N={nbe_global}')

# marcar waves
for N, lbl in [(31, 'Wave1 P75'), (90, 'Wave2'), (220, 'Wave3')]:
    if N <= 250:
        ax.axvline(N, color='#888', linestyle=':', alpha=0.6)
        ax.text(N, ax.get_ylim()[1]*0.92, lbl, rotation=90,
                fontsize=8, ha='right', color='#555')

ax.set_xlabel('Número de clientes (mix Wave1 P75 escalado)', fontsize=11)
ax.set_ylabel('Lucro global / mês (R$)', fontsize=11)
ax.set_title('NeoGov · Curva Ponto de Sucesso Global · price.validated (DT TEST)',
             fontsize=13, fontweight='bold')
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda y, _: f'R$ {y/1000:,.0f}k'))
ax.legend(loc='lower right', fontsize=9)
ax.grid(alpha=0.3)
plt.tight_layout()
plt.savefig(f'{OUT_DIR}/curva-ponto-sucesso-global.png', dpi=130, bbox_inches='tight')
plt.close()

print(f"\n✅ Gráficos gerados:")
print(f"   {OUT_DIR}/curva-lucro-por-cliente.png")
print(f"   {OUT_DIR}/curva-ponto-sucesso-global.png")
