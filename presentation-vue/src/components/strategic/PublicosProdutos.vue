<template>
  <div class="space-y-6">
    <div>
      <h2 class="text-2xl font-bold text-white mb-1">Públicos & Produtos</h2>
      <p class="text-sm text-slate-400">
        Para cada público-alvo (cluster), veja os produtos da CIT AI Tech que o atendem.
        Clique no <span class="inline-flex items-center justify-center w-4 h-4 rounded-full bg-blue-600/30 border border-blue-500 text-blue-300 text-[10px] font-bold">i</span>
        para a explicação completa.
      </p>
    </div>

    <!-- Filtro de cluster -->
    <div class="flex flex-wrap gap-2">
      <button
        @click="selectedCluster = 'all'"
        :class="['px-3 py-1.5 rounded-lg text-xs transition-all border',
          selectedCluster === 'all' ? 'bg-blue-600 text-white border-blue-500' : 'bg-slate-800 text-slate-300 border-slate-700 hover:border-slate-500']"
      >Todos ({{ clusters.length }})</button>
      <button
        v-for="cl in clusters" :key="cl.id"
        @click="selectedCluster = cl.id"
        :class="['px-3 py-1.5 rounded-lg text-xs transition-all border',
          selectedCluster === cl.id ? 'bg-blue-600 text-white border-blue-500' : 'bg-slate-800 text-slate-300 border-slate-700 hover:border-slate-500']"
      >
        <span class="mr-1">{{ cl.emoji }}</span>{{ cl.name }}
      </button>
    </div>

    <!-- Clusters -->
    <div v-for="cl in filteredClusters" :key="cl.id" class="bg-slate-900/40 border border-slate-700 rounded-2xl p-5">
      <!-- Cluster header -->
      <div class="flex items-start justify-between mb-4 gap-4">
        <div class="flex-1">
          <div class="flex items-center gap-3 mb-2">
            <span class="text-3xl">{{ cl.emoji }}</span>
            <div>
              <h3 class="text-xl font-bold text-white">{{ cl.name }}</h3>
              <p class="text-xs text-slate-400">
                Wave {{ cl.wave }} · {{ formatStatus(cl.status) }}
                <span v-if="cl.universe_size" class="ml-2">· Universo: {{ formatNumber(cl.universe_size) }} {{ cl.universe_unit }}</span>
              </p>
            </div>
          </div>
          <p class="text-sm text-slate-300 leading-relaxed">
            <span class="text-slate-400">Dor LGPD:</span> {{ cl.lgpd_pain }}
          </p>
        </div>
        <div class="text-right shrink-0">
          <div class="text-xs text-slate-500 uppercase">FDC-U</div>
          <div :class="['text-2xl font-bold', scoreColor(cl.fdc_u_score)]">
            {{ cl.fdc_u_score?.toFixed?.(2) ?? '—' }}
          </div>
          <div class="text-xs text-slate-500">rank #{{ cl.fdc_u_rank ?? '—' }}</div>
        </div>
      </div>

      <!-- Produtos do cluster -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
        <div
          v-for="pid in cl.products_core" :key="pid"
          class="bg-slate-950/60 border border-slate-700 rounded-xl p-4 hover:border-blue-500/50 transition-all"
        >
          <div class="flex items-start justify-between mb-2 gap-2">
            <div class="flex-1">
              <div class="flex items-center gap-2 mb-1">
                <span class="text-xs font-mono text-blue-400 bg-blue-950/50 px-1.5 py-0.5 rounded">{{ pid }}</span>
                <span v-if="productById(pid)?.status" :class="['text-[10px] uppercase font-bold px-1.5 py-0.5 rounded',
                  productById(pid)?.status === 'exists_today' ? 'bg-green-900/60 text-green-400' : 'bg-yellow-900/60 text-yellow-400']">
                  {{ productById(pid)?.status === 'exists_today' ? 'Existe hoje' : 'Novo ICT' }}
                </span>
                <span v-if="productById(pid)?.inpi_required" class="text-[10px] uppercase font-bold px-1.5 py-0.5 rounded bg-purple-900/60 text-purple-300">
                  INPI obrig.
                </span>
              </div>
              <h4 class="text-sm font-semibold text-white">{{ productById(pid)?.name || pid }}</h4>
            </div>
            <button
              @click="openProduct(pid)"
              class="shrink-0 inline-flex items-center justify-center w-6 h-6 rounded-full bg-blue-600/30 border border-blue-500 text-blue-300 text-xs font-bold hover:bg-blue-600/50 transition-all"
              title="Explicação completa"
            >i</button>
          </div>
          <p class="text-xs text-slate-400 leading-relaxed mb-2">
            {{ productById(pid)?.short_description || '[DADO PENDENTE]' }}
          </p>
          <div class="flex items-center justify-between text-xs">
            <span class="text-slate-500">{{ formatModel(productById(pid)?.model) }}</span>
            <span class="text-emerald-400 font-mono text-[11px]">{{ productById(pid)?.pricing_est || '—' }}</span>
          </div>
          <div class="mt-2 flex items-center gap-2">
            <div class="flex-1 h-1 bg-slate-800 rounded-full overflow-hidden">
              <div :class="['h-full', vvvBar(productById(pid)?.vvv)]" :style="{ width: ((productById(pid)?.vvv ?? 0) * 100) + '%' }"></div>
            </div>
            <span class="text-[10px] text-slate-500 font-mono">VVV {{ (productById(pid)?.vvv ?? 0).toFixed(2) }}</span>
          </div>
        </div>

        <div v-if="!cl.products_core?.length" class="col-span-full text-xs text-slate-500 italic py-4 text-center">
          Sem produtos mapeados para este público — [DADO PENDENTE]
        </div>
      </div>

      <!-- Footer cluster: canal + objeção -->
      <div class="mt-4 pt-4 border-t border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
        <div>
          <div class="text-slate-500 uppercase mb-1">Canal de venda</div>
          <div class="text-slate-300">{{ (cl.channel || []).join(' · ') }}</div>
        </div>
        <div>
          <div class="text-slate-500 uppercase mb-1">Objeção principal</div>
          <div class="text-slate-300 italic">"{{ cl.main_objection }}"</div>
          <div class="text-emerald-400 mt-1">→ {{ cl.objection_counter }}</div>
        </div>
      </div>
    </div>

    <!-- Modal explicação produto -->
    <div
      v-if="openProductId"
      class="fixed inset-0 z-50 bg-black/70 backdrop-blur-sm flex items-center justify-center p-4"
      @click.self="openProductId = null"
    >
      <div class="bg-slate-900 border border-slate-700 rounded-2xl max-w-2xl w-full max-h-[85vh] overflow-y-auto">
        <div class="p-6">
          <div class="flex items-start justify-between mb-4 gap-4">
            <div>
              <div class="flex items-center gap-2 mb-2">
                <span class="text-xs font-mono text-blue-400 bg-blue-950/50 px-2 py-0.5 rounded">{{ openProductId }}</span>
                <span v-if="openProductData?.exclusive_b2g" class="text-[10px] uppercase font-bold px-2 py-0.5 rounded bg-indigo-900/60 text-indigo-300">Exclusivo B2G</span>
                <span v-if="openProductData?.gate_poc_m4" class="text-[10px] uppercase font-bold px-2 py-0.5 rounded bg-red-900/60 text-red-300">Gate PoC M4</span>
              </div>
              <h3 class="text-xl font-bold text-white">{{ openProductData?.name }}</h3>
            </div>
            <button @click="openProductId = null" class="text-slate-500 hover:text-white text-2xl leading-none">×</button>
          </div>

          <p class="text-sm text-slate-300 mb-4 leading-relaxed">{{ openProductData?.short_description }}</p>

          <div class="space-y-3 text-sm">
            <div class="bg-slate-950/60 border border-slate-800 rounded-lg p-3">
              <div class="text-xs text-slate-500 uppercase mb-1">Origem (derived_from)</div>
              <p class="text-slate-300">{{ openProductData?.derived_from || '[DADO PENDENTE]' }}</p>
            </div>
            <div class="bg-slate-950/60 border border-slate-800 rounded-lg p-3">
              <div class="text-xs text-slate-500 uppercase mb-1">O que resolve</div>
              <p class="text-slate-300">{{ openProductData?.solves || '[DADO PENDENTE]' }}</p>
            </div>
            <div class="grid grid-cols-2 gap-3">
              <div class="bg-slate-950/60 border border-slate-800 rounded-lg p-3">
                <div class="text-xs text-slate-500 uppercase mb-1">Modelo</div>
                <p class="text-slate-300 text-xs">{{ formatModel(openProductData?.model) }}</p>
              </div>
              <div class="bg-slate-950/60 border border-slate-800 rounded-lg p-3">
                <div class="text-xs text-slate-500 uppercase mb-1">Pricing estimado</div>
                <p class="text-emerald-400 font-mono text-xs">{{ openProductData?.pricing_est }}</p>
              </div>
            </div>
            <div v-if="openProductData?.gate_description" class="bg-red-950/30 border border-red-800/50 rounded-lg p-3">
              <div class="text-xs text-red-400 uppercase mb-1 font-bold">⚠ Gate</div>
              <p class="text-slate-200 text-xs">{{ openProductData.gate_description }}</p>
            </div>
            <div v-if="openProductData?.systems_by_segment" class="bg-slate-950/60 border border-slate-800 rounded-lg p-3">
              <div class="text-xs text-slate-500 uppercase mb-2">Sistemas integrados por segmento</div>
              <div v-for="(systems, segId) in openProductData.systems_by_segment" :key="segId" class="mb-1.5 text-xs">
                <span class="text-slate-400">{{ formatSegmentName(segId) }}:</span>
                <span class="text-slate-200 ml-1">{{ systems.join(', ') }}</span>
              </div>
            </div>
            <div class="bg-slate-950/60 border border-slate-800 rounded-lg p-3">
              <div class="text-xs text-slate-500 uppercase mb-2">Atende os públicos</div>
              <div class="flex flex-wrap gap-1.5">
                <span v-for="s in (openProductData?.segments || [])" :key="s"
                  class="text-[11px] px-2 py-0.5 rounded bg-slate-800 text-slate-300">
                  {{ formatSegmentName(s) }}
                </span>
              </div>
            </div>
            <div class="flex items-center gap-2 pt-2">
              <div class="text-xs text-slate-500 uppercase">Confiabilidade VVV</div>
              <div class="flex-1 h-1.5 bg-slate-800 rounded-full overflow-hidden">
                <div :class="['h-full', vvvBar(openProductData?.vvv)]" :style="{ width: ((openProductData?.vvv ?? 0) * 100) + '%' }"></div>
              </div>
              <span class="text-xs text-slate-300 font-mono">{{ (openProductData?.vvv ?? 0).toFixed(2) }}</span>
            </div>
            <div class="text-xs text-slate-500 italic pt-1">
              Fonte: NEOGOV-DATA-v2.json · {{ openProductData?.id }}
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const props = defineProps({
  clusters: { type: Array, default: () => [] },
  products: { type: Array, default: () => [] },
})

