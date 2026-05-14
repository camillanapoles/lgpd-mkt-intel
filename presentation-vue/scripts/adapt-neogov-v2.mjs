#!/usr/bin/env node
import { readFileSync, writeFileSync } from 'fs'
import { fileURLToPath } from 'url'
import { dirname, join } from 'path'

const __dirname = dirname(fileURLToPath(import.meta.url))
const ROOT = join(__dirname, '..')
const V2_SRC = join(ROOT, '..', '..', 'docs', 'NEOGOV-DATA-v2.json')
const OUT = join(ROOT, 'public', 'strategic-data-unified.json')

const PENDING = '[DADO PENDENTE]'

const v2 = JSON.parse(readFileSync(V2_SRC, 'utf8'))

const sortedByScore = [...v2.clusters]
  .filter(c => typeof (c.fdc_u_score ?? c.fdc_u_score_est) === 'number')
  .sort((a, b) => (b.fdc_u_score ?? b.fdc_u_score_est) - (a.fdc_u_score ?? a.fdc_u_score_est))

const rankingPure = sortedByScore.map((c, i) => ({
  rank: i + 1,
  cluster_id: c.id,
  cluster_name: c.name,
  score: c.fdc_u_score ?? c.fdc_u_score_est,
  badge: c.status === 'priority_critical' ? 'PRIORITY CRITICAL'
       : c.status === 'active_today' ? 'ATIVO HOJE'
       : c.status === 'conditional_poc' ? 'CONDICIONAL — Gate PoC'
       : c.status === 'declared_target' ? 'ALVO DECLARADO'
       : c.status === 'wave_3' ? 'WAVE 3'
       : PENDING
}))

const waveOrder = (v2.roadmap?.waves || []).flatMap(w => w.cluster_ids || [])

const spearheadId = rankingPure[0]?.cluster_id
const spearheadCluster = v2.clusters.find(c => c.id === spearheadId)
const parallelCluster = v2.clusters.find(c => c.wave === '2B' || c.wave === 2.1 || (c.id !== spearheadId && c.status === 'priority_critical'))

const clusters = v2.clusters.map(c => ({
  id: c.id,
  name: c.name,
  code: c.code || PENDING,
  emoji: { educacao_privada: '🎓', saude_privada: '🏥', setor_publico_municipal: '🏛️',
           setor_publico_estadual: '🏢', setor_publico_federal: '🇧🇷', entidades_associativas: '🤝' }[c.id] || '📌',
  description: c.lgpd_pain || PENDING,
  status: c.status || PENDING,
  wave: c.wave ?? PENDING,
  wave_start_month: c.wave_start_month ?? null,
  universe_size: c.universe ?? c.universe_icp ?? null,
  universe_unit: c.universe_unit || c.universe_detail || PENDING,
  universe_source: c.universe_source || PENDING,
  universe_vvv: c.vvv_universe ?? null,
  fdc_u_score: c.fdc_u_score ?? c.fdc_u_score_est ?? null,
  fdc_u_rank: rankingPure.find(r => r.cluster_id === c.id)?.rank ?? null,
  fdc_u_vvv: c.fdc_u_vvv ?? null,
  fdc_u_note: c.fdc_u_note || null,
  decisor: c.decisor || PENDING,
  sales_cycle_days: c.sales_cycle_days || (c.sales_cycle_months ? [c.sales_cycle_months[0]*30, c.sales_cycle_months[1]*30] : null),
  lgpd_pain: c.lgpd_pain || PENDING,
  key_regulation: c.key_regulation || c.key_data || null,
  competition: c.competition || c.competition_note || PENDING,
  products_core: c.products_core || [],
  pricing: c.pricing_est || { note: c.pricing_est_note || PENDING },
  margins: c.unit_economics?.gross_margin ? { gross_margin: c.unit_economics.gross_margin } : null,
  unit_economics: c.unit_economics || null,
  channel: c.channel || [PENDING],
  main_objection: c.main_objection || PENDING,
  objection_counter: c.objection_counter || PENDING,
  trigger: c.trigger || null,
  gate: c.gate || null,
  prerequisite: c.prerequisite || null,
  exclusive_b2g: c.exclusive_b2g || false,
  systems_by_segment: c.systems_by_segment || null,
  gap_note: c.gap || null
}))

