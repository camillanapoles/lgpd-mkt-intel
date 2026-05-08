<template>
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
    <!-- Header -->
    <div class="mb-6">
      <h1 class="font-display text-3xl font-bold text-slate-900">Analise SWOT</h1>
      <p class="text-slate-600 mt-2">Forcas, Fracas, Oportunidades e Ameacas</p>
    </div>

    <!-- Filter Buttons -->
    <div class="flex flex-wrap items-center gap-3 mb-6">
      <span class="text-sm font-medium text-slate-600">Filtrar:</span>
      <button
        v-for="cat in categories"
        :key="cat.key"
        @click="toggleFilter(cat.key)"
        :class="[
          'px-4 py-2 rounded-lg text-sm font-medium transition-all border',
          activeFilters.has(cat.key)
            ? `${cat.activeBg} ${cat.activeText} ${cat.activeBorder} shadow-sm`
            : 'bg-slate-100 text-slate-500 border-slate-200 hover:bg-slate-200'
        ]"
      >
        {{ cat.label }}
        <span class="ml-1 text-xs opacity-75">({{ getCategoryCount(cat.key) }})</span>
      </button>
      <button
        v-if="activeFilters.size > 0"
        @click="activeFilters.clear()"
        class="px-3 py-2 rounded-lg text-sm text-slate-500 hover:text-slate-700 hover:bg-slate-100"
      >
        Limpar
      </button>
    </div>

    <!-- SWOT Grid -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
      <!-- Strengths -->
      <div v-if="showCategory('S')" class="card p-6 border-t-4 border-green-500">
        <div class="flex items-center gap-3 mb-4">
          <div class="w-10 h-10 rounded-lg bg-green-100 flex items-center justify-center">
            <svg class="w-6 h-6 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
          </div>
          <div>
            <h2 class="font-display text-lg font-semibold text-green-800">STRENGTHS</h2>
            <p class="text-sm text-green-600">Pontos Fortes Internos</p>
          </div>
        </div>
        <div class="space-y-3">
          <div
            v-for="item in strengths"
            :key="item.id"
            class="p-3 bg-green-50 rounded-lg cursor-pointer hover:bg-green-100 transition-colors"
            @click="toggleExpanded(item.id)"
          >
            <div class="flex items-start justify-between gap-2">
              <div class="flex-1">
                <div class="flex items-center gap-2">
                  <span class="font-mono text-xs text-green-600 font-bold">{{ item.id }}</span>
                  <span :class="vvvBadgeClass(item.vvv)" class="text-xs font-semibold px-1.5 py-0.5 rounded">
                    VVV {{ item.vvv.toFixed(1) }}
                  </span>
                </div>
                <p class="text-sm text-slate-700 mt-1">{{ item.text }}</p>
              </div>
              <span :class="`badge ${getImpactBadgeClass(item.impact)}`">{{ item.impact }}</span>
            </div>
            <!-- Expandable source/detail -->
            <div v-if="expandedItems.has(item.id)" class="mt-2 pt-2 border-t border-green-200">
              <p class="text-xs text-slate-500">
                <strong>Fonte:</strong> {{ item.source }}
              </p>
              <p class="text-xs text-slate-500 mt-1">
                <strong>Impacto:</strong> {{ item.impact }} | <strong>VVV:</strong> {{ item.vvv.toFixed(2) }}
              </p>
            </div>
          </div>
        </div>

        <!-- Top Actions -->
        <div v-if="topActions.strengths.length" class="mt-4 pt-4 border-t border-green-200">
          <h4 class="text-sm font-semibold text-green-800 mb-2">Acoes Prioritarias</h4>
          <div class="space-y-1.5">
            <div v-for="(action, idx) in topActions.strengths" :key="idx" class="flex items-start gap-2">
              <span class="text-xs font-bold text-green-600 mt-0.5">{{ idx + 1 }}.</span>
              <p class="text-xs text-slate-700">{{ action }}</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Weaknesses -->
      <div v-if="showCategory('W')" class="card p-6 border-t-4 border-red-500">
        <div class="flex items-center gap-3 mb-4">
          <div class="w-10 h-10 rounded-lg bg-red-100 flex items-center justify-center">
            <svg class="w-6 h-6 text-red-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
            </svg>
          </div>
          <div>
            <h2 class="font-display text-lg font-semibold text-red-800">WEAKNESSES</h2>
            <p class="text-sm text-red-600">Fracas Internas</p>
          </div>
        </div>
        <div class="space-y-3">
          <div
            v-for="item in weaknesses"
            :key="item.id"
            class="p-3 bg-red-50 rounded-lg cursor-pointer hover:bg-red-100 transition-colors"
            @click="toggleExpanded(item.id)"
          >
            <div class="flex items-start justify-between gap-2">
              <div class="flex-1">
                <div class="flex items-center gap-2">
                  <span class="font-mono text-xs text-red-600 font-bold">{{ item.id }}</span>
                  <span :class="vvvBadgeClass(item.vvv)" class="text-xs font-semibold px-1.5 py-0.5 rounded">
                    VVV {{ item.vvv.toFixed(1) }}
                  </span>
                </div>
                <p class="text-sm text-slate-700 mt-1">{{ item.text }}</p>
              </div>
              <span :class="`badge ${getImpactBadgeClass(item.impact)}`">{{ item.impact }}</span>
            </div>
            <div v-if="expandedItems.has(item.id)" class="mt-2 pt-2 border-t border-red-200">
              <p class="text-xs text-slate-500">
                <strong>Fonte:</strong> {{ item.source }}
              </p>
              <p class="text-xs text-slate-500 mt-1">
                <strong>Impacto:</strong> {{ item.impact }} | <strong>VVV:</strong> {{ item.vvv.toFixed(2) }}
              </p>
            </div>
          </div>
        </div>

        <!-- Top Actions -->
        <div v-if="topActions.weaknesses.length" class="mt-4 pt-4 border-t border-red-200">
          <h4 class="text-sm font-semibold text-red-800 mb-2">Acoes Prioritarias</h4>
          <div class="space-y-1.5">
            <div v-for="(action, idx) in topActions.weaknesses" :key="idx" class="flex items-start gap-2">
              <span class="text-xs font-bold text-red-600 mt-0.5">{{ idx + 1 }}.</span>
              <p class="text-xs text-slate-700">{{ action }}</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Opportunities -->
      <div v-if="showCategory('O')" class="card p-6 border-t-4 border-blue-500">
        <div class="flex items-center gap-3 mb-4">
          <div class="w-10 h-10 rounded-lg bg-blue-100 flex items-center justify-center">
            <svg class="w-6 h-6 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
            </svg>
          </div>
          <div>
            <h2 class="font-display text-lg font-semibold text-blue-800">OPPORTUNITIES</h2>
            <p class="text-sm text-blue-600">Oportunidades Externas</p>
          </div>
        </div>
        <div class="space-y-3">
          <div
            v-for="item in opportunities"
            :key="item.id"
            class="p-3 bg-blue-50 rounded-lg cursor-pointer hover:bg-blue-100 transition-colors"
            @click="toggleExpanded(item.id)"
          >
            <div class="flex items-start justify-between gap-2">
              <div class="flex-1">
                <div class="flex items-center gap-2">
                  <span class="font-mono text-xs text-blue-600 font-bold">{{ item.id }}</span>
                  <span :class="vvvBadgeClass(item.vvv)" class="text-xs font-semibold px-1.5 py-0.5 rounded">
                    VVV {{ item.vvv.toFixed(1) }}
                  </span>
                </div>
                <p class="text-sm text-slate-700 mt-1">{{ item.text }}</p>
              </div>
              <span :class="`badge ${getImpactBadgeClass(item.impact)}`">{{ item.impact }}</span>
            </div>
            <div v-if="expandedItems.has(item.id)" class="mt-2 pt-2 border-t border-blue-200">
              <p class="text-xs text-slate-500">
                <strong>Fonte:</strong> {{ item.source }}
              </p>
              <p class="text-xs text-slate-500 mt-1">
                <strong>Impacto:</strong> {{ item.impact }} | <strong>VVV:</strong> {{ item.vvv.toFixed(2) }}
              </p>
            </div>
          </div>
        </div>

        <!-- Top Actions -->
        <TopActions v-if="topActions.opportunities.length" :actions="topActions.opportunities" color="blue" />
      </div>

      <!-- Threats -->
      <div v-if="showCategory('T')" class="card p-6 border-t-4 border-amber-500">
        <div class="flex items-center gap-3 mb-4">
          <div class="w-10 h-10 rounded-lg bg-amber-100 flex items-center justify-center">
            <svg class="w-6 h-6 text-amber-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
          </div>
          <div>
            <h2 class="font-display text-lg font-semibold text-amber-800">THREATS</h2>
            <p class="text-sm text-amber-600">Ameacas Externas</p>
          </div>
        </div>
        <div class="space-y-3">
          <div
            v-for="item in threats"
            :key="item.id"
            class="p-3 bg-amber-50 rounded-lg cursor-pointer hover:bg-amber-100 transition-colors"
            @click="toggleExpanded(item.id)"
          >
            <div class="flex items-start justify-between gap-2">
              <div class="flex-1">
                <div class="flex items-center gap-2">
                  <span class="font-mono text-xs text-amber-600 font-bold">{{ item.id }}</span>
                  <span :class="vvvBadgeClass(item.vvv)" class="text-xs font-semibold px-1.5 py-0.5 rounded">
                    VVV {{ item.vvv.toFixed(1) }}
                  </span>
                </div>
                <p class="text-sm text-slate-700 mt-1">{{ item.text }}</p>
              </div>
              <span :class="`badge ${getImpactBadgeClass(item.impact)}`">{{ item.impact }}</span>
            </div>
            <div v-if="expandedItems.has(item.id)" class="mt-2 pt-2 border-t border-amber-200">
              <p class="text-xs text-slate-500">
                <strong>Fonte:</strong> {{ item.source }}
              </p>
              <p class="text-xs text-slate-500 mt-1">
                <strong>Impacto:</strong> {{ item.impact }} | <strong>VVV:</strong> {{ item.vvv.toFixed(2) }}
              </p>
            </div>
          </div>
        </div>

        <!-- Top Actions -->
        <TopActions v-if="topActions.threats.length" :actions="topActions.threats" color="amber" />
      </div>
    </div>

    <!-- Strategic Summary -->
    <div class="card p-6">
      <h3 class="font-display text-lg font-semibold text-slate-900 mb-4">Resumo Estrategico</h3>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div class="p-4 bg-green-50 rounded-lg border border-green-200">
          <h4 class="font-medium text-green-800 mb-2">Forcas Estrategicas</h4>
          <p class="text-sm text-slate-700">
            <strong>S1 + S2 =</strong> Gap de mercado + Arbitragem regulatoria = Defesa contra entrada
          </p>
        </div>
        <div class="p-4 bg-red-50 rounded-lg border border-red-200">
          <h4 class="font-medium text-red-800 mb-2">Risco Critico</h4>
          <p class="text-sm text-slate-700">
            <strong>W1 + T4 =</strong> Sales municipal + ciclo longo = <strong>MUST resolver pre-commitment</strong>
          </p>
        </div>
        <div class="p-4 bg-blue-50 rounded-lg border border-blue-200">
          <h4 class="font-medium text-blue-800 mb-2">Aposta Principal</h4>
          <p class="text-sm text-slate-700">
            <strong>O1 + O2 =</strong> ANPD + TCE = Demanda forcada mantem janela aberta 3-5 anos
          </p>
        </div>
        <div class="p-4 bg-purple-50 rounded-lg border border-purple-200">
          <h4 class="font-medium text-purple-800 mb-2">Unfair Advantage</h4>
          <p class="text-sm text-slate-700">
            <strong>S4 + S5 =</strong> Data 100% Brasil + DPO incluido = Barreira a entrada (alto custo fixo)
          </p>
        </div>
      </div>
    </div>

    <!-- Action Items -->
    <div class="mt-6 card p-6">
      <h3 class="font-display text-lg font-semibold text-slate-900 mb-4">Acoes Imediatas</h3>
      <div class="space-y-3">
        <div class="flex items-start gap-3 p-3 bg-red-50 rounded-lg border border-red-200">
          <span class="badge badge-danger mt-0.5">CRITICO</span>
          <div>
            <p class="font-medium text-slate-900">Resolver W1: Experiencia em vendas municipais</p>
            <p class="text-sm text-slate-600">Co-founder ou advisor com track record comprovado</p>
          </div>
        </div>
        <div class="flex items-start gap-3 p-3 bg-amber-50 rounded-lg border border-amber-200">
          <span class="badge badge-warning mt-0.5">URGENTE</span>
          <div>
            <p class="font-medium text-slate-900">Mitigar T4: Ciclo de vendas longo</p>
            <p class="text-sm text-slate-600">Foco em municipios com flags do TCE (urgencia)</p>
          </div>
        </div>
        <div class="flex items-start gap-3 p-3 bg-blue-50 rounded-lg border border-blue-200">
          <span class="badge badge-info mt-0.5">OPORTUNIDADE</span>
          <div>
            <p class="font-medium text-slate-900">Capturar O1 + O2: Demanda ANPD/TCE</p>
            <p class="text-sm text-slate-600">Conteudo de marketing focado em fiscalizacao e multas</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, computed } from 'vue'
