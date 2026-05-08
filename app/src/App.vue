<template>
  <div class="min-h-screen flex flex-col">
    <!-- Navigation -->
    <Navigation />

    <!-- Main Content -->
    <main class="flex-1">
      <router-view />
    </main>

    <!-- Footer -->
    <footer class="bg-slate-900 text-slate-400 py-6 mt-auto">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex flex-col md:flex-row justify-between items-center gap-4">
          <p class="text-sm">LGPD Executive Dashboard - Contabilizei da Privacy</p>
          <p class="text-xs">Versão 1.0.0 | Atualizado: Maio 2026</p>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup>
import Navigation from './components/Navigation.vue'
</script>
