<template>
  <div class="min-h-screen bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900">
    <nav class="bg-slate-950/50 backdrop-blur border-b border-slate-700 sticky top-0 z-50">
      <div class="max-w-7xl mx-auto px-4 py-3">
        <div class="flex items-center justify-between mb-2">
          <h1 class="text-lg font-bold text-white">
            {{ data?.company?.name || 'NeoGov' }} — Strategic Intel
          </h1>
          <div v-if="data" class="flex items-center gap-3 text-sm">
            <span class="text-slate-400">
              FDC-U Top:
              <span class="font-bold text-white">{{ topClusterName }}</span>
            </span>
            <span class="text-slate-500">|</span>
            <span class="text-slate-400">
              Gaps VVV=0:
              <span class="font-bold text-red-400">{{ criticalGapCount }}</span>
            </span>
          </div>
        </div>
        <div class="flex gap-2 overflow-x-auto pb-1">
          <button
            v-for="tab in tabs"
            :key="tab.id"
            @click="activeTab = tab.id"
            :class="[
              'px-3 py-1.5 rounded-lg text-xs whitespace-nowrap transition-all',
              activeTab === tab.id
                ? 'bg-blue-600 text-white'
                : 'text-slate-300 hover:bg-slate-700',
            ]"
          >
            {{ tab.label }}
          </button>
        </div>
      </div>
    </nav>

    <main class="max-w-7xl mx-auto px-4 py-8">
      <div v-if="!data" class="text-center py-20">
        <div class="inline-block w-8 h-8 border-2 border-blue-500 border-t-transparent rounded-full animate-spin mb-4"></div>
        <p class="text-slate-400">Carregando dados estrategicos...</p>
      </div>

      <div v-else-if="loadError" class="text-center py-20">
        <p class="text-red-400 mb-2">Erro ao carregar strategic-data-unified.json</p>
        <p class="text-slate-500 text-sm">{{ loadError }}</p>
      </div>

      <template v-else>
        <Dashboard5s
          v-if="activeTab === 'dashboard'"
          :clusters="data.clusters"
          :kpis="data.kpis"
          :risks="data.risks"
          :company="data.company"
          :sun_tzu_factors="data.sun_tzu_factors"
          :fdcu="data.fdc_u"
        />

        <FdcuInteractive
          v-else-if="activeTab === 'fdcu'"
          :fdcu="data.fdc_u"
          :clusters="data.clusters"
          @fdcu-weights-changed="fdcuWeights = $event"
        />

        <RoadmapViewer
          v-else-if="activeTab === 'roadmap'"
          :roadmap="data.roadmap"
          :clusters="data.clusters"
        />

        <SwotAnalysis
          v-else-if="activeTab === 'swot'"
          :diagnostic="data.diagnostic"
        />

        <ScenarioSimulator
          v-else-if="activeTab === 'scenarios'"
          :scenarios="data.scenarios"
          :clusters="data.clusters"
          @scenario-change="scenarioState = $event"
        />

        <StatusPage
          v-else-if="activeTab === 'status'"
          :vvv_gaps="data.vvv_gaps"
          :action_plan="data.action_plan"
        />

        <CompetitiveView
          v-else-if="activeTab === 'competitive'"
          :competitive="data.competitive"
        />
      </template>
    </main>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import Dashboard5s from './components/strategic/Dashboard5s.vue'
import FdcuInteractive from './components/strategic/FdcuInteractive.vue'
import RoadmapViewer from './components/strategic/RoadmapViewer.vue'
import SwotAnalysis from './components/strategic/SwotAnalysis.vue'
import ScenarioSimulator from './components/strategic/ScenarioSimulator.vue'
import StatusPage from './components/strategic/StatusPage.vue'
import CompetitiveView from './components/strategic/CompetitiveView.vue'

const activeTab = ref('dashboard')
const data = ref(null)
const loadError = ref(null)
const fdcuWeights = ref({})
const scenarioState = ref({})

const tabs = [
  { id: 'dashboard', label: 'Dashboard' },
  { id: 'fdcu', label: 'FDC-U' },
  { id: 'roadmap', label: 'Roadmap' },
  { id: 'swot', label: 'SWOT' },
  { id: 'scenarios', label: 'Cenarios' },
  { id: 'status', label: 'VVV Gaps' },
  { id: 'competitive', label: 'Competitivo' },
]

const topClusterName = computed(() => {
  return data.value?.fdc_u?.ranking_pure?.[0]?.cluster_name || '—'
})

const criticalGapCount = computed(() => {
  return (data.value?.vvv_gaps || []).filter(g => g.vvv_score === 0).length
})

onMounted(async () => {
  try {
    const base = import.meta.env.BASE_URL
    const response = await fetch(`${base}strategic-data-unified.json`)
    if (!response.ok) throw new Error(`HTTP ${response.status}`)
    data.value = await response.json()
  } catch (err) {
    loadError.value = err.message
  }
})
</script>
