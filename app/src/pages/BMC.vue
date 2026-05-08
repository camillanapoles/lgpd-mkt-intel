<template>
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
    <!-- Header -->
    <div class="mb-6">
      <h1 class="font-display text-3xl font-bold text-slate-900">Business Model Canvas</h1>
      <p class="text-slate-600 mt-2">Modelo de negocios - Contabilizei da Privacy</p>
      <div class="flex items-center gap-3 mt-3">
        <span class="badge badge-success">Interativo</span>
        <span class="text-sm text-slate-500">Clique nos blocos para detalhes</span>
      </div>
    </div>

    <!-- VVV Filter -->
    <div class="mb-6 flex items-center gap-3">
      <span class="text-sm font-medium text-slate-700">Filtrar VVV:</span>
      <div class="flex gap-2">
        <button
          v-for="level in vvvFilters"
          :key="level.value"
          :class="[
            'px-3 py-1 rounded-full text-xs font-medium border transition-colors',
            activeFilter === level.value
              ? 'bg-slate-800 text-white border-slate-800'
              : 'bg-white text-slate-600 border-slate-300 hover:border-slate-400'
          ]"
          @click="activeFilter = activeFilter === level.value ? null : level.value"
        >
          {{ level.label }}
        </button>
      </div>
    </div>

    <!-- BMC Canvas -->
    <div class="grid grid-cols-5 gap-3 mb-3">
      <!-- Row 1: KP | KA | VP | CR | CS -->
      <BmcBlock
        :block="getBlock('kp')"
        :is-expanded="expandedId === 'kp'"
        :is-highlighted="isHighlighted('kp')"
        :related-ids="getRelatedIds('kp')"
        @toggle="toggleBlock('kp')"
        @mouseenter="hoveredId = 'kp'"
        @mouseleave="hoveredId = null"
      />
      <BmcBlock
        :block="getBlock('ka')"
        :is-expanded="expandedId === 'ka'"
        :is-highlighted="isHighlighted('ka')"
        :related-ids="getRelatedIds('ka')"
        @toggle="toggleBlock('ka')"
        @mouseenter="hoveredId = 'ka'"
        @mouseleave="hoveredId = null"
      />
      <BmcBlock
        :block="getBlock('vp')"
        :is-expanded="expandedId === 'vp'"
        :is-highlighted="isHighlighted('vp')"
        :related-ids="getRelatedIds('vp')"
        :is-center="true"
        @toggle="toggleBlock('vp')"
        @mouseenter="hoveredId = 'vp'"
        @mouseleave="hoveredId = null"
      />
      <BmcBlock
        :block="getBlock('cr')"
        :is-expanded="expandedId === 'cr'"
        :is-highlighted="isHighlighted('cr')"
        :related-ids="getRelatedIds('cr')"
        @toggle="toggleBlock('cr')"
        @mouseenter="hoveredId = 'cr'"
        @mouseleave="hoveredId = null"
      />
      <BmcBlock
        :block="getBlock('cs')"
        :is-expanded="expandedId === 'cs'"
        :is-highlighted="isHighlighted('cs')"
        :related-ids="getRelatedIds('cs')"
        @toggle="toggleBlock('cs')"
        @mouseenter="hoveredId = 'cs'"
        @mouseleave="hoveredId = null"
      />

      <!-- Row 2: KR | CH (spanning under their parent columns) -->
      <BmcBlock
        :block="getBlock('kr')"
        :is-expanded="expandedId === 'kr'"
        :is-highlighted="isHighlighted('kr')"
        :related-ids="getRelatedIds('kr')"
        @toggle="toggleBlock('kr')"
        @mouseenter="hoveredId = 'kr'"
        @mouseleave="hoveredId = null"
      />
      <div></div>
      <div></div>
      <BmcBlock
        :block="getBlock('ch')"
        :is-expanded="expandedId === 'ch'"
        :is-highlighted="isHighlighted('ch')"
        :related-ids="getRelatedIds('ch')"
        @toggle="toggleBlock('ch')"
        @mouseenter="hoveredId = 'ch'"
        @mouseleave="hoveredId = null"
      />
      <div></div>
    </div>

    <!-- Row 3: Cost Structure | Revenue Streams -->
    <div class="grid grid-cols-5 gap-3 mb-8">
      <div class="col-span-3">
        <BmcBlock
          :block="getBlock('cst')"
          :is-expanded="expandedId === 'cst'"
          :is-highlighted="isHighlighted('cst')"
          :related-ids="getRelatedIds('cst')"
          @toggle="toggleBlock('cst')"
          @mouseenter="hoveredId = 'cst'"
          @mouseleave="hoveredId = null"
        />
      </div>
      <div class="col-span-2">
        <BmcBlock
          :block="getBlock('rs')"
          :is-expanded="expandedId === 'rs'"
          :is-highlighted="isHighlighted('rs')"
          :related-ids="getRelatedIds('rs')"
          @toggle="toggleBlock('rs')"
          @mouseenter="hoveredId = 'rs'"
          @mouseleave="hoveredId = null"
        />
      </div>
    </div>

    <!-- Relationships Legend -->
    <div class="card p-4 mb-6">
      <h3 class="font-display font-semibold text-slate-900 mb-3">Relacionamentos</h3>
      <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-2">
        <div
          v-for="rel in relationships"
          :key="rel.id"
          class="flex items-center gap-2 text-sm px-3 py-2 rounded-lg bg-slate-50"
        >
          <span :class="relationshipDotClass(rel.strength)"></span>
          <span class="text-slate-600">{{ getBlockTitle(rel.from) }}</span>
          <span class="text-slate-400">{{ getRelArrow(rel.type) }}</span>
          <span class="text-slate-600">{{ getBlockTitle(rel.to) }}</span>
        </div>
      </div>
    </div>

    <!-- Gaps & Validation Notes -->
    <div class="card p-6">
      <h3 class="font-display font-semibold text-slate-900 mb-4">Gaps & Notas de Validacao</h3>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div v-for="note in validationNotes" :key="note.id">
          <h4 :class="['font-medium mb-3', noteCategoryClass(note.category)]">{{ note.title }}</h4>
          <ul class="space-y-2">
            <li
              v-for="(item, idx) in note.items"
              :key="idx"
              class="flex items-start gap-2 text-sm text-slate-600"
            >
              <span :class="noteBulletClass(note.category)">-</span>
              <span>{{ item }}</span>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import bmcData from '../../bmc-interactive.json'

