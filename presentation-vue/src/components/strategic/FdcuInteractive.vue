<template>
  <div class="space-y-6">
    <!-- Header com Fórmula FDC-U -->
    <div class="bg-slate-800/50 rounded-xl p-6 border border-slate-700">
      <h2 class="text-2xl font-bold text-white mb-4">FDC-U Interactive Editor</h2>
      <div class="bg-slate-900/50 rounded-lg p-4 mb-4">
        <p class="text-slate-300 text-center text-lg font-mono">
          Score = <span class="text-blue-400">Impacto(0.30)</span> + <span class="text-green-400">Urgência(0.25)</span> + <span class="text-yellow-400">VVV(0.20)</span> + <span class="text-purple-400">Esforço-Inv(0.15)</span> + <span class="text-red-400">Risco-Inv(0.10)</span>
        </p>
      </div>

      <!-- KPIs Globais -->
      <div class="grid grid-cols-2 md:grid-cols-5 gap-4">
        <div class="bg-slate-700/50 rounded-lg p-3 text-center">
          <p class="text-slate-400 text-sm">Score Médio</p>
          <p class="text-2xl font-bold" :class="averageScoreClass">{{ averageScore.toFixed(2) }}</p>
        </div>
        <div class="bg-slate-700/50 rounded-lg p-3 text-center">
          <p class="text-slate-400 text-sm">VVV Médio</p>
          <p class="text-2xl font-bold" :class="averageVvvClass">{{ averageVvv.toFixed(2) }}</p>
        </div>
        <div class="bg-slate-700/50 rounded-lg p-3 text-center">
          <p class="text-slate-400 text-sm">Gaps Críticos</p>
          <p class="text-2xl font-bold text-red-400">{{ criticalGaps }}</p>
        </div>
        <div class="bg-slate-700/50 rounded-lg p-3 text-center">
          <p class="text-slate-400 text-sm">Quick Wins</p>
          <p class="text-2xl font-bold text-green-400">{{ quickWins }}</p>
        </div>
        <div class="bg-slate-700/50 rounded-lg p-3 text-center">
          <p class="text-slate-400 text-sm">Total Itens</p>
          <p class="text-2xl font-bold text-slate-300">{{ items.length }}</p>
        </div>
      </div>
    </div>

    <!-- Controles de Visualização -->
    <div class="flex gap-4 flex-wrap">
      <button
        @click="sortBy = 'score'"
        :class="sortBy === 'score' ? 'bg-blue-600' : 'bg-slate-700'"
        class="px-4 py-2 rounded-lg text-white transition-all"
      >
        Ordenar por Score
      </button>
      <button
        @click="sortBy = 'vvv'"
        :class="sortBy === 'vvv' ? 'bg-blue-600' : 'bg-slate-700'"
        class="px-4 py-2 rounded-lg text-white transition-all"
      >
        Ordenar por VVV
      </button>
      <button
        @click="showOnlyCritical = !showOnlyCritical"
        :class="showOnlyCritical ? 'bg-red-600' : 'bg-slate-700'"
        class="px-4 py-2 rounded-lg text-white transition-all"
      >
        {{ showOnlyCritical ? 'Mostrar Todos' : 'Apenas Críticos (VVV<0.5)' }}
      </button>
      <button
        @click="resetAll"
        class="px-4 py-2 rounded-lg bg-orange-600 text-white transition-all hover:bg-orange-500"
      >
        Resetar Valores
      </button>
    </div>

    <!-- Matriz de Itens Editáveis -->
    <div class="space-y-4">
      <div
        v-for="item in sortedItems"
        :key="item.id"
        class="bg-slate-800/50 rounded-xl p-6 border transition-all"
        :class="getItemBorderClass(item)"
      >
        <!-- Header do Item -->
        <div class="flex items-center justify-between mb-4">
          <div class="flex-1">
            <div class="flex items-center gap-2">
              <h3 class="text-xl font-bold text-white">{{ item.name }}</h3>
              <button
                @click.stop="toggleInfo(`fdcu-${item.id}`)"
                class="w-5 h-5 flex items-center justify-center rounded-full text-xs transition-colors"
                :class="expandedInfo.has(`fdcu-${item.id}`) ? 'bg-accent-600 text-white' : 'bg-slate-700 text-slate-400 hover:bg-slate-600'"
                title="Ver detalhes FDC-U"
              >i</button>
            </div>
            <p class="text-slate-400 text-sm">{{ item.description }}</p>
          </div>
          <div class="text-right">
            <p class="text-3xl font-bold" :class="getScoreClass(item.score)">{{ item.score.toFixed(2) }}</p>
            <p class="text-sm" :class="getCategoryClass(item)">{{ getCategoryLabel(item) }}</p>
            <p v-if="item.delta !== 0" class="text-sm font-bold" :class="item.delta > 0 ? 'text-green-400' : 'text-red-400'">
              {{ item.delta > 0 ? '+' : '' }}{{ item.delta.toFixed(2) }}
            </p>
          </div>
        </div>
        <div v-if="expandedInfo.has(`fdcu-${item.id}`)" class="mb-4 p-3 rounded bg-slate-900/50 border border-slate-700/50 space-y-1">
          <p class="text-xs text-slate-400">Dimensao: {{ item.dimensao || 'N/A' }} — Status: {{ item.status || 'N/A' }}</p>
          <p class="text-xs text-slate-400">Fonte: <span class="text-accent-400">{{ item.fonte }}</span></p>
          <p class="text-xs text-slate-400">VVV: {{ item.vvv.toFixed(2) }} — {{ vvvExplanation(item.vvv) }}</p>
          <p v-if="item.prazo" class="text-xs text-slate-500">Prazo: {{ item.prazo }}</p>
        </div>

        <!-- Controles Editáveis -->
        <div class="grid grid-cols-2 md:grid-cols-5 gap-4">
          <!-- Impacto -->
          <div class="space-y-2">
            <label class="flex items-center justify-between text-sm">
              <span class="text-blue-400">Impacto</span>
              <span class="text-white font-bold">{{ item.impacto }}</span>
            </label>
            <input
              type="range"
              v-model.number="item.impacto"
              min="0"
              max="10"
              step="1"
              @input="updateScore(item)"
              class="w-full h-2 bg-slate-700 rounded-lg appearance-none cursor-pointer accent-blue-500"
            >
            <div class="flex justify-between text-xs text-slate-500">
              <span>0</span>
              <span>10</span>
            </div>
          </div>

          <!-- Urgência -->
          <div class="space-y-2">
            <label class="flex items-center justify-between text-sm">
              <span class="text-green-400">Urgência</span>
              <span class="text-white font-bold">{{ item.urgencia }}</span>
            </label>
            <input
              type="range"
              v-model.number="item.urgencia"
              min="0"
              max="10"
              step="1"
              @input="updateScore(item)"
              class="w-full h-2 bg-slate-700 rounded-lg appearance-none cursor-pointer accent-green-500"
            >
            <div class="flex justify-between text-xs text-slate-500">
              <span>0</span>
              <span>10</span>
            </div>
          </div>

          <!-- VVV -->
          <div class="space-y-2">
            <label class="flex items-center justify-between text-sm">
              <span class="text-yellow-400">VVV</span>
              <span class="text-white font-bold">{{ item.vvv.toFixed(1) }}</span>
            </label>
            <input
              type="range"
              v-model.number="item.vvv"
              min="0"
              max="1"
              step="0.1"
              @input="updateScore(item)"
              class="w-full h-2 bg-slate-700 rounded-lg appearance-none cursor-pointer accent-yellow-500"
            >
            <div class="flex justify-between text-xs text-slate-500">
              <span>0</span>
              <span>1</span>
            </div>
          </div>

          <!-- Esforço (Inverso) -->
          <div class="space-y-2">
            <label class="flex items-center justify-between text-sm">
              <span class="text-purple-400">Esforço</span>
              <span class="text-white font-bold">{{ item.esforco }}</span>
            </label>
            <input
              type="range"
              v-model.number="item.esforco"
              min="0"
              max="10"
              step="1"
              @input="updateScore(item)"
              class="w-full h-2 bg-slate-700 rounded-lg appearance-none cursor-pointer accent-purple-500"
            >
            <div class="flex justify-between text-xs text-slate-500">
              <span>0</span>
              <span>10</span>
            </div>
            <p class="text-xs text-slate-500 text-center">Inverso: menos = melhor</p>
          </div>

          <!-- Risco (Inverso) -->
          <div class="space-y-2">
            <label class="flex items-center justify-between text-sm">
              <span class="text-red-400">Risco</span>
              <span class="text-white font-bold">{{ item.risco }}</span>
            </label>
            <input
              type="range"
              v-model.number="item.risco"
              min="0"
              max="10"
              step="1"
              @input="updateScore(item)"
              class="w-full h-2 bg-slate-700 rounded-lg appearance-none cursor-pointer accent-red-500"
            >
            <div class="flex justify-between text-xs text-slate-500">
              <span>0</span>
              <span>10</span>
            </div>
            <p class="text-xs text-slate-500 text-center">Inverso: menos = melhor</p>
          </div>
        </div>

        <!-- Breakdown do Score -->
        <div class="mt-4 p-3 bg-slate-900/50 rounded-lg">
          <p class="text-xs text-slate-400 mb-2">Breakdown:</p>
          <div class="grid grid-cols-5 gap-2 text-center text-sm">
            <div>
              <p class="text-blue-400">{{ (item.impacto * 0.30).toFixed(2) }}</p>
              <p class="text-xs text-slate-500">Impacto×0.30</p>
            </div>
            <div>
              <p class="text-green-400">{{ (item.urgencia * 0.25).toFixed(2) }}</p>
              <p class="text-xs text-slate-500">Urgência×0.25</p>
            </div>
            <div>
              <p class="text-yellow-400">{{ (item.vvv * 0.20).toFixed(2) }}</p>
              <p class="text-xs text-slate-500">VVV×0.20</p>
            </div>
            <div>
              <p class="text-purple-400">{{ ((10 - item.esforco) * 0.15).toFixed(2) }}</p>
              <p class="text-xs text-slate-500">(10-Esfo)×0.15</p>
            </div>
            <div>
              <p class="text-red-400">{{ ((10 - item.risco) * 0.10).toFixed(2) }}</p>
              <p class="text-xs text-slate-500">(10-Risco)×0.10</p>
            </div>
          </div>
        </div>

        <!-- Fonte e Gap -->
        <div class="mt-3 flex items-center justify-between text-sm">
          <span class="text-slate-500">
            Fonte: <span class="text-slate-400">{{ item.fonte }}</span>
          </span>
          <span v-if="item.vvv < 0.5" class="text-red-400 font-bold">
            ⚠️ GAP CRÍTICO - VVV < 0.5
          </span>
        </div>
      </div>
    </div>

    <!-- Legenda -->
    <div class="bg-slate-800/50 rounded-xl p-4 border border-slate-700">
      <h4 class="text-white font-bold mb-3">Legenda de Categorias</h4>
      <div class="grid grid-cols-2 md:grid-cols-4 gap-3 text-sm">
        <div class="flex items-center gap-2">
          <div class="w-4 h-4 rounded bg-red-500"></div>
          <span class="text-slate-300">Crítico (8.0+)</span>
        </div>
        <div class="flex items-center gap-2">
          <div class="w-4 h-4 rounded bg-orange-500"></div>
          <span class="text-slate-300">Alto (6.5-7.9)</span>
        </div>
        <div class="flex items-center gap-2">
          <div class="w-4 h-4 rounded bg-yellow-500"></div>
          <span class="text-slate-300">Médio (5.0-6.4)</span>
        </div>
        <div class="flex items-center gap-2">
          <div class="w-4 h-4 rounded bg-slate-500"></div>
          <span class="text-slate-300">Baixo (<5.0)</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch, reactive } from 'vue'

