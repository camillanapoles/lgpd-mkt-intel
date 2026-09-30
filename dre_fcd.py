#!/usr/bin/env python3
"""
NeoGov · DRE + FCD · 3 cenários · LÓGICA pura rastreável ao SSOT v1.0.7
Sub-estratifica Classe III (absorve débito D17).
Toda estimativa marcada. Nada fabricado.
"""
import json

s = json.load(open('/mnt/user-data/outputs/neogov-v21/data/neogov-pricing-cost-ssot-latest.json'))
assert s['$meta']['version'] == "1.0.7"

CF_m = s['cost_model']['fixed_costs_company_monthly_brl']['total_cf_monthly_brl']
CF_y = CF_m * 12
sc = s['scenarios']

print("="*78)
print("DRE + FCD · NeoGov · LÓGICA pura · SSOT v1.0.7")
print("="*78)
print(f"\nCF anual fixo: R$ {CF_y:,.0f}  (= CF mensal R$ {CF_m:,} × 12)")

# ===== PREMISSA · taxa de desconto FCD =====
# 🟡 ESTIMATIVA-ANÁLOGO (D-015): early-stage BR SaaS · SELIC base + prêmio risco equity
# Lastro: prática VC BR early-stage 20-30% nominal · usar 25% (meio do range)
# D001-NOVO-20 (NOVO): calibrar WACC com captação real / SELIC vigente
DISCOUNT = 0.25
print(f"\nTaxa de desconto FCD: {DISCOUNT:.0%}  🟡 D-015 (early-stage BR · SELIC+prêmio · D001-NOVO-20 calibra)")

# ===== DRE PROJETADO · 3 cenários · horizonte 5 anos =====
# Margem de contribuição média ponderada (da curva v2: receita - CSC variável)
# Da curva: N=163 → ARR R$12.06M · lucro R$5.92M/ano → margem op 49%
# margem contribuição (antes CF) ≈ receita × 0.72 (média ponderada mix · curva v2)
MARGEM_CONTRIB = 0.72  # 🟡 D-015 · derivado curva v2 (ABC · D001-NOVO-8 calibra)

cenarios = {
    'A_P25_conservador': {'prob': 0.25, 'arr': [0.9e6, 2.2e6, 4.5e6, 6.0e6, 7.5e6]},
    'B_P50_provavel':    {'prob': 0.50, 'arr': [2.3e6, 7.0e6, 14.0e6, 22.0e6, 30.0e6]},
    'C_P75_otimista':    {'prob': 0.25, 'arr': [4.5e6, 14.0e6, 28.0e6, 40.0e6, 52.0e6]},
}
# ARR trajetória: 🟡 D-015 ancorado em ssot.scenarios (M12/M36) · interpolado anos 1-5

print("\n" + "─"*78)
print("DRE PROJETADO (R$ · 5 anos · margem contrib 72% 🟡 · CF R$1,71M/ano)")
print("─"*78)
print(f"{'Cenário':<22}{'Ano1':>11}{'Ano2':>11}{'Ano3':>11}{'Ano4':>11}{'Ano5':>11}")
for nome, c in cenarios.items():
    linha_receita = c['arr']
    linha_ebitda = [r*MARGEM_CONTRIB - CF_y for r in linha_receita]
    print(f"{nome:<22}" + "".join(f"{r/1e6:>10.1f}M" for r in linha_receita))
    print(f"{'  → EBITDA':<22}" + "".join(f"{e/1e6:>10.1f}M" for e in linha_ebitda))
    c['ebitda'] = linha_ebitda

# ===== FCD · valor presente · 3 cenários =====
print("\n" + "─"*78)
print(f"FCD · Valor Presente Líquido (desconto {DISCOUNT:.0%} 🟡)")
print("─"*78)
vpl_ponderado = 0
for nome, c in cenarios.items():
    vpl = sum(e / (1+DISCOUNT)**(i+1) for i, e in enumerate(c['ebitda']))
    c['vpl'] = vpl
    contrib = vpl * c['prob']
    vpl_ponderado += contrib
    print(f"  {nome:<22} VPL 5a = R$ {vpl/1e6:>7.2f}M  × prob {c['prob']} = R$ {contrib/1e6:>6.2f}M")
print(f"\n  🎯 VPL ESPERADO PONDERADO (E[VPL]) = R$ {vpl_ponderado/1e6:.2f}M")

# ===== SUB-ESTRATIFICAÇÃO CLASSE III (absorve D17) =====
print("\n" + "─"*78)
print("SUB-ESTRATIFICAÇÃO CLASSE III (resolve D17 · range R$1M-143M absurdo)")
print("─"*78)
# Base FATO: Classe III = arrecadação >R$500k/semestre (>R$1M/ano)
# Sub-faixas 🟡 D-015 (análogo distribuição log · D001-NOVO-17 calibra c/ dado real)
classe3_sub = {
    'III-A (R$1-3M/ano arrecad.)':  {'preco': 5000,  'csc': 1217, 'pct_de_III': 0.55},
    'III-B (R$3-10M/ano arrecad.)': {'preco': 15000, 'csc': 6677, 'pct_de_III': 0.35},
    'III-C (>R$10M/ano · custom)':  {'preco': 30000, 'csc': 18727,'pct_de_III': 0.10},
}
print(f"{'Sub-faixa':<32}{'preço/mês':>11}{'CSC':>9}{'margem':>9}{'% de III':>10}")
for k, v in classe3_sub.items():
    m = (v['preco']-v['csc'])/v['preco']*100
    print(f"{k:<32}{v['preco']:>10,}{v['csc']:>9,}{m:>8.0f}%{v['pct_de_III']*100:>9.0f}%")
print("  🟡 D-015 · sub-faixas análogas · D001-NOVO-17 calibra c/ arrecadação real (sigilosa)")
print("  → substitui o tier único cartorio_classe3 R$9.000 provisório (Apêndice N)")

# ===== PONTO DE EQUILÍBRIO CONSOLIDADO =====
print("\n" + "─"*78)
print("SÍNTESE FINANCEIRA")
print("─"*78)
print(f"  Break-even operacional: 37 clientes (curva v2 · Wave1 mix)")
print(f"  Sucesso global: 163 clientes · ARR R$12M · margem op 49%")
print(f"  E[VPL] 5 anos ponderado: R$ {vpl_ponderado/1e6:.2f}M")
print(f"  Cenário B (P50 · provável): VPL R$ {cenarios['B_P50_provavel']['vpl']/1e6:.2f}M")
print(f"  Uplift cartório Wave3-5: +R$312k/mês (curva v2 · 🟡 2% TAM)")
