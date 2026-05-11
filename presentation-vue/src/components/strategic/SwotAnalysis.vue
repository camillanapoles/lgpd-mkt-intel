<template>
  <div class="space-y-6">
    <!-- Header with VI/AE indices -->
    <div class="flex items-start justify-between">
      <h2 class="text-2xl font-bold text-white">Analise SWOT NeoGov</h2>
      <div class="flex gap-4">
        <div class="text-center bg-slate-800/50 border border-slate-700 rounded-lg px-4 py-2">
          <p class="text-xs text-slate-400 mb-1">VI (Value Index)</p>
          <p class="text-xl font-bold font-mono" :class="viColor">{{ vi.toFixed(2) }}</p>
        </div>
        <div class="text-center bg-slate-800/50 border border-slate-700 rounded-lg px-4 py-2">
          <p class="text-xs text-slate-400 mb-1">AE (Alert Index)</p>
          <p class="text-xl font-bold font-mono" :class="aeColor">{{ ae.toFixed(2) }}</p>
        </div>
        <div class="text-center bg-slate-800/50 border rounded-lg px-4 py-2" :class="quadrantBorder">
          <p class="text-xs text-slate-400 mb-1">Quadrante</p>
          <p class="text-sm font-bold" :class="quadrantColor">{{ quadrantLabel }}</p>
        </div>
      </div>
    </div>

    <!-- 4-quadrant grid -->
    <div class="grid grid-cols-2 gap-4">
      <div
        v-for="q in quadrants"
        :key="q.key"
        class="rounded-xl border-2 p-5 transition-all cursor-pointer"
        :class="[q.bg, activeQuadrant === q.key ? q.borderActive : q.border]"
        @click="activeQuadrant = q.key"
      >
        <div class="flex items-center justify-between mb-3">
          <h3 class="text-base font-bold" :class="q.text">{{ q.title }}</h3>
          <div class="flex items-center gap-2">
            <span class="text-xs text-slate-500">{{ quadrantItems(q.key).length }} itens</span>
            <span class="text-xs px-2 py-0.5 rounded font-mono" :class="q.scoreClass">
              &Sigma;={{ quadrantSum(q.key).toFixed(0) }}
            </span>
          </div>
        </div>

        <div class="space-y-2">
          <div
            v-for="item in quadrantItems(q.key)"
            :key="item.id || item.texto"
            class="p-2 rounded-lg bg-black/20 hover:bg-black/30 transition-colors"
          >
            <div class="flex items-start gap-2">
              <span class="text-xs font-mono text-slate-500 shrink-0 mt-0.5">{{ item.id }}</span>
              <div class="flex-1 min-w-0">
                <div class="flex items-start gap-2">
                  <p class="text-sm text-white flex-1">{{ item.texto }}</p>
                  <button
                    @click.stop="toggleInfo(item.id)"
                    class="shrink-0 w-5 h-5 flex items-center justify-center rounded-full text-xs transition-colors"
                    :class="expanded.has(item.id) ? 'bg-blue-600 text-white' : 'bg-slate-700 text-slate-400 hover:bg-slate-600'"
                  >i</button>
                </div>
                <div class="flex items-center gap-2 mt-1">
                  <div class="flex-1 h-1.5 bg-black/30 rounded-full overflow-hidden">
                    <div
                      class="h-full rounded-full"
                      :class="vvvBar(item.vvv)"
                      :style="{ width: `${(item.vvv || 0) * 100}%` }"
                    />
                  </div>
                  <span class="text-xs font-mono" :class="vvvText(item.vvv)">
                    {{ (item.vvv || 0).toFixed(1) }}
                  </span>
                  <span v-if="item.score" class="text-xs font-mono text-slate-400">
                    {{ item.score }}pts
                  </span>
                </div>
                <div v-if="expanded.has(item.id)" class="mt-2 pt-2 border-t border-white/10 space-y-1">
                  <p class="text-xs text-slate-400">VVV {{ (item.vvv || 0).toFixed(2) }} — {{ vvvLabel(item.vvv) }}</p>
                  <p v-if="item.fonte" class="text-xs text-blue-400 break-all">{{ item.fonte }}</p>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div v-if="topActions(q.key).length" class="mt-3 pt-3 border-t border-white/10">
          <p class="text-xs text-slate-400 mb-1">Acoes prioritarias:</p>
          <p v-for="a in topActions(q.key)" :key="a" class="text-xs text-slate-300">{{ a }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, reactive } from 'vue'

