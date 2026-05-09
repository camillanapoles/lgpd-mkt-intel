<template>
  <div class="art-of-war">
    <div class="flex items-center justify-between mb-6">
      <h2 class="text-h2 text-white">Arte da Guerra - Motor de Decisao</h2>
      <div class="flex items-center gap-3">
        <span class="text-caption text-slate-400">Sun Tzu + Teoria dos Jogos</span>
      </div>
    </div>

    <!-- SCORE GLOBAL -->
    <div class="bg-slate-800/50 border-2 rounded-card p-6 mb-6 text-center" :class="scoreBorderClass">
      <p class="text-caption text-slate-400 mb-1">PRONTIDAO ESTRATEGICA</p>
      <p class="text-display font-bold" :class="scoreTextClass">{{ globalScore.toFixed(1) }}</p>
      <p class="text-h4 mt-1" :class="scoreTextClass">{{ actionLabel }}</p>
      <p class="text-body-sm text-slate-400 mt-2">{{ actionDescription }}</p>
    </div>

    <!-- 5 DIMENSOES -->
    <div class="grid gap-3 mb-6">
      <div
        v-for="(dim, key) in dimensions"
        :key="key"
        class="bg-slate-800/50 border border-slate-700 rounded-card p-4"
      >
        <div class="flex items-center justify-between mb-2">
          <div class="flex items-center gap-3">
            <span class="text-2xl">{{ dimIcon(key) }}</span>
            <div>
              <h3 class="text-h4 text-white">{{ dim.label }}</h3>
              <p class="text-caption text-slate-500 italic">"{{ dim.sun_tzu }}"</p>
            </div>
          </div>
          <div class="text-right">
            <p class="text-h3 font-bold" :class="dimScoreClass(key)">{{ dimScore(key).toFixed(1) }}</p>
            <p class="text-caption text-slate-400">peso: {{ (dim.weight * 100).toFixed(0) }}%</p>
          </div>
        </div>
        <div class="h-3 bg-slate-700 rounded-full overflow-hidden mb-3">
          <div
            class="h-full rounded-full transition-all duration-700"
            :class="dimBarClass(key)"
            :style="{ width: `${Math.max(0, dimScore(key))}%` }"
          />
        </div>
        <div class="grid grid-cols-2 gap-2">
          <div
            v-for="item in dim.items"
            :key="item.id"
            :class="[
              'flex items-center gap-2 p-2 rounded-lg text-caption',
              item.polaridade === 1 ? 'bg-green-950/20' : 'bg-red-950/20',
            ]"
          >
            <span :class="item.polaridade === 1 ? 'text-green-400' : 'text-red-400'">
              {{ item.polaridade === 1 ? '+' : '-' }}{{ (item.vvv * item.fator).toFixed(1) }}
            </span>
            <span class="text-slate-300 truncate flex-1">{{ item.description }}</span>
            <span class="text-slate-500 shrink-0">VVV:{{ item.vvv }}</span>
          </div>
        </div>
      </div>
    </div>

    <!-- AUDIENCIAS -->
    <div class="mb-6">
      <h3 class="text-h3 text-white mb-4">Estrategia por Publico-Alvo</h3>
      <div class="flex gap-2 mb-3 overflow-x-auto">
        <button
          v-for="aud in snti.audiences"
          :key="aud.id"
          @click="activeAudience = aud.id"
          :class="[
            'px-3 py-2 rounded-lg text-caption whitespace-nowrap transition-all border',
            activeAudience === aud.id ? 'bg-accent-600 text-white border-accent-500' : 'bg-slate-800 text-slate-300 border-slate-700 hover:border-slate-500',
          ]"
        >
          {{ aud.icon }} {{ aud.label }}
        </button>
      </div>

      <div v-if="activeAud" class="space-y-4">
        <!-- Persona -->
        <div class="bg-slate-800/50 border border-slate-700 rounded-card p-5">
          <h4 class="text-h4 text-white mb-3">{{ activeAud.icon }} {{ activeAud.persona.titulo }}</h4>
          <div class="grid md:grid-cols-2 gap-4">
            <div>
              <p class="text-caption text-accent-400 mb-1">Perfil</p>
              <p class="text-body-sm text-slate-300">{{ activeAud.persona.perfil }}</p>
            </div>
            <div>
              <p class="text-caption text-accent-400 mb-1">Lei Aplicavel</p>
              <p class="text-body-sm text-slate-300">{{ activeAud.persona.lei_aplicavel }}</p>
            </div>
            <div>
              <p class="text-caption text-red-400 mb-1">Risco sem Servico</p>
              <p class="text-body-sm text-slate-300">{{ activeAud.persona.risco_sem_servico }}</p>
            </div>
            <div>
              <p class="text-caption text-green-400 mb-1">Valor Entregue</p>
              <p class="text-body-sm text-slate-300">{{ activeAud.persona.valor_entregue }}</p>
            </div>
            <div>
              <p class="text-caption text-yellow-400 mb-1">Pain Point</p>
              <p class="text-body-sm text-slate-300">{{ activeAud.persona.pain_point }}</p>
            </div>
            <div>
              <p class="text-caption text-blue-400 mb-1">Canal Ideal</p>
              <p class="text-body-sm text-slate-300">{{ activeAud.persona.canal_ideal }}</p>
            </div>
          </div>
        </div>

        <!-- Sun Tzu Strategy -->
        <div class="bg-accent-950/20 border border-accent-900/30 rounded-card p-4">
          <p class="text-caption text-accent-400 font-medium mb-1">Estrategia Sun Tzu</p>
          <p class="text-body-sm text-white italic">"{{ activeAud.sun_tzu_strategy }}"</p>
          <div class="mt-2 space-y-1">
            <p v-for="q in activeAud.sun_tzu_quotes" :key="q" class="text-caption text-slate-400">
              &#9670; {{ q }}
            </p>
          </div>
        </div>

        <!-- Game Theory Payoff Matrix -->
        <div class="bg-slate-800/50 border border-slate-700 rounded-card p-4">
          <h4 class="text-h4 text-white mb-3">Teoria dos Jogos - Payoff Matrix</h4>
          <div class="grid grid-cols-2 gap-3">
            <div
              v-for="(scenario, skey) in activeAud.game_theory"
              :key="skey"
              class="p-3 rounded-lg bg-black/20"
            >
              <p class="text-caption text-accent-400 mb-1">{{ scenarioLabel(skey) }}</p>
              <div class="flex gap-3 mb-1">
                <span class="text-body-sm text-white">Nos: {{ scenario.nos }}</span>
                <span class="text-body-sm text-slate-400">Compet: {{ scenario.competidor }}</span>
              </div>
              <p class="text-caption text-slate-500">{{ scenario.resultado }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- OPPORTUNITY MATRIX -->
    <div class="bg-slate-800/50 border border-slate-700 rounded-card p-5">
      <h3 class="text-h4 text-white mb-3">Mapa de Oportunidades (TODOS os Cenarios)</h3>
      <div class="grid md:grid-cols-3 gap-3">
        <div
          v-for="opp in snti.opportunity_matrix.segments"
          :key="opp.id"
          :class="[
            'p-3 rounded-lg border',
            opp.prioridade === 'P0' ? 'bg-green-950/10 border-green-900/30' :
            opp.prioridade === 'P1' ? 'bg-blue-950/10 border-blue-900/30' :
            'bg-slate-800/30 border-slate-700',
          ]"
        >
          <div class="flex items-center justify-between mb-1">
            <span :class="[
              'text-caption font-bold px-1.5 py-0.5 rounded',
              opp.prioridade === 'P0' ? 'bg-green-900/50 text-green-400' :
              opp.prioridade === 'P1' ? 'bg-blue-900/50 text-blue-400' :
              'bg-slate-700 text-slate-300',
            ]">{{ opp.prioridade }}</span>
            <span class="text-caption text-slate-500">{{ opp.status }}</span>
          </div>
          <p class="text-body-sm text-white mb-1">{{ opp.label }}</p>
          <p class="text-caption text-accent-400">{{ opp.tam }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const props = defineProps({
  snti: { type: Object, required: true },
})

const activeAudience = ref(props.snti.audiences?.[0]?.id || '')

const dimensions = computed(() => props.snti.dimensions || {})

const dimScore = (key) => {
  const dim = dimensions.value[key]
  if (!dim) return 0
  const items = dim.items || []
  const totalPos = items.filter(i => i.polaridade === 1).reduce((s, i) => s + i.vvv * i.fator, 0)
  const totalNeg = items.filter(i => i.polaridade === -1).reduce((s, i) => s + i.vvv * i.fator, 0)
  const maxPos = items.filter(i => i.polaridade === 1).reduce((s, i) => s + i.fator, 0)
  if (maxPos === 0) return 0
  return ((totalPos - totalNeg) / maxPos) * 100
}

const globalScore = computed(() => {
  let score = 0
  for (const key of Object.keys(dimensions.value)) {
    score += dimScore(key) * (dimensions.value[key].weight || 0.2)
  }
  return score
})

const rules = computed(() => props.snti.decision_rules?.rules || [])

const currentRule = computed(() => {
  for (const rule of rules.value) {
    if (globalScore.value >= rule.score_min) return rule
  }
  return rules.value[rules.value.length - 1] || {}
})

const actionLabel = computed(() => currentRule.value.action || '?')
const actionDescription = computed(() => currentRule.value.description || '')

const scoreTextClass = computed(() => {
  const s = globalScore.value
  if (s >= 75) return 'text-green-400'
  if (s >= 60) return 'text-yellow-400'
  if (s >= 40) return 'text-orange-400'
  return 'text-red-400'
})

const scoreBorderClass = computed(() => {
  const s = globalScore.value
  if (s >= 75) return 'border-green-500'
  if (s >= 60) return 'border-yellow-500'
  if (s >= 40) return 'border-orange-500'
  return 'border-red-500'
})

const dimIcon = (key) => {
  const icons = { dao: '⚖', ceu: '🌙', terra: '🏔', comandante: '⚔', metodo: '📋' }
  return icons[key] || '📊'
}

const dimScoreClass = (key) => {
  const s = dimScore(key)
  if (s >= 75) return 'text-green-400'
  if (s >= 50) return 'text-yellow-400'
  return 'text-red-400'
}

const dimBarClass = (key) => {
  const s = dimScore(key)
  if (s >= 75) return 'bg-green-500'
  if (s >= 50) return 'bg-yellow-500'
  if (s >= 25) return 'bg-orange-500'
  return 'bg-red-500'
}

const activeAud = computed(() => {
  return props.snti.audiences?.find(a => a.id === activeAudience.value) || null
})

const scenarioLabel = (key) => {
  const labels = {
    nos_entramos_primeiro: 'Nos entramos primeiro',
    competidor_entra_primeiro: 'Competidor entra primeiro',
    ambos_entram: 'Ambos entram',
    ninguem_entra: 'Ninguem entra',
  }
  return labels[key] || key.replace(/_/g, ' ')
}
</script>
