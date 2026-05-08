<template>
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
    <!-- Header -->
    <div class="mb-8">
      <h1 class="font-display text-3xl font-bold text-slate-900">Análise de Cenários</h1>
      <p class="text-slate-600 mt-2">Simule diferentes estratégias e seus impactos financeiros</p>
    </div>

    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
      <!-- Scenario Selector -->
      <div class="lg:col-span-1">
        <ScenarioSelector @scenario-change="handleScenarioChange" />
      </div>

      <!-- Results -->
      <div class="lg:col-span-2 space-y-6">
        <!-- Selected Scenario Overview -->
        <div class="card p-6">
          <h3 class="font-display font-semibold text-slate-900 mb-4">Cenário Selecionado</h3>
          <div class="flex items-center gap-4 mb-4">
            <span class="text-2xl font-bold text-primary-600">{{ selectedScenario.name }}</span>
            <span :class="`badge ${getScenarioBadgeClass()}`">{{ getScenarioLabel() }}</span>
          </div>
          <p class="text-slate-600">{{ selectedScenario.description }}</p>

          <div class="mt-4 grid grid-cols-2 gap-4 text-sm">
            <div>
              <p class="text-slate-500">Market Share Alvo</p>
              <p class="font-medium">{{ (selectedScenario.assumptions.marketShare * 100).toFixed(0) }}%</p>
            </div>
            <div>
              <p class="text-slate-500">Pricing</p>
              <p class="font-medium capitalize">{{ selectedScenario.assumptions.pricing }}</p>
            </div>
            <div>
              <p class="text-slate-500">Sales Cycle</p>
              <p class="font-medium capitalize">{{ selectedScenario.assumptions.salesCycle }}</p>
            </div>
            <div>
              <p class="text-slate-500">Churn Estimado</p>
              <p class="font-medium">{{ (selectedScenario.assumptions.churn * 100).toFixed(0) }}%</p>
            </div>
          </div>
        </div>

        <!-- 3-Year Projection -->
        <div class="card p-6">
          <h3 class="font-display font-semibold text-slate-900 mb-4">Projeção 3 Anos</h3>
          <div class="overflow-x-auto">
            <table class="w-full text-sm">
              <thead>
                <tr class="border-b border-slate-200">
                  <th class="text-left py-3 px-4 font-medium text-slate-600">Métrica</th>
                  <th class="text-right py-3 px-4 font-medium text-slate-600">Ano 1</th>
                  <th class="text-right py-3 px-4 font-medium text-slate-600">Ano 2</th>
                  <th class="text-right py-3 px-4 font-medium text-slate-600">Ano 3</th>
                </tr>
              </thead>
              <tbody>
                <tr class="border-b border-slate-100">
                  <td class="py-3 px-4 text-slate-700">Clientes</td>
                  <td class="text-right py-3 px-4 font-medium">{{ selectedScenario.projections.year1.customers }}</td>
                  <td class="text-right py-3 px-4 font-medium">{{ selectedScenario.projections.year2.customers }}</td>
                  <td class="text-right py-3 px-4 font-medium">{{ selectedScenario.projections.year3.customers }}</td>
                </tr>
                <tr class="border-b border-slate-100">
                  <td class="py-3 px-4 text-slate-700">ARR</td>
                  <td class="text-right py-3 px-4 font-medium">{{ formatCurrency(selectedScenario.projections.year1.arr) }}</td>
                  <td class="text-right py-3 px-4 font-medium">{{ formatCurrency(selectedScenario.projections.year2.arr) }}</td>
                  <td class="text-right py-3 px-4 font-medium">{{ formatCurrency(selectedScenario.projections.year3.arr) }}</td>
                </tr>
                <tr class="border-b border-slate-100">
                  <td class="py-3 px-4 text-slate-700">CAC</td>
                  <td class="text-right py-3 px-4 font-medium">{{ formatCurrency(selectedScenario.projections.year1.cac) }}</td>
                  <td class="text-right py-3 px-4 font-medium">{{ formatCurrency(selectedScenario.projections.year2.cac) }}</td>
                  <td class="text-right py-3 px-4 font-medium">{{ formatCurrency(selectedScenario.projections.year3.cac) }}</td>
                </tr>
                <tr>
                  <td class="py-3 px-4 text-slate-700">LTV:CAC</td>
                  <td class="text-right py-3 px-4 font-medium">{{ calculateLTVCac(selectedScenario.projections.year1).toFixed(1) }}x</td>
                  <td class="text-right py-3 px-4 font-medium">{{ calculateLTVCac(selectedScenario.projections.year2).toFixed(1) }}x</td>
                  <td class="text-right py-3 px-4 font-medium">{{ calculateLTVCac(selectedScenario.projections.year3).toFixed(1) }}x</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <!-- Scenario Comparison Chart -->
        <ChartComponent
          title="Comparação de Cenários - ARR Ano 3"
          type="bar"
          :height="'300px'"
          :data="comparisonData"
          :legend="comparisonLegend"
        />

        <!-- Sensitivity Analysis -->
        <div class="card p-6">
          <h3 class="font-display font-semibold text-slate-900 mb-4">Análise de Sensibilidade</h3>
          <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
            <div class="p-4 bg-slate-50 rounded-lg">
              <p class="text-sm text-slate-600">Impacto Pricing +20%</p>
              <p class="text-lg font-bold text-green-600 mt-1">+{{ calculatePricingSensitivity() }}% ARR</p>
            </div>
            <div class="p-4 bg-slate-50 rounded-lg">
              <p class="text-sm text-slate-600">Impacto Churn +5pp</p>
              <p class="text-lg font-bold text-red-600 mt-1">-{{ calculateChurnSensitivity() }}% LTV</p>
            </div>
            <div class="p-4 bg-slate-50 rounded-lg">
              <p class="text-sm text-slate-600">Impacto CAC -30%</p>
              <p class="text-lg font-bold text-green-600 mt-1">+{{ calculateCacSensitivity() }}% Margem</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import strategicData from '../data/strategicData.js'
