<template>
  <div class="card p-6">
    <div class="flex items-center justify-between mb-4">
      <h3 class="font-display font-semibold text-slate-900">{{ title }}</h3>
      <div v-if="legend" class="flex gap-4 text-xs">
        <span v-for="item in legend" :key="item.label" class="flex items-center gap-1">
          <span class="w-3 h-3 rounded" :style="{ backgroundColor: item.color }"></span>
          {{ item.label }}
        </span>
      </div>
    </div>
    <div class="relative" :style="{ height: height }">
      <canvas :id="canvasId"></canvas>
    </div>
  </div>
</template>

<script setup>
import { onMounted, watch } from 'vue'
import Chart from 'chart.js/auto'

const props = defineProps({
  title: String,
  type: { type: String, default: 'bar' },
  data: Object,
  options: Object,
  height: { type: String, default: '300px' },
  legend: Array
})

const canvasId = `chart-${Math.random().toString(36).substr(2, 9)}`
let chartInstance = null

const createChart = () => {
  const ctx = document.getElementById(canvasId)
  if (!ctx) return

  if (chartInstance) {
    chartInstance.destroy()
  }

  const defaultOptions = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        display: !props.legend
      }
    }
  }

  chartInstance = new Chart(ctx, {
    type: props.type,
    data: props.data,
    options: { ...defaultOptions, ...props.options }
  })
}

onMounted(() => {
  createChart()
})

watch(() => props.data, () => {
  createChart()
}, { deep: true })
</script>
