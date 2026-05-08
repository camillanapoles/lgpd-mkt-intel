<template>
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
    <!-- Header -->
    <div class="mb-8">
      <h1 class="font-display text-3xl font-bold text-slate-900">Análise de Cenários</h1>
      <p class="text-slate-600 mt-2">Simule diferentes estratégias e seus impactos financeiros</p>
    </div>

    <!-- GO/NO-GO Indicator -->
    <div class="card p-5 mb-6" :class="goNogoClass">
      <div class="flex items-center justify-between">
        <div class="flex items-center gap-3">
          <span class="text-3xl">{{ goNogoIndicator.emoji }}</span>
          <div>
            <h3 class="font-display font-bold text-lg">{{ goNogoIndicator.label }}</h3>
            <p class="text-sm opacity-80">{{ goNogoIndicator.description }}</p>
          </div>
        </div>
        <div class="text-right">
          <p class="text-sm opacity-70">Score de Viabilidade</p>
          <p class="text-2xl font-bold">{{ viabilityScore.toFixed(1) }}/10</p>
        </div>
      </div>
    </div>

    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
      <!-- Left Column: ScenarioSelector + Sliders -->
      <div class="lg:col-span-1 space-y-6">
        <!-- Scenario Selector (existing component) -->
        <ScenarioSelector @scenario-change="handleScenarioChange" />

        <!-- Interactive Sliders -->
        <div class="card p-6">
          <h3 class="font-display font-semibold text-slate-900 mb-4">Variáveis Interativas</h3>
          <div class="space-y-5">
            <div v-for="slider in numericSliders" :key="slider.id">
              <div class="flex items-center justify-between mb-1">
                <label class="text-sm font-medium text-slate-700">
                  {{ slider.label }}
                  <span v-if="slider.impact === 'high'" class="text-xs text-red-500 ml-1">HIGH</span>
                </label>
                <span class="text-sm font-semibold text-primary-600">{{ slider.format ? slider.format(sliderValues[slider.id]) : sliderValues[slider.id] }}</span>
              </div>
              <input
                type="range"
                :min="slider.min"
                :max="slider.max"
                :step="slider.step || 1"
                v-model.number="sliderValues[slider.id]"
                class="w-full h-2 bg-slate-200 rounded-lg appearance-none cursor-pointer accent-primary-600"
              />
              <div class="flex justify-between text-xs text-slate-400 mt-1">
                <span>{{ slider.min }}</span>
                <span>{{ slider.max }}</span>
              </div>
            </div>

            <!-- Boolean slider for Advisor -->
            <div v-for="slider in booleanSliders" :key="slider.id" class="flex items-center justify-between">
              <label class="text-sm font-medium text-slate-700">
                {{ slider.label }}
                <span v-if="slider.impact === 'high'" class="text-xs text-red-500 ml-1">HIGH</span>
              </label>
              <button
                @click="sliderValues[slider.id] = !sliderValues[slider.id]"
                class="relative inline-flex h-6 w-11 items-center rounded-full transition-colors"
                :class="sliderValues[slider.id] ? 'bg-primary-600' : 'bg-slate-300'"
              >
                <span
                  class="inline-block h-4 w-4 transform rounded-full bg-white transition-transform"
                  :class="sliderValues[slider.id] ? 'translate-x-6' : 'translate-x-1'"
                />
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- Right Column -->
      <div class="lg:col-span-2 space-y-6">
        <!-- 3 Scenario Cards: Bear / Base / Bull -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div
            v-for="(caseData, caseKey) in scenarioCases"
            :key="caseKey"
            class="card p-5 border-l-4 transition-all"
            :class="getCaseCardClass(caseKey)"
          >
            <div class="flex items-center justify-between mb-3">
              <h4 class="font-display font-bold text-slate-900">{{ getCaseLabel(caseKey) }}</h4>
              <span :class="getCaseBadgeClass(caseKey)" class="text-xs font-medium px-2 py-1 rounded-full">{{ getCaseTag(caseKey) }}</span>
            </div>
            <div class="space-y-2 text-sm">
              <div class="flex justify-between">
                <span class="text-slate-500">MRR</span>
                <span class="font-semibold text-slate-900">{{ caseData.mrr }}</span>
              </div>
              <div class="flex justify-between">
                <span class="text-slate-500">Clientes</span>
                <span class="font-semibold text-slate-900">{{ caseData.customers }}</span>
              </div>
              <div class="flex justify-between">
                <span class="text-slate-500">Churn</span>
                <span class="font-semibold" :class="caseData.churn > 0.04 ? 'text-red-600' : 'text-green-600'">{{ (caseData.churn * 100).toFixed(1) }}%</span>
              </div>
              <div class="flex justify-between">
                <span class="text-slate-500">Runway</span>
                <span class="font-semibold text-slate-900">{{ calculateRunway(caseData) }} meses</span>
              </div>
              <div class="flex justify-between border-t border-slate-100 pt-2">
                <span class="text-slate-500">LTV:CAC</span>
                <span class="font-bold" :class="calculateLtvCac(caseData) > 3 ? 'text-green-600' : 'text-amber-600'">{{ calculateLtvCac(caseData).toFixed(1) }}x</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Projections Timeline by Phase -->
        <div class="card p-6">
          <h3 class="font-display font-semibold text-slate-900 mb-4">Projeções por Fase</h3>
          <div class="relative">
            <!-- Timeline bar -->
            <div class="absolute top-6 left-0 right-0 h-1 bg-slate-200 rounded"></div>
            <div class="grid grid-cols-4 gap-4 relative">
              <div
                v-for="(phase, phaseKey) in projectionsPhases"
                :key="phaseKey"
                class="text-center"
              >
                <div class="w-12 h-12 mx-auto rounded-full flex items-center justify-center text-white font-bold text-sm mb-3 relative z-10"
                  :class="getPhaseColor(phaseKey)"
                >
                  {{ getPhaseNumber(phaseKey) }}
                </div>
                <p class="text-xs font-medium text-slate-600 mb-1">{{ phase.label }}</p>
                <p class="text-lg font-bold text-slate-900">{{ phase.mrr }}</p>
                <p class="text-xs text-slate-500">{{ phase.customers }} clientes</p>
              </div>
            </div>
          </div>
          <div class="mt-6 p-4 bg-primary-50 rounded-lg flex items-center gap-3">
            <span class="text-sm font-medium text-primary-900">Break-even:</span>
            <span class="text-sm text-primary-700">{{ projections.break_even.customers }} clientes no mês {{ projections.break_even.month }}</span>
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
          <p class="text-sm text-slate-500 mb-4">Impacto das variáveis nos resultados (baseado nos sliders atuais)</p>
          <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
            <div class="p-4 bg-slate-50 rounded-lg">
              <p class="text-sm text-slate-600">LOIs +2 impacto MRR</p>
              <p class="text-lg font-bold mt-1" :class="sensitivityResults.loisImpact > 0 ? 'text-green-600' : 'text-red-600'">
                {{ sensitivityResults.loisImpact > 0 ? '+' : '' }}{{ formatCurrency(sensitivityResults.loisImpact) }}
              </p>
              <p class="text-xs text-slate-400 mt-1">{{ sliderValues.lois }} LOIs atuais</p>
            </div>
            <div class="p-4 bg-slate-50 rounded-lg">
              <p class="text-sm text-slate-600">Churn +2pp impacto LTV</p>
              <p class="text-lg font-bold text-red-600 mt-1">-{{ sensitivityResults.churnImpact }}%</p>
              <p class="text-xs text-slate-400 mt-1">{{ sliderValues.churn }}% churn atual</p>
            </div>
            <div class="p-4 bg-slate-50 rounded-lg">
              <p class="text-sm text-slate-600">ARPU +R$200 impacto MRR</p>
              <p class="text-lg font-bold text-green-600 mt-1">+{{ formatCurrency(sensitivityResults.arpuImpact) }}</p>
              <p class="text-xs text-slate-400 mt-1">R$ {{ sliderValues.arpu }} ARPU atual</p>
            </div>
          </div>

          <!-- Sensitivity slider heatmap -->
          <div class="mt-6">
            <h4 class="text-sm font-medium text-slate-700 mb-3">Impacto Relativo por Variável</h4>
            <div class="space-y-3">
              <div v-for="item in sensitivityHeatmap" :key="item.label" class="flex items-center gap-3">
                <span class="text-sm text-slate-600 w-32 flex-shrink-0">{{ item.label }}</span>
                <div class="flex-1 h-6 bg-slate-100 rounded-full overflow-hidden relative">
                  <div
                    class="h-full rounded-full transition-all duration-500"
                    :class="item.color"
                    :style="{ width: item.width + '%' }"
                  ></div>
                </div>
                <span class="text-xs font-medium text-slate-700 w-12 text-right">{{ item.impact }}</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, computed } from 'vue'