import strategicData from '../data/strategicData.js'
import unifiedData from '../../strategic-data-unified.json'

// ---------- Data mapping ----------

function deriveImpact(vvv) {
  if (vvv >= 0.7) return 'high'
  if (vvv >= 0.4) return 'medium'
  return 'low'
}

function mapSwotItems(rawItems) {
  if (!rawItems) return []
  return rawItems.map(item => ({
    id: item.id,
    text: item.text || item.texto || '',
    impact: deriveImpact(item.vvv ?? 0),
    vvv: item.vvv ?? 0,
    source: item.source || item.fonte || ''
  }))
}

// Prefer unified JSON swot_interactive, fall back to strategicData.swot
const interactive = unifiedData?.swot_interactive

const strengths = computed(() => {
  if (interactive?.forcas?.length) {
    return mapSwotItems(interactive.forcas)
  }
  return (strategicData.swot?.strengths || []).map(s => ({
    id: s.id,
    text: s.text,
    impact: s.impact?.toLowerCase() || 'medium',
    vvv: s.vvv ?? 0.5,
    source: s.source || 'strategic-planning'
  }))
})

const weaknesses = computed(() => {
  if (interactive?.fracas?.length) {
    return mapSwotItems(interactive.fracas)
  }
  return (strategicData.swot?.weaknesses || []).map(w => ({
    id: w.id,
    text: w.text,
    impact: w.impact?.toLowerCase() || 'medium',
    vvv: w.vvv ?? 0.5,
    source: w.source || 'strategic-planning',
    mitigation: w.mitigation
  }))
})

