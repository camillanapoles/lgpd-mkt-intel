<template>
  <!-- Login Gate -->
  <div
    v-if="loginState !== 'authenticated'"
    class="min-h-screen bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 flex items-center justify-center p-4"
  >
    <div class="w-full max-w-sm">
      <!-- Card -->
      <div class="bg-slate-800/60 backdrop-blur border border-slate-700 rounded-2xl shadow-2xl p-8">
        <!-- Logo / Brand -->
        <div class="text-center mb-8">
          <div class="inline-flex items-center justify-center w-14 h-14 rounded-xl bg-blue-600/20 border border-blue-500/30 mb-4">
            <svg class="w-7 h-7 text-blue-400" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5">
              <path stroke-linecap="round" stroke-linejoin="round"
                d="M9 12.75L11.25 15 15 9.75m-3-7.036A11.959 11.959 0 013.598 6 11.99 11.99 0 003 9.749c0 5.592 3.824 10.29 9 11.623 5.176-1.332 9-6.03 9-11.622 0-1.31-.21-2.571-.598-3.751h-.152c-3.196 0-6.1-1.248-8.25-3.285z" />
            </svg>
          </div>
          <h1 class="text-xl font-bold text-white tracking-tight">NeoGov Strategic Intelligence</h1>
          <p class="text-slate-400 text-sm mt-1">Acesso restrito — dados confidenciais</p>
        </div>

        <!-- Checking state (auto-decrypt from session) -->
        <div v-if="loginState === 'checking'" class="text-center py-4">
          <div class="inline-block w-6 h-6 border-2 border-blue-500 border-t-transparent rounded-full animate-spin mb-3"></div>
          <p class="text-slate-400 text-sm">Verificando sessão...</p>
        </div>

        <!-- Login form -->
        <form v-else @submit.prevent="handleLogin" class="space-y-4">
          <div>
            <label class="block text-xs font-medium text-slate-400 mb-1.5 uppercase tracking-wider">
              Senha de acesso
            </label>
            <input
              ref="passwordInput"
              v-model="password"
              type="password"
              placeholder="••••••••"
              autocomplete="current-password"
              :disabled="loginState === 'loading'"
              class="w-full bg-slate-900/70 border border-slate-600 text-white placeholder-slate-600 rounded-lg px-4 py-2.5 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all disabled:opacity-50"
            />
          </div>

          <!-- Error message -->
          <div
            v-if="loginState === 'error'"
            class="flex items-center gap-2 bg-red-500/10 border border-red-500/30 rounded-lg px-3 py-2.5"
          >
            <svg class="w-4 h-4 text-red-400 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
              <path stroke-linecap="round" stroke-linejoin="round" d="M12 9v3.75m9-.75a9 9 0 11-18 0 9 9 0 0118 0zm-9 3.75h.008v.008H12v-.008z" />
            </svg>
            <p class="text-red-400 text-sm">{{ loginError }}</p>
          </div>

          <button
            type="submit"
            :disabled="!password || loginState === 'loading'"
            class="w-full bg-blue-600 hover:bg-blue-500 disabled:bg-slate-700 disabled:text-slate-500 text-white font-medium py-2.5 rounded-lg text-sm transition-all focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 focus:ring-offset-slate-800 flex items-center justify-center gap-2"
          >
            <span v-if="loginState === 'loading'" class="inline-block w-4 h-4 border-2 border-white/40 border-t-white rounded-full animate-spin"></span>
            <span>{{ loginState === 'loading' ? 'Verificando...' : 'Entrar' }}</span>
          </button>
        </form>

        <!-- Footer -->
        <p class="text-center text-slate-600 text-xs mt-6">
          NeoGov © {{ currentYear }} — uso interno
        </p>
      </div>
    </div>
  </div>

  <!-- Authenticated App -->
  <div v-else class="min-h-screen bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900">
    <nav class="bg-slate-950/50 backdrop-blur border-b border-slate-700 sticky top-0 z-50">
      <div class="max-w-7xl mx-auto px-4 py-3">
        <div class="flex items-center justify-between mb-2">
          <h1 class="text-lg font-bold text-white">
            {{ companyName }} — Strategic Intel
          </h1>
          <div class="flex items-center gap-3 text-sm">
            <span class="text-slate-400">
              FDC-U Top:
              <span class="font-bold text-white">{{ topClusterName }}</span>
            </span>
            <span class="text-slate-500">|</span>
            <span class="text-slate-400">
              Gaps VVV=0:
              <span class="font-bold text-red-400">{{ criticalGapCount }}</span>
            </span>
            <span class="text-slate-500">|</span>
            <button
              @click="handleLogout"
              class="flex items-center gap-1.5 text-slate-400 hover:text-white transition-colors text-xs border border-slate-700 hover:border-slate-500 rounded-md px-2.5 py-1"
            >
              <svg class="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 9V5.25A2.25 2.25 0 0013.5 3h-6a2.25 2.25 0 00-2.25 2.25v13.5A2.25 2.25 0 007.5 21h6a2.25 2.25 0 002.25-2.25V15m3 0l3-3m0 0l-3-3m3 3H9" />
              </svg>
              Sair
            </button>
          </div>
        </div>
        <div class="flex gap-2 overflow-x-auto pb-1">
          <button
            v-for="tab in tabs"
            :key="tab.id"
            @click="activeTab = tab.id"
            :class="[
              'px-3 py-1.5 rounded-lg text-xs whitespace-nowrap transition-all',
              activeTab === tab.id
                ? 'bg-blue-600 text-white'
                : 'text-slate-300 hover:bg-slate-700',
            ]"
          >
            {{ tab.label }}
          </button>
        </div>
      </div>
    </nav>

    <main class="max-w-7xl mx-auto px-4 py-8">
      <div v-if="loadError" class="text-center py-20">
        <p class="text-red-400 mb-2">Erro ao carregar dados estratégicos</p>
        <p class="text-slate-500 text-sm">{{ loadError }}</p>
      </div>

      <template v-else-if="data">
        <Dashboard5s
          v-if="activeTab === 'dashboard'"
          :clusters="data.clusters"
          :kpis="data.kpis"
          :risks="data.risks"
          :company="data.company"
          :sun_tzu_factors="data.sun_tzu_factors"
          :fdcu="data.fdc_u"
        />

        <FdcuInteractive
          v-else-if="activeTab === 'fdcu'"
          :fdcu="data.fdc_u"
          :clusters="data.clusters"
          @fdcu-weights-changed="fdcuWeights = $event"
        />

        <RoadmapViewer
          v-else-if="activeTab === 'roadmap'"
          :roadmap="data.roadmap"
          :clusters="data.clusters"
        />

        <SwotAnalysis
          v-else-if="activeTab === 'swot'"
          :diagnostic="data.diagnostic"
        />

        <ScenarioSimulator
          v-else-if="activeTab === 'scenarios'"
          :scenarios="data.scenarios"
          :clusters="data.clusters"
          @scenario-change="scenarioState = $event"
        />

        <StatusPage
          v-else-if="activeTab === 'status'"
          :vvv_gaps="data.vvv_gaps"
          :action_plan="data.action_plan"
        />

        <CompetitiveView
          v-else-if="activeTab === 'competitive'"
          :competitive="data.competitive"
        />
      </template>
    </main>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, nextTick } from 'vue'
