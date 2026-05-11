<template>
  <div class="space-y-6">
    <!-- Header -->
    <div class="bg-slate-800/50 border border-slate-700 rounded-xl p-6">
      <div class="flex items-center justify-between mb-4">
        <h2 class="text-2xl font-bold text-white">FDC-U Ranking Interativo</h2>
        <div class="flex items-center gap-2">
          <span class="text-xs text-slate-400">Soma pesos:</span>
          <span class="text-sm font-bold font-mono" :class="weightsSum === 1.0 ? 'text-green-400' : 'text-red-400'">
            {{ weightsSum.toFixed(2) }}
          </span>
        </div>
      </div>

      <!-- Formula -->
      <div class="bg-slate-900/50 rounded-lg p-3 text-xs font-mono text-slate-400">
        Score = &Sigma;[ raw_score<sub>dim</sub> &times; weight<sub>dim</sub> ] por cluster
      </div>
    </div>

    <!-- View Toggle -->
    <div class="flex gap-3">
      <button
        @click="activeView = 'pure'"
        :class="activeView === 'pure' ? 'bg-blue-600 text-white' : 'bg-slate-700 text-slate-300 hover:bg-slate-600'"
        class="px-4 py-2 rounded-lg text-sm font-medium transition-all"
      >
        Ranking Puro FDC-U
      </button>
      <button
        @click="activeView = 'strategic'"
        :class="activeView === 'strategic' ? 'bg-purple-600 text-white' : 'bg-slate-700 text-slate-300 hover:bg-slate-600'"
        class="px-4 py-2 rounded-lg text-sm font-medium transition-all"
      >
        Decisao Estrategica BSC-03
      </button>
    </div>

    <div class="grid lg:grid-cols-2 gap-6">
      <!-- Rankings Panel -->
      <div class="space-y-4">
        <!-- Pure Ranking -->
        <div v-if="activeView === 'pure'" class="bg-slate-800/50 border border-slate-700 rounded-xl p-5">
          <h3 class="text-base font-bold text-white mb-4">Ranking Puro FDC-U</h3>
          <div class="space-y-3">
            <div
              v-for="item in computedRanking"
              :key="item.cluster_id"
              class="rounded-lg p-3 bg-slate-900/40 border border-slate-700/50"
            >
              <div class="flex items-center gap-3 mb-2">
                <span class="text-xl font-bold w-7 text-center" :class="rankColor(item.rank)">
                  {{ item.rank }}
                </span>
                <div class="flex-1 min-w-0">
                  <p class="text-sm font-medium text-white">{{ item.cluster_name }}</p>
                  <div class="flex items-center gap-2 mt-1">
                    <div class="flex-1 h-2 bg-slate-700 rounded-full overflow-hidden">
                      <div
                        class="h-full rounded-full transition-all duration-500"
                        :class="scoreBarClass(item.score)"
                        :style="{ width: `${(item.score / 10) * 100}%` }"
                      />
                    </div>
                    <span class="text-sm font-bold font-mono" :class="scoreTextClass(item.score)">
                      {{ item.score.toFixed(2) }}
                    </span>
                  </div>
                </div>
                <span class="text-xs px-2 py-0.5 rounded shrink-0" :class="badgeClass(item.badge)">
                  {{ item.badge }}
                </span>
              </div>
              <!-- Depth alert -->
              <div v-if="depthAlert(item.cluster_id)" class="mt-2 pt-2 border-t border-slate-700/50">
                <span
                  class="text-xs px-2 py-0.5 rounded"
                  :class="alertClass(depthAlert(item.cluster_id))"
                >
                  {{ depthAlert(item.cluster_id)?.status }}
                </span>
                <span class="text-xs text-slate-500 ml-2">{{ depthAlert(item.cluster_id)?.acao }}</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Strategic BSC-03 Ranking -->
        <div v-if="activeView === 'strategic'" class="bg-slate-800/50 border border-slate-700 rounded-xl p-5">
          <h3 class="text-base font-bold text-white mb-1">Decisao Estrategica BSC-03</h3>
          <p v-if="fdcu?.ranking_strategic_bsc03?.note" class="text-xs text-slate-400 italic mb-4">
            {{ fdcu.ranking_strategic_bsc03.note }}
          </p>
          <div class="space-y-3">
            <div v-if="fdcu?.ranking_strategic_bsc03?.spearhead" class="p-3 rounded-lg border border-green-700/50 bg-green-950/20">
              <p class="text-xs text-green-400 font-bold mb-1">SPEARHEAD (Lanca)</p>
              <p class="text-sm text-white">{{ fdcu.ranking_strategic_bsc03.spearhead }}</p>
            </div>
            <div v-if="fdcu?.ranking_strategic_bsc03?.parallel?.length" class="p-3 rounded-lg border border-blue-700/50 bg-blue-950/20">
              <p class="text-xs text-blue-400 font-bold mb-2">PARALLEL (Paralelo)</p>
              <ul class="space-y-1">
                <li v-for="p in fdcu.ranking_strategic_bsc03.parallel" :key="p" class="text-sm text-white flex items-start gap-2">
                  <span class="text-blue-400 mt-0.5">›</span>{{ p }}
                </li>
              </ul>
            </div>
            <div v-if="fdcu?.ranking_strategic_bsc03?.rationale" class="p-3 rounded-lg border border-slate-600 bg-slate-900/30">
              <p class="text-xs text-slate-400 font-bold mb-1">RATIONALE</p>
              <p class="text-xs text-slate-300">{{ fdcu.ranking_strategic_bsc03.rationale }}</p>
            </div>
          </div>
        </div>

        <!-- Depth Alerts -->
        <div v-if="depthAlerts.length" class="bg-slate-800/50 border border-slate-700 rounded-xl p-5">
          <h3 class="text-base font-bold text-white mb-3">Alertas de Profundidade</h3>
          <div class="space-y-2">
            <div
              v-for="(alert, key) in fdcu?.depth_alerts"
              :key="key"
              class="flex items-center gap-3 p-2 rounded-lg"
              :class="alertBg(alert)"
            >
              <span class="text-sm font-bold text-white capitalize w-12">{{ key }}</span>
              <span class="text-xs px-2 py-0.5 rounded" :class="alertClass(alert)">{{ alert.status }}</span>
              <span class="text-xs text-slate-400 flex-1">{{ alert.acao }}</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Weight Sliders -->
      <div class="bg-slate-800/50 border border-slate-700 rounded-xl p-5">
        <div class="flex items-center justify-between mb-4">
          <h3 class="text-base font-bold text-white">Pesos das Dimensoes</h3>
          <button
            @click="resetWeights"
            class="text-xs px-3 py-1 rounded bg-slate-700 text-slate-300 hover:bg-slate-600 transition-colors"
          >
            Resetar
          </button>
        </div>
        <div class="space-y-4">
          <div
            v-for="(dim, idx) in dimensions"
            :key="dim.id"
            class="space-y-1"
          >
            <div class="flex items-center justify-between text-sm">
              <span class="text-slate-300">{{ dim.name }}</span>
              <div class="flex items-center gap-2">
                <span class="text-xs text-slate-500">{{ dim.function }}</span>
                <span class="font-mono font-bold text-white">{{ weights[idx].toFixed(2) }}</span>
              </div>
            </div>
            <input
              type="range"
              :value="weights[idx]"
              min="0"
              max="0.5"
              step="0.01"
              @input="updateWeight(idx, Number($event.target.value))"
              class="w-full h-2 bg-slate-700 rounded-lg appearance-none cursor-pointer accent-blue-500"
            />
          </div>
        </div>
        <div class="mt-4 pt-4 border-t border-slate-700 text-xs text-slate-500">
          Mova os sliders para recalcular o ranking em tempo real.
          A soma e normalizada automaticamente para 1.0.
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue'

