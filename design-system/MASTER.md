# LGPD Gov Dashboard Design System

**Version:** 1.0.0
**Last Updated:** 2026-05-08
**Status:** Production Ready

---

## Table of Contents

1. [Principles](#principles)
2. [Color System](#color-system)
3. [Typography](#typography)
4. [Spacing & Layout](#spacing--layout)
5. [Components](#components)
6. [Accessibility](#accessibility)
7. [Dark Mode](#dark-mode)
8. [Implementation](#implementation)

---

## Principles

### Core Values

| Principle | Description | Application |
|-----------|-------------|-------------|
| **Trust** | Build confidence through consistency | Government-standard blues, verified badges, clear status |
| **Transparency** | Make information clear and accessible | High contrast, readable fonts, explicit feedback |
| **Professionalism** | Maintain dignity and seriousness | Clean layouts, purposeful animations, no clutter |
| **Efficiency** | Respect public servants' time | Clear hierarchy, quick scanning, mobile-optimized |

### Accessibility First

- WCAG 2.1 AA compliance minimum
- 4.5:1 contrast ratio for normal text
- 3:1 contrast ratio for large text
- Keyboard navigation support
- Screen reader optimized
- Color-blind safe palettes

---

## Color System

### Primary Palette (Government Trust Blues)

```css
:root {
  /* Primary - Government Blue */
  --color-primary-50: #eff6ff;
  --color-primary-100: #dbeafe;
  --color-primary-200: #bfdbfe;
  --color-primary-300: #93c5fd;
  --color-primary-400: #60a5fa;
  --color-primary-500: #3b82f6;
  --color-primary-600: #2563eb;
  --color-primary-700: #1d4ed8;
  --color-primary-800: #1e40af;
  --color-primary-900: #1e3a8a;

  /* Semantic mappings */
  --color-primary: var(--color-primary-600);
  --color-primary-hover: var(--color-primary-700);
  --color-primary-active: var(--color-primary-800);
  --color-primary-light: var(--color-primary-50);
}
```

### Secondary Palette (Compliance Greens)

```css
:root {
  /* Success - Compliance Green */
  --color-success-50: #f0fdf4;
  --color-success-100: #dcfce7;
  --color-success-200: #bbf7d0;
  --color-success-300: #86efac;
  --color-success-400: #4ade80;
  --color-success-500: #22c55e;
  --color-success-600: #16a34a;
  --color-success-700: #15803d;
  --color-success-800: #166534;
  --color-success-900: #14532d;

  /* Semantic mappings */
  --color-success: var(--color-success-600);
  --color-success-hover: var(--color-success-700);
}
```

### Semantic Colors

```css
:root {
  /* Warning - Alert Orange */
  --color-warning-50: #fffbeb;
  --color-warning-100: #fef3c7;
  --color-warning-500: #f59e0b;
  --color-warning-600: #d97706;
  --color-warning: var(--color-warning-600);

  /* Error - Critical Red */
  --color-error-50: #fef2f2;
  --color-error-100: #fee2e2;
  --color-error-500: #ef4444;
  --color-error-600: #dc2626;
  --color-error: var(--color-error-600);

  /* Info - Neutral Blue */
  --color-info-500: #0ea5e9;
  --color-info-600: #0284c7;
  --color-info: var(--color-info-600);
}
```

### Neutral Palette

```css
:root {
  /* Gray Scale */
  --color-gray-50: #f9fafb;
  --color-gray-100: #f3f4f6;
  --color-gray-200: #e5e7eb;
  --color-gray-300: #d1d5db;
  --color-gray-400: #9ca3af;
  --color-gray-500: #6b7280;
  --color-gray-600: #4b5563;
  --color-gray-700: #374151;
  --color-gray-800: #1f2937;
  --color-gray-900: #111827;

  /* Semantic mappings */
  --color-text-primary: var(--color-gray-900);
  --color-text-secondary: var(--color-gray-600);
  --color-text-tertiary: var(--color-gray-500);
  --color-text-inverse: #ffffff;
  --color-border: var(--color-gray-200);
  --color-border-subtle: var(--color-gray-100);
  --color-bg-primary: #ffffff;
  --color-bg-secondary: var(--color-gray-50);
  --color-bg-tertiary: var(--color-gray-100);
}
```

### Color Contrast Requirements

| Text Size | Minimum Contrast | Usage |
|-----------|------------------|-------|
| Normal (16px+) | 4.5:1 | Body text, labels |
| Large (24px+) | 3:1 | Headings, key messages |
| UI Components | 3:1 | Buttons, badges, icons |

---

## Typography

### Font Stack

```css
:root {
  --font-family-sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI',
                      Roboto, 'Helvetica Neue', Arial, sans-serif;
  --font-family-mono: 'JetBrains Mono', 'Fira Code', Consolas, monospace;
}
```

### Type Scale

| Size | px | rem | Line Height | Weight | Usage |
|------|-----|-----|-------------|--------|-------|
| xs | 12 | 0.75 | 1.5 | 400 | Captions, legal |
| sm | 14 | 0.875 | 1.5 | 400 | Secondary text |
| base | 16 | 1 | 1.5 | 400 | Body text |
| lg | 18 | 1.125 | 1.5 | 400 | Emphasized body |
| xl | 20 | 1.25 | 1.5 | 500 | Subheadings |
| 2xl | 24 | 1.5 | 1.33 | 600 | Section headers |
| 3xl | 30 | 1.875 | 1.2 | 600 | Page titles |
| 4xl | 36 | 2.25 | 1.2 | 700 | Display titles |
| 5xl | 48 | 3 | 1.1 | 700 | Hero titles |

```css
:root {
  --text-xs: 0.75rem;
  --text-sm: 0.875rem;
  --text-base: 1rem;
  --text-lg: 1.125rem;
  --text-xl: 1.25rem;
  --text-2xl: 1.5rem;
  --text-3xl: 1.875rem;
  --text-4xl: 2.25rem;
  --text-5xl: 3rem;

  --leading-tight: 1.2;
  --leading-snug: 1.33;
  --leading-normal: 1.5;
  --leading-relaxed: 1.625;
}
```

### Font Weights

```css
:root {
  --font-weight-normal: 400;
  --font-weight-medium: 500;
  --font-weight-semibold: 600;
  --font-weight-bold: 700;
}
```

---

## Spacing & Layout

### Spacing Scale

```css
:root {
  --spacing-0: 0;
  --spacing-1: 0.25rem;    /* 4px */
  --spacing-2: 0.5rem;     /* 8px */
  --spacing-3: 0.75rem;    /* 12px */
  --spacing-4: 1rem;       /* 16px */
  --spacing-5: 1.25rem;    /* 20px */
  --spacing-6: 1.5rem;     /* 24px */
  --spacing-8: 2rem;       /* 32px */
  --spacing-10: 2.5rem;    /* 40px */
  --spacing-12: 3rem;      /* 48px */
  --spacing-16: 4rem;      /* 64px */
  --spacing-20: 5rem;      /* 80px */
  --spacing-24: 6rem;      /* 96px */
}
```

### Container Widths

```css
:root {
  --container-sm: 640px;
  --container-md: 768px;
  --container-lg: 1024px;
  --container-xl: 1280px;
  --container-2xl: 1536px;
}
```

### Grid System

```css
:root {
  --grid-columns: 12;
  --grid-gap: var(--spacing-6);
  --grid-gap-sm: var(--spacing-4);
}
```

### Border Radius

```css
:root {
  --radius-none: 0;
  --radius-sm: 0.25rem;    /* 4px */
  --radius-base: 0.375rem; /* 6px */
  --radius-md: 0.5rem;     /* 8px */
  --radius-lg: 0.75rem;    /* 12px */
  --radius-xl: 1rem;       /* 16px */
  --radius-full: 9999px;
}
```

### Shadows

```css
:root {
  --shadow-xs: 0 1px 2px rgba(0, 0, 0, 0.05);
  --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.1), 0 1px 2px rgba(0, 0, 0, 0.06);
  --shadow-base: 0 4px 6px rgba(0, 0, 0, 0.07), 0 2px 4px rgba(0, 0, 0, 0.06);
  --shadow-md: 0 10px 15px rgba(0, 0, 0, 0.1), 0 4px 6px rgba(0, 0, 0, 0.05);
  --shadow-lg: 0 20px 25px rgba(0, 0, 0, 0.1), 0 10px 10px rgba(0, 0, 0, 0.04);
  --shadow-xl: 0 25px 50px rgba(0, 0, 0, 0.25);
}
```

---

## Components

### Button

```css
:root {
  --button-height: 2.5rem;
  --button-padding-x: var(--spacing-4);
  --button-font-size: var(--text-sm);
  --button-font-weight: var(--font-weight-medium);
  --button-radius: var(--radius-md);
  --button-transition: all 150ms ease;
}

/* Base Button */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: var(--spacing-2);
  height: var(--button-height);
  padding: 0 var(--button-padding-x);
  font-size: var(--button-font-size);
  font-weight: var(--button-font-weight);
  border-radius: var(--button-radius);
  transition: var(--button-transition);
  cursor: pointer;
  border: none;
}

/* Primary Button */
.btn-primary {
  background-color: var(--color-primary);
  color: var(--color-text-inverse);
}

.btn-primary:hover {
  background-color: var(--color-primary-hover);
}

.btn-primary:focus-visible {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
}

/* Secondary Button */
.btn-secondary {
  background-color: var(--color-bg-secondary);
  color: var(--color-text-primary);
  border: 1px solid var(--color-border);
}

.btn-secondary:hover {
  background-color: var(--color-bg-tertiary);
}

/* Ghost Button */
.btn-ghost {
  background-color: transparent;
  color: var(--color-primary);
}

.btn-ghost:hover {
  background-color: var(--color-primary-light);
}
```

### Card

```css
:root {
  --card-padding: var(--spacing-6);
  --card-radius: var(--radius-lg);
  --card-shadow: var(--shadow-base);
  --card-border: 1px solid var(--color-border-subtle);
}

.card {
  background-color: var(--color-bg-primary);
  border-radius: var(--card-radius);
  box-shadow: var(--card-shadow);
  border: var(--card-border);
  overflow: hidden;
}

.card-header {
  padding: var(--card-padding);
  border-bottom: 1px solid var(--color-border-subtle);
}

.card-body {
  padding: var(--card-padding);
}

.card-footer {
  padding: var(--card-padding);
  border-top: 1px solid var(--color-border-subtle);
  background-color: var(--color-bg-secondary);
}
```

### KPI Card

```css
.kpi-card {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-2);
}

.kpi-label {
  font-size: var(--text-sm);
  color: var(--color-text-secondary);
  font-weight: var(--font-weight-medium);
}

.kpi-value {
  font-size: var(--text-4xl);
  font-weight: var(--font-weight-bold);
  color: var(--color-text-primary);
  line-height: var(--leading-tight);
}

.kpi-change {
  display: inline-flex;
  align-items: center;
  gap: var(--spacing-1);
  font-size: var(--text-sm);
  font-weight: var(--font-weight-medium);
}

.kpi-change--positive {
  color: var(--color-success);
}

.kpi-change--negative {
  color: var(--color-error);
}

.kpi-change--neutral {
  color: var(--color-text-secondary);
}
```

### Badge

```css
.badge {
  display: inline-flex;
  align-items: center;
  padding: var(--spacing-1) var(--spacing-2);
  font-size: var(--text-xs);
  font-weight: var(--font-weight-medium);
  border-radius: var(--radius-full);
  gap: var(--spacing-1);
}

.badge--success {
  background-color: var(--color-success-100);
  color: var(--color-success-700);
}

.badge--warning {
  background-color: var(--color-warning-100);
  color: var(--color-warning-700);
}

.badge--error {
  background-color: var(--color-error-100);
  color: var(--color-error-700);
}

.badge--info {
  background-color: var(--color-info-100);
  color: var(--color-info-700);
}

.badge--neutral {
  background-color: var(--color-gray-100);
  color: var(--color-gray-700);
}
```

### Alert

```css
.alert {
  display: flex;
  gap: var(--spacing-3);
  padding: var(--spacing-4);
  border-radius: var(--radius-md);
  border-left: 4px solid;
}

.alert--info {
  background-color: var(--color-info-50);
  border-color: var(--color-info-500);
  color: var(--color-info-700);
}

.alert--success {
  background-color: var(--color-success-50);
  border-color: var(--color-success-500);
  color: var(--color-success-700);
}

.alert--warning {
  background-color: var(--color-warning-50);
  border-color: var(--color-warning-500);
  color: var(--color-warning-700);
}

.alert--error {
  background-color: var(--color-error-50);
  border-color: var(--color-error-500);
  color: var(--color-error-700);
}

.alert-icon {
  flex-shrink: 0;
  width: 1.25rem;
  height: 1.25rem;
}

.alert-content {
  flex: 1;
}

.alert-title {
  font-weight: var(--font-weight-semibold);
  margin-bottom: var(--spacing-1);
}

.alert-message {
  font-size: var(--text-sm);
}
```

### Progress Bar

```css
:root {
  --progress-height: 0.5rem;
  --progress-radius: var(--radius-full);
}

.progress {
  width: 100%;
  height: var(--progress-height);
  background-color: var(--color-gray-200);
  border-radius: var(--progress-radius);
  overflow: hidden;
}

.progress-bar {
  height: 100%;
  background-color: var(--color-primary);
  border-radius: var(--progress-radius);
  transition: width 300ms ease;
}

.progress-bar--success {
  background-color: var(--color-success);
}

.progress-bar--warning {
  background-color: var(--color-warning);
}

.progress-bar--error {
  background-color: var(--color-error);
}
```

### Table

```css
.table-container {
  width: 100%;
  overflow-x: auto;
  border-radius: var(--radius-lg);
  border: var(--card-border);
}

.table {
  width: 100%;
  border-collapse: collapse;
  background-color: var(--color-bg-primary);
}

.table thead {
  background-color: var(--color-bg-secondary);
  border-bottom: 1px solid var(--color-border);
}

.table th {
  padding: var(--spacing-3) var(--spacing-4);
  text-align: left;
  font-size: var(--text-xs);
  font-weight: var(--font-weight-semibold);
  color: var(--color-text-secondary);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.table td {
  padding: var(--spacing-3) var(--spacing-4);
  border-bottom: 1px solid var(--color-border-subtle);
  font-size: var(--text-sm);
  color: var(--color-text-primary);
}

.table tbody tr:hover {
  background-color: var(--color-bg-secondary);
}

.table tbody tr:last-child td {
  border-bottom: none;
}
```

### Modal

```css
.modal-backdrop {
  position: fixed;
  inset: 0;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  padding: var(--spacing-4);
}

.modal {
  background-color: var(--color-bg-primary);
  border-radius: var(--radius-xl);
  box-shadow: var(--shadow-xl);
  max-width: 500px;
  width: 100%;
  max-height: 90vh;
  overflow: auto;
}

.modal-header {
  padding: var(--spacing-6);
  border-bottom: 1px solid var(--color-border-subtle);
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.modal-title {
  font-size: var(--text-xl);
  font-weight: var(--font-weight-semibold);
  color: var(--color-text-primary);
}

.modal-body {
  padding: var(--spacing-6);
}

.modal-footer {
  padding: var(--spacing-6);
  border-top: 1px solid var(--color-border-subtle);
  display: flex;
  gap: var(--spacing-3);
  justify-content: flex-end;
}
```

### Status Indicator

```css
.status-indicator {
  display: inline-flex;
  align-items: center;
  gap: var(--spacing-2);
}

.status-dot {
  width: 0.5rem;
  height: 0.5rem;
  border-radius: var(--radius-full);
  position: relative;
}

.status-dot::after {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: inherit;
  animation: pulse 2s ease-in-out infinite;
}

.status-dot--online {
  background-color: var(--color-success);
}

.status-dot--online::after {
  background-color: var(--color-success);
}

.status-dot--offline {
  background-color: var(--color-gray-400);
}

.status-dot--offline::after {
  display: none;
}

.status-dot--busy {
  background-color: var(--color-warning);
}

.status-dot--busy::after {
  background-color: var(--color-warning);
}

@keyframes pulse {
  0%, 100% {
    opacity: 1;
    transform: scale(1);
  }
  50% {
    opacity: 0.5;
    transform: scale(1.5);
  }
}
```

---

## Accessibility

### Focus States

```css
:focus-visible {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
}

:focus {
  outline: none;
}

button:focus-visible,
a:focus-visible,
input:focus-visible,
select:focus-visible,
textarea:focus-visible {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
}
```

### Skip Links

```css
.skip-link {
  position: absolute;
  top: -40px;
  left: 0;
  background: var(--color-primary);
  color: var(--color-text-inverse);
  padding: var(--spacing-2) var(--spacing-4);
  z-index: 100;
  transition: top 150ms ease;
}

.skip-link:focus {
  top: 0;
}
```

### Screen Reader Only

```css
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}

.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  padding: inherit;
  margin: inherit;
  overflow: visible;
  clip: auto;
  white-space: normal;
}
```

### Reduced Motion

```css
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

---

## Dark Mode

### Dark Mode Variables

```css
:root[data-theme="dark"] {
  /* Primary colors adjust for dark */
  --color-primary-light: var(--color-primary-900);

  /* Text colors invert */
  --color-text-primary: var(--color-gray-100);
  --color-text-secondary: var(--color-gray-400);
  --color-text-tertiary: var(--color-gray-500);

  /* Background colors invert */
  --color-bg-primary: var(--color-gray-900);
  --color-bg-secondary: var(--color-gray-800);
  --color-bg-tertiary: var(--color-gray-700);

  /* Border colors adjust */
  --color-border: var(--color-gray-700);
  --color-border-subtle: var(--color-gray-800);

  /* Shadow adjustments */
  --shadow-xs: 0 1px 2px rgba(0, 0, 0, 0.3);
  --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.4);
  --shadow-base: 0 4px 6px rgba(0, 0, 0, 0.4);
  --shadow-md: 0 10px 15px rgba(0, 0, 0, 0.5);
  --shadow-lg: 0 20px 25px rgba(0, 0, 0, 0.5);
}
```

### Dark Mode Toggle

```html
<button
  class="theme-toggle"
  aria-label="Alternar tema escuro"
  data-theme-toggle
>
  <svg class="sun-icon" aria-hidden="true">
    <!-- Sun SVG -->
  </svg>
  <svg class="moon-icon" aria-hidden="true">
    <!-- Moon SVG -->
  </svg>
</button>
```

```javascript
// Theme toggle implementation
const themeToggle = document.querySelector('[data-theme-toggle]');
const root = document.documentElement;

// Check for saved preference or system preference
const savedTheme = localStorage.getItem('theme');
const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;

const initialTheme = savedTheme || (systemPrefersDark ? 'dark' : 'light');
root.setAttribute('data-theme', initialTheme);

themeToggle.addEventListener('click', () => {
  const currentTheme = root.getAttribute('data-theme');
  const newTheme = currentTheme === 'dark' ? 'light' : 'dark';

  root.setAttribute('data-theme', newTheme);
  localStorage.setItem('theme', newTheme);
});
```

---

## Implementation

### Tailwind Config

```javascript
// tailwind.config.js
module.exports = {
  darkMode: ['class', '[data-theme="dark"]'],
  theme: {
    extend: {
      colors: {
        primary: {
          50: '#eff6ff',
          100: '#dbeafe',
          200: '#bfdbfe',
          300: '#93c5fd',
          400: '#60a5fa',
          500: '#3b82f6',
          600: '#2563eb',
          700: '#1d4ed8',
          800: '#1e40af',
          900: '#1e3a8a',
        },
        success: {
          50: '#f0fdf4',
          100: '#dcfce7',
          200: '#bbf7d0',
          300: '#86efac',
          400: '#4ade80',
          500: '#22c55e',
          600: '#16a34a',
          700: '#15803d',
          800: '#166534',
          900: '#14532d',
        },
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
        mono: ['JetBrains Mono', 'monospace'],
      },
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
    require('@tailwindcss/aspect-ratio'),
  ],
};
```

### CSS Variables Import

```css
/* styles.css - Import at the top of your stylesheet */
@import './design-system/tokens.css';

/* Or include directly in your main CSS file */
@layer base {
  :root {
    /* All design system variables */
  }

  * {
    @apply border-border;
  }

  body {
    @apply bg-bg-primary text-text-primary font-sans;
  }
}
```

### Vue.js Component Example

```vue
<template>
  <div class="card">
    <div class="card-header">
      <h3 class="text-lg font-semibold">{{ title }}</h3>
    </div>
    <div class="card-body">
      <div class="kpi-card">
        <span class="kpi-label">{{ label }}</span>
        <span class="kpi-value">{{ value }}</span>
        <span v-if="change" :class="changeClass" class="kpi-change">
          <component :is="changeIcon" class="w-4 h-4" />
          {{ change }}
        </span>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue';

const props = defineProps({
  title: String,
  label: String,
  value: [String, Number],
  change: String,
  changeType: {
    type: String,
    default: 'neutral',
    validator: (v) => ['positive', 'negative', 'neutral'].includes(v),
  },
});

const changeClass = computed(() => `kpi-change--${props.changeType}`);
</script>
```

---

## Component Variants

### Button Variants

| Variant | Purpose | Classes |
|---------|---------|---------|
| `btn-primary` | Primary actions | `bg-primary text-white hover:bg-primary-700` |
| `btn-secondary` | Secondary actions | `bg-gray-100 text-gray-900 hover:bg-gray-200` |
| `btn-ghost` | Tertiary actions | `bg-transparent text-primary hover:bg-primary-50` |
| `btn-danger` | Destructive actions | `bg-error text-white hover:bg-error-700` |

### Badge Variants

| Variant | Meaning | Usage |
|---------|---------|-------|
| `badge--success` | Compliant | LGPD requirements met |
| `badge--warning` | Attention needed | Action required soon |
| `badge--error` | Non-compliant | Violations detected |
| `badge--info` | Information | Status updates |
| `badge--neutral` | Uncategorized | General labels |

---

## Mobile Considerations

### Responsive Breakpoints

```css
:root {
  --breakpoint-sm: 640px;
  --breakpoint-md: 768px;
  --breakpoint-lg: 1024px;
  --breakpoint-xl: 1280px;
}
```

### Touch Targets

Minimum touch target size: 44px × 44px (WCAG 2.1 AAA)

```css
@media (pointer: coarse) {
  .btn {
    min-height: 2.75rem;
    min-width: 2.75rem;
  }
}
```

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-05-08 | Initial release - government dashboard design system |

---

## Maintenance

This design system is maintained by the ICT LGPD team. For questions or suggestions, please refer to the project repository.

**Last Review:** 2026-05-08
**Next Review:** 2026-08-08
