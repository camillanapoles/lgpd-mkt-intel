#!/usr/bin/env python3
"""
NeoGov · Curva Ponto de Sucesso v2 · SSOT v1.0.7
MUDANÇA vs v1: lê v1.0.7 (5 segmentos) · cartórios tratados HONESTAMENTE
  - Wave 1 P75 mix = SEM cartórios (cartório é Wave 3-5 · NÃO inflar Wave 1)
  - Cenário separado "cartório-inclusive Wave 3-5" mostra uplift quando entram
RGO-9: não fabricar que cartório muda break-even Wave 1.
"""
import json, math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

SSOT_PATH = '/mnt/user-data/outputs/neogov-v21/data/neogov-pricing-cost-ssot-latest.json'
OUT = '/mnt/user-data/outputs/neogov-v21/data'

ssot = json.load(open(SSOT_PATH))
assert ssot['$meta']['version'] == "1.0.7", "SSOT versão inesperada"

tiers = ssot['pricing_tiers']
CF = ssot['cost_model']['fixed_costs_company_monthly_brl']['total_cf_monthly_brl']
mix = ssot['mix_wave1_p75']
mix_w1 = {k: v for k, v in mix.items()
          if k in tiers and isinstance(v, (int, float)) and not k.startswith('_')}
mix_w1_total = sum(mix_w1.values())  # 31 · SEM cartórios (correto · Wave 1)

def margin(tk):
    t = tiers[tk]
    return t['price']['validated'] - t['cost']['csc_total']

# ===== FUNÇÃO 1 · LUCRO POR CLIENTE (19 tiers · inclui cartórios) =====
def profit_per_client(tk): return margin(tk)
def break_even_iso(tk):
    m = margin(tk)
    return math.ceil(CF / m) if m > 0 else float('inf')

# ===== FUNÇÃO 2 · CURVA GLOBAL WAVE 1 (mix P75 · SEM cartórios · HONESTO) =====
def profit_w1(N):
    scale = N / mix_w1_total
    rev = sum(qty*scale*tiers[tk]['price']['validated'] for tk,qty in mix_w1.items())
    csc = sum(qty*scale*tiers[tk]['cost']['csc_total'] for tk,qty in mix_w1.items())
    return rev - csc - CF, rev

def be_w1():
    for N in range(1, 3000):
        if profit_w1(N)[0] >= 0: return N
    return None

# ===== FUNÇÃO 3 · UPLIFT CARTÓRIO Wave 3-5 (cenário separado · honesto) =====
# Penetração conservadora: 2% de 13.567 serventias FATO = ~270 cartórios Wave 3-5
# Distribuição por classe FATO: I 30,1% · II 26,5% · III 21,5% (resto sem arrec. típica)
# Aplicar proporção sobre os que adotam (assume mesma distribuição)
CART_TAM = 13567
CART_PENETRACAO = 0.02  # 🟡 ESTIMATIVA-ANÁLOGO (D-015 · análogo Gamma pós-ECA · D001-NOVO-7)
def cartorio_uplift():
    n_cart = round(CART_TAM * CART_PENETRACAO)  # ~271
    # distribuição entre os que adotam (normalizar 30.1/26.5/21.5)
    tot = 30.1 + 26.5 + 21.5
    dist = {'cartorio_classe1': 30.1/tot, 'cartorio_classe2': 26.5/tot, 'cartorio_classe3': 21.5/tot}
    rev = csc = 0
    detalhe = {}
    for tk, frac in dist.items():
        nc = round(n_cart * frac)
        r = nc * tiers[tk]['price']['validated']
        c = nc * tiers[tk]['cost']['csc_total']
        rev += r; csc += c
        detalhe[tk] = (nc, r, r-c)
    return n_cart, rev, rev-csc, detalhe

# ===== RELATÓRIO =====
print("="*80)
print("NEOGOV · CURVA PONTO DE SUCESSO v2 · SSOT v1.0.7 · cartório honesto")
print("="*80)
print(f"\nCF mensal: R$ {CF:,.0f} · Mix Wave1 P75: {mix_w1_total} clientes (SEM cartórios · correto)")

