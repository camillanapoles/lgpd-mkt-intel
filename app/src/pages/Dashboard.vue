<template>
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
    <!-- Header -->
    <div class="mb-8">
      <h1 class="font-display text-3xl font-bold text-slate-900">Dashboard Executivo</h1>
      <p class="text-slate-600 mt-2">Visão estratégica - Contabilizei da Privacy</p>
      <div class="flex items-center gap-2 mt-3">
        <span class="badge badge-success">GO - Pronto para validação</span>
        <span class="text-sm text-slate-500">Score estratégico: {{ data.metadata.strategicScore }}/10</span>
      </div>
    </div>

    <!-- Key Metrics -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
      <MetricCard
        label="TAM"
        :value="data.marketAnalysis.tam.label"
        :description="data.marketAnalysis.tam.description"
        :icon="ShieldIcon"
        icon-bg="bg-blue-100"
        icon-color="text-blue-600"
      />
      <MetricCard
        label="SAM"
        :value="data.marketAnalysis.sam.label"
        :description="data.marketAnalysis.sam.description"
        :icon="TargetIcon"
        icon-bg="bg-green-100"
        icon-color="text-green-600"
      />
      <MetricCard
        label="Municípios Alvo"
        :value="data.marketAnalysis.municipalities.label"
        :description="data.marketAnalysis.municipalities.description"
        :icon="BuildingIcon"
        icon-bg="bg-purple-100"
        icon-color="text-purple-600"
      />
      <MetricCard
        label="CAGR"
        :value="data.marketAnalysis.growthRate.label"
        :description="data.marketAnalysis.growthRate.description"
        :icon="TrendingUpIcon"
        icon-bg="bg-amber-100"
        icon-color="text-amber-600"
        trend="15-20%"
        trend-label="crescimento anual"
        :trend-up="true"
      />
    </div>

    <!-- Charts Row -->
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-8">
      <ChartComponent
        title="Market Size (TAM/SAM/SOM)"
        type="bar"
        :height="'280px'"
        :data="marketSizeData"
        :legend="marketSizeLegend"
      />
      <ChartComponent
        title="Unit Economics"
        type="doughnut"
        :height="'280px'"
        :data="unitEconomicsData"
        :legend="unitEconomicsLegend"
      />
    </div>

    <!-- Strategic Overview -->
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
      <!-- Investment Required -->
      <div class="card p-6">
        <h3 class="font-display font-semibold text-slate-900 mb-4">Investimento até PMF</h3>
        <p class="text-4xl font-bold text-primary-600">R$ 960K</p>
        <p class="text-sm text-slate-500 mt-2">Mês 30-36 break-even</p>
        <div class="mt-4 space-y-2">
          <div class="flex justify-between text-sm">
            <span class="text-slate-600">Validação</span>
            <span class="font-medium">R$ 90K</span>
          </div>
          <div class="w-full bg-slate-200 rounded-full h-2">
            <div class="bg-primary-600 h-2 rounded-full" style="width: 9%"></div>
          </div>
          <div class="flex justify-between text-sm">
            <span class="text-slate-600">MVP</span>
            <span class="font-medium">R$ 150K</span>
          </div>
          <div class="w-full bg-slate-200 rounded-full h-2">
            <div class="bg-primary-600 h-2 rounded-full" style="width: 16%"></div>
          </div>
          <div class="flex justify-between text-sm">
            <span class="text-slate-600">PMF</span>
            <span class="font-medium">R$ 720K</span>
          </div>
          <div class="w-full bg-slate-200 rounded-full h-2">
            <div class="bg-primary-600 h-2 rounded-full" style="width: 75%"></div>
          </div>
        </div>
      </div>

      <!-- Quick SWOT -->
      <div class="card p-6">
        <h3 class="font-display font-semibold text-slate-900 mb-4">SWOT Resumido</h3>
        <div class="grid grid-cols-2 gap-4 text-sm">
          <div>
            <p class="font-medium text-green-700 mb-1">Forças</p>
            <ul class="text-slate-600 space-y-1">
              <li>• Gap municipal</li>
              <li>• Arbitragem R$65K</li>
              <li>• DPO fractionado</li>
            </ul>
          </div>
          <div>
            <p class="font-medium text-red-700 mb-1">Fraquezas</p>
            <ul class="text-slate-600 space-y-1">
              <li>• Sem sales municipal</li>
              <li>• Marca unknown</li>
              <li>• Capital limitado</li>
            </ul>
          </div>
          <div>
            <p class="font-medium text-blue-700 mb-1">Oportunidades</p>
            <ul class="text-slate-600 space-y-1">
              <li>• ANPD ativa 2025+</li>
              <li>• TCEs fiscalizando</li>
              <li>• 4.011 greenfield</li>
            </ul>
          </div>
          <div>
            <p class="font-medium text-amber-700 mb-1">Ameaças</p>
            <ul class="text-slate-600 space-y-1">
              <li>• Inadimplência</li>
              <li>• Competição</li>
              <li>• Sales cycle longo</li>
            </ul>
          </div>
        </div>
      </div>

      <!-- Key Actions -->
      <div class="card p-6">
        <h3 class="font-display font-semibold text-slate-900 mb-4">Ações Críticas</h3>
        <div class="space-y-3">
          <div class="flex items-start gap-3">
            <span class="badge badge-danger mt-0.5">CRÍTICO</span>
            <div>
              <p class="text-sm font-medium text-slate-900">Resolver sales municipal</p>
              <p class="text-xs text-slate-500">Co-founder/advisor com track record</p>
            </div>
          </div>
          <div class="flex items-start gap-3">
            <span class="badge badge-warning mt-0.5">URGENTE</span>
            <div>
              <p class="text-sm font-medium text-slate-900">Validar com 3 LOIs</p>
              <p class="text-xs text-slate-500">Fase 1-3 meses, foco TCE-flagged</p>
            </div>
          </div>
          <div class="flex items-start gap-3">
            <span class="badge badge-info mt-0.5">IMPORTANTE</span>
            <div>
              <p class="text-sm font-medium text-slate-900">Setup DPO pool</p>
              <p class="text-xs text-slate-500">2-3 DPOs certificados iniciais</p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Revenue Model Preview -->
    <div class="mt-8 card p-6">
      <h3 class="font-display font-semibold text-slate-900 mb-4">Modelo de Receita</h3>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div class="p-4 bg-slate-50 rounded-lg">
          <p class="text-sm font-medium text-slate-600">Core</p>
          <p class="text-2xl font-bold text-slate-900 mt-1">R$ 297-997</p>
          <p class="text-xs text-slate-500 mt-1">/mês - LGPD compliance completo</p>
        </div>
        <div class="p-4 bg-primary-50 rounded-lg border-2 border-primary-200">
          <p class="text-sm font-medium text-primary-700">Plus (Recomendado)</p>
          <p class="text-2xl font-bold text-primary-900 mt-1">+R$ 800-2000</p>
          <p class="text-xs text-primary-600 mt-1">/mês - DPO fractionado + gestão incidentes</p>
        </div>
        <div class="p-4 bg-slate-50 rounded-lg">
          <p class="text-sm font-medium text-slate-600">Premium</p>
          <p class="text-2xl font-bold text-slate-900 mt-1">+R$ 500-1000</p>
          <p class="text-xs text-slate-500 mt-1">/mês - ISO roadmap + consultoria</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import strategicData from '../data/strategicData.js'