import strategicData from '../data/strategicData.js'
import ScenarioSelector from '../components/ScenarioSelector.vue'
import ChartComponent from '../components/ChartComponent.vue'

const scenarios = ref(strategicData.scenarios)
const selectedScenario = ref(scenarios.value[1])

const si = strategicData.scenarioInteractive

const sliderValues = reactive({
  lois: si.sliders.find(s => s.id === 'lois').value,
  advisor: si.sliders.find(s => s.id === 'advisor').value,
  funding: si.sliders.find(s => s.id === 'funding').value,
  churn: si.sliders.find(s => s.id === 'churn').value,
  arpu: si.sliders.find(s => s.id === 'arpu').value
})

const numericSliders = si.sliders.filter(s => s.type !== 'boolean').map(s => {
  if (s.id === 'churn') return { ...s, format: v => v + '%' }
  if (s.id === 'funding') return { ...s, format: v => 'R$ ' + v + 'K' }
  if (s.id === 'arpu') return { ...s, format: v => 'R$ ' + v }
  return s
})

const booleanSliders = si.sliders.filter(s => s.type === 'boolean')

const scenarioCases = si.cases

const projections = si.projections

const projectionsPhases = computed(() => {
  const { break_even, ...phases } = si.projections
  return phases
})

// --- Scenario change handler ---
const handleScenarioChange = (scenario) => {
  const found = scenarios.value.find(s => s.id === scenario.type)
  if (found) {
    selectedScenario.value = found
  }
}

