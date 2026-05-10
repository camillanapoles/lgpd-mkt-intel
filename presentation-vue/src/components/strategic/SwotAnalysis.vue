<template>
  <div class="swot-analysis">
    <!-- Header -->
    <div class="flex items-center justify-between mb-4">
      <h2 class="text-h2 text-white">Analise SWOT</h2>
      <div class="flex items-center gap-2">
        <span class="text-caption text-slate-400">Confianca:</span>
        <span class="text-caption font-bold" :class="confidenceColor">
          {{ (confidence * 100).toFixed(0) }}%
        </span>
      </div>
    </div>

    <!-- View mode toggle (R3: Sub-Engine per audience) -->
    <div class="flex items-center gap-2 mb-4">
      <button
        @click="viewMode = 'global'"
        :class="[
          'px-3 py-1 rounded-lg text-caption transition-all border',
          viewMode === 'global'
            ? 'bg-accent-600 text-white border-accent-500'
            : 'bg-slate-800 text-slate-400 border-slate-700 hover:border-slate-500',
        ]"
      >Visao Global</button>
      <button
        @click="setAudienceMode"
        :class="[
          'px-3 py-1 rounded-lg text-caption transition-all border',
          viewMode === 'audience'
            ? 'bg-accent-600 text-white border-accent-500'
            : 'bg-slate-800 text-slate-400 border-slate-700 hover:border-slate-500',
        ]"
      >Por Publico-Alvo</button>
      <span v-if="viewMode === 'audience' && selectedAudience" class="text-caption text-accent-400">
        — {{ selectedAudience.label }}
      </span>
    </div>

    <!-- Audience tab strip -->
    <div v-if="viewMode === 'audience' && audiences.length" class="flex flex-wrap gap-2 mb-4">
      <button
        v-for="aud in audiences"
        :key="aud.id"
        @click="selectedAudienceId = aud.id"
        :class="[
          'px-3 py-1.5 rounded-lg text-caption transition-all border flex items-center gap-1.5',
          selectedAudienceId === aud.id
            ? 'bg-slate-700 text-white border-slate-500'
            : 'bg-slate-800/50 text-slate-400 border-slate-700 hover:border-slate-500',
        ]"
      >
        <span>{{ aud.icon }}</span>
        <span>{{ aud.label }}</span>
      </button>
    </div>

    <!-- Persona banner -->
    <div
      v-if="viewMode === 'audience' && selectedAudience"
      class="bg-slate-800/50 border border-slate-700 rounded-card p-4 mb-5 space-y-2"
    >
      <div class="flex items-center gap-2">
        <span class="text-xl">{{ selectedAudience.icon }}</span>
        <h3 class="text-h4 text-white">{{ selectedAudience.persona?.titulo || selectedAudience.label }}</h3>
        <span class="ml-auto text-caption text-slate-500 italic">Contexto por publico-alvo</span>
      </div>
      <p v-if="selectedAudience.sun_tzu_strategy" class="text-caption italic text-accent-400">"{{ selectedAudience.sun_tzu_strategy }}"</p>
      <div v-if="selectedAudience.persona" class="grid grid-cols-1 gap-1 pt-2 border-t border-slate-700/50">
        <div v-if="selectedAudience.persona.pain_point" class="flex gap-2">
          <span class="text-caption text-slate-500 shrink-0 w-28">Dor principal:</span>
          <span class="text-caption text-slate-300">{{ selectedAudience.persona.pain_point }}</span>
        </div>
        <div v-if="selectedAudience.persona.valor_entregue" class="flex gap-2">
          <span class="text-caption text-slate-500 shrink-0 w-28">Valor entregue:</span>
          <span class="text-caption text-slate-300">{{ selectedAudience.persona.valor_entregue }}</span>
        </div>
        <div v-if="selectedAudience.persona.canal_ideal" class="flex gap-2">
          <span class="text-caption text-slate-500 shrink-0 w-28">Canal ideal:</span>
          <span class="text-caption text-slate-300">{{ selectedAudience.persona.canal_ideal }}</span>
        </div>
      </div>
      <p class="text-caption text-slate-500 pt-1">
        Os itens SWOT abaixo sao o campo de batalha global — lidos atraves da lente deste publico.
      </p>
    </div>

    <!-- SWOT grid -->
    <div class="grid grid-cols-2 gap-4">
      <div
        v-for="quadrant in quadrants"
        :key="quadrant.key"
        :class="[
          'rounded-card border-2 p-4 transition-all cursor-pointer',
          activeQuadrant === quadrant.key
            ? `${quadrant.bgActive} ${quadrant.borderActive} shadow-card-hover`
            : `${quadrant.bg} ${quadrant.border}`,
        ]"
        @click="activeQuadrant = quadrant.key"
        @mouseenter="hoveredQuadrant = quadrant.key"
        @mouseleave="hoveredQuadrant = null"
      >
        <div class="flex items-center justify-between mb-3">
          <h3 :class="['text-h4', quadrant.text]">{{ quadrant.title }}</h3>
          <span class="text-caption text-slate-400">{{ items(quadrant.key).length }}</span>
        </div>

        <div class="space-y-2">
          <div
            v-for="item in items(quadrant.key)"
            :key="item.id"
            class="flex items-start gap-2 p-2 rounded-lg bg-black/20 hover:bg-black/30 transition-colors"
          >
            <span class="text-caption font-mono text-slate-400 mt-0.5 shrink-0">{{ item.id }}</span>
            <div class="flex-1 min-w-0">
              <div class="flex items-center gap-1.5">
                <p class="text-body-sm text-white flex-1">{{ item.texto }}</p>
                <button
                  @click.stop="toggleInfo(item.id)"
                  class="shrink-0 w-5 h-5 flex items-center justify-center rounded-full text-xs transition-colors"
                  :class="expandedInfo.has(item.id) ? 'bg-accent-600 text-white' : 'bg-slate-700 text-slate-400 hover:bg-slate-600'"
                  title="Ver fonte e detalhes"
                >i</button>
              </div>
              <div class="flex items-center gap-2 mt-1">
                <div class="flex-1 h-1.5 bg-black/30 rounded-full overflow-hidden">
                  <div
                    class="h-full rounded-full transition-all duration-500"
                    :class="vvvBarClass(item.vvv)"
                    :style="{ width: `${item.vvv * 100}%` }"
                  />
                </div>
                <span class="text-caption" :class="vvvTextClass(item.vvv)">
                  {{ item.vvv.toFixed(1) }}
                </span>
              </div>
              <div v-if="expandedInfo.has(item.id)" class="space-y-1 border-t border-slate-700/50 mt-1 pt-1.5">
                <p class="text-caption text-slate-400">VVV: {{ item.vvv.toFixed(2) }} — {{ vvvExplanation(item.vvv) }}</p>
                <div class="flex items-center gap-2 flex-wrap">
                  <span class="text-caption text-slate-500">Fonte:</span>
                  <span class="text-accent-400 text-xs">{{ item.fonte || 'Nao mapeada' }}</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div v-if="topActions(quadrant.key).length" class="mt-3 pt-3 border-t border-white/10">
          <p class="text-caption text-slate-400 mb-1">Acoes prioritarias:</p>
          <p
            v-for="action in topActions(quadrant.key)"
            :key="action"
            class="text-caption text-slate-300"
          >
            {{ action }}
          </p>
        </div>
      </div>
    </div>

  </div>