const kpis = (v2.roadmap?.kpis || []).map(k => ({
  month: k.month,
  arr: k.arr_range || [null, null],
  active_clients: k.active_clients || [null, null],
  mrr: k.arr_range ? [Math.round(k.arr_range[0]/12), Math.round(k.arr_range[1]/12)] : [null, null]
}))

const fdcuDimensions = [
  { id: 'fdc_u_score', name: 'FDC-U Score', weight: 1.0, function: '+', vvv: PENDING, source: 'NEOGOV-BUSINESS-PLAN-FINAL-v2.0.md' }
]

const fdc_u = {
  dimensions: fdcuDimensions,
  scores: Object.fromEntries(v2.clusters.map(c => [c.id, { fdc_u_score: c.fdc_u_score ?? c.fdc_u_score_est ?? null }])),
  ranking_pure: rankingPure,
  ranking_strategic_bsc03: {
    note: `BSC-03 derivado de v2 roadmap.waves. Spearhead=${spearheadCluster?.name || PENDING}, Parallel=${parallelCluster?.name || PENDING}.`,
    wave_order: waveOrder,
    spearhead: spearheadId || PENDING,
    spearhead_name: spearheadCluster?.name || PENDING,
    parallel: parallelCluster?.id || PENDING,
    parallel_name: parallelCluster?.name || PENDING,
    rationale: spearheadCluster && parallelCluster
      ? `${spearheadCluster.name} = FDC-U rank #1 (${spearheadCluster.fdc_u_score}). ${parallelCluster.name} = paralela crítica (${parallelCluster.lgpd_pain || ''}).`
      : PENDING
  },
  depth_alerts: PENDING,
  sensitivity: PENDING
}

const sun_tzu_factors = {
  dao:   { name: 'Dao — Propósito Moral',  score: null, max: 10, description: PENDING + ' — não coberto por NEOGOV-DATA-v2' },
  tian:  { name: 'Tian — Timing/Céu',      score: null, max: 10, description: PENDING + ' — não coberto por NEOGOV-DATA-v2' },
  di:    { name: 'Di — Terreno',           score: null, max: 10, description: PENDING + ' — não coberto por NEOGOV-DATA-v2' },
  jiang: { name: 'Jiang — Comando',        score: null, max: 10, description: PENDING + ' — não coberto por NEOGOV-DATA-v2' },
  fa:    { name: 'Fa — Método/Disciplina', score: null, max: 10, description: PENDING + ' — não coberto por NEOGOV-DATA-v2' }
}

const diagnostic = {
  sun_tzu: { dao: null, tian: null, di: null, jiang: null, fa: null, total: null, interpretation: PENDING },
  swot: { forces: [PENDING], weaknesses: [PENDING], opportunities: [PENDING], threats: [PENDING] }
}

