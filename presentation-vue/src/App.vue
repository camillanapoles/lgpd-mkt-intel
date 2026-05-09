<template>
  <div class="min-h-screen bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900">
    <nav class="bg-slate-950/50 backdrop-blur border-b border-slate-700 sticky top-0 z-50">
      <div class="max-w-7xl mx-auto px-4 py-4 flex items-center justify-between">
        <h1 class="text-xl font-bold text-white">LGPD Strategic Dashboard</h1>
        <div class="flex gap-4">
          <button v-for="tab in tabs" :key="tab.id"
                  @click="activeTab = tab.id"
                  :class="activeTab === tab.id ? 'bg-blue-600 text-white' : 'text-slate-300 hover:bg-slate-700'"
                  class="px-4 py-2 rounded-lg transition-all">
            {{ tab.label }}
          </button>
        </div>
      </div>
    </nav>

    <main class="max-w-7xl mx-auto px-4 py-8">
      <Dashboard5s
        v-if="activeTab === 'dashboard'"
        :kpi-data="dashboardData"
        :validation="validationData"
        :priorities="prioritiesData"
        :dashboard="dashboardMeta"
      />

      <SwotAnalysis
        v-else-if="activeTab === 'swot'"
        :swot="swotData"
        :confidence="validationData?.confidence_badges?.swot || 0.82"
      />

      <BmcInteractive v-else-if="activeTab === 'bmc'" :bmc="bmcData" />

      <ScenarioSimulator
        v-else-if="activeTab === 'scenarios'"
        :scenarios="scenariosData"
      />

      <RoadmapViewer
        v-else-if="activeTab === 'roadmap'"
        :roadmap="roadmapData"
      />

      <FdcuInteractive
        v-else-if="activeTab === 'fdcu'"
        :priorities="prioritiesData"
        :validation="validationData"
      />
    </main>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import Dashboard5s from './components/strategic/Dashboard5s.vue'
import SwotAnalysis from './components/strategic/SwotAnalysis.vue'
import BmcInteractive from './components/BmcInteractive.vue'
import ScenarioSimulator from './components/strategic/ScenarioSimulator.vue'
import RoadmapViewer from './components/strategic/RoadmapViewer.vue'
import FdcuInteractive from './components/strategic/FdcuInteractive.vue'

const activeTab = ref('dashboard')

const tabs = [
  { id: 'dashboard', label: 'Dashboard 5s' },
  { id: 'swot', label: 'SWOT' },
  { id: 'bmc', label: 'BMC' },
  { id: 'scenarios', label: 'Cenários' },
  { id: 'roadmap', label: 'Roadmap' },
  { id: 'fdcu', label: 'FDC-U Editor' }
]

const dashboardData = ref(null)
const swotData = ref(null)
const bmcData = ref(null)
const scenariosData = ref(null)
const roadmapData = ref(null)
const validationData = ref(null)
const prioritiesData = ref(null)
const dashboardMeta = ref(null)

onMounted(async () => {
  const base = import.meta.env.BASE_URL
  const response = await fetch(`${base}strategic-data-unified.json`)
  const data = await response.json()
  dashboardData.value = data.kpi_5s
  swotData.value = data.swot_interactive
  bmcData.value = data.bmc_interactive
  scenariosData.value = data.scenarios
  roadmapData.value = data.roadmap
  validationData.value = data.validation
  prioritiesData.value = data.priorities
  dashboardMeta.value = data.dashboard
})
</script>