import Dashboard5s from './components/strategic/Dashboard5s.vue'
import FdcuInteractive from './components/strategic/FdcuInteractive.vue'
import RoadmapViewer from './components/strategic/RoadmapViewer.vue'
import SwotAnalysis from './components/strategic/SwotAnalysis.vue'
import ScenarioSimulator from './components/strategic/ScenarioSimulator.vue'
import StatusPage from './components/strategic/StatusPage.vue'
import CompetitiveView from './components/strategic/CompetitiveView.vue'
import { decryptPayload, type EncryptedPayload } from './utils/crypto'

// ── Auth state ─────────────────────────────────────────────────────────────
type LoginState = 'checking' | 'login' | 'loading' | 'authenticated' | 'error'

const SESSION_KEY = 'ngov-session'

const loginState = ref<LoginState>('checking')
const password = ref('')
const loginError = ref('')
const passwordInput = ref<HTMLInputElement | null>(null)

// ── App state ───────────────────────────────────────────────────────────────
const activeTab = ref('dashboard')
const data = ref<Record<string, unknown> | null>(null)
const loadError = ref<string | null>(null)
const fdcuWeights = ref<Record<string, unknown>>({})
const scenarioState = ref<Record<string, unknown>>({})

// Encrypted payload cached after initial fetch
let encryptedPayload: EncryptedPayload | null = null