const opportunities = computed(() => {
  if (interactive?.oportunidades?.length) {
    return mapSwotItems(interactive.oportunidades)
  }
  return (strategicData.swot?.opportunities || []).map(o => ({
    id: o.id,
    text: o.text,
    impact: o.impact?.toLowerCase() || 'medium',
    vvv: o.vvv ?? 0.5,
    source: o.source || 'strategic-planning',
    timing: o.timing
  }))
})

const threats = computed(() => {
  if (interactive?.ameacas?.length) {
    return mapSwotItems(interactive.ameacas)
  }
  return (strategicData.swot?.threats || []).map(t => ({
    id: t.id,
    text: t.text,
    impact: t.impact?.toLowerCase() || 'medium',
    vvv: t.vvv ?? 0.5,
    source: t.source || 'strategic-planning',
    mitigation: t.mitigation
  }))
})

// Top actions per quadrant
const topActions = computed(() => {
  const raw = interactive?.top_actions || {}
  return {
    strengths: raw.forcas || [],
    weaknesses: raw.fracas || [],
    opportunities: raw.oportunidades || [],
    threats: raw.ameacas || []
  }
})

// ---------- Filters ----------

const activeFilters = reactive(new Set())

const categories = [
  { key: 'S', label: 'Strengths', activeBg: 'bg-green-100', activeText: 'text-green-800', activeBorder: 'border-green-300' },
  { key: 'W', label: 'Weaknesses', activeBg: 'bg-red-100', activeText: 'text-red-800', activeBorder: 'border-red-300' },
  { key: 'O', label: 'Opportunities', activeBg: 'bg-blue-100', activeText: 'text-blue-800', activeBorder: 'border-blue-300' },
  { key: 'T', label: 'Threats', activeBg: 'bg-amber-100', activeText: 'text-amber-800', activeBorder: 'border-amber-300' }
]