const props = defineProps({
  diagnostic: { type: Object, default: null },
})

const activeQuadrant = ref('forcas')
const expanded = reactive(new Set())

const toggleInfo = (key) => {
  expanded.has(key) ? expanded.delete(key) : expanded.add(key)
}

const swot = computed(() => props.diagnostic?.swot || {})

const quadrants = [
  {
    key: 'forcas',
    title: 'Forcas',
    bg: 'bg-green-950/30',
    border: 'border-green-900/30',
    borderActive: 'border-green-500',
    text: 'text-green-400',
    scoreClass: 'text-green-400 bg-green-900/30',
  },
  {
    key: 'fracas',
    title: 'Fraquezas',
    bg: 'bg-red-950/30',
    border: 'border-red-900/30',
    borderActive: 'border-red-500',
    text: 'text-red-400',
    scoreClass: 'text-red-400 bg-red-900/30',
  },
  {
    key: 'oportunidades',
    title: 'Oportunidades',
    bg: 'bg-blue-950/30',
    border: 'border-blue-900/30',
    borderActive: 'border-blue-500',
    text: 'text-blue-400',
    scoreClass: 'text-blue-400 bg-blue-900/30',
  },
  {
    key: 'ameacas',
    title: 'Ameacas',
    bg: 'bg-amber-950/30',
    border: 'border-amber-900/30',
    borderActive: 'border-amber-500',
    text: 'text-amber-400',
    scoreClass: 'text-amber-400 bg-amber-900/30',
  },
]

const quadrantItems = (key) => swot.value[key] || []
const topActions = (key) => {
  const a = swot.value?.top_actions?.[key]
  return Array.isArray(a) ? a : []
}

const quadrantSum = (key) => {
  return quadrantItems(key).reduce((s, i) => s + (i.score || 0), 0)
}

// VI = (SigmaF - Sigmaf) / (SigmaF + Sigmaf)
const sigmaF = computed(() => quadrantSum('forcas'))
const sigmaf = computed(() => quadrantSum('fracas'))
const sigmaO = computed(() => quadrantSum('oportunidades'))
const sigmaA = computed(() => quadrantSum('ameacas'))

const vi = computed(() => {
  const num = sigmaF.value - sigmaf.value
  const den = sigmaF.value + sigmaf.value
  if (den === 0) return 0
  return num / den
})

const ae = computed(() => {
  const num = sigmaO.value - sigmaA.value
  const den = sigmaO.value + sigmaA.value
  if (den === 0) return 0
  return num / den
})

const viColor = computed(() => vi.value > 0 ? 'text-green-400' : vi.value < 0 ? 'text-red-400' : 'text-yellow-400')
const aeColor = computed(() => ae.value > 0 ? 'text-green-400' : ae.value < 0 ? 'text-red-400' : 'text-yellow-400')

const quadrantLabel = computed(() => {
  if (vi.value > 0 && ae.value > 0) return 'AGRESSIVO'
  if (vi.value > 0 && ae.value <= 0) return 'DEFENSIVO'
  if (vi.value <= 0 && ae.value > 0) return 'TURNAROUND'
  return 'SOBREVIVENCIA'
})

const quadrantColor = computed(() => {
  if (quadrantLabel.value === 'AGRESSIVO') return 'text-green-400'
  if (quadrantLabel.value === 'DEFENSIVO') return 'text-blue-400'
  if (quadrantLabel.value === 'TURNAROUND') return 'text-yellow-400'
  return 'text-red-400'
})

const quadrantBorder = computed(() => {
  if (quadrantLabel.value === 'AGRESSIVO') return 'border-green-700/50'
  if (quadrantLabel.value === 'DEFENSIVO') return 'border-blue-700/50'
  if (quadrantLabel.value === 'TURNAROUND') return 'border-yellow-700/50'
  return 'border-red-700/50'
})

const vvvBar = (v) => {
  if ((v || 0) >= 0.8) return 'bg-green-500'
  if ((v || 0) >= 0.5) return 'bg-yellow-500'
  return 'bg-red-500'
}

const vvvText = (v) => {
  if ((v || 0) >= 0.8) return 'text-green-400'
  if ((v || 0) >= 0.5) return 'text-yellow-400'
  return 'text-red-400'
}

const vvvLabel = (v) => {
  if ((v || 0) >= 0.95) return 'Fato verificado'
  if ((v || 0) >= 0.8) return 'Fonte oficial'
  if ((v || 0) >= 0.5) return 'Analise fundamentada'
  return 'Gap — nao verificado'
}
</script>