const selectedCluster = ref('all')
const openProductId = ref(null)

const filteredClusters = computed(() =>
  selectedCluster.value === 'all'
    ? props.clusters
    : props.clusters.filter(c => c.id === selectedCluster.value)
)

const productById = (id) => props.products.find(p => p.id === id)

const openProductData = computed(() => openProductId.value ? productById(openProductId.value) : null)

const openProduct = (id) => { openProductId.value = id }

const formatNumber = (n) => {
  if (typeof n !== 'number') return n ?? '—'
  return n.toLocaleString('pt-BR')
}

const formatStatus = (s) => ({
  priority_critical: 'Prioridade crítica',
  active_today: 'Ativo hoje',
  conditional_poc: 'Condicional · PoC',
  declared_target: 'Alvo declarado',
  wave_3: 'Wave 3'
})[s] || s || '[DADO PENDENTE]'

const formatModel = (m) => ({
  assinatura_mensal: 'Assinatura mensal',
  projeto_setup_mais_assinatura: 'Setup + assinatura',
  usage_based: 'Por uso',
  usage_based_mais_setup: 'Por uso + setup'
})[m] || m || '—'

const formatSegmentName = (segId) => {
  const c = props.clusters.find(c => c.id === segId)
  if (c) return c.name
  return ({
    setor_publico_municipal: 'Setor Público Municipal',
    setor_publico_estadual: 'Setor Público Estadual',
    setor_publico_federal: 'Setor Público Federal',
    saude_privada: 'Saúde Privada',
    educacao_privada: 'Educação Privada',
    entidades_associativas: 'Entidades Associativas',
    all: 'Todos os públicos'
  })[segId] || segId
}

const scoreColor = (s) => {
  if (s == null) return 'text-slate-500'
  if (s >= 8) return 'text-green-400'
  if (s >= 6) return 'text-yellow-400'
  return 'text-red-400'
}

const vvvBar = (v) => {
  if (v == null) return 'bg-slate-700'
  if (v >= 0.85) return 'bg-green-500'
  if (v >= 0.70) return 'bg-yellow-500'
  return 'bg-red-500'
}
</script>
