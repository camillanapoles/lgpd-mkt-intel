// Strategic Data extracted from BUSINESS-PLAN.md
export const strategicData = {
  metadata: {
    version: '1.0.0',
    lastUpdated: '2026-05-08',
    project: 'LGPD SaaS + Consultoria - Contabilizei da Privacy',
    status: 'GO - com pré-condições de validação',
    strategicScore: 7.2
  },

  marketAnalysis: {
    tam: { value: 800000000, label: '$800M-$1.5B', description: 'Brasil RegTech+Legaltech' },
    sam: { value: 60000000, label: 'R$60M/ano', description: 'Prefeituras sem LGPD' },
    som: { value: 1200000, label: 'R$1.2M/ano', description: '5 anos, 2% share' },
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
    }
  },

  unitEconomics: {
    arpu: 800,
    ltv: 28800,
    cac: 2500,
    paybackMonths: 14,
    ltvCacRatio: 11.5,
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
  }
}

export default strategicData
