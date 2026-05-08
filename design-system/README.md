# LGPD Gov Dashboard - Design System

## Quick Start

### 1. Import the CSS

```html
<link rel="stylesheet" href="/design-system/tokens.css">
<link rel="stylesheet" href="/design-system/components.css">
```

Or in your main CSS:

```css
@import './design-system/tokens.css';
@import './design-system/components.css';
```

### 2. Use the Components

```html
<!-- KPI Card -->
<div class="card">
  <div class="card-body">
    <div class="kpi-card">
      <span class="kpi-label">Conformidade LGPD</span>
      <span class="kpi-value">94.5%</span>
      <span class="kpi-change kpi-change--positive">
        <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 10l7-7m0 0l7 7m-7-7v18" />
        </svg>
        +2.3%
      </span>
    </div>
  </div>
</div>

<!-- Alert -->
<div class="alert alert--warning">
  <svg class="alert-icon" fill="currentColor" viewBox="0 0 20 20">
    <path fill-rule="evenodd" d="M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z" clip-rule="evenodd" />
  </svg>
  <div class="alert-content">
    <div class="alert-title">Atenção Necessária</div>
    <div class="alert-message">3 solicitações de acesso pendentes desta semana.</div>
  </div>
</div>

<!-- Status Badge -->
<span class="badge badge--success">
  <span class="badge-dot"></span>
  Conforme
</span>
```

### 3. Dark Mode Support

```javascript
// Toggle dark mode
const root = document.documentElement;
const currentTheme = root.getAttribute('data-theme');
const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
root.setAttribute('data-theme', newTheme);
localStorage.setItem('theme', newTheme);
```

## File Structure

```
design-system/
├── MASTER.md          # Complete documentation (this file)
├── tokens.css         # CSS variables (colors, typography, spacing)
├── components.css     # Component styles (buttons, cards, alerts, etc.)
├── tokens.json        # Design tokens in JSON format
└── README.md          # Quick start guide
```

## Color Palette Quick Reference

| Color | Hex | Usage |
|-------|-----|-------|
| Primary 600 | `#2563eb` | Primary actions, links |
| Success 600 | `#16a34a` | Compliance, success states |
| Warning 600 | `#d97706` | Warnings, attention needed |
| Error 600 | `#dc2626` | Non-compliance, errors |

## Accessibility Checklist

- [x] WCAG 2.1 AA compliant colors (4.5:1 contrast ratio)
- [x] Focus visible states for all interactive elements
- [x] Reduced motion support
- [x] Screen reader optimized markup
- [x] Keyboard navigation support
- [x] High contrast mode support

## Browser Support

- Chrome/Edge 90+
- Firefox 88+
- Safari 14+
- Mobile Safari iOS 14+
- Chrome Android

## License

Internal use - ICT LGPD Team
