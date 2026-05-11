<template>
  <div class="space-y-6">
    <!-- Header -->
    <div class="flex items-center justify-between">
      <h2 class="text-2xl font-bold text-white">Simulador de Cenarios</h2>
      <div class="flex gap-2">
        <button
          @click="loadFromStorage"
          class="text-xs px-3 py-1.5 rounded bg-slate-700 text-slate-300 hover:bg-slate-600 transition-colors"
        >
          Carregar
        </button>
        <button
          @click="saveToStorage"
          class="text-xs px-3 py-1.5 rounded bg-blue-700 text-white hover:bg-blue-600 transition-colors"
        >
          Salvar
        </button>
        <button
          @click="exportJSON"
          class="text-xs px-3 py-1.5 rounded bg-green-700 text-white hover:bg-green-600 transition-colors"
        >
          Exportar JSON
        </button>
      </div>
    </div>

    <!-- Scenario Selector -->
    <div class="grid grid-cols-3 gap-4">
      <button
        v-for="sc in scenarioOptions"
        :key="sc.key"
        @click="activeScenario = sc.key"
        class="rounded-xl border-2 p-5 text-left transition-all"
        :class="activeScenario === sc.key ? sc.activeCls : sc.idleCls"
      >
        <div class="flex items-center justify-between mb-2">
          <h3 class="text-base font-bold text-white">{{ sc.label }}</h3>
          <span v-if="activeScenario === sc.key" class="text-xs px-2 py-0.5 rounded bg-white/20 text-white">
            Ativo
          </span>
        </div>
        <p class="text-xs text-slate-400">{{ sc.description }}</p>
      </button>
    </div>

    <!-- Active Scenario KPI Table -->
    <div v-if="activeScenarioData" class="bg-slate-800/50 border border-slate-700 rounded-xl p-6">
      <h3 class="text-base font-bold text-white mb-4">
        KPIs — Cenario <span :class="activeScenarioColor">{{ activeScenarioLabel }}</span>
      </h3>
      <div class="overflow-x-auto">
        <table class="w-full text-sm">
          <thead>
            <tr class="border-b border-slate-700">
              <th class="text-left text-slate-400 font-medium py-2 pr-6">Metrica</th>
              <th class="text-right text-slate-400 font-medium py-2 px-3">M12</th>
              <th class="text-right text-slate-400 font-medium py-2 px-3">M18</th>
              <th class="text-right text-slate-400 font-medium py-2 px-3">M24</th>
              <th class="text-right text-slate-400 font-medium py-2 px-3">M36</th>
            </tr>
          </thead>
          <tbody>
            <tr class="border-b border-slate-700/30">
              <td class="py-2 pr-6 text-slate-300">ARR</td>
              <td
                v-for="mo in ['m12','m18','m24','m36']"
                :key="mo"
                class="py-2 px-3 text-right font-mono text-green-400 font-bold"
              >
                {{ activeScenarioData.arr?.[mo] || activeScenarioData[`arr_${mo}`] || '—' }}
              </td>
            </tr>
            <tr class="border-b border-slate-700/30">
              <td class="py-2 pr-6 text-slate-300">Clientes</td>
              <td
                v-for="mo in ['m12','m18','m24','m36']"
                :key="mo"
                class="py-2 px-3 text-right text-white"
              >
                {{ activeScenarioData.clients?.[mo] || activeScenarioData[`clients_${mo}`] || '—' }}
              </td>
            </tr>
            <tr class="border-b border-slate-700/30">
              <td class="py-2 pr-6 text-slate-300">Breakeven</td>
              <td colspan="4" class="py-2 px-3 text-right text-yellow-400">
                {{ activeScenarioData.breakeven || '—' }}
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- ARR Preview (computed from sliders) -->
    <div class="bg-slate-800/50 border border-slate-700 rounded-xl p-5">
      <div class="flex items-center justify-between mb-2">
        <h3 class="text-sm font-bold text-white">ARR Preview (calculado)</h3>
        <span class="text-lg font-bold font-mono text-green-400">{{ computedARR }}</span>
      </div>
      <p class="text-xs text-slate-500">
        Clientes Saúde Privada × MRR × 12 + Escolas Educação Privada × MRR × 12
      </p>
    </div>

    <!-- Sliders -->
    <div class="grid md:grid-cols-2 gap-4">
      <div
        v-for="slider in scenarios?.sliders || []"
        :key="slider.id"
        class="bg-slate-800/50 border border-slate-700 rounded-xl p-4"
      >
        <div class="flex items-center justify-between mb-3">
          <label class="text-sm font-medium text-white">{{ slider.label }}</label>
          <span
            class="text-xs px-2 py-0.5 rounded"
            :class="slider.impact === 'high' ? 'bg-red-900/50 text-red-400' : 'bg-yellow-900/50 text-yellow-400'"
          >
            {{ slider.impact === 'high' ? 'Alto impacto' : 'Medio impacto' }}
          </span>
        </div>

        <!-- Boolean toggle -->
        <template v-if="slider.type === 'boolean'">
          <div class="flex items-center gap-3">
            <button
              @click="toggleBool(slider.id)"
              class="w-12 h-6 rounded-full relative transition-all duration-300"
              :class="sliderValues[slider.id] ? 'bg-green-500' : 'bg-slate-600'"
            >
              <span
                class="absolute top-0.5 w-5 h-5 rounded-full bg-white transition-all duration-300"
                :class="sliderValues[slider.id] ? 'left-6' : 'left-0.5'"
              />
            </button>
            <span class="text-sm text-slate-300">{{ sliderValues[slider.id] ? 'Sim' : 'Nao' }}</span>
          </div>
        </template>

        <!-- Select / options -->
        <template v-else-if="slider.options?.length">
          <select
            :value="sliderValues[slider.id]"
            @change="updateSlider(slider.id, $event.target.value)"
            class="w-full bg-slate-700 text-white rounded-lg px-3 py-2 text-sm border border-slate-600"
          >
            <option v-for="opt in slider.options" :key="opt" :value="opt">{{ opt }}</option>
          </select>
        </template>

        <!-- Range -->
        <template v-else>
          <div class="flex items-center gap-3">
            <input
              type="range"
              :min="slider.min"
              :max="slider.max"
              :step="slider.step || 1"
              :value="sliderValues[slider.id]"
              @input="updateSlider(slider.id, Number($event.target.value))"
              class="flex-1 h-2 bg-slate-700 rounded-lg appearance-none cursor-pointer accent-blue-500"
            />
            <span class="text-sm font-bold font-mono text-white w-20 text-right">
              {{ sliderValues[slider.id] }}
            </span>
          </div>
          <div class="flex justify-between text-xs text-slate-500 mt-1">
            <span>{{ slider.min }}</span>
            <span>{{ slider.max }}</span>
          </div>
        </template>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, computed, watch } from 'vue'

