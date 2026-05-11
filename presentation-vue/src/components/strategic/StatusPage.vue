<template>
  <div class="space-y-6">
    <!-- Header -->
    <div class="flex items-center justify-between">
      <h2 class="text-2xl font-bold text-white">VVV Research Gaps</h2>
      <span class="text-sm text-slate-400">
        {{ criticalCount }} gap(s) CRITICO(s)
      </span>
    </div>

    <!-- VVV Gaps Table -->
    <div class="bg-slate-800/50 border border-slate-700 rounded-xl overflow-hidden">
      <div class="p-4 border-b border-slate-700">
        <h3 class="text-base font-bold text-white">Gaps de Validacao VVV</h3>
      </div>
      <div class="overflow-x-auto">
        <table class="w-full text-sm">
          <thead>
            <tr class="border-b border-slate-700 bg-slate-900/30">
              <th class="text-left text-slate-400 font-medium py-3 px-4">ID</th>
              <th class="text-left text-slate-400 font-medium py-3 px-4">Descricao</th>
              <th class="text-left text-slate-400 font-medium py-3 px-4 w-32">VVV Score</th>
              <th class="text-left text-slate-400 font-medium py-3 px-4">Classificacao</th>
              <th class="text-left text-slate-400 font-medium py-3 px-4">Acao Requerida</th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="gap in sortedGaps"
              :key="gap.id"
              class="border-b border-slate-700/30 hover:bg-slate-700/20 transition-colors"
              :class="gap.vvv_score === 0 ? 'bg-red-950/20' : ''"
            >
              <td class="py-3 px-4">
                <span class="font-mono text-xs px-2 py-1 rounded" :class="gapIdClass(gap)">
                  {{ gap.id }}
                </span>
              </td>
              <td class="py-3 px-4 text-slate-200 max-w-xs">{{ gap.description }}</td>
              <td class="py-3 px-4">
                <div class="flex items-center gap-2">
                  <div class="w-16 h-2 bg-slate-700 rounded-full overflow-hidden">
                    <div
                      class="h-full rounded-full transition-all"
                      :class="vvvBarClass(gap.vvv_score)"
                      :style="{ width: `${gap.vvv_score * 100}%` }"
                    />
                  </div>
                  <span class="font-mono text-xs" :class="vvvTextClass(gap.vvv_score)">
                    {{ gap.vvv_score.toFixed(2) }}
                  </span>
                </div>
              </td>
              <td class="py-3 px-4">
                <span class="text-xs px-2 py-1 rounded font-bold" :class="classificationClass(gap.classification)">
                  {{ gap.classification }}
                </span>
              </td>
              <td class="py-3 px-4 text-slate-400 text-xs max-w-xs">{{ gap.action_required }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- Action Plan -->
    <div v-if="actionPlan" class="bg-slate-800/50 border border-slate-700 rounded-xl p-6">
      <h3 class="text-base font-bold text-white mb-4">Plano de Acao</h3>
      <div class="grid md:grid-cols-3 gap-4">
        <div
          v-for="period in actionPeriods"
          :key="period.key"
          class="bg-slate-900/40 border border-slate-700/50 rounded-lg p-4"
        >
          <h4 class="text-sm font-bold mb-3" :class="period.color">{{ period.label }}</h4>
          <ul class="space-y-2">
            <li
              v-for="item in (actionPlan[period.key] || [])"
              :key="item"
              class="flex items-start gap-2 text-xs text-slate-300"
            >
              <span class="shrink-0 mt-0.5" :class="period.color">☐</span>
              {{ item }}
            </li>
            <li v-if="!(actionPlan[period.key] || []).length" class="text-xs text-slate-600 italic">
              Sem acoes definidas.
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  vvv_gaps: { type: Array, default: () => [] },
  action_plan: { type: Object, default: null },
})

const actionPlan = computed(() => props.action_plan)

const sortedGaps = computed(() => {
  return [...(props.vvv_gaps || [])].sort((a, b) => a.vvv_score - b.vvv_score)
})

const criticalCount = computed(() => {
  return (props.vvv_gaps || []).filter(g => g.vvv_score === 0 || g.classification === 'CRITICAL').length
})

const actionPeriods = [
  { key: 'dias_30', label: '30 Dias', color: 'text-yellow-400' },
  { key: 'dias_60', label: '60 Dias', color: 'text-blue-400' },
  { key: 'dias_90', label: '90 Dias', color: 'text-green-400' },
]

const gapIdClass = (gap) => {
  if (gap.vvv_score === 0) return 'bg-red-900/60 text-red-300 border border-red-600'
  if (gap.vvv_score < 0.5) return 'bg-orange-900/60 text-orange-300'
  return 'bg-slate-700 text-slate-300'
}

const vvvBarClass = (score) => {
  if (score === 0) return 'bg-red-600'
  if (score < 0.5) return 'bg-orange-500'
  if (score < 0.8) return 'bg-yellow-500'
  return 'bg-green-500'
}

const vvvTextClass = (score) => {
  if (score === 0) return 'text-red-400 font-bold'
  if (score < 0.5) return 'text-orange-400'
  if (score < 0.8) return 'text-yellow-400'
  return 'text-green-400'
}

const classificationClass = (cls) => {
  if (!cls) return 'bg-slate-700 text-slate-400'
  const c = cls.toUpperCase()
  if (c === 'CRITICAL') return 'bg-red-900/60 text-red-300 border border-red-600'
  if (c === 'HIGH') return 'bg-orange-900/60 text-orange-300'
  if (c === 'MEDIUM') return 'bg-yellow-900/60 text-yellow-300'
  return 'bg-slate-700 text-slate-400'
}
</script>
