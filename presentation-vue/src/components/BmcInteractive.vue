<template>
  <div class="bmc-interactive">
    <div class="flex items-center justify-between mb-6">
      <h2 class="text-h2 text-white">Business Model Canvas</h2>
      <div class="flex items-center gap-2">
        <button
          @click="showGaps = !showGaps"
          :class="[
            'px-3 py-1.5 rounded-lg text-caption transition-all',
            showGaps ? 'bg-yellow-600 text-white' : 'bg-slate-700 text-slate-300 hover:bg-slate-600',
          ]"
        >
          {{ showGaps ? 'Ocultar Gaps' : 'Ver Gaps' }}
        </button>
      </div>
    </div>

    <div class="grid grid-cols-5 gap-2">
      <div class="col-span-1 space-y-2">
        <BmcBlock :block="getBlock('kp')" @click="activeBlock = 'kp'" :active="activeBlock === 'kp'" />
        <BmcBlock :block="getBlock('ka')" @click="activeBlock = 'ka'" :active="activeBlock === 'ka'" />
        <BmcBlock :block="getBlock('kr')" @click="activeBlock = 'kr'" :active="activeBlock === 'kr'" />
      </div>

      <div class="col-span-1 space-y-2">
        <BmcBlock :block="getBlock('vp')" @click="activeBlock = 'vp'" :active="activeBlock === 'vp'" highlight />
        <BmcBlock :block="getBlock('cr')" @click="activeBlock = 'cr'" :active="activeBlock === 'cr'" />
      </div>

      <div class="col-span-1">
        <BmcBlock :block="getBlock('ch')" @click="activeBlock = 'ch'" :active="activeBlock === 'ch'" />
      </div>

      <div class="col-span-1 space-y-2">
        <BmcBlock :block="getBlock('cs')" @click="activeBlock = 'cs'" :active="activeBlock === 'cs'" />
      </div>

      <div class="col-span-1 space-y-2">
        <BmcBlock :block="getCostBlock()" @click="activeBlock = 'cost'" :active="activeBlock === 'cost'" />
        <BmcBlock :block="getBlock('rs')" @click="activeBlock = 'rs'" :active="activeBlock === 'rs'" />
      </div>
    </div>

    <div v-if="activeBlockData" class="mt-4 p-4 rounded-card bg-slate-800/50 border border-slate-700">
      <div class="flex items-center justify-between mb-3">
        <h3 class="text-h4 text-white">{{ activeBlockData.label }}</h3>
        <div class="flex items-center gap-2">
          <span class="text-caption text-slate-400">VVV:</span>
          <div class="w-20 h-2 bg-slate-700 rounded-full overflow-hidden">
            <div
              class="h-full rounded-full"
              :class="vvvBarClass(activeBlockData.vvv)"
              :style="{ width: `${activeBlockData.vvv * 100}%` }"
            />
          </div>
          <span class="text-caption font-mono" :class="vvvTextClass(activeBlockData.vvv)">
            {{ activeBlockData.vvv.toFixed(2) }}
          </span>
          <button
            @click.stop="toggleInfo(activeBlock)"
            class="shrink-0 w-5 h-5 flex items-center justify-center rounded-full text-xs transition-colors"
            :class="expandedInfo.has(activeBlock) ? 'bg-accent-600 text-white' : 'bg-slate-700 text-slate-400 hover:bg-slate-600'"
            title="Ver fonte e detalhes"
          >i</button>
        </div>
      </div>

      <div v-if="expandedInfo.has(activeBlock)" class="space-y-1 border-t border-slate-700/50 mb-3 pt-1.5">
        <p class="text-caption text-slate-400">VVV: {{ activeBlockData.vvv.toFixed(2) }} — {{ vvvExplanation(activeBlockData.vvv) }}</p>
        <div class="flex items-center gap-2 flex-wrap">
          <span class="text-caption text-slate-500">Fonte:</span>
          <span class="text-accent-400 text-xs">{{ activeBlockData.fonte || 'Nao mapeada' }}</span>
        </div>
      </div>

      <div class="grid md:grid-cols-2 gap-3">
        <div v-for="(item, i) in activeBlockData.items" :key="i"
          class="flex items-start gap-2 p-2 rounded-lg bg-black/20">
          <span class="text-accent-400 shrink-0">&#8226;</span>
          <p class="text-body-sm text-slate-300">{{ item }}</p>
        </div>
      </div>

      <div v-if="activeBlockData.kpi" class="mt-3 pt-3 border-t border-slate-700">
        <span class="text-caption text-slate-400">KPI: </span>
        <span class="text-body-sm text-accent-400">{{ activeBlockData.kpi }}</span>
      </div>
    </div>

    <div v-if="showGaps && bmc.gaps?.length" class="mt-4 p-4 rounded-card bg-yellow-950/20 border border-yellow-900/30">
      <h3 class="text-h4 text-yellow-400 mb-2">Gaps Identificados</h3>
      <div class="grid md:grid-cols-3 gap-2">
        <div v-for="gap in bmc.gaps" :key="gap"
          class="flex items-start gap-2 p-2 rounded-lg bg-black/20">
          <span class="text-yellow-500">&#9888;</span>
          <p class="text-body-sm text-slate-300">{{ gap }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, reactive, h } from 'vue'

