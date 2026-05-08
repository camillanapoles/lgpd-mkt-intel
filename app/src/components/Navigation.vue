<template>
  <nav class="bg-white border-b border-slate-200 sticky top-0 z-50">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-16">
        <!-- Logo -->
        <div class="flex items-center gap-3">
          <div class="w-10 h-10 bg-gradient-to-br from-primary-500 to-primary-700 rounded-lg flex items-center justify-center">
            <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
            </svg>
          </div>
          <div>
            <h1 class="font-display font-bold text-slate-900 text-lg">LGPD Dashboard</h1>
            <p class="text-xs text-slate-500">Contabilizei da Privacy</p>
          </div>
        </div>

        <!-- Desktop Navigation -->
        <div class="hidden md:flex items-center gap-1">
          <router-link
            v-for="item in navItems"
            :key="item.name"
            :to="item.path"
            class="px-4 py-2 rounded-lg text-sm font-medium transition-colors"
            :class="$route.name === item.name
              ? 'bg-primary-50 text-primary-700'
              : 'text-slate-600 hover:bg-slate-100 hover:text-slate-900'"
          >
            {{ item.label }}
          </router-link>
        </div>

        <!-- Mobile Menu Button -->
        <button
          @click="mobileMenuOpen = !mobileMenuOpen"
          class="md:hidden p-2 rounded-lg text-slate-600 hover:bg-slate-100"
        >
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path v-if="!mobileMenuOpen" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
            <path v-else stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
          </svg>
        </button>
      </div>

      <!-- Mobile Navigation -->
      <div v-show="mobileMenuOpen" class="md:hidden py-4 border-t border-slate-200">
        <div class="flex flex-col gap-1">
          <router-link
            v-for="item in navItems"
            :key="item.name"
            :to="item.path"
            @click="mobileMenuOpen = false"
            class="px-4 py-2 rounded-lg text-sm font-medium transition-colors"
            :class="$route.name === item.name
              ? 'bg-primary-50 text-primary-700'
              : 'text-slate-600 hover:bg-slate-100'"
          >
            {{ item.label }}
          </router-link>
        </div>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { ref } from 'vue'

const mobileMenuOpen = ref(false)

const navItems = [
  { name: 'dashboard', label: 'Dashboard', path: '/' },
  { name: 'scenarios', label: 'Cenários', path: '/cenarios' },
  { name: 'bmc', label: 'BMC', path: '/bmc' },
  { name: 'roadmap', label: 'Roadmap', path: '/roadmap' },
  { name: 'swot', label: 'SWOT', path: '/swot' },
  { name: 'wiki', label: 'Wiki', path: '/wiki' }
]
</script>