import MetricCard from '../components/MetricCard.vue'
import ChartComponent from '../components/ChartComponent.vue'

const data = ref(strategicData)

// Icons as simple SVG components
const ShieldIcon = {
  template: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>'
}
const TargetIcon = {
  template: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>'
}
const BuildingIcon = {
  template: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 21h18M5 21V7l8-4 8 4v14M8 21v-2a2 2 0 012-2h4a2 2 0 012 2v2"/></svg>'
}
const TrendingUpIcon = {
  template: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/><polyline points="17 6 23 6 23 12"/></svg>'
}

const marketSizeData = computed(() => ({
  labels: ['TAM', 'SAM', 'SOM (5 anos)'],
  datasets: [{
    label: 'Market Size (R$ milhões)',
    data: [800, 60, 1.2],
    backgroundColor: ['#0ea5e9', '#10b981', '#f59e0b'],
    borderRadius: 8
  }]
}))

const marketSizeLegend = [
  { label: 'TAM', color: '#0ea5e9' },
  { label: 'SAM', color: '#10b981' },
  { label: 'SOM', color: '#f59e0b' }
]

const unitEconomicsData = computed(() => ({
  labels: ['LTV', 'CAC', 'ARPU (mês)', 'Payback (meses)'],
  datasets: [{
    data: [data.value.unitEconomics.ltv, data.value.unitEconomics.cac, data.value.unitEconomics.arpu, data.value.unitEconomics.paybackMonths * 100],
    backgroundColor: ['#10b981', '#ef4444', '#3b82f6', '#f59e0b'],
    borderWidth: 0
  }]
}))

const unitEconomicsLegend = [
  { label: 'LTV: R$ 28.8K', color: '#10b981' },
  { label: 'CAC: R$ 2.5K', color: '#ef4444' },
  { label: 'ARPU: R$ 800', color: '#3b82f6' },
  { label: 'Payback: 14 meses', color: '#f59e0b' }
]
</script>
