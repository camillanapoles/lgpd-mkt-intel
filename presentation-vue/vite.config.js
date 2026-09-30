import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  base: '/lgpd-mkt-intel/',
  build: {
    outDir: 'dist',
    assetsDir: 'assets',
    rollupOptions: {
      output: {
        manualChunks: {
          'chart': ['chart.js', 'vue-chartjs'],
          'animation': ['gsap'],
          'vendor': ['vue', 'vue-router', 'pinia']
        }
      }
    }
  }
})
