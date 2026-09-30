# LGPD Strategic Presentation

Painel estrategico interativo para planejamento LGPD e alinhamento de decisoes em reunioes.

## Stack Tecnologico

- **Vue 3** - Framework reativo
- **Vite** - Build tool
- **TypeScript** - Tipagem estatica
- **Tailwind CSS** - Estilizacao
- **Pinia** - Gerenciamento de estado
- **Chart.js + vue-chartjs** - Visualizacao de dados
- **GSAP** - Animacoes avancadas
- **GitHub Pages** - Deploy

## Estrutura

```
src/
├── components/
│   ├── strategic/          # Componentes de analise estrategica
│   │   ├── SwotAnalysis.vue
│   │   ├── BusinessModelCanvas.vue
│   │   ├── RoadmapViewer.vue
│   │   ├── ScenarioSimulator.vue
│   │   └── Dashboard5s.vue
│   ├── layout/             # Componentes de layout
│   │   ├── PresentationNav.vue
│   │   ├── SlideContainer.vue
│   │   └── ProgressBar.vue
│   └── interactive/        # Componentes interativos
│       ├── DecisionMatrix.vue
│       ├── StakeholderMap.vue
│       ├── TimelineSlider.vue
│       └── ComparisonTable.vue
├── views/                  # Views principais
├── stores/                 # Pinia stores
├── types/                  # Tipos TypeScript
├── data/                   # Fonte unica JSON
├── composables/            # Vue composables
└── assets/                 # Recursos estaticos
```

## Instalacao

```bash
npm install
```

## Desenvolvimento

```bash
npm run dev
```

## Build

```bash
npm run build
```

O output fica em `dist/`, pronto para deploy.

## Deploy GitHub Pages

O deploy e automatico via GitHub Actions. A cada push para `main`, o workflow em `.github/workflows/deploy.yml` executa build e publica em GitHub Pages.

### URL

```
https://camillanapoles.github.io/lgpd-mkt-intel/lgpd-strategy/
```

### Configuracao no Repositorio

1. Acesse **Settings > Pages**
2. Em **Source**, selecione **GitHub Actions**
3. Faca push para `main` -- o workflow cuida do resto

### Primeiro Deploy

```bash
# Certifique-se de que package-lock.json existe
npm install

# Teste o build localmente antes de push
npm run build
ls dist/   # deve conter index.html e assets/
```

### Custom Domain (Opcional)

Para usar um dominio personalizado em vez de `username.github.io`:

**1. Crie o arquivo CNAME no diretorio `public/`:**
```
echo "seu-dominio.com" > public/CNAME
```

**2. Configure DNS no seu provedor:**

| Tipo  | Nome             | Valor                                    |
|-------|------------------|------------------------------------------|
| CNAME | `www`            | `camillanapoles.github.io`               |
| CNAME | `@` (ou vazio)   | `camillanapoles.github.io`               |

**3. Configure no GitHub:**

1. Acesse **Settings > Pages > Custom domain**
2. Insira `seu-dominio.com`
3. Marque **Enforce HTTPS** (leva alguns minutos apos o DNS propagar)
4. O GitHub cria automaticamente 4 registros no repositorio:
   - Um commit com `CNAME` no `gh-pages` branch
   - Um commit com `_headers` (HSTS)

**4. Verifique a propagacao:**
```bash
dig seu-dominio.com CNAME +short
# Deve retornar: camillanapoles.github.io
```

**Nota:** Se usar custom domain, remova o `base` prefixo de `vite.config.js` e altere para `base: '/'`.

### Ativar Analytics

O template em `index.html` contem placeholders para GTM e GA4. Para ativar:

**Google Tag Manager:**
1. Substitua `GTM-XXXXXXX` pelo seu Container ID
2. Descomente as tags `<script>` do GTM (head e body)

**Google Analytics 4:**
1. Substitua `G-XXXXXXXXXX` pelo seu Measurement ID
2. Descomente as tags `<script>` do GA4

### SPA Routing

O arquivo `public/404.html` implementa o redirect de SPA para GitHub Pages. Quando o usuario acessa uma URL direta (ex: `/lgpd-strategy/swot`), o GitHub Pages serve `404.html`, que redireciona para `index.html` com o caminho preservado como query parameter.

## Fonte Unica de Verdade

Todos os dados estrategicos residem em `src/data/` com validacao VVV:

- **V**erified - Verificado por agente especialista
- **V**alidated - Validado contra metodologia
- **V**eracity - Fontes rastreaveis

## Metodologia

1. Extracao de cenario atual da transcricao
2. Mapeamento de insights com fontes
3. Analise SWOT justificada
4. BMC alinhado ao plano estrategico
5. Roadmap com dependencias
6. Simulacao de cenarios interativa
7. Dashboard 5s para decisoes rapidas