const blocks = bmcData.canvas.blocks
const relationships = bmcData.relationships
const validationNotes = bmcData.validation_notes

const expandedId = ref(null)
const hoveredId = ref(null)
const activeFilter = ref(null)

const vvvFilters = [
  { value: 'high', label: 'Alto (>0.8)' },
  { value: 'medium', label: 'Medio (0.5-0.8)' },
  { value: 'low', label: 'Baixo (<0.5)' }
]

function getBlock(id) {
  return blocks.find(b => b.id === id)
}

function getBlockTitle(id) {
  const block = getBlock(id)
  return block ? block.title.split(' ')[0] : id.toUpperCase()
}

function toggleBlock(id) {
  expandedId.value = expandedId.value === id ? null : id
}

const relationshipMap = computed(() => {
  const map = {}
  for (const rel of relationships) {
    if (!map[rel.from]) map[rel.from] = new Set()
    if (!map[rel.to]) map[rel.to] = new Set()
    map[rel.from].add(rel.to)
    map[rel.to].add(rel.from)
  }
  return map
})

function getRelatedIds(id) {
  return relationshipMap.value[id] ? [...relationshipMap.value[id]] : []
}

function isHighlighted(id) {
  if (!hoveredId.value) return false
  if (hoveredId.value === id) return true
  const related = relationshipMap.value[hoveredId.value]
  return related ? related.has(id) : false
}

