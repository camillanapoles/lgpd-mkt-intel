<template>
  <div>
    <div class="flex items-center justify-between mb-6">
      <h2 class="text-h2 text-white">Status da Pesquisa</h2>
      <span class="text-caption text-slate-400">
        {{ stats.concluido }}/{{ stats.total }} CONCLUIDO ({{ stats.pct }}%)
      </span>
    </div>

    <div class="flex items-center gap-2 mb-4">
      <span class="text-caption px-2 py-0.5 rounded bg-slate-700/60 text-slate-300 border border-slate-600">
        Visao Global
      </span>
      <span class="text-caption text-slate-500 italic">
        (este componente exibe dados consolidados — nao filtra por publico-alvo)
      </span>
    </div>

    <!-- PROGRESS BAR -->
    <div class="bg-slate-800/50 border border-slate-700 rounded-card p-4 mb-6">
      <div class="flex items-center justify-between mb-2">
        <span class="text-caption text-slate-300">Progresso Geral</span>
        <span class="text-caption font-bold" :class="stats.pct >= 80 ? 'text-green-400' : stats.pct >= 50 ? 'text-yellow-400' : 'text-red-400'">
          {{ stats.pct }}%
        </span>
      </div>
      <div class="h-3 bg-slate-700 rounded-full overflow-hidden">
        <div
          class="h-full rounded-full transition-all duration-700"
          :class="stats.pct >= 80 ? 'bg-green-500' : stats.pct >= 50 ? 'bg-yellow-500' : 'bg-red-500'"
          :style="{ width: `${stats.pct}%` }"
        />
      </div>
      <div class="flex gap-4 mt-3 text-caption text-slate-400">
        <span class="flex items-center gap-1">
          <span class="w-2 h-2 rounded-full bg-green-500" />
          Validado: {{ stats.validado }}
        </span>
        <span class="flex items-center gap-1">
          <span class="w-2 h-2 rounded-full bg-blue-500" />
          Concluido: {{ stats.concluido - stats.validado }}
        </span>
        <span class="flex items-center gap-1">
          <span class="w-2 h-2 rounded-full bg-yellow-500" />
          Pesquisando: {{ stats.pesquisando }}
        </span>
      </div>
    </div>

    <!-- FILTERS -->
    <div class="flex gap-2 mb-6">
      <button
        v-for="f in filters"
        :key="f.value"
        @click="filter = f.value"
        :class="[
          'px-3 py-1.5 rounded-lg text-caption transition-all',
          filter === f.value ? 'bg-accent-600 text-white' : 'bg-slate-800 text-slate-300 hover:bg-slate-700',
        ]"
      >
        {{ f.label }} <span class="text-slate-400">({{ f.count }})</span>
      </button>
    </div>

    <!-- ITEMS BY DIMENSION -->
    <div v-for="(dim, dk) in props.snti.dimensions" :key="dk" class="mb-6">
      <h3 class="text-h4 text-white mb-3">{{ dim.label }}</h3>
      <div class="grid gap-2">
        <div
          v-for="item in dimensionFilteredItems(dk)"
          :key="item.id"
          class="bg-slate-800/50 border border-slate-700 rounded-lg p-4"
        >
          <div class="flex items-start justify-between gap-3">
            <div class="flex-1 min-w-0">
              <div class="flex items-center gap-2 mb-1">
                <span class="text-body-sm text-white">{{ item.description }}</span>
                <span class="text-caption font-bold shrink-0" :class="fdcClass(item.funcao_fdc)">
                  {{ item.funcao_fdc }}
                </span>
                <button
                  @click.stop="toggleInfo(`status-${item.id}`)"
                  class="shrink-0 w-5 h-5 flex items-center justify-center rounded-full text-xs transition-colors"
                  :class="expandedInfo.has(`status-${item.id}`) ? 'bg-accent-600 text-white' : 'bg-slate-700 text-slate-400 hover:bg-slate-600'"
                  title="Ver detalhes"
                >i</button>
              </div>
              <p v-if="item.fonte" class="text-caption text-slate-500 truncate" :title="item.fonte">
                {{ item.fonte }}
              </p>
              <div v-if="expandedInfo.has(`status-${item.id}`)" class="mt-2 pt-2 border-t border-slate-700/50 space-y-1">
                <p class="text-caption text-slate-400">VVV: {{ (item.vvv || 0).toFixed(2) }} — {{ vvvExplanation(item.vvv || 0) }}</p>
                <p class="text-caption text-slate-400">Status: {{ item.fonte_status || 'PESQUISANDO' }} — Funcao FDC-U: {{ item.funcao_fdc }}</p>
                <p v-if="item.fonte" class="text-caption text-accent-400 break-all">Fonte: {{ item.fonte }}</p>
                <p v-if="item.proxima_revisao" class="text-caption text-slate-500">Proxima revisao: {{ item.proxima_revisao }}</p>
              </div>
            </div>
            <div class="flex items-center gap-3 shrink-0">
              <!-- VVV BAR -->
              <div class="w-16">
                <div class="h-2 bg-slate-700 rounded-full overflow-hidden">
                  <div
                    class="h-full rounded-full"
                    :class="vvvBarClass(item.vvv)"
                    :style="{ width: `${(item.vvv || 0) * 100}%` }"
                  />
                </div>
                <p class="text-caption text-slate-400 text-center mt-0.5">{{ (item.vvv || 0).toFixed(2) }}</p>
              </div>
              <!-- STATUS BADGE -->
              <span
                class="px-2 py-0.5 rounded text-caption font-bold"
                :class="statusBadgeClass(item.fonte_status)"
              >
                {{ item.fonte_status || 'PESQUISANDO' }}
              </span>
            </div>
          </div>
        </div>
        <p v-if="dimensionFilteredItems(dk).length === 0" class="text-caption text-slate-500 italic p-2">
          Nenhum item com filtro selecionado.
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, reactive } from 'vue'

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

