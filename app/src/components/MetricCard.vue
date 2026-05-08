<template>
  <div class="card p-6 card-hover">
    <div class="flex items-start justify-between">
      <div>
        <p class="metric-label">{{ label }}</p>
        <p class="metric-value mt-1">{{ value }}</p>
        <p v-if="description" class="text-sm text-slate-500 mt-2">{{ description }}</p>
      </div>
      <div :class="`w-12 h-12 rounded-lg ${iconBg} flex items-center justify-center`">
        <component :is="icon" class="w-6 h-6" :class="iconColor" />
      </div>
    </div>
    <div v-if="trend" class="mt-4 flex items-center gap-2">
      <span :class="`badge ${trendClass}`">
        <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path v-if="trendUp" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6" />
          <path v-else stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 17h8m0 0V9m0 8l-8-8-4 4-6-6" />
        </svg>
        {{ trend }}
      </span>
      <span class="text-xs text-slate-500">{{ trendLabel }}</span>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  label: String,
  value: [String, Number],
  description: String,
  icon: [String, Object],
  iconBg: { type: String, default: 'bg-primary-100' },
  iconColor: { type: String, default: 'text-primary-600' },
  trend: String,
  trendLabel: String,
  trendUp: { type: Boolean, default: true }
})

const trendClass = computed(() => {
  return props.trendUp ? 'badge-success' : 'badge-danger'
})
</script>