const props = defineProps({ bmc: { type: Object, default: () => ({}) } })

const activeBlock = ref(null)
const showGaps = ref(false)
const expandedInfo = reactive(new Set())

const toggleInfo = (key) => {
  expandedInfo.has(key) ? expandedInfo.delete(key) : expandedInfo.add(key)
}

const vvvExplanation = (vvv) => {
  if (vvv >= 0.95) return 'Fato verificado (transcricao/fonte oficial)'
  if (vvv >= 0.8) return 'Fonte oficial citada com confianca alta'
  if (vvv >= 0.5) return 'Analise fundamentada, parcialmente verificada'
  return 'Gap — nao verificado, necessita pesquisa'
}

const getBlock = (id) => {
  return props.bmc.blocks?.find((b) => b.id === id) || { id, label: id, items: [], vvv: 0 }
}

const getCostBlock = () => {
  const block = props.bmc.blocks?.find((b) => b.label === 'Cost Structure')
  return block || { id: 'cost', label: 'Cost Structure', items: [], vvv: 0 }
}

const activeBlockData = computed(() => {
  if (!activeBlock.value) return null
  if (activeBlock.value === 'cost') return getCostBlock()
  return getBlock(activeBlock.value)
})

const vvvBarClass = (vvv) => {
  if (vvv >= 0.9) return 'bg-green-500'
  if (vvv >= 0.7) return 'bg-green-400'
  if (vvv >= 0.5) return 'bg-yellow-500'
  return 'bg-red-500'
}

const vvvTextClass = (vvv) => {
  if (vvv >= 0.8) return 'text-green-400'
  if (vvv >= 0.5) return 'text-yellow-400'
  return 'text-red-400'
}

const BmcBlock = {
  props: {
    block: { type: Object, required: true },
    active: { type: Boolean, default: false },
    highlight: { type: Boolean, default: false },
  },
  emits: ['click'],
  setup(blockProps, { emit }) {
    return () => h(
      'div',
      {
        class: [
          'rounded-lg border p-3 cursor-pointer transition-all',
          blockProps.active
            ? 'border-accent-500 bg-accent-950/30'
            : blockProps.highlight
              ? 'border-blue-900/50 bg-blue-950/20 hover:border-blue-700'
              : 'border-slate-700 bg-slate-800/50 hover:border-slate-500',
        ],
        onClick: () => emit('click'),
      },
      [
        h('div', { class: 'flex items-center justify-between mb-2' }, [
          h('h3', {
            class: [
              'text-caption font-bold',
              blockProps.highlight ? 'text-blue-400' : 'text-accent-400',
            ],
          }, blockProps.block.label),
          h('span', {
            class: [
              'text-caption font-mono px-1 rounded',
              blockProps.block.vvv >= 0.8
                ? 'bg-green-900/50 text-green-400'
                : blockProps.block.vvv >= 0.5
                  ? 'bg-yellow-900/50 text-yellow-400'
                  : 'bg-red-900/50 text-red-400',
            ],
          }, blockProps.block.vvv?.toFixed(1) || '0.0'),
        ]),
        h('ul', { class: 'space-y-0.5' },
          blockProps.block.items?.slice(0, 4).map((item, i) =>
            h('li', { key: i, class: 'text-caption text-slate-400 truncate' }, item)
          )
        ),
      ]
    )
  },
}
</script>
