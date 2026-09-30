# LGPD Executive Dashboard Design System

**Version:** 1.0.0
**Last Updated:** 2026-05-08
**Status:** Production Ready

---

## Overview

This design system is tailored for the **LGPD Executive Dashboard** — an interactive strategic presentation platform for government decision-makers. It prioritizes trust, compliance, governance, and data-driven clarity.

### Product Context

| Attribute | Value |
|-----------|-------|
| **Product Type** | SaaS B2B Government (LGPD Compliance) |
| **Target Audience** | Prefeituras, consórcios, TCEs, decision-makers |
| **Usage Context** | Strategic meetings, conference room presentations |
| **Platform** | Vue 3 + Tailwind CSS |
| **Deployment** | GitHub Pages (static) |

---

## Design Principles

| Principle | Application |
|-----------|-------------|
| **Trust** | Government-standard blues, verified badges, clear status indicators |
| **Transparency** | High contrast (4.5:1+), readable fonts, explicit feedback |
| **Professionalism** | Clean layouts, purposeful animations, no clutter |
| **Efficiency** | Clear hierarchy, quick scanning, mobile-optimized for tablets |

---

## Color System

### Primary Palette (Corporate Trust Navy)

```css
:root {
  --color-primary: #0F172A;      /* Navy - Primary brand */
  --color-on-primary: #FFFFFF;   /* White text on navy */
  --color-secondary: #334155;    /* Slate - Secondary elements */
  --color-accent: #0369A1;       /* Blue - CTA/Action */
  --color-background: #F8FAFC;   /* Light slate - Page bg */
  --color-foreground: #020617;   /* Near black - Text */
  --color-muted: #E8ECF1;        /* Light gray - Disabled/placeholder */
  --color-border: #E2E8F0;       /* Gray - Dividers */
  --color-destructive: #DC2626;  /* Red - Error/delete */
  --color-ring: #0F172A;         /* Navy - Focus ring */
}
```

### Tailwind Config Colors

```javascript
colors: {
  primary: {
    DEFAULT: '#0F172A',
    50: '#F8FAFC',
    100: '#F1F5F9',
    200: '#E2E8F0',
    300: '#CBD5E1',
    400: '#94A3B8',
    500: '#64748B',
    600: '#475569',
    700: '#334155',
    800: '#1E293B',
    900: '#0F172A',
  },
  accent: {
    DEFAULT: '#0369A1',
    50: '#F0F9FF',
    100: '#E0F2FE',
    200: '#BAE6FD',
    300: '#7DD3FC',
    400: '#38BDF8',
    500: '#0EA5E9',
    600: '#0369A1',
    700: '#075985',
    800: '#0C4A6E',
    900: '#082F49',
  },
  success: '#10B981',
  warning: '#F59E0B',
  error: '#DC2626',
  info: '#3B82F6',
}
```

### Semantic Color Mappings

| Usage | Color | Token |
|-------|-------|-------|
| Primary actions | Navy | `--color-primary` |
| Secondary actions | Slate | `--color-secondary` |
| CTA/Highlights | Blue | `--color-accent` |
| Success/Compliance | Green | `--color-success` |
| Warning/Attention | Amber | `--color-warning` |
| Error/Violation | Red | `--color-error` |
| Background | Light slate | `--color-background` |

---

## Typography

### Font Stack

```css
@import url('https://fonts.googleapis.com/css2?family=Lexend:wght@300;400;500;600;700&family=Source+Sans+3:wght@300;400;500;600;700&display=swap');

:root {
  --font-heading: 'Lexend', sans-serif;
  --font-body: 'Source Sans 3', sans-serif;
}
```

### Type Scale

| Role | Size | Weight | Line Height | Usage |
|------|------|--------|-------------|-------|
| Display Hero | 48px (3rem) | 700 | 1.1 | Slide titles |
| H1 | 36px (2.25rem) | 700 | 1.2 | Main headings |
| H2 | 30px (1.875rem) | 600 | 1.2 | Section headers |
| H3 | 24px (1.5rem) | 600 | 1.33 | Subsection headers |
| H4 | 20px (1.25rem) | 500 | 1.5 | Card titles |
| Body Large | 18px (1.125rem) | 400 | 1.5 | Emphasized text |
| Body | 16px (1rem) | 400 | 1.5 | Default text |
| Body Small | 14px (0.875rem) | 400 | 1.5 | Secondary text |
| Caption | 12px (0.75rem) | 400 | 1.5 | Fine print |

### Tailwind Font Classes

```javascript
fontFamily: {
  heading: ['Lexend', 'sans-serif'],
  body: ['Source Sans 3', 'sans-serif'],
},
fontSize: {
  'display': ['3rem', { lineHeight: '1.1', fontWeight: '700' }],
  'h1': ['2.25rem', { lineHeight: '1.2', fontWeight: '700' }],
  'h2': ['1.875rem', { lineHeight: '1.2', fontWeight: '600' }],
  'h3': ['1.5rem', { lineHeight: '1.33', fontWeight: '600' }],
  'h4': ['1.25rem', { lineHeight: '1.5', fontWeight: '500' }],
  'body-lg': ['1.125rem', { lineHeight: '1.5' }],
  'body': ['1rem', { lineHeight: '1.5' }],
  'body-sm': ['0.875rem', { lineHeight: '1.5' }],
  'caption': ['0.75rem', { lineHeight: '1.5' }],
}
```