const props = defineProps({
  fdcu: { type: Object, default: null },
  clusters: { type: Array, default: () => [] },
})

const emit = defineEmits(['fdcu-weights-changed'])

const activeView = ref('pure')

// Initialize weights from fdcu.dimensions
const dimensions = computed(() => props.fdcu?.dimensions || [])
const weights = ref([])

watch(dimensions, (dims) => {
  weights.value = dims.map(d => d.weight ?? 0.1)
}, { immediate: true })

const weightsSum = computed(() => weights.value.reduce((s, w) => s + w, 0))

function updateWeight(idx, val) {
  weights.value[idx] = val
  // Normalize so sum = 1.0
  const sum = weights.value.reduce((s, w) => s + w, 0)
  if (sum > 0) {
    const normalized = weights.value.map(w => w / sum)
    weights.value = normalized
  }
  emit('fdcu-weights-changed', buildWeightsMap())
}

function resetWeights() {
  weights.value = dimensions.value.map(d => d.weight ?? 0.1)
  emit('fdcu-weights-changed', buildWeightsMap())
}

function buildWeightsMap() {
  const map = {}
  dimensions.value.forEach((d, i) => { map[d.id] = weights.value[i] })
  return map
}

// Recompute ranking based on current weights
const computedRanking = computed(() => {
  const pure = props.fdcu?.ranking_pure || []
  const scores = props.fdcu?.scores || {}
  if (!dimensions.value.length || !Object.keys(scores).length) return pure

  // Try to recompute per-cluster using raw scores per dimension
  const recomputed = Object.entries(scores).map(([clusterId, dimScores]) => {
    let score = 0
    dimensions.value.forEach((dim, i) => {
      const raw = dimScores[dim.id]
      if (raw !== undefined) {
        const fn = dim.function
        const adjusted = fn === '-' ? (10 - raw) : raw
        score += adjusted * (weights.value[i] || 0)
      }
    })
    const orig = pure.find(p => p.cluster_id === clusterId)
    return {
      cluster_id: clusterId,
      cluster_name: orig?.cluster_name || clusterId,
      score: parseFloat(score.toFixed(2)),
      badge: orig?.badge || '',
      rank: 0,
    }
  })

  // Re-rank
  recomputed.sort((a, b) => b.score - a.score)
  recomputed.forEach((item, i) => { item.rank = i + 1 })
  return recomputed.length ? recomputed : pure
})