const currentYear = new Date().getFullYear()

const tabs = [
  { id: 'dashboard', label: 'Dashboard' },
  { id: 'fdcu', label: 'FDC-U' },
  { id: 'roadmap', label: 'Roadmap' },
  { id: 'swot', label: 'SWOT' },
  { id: 'scenarios', label: 'Cenarios' },
  { id: 'status', label: 'VVV Gaps' },
  { id: 'competitive', label: 'Competitivo' },
]

// ── Computed ────────────────────────────────────────────────────────────────
const companyName = computed(() => {
  const company = data.value?.company as { name?: string } | undefined
  return company?.name ?? 'NeoGov'
})

const topClusterName = computed(() => {
  const fdcu = data.value?.fdc_u as { ranking_pure?: Array<{ cluster_name?: string }> } | undefined
  return fdcu?.ranking_pure?.[0]?.cluster_name ?? '—'
})

const criticalGapCount = computed(() => {
  const gaps = data.value?.vvv_gaps as Array<{ vvv_score?: number }> | undefined
  return (gaps ?? []).filter(g => g.vvv_score === 0).length
})

// ── Helpers ─────────────────────────────────────────────────────────────────
function getErrorMessage(err: unknown): string {
  if (err instanceof Error) return err.message
  return 'Erro desconhecido'
}

async function fetchEncryptedPayload(): Promise<EncryptedPayload> {
  const base = import.meta.env.BASE_URL as string
  const response = await fetch(`${base}strategic-data-encrypted.json`)
  if (!response.ok) throw new Error(`HTTP ${response.status}`)
  return response.json() as Promise<EncryptedPayload>
}

async function applyDecryptedData(decrypted: unknown): Promise<void> {
  data.value = decrypted as Record<string, unknown>
  loginState.value = 'authenticated'
}

function focusPasswordInput(): void {
  nextTick(() => {
    passwordInput.value?.focus()
  })
}

// ── Auth handlers ────────────────────────────────────────────────────────────
async function handleLogin(): Promise<void> {
  if (!password.value || !encryptedPayload) return

  loginState.value = 'loading'
  loginError.value = ''

  try {
    const decrypted = await decryptPayload(encryptedPayload, password.value)
    // Persist password hash as session token (sessionStorage clears on tab close)
    sessionStorage.setItem(SESSION_KEY, password.value)
    await applyDecryptedData(decrypted)
  } catch {
    loginState.value = 'error'
    loginError.value = 'Senha incorreta. Tente novamente.'
    password.value = ''
    focusPasswordInput()
  }
}

function handleLogout(): void {
  sessionStorage.removeItem(SESSION_KEY)
  data.value = null
  password.value = ''
  loginError.value = ''
  loginState.value = 'login'
  focusPasswordInput()
}

// ── Bootstrap ────────────────────────────────────────────────────────────────
onMounted(async () => {
  try {
    encryptedPayload = await fetchEncryptedPayload()
  } catch (err) {
    // If encrypted file doesn't exist yet, fall back to unencrypted for dev
    const base = import.meta.env.BASE_URL as string
    try {
      const fallback = await fetch(`${base}strategic-data-unified.json`)
      if (!fallback.ok) throw new Error(`HTTP ${fallback.status}`)
      const plainData = await fallback.json()
      data.value = plainData as Record<string, unknown>
      loginState.value = 'authenticated'
      return
    } catch {
      loadError.value = getErrorMessage(err)
      loginState.value = 'login'
      return
    }
  }

  // Check for existing session token
  const savedPassword = sessionStorage.getItem(SESSION_KEY)
  if (savedPassword && encryptedPayload) {
    try {
      const decrypted = await decryptPayload(encryptedPayload, savedPassword)
      await applyDecryptedData(decrypted)
      return
    } catch {
      // Stale/invalid session — clear it and show login
      sessionStorage.removeItem(SESSION_KEY)
    }
  }

  loginState.value = 'login'
  focusPasswordInput()
})
</script>