const expandedInfo = reactive(new Set())
const toggleInfo = (key) => {
  expandedInfo.has(key) ? expandedInfo.delete(key) : expandedInfo.add(key)
}
const vvvExplanation = (vvv) => {
  if (vvv >= 0.95) return 'Fato verificado (transcricao/fonte oficial)'
  if (vvv >= 0.8) return 'Fonte oficial citada com confianca alta'
  if (vvv >= 0.5) return 'Analise fundamentada, parcialmente verificada'
  return 'Gap — nao verificado, necessita pesquisa'
}

const props = defineProps({
  initialData: {
    type: Object,
    default: () => ({})
  }
})

// Map JSON items to component's internal format
const mapJsonItem = (jsonItem) => ({
  id: jsonItem.id,
  name: jsonItem.name || jsonItem.id,
  description: jsonItem.description || '',
  dimensao: jsonItem.dimensao || '',
  impacto: jsonItem.impacto ?? jsonItem.peso ?? 5,
  urgencia: jsonItem.urgencia ?? 5,
  vvv: jsonItem.vvv ?? 0.0,
  esforco: jsonItem.esforco ?? 5,
  risco: jsonItem.risco ?? 3,
  fonte: jsonItem.fonte || 'strategic-data-unified.json',
  prazo: jsonItem.prazo || '',
  status: jsonItem.status || '',
  delta: 0
})

