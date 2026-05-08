<template>
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
    <!-- Header -->
    <div class="mb-8">
      <h1 class="font-display text-3xl font-bold text-slate-900">Roadmap de Implementação</h1>
      <p class="text-slate-600 mt-2">Cronograma faseado até Product-Market Fit</p>
    </div>

    <!-- Timeline -->
    <div class="relative">
      <!-- Progress Bar -->
      <div class="mb-8">
        <div class="flex justify-between text-sm text-slate-600 mb-2">
          <span>Progresso até PMF</span>
          <span>Total: R$ 960K | 24 meses</span>
        </div>
        <div class="w-full bg-slate-200 rounded-full h-3">
          <div class="bg-gradient-to-r from-primary-500 to-primary-700 h-3 rounded-full relative" style="width: 0%">
            <div class="absolute inset-0 bg-white/20 animate-pulse"></div>
          </div>
        </div>
      </div>

      <!-- Phases -->
      <div class="space-y-6">
        <div
          v-for="(phase, index) in phases"
          :key="phase.name"
          class="relative pl-8 pb-8 border-l-2"
          :class="getPhaseBorderColor(index)"
        >
          <!-- Timeline Dot -->
          <div class="absolute -left-3 top-0 w-6 h-6 rounded-full flex items-center justify-center text-xs font-bold"
               :class="getPhaseDotClass(index)">
            {{ index + 1 }}
          </div>

          <!-- Phase Card -->
          <div class="card p-6">
            <div class="flex flex-col md:flex-row md:items-center md:justify-between gap-4 mb-4">
              <div>
                <div class="flex items-center gap-3">
                  <h3 class="font-display text-xl font-semibold text-slate-900">{{ phase.name }}</h3>
                  <span :class="`badge ${getPhaseBadgeClass(index)}`">{{ phase.months }}</span>
                </div>
                <p class="text-slate-600 mt-1">{{ phase.description }}</p>
              </div>
              <div class="text-right">
                <p class="text-sm text-slate-500">Investimento</p>
                <p class="text-2xl font-bold text-primary-600">{{ formatCurrency(phase.investment) }}</p>
                <p class="text-xs text-slate-500">Burn: {{ formatCurrency(phase.burn) }}/mês</p>
              </div>
            </div>

            <!-- Milestone -->
            <div class="p-4 bg-primary-50 rounded-lg mb-4">
              <div class="flex items-center gap-2">
                <svg class="w-5 h-5 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
                <span class="font-medium text-primary-900">Milestone:</span>
                <span class="text-primary-700">{{ phase.milestone }}</span>
              </div>
            </div>

            <!-- KPIs -->
            <div>
              <p class="text-sm font-medium text-slate-700 mb-2">KPIs da Fase:</p>
              <div class="grid grid-cols-1 md:grid-cols-3 gap-2">
                <div v-for="kpi in phase.kpis" :key="kpi" class="flex items-center gap-2 text-sm text-slate-600">
                  <svg class="w-4 h-4 text-green-500 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                  </svg>
                  {{ kpi }}
                </div>
              </div>
            </div>

            <!-- Dependencies -->
            <div v-if="phase.dependencies" class="mt-4 pt-4 border-t border-slate-200">
              <p class="text-sm font-medium text-slate-700 mb-2">Dependências:</p>
              <div class="flex flex-wrap gap-2">
                <span v-for="dep in phase.dependencies" :key="dep" class="px-2 py-1 bg-amber-100 text-amber-700 rounded text-xs">
                  {{ dep }}
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Summary Stats -->
    <div class="mt-8 grid grid-cols-1 md:grid-cols-4 gap-4">
      <div class="card p-4 text-center">
        <p class="text-sm text-slate-500">Investimento Total</p>
        <p class="text-2xl font-bold text-slate-900">R$ 960K</p>
      </div>
      <div class="card p-4 text-center">
        <p class="text-sm text-slate-500">Duração Total</p>
        <p class="text-2xl font-bold text-slate-900">24 meses</p>
      </div>
      <div class="card p-4 text-center">
        <p class="text-sm text-slate-500">Break-even Estimado</p>
        <p class="text-2xl font-bold text-slate-900">Mês 30-36</p>
      </div>
      <div class="card p-4 text-center">
        <p class="text-sm text-slate-500">Clientes no PMF</p>
        <p class="text-2xl font-bold text-slate-900">50</p>
      </div>
    </div>

    <!-- Risk Timeline -->
    <div class="mt-8 card p-6">
      <h3 class="font-display font-semibold text-slate-900 mb-4">Análise de Risco por Fase</h3>
      <div class="space-y-4">
        <div class="flex items-center gap-4">
          <span class="w-24 text-sm font-medium text-slate-600">Validação</span>
          <div class="flex-1 bg-slate-200 rounded-full h-4 overflow-hidden">
            <div class="bg-green-500 h-4 rounded-full" style="width: 30%"></div>
          </div>
          <span class="text-sm text-slate-600">Baixo risco</span>
        </div>
        <div class="flex items-center gap-4">
          <span class="w-24 text-sm font-medium text-slate-600">MVP</span>
          <div class="flex-1 bg-slate-200 rounded-full h-4 overflow-hidden">
            <div class="bg-amber-500 h-4 rounded-full" style="width: 55%"></div>
          </div>
          <span class="text-sm text-slate-600">Médio risco</span>
        </div>
        <div class="flex items-center gap-4">
          <span class="w-24 text-sm font-medium text-slate-600">PMF</span>
          <div class="flex-1 bg-slate-200 rounded-full h-4 overflow-hidden">
            <div class="bg-red-500 h-4 rounded-full" style="width: 75%"></div>
          </div>
          <span class="text-sm text-slate-600">Alto risco (burn)</span>
        </div>
        <div class="flex items-center gap-4">
          <span class="w-24 text-sm font-medium text-slate-600">Scale</span>
          <div class="flex-1 bg-slate-200 rounded-full h-4 overflow-hidden">
            <div class="bg-green-500 h-4 rounded-full" style="width: 40%"></div>
          </div>
          <span class="text-sm text-slate-600">Risco mitigado</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import strategicData from '../data/strategicData.js'