function getRelArrow(type) {
  const arrows = {
    enables: '->',
    creates: '=>',
    required_for: '->',
    delivers_to: '=>',
    maintains: '->',
    reaches: '->',
    funds: '->',
    generates: '=>',
    justifies: '->',
    channel_to: '->',
    amplifies: '->',
    supports: '->'
  }
  return arrows[type] || '->'
}

function relationshipDotClass(strength) {
  const classes = {
    critical: 'w-2 h-2 rounded-full bg-red-500 flex-shrink-0 mt-1.5',
    strong: 'w-2 h-2 rounded-full bg-blue-500 flex-shrink-0 mt-1.5',
    medium: 'w-2 h-2 rounded-full bg-slate-400 flex-shrink-0 mt-1.5'
  }
  return classes[strength] || classes.medium
}

function noteCategoryClass(category) {
  const classes = {
    critical_gaps: 'text-red-700',
    next_steps: 'text-blue-700',
    competitive_threats: 'text-amber-700',
    validated_strengths: 'text-green-700'
  }
  return classes[category] || 'text-slate-700'
}

function noteBulletClass(category) {
  const classes = {
    critical_gaps: 'text-red-500 font-bold',
    next_steps: 'text-blue-500 font-bold',
    competitive_threats: 'text-amber-500 font-bold',
    validated_strengths: 'text-green-500 font-bold'
  }
  return classes[category] || 'text-slate-400'
}
</script>

<script>
export default {
  inheritAttrs: false
}

const STATUS_CLASSES = {
  validated: 'bg-green-100 text-green-800',
  in_development: 'bg-blue-100 text-blue-800',
  in_progress: 'bg-blue-100 text-blue-800',
  needs_validation: 'bg-amber-100 text-amber-800',
  planned: 'bg-slate-100 text-slate-600'
}

const STATUS_LABELS = {
  validated: 'Validado',
  in_development: 'Em dev',
  in_progress: 'Em andamento',
  needs_validation: 'Validar',
  planned: 'Planejado'
}
</script>

