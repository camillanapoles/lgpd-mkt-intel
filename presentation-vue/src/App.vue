<template>
  <div class="min-h-screen bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900">
    <nav class="bg-slate-950/50 backdrop-blur border-b border-slate-700 sticky top-0 z-50">
      <div class="max-w-7xl mx-auto px-4 py-3">
        <div class="flex items-center justify-between mb-2">
          <h1 class="text-lg font-bold text-white">LGPD Strategic Dashboard</h1>
          <span v-if="data" class="text-caption text-slate-400">
            Prontidao: <span class="font-bold" :class="sntiScoreClass">{{ sntiGlobalScore }}</span>/100
            <span class="text-slate-500 mx-1">|</span>
            Confianca: <span class="font-bold" :class="overallConfidenceClass">{{ (data.validation?.confidence_badges?.overall * 100).toFixed(0) }}%</span>
          </span>
        </div>
        <div class="flex gap-2 overflow-x-auto pb-1">
          <button v-for="tab in tabs" :key="tab.id"
                  @click="activeTab = tab.id"
                  :class="[
                    'px-3 py-1.5 rounded-lg text-caption whitespace-nowrap transition-all',
                    activeTab === tab.id ? 'bg-accent-600 text-white' : 'text-slate-300 hover:bg-slate-700',
                  ]">
            {{ tab.label }}
          </button>
        </div>
      </div>
    </nav>

    <main class="max-w-7xl mx-auto px-4 py-8">
      <div v-if="!data" class="text-center py-20">
        <p class="text-body-lg text-slate-400">Carregando dados...</p>
      </div>

      <template v-else>
        <Dashboard5s
          v-if="activeTab === 'dashboard'"
          :kpi-data="data.kpi_5s"
          :validation="data.validation"
          :priorities="data.priorities"
          :dashboard="data.dashboard"
        />

        <SwotAnalysis
          v-else-if="activeTab === 'swot'"
          :swot="data.swot_interactive"
          :confidence="data.validation?.confidence_badges?.swot || 0.82"
        />

        <BmcInteractive v-else-if="activeTab === 'bmc'" :bmc="data.bmc_interactive" />

        <ScenarioSimulator
          v-else-if="activeTab === 'scenarios'"
          :scenarios="data.scenarios"
          @scenario-change="sliderState = $event"
        />

        <RoadmapViewer
          v-else-if="activeTab === 'roadmap'"
          :roadmap="data.roadmap"
        />

        <MacroAnalysis
          v-else-if="activeTab === 'macro'"
          :pestle="data.pestle_analysis"
          :porter="data.porter_five_forces"
          :scorecard="data.market_attractiveness_scorecard"
        />

        <CompetitiveView
          v-else-if="activeTab === 'competitive'"
          :competitive="data.competitive"
        />

        <StakeholderMap
          v-else-if="activeTab === 'stakeholders'"
          :stakeholders="data.stakeholders"
        />

        <FdcuInteractive
          v-else-if="activeTab === 'fdcu'"
          :priorities="data.priorities"
          :validation="data.validation"
        />

        <ArtOfWar
          v-else-if="activeTab === 'snti'"
          :snti="data.snti"
          :scenario-overrides="sntiOverrides"
        />
      </template>
    </main>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import Dashboard5s from './components/strategic/Dashboard5s.vue'
import SwotAnalysis from './components/strategic/SwotAnalysis.vue'
import BmcInteractive from './components/BmcInteractive.vue'
import ScenarioSimulator from './components/strategic/ScenarioSimulator.vue'
import RoadmapViewer from './components/strategic/RoadmapViewer.vue'
import MacroAnalysis from './components/strategic/MacroAnalysis.vue'
import CompetitiveView from './components/strategic/CompetitiveView.vue'
import StakeholderMap from './components/strategic/StakeholderMap.vue'
import FdcuInteractive from './components/strategic/FdcuInteractive.vue'
import ArtOfWar from './components/strategic/ArtOfWar.vue'

const activeTab = ref('dashboard')
const data = ref(null)
const sliderState = ref({})

const tabs = [
  { id: 'dashboard', label: 'Dashboard' },
  { id: 'swot', label: 'SWOT' },
  { id: 'bmc', label: 'BMC' },
  { id: 'scenarios', label: 'Cenarios' },
  { id: 'roadmap', label: 'Roadmap' },
  { id: 'macro', label: 'PESTLE/Porter' },
  { id: 'competitive', label: 'Competitivo' },
  { id: 'stakeholders', label: 'Stakeholders' },
  { id: 'fdcu', label: 'FDC-U' },
  { id: 'snti', label: '⚔ Arte da Guerra' },
]

const overallConfidenceClass = computed(() => {
  const v = data.value?.validation?.confidence_badges?.overall || 0
  if (v >= 0.8) return 'text-green-400'
  if (v >= 0.6) return 'text-yellow-400'
  return 'text-red-400'
})

const computeOverrides = (snti, sliders) => {
  const mapping = snti?.slider_overrides || {}
  const overrides = {}
  for (const [sliderId, config] of Object.entries(mapping)) {
    const val = sliders[sliderId]
    let active = false
    if (config.condition === 'true') active = val === true
    else if (config.condition.startsWith('>=')) active = Number(val) >= Number(config.condition.slice(2))
    else active = val === config.condition

    if (!active) continue
    for (const rule of config.applies_to) {
      overrides[`${rule.dim}:${rule.item_id}`] = {
        vvv: rule.vvv_override,
        fator: rule.fator_override,
        polaridade: rule.polaridade_override,
        description: rule.description_override,
      }
    }
  }
  return overrides
}

const sntiOverrides = computed(() => {
  const snti = data.value?.snti
  if (!snti) return {}
  return computeOverrides(snti, sliderState.value)
})

const sntiGlobalScore = computed(() => {
  const snti = data.value?.snti
  if (!snti) return '?'
  const overrides = sntiOverrides.value
  let score = 0
  for (const [key, dim] of Object.entries(snti.dimensions || {})) {
    const items = (dim.items || []).map(item => {
      const o = overrides[`${key}:${item.id}`]
      if (!o) return item
      return { ...item, vvv: o.vvv ?? item.vvv, fator: o.fator ?? item.fator, polaridade: o.polaridade ?? item.polaridade }
    })
    const totalPos = items.filter(i => i.polaridade === 1).reduce((s, i) => s + i.vvv * i.fator, 0)
    const totalNeg = items.filter(i => i.polaridade === -1).reduce((s, i) => s + i.vvv * i.fator, 0)
    const maxPos = items.filter(i => i.polaridade === 1).reduce((s, i) => s + i.fator, 0)
    const dimScore = maxPos > 0 ? ((totalPos - totalNeg) / maxPos) * 100 : 0
    score += dimScore * (dim.weight || 0.2)
  }
  return score.toFixed(1)
})

const sntiScoreClass = computed(() => {
  const s = parseFloat(sntiGlobalScore.value)
  if (isNaN(s)) return 'text-slate-400'
  if (s >= 75) return 'text-green-400'
  if (s >= 60) return 'text-yellow-400'
  if (s >= 40) return 'text-orange-400'
  return 'text-red-400'
})

onMounted(async () => {
  const base = import.meta.env.BASE_URL
  const response = await fetch(`${base}strategic-data-unified.json`)
  data.value = await response.json()
  const sliders = data.value?.scenarios?.sliders || []
  const initial = {}
  sliders.forEach(s => { initial[s.id] = s.value })
  sliderState.value = initial
})
</script>