const items = ref([])
const originalScores = ref({})
const sortBy = ref('score')
const showOnlyCritical = ref(false)

const initFromData = (data) => {
  const jsonItems = data?.items || []
  items.value = jsonItems.map(mapJsonItem)
  items.value.forEach(item => {
    item.score = calculateScore(item)
    originalScores.value[item.id] = item.score
  })
}

// Initialize from props, react to changes
watch(() => props.initialData, (newData) => {
  if (newData) initFromData(newData)
}, { immediate: true })

function calculateScore(item) {
  return (
    (item.impacto * 0.30) +
    (item.urgencia * 0.25) +
    (item.vvv * 0.20) +
    ((10 - item.esforco) * 0.15) +
    ((10 - item.risco) * 0.10)
  )
}

function updateScore(item) {
  const oldScore = item.score
  item.score = calculateScore(item)
  item.delta = item.score - originalScores.value[item.id]
}

function resetAll() {
  initFromData(props.initialData)
}

const sortedItems = computed(() => {
  let filtered = showOnlyCritical.value
    ? items.value.filter(i => i.vvv < 0.5)
    : items.value

  return [...filtered].sort((a, b) => {
    if (sortBy.value === 'score') return b.score - a.score
    if (sortBy.value === 'vvv') return b.vvv - a.vvv
    return 0
  })
})

