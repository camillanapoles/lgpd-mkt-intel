<template>
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
    <!-- Header -->
    <div class="mb-8">
      <h1 class="font-display text-3xl font-bold text-slate-900">Business Model Canvas</h1>
      <p class="text-slate-600 mt-2">Modelo de negócios - Contabilizei da Privacy</p>
    </div>

    <!-- BMC Grid -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
      <!-- Key Partners -->
      <div class="card p-5">
        <div class="flex items-center gap-2 mb-3">
          <div class="w-8 h-8 rounded-lg bg-blue-100 flex items-center justify-center">
            <svg class="w-4 h-4 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0z" />
            </svg>
          </div>
          <h3 class="font-semibold text-slate-900">Key Partners</h3>
        </div>
        <ul class="space-y-2 text-sm text-slate-600">
          <li v-for="item in bmc.keyPartners" :key="item" class="flex items-start gap-2">
            <span class="text-blue-500 mt-0.5">•</span>
            <span>{{ item }}</span>
          </li>
        </ul>
      </div>

      <!-- Key Activities -->
      <div class="card p-5">
        <div class="flex items-center gap-2 mb-3">
          <div class="w-8 h-8 rounded-lg bg-green-100 flex items-center justify-center">
            <svg class="w-4 h-4 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
            </svg>
          </div>
          <h3 class="font-semibold text-slate-900">Key Activities</h3>
        </div>
        <ul class="space-y-2 text-sm text-slate-600">
          <li v-for="item in bmc.keyActivities" :key="item" class="flex items-start gap-2">
            <span class="text-green-500 mt-0.5">•</span>
            <span>{{ item }}</span>
          </li>
        </ul>
      </div>

      <!-- Key Resources -->
      <div class="card p-5">
        <div class="flex items-center gap-2 mb-3">
          <div class="w-8 h-8 rounded-lg bg-purple-100 flex items-center justify-center">
            <svg class="w-4 h-4 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10" />
            </svg>
          </div>
          <h3 class="font-semibold text-slate-900">Key Resources</h3>
        </div>
        <ul class="space-y-2 text-sm text-slate-600">
          <li v-for="item in bmc.keyResources" :key="item" class="flex items-start gap-2">
            <span class="text-purple-500 mt-0.5">•</span>
            <span>{{ item }}</span>
          </li>
        </ul>
      </div>

      <!-- Value Propositions -->
      <div class="card p-5 border-2 border-primary-200 bg-primary-50/50">
        <div class="flex items-center gap-2 mb-3">
          <div class="w-8 h-8 rounded-lg bg-primary-100 flex items-center justify-center">
            <svg class="w-4 h-4 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z" />
            </svg>
          </div>
          <h3 class="font-semibold text-slate-900">Value Propositions</h3>
        </div>
        <ul class="space-y-2 text-sm text-slate-600">
          <li v-for="item in bmc.valuePropositions" :key="item" class="flex items-start gap-2">
            <span class="text-primary-500 mt-0.5">★</span>
            <span>{{ item }}</span>
          </li>
        </ul>
      </div>

      <!-- Customer Relationships -->
      <div class="card p-5">
        <div class="flex items-center gap-2 mb-3">
          <div class="w-8 h-8 rounded-lg bg-amber-100 flex items-center justify-center">
            <svg class="w-4 h-4 text-amber-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" />
            </svg>
          </div>
          <h3 class="font-semibold text-slate-900">Customer Relationships</h3>
        </div>
        <ul class="space-y-2 text-sm text-slate-600">
          <li v-for="item in bmc.customerRelationships" :key="item" class="flex items-start gap-2">
            <span class="text-amber-500 mt-0.5">•</span>
            <span>{{ item }}</span>
          </li>
        </ul>
      </div>

      <!-- Channels -->
      <div class="card p-5">
        <div class="flex items-center gap-2 mb-3">
          <div class="w-8 h-8 rounded-lg bg-rose-100 flex items-center justify-center">
            <svg class="w-4 h-4 text-rose-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7h12m0 0l-4-4m4 4l-4 4m0 6H4m0 0l4 4m-4-4l4-4" />
            </svg>
          </div>
          <h3 class="font-semibold text-slate-900">Channels</h3>
        </div>
        <ul class="space-y-2 text-sm text-slate-600">
          <li v-for="item in bmc.channels" :key="item" class="flex items-start gap-2">
            <span class="text-rose-500 mt-0.5">•</span>
            <span>{{ item }}</span>
          </li>
        </ul>
      </div>

      <!-- Customer Segments -->
      <div class="card p-5">
        <div class="flex items-center gap-2 mb-3">
          <div class="w-8 h-8 rounded-lg bg-cyan-100 flex items-center justify-center">
            <svg class="w-4 h-4 text-cyan-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0z" />
            </svg>
          </div>
          <h3 class="font-semibold text-slate-900">Customer Segments</h3>
        </div>
        <div class="space-y-3">
          <div v-for="segment in bmc.customerSegments" :key="segment.name" class="p-3 bg-slate-50 rounded-lg">
            <div class="flex items-center justify-between">
              <span class="text-sm font-medium text-slate-700">{{ segment.name }}</span>
              <span class="badge badge-info">P{{ segment.priority }}</span>
            </div>
            <p class="text-xs text-slate-500 mt-1">TAM: {{ segment.tam.toLocaleString('pt-BR') }}</p>
          </div>
        </div>
      </div>

      <!-- Cost Structure -->
      <div class="card p-5 md:col-span-1 lg:col-span-2">
        <div class="flex items-center gap-2 mb-3">
          <div class="w-8 h-8 rounded-lg bg-red-100 flex items-center justify-center">
            <svg class="w-4 h-4 text-red-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 7h6m0 10v-3m-3 3h.01M9 17h.01M9 14h.01M12 14h.01M15 11h.01M12 11h.01M9 11h.01M7 21h10a2 2 0 002-2V5a2 2 0 00-2-2H7a2 2 0 00-2 2v14a2 2 0 002 2z" />
            </svg>
          </div>
          <h3 class="font-semibold text-slate-900">Cost Structure</h3>
          <span class="ml-auto text-sm text-slate-500">Target: 80%+ gross margin</span>
        </div>
        <div class="grid grid-cols-2 md:grid-cols-4 gap-3">
          <div v-for="cost in bmc.costStructure" :key="cost.category" class="text-center p-3 bg-slate-50 rounded-lg">
            <div class="text-2xl font-bold text-slate-900">{{ cost.percentage }}%</div>
            <div class="text-sm font-medium text-slate-700 mt-1">{{ cost.category }}</div>
            <div class="text-xs text-slate-500 mt-1">{{ cost.items.join(', ') }}</div>
          </div>
        </div>
      </div>

      <!-- Revenue Streams -->
      <div class="card p-5">
        <div class="flex items-center gap-2 mb-3">
          <div class="w-8 h-8 rounded-lg bg-green-100 flex items-center justify-center">
            <svg class="w-4 h-4 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
          </div>
          <h3 class="font-semibold text-slate-900">Revenue Streams</h3>
        </div>
        <div class="space-y-2">
          <div v-for="revenue in bmc.revenueStreams" :key="revenue.type" class="flex justify-between items-center p-2 bg-slate-50 rounded">
            <span class="text-sm text-slate-700">{{ revenue.type }}</span>
            <span class="text-sm font-medium text-green-700">{{ revenue.range }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import strategicData from '../data/strategicData.js'

const bmc = ref(strategicData.businessModelCanvas)
</script>
