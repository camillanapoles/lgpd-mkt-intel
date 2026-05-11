<template>
  <div class="space-y-6">
    <!-- Header -->
    <div class="bg-slate-800/50 border border-slate-700 rounded-xl p-6">
      <div class="flex items-start justify-between mb-1">
        <div>
          <h2 class="text-2xl font-bold text-white">{{ company?.name || 'NeoGov' }}</h2>
          <p class="text-slate-400 text-sm mt-1">{{ company?.core_product }}</p>
        </div>
        <span class="text-xs px-2 py-1 rounded bg-blue-900/50 text-blue-400 border border-blue-700 shrink-0 ml-4">
          {{ company?.positioning }}
        </span>
      </div>
    </div>

    <!-- Sun Tzu 5 Factors -->
    <div class="bg-slate-800/50 border border-slate-700 rounded-xl p-6">
      <div class="flex items-center justify-between mb-4">
        <h3 class="text-lg font-bold text-white">5 Fatores Sun Tzu</h3>
        <div class="flex items-center gap-2">
          <span class="text-sm text-slate-400">Total:</span>
          <span class="text-xl font-bold" :class="factorColor(sunTzu?.total, 10)">
            {{ sunTzu?.total?.toFixed(1) }}/{{ sunTzu?.fa?.max || 10 }}
          </span>
        </div>
      </div>
      <p v-if="sunTzu?.interpretation" class="text-xs text-slate-400 italic mb-4">{{ sunTzu.interpretation }}</p>
      <div class="grid grid-cols-5 gap-3">
        <div
          v-for="factor in fiveFactors"
          :key="factor.key"
          class="bg-slate-900/50 rounded-lg p-3 text-center"
        >
          <p class="text-xs text-slate-400 mb-1">{{ factor.name }}</p>
          <p class="text-2xl font-bold" :class="factorColor(factor.score, factor.max)">
            {{ factor.score }}
          </p>
          <div class="h-1.5 bg-slate-700 rounded-full mt-2 overflow-hidden">
            <div
              class="h-full rounded-full transition-all duration-700"
              :class="factorBar(factor.score, factor.max)"
              :style="{ width: `${(factor.score / factor.max) * 100}%` }"
            />
          </div>
          <p class="text-xs text-slate-500 mt-1 truncate" :title="factor.description">{{ factor.description }}</p>
        </div>
      </div>
    </div>

    <!-- KPI Timeline -->
    <div class="bg-slate-800/50 border border-slate-700 rounded-xl p-6">
      <h3 class="text-lg font-bold text-white mb-4">Projecoes Financeiras</h3>
      <div class="overflow-x-auto">
        <table class="w-full text-sm">
          <thead>
            <tr class="border-b border-slate-700">
              <th class="text-left text-slate-400 font-medium py-2 pr-4">Mes</th>
              <th class="text-right text-slate-400 font-medium py-2 px-3">ARR Min</th>
              <th class="text-right text-slate-400 font-medium py-2 px-3">ARR Max</th>
              <th class="text-right text-slate-400 font-medium py-2 px-3">Clientes Min</th>
              <th class="text-right text-slate-400 font-medium py-2 px-3">Clientes Max</th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="kpi in kpiRows"
              :key="kpi.month"
              class="border-b border-slate-700/30 hover:bg-slate-700/20 transition-colors"
            >
              <td class="py-2 pr-4 text-slate-300 font-medium">M{{ kpi.month }}</td>
              <td class="py-2 px-3 text-right font-mono text-green-400">{{ formatCurrency(kpi.arr[0]) }}</td>
              <td class="py-2 px-3 text-right font-mono text-green-300">{{ formatCurrency(kpi.arr[1]) }}</td>
              <td class="py-2 px-3 text-right text-white">{{ kpi.active_clients[0] }}</td>
              <td class="py-2 px-3 text-right text-white">{{ kpi.active_clients[1] }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <div class="grid md:grid-cols-2 gap-6">
      <!-- Risks Summary -->
      <div class="bg-slate-800/50 border border-slate-700 rounded-xl p-6">
        <h3 class="text-lg font-bold text-white mb-4">Riscos Principais</h3>
        <div class="space-y-3">
          <div
            v-for="risk in topRisks"
            :key="risk.id"
            class="p-3 rounded-lg border transition-colors"
            :class="riskBorder(risk)"
          >
            <div class="flex items-start justify-between gap-2">
              <div class="flex-1 min-w-0">
                <div class="flex items-center gap-2 mb-1">
                  <span class="text-xs font-mono text-slate-500">{{ risk.id }}</span>
                  <span class="text-xs px-1.5 py-0.5 rounded font-bold" :class="riskBadge(risk)">
                    {{ risk.impact?.toUpperCase() }}
                  </span>
                </div>
                <p class="text-sm text-white">{{ risk.description }}</p>
              </div>
              <div class="text-right shrink-0">
                <p class="text-xs text-slate-400">Prob</p>
                <p class="text-sm font-bold" :class="probColor(risk.probability)">{{ risk.probability }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Top 3 Clusters by FDC-U -->
      <div class="bg-slate-800/50 border border-slate-700 rounded-xl p-6">
        <h3 class="text-lg font-bold text-white mb-4">Top Clusters FDC-U</h3>
        <div class="space-y-3">
          <div
            v-for="item in topClusters"
            :key="item.rank"
            class="flex items-center gap-4 p-3 rounded-lg bg-slate-900/40 border border-slate-700/50"
          >
            <span class="text-2xl font-bold w-8 text-center" :class="rankColor(item.rank)">
              {{ item.rank }}
            </span>
            <div class="flex-1 min-w-0">
              <p class="text-sm font-medium text-white">{{ item.cluster_name }}</p>
              <div class="h-1.5 bg-slate-700 rounded-full mt-1 overflow-hidden">
                <div
                  class="h-full rounded-full"
                  :class="scoreBar(item.score)"
                  :style="{ width: `${(item.score / 10) * 100}%` }"
                />
              </div>
            </div>
            <div class="shrink-0 text-right">
              <p class="text-lg font-bold font-mono" :class="scoreColor(item.score)">{{ item.score }}</p>
              <p class="text-xs px-2 py-0.5 rounded mt-1" :class="badgeClass(item.badge)">{{ item.badge }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  clusters: { type: Array, default: () => [] },
  kpis: { type: Array, default: () => [] },
  risks: { type: Array, default: () => [] },
  company: { type: Object, default: null },
  sun_tzu_factors: { type: Object, default: null },
  fdcu: { type: Object, default: null },
})

const sunTzu = computed(() => props.sun_tzu_factors)

const fiveFactors = computed(() => {
  const st = sunTzu.value
  if (!st) return []
  return [
    { key: 'dao', name: 'Dao', score: st.dao?.score, max: st.dao?.max || 10, description: st.dao?.description },
    { key: 'tian', name: 'Tian', score: st.tian?.score, max: st.tian?.max || 10, description: st.tian?.description },
    { key: 'di', name: 'Di', score: st.di?.score, max: st.di?.max || 10, description: st.di?.description },
    { key: 'jiang', name: 'Jiang', score: st.jiang?.score, max: st.jiang?.max || 10, description: st.jiang?.description },
    { key: 'fa', name: 'Fa', score: st.fa?.score, max: st.fa?.max || 10, description: st.fa?.description },
  ]
})

const kpiRows = computed(() => {
  return (props.kpis || []).filter(k => [6, 12, 18, 24, 36].includes(k.month))
})

const topRisks = computed(() => {
  return (props.risks || []).slice(0, 6)
})

const topClusters = computed(() => {
  return (props.fdcu?.ranking_pure || []).slice(0, 3)
})

const factorColor = (score, max) => {
  const ratio = score / (max || 10)
  if (ratio >= 0.7) return 'text-green-400'
  if (ratio >= 0.5) return 'text-yellow-400'
  return 'text-red-400'
}

const factorBar = (score, max) => {
  const ratio = score / (max || 10)
  if (ratio >= 0.7) return 'bg-green-500'
  if (ratio >= 0.5) return 'bg-yellow-500'
  return 'bg-red-500'
}

const formatCurrency = (val) => {
  if (!val && val !== 0) return '-'
  if (val >= 1_000_000) return `R$${(val / 1_000_000).toFixed(1)}M`
  if (val >= 1_000) return `R$${(val / 1_000).toFixed(0)}K`
  return `R$${val}`
}

const riskBorder = (risk) => {
  if (risk.impact === 'critical') return 'border-red-700 bg-red-950/20'
  if (risk.impact === 'high') return 'border-yellow-700/50 bg-yellow-950/10'
  return 'border-slate-700 bg-slate-900/20'
}

const riskBadge = (risk) => {
  if (risk.impact === 'critical') return 'bg-red-900/60 text-red-400'
  if (risk.impact === 'high') return 'bg-yellow-900/60 text-yellow-400'
  return 'bg-slate-700 text-slate-300'
}

const probColor = (prob) => {
  if (prob === 'high' || prob === 'alto') return 'text-red-400'
  if (prob === 'medium' || prob === 'medio') return 'text-yellow-400'
  return 'text-green-400'
}

const rankColor = (rank) => {
  if (rank === 1) return 'text-yellow-400'
  if (rank === 2) return 'text-slate-300'
  return 'text-amber-600'
}

const scoreColor = (score) => {
  if (score >= 8) return 'text-green-400'
  if (score >= 6) return 'text-yellow-400'
  return 'text-red-400'
}

const scoreBar = (score) => {
  if (score >= 8) return 'bg-green-500'
  if (score >= 6) return 'bg-yellow-500'
  return 'bg-red-500'
}

const badgeClass = (badge) => {
  if (!badge) return 'text-slate-400'
  const b = badge.toLowerCase()
  if (b.includes('priorit') || b.includes('lider')) return 'bg-green-900/50 text-green-400'
  if (b.includes('viavel') || b.includes('valid')) return 'bg-yellow-900/50 text-yellow-400'
  return 'bg-slate-700/50 text-slate-300'
}
</script>