const averageScore = computed(() => {
  return items.value.reduce((sum, i) => sum + i.score, 0) / items.value.length || 0
})

const averageVvv = computed(() => {
  return items.value.reduce((sum, i) => sum + i.vvv, 0) / items.value.length || 0
})

const criticalGaps = computed(() => {
  return items.value.filter(i => i.vvv < 0.5).length
})

const quickWins = computed(() => {
  return items.value.filter(i => i.impacto >= 8 && i.esforco <= 5).length
})

const averageScoreClass = computed(() => {
  if (averageScore.value >= 6.5) return 'text-green-400'
  if (averageScore.value >= 5.0) return 'text-yellow-400'
  return 'text-red-400'
})

const averageVvvClass = computed(() => {
  if (averageVvv.value >= 0.8) return 'text-green-400'
  if (averageVvv.value >= 0.5) return 'text-yellow-400'
  return 'text-red-400'
})

function getScoreClass(score) {
  if (score >= 8.0) return 'text-red-400'
  if (score >= 6.5) return 'text-orange-400'
  if (score >= 5.0) return 'text-yellow-400'
  return 'text-slate-400'
}

function getCategoryLabel(item) {
  if (item.vvv < 0.5) return 'GAP CRÍTICO'
  if (item.impacto >= 8 && item.esforco <= 5) return 'QUICK_WIN'
  if (item.score >= 8.0) return 'CRÍTICO'
  if (item.score >= 6.5) return 'ALTO'
  if (item.score >= 5.0) return 'MÉDIO'
  return 'BAIXO'
}

function getCategoryClass(item) {
  if (item.vvv < 0.5) return 'text-red-400'
  if (item.impacto >= 8 && item.esforco <= 5) return 'text-green-400'
  return 'text-slate-400'
}

function getItemBorderClass(item) {
  if (item.vvv < 0.5) return 'border-red-500/50'
  if (item.delta > 0.5) return 'border-green-500/50'
  if (item.delta < -0.5) return 'border-red-500/50'
  return 'border-slate-700'
}
</script>
