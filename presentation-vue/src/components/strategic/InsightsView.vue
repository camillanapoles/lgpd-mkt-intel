<template>
  <div class="space-y-6">
    <div>
      <h2 class="text-2xl font-bold text-white mb-1">Insights Estratégicos</h2>
      <p class="text-sm text-slate-400">
        Fatos de mercado validados, gaps a investigar e ações prioritárias para 30/60/90 dias.
      </p>
    </div>

    <!-- Hero: 3 insights chave -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-3">
      <div v-for="(f, i) in heroFacts" :key="f.id"
        class="bg-gradient-to-br from-slate-900 to-slate-800 border border-slate-700 rounded-xl p-4">
        <div class="flex items-center justify-between mb-2">
          <span class="text-xs font-mono text-blue-400">{{ f.id }}</span>
          <span class="text-[10px] uppercase font-bold px-1.5 py-0.5 rounded bg-green-900/60 text-green-400">
            VVV {{ f.vvv?.toFixed?.(2) }}
          </span>
        </div>
        <p class="text-sm text-white font-medium mb-2 leading-snug">{{ f.fact }}</p>
        <p class="text-xs text-emerald-400 italic">→ {{ f.impact }}</p>
        <p v-if="f.source" class="text-[10px] text-slate-500 mt-2 truncate" :title="f.source">
          Fonte: {{ f.source }}
        </p>
      </div>
    </div>

    <!-- Fatos confirmados completos -->
    <div class="bg-slate-900/40 border border-slate-700 rounded-2xl p-5">
      <h3 class="text-lg font-semibold text-white mb-3">📋 Fatos confirmados de mercado ({{ marketFacts.length }})</h3>
      <div class="space-y-2">
        <div v-for="f in marketFacts" :key="f.id"
          class="bg-slate-950/60 border border-slate-800 rounded-lg p-3 hover:border-slate-600 transition">
          <div class="flex items-start gap-3">
            <span class="text-xs font-mono text-blue-400 mt-0.5 shrink-0">{{ f.id }}</span>
            <div class="flex-1">
              <p class="text-sm text-slate-200 mb-1">{{ f.fact }}</p>
              <p class="text-xs text-emerald-400 italic mb-1">→ {{ f.impact }}</p>
              <div class="flex items-center gap-3 text-[10px] text-slate-500">
                <span>VVV {{ f.vvv?.toFixed?.(2) }}</span>
                <a v-if="f.url" :href="f.url" target="_blank" class="text-blue-400 hover:underline truncate max-w-[300px]">
                  🔗 {{ f.url }}
                </a>
                <span v-else>Fonte: {{ f.source }}</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Action plan 30/60/90 -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-3">
      <div v-for="(actions, period) in actionPlan" :key="period"
        class="bg-slate-900/40 border border-slate-700 rounded-2xl p-4">
        <h3 class="text-base font-bold text-white mb-3 flex items-center gap-2">
          <span class="text-blue-400">{{ periodLabel(period) }}</span>
          <span class="text-xs text-slate-500 font-normal">({{ actions.length }} ações)</span>
        </h3>
        <ul class="space-y-2">
          <li v-for="(a, i) in actions" :key="i"
            class="text-xs text-slate-300 flex items-start gap-2">
            <span class="text-blue-500 mt-0.5">▸</span>
            <span :class="a.includes('[CRÍTICO]') ? 'text-red-300 font-medium' : ''">{{ a }}</span>
          </li>
        </ul>
      </div>
    </div>

    <!-- Gaps a validar -->
    <div class="bg-slate-900/40 border border-yellow-700/30 rounded-2xl p-5">
      <h3 class="text-lg font-semibold text-yellow-400 mb-3">⚠ Gaps a validar ({{ gaps.length }})</h3>
      <div class="space-y-2">
        <div v-for="g in gaps" :key="g.id"
          :class="['border rounded-lg p-3 text-xs',
            g.classification === 'CRÍTICO' ? 'border-red-700/50 bg-red-950/20' :
            g.classification === 'ROBUSTO' ? 'border-yellow-700/50 bg-yellow-950/10' :
            'border-slate-700 bg-slate-900/40']">
          <div class="flex items-start justify-between gap-3 mb-1">
            <div class="flex items-center gap-2">
              <span class="font-mono text-slate-400">{{ g.id }}</span>
              <span :class="['text-[10px] uppercase font-bold px-1.5 py-0.5 rounded',
                g.classification === 'CRÍTICO' ? 'bg-red-900/60 text-red-300' :
                g.classification === 'ROBUSTO' ? 'bg-yellow-900/60 text-yellow-300' :
                'bg-slate-700 text-slate-300']">{{ g.classification }}</span>
            </div>
            <span v-if="g.responsible" class="text-slate-400 text-[10px]">resp: {{ g.responsible }}</span>
          </div>
          <p class="text-slate-200">{{ g.description }}</p>
          <p class="text-emerald-400 italic mt-1">→ {{ g.action_required }}</p>
          <div class="text-[10px] text-slate-500 mt-1">
            VVV atual {{ g.vvv_score?.toFixed?.(2) ?? '—' }}
            <span v-if="g.deadline" class="ml-2">· Deadline: {{ g.deadline }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  market_facts: { type: Array, default: () => [] },
  action_plan: { type: Object, default: () => ({}) },
  vvv_gaps: { type: Array, default: () => [] }
})

const marketFacts = computed(() => props.market_facts)
const heroFacts = computed(() => marketFacts.value.slice(0, 3))
const actionPlan = computed(() => ({
  days_30: props.action_plan.days_30 || [],
  days_60: props.action_plan.days_60 || [],
  days_90: props.action_plan.days_90 || []
}))
const gaps = computed(() => props.vvv_gaps)

const periodLabel = (p) => ({ days_30: '30 dias', days_60: '60 dias', days_90: '90 dias' })[p] || p
</script>
