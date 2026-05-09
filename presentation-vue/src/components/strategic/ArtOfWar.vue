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
      <div v-if="hasOverrides" class="mt-3 p-2 rounded-lg bg-accent-950/30 border border-accent-900/40">
        <p class="text-caption text-accent-400 font-bold">WHAT-IF ATIVO - Cenario Simulado</p>
        <p class="text-caption text-slate-400">Override VVV aplicado em {{ overrideCount }} item(ns)</p>
      </div>
    </div>

    <!-- 5 DIMENSOES -->
    <div class="grid gap-3 mb-6">
      <!-- ALERTAS POR DIMENSAO -->
      <div
        v-for="(dim, key) in dimensions"
        :key="key"
        :class="[
          'bg-slate-800/50 border rounded-card p-4',
          dimScore(key) < 40 ? 'border-red-500/60' : dimScore(key) < 60 ? 'border-yellow-500/40' : 'border-slate-700',
        ]"
      >
        <!-- DIMENSION ALERT -->
        <div v-if="dimScore(key) < 60" class="mb-3 p-2 rounded-lg" :class="dimScore(key) < 40 ? 'bg-red-950/30 border border-red-900/50' : 'bg-yellow-950/20 border border-yellow-900/30'">
          <p :class="['text-caption font-bold', dimScore(key) < 40 ? 'text-red-400' : 'text-yellow-400']">
            {{ dimScore(key) < 40 ? 'NAO ATACAR' : 'CAUTELA' }} - {{ dim.label.split(' - ')[0] }} {{ dimScore(key) < 40 ? 'CRITICO' : 'precisa atencao' }}
          </p>
          <p v-if="dimAlertAction(key)" class="text-caption text-slate-300 mt-1">Acao: {{ dimAlertAction(key) }}</p>
        </div>
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
            v-for="rawItem in dim.items"
            :key="rawItem.id"
            :class="[
              'rounded-lg text-caption',
              resolveItem(rawItem, key).polaridade === 1 ? 'bg-green-950/20' : 'bg-red-950/20',
              scenarioOverrides[key + ':' + rawItem.id] ? 'ring-1 ring-accent-500/50' : '',
            ]"
          >
            <div class="flex items-center gap-2 p-2">
              <span :class="resolveItem(rawItem, key).polaridade === 1 ? 'text-green-400' : 'text-red-400'">
                {{ resolveItem(rawItem, key).polaridade === 1 ? '+' : '-' }}{{ (resolveItem(rawItem, key).vvv * resolveItem(rawItem, key).fator).toFixed(1) }}
              </span>
              <span class="text-slate-300 truncate flex-1">{{ resolveItem(rawItem, key).description }}</span>
              <button
                @click="toggleInfo(key, rawItem.id)"
                class="shrink-0 w-5 h-5 flex items-center justify-center rounded-full text-xs transition-colors"
                :class="expandedItems.has(`${key}:${rawItem.id}`) ? 'bg-accent-600 text-white' : 'bg-slate-700 text-slate-400 hover:bg-slate-600'"
                :title="expandedItems.has(`${key}:${rawItem.id}`) ? 'Fechar info' : 'Ver fonte e detalhes'"
              >i</button>
            </div>
            <div
              v-if="expandedItems.has(`${key}:${rawItem.id}`)"
              class="px-2 pb-2 space-y-1 border-t border-slate-700/50 mt-0 pt-1.5"
            >
              <p class="text-slate-400">{{ resolveItem(rawItem, key).explicacao || rawItem.description }}</p>
              <div class="flex items-center gap-2 flex-wrap">
                <span class="text-slate-500">Fonte:</span>
                <span class="text-accent-400 text-xs">{{ resolveItem(rawItem, key).fonte || 'Nao mapeada' }}</span>
              </div>
              <div class="flex items-center gap-2">
                <span class="text-slate-500">Status:</span>
                <span
                  :class="[
                    'px-1.5 py-0.5 rounded text-xs font-bold',
                    resolveItem(rawItem, key).fonte_status === 'VALIDADO' ? 'bg-green-900/50 text-green-400' :
                    resolveItem(rawItem, key).fonte_status === 'CONCLUÍDO' ? 'bg-blue-900/50 text-blue-400' :
                    'bg-yellow-900/50 text-yellow-400'
                  ]"
                >{{ resolveItem(rawItem, key).fonte_status || 'PESQUISANDO' }}</span>
                <span class="text-slate-500">VVV:{{ resolveItem(rawItem, key).vvv.toFixed(2) }}</span>
                <span class="text-slate-500">Peso:{{ resolveItem(rawItem, key).fator }}</span>
              </div>
              <div v-if="resolveItem(rawItem, key).vvv_updated" class="text-xs text-slate-600">
                Atualizado: {{ resolveItem(rawItem, key).vvv_updated }}
              </div>
            </div>
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
import { ref, computed, reactive } from 'vue'

const props = defineProps({
  snti: { type: Object, required: true },
  scenarioOverrides: { type: Object, default: () => ({}) },
})

const activeAudience = ref(props.snti.audiences?.[0]?.id || '')
const expandedItems = reactive(new Set())
const toggleInfo = (dimKey, itemId) => {
  const key = `${dimKey}:${itemId}`
  expandedItems.has(key) ? expandedItems.delete(key) : expandedItems.add(key)
}

const resolveItem = (item, dimKey) => {
  const key = `${dimKey}:${item.id}`
  const override = props.scenarioOverrides[key]
  if (!override) return item
  return {
    ...item,
    vvv: override.vvv ?? item.vvv,
    fator: override.fator ?? item.fator,
    polaridade: override.polaridade ?? item.polaridade,
    description: override.description ?? item.description,
  }
}

const dimensions = computed(() => props.snti.dimensions || {})

const dimScore = (key) => {
  const dim = dimensions.value[key]
  if (!dim) return 0
  const items = (dim.items || []).map(i => resolveItem(i, key))
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

const overrideKeys = computed(() => Object.keys(props.scenarioOverrides || {}))
const hasOverrides = computed(() => overrideKeys.value.length > 0)
const overrideCount = computed(() => overrideKeys.value.length)

const dimAlertAction = (dimKey) => {
  const score = dimScore(dimKey)
  if (score >= 60) return null
  const alerts = props.snti.decision_rules?.alerts || []
  const match = alerts.find(a => a.dimension === dimKey && score < a.threshold)
  return match?.action || null
}
</script>