print("\n[F1] LUCRO/CLIENTE + BREAK-EVEN ISOLADO (19 tiers)")
print(f"{'tier':<22}{'preço':>8}{'csc':>8}{'lucro':>9}{'N b/e':>8}")
for tk in tiers:
    if tk.startswith('_'): continue
    p = tiers[tk]['price']['validated']; c = tiers[tk]['cost']['csc_total']
    nbe = break_even_iso(tk); nbe = '∞' if nbe==float('inf') else nbe
    tag = ' 🟡' if 'cartorio' in tk else ''
    print(f"{tk:<22}{p:>8,.0f}{c:>8,.0f}{margin(tk):>9,.0f}{str(nbe):>8}{tag}")

print("\n[F2] CURVA GLOBAL WAVE 1 (SEM cartórios · HONESTO · inalterado vs v1)")
be1 = be_w1()
print(f"  N break-even Wave1 = {be1} clientes (cartório NÃO altera Wave 1 · RGO-9)")
for N in [31, 50, 90, 163, 220, 600]:
    p, r = profit_w1(N)
    print(f"  N={N:>4} → lucro R$ {p:>11,.0f}/mês · ARR R$ {r*12:>13,.0f} {'✅' if p>=0 else '🔴'}")
# sucesso global ARR>=12M
for N in range(1, 3000):
    p, r = profit_w1(N)
    if r*12 >= 12_000_000:
        print(f"  🎯 SUCESSO GLOBAL: N={N} · ARR R$ {r*12:,.0f} · margem op {p/r*100:.0f}%")
        break

print("\n[F3] UPLIFT CARTÓRIO Wave 3-5 (cenário SEPARADO · 2% TAM = penetração 🟡 D-015)")
nc, crev, cprof, det = cartorio_uplift()
print(f"  Cartórios Wave 3-5: {nc} serventias (2% de {CART_TAM} FATO)")
for tk,(n,r,pr) in det.items():
    print(f"    {tk:<20} {n:>3} × R${tiers[tk]['price']['validated']:>5} = R$ {r:>9,.0f}/mês · lucro R$ {pr:>9,.0f}")
print(f"  TOTAL uplift cartório: +R$ {crev:,.0f}/mês receita · +R$ {cprof:,.0f}/mês lucro")
print(f"  → cartórios ACELERAM sucesso global em Wave 3-5 (mesma CF · infra guarda-chuva)")
print(f"  ⚠️ penetração 2% = ESTIMATIVA D-015 (D001-NOVO-7 piloto calibra · NÃO inflar)")

# ===== GRÁFICO v2 =====
fig, ax = plt.subplots(figsize=(11,7))
Nr = list(range(1,260))
pf = [profit_w1(N)[0] for N in Nr]
ax.plot(Nr, pf, color='#2c5f8a', lw=2.5, label='Lucro Wave1 (sem cartório · honesto)')
ax.fill_between(Nr, pf, 0, where=[x>=0 for x in pf], color='#3a8a3a', alpha=0.15)
ax.fill_between(Nr, pf, 0, where=[x<0 for x in pf], color='#d64545', alpha=0.15)
ax.axhline(0, color='#222', lw=1)
ax.axvline(be1, color='#d4a017', ls='--', lw=2, label=f'Break-even Wave1 · N={be1}')
# linha cartório-inclusive (uplift constante adicionado a partir de N alto = Wave 3-5)
pf_cart = [profit_w1(N)[0] + (cprof if N>=180 else 0) for N in Nr]
ax.plot(Nr, pf_cart, color='#7a4fa0', lw=1.8, ls=':', label=f'+ uplift cartório Wave3-5 (+R${cprof/1000:.0f}k)')
for N,l in [(31,'W1'),(90,'W2'),(220,'W3+cart')]:
    ax.axvline(N, color='#999', ls=':', alpha=.5)
    ax.text(N, ax.get_ylim()[1]*.93, l, rotation=90, fontsize=8, ha='right', color='#666')
ax.set_xlabel('Nº clientes (mix Wave1 P75 escalado)', fontsize=11)
ax.set_ylabel('Lucro global / mês (R$)', fontsize=11)
ax.set_title('NeoGov · Ponto de Sucesso v2 · SSOT v1.0.7 (cartório honesto Wave3-5)', fontsize=13, fontweight='bold')
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda y,_:f'R$ {y/1000:,.0f}k'))
ax.legend(loc='lower right', fontsize=9); ax.grid(alpha=.3)
plt.tight_layout()
plt.savefig(f'{OUT}/curva-ponto-sucesso-global-v2.png', dpi=130, bbox_inches='tight')
plt.close()
print(f"\n✅ Gráfico v2: {OUT}/curva-ponto-sucesso-global-v2.png")
