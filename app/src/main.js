import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import App from './App.vue'
import './styles/main.css'

const routes = [
  { path: '/', component: () => import('./pages/Dashboard.vue'), name: 'dashboard' },
  { path: '/cenarios', component: () => import('./pages/Scenarios.vue'), name: 'scenarios' },
  { path: '/bmc', component: () => import('./pages/BMC.vue'), name: 'bmc' },
  { path: '/roadmap', component: () => import('./pages/Roadmap.vue'), name: 'roadmap' },
  { path: '/swot', component: () => import('./pages/SWOT.vue'), name: 'swot' }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
  scrollBehavior() { return { top: 0 } }
})

// Handle GitHub Pages 404.html SPA redirect
const redirect = window.location.search
if (redirect && redirect[1] === '/') {
  const path = redirect.slice(2).replace(/&/g, '&')
  window.history.replaceState(null, '', path)
}

const app = createApp(App)
app.use(router)
app.mount('#app')
