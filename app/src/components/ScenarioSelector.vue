<template>
  <div class="card p-6">
    <h3 class="font-display font-semibold text-slate-900 mb-4">Seleção de Cenário</h3>

    <!-- Scenario Type -->
    <div class="mb-4">
      <label class="block text-sm font-medium text-slate-700 mb-2">Tipo de Cenário</label>
      <div class="grid grid-cols-2 gap-2">
        <button
          v-for="type in scenarioTypes"
          :key="type.id"
          @click="selectedType = type.id"
          class="px-4 py-2 rounded-lg text-sm font-medium transition-colors"
          :class="selectedType === type.id ? 'bg-primary-100 text-primary-700 border-2 border-primary-300' : 'bg-slate-100 text-slate-600 hover:bg-slate-200'"
        >
          {{ type.label }}
        </button>
      </div>
    </div>

    <!-- Variables -->
    <div class="space-y-3">
      <label class="block text-sm font-medium text-slate-700">Variáveis</label>

      <div v-for="variable in variables" :key="variable.id" class="flex items-center justify-between">
        <span class="text-sm text-slate-600">{{ variable.label }}</span>
        <select
          v-model="selectedVariables[variable.id]"
          class="px-3 py-1.5 rounded-lg border border-slate-300 text-sm focus:outline-none focus:ring-2 focus:ring-primary-500"
        >
          <option v-for="option in variable.options" :key="option.value" :value="option.value">
            {{ option.label }}
          </option>
        </select>
      </div>
    </div>

    <!-- Impact Summary -->
    <div class="mt-6 p-4 bg-slate-50 rounded-lg">
      <h4 class="text-sm font-medium text-slate-700 mb-2">Impacto Estimado</h4>
      <div class="grid grid-cols-2 gap-4">
        <div>
          <p class="text-xs text-slate-500">ARR</p>
          <p class="font-semibold text-slate-900">{{ formatCurrency(calculateImpact().arr) }}</p>
        </div>
        <div>
          <p class="text-xs text-slate-500">Clientes</p>
          <p class="font-semibold text-slate-900">{{ calculateImpact().customers }}</p>
        </div>
        <div>
          <p class="text-xs text-slate-500">CAC</p>
          <p class="font-semibold text-slate-900">{{ formatCurrency(calculateImpact().cac) }}</p>
        </div>
        <div>
          <p class="text-xs text-slate-500">Payback</p>
          <p class="font-semibold text-slate-900">{{ calculateImpact().payback }} meses</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, computed } from 'vue'

const emit = defineEmits(['scenario-change'])

const selectedType = ref('conservative')

const selectedVariables = reactive({
  pricing: 'standard',
  salesCycle: 'medium',
  churn: 'low'
})

const scenarioTypes = [
  { id: 'conservative', label: 'Conservador' },
  { id: 'moderate', label: 'Moderado' },
  { id: 'aggressive', label: 'Agressivo' }
]

const variables = [
  {
    id: 'pricing',
    label: 'Estratégia de Preço',
    options: [
      { value: 'penetration', label: 'Penetração (-20%)' },
      { value: 'standard', label: 'Padrão' },
      { value: 'premium', label: 'Premium (+20%)' }
    ]
  },
  {
    id: 'salesCycle',
    label: 'Ciclo de Vendas',
    options: [
      { value: 'fast', label: 'Rápido (60 dias)' },
      { value: 'medium', label: 'Médio (120 dias)' },
      { value: 'slow', label: 'Lento (180 dias)' }
    ]
  },
  {
    id: 'churn',
    label: 'Taxa de Churn',
    options: [
      { value: 'low', label: 'Baixo (5%)' },
      { value: 'medium', label: 'Médio (10%)' },
      { value: 'high', label: 'Alto (15%)' }
    ]
  }
]

const pricingMultiplier = computed(() => {
  const multipliers = { penetration: 0.8, standard: 1.0, premium: 1.2 }
  return multipliers[selectedVariables.pricing] || 1.0
})

const cycleMultiplier = computed(() => {
  const multipliers = { fast: 1.3, medium: 1.0, slow: 0.7 }
  return multipliers[selectedVariables.salesCycle] || 1.0
})

const baseMetrics = {
  arr: 1200000,
  customers: 150,
  cac: 2500,
  payback: 14
}

const calculateImpact = () => {
  const typeMultiplier = {
    conservative: 0.7,
    moderate: 1.0,
    aggressive: 1.3
  }[selectedType.value] || 1.0

  return {
    arr: Math.round(baseMetrics.arr * pricingMultiplier.value * typeMultiplier),
    customers: Math.round(baseMetrics.customers * cycleMultiplier.value * typeMultiplier),
    cac: Math.round(baseMetrics.cac * (1 / cycleMultiplier.value)),
    payback: Math.round(baseMetrics.payback * (1 / cycleMultiplier.value))
  }
}

const formatCurrency = (value) => {
  return new Intl.NumberFormat('pt-BR', {
    style: 'currency',
    currency: 'BRL',
    minimumFractionDigits: 0,
    maximumFractionDigits: 0
  }).format(value)
}

// Emit changes
watch(() => ({ selectedType, selectedVariables }), () => {
  emit('scenario-change', {
    type: selectedType.value,
    variables: { ...selectedVariables },
    impact: calculateImpact()
  })
}, { deep: true })
</script>

<script>
import { watch } from 'vue'
export default {
  name: 'ScenarioSelector'
}
</script>