const phases = ref([
  {
    name: 'Fase 0 - Validação',
    months: 'Meses 1-3',
    investment: strategicData.roadmap.phase0.investment,
    burn: strategicData.roadmap.phase0.burn,
    description: 'Validação de tese com prospects qualificados',
    milestone: strategicData.roadmap.phase0.milestone,
    kpis: strategicData.roadmap.phase0.kpis,
    dependencies: ['Deck investidor pronto', 'Lista de prospects TCE-flagged']
  },
  {
    name: 'Fase 1 - MVP',
    months: 'Meses 4-6',
    investment: strategicData.roadmap.phase1.investment,
    burn: strategicData.roadmap.phase1.burn,
    description: 'Desenvolvimento MVP e primeiros clientes',
    milestone: strategicData.roadmap.phase1.milestone,
    kpis: strategicData.roadmap.phase1.kpis,
    dependencies: ['3 LOIs assinados', 'Time técnico completo']
  },
  {
    name: 'Fase 2 - PMF',
    months: 'Meses 7-15',
    investment: strategicData.roadmap.phase2.investment,
    burn: strategicData.roadmap.phase2.burn,
    description: 'Escala go-to-market e otimização unit economics',
    milestone: strategicData.roadmap.phase2.milestone,
    kpis: strategicData.roadmap.phase2.kpis,
    dependencies: ['Product-Market Fit', 'CAC provado < R$3K']
  },
  {
    name: 'Fase 3 - Scale',
    months: 'Meses 16-24',
    investment: strategicData.roadmap.phase3.investment,
    burn: strategicData.roadmap.phase3.burn,
    description: 'Expansão agressiva e novos segmentos',
    milestone: strategicData.roadmap.phase3.milestone,
    kpis: strategicData.roadmap.phase3.kpis,
    dependencies: ['Unit economics provados', 'Série A pronta']
  }
])

const getPhaseBorderColor = (index) => {
  const colors = ['border-blue-200', 'border-green-200', 'border-amber-200', 'border-purple-200']
  return colors[index] || 'border-slate-200'
}

const getPhaseDotClass = (index) => {
  const colors = ['bg-blue-500 text-white', 'bg-green-500 text-white', 'bg-amber-500 text-white', 'bg-purple-500 text-white']
  return colors[index] || 'bg-slate-500 text-white'
}

const getPhaseBadgeClass = (index) => {
  const classes = ['badge-info', 'badge-success', 'badge-warning', 'badge-primary']
  return classes[index] || 'badge-info'
}

const formatCurrency = (value) => {
  return new Intl.NumberFormat('pt-BR', {
    style: 'currency',
    currency: 'BRL',
    minimumFractionDigits: 0,
    maximumFractionDigits: 0
  }).format(value)
}
</script>

<style scoped>
.badge-primary {
  @apply bg-purple-100 text-purple-800;
}
</style>
