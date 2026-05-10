<template>
  <div class="dashboard-5s">
    <div class="flex items-center justify-between mb-6">
      <h2 class="text-h2 text-white">Dashboard Estrategico</h2>
      <span class="text-caption text-slate-400">
        {{ dashboard.lastMeeting ? `Ultima reuniao: ${dashboard.lastMeeting}` : '' }}
      </span>
    </div>

    <div class="grid grid-cols-2 md:grid-cols-5 gap-4 mb-6">
      <div
        v-for="kpi in kpiCards"
        :key="kpi.key"
        class="bg-slate-800/50 border border-slate-700 rounded-card p-5 text-center hover:border-slate-500 transition-all relative"
      >
        <button
          @click.stop="toggleInfo(`kpi-${kpi.key}`)"
          class="absolute top-2 right-2 w-5 h-5 flex items-center justify-center rounded-full text-xs transition-colors"
          :class="expandedInfo.has(`kpi-${kpi.key}`) ? 'bg-accent-600 text-white' : 'bg-slate-700 text-slate-400 hover:bg-slate-600'"
          title="Ver detalhes"
        >i</button>
        <p class="text-caption text-slate-400 mb-1">{{ kpi.label }}</p>
        <p class="text-display text-white">{{ kpi.value }}</p>
        <p v-if="kpi.tag" :class="['text-caption mt-2', kpi.tagClass]">{{ kpi.tag }}</p>
        <div v-if="expandedInfo.has(`kpi-${kpi.key}`)" class="mt-2 pt-2 border-t border-slate-700/50 text-left">
          <p class="text-caption text-slate-400">{{ kpiExplanation(kpi.key) }}</p>
        </div>
      </div>
    </div>

    <div class="grid md:grid-cols-2 gap-6">
      <div class="bg-slate-800/50 border border-slate-700 rounded-card p-5">
        <h3 class="text-h4 text-white mb-4">Confianca por Area</h3>
        <div class="space-y-3">
          <div v-for="badge in confidenceBadges" :key="badge.label">
            <div class="flex items-center justify-between mb-1">
              <span class="text-body-sm text-slate-300">{{ badge.label }}</span>
              <div class="flex items-center gap-1.5">
                <span class="text-caption font-mono" :class="badge.textClass">
                  {{ (badge.value * 100).toFixed(0) }}%
                </span>
                <button
                  @click.stop="toggleInfo(`badge-${badge.label}`)"
                  class="w-4 h-4 flex items-center justify-center rounded-full text-xs transition-colors"
                  :class="expandedInfo.has(`badge-${badge.label}`) ? 'bg-accent-600 text-white' : 'bg-slate-700 text-slate-400 hover:bg-slate-600'"
                  title="Ver explicacao"
                >i</button>
              </div>
            </div>
            <div class="h-2 bg-slate-700 rounded-full overflow-hidden">
              <div
                class="h-full rounded-full transition-all duration-700"
                :class="badge.barClass"
                :style="{ width: `${badge.value * 100}%` }"
              />
            </div>
            <p v-if="expandedInfo.has(`badge-${badge.label}`)" class="text-caption text-slate-400 mt-1">
              {{ vvvExplanation(badge.value) }}
            </p>
          </div>
        </div>
      </div>

      <div class="bg-slate-800/50 border border-slate-700 rounded-card p-5">
        <h3 class="text-h4 text-white mb-4">Acoes Urgentes</h3>
        <div class="space-y-2">
          <div
            v-for="item in lowVvvItems"
            :key="item.item"
            class="flex items-start gap-3 p-2 rounded-lg hover:bg-slate-700/30 transition-colors"
          >
            <span
              class="text-caption font-bold px-1.5 py-0.5 rounded mt-0.5 shrink-0"
              :class="priorityClass(item.priority)"
            >
              {{ item.priority }}
            </span>
            <div class="min-w-0">
              <p class="text-body-sm text-white">{{ item.item.replace(/_/g, ' ') }}</p>
              <p class="text-caption text-slate-500">{{ item.acao }}</p>
            </div>
            <span class="text-caption text-slate-400 shrink-0">VVV: {{ item.vvv }}</span>
          </div>
        </div>
      </div>
    </div>

    <div v-if="fdcuTop.length" class="mt-6 bg-slate-800/50 border border-slate-700 rounded-card p-5">
      <h3 class="text-h4 text-white mb-4">Prioridades FDC-U</h3>
      <div class="space-y-2">
        <div
          v-for="item in fdcuTop"
          :key="item.rank"
          class="flex items-center gap-4 p-3 rounded-lg bg-slate-900/30"
        >
          <span class="text-h3 text-accent-400 font-bold w-8 text-center">{{ item.rank }}</span>
          <div class="flex-1 min-w-0">
            <p class="text-body-sm text-white font-medium">{{ item.name.replace(/_/g, ' ') }}</p>
            <p class="text-caption text-slate-400">{{ item.status }}</p>
          </div>
          <div class="text-right shrink-0">
            <p class="text-body-sm text-white font-mono">{{ item.score }}</p>
            <p class="text-caption text-slate-500">VVV: {{ item.vvv }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed, reactive } from 'vue'

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
const kpiExplanation = (key) => {
  const map = {
    headline_mrr: 'MRR projetado mes 30 baseado em cenarios SNTI',
    headline_customers: 'Numero de clientes projetado mes 30',
    headline_month: 'Horizonte de planejamento estrategico',
    critical_vvv_items: 'Itens com VVV abaixo de 0.5 — precisam pesquisa',
    urgent_actions: 'Acoes priorizadas via FDC-U scoring',
  }
  return map[key] || 'KPI estrategico'
}