// --- Viability score & GO/NO-GO ---
const viabilityScore = computed(() => {
  let score = 5.0
  // LOIs: each LOI above 0 adds 0.5, max +3
  score += Math.min(sliderValues.lois * 0.5, 3)
  // Advisor: +1.5 if present
  if (sliderValues.advisor) score += 1.5
  // Funding: bonus if above 800K
  if (sliderValues.funding >= 800) score += 0.5
  // Churn penalty: above 5% hurts
  if (sliderValues.churn > 5) score -= 1.0
  else if (sliderValues.churn <= 3) score += 0.5
  // ARPU bonus: above R$600 is healthy
  if (sliderValues.arpu >= 600) score += 0.5
  return Math.min(Math.max(score, 1), 10)
})

const goNogoIndicator = computed(() => {
  const s = viabilityScore.value
  if (s >= 7) return { label: 'GO', emoji: '✅', description: 'Viabilidade forte. Prosseguir com execução.' }
  if (s >= 5) return { label: 'GO CONDICIONAL', emoji: '⚠️', description: 'Viável com condições. Validar pré-requisitos antes.' }
  return { label: 'NO-GO', emoji: '❌', description: 'Risco alto. Revisar premissas antes de prosseguir.' }
})

const goNogoClass = computed(() => {
  const s = viabilityScore.value
  if (s >= 7) return 'bg-green-50 border border-green-200'
  if (s >= 5) return 'bg-amber-50 border border-amber-200'
  return 'bg-red-50 border border-red-200'
})