---

## Spacing & Layout

### Spacing Scale

| Token | Value | Usage |
|-------|-------|-------|
| `spacing-0` | 0 | None |
| `spacing-1` | 4px | Micro gaps |
| `spacing-2` | 8px | Small gaps |
| `spacing-3` | 12px | Compact padding |
| `spacing-4` | 16px | Default padding |
| `spacing-6` | 24px | Section spacing |
| `spacing-8` | 32px | Large sections |
| `spacing-12` | 48px | Slide margins |
| `spacing-16` | 64px | Hero spacing |

### Container Widths (Presentation)

| Breakpoint | Max Width | Usage |
|------------|-----------|-------|
| Mobile | 100% | Full width |
| Tablet | 768px | Portrait presentation |
| Desktop | 1024px | Landscape presentation |
| Large | 1280px | Widescreen display |

---

## Components

### Button Styles

| Variant | Classes | Usage |
|---------|---------|-------|
| Primary | `bg-primary text-white hover:bg-primary-800` | Main actions |
| Secondary | `bg-slate-100 text-primary hover:bg-slate-200` | Alternative actions |
| Accent | `bg-accent text-white hover:bg-accent-700` | CTAs, highlights |
| Ghost | `text-primary hover:bg-slate-100` | Tertiary actions |
| Destructive | `bg-error text-white hover:bg-error-700` | Delete, cancel |

### Card Styles

```css
.card {
  background: white;
  border: 1px solid var(--color-border);
  border-radius: 12px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  padding: 1.5rem;
}

.card:hover {
  box-shadow: 0 10px 15px rgba(0, 0, 0, 0.1);
  transition: box-shadow 150ms ease;
}
```

### Badge Styles

| Status | Background | Text | Usage |
|--------|-----------|------|-------|
| Success | Green-100 | Green-700 | Compliant |
| Warning | Amber-100 | Amber-700 | Attention needed |
| Error | Red-100 | Red-700 | Non-compliant |
| Info | Blue-100 | Blue-700 | Information |
| Neutral | Gray-100 | Gray-700 | Uncategorized |

---

## Accessibility (WCAG AA)

### Contrast Requirements

| Element | Minimum Ratio | Target Ratio |
|---------|---------------|--------------|
| Normal text (16px+) | 4.5:1 | 7:1 |
| Large text (24px+) | 3:1 | 4.5:1 |
| UI components | 3:1 | 4.5:1 |

### Focus States

```css
:focus-visible {
  outline: 2px solid var(--color-ring);
  outline-offset: 2px;
}
```

### Touch Targets

- Minimum: 44px × 44px (mobile)
- Recommended: 48px × 48px
- Spacing: 8px+ between targets

---

## Animation

### Timing

| Type | Duration | Easing |
|------|----------|--------|
| Micro-interactions | 150ms | ease-out |
| Page transitions | 300ms | ease-in-out |
| Complex animations | 400ms | cubic-bezier(0.4, 0, 0.2, 1) |

### Motion Rules

- Use `transform` and `opacity` only
- Never animate `width`, `height`, `top`, `left`
- Respect `prefers-reduced-motion`

---

## Dark Mode

### Dark Mode Variables

```css
:root[data-theme="dark"] {
  --color-primary: '#F8FAFC';
  --color-on-primary: '#0F172A';
  --color-background: '#0F172A';
  --color-foreground: '#F8FAFC';
  --color-border: '#334155';
  --color-muted: '#1E293B';
}
```

---

## Tailwind Configuration

```javascript
// tailwind.config.js
export default {
  content: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  darkMode: ['class', '[data-theme="dark"]'],
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: '#0F172A',
          50: '#F8FAFC',
          100: '#F1F5F9',
          200: '#E2E8F0',
          300: '#CBD5E1',
          400: '#94A3B8',
          500: '#64748B',
          600: '#475569',
          700: '#334155',
          800: '#1E293B',
          900: '#0F172A',
        },
        accent: {
          DEFAULT: '#0369A1',
          50: '#F0F9FF',
          100: '#E0F2FE',
          200: '#BAE6FD',
          300: '#7DD3FC',
          400: '#38BDF8',
          500: '#0EA5E9',
          600: '#0369A1',
          700: '#075985',
          800: '#0C4A6E',
          900: '#082F49',
        },
      },
      fontFamily: {
        heading: ['Lexend', 'sans-serif'],
        body: ['Source Sans 3', 'sans-serif'],
      },
    },
  },
  plugins: [],
}
```

---

## Pre-Delivery Checklist

- [ ] No emojis as structural icons (use SVG: Heroicons/Lucide)
- [ ] cursor-pointer on all clickable elements
- [ ] Hover states with smooth transitions (150-300ms)
- [ ] Light mode text contrast 4.5:1 minimum
- [ ] Focus states visible for keyboard navigation
- [ ] prefers-reduced-motion respected
- [ ] Responsive tested: 375px, 768px, 1024px, 1440px
- [ ] Touch targets >= 44px × 44px
- [ ] Dark mode contrast verified independently
- [ ] All images have alt text or aria-hidden
- [ ] Color not used as the only indicator of meaning
