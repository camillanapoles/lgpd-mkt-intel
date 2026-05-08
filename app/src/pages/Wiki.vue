<template>
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
    <div class="mb-8">
      <h1 class="font-display text-3xl font-bold text-slate-900">Wiki de Documentos</h1>
      <p class="text-slate-600 mt-2">Links diretos para visualizar os arquivos Markdown no GitHub.</p>
    </div>

    <div class="space-y-6">
      <section
        v-for="section in wikiSections"
        :key="section.title"
        class="card p-6"
      >
        <h2 class="font-display text-xl font-semibold text-slate-900 mb-4">{{ section.title }}</h2>
        <ul class="space-y-2">
          <li v-for="doc in section.docs" :key="doc.path">
            <a
              :href="doc.url"
              target="_blank"
              rel="noopener noreferrer"
              class="text-primary-700 hover:text-primary-800 hover:underline break-all"
            >
              {{ doc.name }}
            </a>
            <p class="text-xs text-slate-500 mt-0.5">{{ doc.path }}</p>
          </li>
        </ul>
      </section>
    </div>
  </div>
</template>

<script setup>
const baseGitHubUrl = 'https://github.com/camillanapoles/lgpd-mkt-intel/blob/main/'

const docsBySection = [
  {
    title: 'Raiz do repositório',
    docs: [
      'BUSINESS-PLAN.md',
      'FLUXO-TESTE-UX.md',
      'battle-card-confidata.md',
      'divisao-funcoes-cronograma.md',
      'draft-pesquisa-lgpd.md',
      'estrategia-diferenciacao-confidata.md',
      'insights-reuniao-06-05.md',
      'inteligencia-mercado-govtech-lgpd.md',
      'memo-confidata-analysis.md',
      'plano-negocios-cit-ai-tech.md',
      'to-plan.md',
      'transcricao-reuniao-lgpd-06-05-26.md'
    ]
  },
  {
    title: 'Documentos em /docs',
    docs: [
      'docs/INPI_CHECKLIST_REGISTRO_SOFTWARE_IA.md',
      'docs/co-founder-advisor-municipal-sales.md',
      'docs/whitepaper-dispensa-licitacao-ict-lgpd.md'
    ]
  },
  {
    title: 'Templates em /docs/templates',
    docs: [
      'docs/templates/LOI-LGPD-Prefeituras-DOCX-PLACEHOLDER.md',
      'docs/templates/LOI-LGPD-Prefeituras.md',
      'docs/templates/README-LOI.md'
    ]
  },
  {
    title: 'Documentação do app',
    docs: [
      'app/README.md'
    ]
  }
]

const wikiSections = docsBySection.map((section) => ({
  title: section.title,
  docs: section.docs.map((path) => ({
    path,
    name: path.split('/').pop(),
    url: `${baseGitHubUrl}${path}`
  }))
}))
</script>