<script setup>
const BmcBlock = {
  name: 'BmcBlock',
  props: {
    block: { type: Object, default: null },
    isExpanded: { type: Boolean, default: false },
    isHighlighted: { type: Boolean, default: false },
    isCenter: { type: Boolean, default: false },
    relatedIds: { type: Array, default: () => [] }
  },
  emits: ['toggle', 'mouseenter', 'mouseleave'],
  setup() {
    return { STATUS_CLASSES, STATUS_LABELS }
  },
  template: `
    <div
      v-if="block"
      :class="[
        'card p-4 cursor-pointer transition-all duration-200 flex flex-col',
        isExpanded ? 'ring-2 ring-primary-400 shadow-lg' : '',
        isHighlighted && !isExpanded ? 'ring-2 ring-blue-300 bg-blue-50/30' : '',
        isCenter && !isExpanded && !isHighlighted ? 'border-2 border-primary-200 bg-primary-50/30' : ''
      ]"
      @click="$emit('toggle')"
      @mouseenter="$emit('mouseenter')"
      @mouseleave="$emit('mouseleave')"
    >
      <!-- Block Header -->
      <div class="flex items-center justify-between mb-2">
        <h3 class="font-semibold text-sm text-slate-900 truncate">{{ block.title }}</h3>
        <span
          :class="[
            'text-xs font-bold px-2 py-0.5 rounded-full',
            vvvBadgeClass(block.vvv_score)
          ]"
        >
          VVV {{ (block.vvv_score * 100).toFixed(0) }}%
        </span>
      </div>

      <!-- Collapsed: Items Summary -->
      <div v-if="!isExpanded" class="flex-1">
        <ul class="space-y-1">
          <li
            v-for="item in block.items.slice(0, 3)"
            :key="item.id"
            class="text-xs text-slate-600 flex items-start gap-1.5"
          >
            <span class="mt-0.5" :class="statusDotClass(item.status)">*</span>
            <span class="line-clamp-1">{{ item.text }}</span>
          </li>
          <li v-if="block.items.length > 3" class="text-xs text-slate-400 italic">
            +{{ block.items.length - 3 }} mais
          </li>
        </ul>

        <!-- KPI Summary -->
        <div v-if="block.kpis && block.kpis.length" class="mt-3 pt-2 border-t border-slate-100">
          <p
            v-for="kpi in block.kpis.slice(0, 1)"
            :key="kpi.name"
            class="text-xs text-slate-500"
          >
            {{ kpi.name }}: {{ kpi.current !== false ? kpi.current : '-' }}/{{ kpi.target }} {{ kpi.unit }}
          </p>
        </div>
      </div>

      <!-- Expanded: Full Details -->
      <div v-else class="flex-1">
        <!-- Items with descriptions -->
        <div class="space-y-2">
          <div
            v-for="item in block.items"
            :key="item.id"
            class="p-2 rounded-lg bg-slate-50"
          >
            <div class="flex items-start justify-between gap-1">
              <div class="flex-1 min-w-0">
                <p class="text-sm font-medium text-slate-800">{{ item.text }}</p>
                <p class="text-xs text-slate-500 mt-0.5">{{ item.description }}</p>
              </div>
              <div class="flex items-center gap-1.5 flex-shrink-0">
                <span
                  :class="[
                    'inline-flex items-center px-1.5 py-0.5 rounded text-xs font-medium',
                    STATUS_CLASSES[item.status] || STATUS_CLASSES.planned
                  ]"
                >
                  {{ STATUS_LABELS[item.status] || item.status }}
                </span>
                <span
                  :class="[
                    'text-xs font-bold',
                    item.vvv >= 0.8 ? 'text-green-600' : item.vvv >= 0.5 ? 'text-amber-600' : 'text-red-600'
                  ]"
                >
                  {{ (item.vvv * 100).toFixed(0) }}%
                </span>
              </div>
            </div>
          </div>
        </div>

        <!-- KPIs -->
        <div v-if="block.kpis && block.kpis.length" class="mt-3 pt-3 border-t border-slate-200">
          <p class="text-xs font-medium text-slate-700 mb-2">KPIs</p>
          <div class="space-y-2">
            <div v-for="kpi in block.kpis" :key="kpi.name" class="flex items-center justify-between">
              <span class="text-xs text-slate-600">{{ kpi.name }}</span>
              <div class="flex items-center gap-2">
                <div class="w-20 bg-slate-200 rounded-full h-1.5">
                  <div
                    class="bg-primary-600 h-1.5 rounded-full transition-all"
                    :style="{ width: kpiProgress(kpi) + '%' }"
                  ></div>
                </div>
                <span class="text-xs text-slate-500 w-16 text-right">
                  {{ kpi.current !== false ? kpi.current : 0 }}/{{ kpi.target }}
                </span>
              </div>
            </div>
          </div>
        </div>

        <!-- Notes -->
        <div v-if="block.notes && block.notes.length" class="mt-3 pt-3 border-t border-slate-200">
          <div class="space-y-1">
            <p v-for="(note, idx) in block.notes" :key="idx" class="text-xs text-slate-500">
              {{ note }}
            </p>
          </div>
        </div>
      </div>
    </div>
  `,
  methods: {
    vvvBadgeClass(score) {
      if (score >= 0.8) return 'bg-green-100 text-green-800'
      if (score >= 0.5) return 'bg-amber-100 text-amber-800'
      return 'bg-red-100 text-red-800'
    },
    statusDotClass(status) {
      const classes = {
        validated: 'text-green-500',
        in_development: 'text-blue-500',
        in_progress: 'text-blue-500',
        needs_validation: 'text-amber-500',
        planned: 'text-slate-400'
      }
      return classes[status] || 'text-slate-400'
    },
    kpiProgress(kpi) {
      const current = kpi.current === false ? 0 : kpi.current
      if (typeof kpi.target === 'boolean') return kpi.current ? 100 : 0
      const pct = (current / kpi.target) * 100
      return Math.min(100, Math.max(0, pct))
    }
  }
}
</script>