const props = defineProps({
  snti: { type: Object, required: true }
})

const filter = ref('ALL')

const allItems = computed(() => {
  const items = []
  for (const [dk, dv] of Object.entries(props.snti.dimensions || {})) {
    for (const item of (dv.items || [])) {
      items.push({ ...item, dimKey: dk, dimLabel: dv.label })
    }
  }
  return items
})

const filteredItems = computed(() => {
  if (filter.value === 'ALL') return allItems.value
  return allItems.value.filter(i => (i.fonte_status || 'PESQUISANDO') === filter.value)
})

const stats = computed(() => {
  const items = allItems.value
  const total = items.length
  if (total === 0) return { total: 0, concluido: 0, pesquisando: 0, validado: 0, pct: 0 }
  const conc = items.filter(i => ['CONCLUÍDO', 'VALIDADO'].includes(i.fonte_status)).length
  const pesq = items.filter(i => !i.fonte_status || i.fonte_status === 'PESQUISANDO').length
  const val = items.filter(i => i.fonte_status === 'VALIDADO').length
  return { total, concluido: conc, pesquisando: pesq, validado: val, pct: Math.round(conc / total * 100) }
})

const filters = computed(() => [
  { value: 'ALL', label: 'Todos', count: stats.value.total },
  { value: 'PESQUISANDO', label: 'Pesquisando', count: stats.value.pesquisando },
  { value: 'CONCLUÍDO', label: 'Concluido', count: stats.value.concluido - stats.value.validado },
  { value: 'VALIDADO', label: 'Validado', count: stats.value.validado },
])

function dimensionFilteredItems(dimKey) {
  return filteredItems.value.filter(i => i.dimKey === dimKey)
}

function statusBadgeClass(status) {
  const s = status || 'PESQUISANDO'
  if (s === 'VALIDADO') return 'bg-green-900/50 text-green-400 border border-green-700'
  if (s === 'CONCLUÍDO') return 'bg-blue-900/50 text-blue-400 border border-blue-700'
  return 'bg-yellow-900/50 text-yellow-400 border border-yellow-700'
}

function vvvBarClass(vvv) {
  const v = vvv || 0
  if (v >= 0.8) return 'bg-green-500'
  if (v >= 0.6) return 'bg-yellow-500'
  return 'bg-red-500'
}

function fdcClass(fn) {
  if (fn === '+') return 'text-green-400'
  if (fn === '-') return 'text-red-400'
  return 'text-slate-400'
}
</script>
