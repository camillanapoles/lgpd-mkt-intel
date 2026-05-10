<template>
  <div class="competitive-view">
    <div class="flex items-center justify-between mb-6">
      <h2 class="text-h2 text-white">Cenario Competitivo</h2>
    </div>

    <div class="flex items-center gap-2 mb-4">
      <span class="text-caption px-2 py-0.5 rounded bg-slate-700/60 text-slate-300 border border-slate-600">
        Visao Global
      </span>
      <span class="text-caption text-slate-500 italic">
        (este componente exibe dados consolidados — nao filtra por publico-alvo)
      </span>
    </div>

    <div class="space-y-4 mb-6">
      <div
        v-for="(comp, key) in competitive.landscape"
        :key="key"
        :class="[
          'rounded-card border-2 p-5',
          comp.status?.includes('THREAT') ? 'border-red-900/50 bg-red-950/10' :
          comp.status?.includes('POTENTIAL') ? 'border-yellow-900/50 bg-yellow-950/10' :
          'border-slate-700 bg-slate-800/50',
        ]"
      >
        <div class="flex items-start justify-between mb-3">
          <div class="flex items-center gap-2">
            <div>
              <h3 class="text-h4 text-white capitalize">{{ key }}</h3>
              <span
                :class="[
                  'text-caption px-2 py-0.5 rounded',
                  statusClass(comp.status),
                ]"
              >
                {{ comp.status }}
              </span>
            </div>
            <button
              @click.stop="toggleInfo(key)"
              class="shrink-0 w-5 h-5 flex items-center justify-center rounded-full text-xs transition-colors"
              :class="expandedInfo.has(key) ? 'bg-accent-600 text-white' : 'bg-slate-700 text-slate-400 hover:bg-slate-600'"
              title="Ver fonte e detalhes"
            >i</button>
          </div>
          <span v-if="comp.timing" class="text-caption text-slate-400">Timeline: {{ comp.timing }}</span>
        </div>

        <div v-if="expandedInfo.has(key)" class="space-y-1 border-t border-slate-700/50 mb-3 pt-1.5">
          <p class="text-caption text-slate-400">Status: {{ comp.status || 'Nao classificado' }} | Impacto: {{ comp.impact || 'Nao avaliado' }}</p>
          <div v-if="comp.timing" class="text-caption text-slate-500">Timeline: {{ comp.timing }}</div>
        </div>

        <div v-if="comp.pricing" class="mb-3">
          <p class="text-caption text-slate-400 mb-1">Pricing</p>
          <div class="flex flex-wrap gap-2">
            <span
              v-for="(price, tier) in comp.pricing"
              :key="tier"
              class="text-caption bg-slate-700/50 px-2 py-1 rounded text-slate-300"
            >
              {{ tier }}: {{ price }}
            </span>
          </div>
        </div>

        <div v-if="comp.gaps" class="mb-3">
          <p class="text-caption text-slate-400 mb-1">Gaps do Competidor</p>
          <div class="flex flex-wrap gap-2">
            <span
              v-for="gap in comp.gaps"
              :key="gap"
              class="text-caption bg-green-900/20 text-green-400 px-2 py-1 rounded"
            >
              {{ gap }}
            </span>
          </div>
        </div>

        <div v-if="comp.estrategia_ict" class="p-3 rounded-lg bg-accent-950/20 border border-accent-900/30">
          <p class="text-caption text-accent-400 font-medium mb-2">Nossa Estrategia</p>
          <div class="grid md:grid-cols-2 gap-2">
            <div v-for="(val, k) in comp.estrategia_ict" :key="k">
              <p class="text-caption text-slate-400">{{ faseLabel(k) }}</p>
              <p class="text-body-sm text-white">{{ val }}</p>
            </div>
          </div>
        </div>

        <div v-if="comp.impact" class="mt-2">
          <span class="text-caption text-slate-400">Impacto: </span>
          <span class="text-caption text-yellow-400">{{ comp.impact }}</span>
        </div>
      </div>
    </div>

    <div v-if="competitive.differentiation?.ict_vs_neogov" class="bg-slate-800/50 border border-slate-700 rounded-card p-5 mb-4">
      <h3 class="text-h4 text-white mb-3">ICT vs NeoGov</h3>
      <div class="grid md:grid-cols-3 gap-3">
        <div
          v-for="(val, dim) in competitive.differentiation.ict_vs_neogov"
          :key="dim"
          class="p-3 rounded-lg bg-black/20"
        >
          <p class="text-caption text-accent-400 capitalize mb-1">{{ dim }}</p>
          <p class="text-body-sm text-white">{{ val }}</p>
        </div>
      </div>
    </div>

    <div v-if="competitive.whitespace" class="bg-slate-800/50 border border-slate-700 rounded-card p-5">
      <h3 class="text-h4 text-white mb-3">Espacos em Branco</h3>
      <div class="grid md:grid-cols-2 gap-2">
        <div
          v-for="space in competitive.whitespace"
          :key="space"
          class="flex items-start gap-2 p-3 rounded-lg bg-accent-950/10"
        >
          <span class="text-accent-400 shrink-0">&#9671;</span>
          <p class="text-body-sm text-slate-300">{{ space }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive } from 'vue'

const props = defineProps({
  competitive: { type: Object, default: () => ({}) },
})

const expandedInfo = reactive(new Set())

const toggleInfo = (key) => {
  expandedInfo.has(key) ? expandedInfo.delete(key) : expandedInfo.add(key)
}

const statusClass = (status) => {
  if (status?.includes('THREAT')) return 'bg-red-900/50 text-red-400'
  if (status?.includes('POTENTIAL')) return 'bg-yellow-900/50 text-yellow-400'
  return 'bg-slate-700 text-slate-300'
}

const faseLabel = (k) => {
  const labels = { fase_1: 'Fase 1', fase_2: 'Fase 2', fase_3: 'Fase 3', diferencial: 'Diferencial' }
  return labels[k] || k.replace(/_/g, ' ')
}
</script>
