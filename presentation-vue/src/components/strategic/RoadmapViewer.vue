<template>
  <div class="roadmap-viewer">
    <div class="flex items-center justify-between mb-6">
      <h2 class="text-h2 text-white">Roadmap Estrategico</h2>
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

    <div class="flex items-center gap-2 mb-4">
      <span class="text-caption px-2 py-0.5 rounded bg-slate-700/60 text-slate-300 border border-slate-600">
        Visao Global
      </span>
      <span class="text-caption text-slate-500 italic">
        (este componente exibe dados consolidados — nao filtra por publico-alvo)
      </span>
    </div>

    <div v-if="activeView === 'timeline'">
      <div class="relative">
        <div
          v-for="(fase, key, index) in roadmap.timeline"
          :key="key"
          class="relative pl-10 pb-8 last:pb-0"
          :class="{ 'border-l-2 border-slate-700': index < phaseCount - 1 }"
        >
          <div
            :class="[
              'absolute -left-3 top-0 w-6 h-6 rounded-full flex items-center justify-center border-2',
              phaseDotClass(fase.status),
            ]"
          >
            <span class="text-caption">{{ phaseIcon(fase.status) }}</span>
          </div>

          <div
            :class="[
              'rounded-card border p-5 transition-all',
              activePhase === key ? 'border-accent-500 bg-accent-950/20' : 'border-slate-700 bg-slate-800/50 hover:border-slate-500',
            ]"
            @click="activePhase = key"
          >
            <div class="flex items-start justify-between mb-2">
              <div>
                <h3 class="text-h4 text-white">{{ fase.nome }}</h3>
                <p class="text-body-sm text-slate-400">{{ fase.periodo }}</p>
              </div>
              <div class="flex items-center gap-1.5">
                <span
                  :class="[
                    'text-caption px-2 py-0.5 rounded',
                    statusBadgeClass(fase.status),
                  ]"
                >
                  {{ statusLabel(fase.status) }}
                </span>
                <button
                  @click.stop="toggleInfo(`phase-${key}`)"
                  class="w-5 h-5 flex items-center justify-center rounded-full text-xs transition-colors"
                  :class="expandedInfo.has(`phase-${key}`) ? 'bg-accent-600 text-white' : 'bg-slate-700 text-slate-400 hover:bg-slate-600'"
                  title="Ver detalhes"
                >i</button>
              </div>
            </div>
            <div v-if="expandedInfo.has(`phase-${key}`)" class="border-t border-slate-700/50 mt-2 pt-2 mb-2 space-y-1">
              <p class="text-caption text-slate-400">Status: {{ statusLabel(fase.status) }} — {{ fase.periodo }}</p>
              <p class="text-caption text-slate-400">Responsavel: {{ fase.responsible }}</p>
              <p v-if="fase.kpi?.length" class="text-caption text-slate-500">KPIs: {{ fase.kpi.length }} indicadores</p>
            </div>

            <p class="text-body-sm text-slate-300 mb-3">{{ fase.objetivo }}</p>

            <div class="flex flex-wrap gap-2 mb-2">
              <span
                v-for="kpi in fase.kpi"
                :key="kpi"
                class="text-caption bg-slate-700/50 px-2 py-1 rounded text-slate-300"
              >
                {{ kpi }}
              </span>
            </div>

            <p class="text-caption text-slate-500">Responsavel: {{ fase.responsible }}</p>
          </div>
        </div>
      </div>
    </div>

    <div v-else-if="activeView === 'milestones'">
      <div class="space-y-3">
        <div
          v-for="ms in roadmap.milestones"
          :key="ms.data"
          :class="[
            'flex items-center gap-4 p-4 rounded-card border transition-all',
            ms.critical ? 'border-red-900/50 bg-red-950/20' : 'border-slate-700 bg-slate-800/50',
          ]"
        >
          <div class="text-center shrink-0">
            <p class="text-body-sm text-white font-bold">{{ formatDate(ms.data) }}</p>
            <p class="text-caption text-slate-500">{{ getDay(ms.data) }}</p>
          </div>
          <div class="flex-1 min-w-0">
            <p class="text-body-sm text-white">{{ ms.evento }}</p>
            <p class="text-caption text-slate-500">{{ ms.responsible }}</p>
            <div v-if="expandedInfo.has(`ms-${ms.data}`)" class="border-t border-slate-700/50 mt-1 pt-1">
              <p class="text-caption text-slate-400">Data: {{ ms.data }} — {{ ms.critical ? 'Marco critico' : 'Marco regular' }}</p>
              <p v-if="ms.responsible" class="text-caption text-slate-500">Responsavel: {{ ms.responsible }}</p>
            </div>
          </div>
          <span
            v-if="ms.critical"
            class="text-caption bg-red-900/50 text-red-400 px-2 py-0.5 rounded shrink-0"
          >
            Critico
          </span>
          <button
            @click.stop="toggleInfo(`ms-${ms.data}`)"
            class="shrink-0 w-5 h-5 flex items-center justify-center rounded-full text-xs transition-colors"
            :class="expandedInfo.has(`ms-${ms.data}`) ? 'bg-accent-600 text-white' : 'bg-slate-700 text-slate-400 hover:bg-slate-600'"
            title="Ver detalhes"
          >i</button>
        </div>
      </div>
    </div>

    <div v-else-if="activeView === 'sprints'">
      <div class="grid md:grid-cols-2 gap-4">
        <div
          v-for="sprint in roadmap.sprints"
          :key="sprint.sprint"
          class="bg-slate-800/50 border border-slate-700 rounded-card p-5"
        >
          <div class="flex items-center justify-between mb-3">
            <div class="flex items-center gap-2">
              <h3 class="text-h4 text-white">Sprint {{ sprint.sprint }}</h3>
              <button
                @click.stop="toggleInfo(`sprint-${sprint.sprint}`)"
                class="w-5 h-5 flex items-center justify-center rounded-full text-xs transition-colors"
                :class="expandedInfo.has(`sprint-${sprint.sprint}`) ? 'bg-accent-600 text-white' : 'bg-slate-700 text-slate-400 hover:bg-slate-600'"
                title="Ver detalhes"
              >i</button>
            </div>
            <span class="text-caption text-slate-400">{{ sprint.periodo }}</span>
          </div>
          <p class="text-body-sm text-slate-300 mb-2">Foco: {{ sprint.foco }}</p>
          <div class="pt-2 border-t border-slate-700">
            <p class="text-caption text-slate-400">
              Marco: <span class="text-accent-400">{{ sprint.marco }}</span>
            </p>
          </div>
          <div v-if="expandedInfo.has(`sprint-${sprint.sprint}`)" class="mt-2 pt-2 border-t border-slate-700/50">
            <p class="text-caption text-slate-400">Periodo: {{ sprint.periodo }}</p>
            <p class="text-caption text-slate-500">Sprint orientado por OKRs e marco-fim definido</p>
          </div>
        </div>
      </div>
    </div>

    <div v-if="roadmap.criticalPath" class="mt-6 p-4 rounded-card bg-slate-800/30 border border-slate-700">
      <h3 class="text-h4 text-white mb-2">Caminho Critico</h3>
      <div class="flex flex-wrap gap-2">
        <template v-for="(step, i) in roadmap.criticalPath" :key="step">
          <span class="text-body-sm text-white bg-slate-700 px-3 py-1 rounded-lg">{{ step }}</span>
          <span v-if="i < roadmap.criticalPath.length - 1" class="text-slate-500 flex items-center">&rarr;</span>
        </template>
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

