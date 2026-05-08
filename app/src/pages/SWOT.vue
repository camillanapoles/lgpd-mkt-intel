<template>
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
    <!-- Header -->
    <div class="mb-8">
      <h1 class="font-display text-3xl font-bold text-slate-900">Análise SWOT</h1>
      <p class="text-slate-600 mt-2">Forças, Fraquezas, Oportunidades e Ameaças</p>
    </div>

    <!-- SWOT Grid -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
      <!-- Strengths -->
      <div class="card p-6 border-t-4 border-green-500">
        <div class="flex items-center gap-3 mb-4">
          <div class="w-10 h-10 rounded-lg bg-green-100 flex items-center justify-center">
            <svg class="w-6 h-6 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
          </div>
          <div>
            <h2 class="font-display text-lg font-semibold text-green-800">STRENGTHS</h2>
            <p class="text-sm text-green-600">Pontos Fortes Internos</p>
          </div>
        </div>
        <div class="space-y-3">
          <div v-for="item in swot.strengths" :key="item.id" class="p-3 bg-green-50 rounded-lg">
            <div class="flex items-start justify-between gap-2">
              <div class="flex-1">
                <span class="font-mono text-xs text-green-600 font-bold">{{ item.id }}</span>
                <p class="text-sm text-slate-700 mt-1">{{ item.text }}</p>
              </div>
              <span :class="`badge ${getImpactBadgeClass(item.impact)}`">{{ item.impact }}</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Weaknesses -->
      <div class="card p-6 border-t-4 border-red-500">
        <div class="flex items-center gap-3 mb-4">
          <div class="w-10 h-10 rounded-lg bg-red-100 flex items-center justify-center">
            <svg class="w-6 h-6 text-red-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
            </svg>
          </div>
          <div>
            <h2 class="font-display text-lg font-semibold text-red-800">WEAKNESSES</h2>
            <p class="text-sm text-red-600">Fraquezas Internas</p>
          </div>
        </div>
        <div class="space-y-3">
          <div v-for="item in swot.weaknesses" :key="item.id" class="p-3 bg-red-50 rounded-lg">
            <div class="flex items-start justify-between gap-2">
              <div class="flex-1">
                <span class="font-mono text-xs text-red-600 font-bold">{{ item.id }}</span>
                <p class="text-sm text-slate-700 mt-1">{{ item.text }}</p>
                <p class="text-xs text-slate-500 mt-1"><strong>Mitigação:</strong> {{ item.mitigation }}</p>
              </div>
              <span :class="`badge ${getImpactBadgeClass(item.impact)}`">{{ item.impact }}</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Opportunities -->
      <div class="card p-6 border-t-4 border-blue-500">
        <div class="flex items-center gap-3 mb-4">
          <div class="w-10 h-10 rounded-lg bg-blue-100 flex items-center justify-center">
            <svg class="w-6 h-6 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
            </svg>
          </div>
          <div>
            <h2 class="font-display text-lg font-semibold text-blue-800">OPPORTUNITIES</h2>
            <p class="text-sm text-blue-600">Oportunidades Externas</p>
          </div>
        </div>
        <div class="space-y-3">
          <div v-for="item in swot.opportunities" :key="item.id" class="p-3 bg-blue-50 rounded-lg">
            <div class="flex items-start justify-between gap-2">
              <div class="flex-1">
                <span class="font-mono text-xs text-blue-600 font-bold">{{ item.id }}</span>
                <p class="text-sm text-slate-700 mt-1">{{ item.text }}</p>
                <p class="text-xs text-blue-600 mt-1"><strong>Timing:</strong> {{ item.timing }}</p>
              </div>
              <span :class="`badge ${getImpactBadgeClass(item.impact)}`">{{ item.impact }}</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Threats -->
      <div class="card p-6 border-t-4 border-amber-500">
        <div class="flex items-center gap-3 mb-4">
          <div class="w-10 h-10 rounded-lg bg-amber-100 flex items-center justify-center">
            <svg class="w-6 h-6 text-amber-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
          </div>
          <div>
            <h2 class="font-display text-lg font-semibold text-amber-800">THREATS</h2>
            <p class="text-sm text-amber-600">Ameaças Externas</p>
          </div>
        </div>
        <div class="space-y-3">
          <div v-for="item in swot.threats" :key="item.id" class="p-3 bg-amber-50 rounded-lg">
            <div class="flex items-start justify-between gap-2">
              <div class="flex-1">
                <span class="font-mono text-xs text-amber-600 font-bold">{{ item.id }}</span>
                <p class="text-sm text-slate-700 mt-1">{{ item.text }}</p>
                <p class="text-xs text-amber-600 mt-1"><strong>Mitigação:</strong> {{ item.mitigation }}</p>
              </div>
              <span :class="`badge ${getProbabilityBadgeClass(item.probability)}`">{{ item.probability }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Strategic Summary -->
    <div class="card p-6">
      <h3 class="font-display text-lg font-semibold text-slate-900 mb-4">Resumo Estratégico</h3>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div class="p-4 bg-green-50 rounded-lg border border-green-200">
          <h4 class="font-medium text-green-800 mb-2">Forças Estratégicas</h4>
          <p class="text-sm text-slate-700">
            <strong>S1 + S2 =</strong> Gap de mercado + Arbitragem regulatória = Defesa contra entrada
          </p>
        </div>
        <div class="p-4 bg-red-50 rounded-lg border border-red-200">
          <h4 class="font-medium text-red-800 mb-2">Risco Crítico</h4>
          <p class="text-sm text-slate-700">
            <strong>W1 + T4 =</strong> Sales municipal + ciclo longo = <strong>MUST resolver pré-commitment</strong>
          </p>
        </div>
        <div class="p-4 bg-blue-50 rounded-lg border border-blue-200">
          <h4 class="font-medium text-blue-800 mb-2">Aposta Principal</h4>
          <p class="text-sm text-slate-700">
            <strong>O1 + O2 =</strong> ANPD + TCE = Demanda forçada mantém janela aberta 3-5 anos
          </p>
        </div>
        <div class="p-4 bg-purple-50 rounded-lg border border-purple-200">
          <h4 class="font-medium text-purple-800 mb-2">Unfair Advantage</h4>
          <p class="text-sm text-slate-700">
            <strong>S4 + S5 =</strong> Data 100% Brasil + DPO incluído = Barreira à entrada (alto custo fixo)
          </p>
        </div>
      </div>
    </div>

    <!-- Action Items -->
    <div class="mt-6 card p-6">
      <h3 class="font-display text-lg font-semibold text-slate-900 mb-4">Ações Imediatas</h3>
      <div class="space-y-3">
        <div class="flex items-start gap-3 p-3 bg-red-50 rounded-lg border border-red-200">
          <span class="badge badge-danger mt-0.5">CRÍTICO</span>
          <div>
            <p class="font-medium text-slate-900">Resolver W1: Experiência em vendas municipais</p>
            <p class="text-sm text-slate-600">Co-founder ou advisor com track record comprovado</p>
          </div>
        </div>
        <div class="flex items-start gap-3 p-3 bg-amber-50 rounded-lg border border-amber-200">
          <span class="badge badge-warning mt-0.5">URGENTE</span>
          <div>
            <p class="font-medium text-slate-900">Mitigar T4: Ciclo de vendas longo</p>
            <p class="text-sm text-slate-600">Foco em municípios com flags do TCE (urgência)</p>
          </div>
        </div>
        <div class="flex items-start gap-3 p-3 bg-blue-50 rounded-lg border border-blue-200">
          <span class="badge badge-info mt-0.5">OPORTUNIDADE</span>
          <div>
            <p class="font-medium text-slate-900">Capturar O1 + O2: Demanda ANPD/TCE</p>
            <p class="text-sm text-slate-600">Conteúdo de marketing focado em fiscalização e multas</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import strategicData from '../data/strategicData.js'

const swot = ref(strategicData.swot)

const getImpactBadgeClass = (impact) => {
  const classes = {
    'ALTO': 'badge-danger',
    'MÉDIO': 'badge-warning',
    'BAIXO': 'badge-success'
  }
  return classes[impact] || 'badge-info'
}

const getProbabilityBadgeClass = (probability) => {
  const classes = {
    'ALTA': 'badge-danger',
    'MÉDIA': 'badge-warning',
    'BAIXA': 'badge-success'
  }
  return classes[probability] || 'badge-info'
}
</script>
