<template>
  <div class="scenario-simulator">
    <div class="flex items-center justify-between mb-6">
      <h2 class="text-h2 text-white">Simulacao de Cenarios</h2>
      <span class="text-caption text-slate-400">
        Cenario ativo:
        <span class="font-bold text-white capitalize">{{ activeScenario }}</span>
      </span>
    </div>

    <div class="grid md:grid-cols-2 gap-6 mb-6">
      <div
        v-for="slider in scenarios.sliders"
        :key="slider.id"
        class="bg-slate-800/50 border border-slate-700 rounded-card p-4"
      >
        <div class="flex items-center justify-between mb-2">
          <label class="text-body-sm text-white font-medium">{{ slider.label }}</label>
          <span
            class="text-caption px-2 py-0.5 rounded"
            :class="slider.impact === 'high' ? 'bg-red-900/50 text-red-400' : 'bg-yellow-900/50 text-yellow-400'"
          >
            {{ slider.impact === 'high' ? 'Alto impacto' : 'Medio impacto' }}
          </span>
        </div>

        <template v-if="slider.type === 'boolean'">
          <button
            @click="toggleSlider(slider.id)"
            :class="[
              'w-12 h-6 rounded-full transition-all duration-300 relative',
              sliderValues[slider.id] ? 'bg-green-500' : 'bg-slate-600',
            ]"
          >
            <span
              :class="[
                'absolute top-0.5 w-5 h-5 rounded-full bg-white transition-all duration-300',
                sliderValues[slider.id] ? 'left-6' : 'left-0.5',
              ]"
            />
          </button>
          <span class="text-caption text-slate-400 ml-3">
            {{ sliderValues[slider.id] ? 'Sim' : 'Nao' }}
          </span>
        </template>

        <template v-else-if="slider.options">
          <select
            :value="sliderValues[slider.id]"
            @change="updateSlider(slider.id, $event.target.value)"
            class="w-full bg-slate-700 text-white rounded-lg px-3 py-2 text-body-sm border border-slate-600"
          >
            <option v-for="opt in slider.options" :key="opt" :value="opt">{{ opt }}</option>
          </select>
        </template>

        <template v-else>
          <div class="flex items-center gap-3">
            <input
              type="range"
              :min="slider.min"
              :max="slider.max"
              :value="sliderValues[slider.id]"
              @input="updateSlider(slider.id, Number($event.target.value))"
              class="flex-1 accent-accent-500"
            />
            <span class="text-body-sm text-white font-mono w-16 text-right">
              {{ sliderValues[slider.id] }}
            </span>
          </div>
          <div class="flex justify-between text-caption text-slate-500 mt-1">
            <span>{{ slider.min }}</span>
            <span>{{ slider.max }}</span>
          </div>
        </template>
      </div>
    </div>

    <div class="grid md:grid-cols-3 gap-4">
      <div
        v-for="(scenario, name) in scenarios.cases"
        :key="name"
        @click="activeScenario = name"
        :class="[
          'rounded-card border-2 p-5 cursor-pointer transition-all',
          activeScenario === name
            ? 'border-accent-500 bg-accent-950/30 shadow-card-hover'
            : 'border-slate-700 bg-slate-800/50 hover:border-slate-500',
        ]"
      >
        <div class="flex items-center justify-between mb-4">
          <h3 class="text-h4 text-white uppercase">{{ scenarioLabel(name) }}</h3>
          <span
            v-if="activeScenario === name"
            class="text-caption bg-accent-500 text-white px-2 py-0.5 rounded"
          >
            Ativo
          </span>
        </div>

        <div class="space-y-3">
          <div class="flex justify-between items-center">
            <span class="text-body-sm text-slate-400">MRR</span>
            <span class="text-body-lg text-white font-bold">{{ scenario.mrr }}</span>
          </div>
          <div class="flex justify-between items-center">
            <span class="text-body-sm text-slate-400">Clientes</span>
            <span class="text-body text-white">{{ scenario.customers }}</span>
          </div>
          <div class="flex justify-between items-center">
            <span class="text-body-sm text-slate-400">Churn</span>
            <span class="text-body text-white">{{ (scenario.churn * 100).toFixed(1) }}%</span>
          </div>
        </div>
      </div>
    </div>

    <div v-if="scenarios.projections" class="mt-6">
      <h3 class="text-h4 text-white mb-3">Projecoes por Fase</h3>
      <div class="grid grid-cols-2 md:grid-cols-4 gap-3">
        <div
          v-for="(proj, phase) in scenarios.projections"
          :key="phase"
          class="bg-slate-800/30 border border-slate-700/50 rounded-lg p-3"
        >
          <p class="text-caption text-slate-400 capitalize">{{ phaseLabel(phase) }}</p>
          <p class="text-body text-white font-bold">{{ proj.mrr }}</p>
          <p class="text-caption text-slate-500">{{ proj.customers }} clientes</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, watch } from 'vue'

const emit = defineEmits(['scenario-change'])

const props = defineProps({
  scenarios: { type: Object, required: true },
})

const activeScenario = ref(props.scenarios.active_scenario || 'base')

const sliderValues = reactive({})
props.scenarios.sliders?.forEach((s) => {
  sliderValues[s.id] = s.value
})

const updateSlider = (id, value) => {
  sliderValues[id] = value
  emit('scenario-change', { ...sliderValues })
}

const toggleSlider = (id) => {
  sliderValues[id] = !sliderValues[id]
  emit('scenario-change', { ...sliderValues })
}

const scenarioLabel = (name) => {
  const labels = { bear: 'Bear', base: 'Base', bull: 'Bull' }
  return labels[name] || name
}

const phaseLabel = (phase) => {
  const labels = {
    phase_1: 'Fase 1 - MVP',
    phase_2: 'Fase 2 - PMF',
    phase_3: 'Fase 3 - Scale',
    phase_4: 'Fase 4 - Enterprise',
    break_even: 'Break-even',
  }
  return labels[phase] || phase.replace(/_/g, ' ')
}
</script>
