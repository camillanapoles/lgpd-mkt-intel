import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useFilterStore = defineStore('filters', () => {
  const activePhase = ref(null)
  const swotCategory = ref(null)
  const bmcHighlight = ref(null)
  const searchQuery = ref('')
  const impactFilter = ref('all')

  const impactLevels = ['all', 'ALTO', 'MÉDIO', 'BAIXO']

  function setPhase(phase) {
    activePhase.value = activePhase.value === phase ? null : phase
  }

  function setSwotCategory(category) {
    swotCategory.value = swotCategory.value === category ? null : category
  }

  function setBmcHighlight(section) {
    bmcHighlight.value = bmcHighlight.value === section ? null : section
  }

  function resetFilters() {
    activePhase.value = null
    swotCategory.value = null
    bmcHighlight.value = null
    searchQuery.value = ''
    impactFilter.value = 'all'
  }

  const hasActiveFilters = computed(() =>
    activePhase.value !== null ||
    swotCategory.value !== null ||
    bmcHighlight.value !== null ||
    searchQuery.value !== '' ||
    impactFilter.value !== 'all'
  )

  return {
    activePhase,
    swotCategory,
    bmcHighlight,
    searchQuery,
    impactFilter,
    impactLevels,
    setPhase,
    setSwotCategory,
    setBmcHighlight,
    resetFilters,
    hasActiveFilters
  }
})
