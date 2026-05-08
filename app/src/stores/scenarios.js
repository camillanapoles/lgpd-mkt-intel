import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useScenarioStore = defineStore('scenarios', () => {
  const selectedScenarioId = ref('moderate')
  const selectedVariables = ref({
    pricing: 'standard',
    salesCycle: 'medium',
    churn: 'low'
  })

  const scenarios = ref([
    {
      id: 'conservative',
      name: 'Conservador',
      description: 'Foco em municípios pequenos, pricing de penetração',
      typeMultiplier: 0.7,
      assumptions: {
        marketShare: 0.01,
        pricing: 'penetration',
        salesCycle: 'slow',
        churn: 0.1
      },
      projections: {
        year1: { customers: 15, arr: 144000, cac: 3000 },
        year2: { customers: 40, arr: 384000, cac: 2500 },
        year3: { customers: 80, arr: 768000, cac: 2000 }
      }
    },
    {
      id: 'moderate',
      name: 'Moderado (Base)',
      description: 'Mix municípios pequenos e médios, pricing padrão',
      typeMultiplier: 1.0,
      assumptions: {
        marketShare: 0.02,
        pricing: 'standard',
        salesCycle: 'medium',
        churn: 0.08
      },
      projections: {
        year1: { customers: 30, arr: 288000, cac: 2500 },
        year2: { customers: 80, arr: 768000, cac: 2000 },
        year3: { customers: 150, arr: 1440000, cac: 1800 }
      }
    },
    {
      id: 'aggressive',
      name: 'Agressivo',
      description: 'Foco em municípios médios, pricing premium, expansion PME ano 2',
      typeMultiplier: 1.3,
      assumptions: {
        marketShare: 0.03,
        pricing: 'premium',
        salesCycle: 'fast',
        churn: 0.05
      },
      projections: {
        year1: { customers: 50, arr: 600000, cac: 3500 },
        year2: { customers: 120, arr: 1440000, cac: 2500 },
        year3: { customers: 250, arr: 3000000, cac: 2000 }
      }
    }
  ])

  const selectedScenario = computed(() =>
    scenarios.value.find(s => s.id === selectedScenarioId.value) || scenarios.value[1]
  )

  const pricingMultiplier = computed(() => {
    const multipliers = { penetration: 0.8, standard: 1.0, premium: 1.2 }
    return multipliers[selectedVariables.value.pricing] || 1.0
  })

  const cycleMultiplier = computed(() => {
    const multipliers = { fast: 1.3, medium: 1.0, slow: 0.7 }
    return multipliers[selectedVariables.value.salesCycle] || 1.0
  })

  const customImpact = computed(() => {
    const baseMetrics = { arr: 1200000, customers: 150, cac: 2500, payback: 14 }
    const typeMultiplier = selectedScenario.value.typeMultiplier

    return {
      arr: Math.round(baseMetrics.arr * pricingMultiplier.value * typeMultiplier),
      customers: Math.round(baseMetrics.customers * cycleMultiplier.value * typeMultiplier),
      cac: Math.round(baseMetrics.cac * (1 / cycleMultiplier.value)),
      payback: Math.round(baseMetrics.payback * (1 / cycleMultiplier.value))
    }
  })

  function setScenario(id) {
    selectedScenarioId.value = id
  }

  function setVariable(key, value) {
    selectedVariables.value = { ...selectedVariables.value, [key]: value }
  }

  return {
    selectedScenarioId,
    selectedVariables,
    scenarios,
    selectedScenario,
    pricingMultiplier,
    cycleMultiplier,
    customImpact,
    setScenario,
    setVariable
  }
})
