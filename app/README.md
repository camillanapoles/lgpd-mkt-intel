# LGPD Executive Dashboard

Dashboard executivo interativo para tomada de decisão estratégica - Contabilizei da Privacy.

## Tecnologias

- **Vue.js 3** - Framework frontend reativo
- **Vite** - Build tool ultra-rápido
- **Vue Router** - Roteamento SPA
- **Chart.js** - Visualização de dados
- **TailwindCSS** - Estilização utility-first

## Estrutura do App

```
app/
├── src/
│   ├── components/        # Componentes reutilizáveis
│   │   ├── Navigation.vue
│   │   ├── MetricCard.vue
│   │   ├── ScenarioSelector.vue
│   │   └── ChartComponent.vue
│   ├── pages/            # Páginas da aplicação
│   │   ├── Dashboard.vue
│   │   ├── Scenarios.vue
│   │   ├── BMC.vue
│   │   ├── Roadmap.vue
│   │   └── SWOT.vue
│   ├── data/             # Dados estratégicos
│   │   └── strategicData.js
│   ├── styles/           # Estilos globais
│   │   └── main.css
│   ├── App.vue           # Componente root
│   └── main.js           # Entry point
├── index.html
├── vite.config.js
├── tailwind.config.js
└── package.json
```

## Desenvolvimento

```bash
cd app
npm install
npm run dev
```

O app estará disponível em `http://localhost:5173`

## Build para Produção

```bash
cd app
npm run build
```

Os arquivos serão gerados em `app/dist/`

## Deploy no GitHub Pages

O deploy é automático via GitHub Actions ao fazer push para `main`.

URL: `https://[username].github.io/LGPD/app/`

## Páginas

1. **Dashboard** - Visão geral com métricas chave (TAM, SAM, SOM, CAGR)
2. **Cenários** - Simulador interativo de diferentes estratégias
3. **BMC** - Business Model Canvas completo
4. **Roadmap** - Cronograma faseado até PMF
5. **SWOT** - Análise de forças, fraquezas, oportunidades e ameaças

## Dados

Os dados estratégicos estão centralizados em `src/data/strategicData.js` e são extraídos do `BUSINESS-PLAN.md`.
