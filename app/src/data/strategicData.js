// Strategic Data - Unified from strategic-data-unified.json + business plan
export const strategicData = {
  metadata: {
    version: '2.1.0',
    lastUpdated: '2026-05-08',
    project: 'LGPD SaaS Municipal - Contabilizei da Privacy',
    framework: 'VVV (Verificacao Verdade Valida) + FDC-U Priority Matrix',
    status: 'GO - com pré-condições de validação',
    strategicScore: 7.2,
    overallConfidence: 0.72
  },

  kpi_5s: {
    headline_mrr: 'R$ 280K',
    headline_customers: 275,
    headline_month: 30,
    critical_vvv_items: 3,
    urgent_actions: 5,
    labels: {
      mrr: 'MRR Projetado (Mês 30 - Base Case)',
      customers: 'Clientes Ativos',
      month: 'Horizonte (meses)',
      vvv: 'Itens VVV < 0.5',
      actions: 'Ações Urgentes'
    }
  },

  marketAnalysis: {
    tam: { value: 60000000, label: 'R$ 60M', description: 'Total municípios sem LGPD (4.011)', vvv: 0.95 },
    sam: { value: 12000000, label: 'R$ 12M', description: 'B2B SaaS municipal 20-100K hab', vvv: 0.8 },
    som: { value: 3000000, label: 'R$ 2-4M', description: '3 anos target inicial', vvv: 0.6 },
    municipalities: { value: 4011, label: '4.011', description: 'Municípios sem LGPD' },
    growthRate: { value: 17.5, label: '15-20%', description: 'CAGR anual' }
  },

  swot: {
    strengths: [
      { id: 'S1', text: 'Gap estratégico: nenhum player DOMINA segmento municipal', impact: 'ALTO' },
      { id: 'S2', text: 'Arbitragem regulatória: Lei 14.133/2021 (R$65K dispensa)', impact: 'ALTO' },
      { id: 'S3', text: 'Produto verticalizado: templates IPTU/e-SUS/education', impact: 'MÉDIO' },
      { id: 'S4', text: 'Unit economics favoráveis: SaaS + DPO fractionado', impact: 'ALTO' },
      { id: 'S5', text: 'Data center 100% Brasil (Art. 26 §1º compliance)', impact: 'ALTO' },
      { id: 'S6', text: 'Pricing transparente (poucos fazem)', impact: 'MÉDIO' }
    ],
    weaknesses: [
      { id: 'W1', text: 'Sem experiência prévia vendas municipais', impact: 'ALTO', mitigation: 'Co-founder/advisor com track record' },
      { id: 'W2', text: 'DPO pool depende de contratação/certificação', impact: 'MÉDIO', mitigation: 'Começar com 2-3 DPOs' },
      { id: 'W3', text: 'Marca desconhecida em mercado confiante', impact: 'MÉDIO', mitigation: 'Primeiros 3 clientes como references' },
      { id: 'W4', text: 'Capital limitado para longos sales cycles', impact: 'ALTO', mitigation: 'Focar municípios TCE-flagged' },
      { id: 'W5', text: 'Stack técnico genérico (sem IP defensável)', impact: 'BAIXO', mitigation: 'IP é em conteúdo + workflows' }
    ],
    opportunities: [
      { id: 'O1', text: 'ANPD oversight ativo 2025+ (forçou demanda)', impact: 'ALTO', timing: 'Imediato' },
      { id: 'O2', text: 'TCEs fiscalizando e multando prefeituras', impact: 'ALTO', timing: 'Em andamento' },
      { id: 'O3', text: '4.011 municípios sem estrutura = greenfield', impact: 'ALTO', timing: 'Janela 3-5 anos' },
      { id: 'O4', text: 'White-label para escritórios advocacia', impact: 'MÉDIO', timing: 'Fase 2-3' },
      { id: 'O5', text: 'Expansão PME (mesmo produto, diferente GTM)', impact: 'ALTO', timing: 'Fase 2' },
      { id: 'O6', text: 'ISO 27701 = certificação como diferencial premium', impact: 'MÉDIO', timing: 'Fase 4' }
    ],
    threats: [
      { id: 'T1', text: 'Inadimplência municipal (12+ meses pagamento)', probability: 'MÉDIA', mitigation: 'Cobrança trimestral' },
      { id: 'T2', text: 'Competidor reage dentro 6-12 meses', probability: 'ALTA', mitigation: 'First-mover + lock-in' },
      { id: 'T3', text: 'ANPD enforcement suaviza (mudança política)', probability: 'BAIXA', mitigation: 'Diversificar PME' },
      { id: 'T4', text: 'Sales cycle >12 meses (burn demais)', probability: 'MÉDIA', mitigation: 'TCE-flagged = urgência' },
      { id: 'T5', text: 'Turnover político quebra contratos', probability: 'MÉDIA', mitigation: 'Serviço essencial' }
    ]
  },

  businessModelCanvas: {
    keyPartners: [
      'Associações de municípios',
      'Escritórios de advocacia',
      'Auditores ISO',
      'AWS (sa-east-1)',
      'ANPD/certificadores'
    ],
    keyActivities: [
      'Dev plataforma',
      'Conteúdo jurídico',
      'Monitoramento LGPD',
      'Treinamentos EAD',
      'Gestão DPO pool'
    ],
    keyResources: [
      'Plataforma SaaS',
      'Pool DPOs certificados',
      'Base jurídica',
      'Marca/confiança',
      'Certificação ISO'
    ],
    valuePropositions: [
      'Abaixo R$65K/ano = sem licitação',
      'DPO fractionado incluído',
      'Templates específicos (IPTU, e-SUS)',
      'Setup em 30 dias, não meses',
      'Relatórios prontos TCE/TCM',
      'Data 100% Brasil (Art. 26)'
    ],
    customerRelationships: [
      'Self-service + suporte',
      'Onboarding guiado',
      'Consultoria tierada',
      'Community (webinars)',
      'Portal do titular'
    ],
    channels: [
      'Self-service web',
      'Marketing digital',
      'Parcerias FNP/FNAM',
      'Events webinars',
      'Referrals (word-of-mouth)',
      'LinkedIn outbound'
    ],
    customerSegments: [
      { name: 'Prefeituras pequenas (<20K)', tam: 2500, priority: 1 },
      { name: 'Prefeituras médias (20-100K)', tam: 1200, priority: 2 },
      { name: 'PMEs', tam: 50000, priority: 3 },
      { name: 'Large enterprise', tam: 500, priority: 4 }
    ],
    costStructure: [
      { category: 'Pessoal', percentage: 60, items: ['Devs', 'DPOs', 'Sales', 'CS'] },
      { category: 'Infra', percentage: 10, items: ['Cloud', 'tools', 'software'] },
      { category: 'Marketing', percentage: 20, items: ['CAC', 'ad spend', 'conteúdo'] },
      { category: 'Legal/ISO', percentage: 10, items: ['Auditorias', 'advocacia'] }
    ],
    revenueStreams: [
      { type: 'Subscription (Core)', range: 'R$297-997/mês' },
      { type: 'DPO-as-a-Service (Plus)', range: '+R$800-2000/mês' },
      { type: 'Consultoria presencial (Premium)', range: '+R$500-1000/mês' },
      { type: 'White-label', range: 'Negociável' }
    ]
  },

  roadmap: {
    phase0: {
      name: 'Validação',
      months: '1-3',
      investment: 90000,
      burn: 30000,
      milestone: '3 LOIs assinados',
      kpis: ['10 conversas qualificadas', '3 LOIs', '1o case draft']
    },
    phase1: {
      name: 'MVP',
      months: '4-6',
      investment: 150000,
      burn: 50000,
      milestone: 'Primeiros 5 clientes',
      kpis: ['MVP funcional', '5 clientes paying', '1o case completo']
    },
    phase2: {
      name: 'PMF',
      months: '7-15',
      investment: 720000,
      burn: 80000,
      milestone: '50 clientes',
      kpis: ['50 clientes paying', 'CAC < R$3K', 'Churn < 10%']
    },
    phase3: {
      name: 'Scale',
      months: '16-24',
      investment: 1350000,
      burn: 150000,
      milestone: '150 clientes',
      kpis: ['150 clientes', 'Unit economics provados', 'Expansão PME iniciada']
    },

    timeline: {
      fase_0: {
        nome: 'Validação',
        periodo: 'Meses 1-2',
        objetivo: 'Validar tese com prospects qualificados e assinar LOIs',
        kpi: ['10 conversas qualificadas', '3 LOIs assinadas', '1o case draft'],
        responsible: 'Camilla + Gislene',
        status: 'in_progress'
      },
      fase_1: {
        nome: 'MVP + Primeiros Clientes',
        periodo: 'Meses 3-6',
        objetivo: 'Desenvolver MVP funcional e conquistar primeiros 5 clientes pagantes',
        kpi: ['MVP funcional', '5 clientes paying', '1o case completo'],
        responsible: 'Time técnico + Sales',
        status: 'pending'
      },
      fase_2: {
        nome: 'Product-Market Fit',
        periodo: 'Meses 7-12',
        objetivo: 'Escalar go-to-market e otimizar unit economics',
        kpi: ['30 clientes paying', 'CAC < R$3K', 'Churn < 10%'],
        responsible: 'Time completo',
        status: 'pending'
      },
      fase_3: {
        nome: 'Scale Municipal',
        periodo: 'Meses 13-18',
        objetivo: 'Expandir base municipal e provar unit economics em escala',
        kpi: ['80 clientes', 'NPS > 50', 'Unit economics positivos'],
        responsible: 'Time completo + Advisors',
        status: 'pending'
      },
      fase_4: {
        nome: 'Expansão PME',
        periodo: 'Meses 19-24',
        objetivo: 'Diversificar para PMEs mantendo core municipal',
        kpi: ['150 clientes total', '20% receita PME', 'ISO 27701 roadmap'],
        responsible: 'Time completo',
        status: 'pending'
      },
      fase_5: {
        nome: 'Série A + White-label',
        periodo: 'Meses 25-36',
        objetivo: 'Preparar para Série A e lançar canal white-label',
        kpi: ['250+ clientes', 'White-label com 3 parceiros', 'ARR R$1.5M+'],
        responsible: 'Leadership + Board',
        status: 'pending'
      }
    },

    milestones: [
      { data: '2026-05-13', evento: 'INPI protocolo', responsible: 'Gislene', critical: true },
      { data: '2026-06-15', evento: 'Primeiras 3 LOIs', responsible: 'Camilla', critical: true },
      { data: '2026-07-01', evento: 'Alpha test interno', responsible: 'Time técnico', critical: false },
      { data: '2026-08-15', evento: 'Alpha test clientes', responsible: 'Time técnico', critical: true },
      { data: '2026-09-30', evento: 'MVP launch', responsible: 'Time técnico', critical: false },
      { data: '2026-11-15', evento: 'PoC piloto 3 prefeituras', responsible: 'Sales + CS', critical: true },
      { data: '2027-01-15', evento: 'First Customer (pago)', responsible: 'Sales', critical: true },
      { data: '2027-06-30', evento: 'ISO 27701 audit', responsible: 'Gislene', critical: false }
    ],

    criticalPath: ['INPI protocolo', 'Alpha test', 'PoC piloto', 'First Customer'],

    sprints: [
      { sprint: 1, periodo: '06-13/05', foco: 'Base juridica + infra', marco: 'INPI protocolo' },
      { sprint: 2, periodo: '13-20/05', foco: 'LOI kit + prospecting', marco: 'LOI kit pronto' },
      { sprint: 3, periodo: '20-27/05', foco: 'Prospect meetings', marco: '5 meetings agendadas' },
      { sprint: 4, periodo: '27/05-03/06', foco: 'LOI closing', marco: '3 LOIs assinadas' }
    ]
  },

  unitEconomics: {
    arpu: 397,
    ltv: 10800,
    cac: 1800,
    paybackMonths: 4,
    ltvCacRatio: 6.0,
    grossMargin: 80,
    churnRate: 8
  },

  scenarios: [
    {
      id: 'conservative',
      name: 'Conservador',
      description: 'Foco em municípios pequenos, pricing de penetração',
      assumptions: {
        marketShare: 0.01,
        pricing: 'penetration',
        salesCycle: 'slow',
        churn: 0.1
      },
      projections: {
        year1: { customers: 15, arr: 144000, cac: 3000 },
        year2: { customers: 40, arr: 384000, cac: 2500 },
        year3: { customers: 80, arr: 768000, cac: 2000 }
      }
    },
    {
      id: 'moderate',
      name: 'Moderado (Base)',
      description: 'Mix municípios pequenos e médios, pricing padrão',
      assumptions: {
        marketShare: 0.02,
        pricing: 'standard',
        salesCycle: 'medium',
        churn: 0.08
      },
      projections: {
        year1: { customers: 30, arr: 288000, cac: 2500 },
        year2: { customers: 80, arr: 768000, cac: 2000 },
        year3: { customers: 150, arr: 1440000, cac: 1800 }
      }
    },
    {
      id: 'aggressive',
      name: 'Agressivo',
      description: 'Foco em municípios médios, pricing premium, expansion PME ano 2',
      assumptions: {
        marketShare: 0.03,
        pricing: 'premium',
        salesCycle: 'fast',
        churn: 0.05
      },
      projections: {
        year1: { customers: 50, arr: 600000, cac: 3500 },
        year2: { customers: 120, arr: 1440000, cac: 2500 },
        year3: { customers: 250, arr: 3000000, cac: 2000 }
      }
    }
  },

  scenarioInteractive: {
    active: 'base',
    sliders: [
      { id: 'lois', label: 'LOIs Assinadas', min: 0, max: 10, value: 3, impact: 'high' },
      { id: 'advisor', label: 'Advisor Municipal', type: 'boolean', value: false, impact: 'high' },
      { id: 'funding', label: 'Funding (R$ mil)', min: 500, max: 2000, value: 960, impact: 'medium' },
      { id: 'churn', label: 'Churn Mensal (%)', min: 1, max: 10, value: 3, step: 0.5, impact: 'high' },
      { id: 'arpu', label: 'ARPU (R$)', min: 200, max: 1500, value: 800, step: 50, impact: 'medium' }
    ],
    cases: {
      bear: { mrr: 'R$ 120K', mrrValue: 120000, customers: 150, month: 30, churn: 0.05 },
      base: { mrr: 'R$ 280K', mrrValue: 280000, customers: 275, month: 30, churn: 0.025 },
      bull: { mrr: 'R$ 550K', mrrValue: 550000, customers: 500, month: 30, churn: 0.015 }
    },
    projections: {
      phase_1: { label: 'MVP (M3-5)', mrr: 'R$ 25K', mrrValue: 25000, customers: 5 },
      phase_2: { label: 'PMF (M6-9)', mrr: 'R$ 150K', mrrValue: 150000, customers: 50 },
      phase_3: { label: 'Scale (M10-14)', mrr: 'R$ 300K', mrrValue: 300000, customers: 150 },
      phase_4: { label: 'Enterprise (M15-20)', mrr: 'R$ 1M', mrrValue: 1000000, customers: 500 },
      break_even: { customers: 350, month: 42 }
    }
  },

  competitiveAnalysis: {
    direct: [
      { name: 'Confidata', focus: 'Enterprise', pricing: 'Alto', dpoIncluded: false, specialization: 'Genérico' },
      { name: 'S traversal', focus: 'Enterprise', pricing: 'Alto', dpoIncluded: false, specialization: 'Genérico' },
      { name: 'LGPDbox', focus: 'PME', pricing: 'Médio', dpoIncluded: false, specialization: 'Genérico' }
    ],
    indirect: [
      { name: 'Escritórios adv', focus: 'Projects', pricing: 'Muito alto', dpoIncluded: true, specialization: 'Alta' },
      { name: 'Big 4', focus: 'Enterprise', pricing: 'Muito alto', dpoIncluded: true, specialization: 'Genérico' }
    ],
    gapAnalysis: {
      municipal: true,
      dpoIncluded: true,
      pricing: null,
      setupSpeed: true,
      dataLocation: true
    }
  },

  priorities: {
    fdcu: {
      top_critical: [
        { rank: 1, name: 'LOIs Assinadas', score: 9.35, vvv: 0.0, status: 'CRITICO - BLOQUEIO' },
        { rank: 2, name: 'Co-Founder/Advisor', score: 9.0, vvv: 0.3, status: 'ALTO RISCO' },
        { rank: 3, name: 'Parecer Jurídico', score: 8.35, vvv: 0.5, status: 'NEEDS_VALIDATION' },
        { rank: 4, name: 'Unit Economics', score: 6.7, vvv: 0.6, status: 'CORRIGIDO' },
        { rank: 5, name: 'Consórcios Map', score: 6.55, vvv: 0.8, status: 'PARCIAL VALIDADO' }
      ]
    }
  },

  validation: {
    low_vvv_items: [
      { item: 'LOIs Assinadas', vvv: 0.0, acao: 'Obter 3+ assinaturas', priority: 'CRITICA' },
      { item: 'Custo Desenvolvimento', vvv: 0.4, acao: 'Camilla orçamento', priority: 'ALTA' },
      { item: 'Advisor Confirmado', vvv: 0.3, acao: 'Contratar co-founder', priority: 'ALTA' },
      { item: 'OSCIP Status', vvv: 0.0, acao: 'Verificar governo federal', priority: 'MEDIA' },
      { item: 'Conversão Real', vvv: 0.0, acao: 'Simone histórico', priority: 'MEDIA' }
    ],
    confidence_badges: {
      swot: 0.82,
      market: 0.78,
      competitive: 0.88,
      financial: 0.65,
      legal: 0.55,
      overall: 0.72
    }
  }
}

export default strategicData