const props = defineProps({
  scenarios: { type: Object, default: null },
  clusters: { type: Array, default: () => [] },
})

const emit = defineEmits(['scenario-change'])

const activeScenario = ref(props.scenarios?.active_scenario || 'realistic')

// Initialize slider values from scenarios.sliders
const sliderValues = reactive({})
watch(() => props.scenarios?.sliders, (sliders) => {
  sliders?.forEach(s => {
    if (!(s.id in sliderValues)) sliderValues[s.id] = s.value
  })
}, { immediate: true })

const scenarioOptions = [
  {
    key: 'pessimistic',
    label: 'Pessimista',
    description: 'Churn alto, conversao baixa, sem advisor',
    activeCls: 'border-red-500 bg-red-950/30',
    idleCls: 'border-slate-700 bg-slate-800/50 hover:border-red-700/50',
  },
  {
    key: 'realistic',
    label: 'Realista',
    description: 'Premissas centrais validadas',
    activeCls: 'border-blue-500 bg-blue-950/30',
    idleCls: 'border-slate-700 bg-slate-800/50 hover:border-blue-700/50',
  },
  {
    key: 'optimistic',
    label: 'Otimista',
    description: 'Todas alavancas ativas (LOIs, advisor, funding)',
    activeCls: 'border-green-500 bg-green-950/30',
    idleCls: 'border-slate-700 bg-slate-800/50 hover:border-green-700/50',
  },
]

const activeScenarioData = computed(() => {
  if (!props.scenarios) return null
  return props.scenarios[activeScenario.value] || null
})

const activeScenarioLabel = computed(() => {
  return scenarioOptions.find(s => s.key === activeScenario.value)?.label || activeScenario.value
})

const activeScenarioColor = computed(() => {
  if (activeScenario.value === 'pessimistic') return 'text-red-400'
  if (activeScenario.value === 'optimistic') return 'text-green-400'
  return 'text-blue-400'
})

// Computed ARR from slider values
const computedARR = computed(() => {
  const betaClients = sliderValues['beta_clients_m12'] || 0
  const betaMrr = sliderValues['beta_mrr_k'] ? sliderValues['beta_mrr_k'] * 1000 : (sliderValues['beta_mrr'] || 0)
  const gammaClients = sliderValues['gamma_clients_m12'] || 0
  const gammaMrr = sliderValues['gamma_mrr'] || 0
  const arr = betaClients * betaMrr * 12 + gammaClients * gammaMrr * 12
  if (arr === 0) return '—'
  if (arr >= 1_000_000) return `R$${(arr / 1_000_000).toFixed(1)}M`
  if (arr >= 1_000) return `R$${(arr / 1_000).toFixed(0)}K`
  return `R$${arr.toFixed(0)}`
})

function updateSlider(id, value) {
  sliderValues[id] = value
  emit('scenario-change', { scenario: activeScenario.value, sliders: { ...sliderValues } })
}

function toggleBool(id) {
  sliderValues[id] = !sliderValues[id]
  emit('scenario-change', { scenario: activeScenario.value, sliders: { ...sliderValues } })
}

function saveToStorage() {
  try {
    localStorage.setItem('neogov-scenario-state', JSON.stringify({
      activeScenario: activeScenario.value,
      sliders: { ...sliderValues },
    }))
    alert('Estado salvo!')
  } catch (e) {
    console.error('Save failed', e)
  }
}

function loadFromStorage() {
  try {
    const raw = localStorage.getItem('neogov-scenario-state')
    if (!raw) { alert('Nenhum estado salvo encontrado.'); return }
    const parsed = JSON.parse(raw)
    if (parsed.activeScenario) activeScenario.value = parsed.activeScenario
    if (parsed.sliders) Object.assign(sliderValues, parsed.sliders)
    emit('scenario-change', { scenario: activeScenario.value, sliders: { ...sliderValues } })
  } catch (e) {
    console.error('Load failed', e)
  }
}

function exportJSON() {
  const state = {
    activeScenario: activeScenario.value,
    sliders: { ...sliderValues },
    computed_arr: computedARR.value,
    exported_at: new Date().toISOString(),
  }
  const blob = new Blob([JSON.stringify(state, null, 2)], { type: 'application/json' })
  const url = URL.createObjectURL(blob)
  const a = document.createElement('a')
  a.href = url
  a.download = `neogov-scenario-${activeScenario.value}-${Date.now()}.json`
  a.click()
  URL.revokeObjectURL(url)
}
</script>