</template>

<script setup>
import { ref, computed, reactive, onMounted } from 'vue'

const props = defineProps({
  swot: { type: Object, required: true },
  confidence: { type: Number, default: 0.82 },
})

// Audience state (R3: Sub-Engine per audience)
const viewMode = ref('global')
const selectedAudienceId = ref(null)
const audiences = ref([])

const selectedAudience = computed(() =>
  audiences.value.find(a => a.id === selectedAudienceId.value) ?? null
)

const setAudienceMode = () => {
  viewMode.value = 'audience'
  if (!selectedAudienceId.value && audiences.value.length) {
    selectedAudienceId.value = audiences.value[0].id
  }
}

onMounted(async () => {
  try {
    const base = import.meta.env.BASE_URL
    const r = await fetch(`${base}strategic-data-unified.json`)
    const json = await r.json()
    audiences.value = json?.snti?.audiences ?? []
  } catch {
    audiences.value = []
  }
})

// Existing state
const activeQuadrant = ref('forcas')
const hoveredQuadrant = ref(null)
const expandedInfo = reactive(new Set())

const toggleInfo = (key) => {
  expandedInfo.has(key) ? expandedInfo.delete(key) : expandedInfo.add(key)
}

const quadrants = [
  {
    key: 'forcas',
    title: 'Forcas',
    bg: 'bg-green-950/30',
    bgActive: 'bg-green-950/50',
    border: 'border-green-900/30',
    borderActive: 'border-green-500',
    text: 'text-green-400',
  },
  {
    key: 'fracas',
    title: 'Fraquezas',
    bg: 'bg-red-950/30',
    bgActive: 'bg-red-950/50',
    border: 'border-red-900/30',
    borderActive: 'border-red-500',
    text: 'text-red-400',
  },
  {
    key: 'oportunidades',
    title: 'Oportunidades',
    bg: 'bg-blue-950/30',
    bgActive: 'bg-blue-950/50',
    border: 'border-blue-900/30',
    borderActive: 'border-blue-500',
    text: 'text-blue-400',
  },
  {
    key: 'ameacas',
    title: 'Ameacas',
    bg: 'bg-amber-950/30',
    bgActive: 'bg-amber-950/50',
    border: 'border-amber-900/30',
    borderActive: 'border-amber-500',
    text: 'text-amber-400',
  },
]

const items = (key) => props.swot[key] || []

const topActions = (key) => {
  const actions = props.swot.top_actions?.[key]
  return Array.isArray(actions) ? actions : []
}

const vvvBarClass = (vvv) => {
  if (vvv >= 0.8) return 'bg-green-500'
  if (vvv >= 0.5) return 'bg-yellow-500'
  return 'bg-red-500'
}

const vvvTextClass = (vvv) => {
  if (vvv >= 0.8) return 'text-green-400'
  if (vvv >= 0.5) return 'text-yellow-400'
  return 'text-red-400'
}

const confidenceColor = computed(() => {
  if (props.confidence >= 0.8) return 'text-green-400'
  if (props.confidence >= 0.6) return 'text-yellow-400'
  return 'text-red-400'
})

const vvvExplanation = (vvv) => {
  if (vvv >= 0.95) return 'Fato verificado (transcricao/fonte oficial)'
  if (vvv >= 0.8) return 'Fonte oficial citada com confianca alta'
  if (vvv >= 0.5) return 'Analise fundamentada, parcialmente verificada'
  return 'Gap — nao verificado, necessita pesquisa'
}
</script>