const props = defineProps({
  kpiData: { type: Object, default: null },
  validation: { type: Object, default: null },
  priorities: { type: Object, default: null },
  dashboard: { type: Object, default: null },
})

const kpiCards = computed(() => {
  if (!props.kpiData) return []
  const k = props.kpiData
  const labels = k.labels || {}
  return [
    {
      key: 'headline_mrr',
      label: labels.mrr || 'MRR',
      value: k.headline_mrr,
      tag: 'MRR Mes 30',
      tagClass: 'text-green-400',
    },
    {
      key: 'headline_customers',
      label: labels.customers || 'Clientes',
      value: k.headline_customers,
    },
    {
      key: 'headline_month',
      label: labels.month || 'Horizonte',
      value: `${k.headline_month} meses`,
    },
    {
      key: 'critical_vvv_items',
      label: labels.vvv || 'Itens VVV < 0.5',
      value: k.critical_vvv_items,
      tag: 'Criticos',
      tagClass: 'text-red-400',
    },
    {
      key: 'urgent_actions',
      label: labels.actions || 'Acoes Urgentes',
      value: k.urgent_actions,
    },
  ]
})

const confidenceBadges = computed(() => {
  if (!props.validation?.confidence_badges) return []
  const badges = props.validation.confidence_badges
  const labelMap = {
    swot: 'SWOT',
    market: 'Mercado',
    competitive: 'Competitivo',
    financial: 'Financeiro',
    legal: 'Juridico',
    overall: 'Geral',
  }
  return Object.entries(badges).map(([key, value]) => {
    const barClass =
      value >= 0.8 ? 'bg-green-500' : value >= 0.6 ? 'bg-yellow-500' : 'bg-red-500'
    const textClass =
      value >= 0.8 ? 'text-green-400' : value >= 0.6 ? 'text-yellow-400' : 'text-red-400'
    return { label: labelMap[key] || key, value, barClass, textClass }
  })
})

const lowVvvItems = computed(() => {
  return props.validation?.low_vvv_items || []
})

const fdcuTop = computed(() => {
  return props.priorities?.fdcu?.top_critical || []
})

const priorityClass = (priority) => {
  if (priority === 'CRITICA') return 'bg-red-900/50 text-red-400'
  if (priority === 'ALTA') return 'bg-yellow-900/50 text-yellow-400'
  return 'bg-slate-700 text-slate-300'
}
</script>
