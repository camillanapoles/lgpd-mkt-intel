import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import App from './App.vue'
import './styles/main.css'

// Pages
import Dashboard from './pages/Dashboard.vue'
import Scenarios from './pages/Scenarios.vue'
import BMC from './pages/BMC.vue'
import Roadmap from './pages/Roadmap.vue'
import SWOT from './pages/SWOT.vue'
import Wiki from './pages/Wiki.vue'

const routes = [
  { path: '/', component: Dashboard, name: 'dashboard' },
  { path: '/cenarios', component: Scenarios, name: 'scenarios' },
  { path: '/bmc', component: BMC, name: 'bmc' },
  { path: '/roadmap', component: Roadmap, name: 'roadmap' },
  { path: '/swot', component: SWOT, name: 'swot' },
  { path: '/wiki', component: Wiki, name: 'wiki' }
]

const router = createRouter({
  history: createWebHistory('/LGPD/app/'),
  routes
})

const app = createApp(App)
app.use(router)
app.mount('#app')