const scenarios = {
  active_scenario: 'realistic',
  pessimistic: { label: 'Pessimista', arr_m12: v2.roadmap?.waves?.[0]?.target_arr?.[0] ?? null,
                 active_clients_m12: 10, breakeven_month: 24 },
  realistic:   { label: 'Realista',   arr_m12: v2.roadmap?.kpis?.find(k => k.month === 12)?.arr_range?.[0] ?? null,
                 active_clients_m12: v2.roadmap?.kpis?.find(k => k.month === 12)?.active_clients?.[0] ?? null,
                 breakeven_month: 18 },
  optimistic:  { label: 'Otimista',   arr_m12: v2.roadmap?.kpis?.find(k => k.month === 12)?.arr_range?.[1] ?? null,
                 active_clients_m12: v2.roadmap?.kpis?.find(k => k.month === 12)?.active_clients?.[1] ?? null,
                 breakeven_month: 15 },
  sliders: [
    { id: 'edu_clients_m12', label: 'Escolas Educação Privada (M12)', min: 5, max: 50, value: 20, step: 1, cluster: 'educacao_privada', unit: 'escolas' },
    { id: 'saude_clients_m12', label: 'Hospitais Saúde Privada (M12)', min: 0, max: 15, value: 5, step: 1, cluster: 'saude_privada', unit: 'hospitais' },
    { id: 'gov_mun_clients_m12', label: 'Municípios B2G (M12)', min: 3, max: 30, value: 10, step: 1, cluster: 'setor_publico_municipal', unit: 'municípios' },
    { id: 'avg_ticket_edu', label: 'Ticket médio Educação (R$/ano)', min: 30000, max: 80000, value: 45000, step: 1000, cluster: 'educacao_privada', unit: 'BRL/ano' },
    { id: 'avg_ticket_saude', label: 'Ticket médio Saúde (R$/ano)', min: 100000, max: 300000, value: 180000, step: 5000, cluster: 'saude_privada', unit: 'BRL/ano' },
    { id: 'avg_ticket_gov', label: 'Ticket médio Município (R$/ano)', min: 15000, max: 50000, value: 25000, step: 1000, cluster: 'setor_publico_municipal', unit: 'BRL/ano' },
    { id: 'churn_rate', label: 'Churn anual (%)', min: 5, max: 30, value: 12, step: 1, cluster: 'all', unit: '%' },
    { id: 'cac_multiplier', label: 'CAC multiplier (vs estimado)', min: 0.5, max: 2.0, value: 1.0, step: 0.1, cluster: 'all', unit: 'x' }
  ]
}

const vvv_gaps = (v2.gaps_to_validate || []).map(g => ({
  id: g.id,
  description: g.description,
  vvv_score: g.vvv_current ?? null,
  classification: g.priority === 'CRÍTICO' ? 'CRÍTICO' : g.priority === 'ALTO' ? 'ROBUSTO' : (g.priority || PENDING),
  action_required: g.action || PENDING,
  responsible: g.responsible || null,
  deadline: g.deadline_month ? `M${g.deadline_month}` : (g.deadline_days ? `${g.deadline_days}d` : null)
}))

const action_plan = {
  days_30: (v2.action_plan_30_60_90?.days_30 || []).map(a => typeof a === 'string' ? a :
    `${a.action}${a.responsible ? ' — ' + a.responsible : ''}${a.critical ? ' [CRÍTICO]' : ''}${a.deadline_days ? ' (' + a.deadline_days + 'd)' : ''}`),
  days_60: (v2.action_plan_30_60_90?.days_60 || []).map(a => typeof a === 'string' ? a :
    `${a.action}${a.responsible ? ' — ' + a.responsible : ''}${a.critical ? ' [CRÍTICO]' : ''}`),
  days_90: (v2.action_plan_30_60_90?.days_90 || []).map(a => typeof a === 'string' ? a :
    `${a.action}${a.responsible ? ' — ' + a.responsible : ''}${a.critical ? ' [CRÍTICO]' : ''}`)
}

const competitive = {
  healthcare: (v2.competitive?.tier1_healthcare || []).map(c => ({
    name: c.name,
    focus: c.focus || PENDING,
    pricing: typeof c.pricing === 'object' ? c.pricing : { note: c.pricing || PENDING },
    pricing_vvv: c.pricing_vvv ?? null,
    pricing_source: c.pricing_source || PENDING,
    differentials: c.differentials || PENDING,
    threat_level: c.threat_level || PENDING
  })),
  education: [{ name: 'ZERO competitors detectados', focus: 'Educação Privada', pricing: { note: 'Oceano azul confirmado — INEP 42.491 escolas privadas sem SaaS LGPD dedicado' }, threat_level: 'OPORTUNIDADE' }],
  generalist: (v2.competitive?.tier2_generalist || []).map(c => ({
    name: c.name,
    pricing: c.pricing_entry ? { entry: c.pricing_entry, currency: c.currency, period: c.period } :
             (c.pricing_min_usd ? { min_usd: c.pricing_min_usd } : { model: c.model || PENDING }),
    pricing_vvv: c.pricing_vvv ?? null,
    positioning: c.positioning || PENDING
  })),
  education_note: 'F03 confirmado VVV 0.95 — 42.491 escolas privadas básicas sem SaaS LGPD dedicado (INEP 2024). Janela fecha com ECA Digital vigência mar/2026.',
  positioning_gap: v2.competitive?.gap_pricing || null
}