const props = defineProps({
  roadmap: { type: Object, required: true },
})

const activeView = ref('timeline')
const activePhase = ref(null)

const views = [
  { id: 'timeline', label: 'Fases' },
  { id: 'milestones', label: 'Milestones' },
  { id: 'sprints', label: 'Sprints' },
]

const phaseCount = computed(() => Object.keys(props.roadmap.timeline || {}).length)

const phaseDotClass = (status) => ({
  'bg-green-500 border-green-400': status === 'in_progress',
  'bg-slate-600 border-slate-500': status === 'pending',
  'bg-blue-500 border-blue-400': status === 'completed',
})

const phaseIcon = (status) => {
  if (status === 'in_progress') return '▶'
  if (status === 'completed') return '✓'
  return '○'
}

const statusBadgeClass = (status) => ({
  'bg-green-900/50 text-green-400': status === 'in_progress',
  'bg-slate-700 text-slate-400': status === 'pending',
  'bg-blue-900/50 text-blue-400': status === 'completed',
})

const statusLabel = (status) => {
  const labels = { in_progress: 'Em andamento', pending: 'Pendente', completed: 'Concluido' }
  return labels[status] || status
}

const formatDate = (dateStr) => {
  const [y, m, d] = dateStr.split('-')
  return `${d}/${m}`
}

const getDay = (dateStr) => {
  const days = ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab']
  const date = new Date(dateStr + 'T12:00:00')
  return days[date.getDay()]
}
</script>
