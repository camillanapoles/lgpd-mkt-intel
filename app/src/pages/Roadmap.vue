<template>
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
    <!-- Header -->
    <div class="mb-8">
      <h1 class="font-display text-3xl font-bold text-slate-900">Roadmap de Implementação</h1>
      <p class="text-slate-600 mt-2">Cronograma faseado com 6 fases ate Série A</p>
      <div class="flex items-center gap-3 mt-3">
        <span class="badge badge-info">Fase atual: {{ currentPhaseName }}</span>
        <span class="text-sm text-slate-500">Total: R$ 2.31M | 36 meses</span>
      </div>
    </div>

    <!-- Current Sprints -->
    <div class="mb-8">
      <h2 class="font-display text-xl font-semibold text-slate-900 mb-4">Sprints Atuais</h2>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        <div
          v-for="sprint in roadmap.sprints"
          :key="sprint.sprint"
          class="card p-4"
          :class="{ 'ring-2 ring-primary-400': isCurrentSprint(sprint) }"
        >
          <div class="flex items-center justify-between mb-2">
            <span class="text-sm font-bold text-primary-600">Sprint {{ sprint.sprint }}</span>
            <span class="text-xs text-slate-500">{{ sprint.periodo }}</span>
          </div>
          <p class="text-sm text-slate-700 font-medium">{{ sprint.foco }}</p>
          <div class="mt-2 flex items-center gap-1.5">
            <svg class="w-3.5 h-3.5 text-amber-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 21v-4m0 0V5a2 2 0 012-2h6.5l1 1H21l-3 6 3 6h-8.5l-1-1H5a2 2 0 00-2 2z" />
            </svg>
            <span class="text-xs text-amber-700">{{ sprint.marco }}</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Timeline Phases -->
    <div class="mb-8">
      <h2 class="font-display text-xl font-semibold text-slate-900 mb-4">Timeline por Fase</h2>
      <div class="space-y-0">
        <div
          v-for="(phase, key, index) in roadmap.timeline"
          :key="key"
          class="relative pl-10 pb-8 border-l-2"
          :class="phaseBorderColor(phase.status)"
        >
          <!-- Timeline Dot -->
          <div
            class="absolute -left-3.5 top-0 w-7 h-7 rounded-full flex items-center justify-center text-xs font-bold border-2"
            :class="phaseDotClass(phase.status)"
          >
            {{ index + 1 }}
          </div>

          <!-- Phase Card -->
          <div class="card p-6" :class="{ 'ring-2 ring-blue-300': phase.status === 'in_progress' }">
            <!-- Phase Header -->
            <div class="flex flex-col md:flex-row md:items-start md:justify-between gap-3 mb-4">
              <div>
                <div class="flex items-center gap-3 flex-wrap">
                  <h3 class="font-display text-lg font-semibold text-slate-900">{{ phase.nome }}</h3>
                  <span class="badge" :class="statusBadgeClass(phase.status)">{{ statusLabel(phase.status) }}</span>
                  <span class="badge badge-info">{{ phase.periodo }}</span>
                  <span
                    v-if="isCriticalPath(phase.nome)"
                    class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-xs font-medium bg-red-100 text-red-800"
                  >
                    <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20">
                      <path fill-rule="evenodd" d="M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z" clip-rule="evenodd" />
                    </svg>
                    Caminho Critico
                  </span>
                </div>
                <p class="text-slate-600 mt-1 text-sm">{{ phase.objetivo }}</p>
              </div>
              <div class="flex items-center gap-2 text-sm text-slate-600 md:text-right flex-shrink-0">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                </svg>
                {{ phase.responsible }}
              </div>
            </div>

            <!-- KPIs -->
            <div>
              <p class="text-sm font-medium text-slate-700 mb-2">KPIs:</p>
              <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-2">
                <div v-for="kpi in phase.kpi" :key="kpi" class="flex items-center gap-2 text-sm text-slate-600">
                  <svg
                    class="w-4 h-4 flex-shrink-0"
                    :class="phase.status === 'completed' ? 'text-green-500' : phase.status === 'in_progress' ? 'text-blue-500' : 'text-slate-400'"
                    fill="none" stroke="currentColor" viewBox="0 0 24 24"
                  >
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                  </svg>
                  {{ kpi }}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Milestones -->
    <div class="mb-8">
      <h2 class="font-display text-xl font-semibold text-slate-900 mb-4">Milestones</h2>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div
          v-for="ms in roadmap.milestones"
          :key="ms.evento"
          class="card p-4 flex items-start gap-4"
          :class="{ 'border-red-300 bg-red-50/30': ms.critical }"
        >
          <!-- Date -->
          <div class="flex-shrink-0 text-center min-w-[4.5rem]">
            <p class="text-xs text-slate-500 uppercase tracking-wide">Data</p>
            <p class="text-sm font-bold text-slate-900 mt-0.5">{{ formatDate(ms.data) }}</p>
          </div>

          <!-- Divider -->
          <div class="flex-shrink-0 w-px bg-slate-200 self-stretch"></div>

          <!-- Content -->
          <div class="flex-1 min-w-0">
            <div class="flex items-center gap-2 flex-wrap">
              <p class="font-medium text-slate-900">{{ ms.evento }}</p>
              <span v-if="ms.critical" class="inline-flex items-center gap-1 px-1.5 py-0.5 rounded text-xs font-medium bg-red-100 text-red-700">
                Critico
              </span>
              <span v-if="isCriticalPathMilestone(ms.evento)" class="inline-flex items-center gap-1 px-1.5 py-0.5 rounded text-xs font-medium bg-amber-100 text-amber-700">
                Caminho Critico
              </span>
            </div>
            <p class="text-sm text-slate-500 mt-0.5">
              <span class="font-medium">Resp.:</span> {{ ms.responsible }}
            </p>
          </div>
        </div>
      </div>
    </div>

    <!-- Critical Path -->
    <div class="mb-8">
      <h2 class="font-display text-xl font-semibold text-slate-900 mb-4">Caminho Critico</h2>
      <div class="card p-6">
        <div class="flex items-center gap-2 flex-wrap">
          <template v-for="(step, idx) in roadmap.criticalPath" :key="step">
            <div class="flex items-center gap-2 px-3 py-2 bg-red-50 border border-red-200 rounded-lg">
              <span class="flex items-center justify-center w-6 h-6 rounded-full bg-red-600 text-white text-xs font-bold">{{ idx + 1 }}</span>
              <span class="text-sm font-medium text-red-900">{{ step }}</span>
            </div>
            <svg v-if="idx < roadmap.criticalPath.length - 1" class="w-5 h-5 text-red-400 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
            </svg>
          </template>
        </div>
      </div>
    </div>

    <!-- Summary Stats -->
    <div class="grid grid-cols-1 md:grid-cols-4 gap-4">
      <div class="card p-4 text-center">
        <p class="text-sm text-slate-500">Fases</p>
        <p class="text-2xl font-bold text-slate-900">6</p>
      </div>
      <div class="card p-4 text-center">
        <p class="text-sm text-slate-500">Duracao Total</p>
        <p class="text-2xl font-bold text-slate-900">36 meses</p>
      </div>
      <div class="card p-4 text-center">
        <p class="text-sm text-slate-500">Milestones Criticos</p>
        <p class="text-2xl font-bold text-red-600">{{ criticalMilestonesCount }}</p>
      </div>
      <div class="card p-4 text-center">
        <p class="text-sm text-slate-500">Sprint Atual</p>
        <p class="text-2xl font-bold text-primary-600">{{ currentSprintLabel }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import strategicData from '../data/strategicData.js'

const roadmap = strategicData.roadmap

const currentPhaseName = computed(() => {
  const phases = Object.values(roadmap.timeline)
  const current = phases.find(p => p.status === 'in_progress')
  return current ? current.nome : '-'
})

const criticalMilestonesCount = computed(() =>
  roadmap.milestones.filter(ms => ms.critical).length
)

const currentSprintLabel = computed(() => {
  if (roadmap.sprints.length === 0) return '-'
  return `${roadmap.sprints[0].sprint}`
})

function isCurrentSprint(sprint) {
  return sprint.sprint === 1
}

function isCriticalPath(phaseNome) {
  return roadmap.criticalPath.some(cp => cp.toLowerCase().includes(phaseNome.toLowerCase().split(' ')[0].toLowerCase()))
}

function isCriticalPathMilestone(evento) {
  return roadmap.criticalPath.includes(evento)
}

function phaseBorderColor(status) {
  if (status === 'in_progress') return 'border-blue-400'
  if (status === 'completed') return 'border-green-400'
  return 'border-slate-200'
}

function phaseDotClass(status) {
  if (status === 'in_progress') return 'bg-blue-500 text-white border-blue-300 animate-pulse'
  if (status === 'completed') return 'bg-green-500 text-white border-green-300'
  return 'bg-slate-300 text-slate-600 border-slate-200'
}

function statusBadgeClass(status) {
  if (status === 'in_progress') return 'bg-blue-100 text-blue-800'
  if (status === 'completed') return 'bg-green-100 text-green-800'
  return 'bg-slate-100 text-slate-600'
}

function statusLabel(status) {
  if (status === 'in_progress') return 'Em andamento'
  if (status === 'completed') return 'Concluido'
  return 'Pendente'
}

function formatDate(dateStr) {
  const [year, month, day] = dateStr.split('-')
  return `${day}/${month}/${year}`
}
</script>
