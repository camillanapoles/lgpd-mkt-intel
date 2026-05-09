<template>
  <div class="stakeholder-map">
    <div class="flex items-center justify-between mb-6">
      <h2 class="text-h2 text-white">Stakeholders & RACI</h2>
      <div class="flex gap-2">
        <button
          v-for="view in views"
          :key="view.id"
          @click="activeView = view.id"
          :class="[
            'px-3 py-1.5 rounded-lg text-caption transition-all',
            activeView === view.id ? 'bg-accent-600 text-white' : 'bg-slate-700 text-slate-300 hover:bg-slate-600',
          ]"
        >
          {{ view.label }}
        </button>
      </div>
    </div>

    <div v-if="activeView === 'internal'">
      <div class="grid md:grid-cols-2 gap-4 mb-6">
        <div
          v-for="member in stakeholders.internal"
          :key="member.nome"
          class="bg-slate-800/50 border border-slate-700 rounded-card p-5"
        >
          <div class="flex items-start justify-between mb-2">
            <div>
              <h3 class="text-h4 text-white">{{ member.nome }}</h3>
              <p class="text-body-sm text-accent-400">{{ member.role }}</p>
            </div>
            <span
              :class="[
                'text-caption px-2 py-0.5 rounded',
                powerClass(member.power),
              ]"
            >
              {{ member.power }}
            </span>
          </div>
          <p class="text-body-sm text-slate-300 mb-3">{{ member.focus }}</p>
          <div class="flex items-center gap-2">
            <span class="text-caption text-slate-400">Alinhamento:</span>
            <div class="flex-1 h-2 bg-slate-700 rounded-full overflow-hidden">
              <div
                class="h-full rounded-full bg-accent-500 transition-all duration-700"
                :style="{ width: `${member.alignment * 100}%` }"
              />
            </div>
            <span class="text-caption text-white font-mono">{{ (member.alignment * 100).toFixed(0) }}%</span>
            <button
              @click.stop="toggleInfo(`int-${member.nome}`)"
              class="shrink-0 w-5 h-5 flex items-center justify-center rounded-full text-xs transition-colors"
              :class="expandedInfo.has(`int-${member.nome}`) ? 'bg-accent-600 text-white' : 'bg-slate-700 text-slate-400 hover:bg-slate-600'"
              title="Ver fonte e detalhes"
            >i</button>
          </div>
          <div v-if="expandedInfo.has(`int-${member.nome}`)" class="px-2 pb-1 space-y-1 border-t border-slate-700/50 mt-2 pt-1.5">
            <p class="text-caption text-slate-400">Poder: {{ member.power }} | Role: {{ member.role }}</p>
            <div class="flex items-center gap-2 flex-wrap">
              <span class="text-caption text-slate-500">Fonte:</span>
              <span class="text-accent-400 text-xs">{{ member.fonte || 'Nao mapeada' }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div v-else-if="activeView === 'external'">
      <div class="space-y-3">
        <div
          v-for="group in stakeholders.external"
          :key="group.tipo"
          class="bg-slate-800/50 border border-slate-700 rounded-card p-4"
        >
          <div class="flex items-center justify-between mb-2">
            <div class="flex items-center gap-2">
              <h3 class="text-h4 text-white">{{ group.tipo }}</h3>
              <button
                @click.stop="toggleInfo(`ext-${group.tipo}`)"
                class="shrink-0 w-5 h-5 flex items-center justify-center rounded-full text-xs transition-colors"
                :class="expandedInfo.has(`ext-${group.tipo}`) ? 'bg-accent-600 text-white' : 'bg-slate-700 text-slate-400 hover:bg-slate-600'"
                title="Ver fonte e detalhes"
              >i</button>
            </div>
            <div class="flex items-center gap-3">
              <span :class="['text-caption px-2 py-0.5 rounded', powerClass(group.power)]">
                Poder: {{ group.power }}
              </span>
              <div class="flex items-center gap-1">
                <span class="text-caption text-slate-400">Alinhamento:</span>
                <div class="w-16 h-2 bg-slate-700 rounded-full overflow-hidden">
                  <div
                    class="h-full rounded-full transition-all duration-700"
                    :class="alignmentColor(group.alignment)"
                    :style="{ width: `${group.alignment * 100}%` }"
                  />
                </div>
                <span class="text-caption text-white font-mono">{{ (group.alignment * 100).toFixed(0) }}%</span>
              </div>
            </div>
          </div>
          <p class="text-body-sm text-slate-300">{{ group.interesse }}</p>
          <div v-if="expandedInfo.has(`ext-${group.tipo}`)" class="space-y-1 border-t border-slate-700/50 mt-2 pt-1.5">
            <p class="text-caption text-slate-400">Interesse: {{ group.interesse }}</p>
            <div class="flex items-center gap-2 flex-wrap">
              <span class="text-caption text-slate-500">Poder:</span>
              <span class="text-accent-400 text-xs">{{ group.power }}</span>
              <span class="text-caption text-slate-500 ml-2">Alinhamento:</span>
              <span class="text-accent-400 text-xs">{{ (group.alignment * 100).toFixed(0) }}%</span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div v-else-if="activeView === 'raci'">
      <div class="overflow-x-auto">
        <table class="w-full text-body-sm">
          <thead>
            <tr class="border-b border-slate-700">
              <th class="text-left text-slate-400 font-medium pb-3 pr-4">Atividade</th>
              <th v-for="initials in raciInitials" :key="initials" class="text-center text-slate-400 font-medium pb-3 px-3">
                {{ initials }}
              </th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="(entry, activity) in stakeholders.raci"
              :key="activity"
              class="border-b border-slate-800 hover:bg-slate-800/30 transition-colors"
            >
              <td class="py-3 pr-4 text-white">{{ activity }}</td>
              <td
                v-for="role in ['R', 'A', 'C', 'I']"
                :key="role"
                class="text-center py-3 px-3"
              >
                <span
                  v-if="entry[role]"
                  :class="[
                    'inline-block w-8 h-8 leading-8 rounded-lg text-caption font-bold',
                    roleClass(role),
                  ]"
                >
                  {{ entry[role]?.charAt(0) }}
                </span>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="flex gap-4 mt-4">
        <span v-for="(label, role) in raciLegend" :key="role" class="flex items-center gap-2">
          <span :class="['text-caption font-bold px-2 py-0.5 rounded', roleClass(role)]">{{ role }}</span>
          <span class="text-caption text-slate-400">{{ label }}</span>
        </span>
      </div>
    </div>

    <div v-if="stakeholders.gaps?.length" class="mt-6 p-4 rounded-card bg-yellow-950/20 border border-yellow-900/30">
      <h3 class="text-h4 text-yellow-400 mb-2">Gaps Identificados</h3>
      <div class="space-y-1">
        <p v-for="gap in stakeholders.gaps" :key="gap" class="text-body-sm text-slate-300">
          <span class="text-yellow-500">&#9888;</span> {{ gap }}
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, reactive } from 'vue'