import ScenarioSelector from '../components/ScenarioSelector.vue'
import ChartComponent from '../components/ChartComponent.vue'

const scenarios = ref(strategicData.scenarios)
const selectedScenario = ref(scenarios.value[1]) // Default to moderate

const handleScenarioChange = (scenario) => {
  // Find matching scenario
  const found = scenarios.value.find(s => s.id === scenario.type)
  if (found) {
    selectedScenario.value = found
  }
}

const getScenarioBadgeClass = () => {
  const classes = {
    conservative: 'badge-info',
    moderate: 'badge-success',
    aggressive: 'badge-warning'
  }
  return classes[selectedScenario.value.id] || 'badge-info'
}

const getScenarioLabel = () => {
  const labels = {
    conservative: 'Baixo Risco',
    moderate: 'Balanceado',
    aggressive: 'Alto Retorno'
  }
  return labels[selectedScenario.value.id] || ''
}

const formatCurrency = (value) => {
  return new Intl.NumberFormat('pt-BR', {
    style: 'currency',
    currency: 'BRL',
    minimumFractionDigits: 0,
    maximumFractionDigits: 0
  }).format(value)
}

const calculateLTVCac = (year) => {
  const ltv = strategicData.unitEconomics.ltv
  return ltv / year.cac
}

const comparisonData = computed(() => ({
  labels: scenarios.value.map(s => s.name),
  datasets: [{
    label: 'ARR Ano 3 (R$ milhões)',
    data: scenarios.value.map(s => s.projections.year3.arr / 1000000),
    backgroundColor: ['#3b82f6', '#10b981', '#f59e0b'],
    borderRadius: 8
  }]
}))

const comparisonLegend = computed(() =>
  scenarios.value.map((s, i) => ({
    label: s.name,
    color: ['#3b82f6', '#10b981', '#f59e0b'][i]
  }))
)

const calculatePricingSensitivity = () => {
  return 20 // 20% increase in pricing = 20% increase in ARR (simplified)
}

const calculateChurnSensitivity = () => {
  const baseChurn = selectedScenario.value.assumptions.churn
  const newChurn = baseChurn + 0.05
  const baseLTV = strategicData.unitEconomics.arpu * 12 / baseChurn
  const newLTV = strategicData.unitEconomics.arpu * 12 / newChurn
  return ((baseLTV - newLTV) / baseLTV * 100).toFixed(0)
}

const calculateCacSensitivity = () => {
  const baseCac = selectedScenario.projections.year1.cac
  const newCac = baseCac * 0.7
  const ltv = strategicData.unitEconomics.ltv
  const baseMargin = ((ltv - baseCac) / ltv * 100)
  const newMargin = ((ltv - newCac) / ltv * 100)
  return (newMargin - baseMargin).toFixed(0)
}
</script>