const depthAlerts = computed(() => Object.entries(props.fdcu?.depth_alerts || []))

function depthAlert(clusterId) {
  const alerts = props.fdcu?.depth_alerts || {}
  return alerts[clusterId] || null
}

function rankColor(rank) {
  if (rank === 1) return 'text-yellow-400'
  if (rank === 2) return 'text-slate-300'
  if (rank === 3) return 'text-amber-600'
  return 'text-slate-500'
}

function scoreBarClass(score) {
  if (score >= 8) return 'bg-green-500'
  if (score >= 6) return 'bg-yellow-500'
  if (score >= 4) return 'bg-orange-500'
  return 'bg-red-500'
}

function scoreTextClass(score) {
  if (score >= 8) return 'text-green-400'
  if (score >= 6) return 'text-yellow-400'
  if (score >= 4) return 'text-orange-400'
  return 'text-red-400'
}

function badgeClass(badge) {
  if (!badge) return 'bg-slate-700 text-slate-400'
  const b = badge.toLowerCase()
  if (b.includes('priorit') || b.includes('lider')) return 'bg-green-900/50 text-green-400 border border-green-700'
  if (b.includes('viavel') || b.includes('valid')) return 'bg-yellow-900/50 text-yellow-400 border border-yellow-700'
  return 'bg-slate-700 text-slate-400'
}

function alertClass(alert) {
  if (!alert) return 'bg-slate-700 text-slate-400'
  const color = alert.color || ''
  if (color === 'green') return 'bg-green-900/50 text-green-400'
  if (color === 'yellow') return 'bg-yellow-900/50 text-yellow-400'
  if (color === 'red') return 'bg-red-900/50 text-red-400'
  return 'bg-slate-700 text-slate-400'
}

function alertBg(alert) {
  const color = alert?.color || ''
  if (color === 'green') return 'bg-green-950/20'
  if (color === 'yellow') return 'bg-yellow-950/20'
  if (color === 'red') return 'bg-red-950/20'
  return 'bg-slate-900/20'
}
</script>
