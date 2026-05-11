<template>
  <div class="space-y-6">
    <!-- Header -->
    <div class="flex items-center justify-between">
      <h2 class="text-2xl font-bold text-white">Roadmap NeoGov</h2>
      <div class="flex items-center gap-4 text-sm text-slate-400">
        <span>Investimento total: <strong class="text-white">R$7.4M</strong></span>
        <span>Breakeven: <strong class="text-yellow-400">M18-M24</strong></span>
      </div>
    </div>

    <!-- Timeline horizontal bar -->
    <div class="bg-slate-800/50 border border-slate-700 rounded-xl p-6 overflow-x-auto">
      <h3 class="text-base font-bold text-white mb-4">Timeline M1–M36</h3>
      <div class="relative" style="min-width: 700px;">
        <!-- Month axis -->
        <div class="flex mb-2">
          <div
            v-for="m in timelineMonths"
            :key="m"
            class="text-xs text-slate-500 text-center flex-1"
          >
            {{ m % 6 === 0 ? `M${m}` : '' }}
          </div>
        </div>

        <!-- Wave bars -->
        <div class="space-y-2">
          <div
            v-for="wave in waves"
            :key="wave.id"
            class="relative h-10 flex items-center"
          >
            <!-- Label before bar -->
            <div class="w-32 shrink-0 pr-2 text-right">
              <span class="text-xs font-medium text-slate-300 truncate block">{{ wave.name }}</span>
            </div>
            <!-- Bar container -->
            <div class="flex-1 relative h-8">
              <div class="absolute inset-y-0 w-full bg-slate-900/40 rounded"></div>
              <div
                class="absolute inset-y-1 rounded flex items-center px-2 overflow-hidden"
                :class="waveColor(wave.id)"
                :style="waveStyle(wave)"
                :title="`${wave.name}: M${wave.start_month}–M${wave.end_month}`"
              >
                <span class="text-xs text-white font-medium whitespace-nowrap overflow-hidden text-ellipsis">
                  {{ wave.target_arr || wave.investment }}
                </span>
              </div>
              <!-- Milestones dots -->
              <div
                v-for="ms in waveMilestones(wave)"
                :key="ms"
                class="absolute top-1/2 -translate-y-1/2 w-2 h-2 rounded-full bg-white border border-slate-900"
                :style="{ left: `${((ms - 1) / 36) * 100}%` }"
                :title="`Milestone M${ms}`"
              />
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Wave Detail Cards -->
    <div class="grid md:grid-cols-2 xl:grid-cols-3 gap-4">
      <div
        v-for="wave in waves"
        :key="wave.id"
        class="bg-slate-800/50 border rounded-xl p-4 transition-all cursor-pointer"
        :class="[waveCardBorder(wave.id), activeWave === wave.id ? 'ring-1 ring-white/20' : '']"
        @click="activeWave = activeWave === wave.id ? null : wave.id"
      >
        <div class="flex items-start justify-between mb-3">
          <div>
            <div class="flex items-center gap-2 mb-1">
              <span class="w-3 h-3 rounded-full shrink-0" :class="waveDot(wave.id)"></span>
              <h4 class="text-sm font-bold text-white">{{ wave.name }}</h4>
            </div>
            <p class="text-xs text-slate-400">M{{ wave.start_month }} → M{{ wave.end_month }}</p>
          </div>
          <div class="text-right">
            <p class="text-xs text-slate-400">ARR alvo</p>
            <p class="text-sm font-bold text-green-400">{{ wave.target_arr || '—' }}</p>
          </div>
        </div>

        <div class="flex items-center justify-between text-xs text-slate-400 mb-3">
          <span>Investimento: <strong class="text-white">{{ wave.investment || '—' }}</strong></span>
          <span class="flex gap-1 flex-wrap">
            <span
              v-for="cid in (wave.cluster_ids || [])"
              :key="cid"
              class="px-1.5 py-0.5 rounded bg-slate-700 text-slate-300"
            >{{ cid }}</span>
          </span>
        </div>

        <!-- Milestones -->
        <div v-if="wave.milestones?.length" class="border-t border-slate-700/50 pt-3">
          <p class="text-xs text-slate-500 mb-2">Milestones</p>
          <ul class="space-y-1">
            <li
              v-for="ms in wave.milestones"
              :key="ms"
              class="text-xs text-slate-300 flex items-start gap-1.5"
            >
              <span class="text-slate-500 mt-0.5 shrink-0">›</span>{{ ms }}
            </li>
          </ul>
        </div>

        <!-- Gate Criteria (collapsible) -->
        <div v-if="activeWave === wave.id && gateFor(wave.id)?.length" class="mt-3 border-t border-slate-700/50 pt-3">
          <p class="text-xs text-slate-400 font-bold mb-2">Gate Criteria</p>
          <ul class="space-y-1">
            <li
              v-for="gate in gateFor(wave.id)"
              :key="gate"
              class="text-xs text-slate-300 flex items-start gap-1.5"
            >
              <span class="text-green-400 mt-0.5 shrink-0">✓</span>{{ gate }}
            </li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Kill Criteria -->
    <div v-if="roadmap?.kill_criteria?.length" class="bg-red-950/20 border border-red-700/50 rounded-xl p-5">
      <h3 class="text-base font-bold text-red-400 mb-3">Kill Criteria (Stop Loss)</h3>
      <ul class="space-y-2">
        <li
          v-for="kc in roadmap.kill_criteria"
          :key="kc"
          class="flex items-start gap-2 text-sm text-slate-300"
        >
          <span class="text-red-400 shrink-0 mt-0.5">✕</span>{{ kc }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const props = defineProps({
  roadmap: { type: Object, required: true },
  clusters: { type: Array, default: () => [] },
})

const activeWave = ref(null)
const timelineMonths = Array.from({ length: 36 }, (_, i) => i + 1)

const waves = computed(() => props.roadmap?.waves || [])

const waveStyle = (wave) => {
  const total = 36
  const start = ((wave.start_month - 1) / total) * 100
  const width = ((wave.end_month - wave.start_month + 1) / total) * 100
  return { left: `${start}%`, width: `${width}%` }
}

const waveMilestones = (wave) => {
  // Extract month numbers from milestone strings like "M3: ..."
  const ms = []
  ;(wave.milestones || []).forEach(m => {
    const match = m.match(/^M(\d+)/)
    if (match) ms.push(parseInt(match[1]))
  })
  return ms
}

const waveColor = (id) => {
  const map = {
    wave1: 'bg-amber-500/70',
    wave_1: 'bg-amber-500/70',
    '1': 'bg-amber-500/70',
    wave2a: 'bg-blue-500/70',
    wave_2a: 'bg-blue-500/70',
    '2a': 'bg-blue-500/70',
    wave2b: 'bg-purple-500/70',
    wave_2b: 'bg-purple-500/70',
    '2b': 'bg-purple-500/70',
    wave3: 'bg-green-500/70',
    wave_3: 'bg-green-500/70',
    '3': 'bg-green-500/70',
    wave4: 'bg-orange-500/70',
    wave_4: 'bg-orange-500/70',
    '4': 'bg-orange-500/70',
    wave5: 'bg-slate-500/70',
    wave_5: 'bg-slate-500/70',
    '5': 'bg-slate-500/70',
  }
  return map[id] || map[String(id).replace('wave', '')] || 'bg-slate-500/70'
}

const waveDot = (id) => waveColor(id).replace('/70', '')

const waveCardBorder = (id) => {
  const map = {
    wave1: 'border-amber-700/50', wave_1: 'border-amber-700/50', '1': 'border-amber-700/50',
    wave2a: 'border-blue-700/50', wave_2a: 'border-blue-700/50', '2a': 'border-blue-700/50',
    wave2b: 'border-purple-700/50', wave_2b: 'border-purple-700/50', '2b': 'border-purple-700/50',
    wave3: 'border-green-700/50', wave_3: 'border-green-700/50', '3': 'border-green-700/50',
    wave4: 'border-orange-700/50', wave_4: 'border-orange-700/50', '4': 'border-orange-700/50',
    wave5: 'border-slate-600', wave_5: 'border-slate-600', '5': 'border-slate-600',
  }
  return map[id] || map[String(id).replace('wave', '')] || 'border-slate-700'
}

const gateFor = (waveId) => {
  const gates = props.roadmap?.gate_criteria || {}
  // Try multiple key patterns
  for (const [key, val] of Object.entries(gates)) {
    if (key.includes(String(waveId))) return val
  }
  // Try by position
  const waveIndex = waves.value.findIndex(w => w.id === waveId)
  if (waveIndex < waves.value.length - 1) {
    const nextWave = waves.value[waveIndex + 1]
    const gateKey = Object.keys(gates).find(k =>
      k.includes(String(waveId)) || k.includes(String(nextWave?.id))
    )
    return gateKey ? gates[gateKey] : []
  }
  return []
}
</script>