const props = defineProps({
  stakeholders: { type: Object, default: () => ({}) },
})

const activeView = ref('internal')
const expandedInfo = reactive(new Set())

const toggleInfo = (key) => {
  expandedInfo.has(key) ? expandedInfo.delete(key) : expandedInfo.add(key)
}

const views = [
  { id: 'internal', label: 'Time' },
  { id: 'external', label: 'Externos' },
  { id: 'raci', label: 'RACI' },
]

const raciInitials = computed(() => {
  const set = new Set()
  Object.values(props.stakeholders.raci || {}).forEach((entry) => {
    Object.values(entry).forEach((v) => { if (v) set.add(v.charAt(0)) })
  })
  return [...set]
})

const raciLegend = { R: 'Responsavel', A: 'Aprovador', C: 'Consultado', I: 'Informado' }

const roleClass = (role) => {
  const classes = {
    R: 'bg-blue-900/50 text-blue-400',
    A: 'bg-green-900/50 text-green-400',
    C: 'bg-yellow-900/50 text-yellow-400',
    I: 'bg-slate-700 text-slate-300',
  }
  return classes[role] || ''
}

const powerClass = (power) => {
  if (power === 'Alto') return 'bg-red-900/50 text-red-400'
  if (power === 'Medio') return 'bg-yellow-900/50 text-yellow-400'
  return 'bg-slate-700 text-slate-300'
}

const alignmentColor = (val) => {
  if (val >= 0.8) return 'bg-green-500'
  if (val >= 0.5) return 'bg-yellow-500'
  return 'bg-red-500'
}
</script>
