<template>
  <div class="macro-analysis">
    <div class="flex items-center justify-between mb-6">
      <h2 class="text-h2 text-white">Analise Macro Ambiente</h2>
      <div class="flex gap-2">
        <button
          v-for="view in views"
          :key="view.id"
          @click="activeView = view.id"
          :class="[
            'px-3 py-1.5 rounded-lg text-caption transition-all',
            activeView === view.id ? 'bg-accent-600 text-white' : 'bg-slate-700 text-slate-300 hover:bg-slate-600',
          ]"
        >
          {{ view.label }}
        </button>
      </div>
    </div>

    <div v-if="activeView === 'pestle'">
      <div class="grid md:grid-cols-2 gap-4">
        <div
          v-for="(factors, category) in pestle"
          :key="category"
          class="bg-slate-800/50 border border-slate-700 rounded-card p-5"
        >
          <div class="flex items-center gap-3 mb-4">
            <span class="text-2xl">{{ categoryIcon(category) }}</span>
            <div>
              <h3 class="text-h4 text-white capitalize">{{ categoryLabel(category) }}</h3>
              <span class="text-caption text-slate-400">{{ categorySubtitle(category) }}</span>
            </div>
          </div>

          <div class="space-y-4">
            <div
              v-for="(factor, key) in factors"
              :key="key"
              class="p-3 rounded-lg bg-black/20 hover:bg-black/30 transition-colors"
            >
              <div class="flex items-start justify-between mb-2">
                <p class="text-body-sm text-white flex-1">{{ factor.fato }}</p>
              </div>
              <div class="flex items-center gap-2 mb-2">
                <span
                  :class="[
                    'text-caption px-2 py-0.5 rounded',
                    impactClass(factor.impacto),
                  ]"
                >
                  {{ factor.impacto }}
                </span>
                <span class="text-caption text-slate-500">VVV: {{ factor.vvv.toFixed(2) }}</span>
              </div>
              <div class="flex items-center gap-2">
                <div class="flex-1 h-1.5 bg-black/30 rounded-full overflow-hidden">
                  <div
                    class="h-full rounded-full transition-all duration-500"
                    :class="vvvBarClass(factor.vvv)"
                    :style="{ width: `${factor.vvv * 100}%` }"
                  />
                </div>
              </div>
              <p class="text-caption text-slate-500 mt-1">Fonte: {{ factor.fonte }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div v-else-if="activeView === 'porter'">
      <div class="space-y-4">
        <div
          v-for="(force, key) in porter"
          :key="key"
          class="bg-slate-800/50 border border-slate-700 rounded-card p-5"
        >
          <div class="flex items-start justify-between mb-3">
            <div>
              <h3 class="text-h4 text-white">{{ porterTitle(key) }}</h3>
              <div class="flex items-center gap-2 mt-1">
                <span class="text-caption text-slate-400">Rating:</span>
                <div class="flex gap-0.5">
                  <div
                    v-for="i in 5"
                    :key="i"
                    :class="[
                      'w-6 h-2 rounded-sm',
                      i <= force.rating ? 'bg-accent-500' : 'bg-slate-700',
                    ]"
                  />
                </div>
                <span class="text-caption font-bold" :class="porterColor(force.rating)">
                  {{ force.label }}
                </span>
              </div>
            </div>
            <span class="text-caption text-slate-400">VVV: {{ force.vvv.toFixed(2) }}</span>
          </div>

          <p class="text-body-sm text-slate-300 mb-3">{{ force.justification }}</p>

          <div class="p-3 rounded-lg bg-accent-950/20 border border-accent-900/30">
            <p class="text-caption text-accent-400 font-medium mb-1">Implicacao Estrategica</p>
            <p class="text-body-sm text-white">{{ force.strategic_implication }}</p>
          </div>
        </div>
      </div>
    </div>

    <div v-else-if="activeView === 'scorecard'">
      <div class="bg-slate-800/50 border border-slate-700 rounded-card p-5 mb-4">
        <div class="flex items-center justify-between mb-4">
          <h3 class="text-h4 text-white">Market Attractiveness Scorecard</h3>
          <div class="text-right">
            <p class="text-display text-accent-400">{{ scorecard.overall_score }}</p>
            <p class="text-caption text-accent-400 font-bold">{{ scorecard.label }}</p>
          </div>
        </div>

        <div class="space-y-3">
          <div
            v-for="factor in scorecard.factors"
            :key="factor.factor"
            class="flex items-center gap-4"
          >
            <span class="text-body-sm text-slate-300 w-48 shrink-0">{{ factor.factor }}</span>
            <div class="flex-1 h-3 bg-slate-700 rounded-full overflow-hidden">
              <div
                class="h-full rounded-full transition-all duration-700"
                :class="scoreBarClass(factor.score)"
                :style="{ width: `${(factor.score / 10) * 100}%` }"
              />
            </div>
            <span class="text-body-sm text-white font-mono w-8 text-right">{{ factor.score }}/10</span>
            <span class="text-caption text-slate-500 w-12 text-right">{{ (factor.weight * 100).toFixed(0) }}%</span>
            <span class="text-body-sm text-white font-mono w-10 text-right">{{ factor.weighted.toFixed(1) }}</span>
          </div>
        </div>

        <div class="mt-4 pt-4 border-t border-slate-700">
          <p class="text-caption text-slate-400 mb-2">Janela de Oportunidade</p>
          <div class="flex items-center gap-4">
            <span class="text-body-sm text-white">{{ scorecard.entry_timeline.window_opportunity }}</span>
            <span class="text-slate-600">&rarr;</span>
            <span class="text-body-sm text-accent-400">{{ scorecard.entry_timeline.recommendation }}</span>
          </div>
        </div>
      </div>

      <div v-if="scorecard.critical_success_factors" class="bg-slate-800/50 border border-slate-700 rounded-card p-5">
        <h3 class="text-h4 text-white mb-3">Fatores Criticos de Sucesso</h3>
        <div class="grid md:grid-cols-2 gap-2">
          <div
            v-for="csf in scorecard.critical_success_factors"
            :key="csf"
            class="flex items-start gap-2 p-2 rounded-lg bg-black/20"
          >
            <span class="text-accent-400 shrink-0 mt-0.5">&#9670;</span>
            <p class="text-body-sm text-slate-300">{{ csf }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const props = defineProps({
  pestle: { type: Object, default: () => ({}) },
  porter: { type: Object, default: () => ({}) },
  scorecard: { type: Object, default: () => ({}) },
})

const activeView = ref('pestle')

const views = [
  { id: 'pestle', label: 'PESTLE' },
  { id: 'porter', label: "Porter's 5" },
  { id: 'scorecard', label: 'Scorecard' },
]

const categoryIcon = (cat) => {
  const icons = { political: '🏛', economic: '💰', social: '👥', technological: '⚡', legal: '⚖', environmental: '🌱' }
  return icons[cat] || '📊'
}

const categoryLabel = (cat) => {
  const labels = { political: 'Politico', economic: 'Economico', social: 'Social', technological: 'Tecnologico', legal: 'Legal', environmental: 'Ambiental' }
  return labels[cat] || cat
}

const categorySubtitle = (cat) => {
  const subs = { political: 'Regulacao e governanca', economic: 'Mercado e financiamento', social: 'Demanda e cultura', technological: 'Infraestrutura e inovacao', legal: 'Legislacao e compliance', environmental: 'Sustentabilidade' }
  return subs[cat] || ''
}

const porterTitle = (key) => {
  const titles = {
    threat_new_entrants: 'Ameaca de Novos Entrantes',
    bargaining_power_suppliers: 'Poder de Negociacao - Fornecedores',
    bargaining_power_buyers: 'Poder de Negociacao - Compradores',
    threat_substitutes: 'Ameaca de Substitutos',
    competitive_rivalry: 'Rivalidade Competitiva',
  }
  return titles[key] || key.replace(/_/g, ' ')
}

const impactClass = (impact) => {
  if (impact?.includes('Critico')) return 'bg-red-900/50 text-red-400'
  if (impact?.includes('Alto')) return 'bg-yellow-900/50 text-yellow-400'
  if (impact?.includes('Medio')) return 'bg-blue-900/50 text-blue-400'
  return 'bg-slate-700 text-slate-300'
}

const vvvBarClass = (vvv) => {
  if (vvv >= 0.9) return 'bg-green-500'
  if (vvv >= 0.8) return 'bg-green-400'
  if (vvv >= 0.6) return 'bg-yellow-500'
  return 'bg-red-500'
}

const porterColor = (rating) => {
  if (rating >= 4) return 'text-red-400'
  if (rating >= 3) return 'text-yellow-400'
  return 'text-green-400'
}

const scoreBarClass = (score) => {
  if (score >= 9) return 'bg-green-500'
  if (score >= 7) return 'bg-green-400'
  if (score >= 5) return 'bg-yellow-500'
  return 'bg-red-500'
}
</script>