function toggleFilter(key) {
  if (activeFilters.has(key)) {
    activeFilters.delete(key)
  } else {
    activeFilters.add(key)
  }
}

function showCategory(key) {
  if (activeFilters.size === 0) return true
  return activeFilters.has(key)
}

function getCategoryCount(key) {
  const counts = { S: strengths.value.length, W: weaknesses.value.length, O: opportunities.value.length, T: threats.value.length }
  return counts[key] || 0
}

// ---------- Expandable items ----------

const expandedItems = reactive(new Set())

function toggleExpanded(id) {
  if (expandedItems.has(id)) {
    expandedItems.delete(id)
  } else {
    expandedItems.add(id)
  }
}

// ---------- Badge helpers ----------

function vvvBadgeClass(vvv) {
  if (vvv >= 0.7) return 'bg-green-600 text-white'
  if (vvv >= 0.4) return 'bg-yellow-500 text-white'
  return 'bg-red-600 text-white'
}

function getImpactBadgeClass(impact) {
  const normalized = (impact || '').toLowerCase()
  if (normalized === 'high' || normalized === 'alto' || normalized === 'critica' || normalized === 'critico') return 'badge-danger'
  if (normalized === 'medium' || normalized === 'medio' || normalized === 'media') return 'badge-warning'
  return 'badge-success'
}
</script>