// --- Case card helpers ---
const getCaseLabel = (key) => ({ bear: 'Bear', base: 'Base', bull: 'Bull' }[key] || key)
const getCaseTag = (key) => ({ bear: 'Pessimista', base: 'Realista', bull: 'Otimista' }[key] || '')
const getCaseCardClass = (key) => ({
  bear: 'border-l-red-400',
  base: 'border-l-primary-500',
  bull: 'border-l-green-500'
}[key] || '')
const getCaseBadgeClass = (key) => ({
  bear: 'bg-red-100 text-red-700',
  base: 'bg-primary-100 text-primary-700',
  bull: 'bg-green-100 text-green-700'
}[key] || '')

// --- Case metric calculations ---
const calculateRunway = (caseData) => {
  const monthlyBurn = sliderValues.funding * 1000 / 18 // 18-month plan
  if (monthlyBurn <= 0) return 0
  return Math.round(caseData.mrrValue / monthlyBurn * 10)
}

const calculateLtvCac = (caseData) => {
  const arpu = sliderValues.arpu
  const churnRate = sliderValues.churn / 100
  if (churnRate <= 0) return 0
  const ltv = arpu / churnRate
  const cac = strategicData.unitEconomics.cac
  return ltv / cac
}

// --- Phase helpers ---
const getPhaseColor = (phaseKey) => ({
  phase_1: 'bg-blue-500',
  phase_2: 'bg-primary-500',
  phase_3: 'bg-purple-500',
  phase_4: 'bg-green-500'
}[phaseKey] || 'bg-slate-400')

const getPhaseNumber = (phaseKey) => ({
  phase_1: '1',
  phase_2: '2',
  phase_3: '3',
  phase_4: '4'
}[phaseKey] || '?')

// --- Chart data ---
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

// --- Sensitivity analysis ---
const sensitivityResults = computed(() => {
  const currentArpu = sliderValues.arpu
  const currentChurn = sliderValues.churn
  const currentLois = sliderValues.lois

  // LOIs +2 impact on MRR (each LOI represents ~potential customers)
  const loisImpact = currentLois >= 8 ? 0 : (currentLois + 2) * 5000 * 12 - currentLois * 5000 * 12

  // Churn +2pp impact on LTV percentage
  const baseLtv = currentChurn > 0 ? currentArpu / (currentChurn / 100) : 0
  const newChurn = currentChurn + 2
  const newLtv = newChurn > 0 ? currentArpu / (newChurn / 100) : 0
  const churnImpact = baseLtv > 0 ? ((baseLtv - newLtv) / baseLtv * 100).toFixed(0) : 0

  // ARPU +R$200 impact on MRR (base case 275 customers)
  const arpuImpact = 200 * 275

  return { loisImpact, churnImpact: Number(churnImpact), arpuImpact }
})

const sensitivityHeatmap = computed(() => {
  const items = [
    { label: 'LOIs Assinadas', impact: sliderValues.lois >= 5 ? 'ALTO' : 'MEDIO', value: sliderValues.lois / 10, color: 'bg-red-400' },
    { label: 'Advisor', impact: sliderValues.advisor ? 'ALTO' : 'BAIXO', value: sliderValues.advisor ? 0.9 : 0.1, color: sliderValues.advisor ? 'bg-green-400' : 'bg-slate-300' },
    { label: 'Funding', impact: sliderValues.funding >= 1000 ? 'ALTO' : 'MEDIO', value: sliderValues.funding / 2000, color: 'bg-blue-400' },
    { label: 'Churn', impact: sliderValues.churn <= 3 ? 'BOM' : 'ALTO', value: 1 - (sliderValues.churn / 10), color: sliderValues.churn <= 3 ? 'bg-green-400' : 'bg-red-400' },
    { label: 'ARPU', impact: sliderValues.arpu >= 600 ? 'BOM' : 'MEDIO', value: sliderValues.arpu / 1500, color: sliderValues.arpu >= 600 ? 'bg-green-400' : 'bg-amber-400' }
  ]
  return items.map(item => ({ ...item, width: Math.round(item.value * 100) }))
})

// --- Formatting ---
const formatCurrency = (value) => {
  return new Intl.NumberFormat('pt-BR', {
    style: 'currency',
    currency: 'BRL',
    minimumFractionDigits: 0,
    maximumFractionDigits: 0
  }).format(value)
}
</script>