const roadmap = {
  waves: (v2.roadmap?.waves || []).map(w => ({
    id: w.id,
    name: w.name,
    start_month: w.start_month,
    end_month: w.end_month,
    cluster_ids: w.cluster_ids || [],
    cluster_names: (w.cluster_ids || []).map(cid => v2.clusters.find(c => c.id === cid)?.name || cid),
    investment_est: w.investment_est || null,
    target_arr: w.target_arr || null,
    gate: w.gate || null,
    urgency: w.urgency || null,
    prerequisite: w.prerequisite || null,
    key_action: w.key_action || null
  })),
  milestones: v2.roadmap?.milestones || [],
  kpis_per_month: v2.roadmap?.kpis || []
}

const risks = (v2.risks || []).map(r => ({
  id: r.id,
  description: r.description,
  probability: (r.probability || '').toLowerCase().replace('alta','high').replace('média','medium').replace('media','medium').replace('baixa','low'),
  impact: (r.impact || '').toLowerCase().replace('crítico','critical').replace('critico','critical').replace('alto','high').replace('médio','medium').replace('medio','medium'),
  mitigation: r.mitigation || PENDING,
  responsible: r.responsible || null,
  deadline_days: r.deadline_days || null
}))

const market_facts = v2.market_confirmed_facts || []
const products = v2.products || []

const integration_costs = {
  source: 'NEOGOV-DATA-v2 derived — pricing.setup from clusters',
  by_cluster: Object.fromEntries(v2.clusters.filter(c => c.pricing_est?.setup).map(c => [c.id, c.pricing_est.setup]))
}

const metadata = {
  version: v2.meta?.version || '2.0.0',
  source: v2.meta?.source || PENDING,
  generated_at: new Date().toISOString(),
  vvv_global: v2.meta?.vvv_global ?? null,
  notes: v2.meta?.notes || '',
  adapter: 'adapt-neogov-v2.mjs',
  pending_marker: PENDING,
  pending_fields: ['sun_tzu_factors.scores', 'diagnostic.swot.*', 'fdc_u.depth_alerts', 'fdc_u.sensitivity', 'fdc_u.dimensions (single dimension only — full multi-dim weights not in v2)']
}

const out = {
  metadata,
  company: v2.company,
  team: v2.team,
  products,
  clusters,
  kpis,
  fdc_u,
  sun_tzu_factors,
  diagnostic,
  scenarios,
  vvv_gaps,
  action_plan,
  competitive,
  roadmap,
  risks,
  market_confirmed_facts: market_facts,
  integration_costs
}

writeFileSync(OUT, JSON.stringify(out, null, 2), 'utf8')
console.log(`OK — wrote ${OUT}`)
console.log(`Clusters: ${clusters.length}`)
console.log(`Products: ${products.length}`)
console.log(`Risks: ${risks.length}`)
console.log(`KPIs (months): ${kpis.length}`)
console.log(`VVV gaps: ${vvv_gaps.length}`)
console.log(`Market facts: ${market_facts.length}`)
console.log(`FDC-U ranking entries: ${rankingPure.length}`)
console.log(`PENDING marker: "${PENDING}" used in sun_tzu_factors, diagnostic, fdc_u.depth_alerts/sensitivity`)
