---
id: MODULO-DOCUMENTACAO-TECNICA-v1.0
type: TECHNICAL_WRITING_ARCHITECTURE
alias: MDT / TechWrite-PIER
layers: [0, 0.5, 1, 2, 3, 4]
status: ACTIVE
created: 2026-03-23
paradigm: PIER_ANALYSIS + CHUNKED_COMPOSITION + META_AUDIT
integrates_with: [MIGA, MODULO-PESQUISA-SISTEMATICA]
agnostic_scope: [User_Documentation, Agent_Instructions, Technical_Specs, API_Docs]
---

# MÓDULO DE DOCUMENTAÇÃO TÉCNICA (MDT) v1.0

## Arquitetura PIER + Escrita em Chunks + Avaliação Independente

### LAYER 0 - PRINCÍPIOS EPISTEMOLÓGICOS DA DOCUMENTAÇÃO

#### 0.1 MANDATOS ABSOLUTOS DE ESCRITA TÉCNICA

```
PRIORITY[CRITICAL]:
├─ ENSINAR_A_PESCAR: Documento deve ensinar método, não apenas mostrar resultado
├─ ZERO_HALLUCINATION_FACTUAL: Nenhuma afirmação sem âncora em fonte verificável
├─ VERACIDADE_VETORIAL: Cada claim deve ter vetor de validação [FONTE + DATA + CONFIANÇA]
├─ COESÃO_FRACTAL: Estrutura clara em 3 escalas (macro/seção/parágrafo)
├─ PROGRESSÃO_PEDAGÓGICA: Do conhecido para o desconhecido; do simples ao complexo
├─ AGNOSTICISMO_CONTEXTUAL: Adaptável a qualquer domínio (user/agent/system)
├─ CHUNK_INDEPENDÊNCIA: Cada segmento deve ser autocontido e verificável isoladamente
└─ AUDITORIA_INDEPENDENTE: Avaliador distinto (persona separada) valida antes de entrega
```

#### 0.2 SISTEMA DE TIPOS DOCUMENTAIS EXAUSTIVO (TD-Inventory)

**Taxonomia PIER de Documentos (Contextual-Holística)**

```yaml
Document_Types_Matrix:
  By_Purpose:
    - type: INSTRUCTIONAL
      description: "Ensina como fazer (ensinar a pescar)"
      characteristics: [Step-by-step, Prerequisites, Verification_points]
      examples: [Tutorials, Guides, HOW-TOs]
      metrics: [Completion_rate, Error_rate, Time_to_complete]
      
    - type: REFERENTIAL
      description: "Informação de consulta rápida"
      characteristics: [Searchable, Indexed, Concise_facts]
      examples: [API_Reference, Glossaries, Cheat_sheets]
      metrics: [Lookup_time, Accuracy, Coverage]
      
    - type: CONCEPTUAL
      description: "Explica por que e como funciona"
      characteristics: [Abstraction_layers, Analogies, Visual_models]
      examples: [Architecture_docs, Explanations, Whitepapers]
      metrics: [Comprehension_score, Retention_rate, Concept_clarity]
      
    - type: PROCEDURAL
      description: "Processos operacionais formais"
      characteristics: [Checklists, Decision_trees, SLA_definitions]
      examples: [Runbooks, SOPs, Playbooks]
      metrics: [Compliance_rate, Execution_consistency, Audit_pass_rate]
      
    - type: SPECIFICATION
      description: "Especificações técnicas precisas"
      characteristics: [Unambiguous, Verifiable, Versioned]
      examples: [RFCs, Technical_Specs, Requirements]
      metrics: [Ambiguity_index, Implementability, Test_coverage]

  By_Audience:
    User_Personas:
      - NOVICE: "Primeiro contato; necessita fundamentos"
      - PRACTITIONER: "Uso diário; necessita eficiência"
      - EXPERT: "Casos edge; necessita profundidade"
      - MAINTAINER: "Long-term; necessita contexto histórico"
      
    Agent_Personas:
      - EXECUTOR: "Instruções atômicas (Zero-Cog)"
      - ORCHESTRATOR: "Estratégias e adaptações"
      - AUDITOR: "Validação e conformidade"

  By_Lifecycle:
    - DRAFT: "Em desenvolvimento; sujeito a mudanças"
    - REVIEW: "Sob validação; bloqueado para edições"
    - PUBLISHED: "Autoritativo; versionado semanticamente"
    - DEPRECATED: "Legado; substituído por novo"
    - ARCHIVED: "Histórico; mantido para referência"
```

**Seletor Inteligente de Tipo Documental**

```python
def select_document_type(context_analysis):
    """
    Algoritmo de seleção baseado em critérios mensuráveis
    """
    scoring_matrix = {
        'instructional_weight': 0,
        'referential_weight': 0,
        'conceptual_weight': 0,
        'procedural_weight': 0,
        'specification_weight': 0
    }
    
    ## Critérios de Contexto (INPUT)
    if context_analysis['user_intent'] == 'learn_to_do':
        scoring_matrix['instructional_weight'] += 3
        scoring_matrix['conceptual_weight'] += 1
        
    if context_analysis['user_intent'] == 'lookup_info':
        scoring_matrix['referential_weight'] += 3
        
    if context_analysis['complexity_level'] == 'high':
        scoring_matrix['conceptual_weight'] += 2
        scoring_matrix['specification_weight'] += 1
        
    if context_analysis['compliance_required']:
        scoring_matrix['procedural_weight'] += 3
        
    if context_analysis['implementation_focus']:
        scoring_matrix['specification_weight'] += 2
        scoring_matrix['instructional_weight'] += 1
    
    ## Critérios de Audiência
    audience_modifier = {
        'NOVICE': {'instructional': 1.5, 'conceptual': 1.2},
        'PRACTITIONER': {'referential': 1.5, 'procedural': 1.3},
        'EXPERT': {'specification': 1.4, 'conceptual': 1.1},
        'EXECUTOR_ZERO_COG': {'procedural': 2.0, 'instructional': 0.5}
    }
    
    selected_type = max(scoring_matrix, key=scoring_matrix.get)
    confidence = scoring_matrix[selected_type] / sum(scoring_matrix.values())
    
    return {
        'selected_type': selected_type.replace('_weight', ''),
        'confidence_score': confidence,
        'hybrid_recommendation': confidence < 0.6,  ## Se baixa confiança, sugerir híbrido
        'rationale': generate_selection_rationale(scoring_matrix)
    }
```
---

### LAYER 0.5 - MOTOR PIER DE ANÁLISE DOCUMENTAL

**0.5.1 Framework PIER (Purpose, Information, Execution, Review)**

#### [P] PURPOSE - Arqueologia da Intenção Documental

**Objetivo**: Escavar o propósito real do documento além do solicitado superficialmente.

```yaml
Purpose_Excavation:
  Surface_Level: "O que o usuário pediu explicitamente"
  Operational_Level: "O que precisa ser documentado para execução"
  Strategic_Level: "Por que este documento existe no ecossistema maior"
  Pedagogical_Level: "Como este documento ensina a pescar (metacognição)"
  
  Validation_Checks:
    - Does_it_teach_to_fish: "Leitor sai apto a replicar ou apenas a seguir?"
    - Scope_Boundaries: "O que está IN vs O que está OUT (explicitado)"
    - Success_Criteria: "Como saber se o documento cumpriu seu propósito"
    - Failure_Modes: "O que acontece se o documento for mal interpretado"
```
#### [I] INFORMATION - Mapeamento Ontológico do Conhecimento

**Objetivo**: Inventariar todo o conhecimento necessário de forma exaustiva.

```yaml
Information_Taxonomy:
  Primary_Sources:
    - category: AUTHORITATIVE
      examples: [Official_docs, RFCs, Academic_papers, Source_code]
      validation: "Verificável via checksum ou citação direta"
      recency_weight: 1.0  ## 2026 = 1.0, 2025 = 0.5, <2025 = 0.2
      
  Secondary_Sources:
    - category: ANALYTICAL
      examples: [Technical_blogs, Case_studies, Benchmarks]
      validation: "Cross-reference com primária"
      recency_weight: 0.8
      
  Tertiary_Sources:
    - category: CONTEXTUAL
      examples: [Forums, Comments, Experience_reports]
      validation: "Usar como indicador de problemas comuns, não como verdade"
      recency_weight: 0.4

  Source_Validation_Matrix:
    VVV:  ## Veracity, Validity, Verification
      Veracity: "Conteúdo corresponde à realidade?"
      Validity: "Fonte é legítima e não foi comprometida?"
      Verification: "Posso confirmar independentemente?"
      
    Inclusion_Criteria:
      - Must_be_verifiable: "Posso apontar para URL/commit/paper?"
      - Must_be_relevant: "Data > 2026 OU fundamental estável (matemática)"
      - Must_be_accessible: "Leitor pode acessar (não paywall intransponível)"
      
    Exclusion_Criteria:
      - Deprecated: "Versão substituída por nova (sem compatibilidade)"
      - Unverified_claims: "Sem evidência empírica"
      - SEO_farms: "Conteúdo gerado para ranking, não para valor"
      - Circular_references: "Fonte A cita B que cita A"
```
#### [E] EXECUTION - Arquitetura de Escrita em Chunks

**Objetivo**: Produção incremental onde cada chunk é independente e verificável.

```yaml
Chunk_Architecture:
  Chunk_Size:
    Optimal: "300-500 tokens ou 1 conceito completo"
    Maximum: "800 tokens (limite de coesão)"
    Minimum: "50 tokens (fragmento mínimo significativo)"
    
  Chunk_Types:
    DEFINITION: "Conceito novo sendo introduzido"
    PROCEDURE: "Passo executável"
    VALIDATION: "Como verificar se funcionou"
    CONTEXT: "Por que isso importa"
    EXAMPLE: "Ilustração concreta"
    EXCEPTION: "Caso edge ou erro comum"
    
  Chunk_Independence_Rule: |
    Cada chunk deve ser compreensível sem ler o documento inteiro.
    Chunk deve ter: Context_setup, Core_content, Next_pointer.
    
  Chunk_Refactoring: |
    Chunks podem ser reordenados, removidos ou adicionados
    sem quebrar o documento (navigability graph).
    
  Progressive_Disclosure: |
    Nível 1 (Scan): Headers + Summaries (10% do conteúdo)
    Nível 2 (Read): Chunks principais (60% do conteúdo)
    Nível 3 (Study): Chunks profundos + Referências (30% do conteúdo)

Writing_Workflow:
  Phase_1: Chunk_Outline
    - Mapear todos os chunks necessários (índice preliminar)
    - Definir dependências entre chunks (DAG interno)
    - Marcar chunks críticos vs opcionais
    
  Phase_2: Chunk_Drafting
    - Escrever chunks independentemente
    - Não editar durante drafting (modo flow)
    - Marcar [DRAFT] em chunks não revisados
    
  Phase_3: Chunk_Integration
    - Verificar transições entre chunks
    - Adicionar cross-references
    - Validar coesão global
    
  Phase_4: Chunk_Optimization
    - Refatorar chunks longos (>800 tokens)
    - Combinar chunks curtos demais (<50 tokens)
    - Balancear profundidade
```
#### [R] REVIEW - Sistema de Avaliação Holística

**Objetivo**: Verificação multidimensional da qualidade documental.

```yaml
Holistic_Review_Criteria:
  Content_Quality:
    - Accuracy: "Fatos estão corretos?"
    - Completeness: "Nada essencial está faltando?"
    - Relevance: "Tudo presente é necessário?"
    - Currency: "Informação é atual (2026 > 2025)?"
    
  Structural_Quality:
    - Architecture: "Organização lógica clara?"
    - Navigation: "Leitor encontra o que precisa?"
    - Hierarchy: "Níveis de heading apropriados?"
    - Chunking: "Segmentação favorece compreensão?"
    
  Linguistic_Quality:
    - Orthography: "Sem erros ortográficos/gramaticais"
    - Style: "Tom apropriado à audiência"
    - Clarity: "Uma interpretação possível (não ambíguo)"
    - Conciseness: "Sem redundância"
    
  Pedagogical_Quality:
    - Progression: "Do básico ao avançado?"
    - Examples: "Ilustrações suficientes e claras?"
    - Practice: "Oportunidades para aplicar?"
    - Teach_to_fish: "Metodologia transferível?"
    
  Technical_Quality:
    - Code_quality: "Se há código, é executável?"
    - Versioning: "Versões de ferramentas especificadas?"
    - Compatibility: "Ambiente de execução definido?"
    - Maintainability: "Fácil atualizar quando mudar?"
```
---

### LAYER 1 - ARQUITETURA DE TEMPLATES E FORMATOS

#### 1.1 Sistema de Templates LaTeX/MD Agnóstico

```latex
% Template Base PIER-LaTeX
\documentclass[technical]{pier-doc}
% ou \documentclass[instructional]{pier-doc}
% ou \documentclass[referential]{pier-doc}

% Metadados PIER
\pierMetadata{
  docId={UUID},
  version={SemVer},
  type={INSTRUCTIONAL|REFERENTIAL|CONCEPTUAL|PROCEDURAL|SPECIFICATION},
  audience={NOVICE|PRACTITIONER|EXPERT|EXECUTOR},
  status={DRAFT|REVIEW|PUBLISHED},
  validationDate={YYYY-MM-DD},
  auditorId={UUID_AVALIADOR},
  sourceHash={SHA256_SOURCES}
}

\begin{document}

\pierHeader{
  title={Título do Documento},
  subtitle={Subtítulo Descritivo},
  context={Contexto de Aplicação},
  prerequisites={[Lista de pré-requisitos]}
}

% Navegação de Progressão
\pierProgression{
  \level{Scan}{Resumo Executivo + Índice}
  \level{Read}{Corpo Principal em Chunks}
  \level{Study}{Apêndices + Referências}
}

% Chunks Documentais
\begin{pierChunk}[chunkId=001, type=DEFINITION, depends={}]
  \chunkHeader{Conceito Fundamental}
  \chunkContent{...}
  \chunkValidation{Como verificar compreensão...}
\end{pierChunk}

\begin{pierChunk}[chunkId=002, type=PROCEDURE, depends={001}]
  \chunkHeader{Execução Passo-a-Passo}
  \chunkContent{...}
  \chunkCheckpoint{Verificação intermediária...}
\end{pierChunk}

% Referências VVV (Veracity, Validity, Verification)
\begin{pierSources}
  \source[primary]{url}{date}{confidence}{description}
  \source[secondary]{url}{date}{confidence}{description}
\end{pierSources}

\end{document}
```

#### 1.2 Validação de Escrita por Critérios Mensuráveis

```python
class DocumentQualityMetrics:
    """
    Métricas objetivas para avaliação de documentos técnicos
    """
    
    def __init__(self, document_chunks):
        self.chunks = document_chunks
        self.scores = {}
        
    def measure_coesion(self):
        """
        Índice de coesão textual (fluxo entre chunks)
        """
        transitions = 0
        smooth_transitions = 0
        
        for i in range(len(self.chunks) - 1):
            transitions += 1
            if self.has_logical_bridge(self.chunks[i], self.chunks[i+1]):
                smooth_transitions += 1
                
        return smooth_transitions / transitions if transitions > 0 else 0
    
    def measure_originality(self):
        """
        Detecção de plágio via análise de similaridade
        """
        ## Implementar análise de shingles ou similar
        ## Retornar índice de originalidade (0-1)
        pass
    
    def measure_veracity_coverage(self):
        """
        % de afirmações com fonte verificável
        """
        total_claims = self.extract_claims()
        sourced_claims = [c for c in total_claims if c.has_source()]
        return len(sourced_claims) / len(total_claims)
    
    def measure_pedagogical_progression(self):
        """
        Complexidade crescente ao longo do documento
        """
        complexity_scores = [c.complexity_level for c in self.chunks]
        ## Verificar se é monotonicamente crescente ou tem picos justificados
        return self.calculate_progression_score(complexity_scores)
    
    def calculate_overall_score(self):
        weights = {
            'coesion': 0.15,
            'originality': 0.20,
            'veracity': 0.25,
            'pedagogical': 0.20,
            'technical': 0.20
        }
        
        total = sum(self.scores[k] * weights[k] for k in weights)
        return {
            'total': total,
            'threshold': 0.90,
            'passed': total >= 0.90,
            'breakdown': self.scores
        }
```

---

### LAYER 2 - SISTEMA DE AVALIAÇÃO INDEPENDENTE (META-AUDITOR)


#### 2.1 Persona do Avaliador Independente

```yaml
Persona_Avaliador_Independente:
  Identity: "Auditor_Técnico_Documental_v1.0"
  Role: "Red_Team_Documental"
  Independence: "Não participou da escrita; sem viés de confirmação"
  
  Mandate: |
    "Sou o olhar crítico que não escreveu o documento.
    Minha única lealdade é à verdade técnica e à clareza.
    Não tenho apego ao texto; posso sugerir deleção total se necessário.
    Busco falhas que o autor não viu por estar próximo demais."
    
  Bias_Neutralization:
    - Sunk_Cost: "Ignorar tempo investido na escrita"
    - Authority: "Não aceitar como verdade por estar escrito"
    - Confirmation: "Buscar evidências contrárias às claims"
    - Novelty: "Não valorizar apenas porque é novo"
    
  Evaluation_Dimensions:
    Factual_Accuracy: "Cada fato verificado contra fontes primárias"
    Logical_Coherence: "Argumentos válidos; sem falácias"
    Completeness: "Nada essencial omitido"
    Clarity: "Uma interpretação possível"
    Utility: "Leitor consegue aplicar o que leu"
    Maintainability: "Documento envelhece bem"
```
#### 2.2 Protocolo de Auditoria em 3 Fases

**Fase 1: Auditoria de Conteúdo (What)**

```python
def audit_content(document):
    """
    Verificação factual e de veracidade
    """
    findings = []
    
    ## 1.1 Verificação de Fontes (VVV)
    for claim in document.extract_factual_claims():
        if not claim.source:
            findings.append({
                'severity': 'CRITICAL',
                'type': 'UNSOURCED_CLAIM',
                'location': claim.location,
                'recommendation': 'Adicionar fonte primária ou marcar como [OPINION]'
            })
        elif claim.source.date < '2026-01-01' and not claim.source.is_fundamental:
            findings.append({
                'severity': 'WARNING',
                'type': 'LEGACY_SOURCE',
                'location': claim.location,
                'recommendation': 'Buscar atualização 2026 ou adicionar [LEGACY]'
            })
    
    ## 1.2 Verificação de Código/Comandos (se aplicável)
    for code_block in document.code_blocks:
        if not code_block.tested:
            findings.append({
                'severity': 'HIGH',
                'type': 'UNTESTED_CODE',
                'recommendation': 'Testar em ambiente limpo ou marcar como [UNTESTED]'
            })
    
    ## 1.3 Verificação de Plágio
    similarity_score = check_similarity_external(code_block.content)
    if similarity_score > 0.3:  ## 30% similaridade
        findings.append({
            'severity': 'CRITICAL',
            'type': 'PLAGIARISM_RISK',
            'similarity': similarity_score,
            'recommendation': 'Reescrever ou citar apropriadamente'
        })
    
    return findings
```

**Fase 2: Auditoria Estrutural (How)**

```python
def audit_structure(document):
    """
    Verificação de organização e coesão
    """
    findings = []
    
    ## 2.1 Arquitetura de Informação
    if document.depth > 4:
        findings.append({
            'severity': 'MEDIUM',
            'type': 'DEEP_HIERARCHY',
            'message': 'Nesting > 4 níveis dificulta navegação',
            'recommendation': 'Achatar estrutura ou dividir em documentos'
        })
    
    ## 2.2 Chunk Balance
    chunk_sizes = [len(chunk) for chunk in document.chunks]
    if max(chunk_sizes) > 800:
        findings.append({
            'severity': 'MEDIUM',
            'type': 'CHUNK_TOO_LONG',
            'location': max(chunk_sizes).location,
            'recommendation': 'Dividir em 2+ chunks'
        })
    
    ## 2.3 Orfãos e Janelas (Chunks sem conexão)
    for chunk in document.chunks:
        if not chunk.has_incoming_ref and chunk.id != '001':
            findings.append({
                'severity': 'LOW',
                'type': 'ORPHAN_CHUNK',
                'chunk': chunk.id,
                'recommendation': 'Adicionar transição do chunk anterior'
            })
    
    ## 2.4 Coerência Global
    coherence_score = calculate_semantic_coherence(document.chunks)
    if coherence_score < 0.85:
        findings.append({
            'severity': 'HIGH',
            'type': 'LOW_COHERENCE',
            'score': coherence_score,
            'recommendation': 'Revisar fluxo lógico entre seções'
        })
    
    return findings
```

**Fase 3: Auditoria Pedagógica (Why)**

```python
def audit_pedagogy(document):
    """
    Verificação se documento ensina a pescar
    """
    findings = []
    
    ## 3.1 Presença de Metodologia
    if not document.contains_methodology_transfer():
        findings.append({
            'severity': 'HIGH',
            'type': 'NO_TEACHING_METHOD',
            'message': 'Documento mostra peixe mas não ensina a pescar',
            'recommendation': 'Adicionar seção "Por que funciona" ou "Como adaptar"'
        })
    
    ## 3.2 Progressão de Complexidade
    complexity_curve = extract_complexity_curve(document)
    if not is_monotonically_increasing(complexity_curve):
        findings.append({
            'severity': 'MEDIUM',
            'type': 'ERRATIC_PROGRESSION',
            'recommendation': 'Reordenar chunks por dificuldade crescente'
        })
    
    ## 3.3 Checkpoints de Validação
    validation_chunks = [c for c in document.chunks if c.type == 'VALIDATION']
    procedure_chunks = [c for c in document.chunks if c.type == 'PROCEDURE']
    
    if len(validation_chunks) < len(procedure_chunks) * 0.5:
        findings.append({
            'severity': 'MEDIUM',
            'type': 'INSUFFICIENT_VALIDATION',
            'recommendation': 'Adicionar mais "Como verificar se funcionou"'
        })
    
    ## 3.4 Contextualização
    if not document.has_context_section():
        findings.append({
            'severity': 'LOW',
            'type': 'MISSING_CONTEXT',
            'recommendation': 'Adicionar "Quando usar isto" e "Quando NÃO usar"'
        })
    
    return findings
```

#### 2.3 Relatório de Auditoria e Certificação

```yaml
Audit_Report_Template:
  Header:
    audit_id: UUID
    document_id: UUID
    auditor_version: "Auditor_Técnico_v1.0"
    audit_date: 2026-03-23
    independence_declaration: "Auditor não participou da redação"
    
  Executive_Summary:
    overall_score: 0.94  ## 0-1
    status: [APPROVED|CONDITIONAL|REJECTED]
    critical_issues: 0
    warnings: 3
    suggestions: 5
    
  Detailed_Findings:
    - category: "Content"
      findings: [...]
    - category: "Structure"
      findings: [...]
    - category: "Pedagogy"
      findings: [...]
      
  Action_Items:
    blocking: []  ## Deve resolver antes de publicar
    recommended: []  ## Deve resolver se possível
    optional: []  ## Nice to have
    
  Certification:
    stamp: "AUDITED_INDEPENDENTLY"
    valid_until: "2026-06-23"  ## 3 meses ou até próxima versão major
    auditor_hash: SHA256(auditor_identity + audit_date)
```

---

### LAYER 3 - INTEGRAÇÃO COM MIGA E SISTEMA DE PROJETOS

#### 3.1 MDT como Sub-processo do MIGA

```yaml
Integration_MIGA_MDT:
  
  Trigger: |
    MIGA[S1] detecta que entregável é documento técnico
    → Instancia MDT como capability especializada
    
  Handoff_MIGA_to_MDT:
    input:
      project_context: "Contexto do projeto pai"
      document_requirements: "Especificação do que documentar"
      audience_profile: "NOVICE|PRACTITIONER|EXPERT|EXECUTOR"
      constraints: "Tempo, formato, tamanho máximo"
      
    output_expected:
      document_type: "Selecionado via algoritmo PIER"
      chunk_structure: "Esqueleto de chunks"
      quality_threshold: "Mínimo aceitável (default: 0.90)"
      
  Execution_Flow:
    MIGA[S3.1]: "Ativar MDT-PIER Analysis"
      → MDT executa [P]urpose, [I]nformation mapping
      → Retorna para MIGA: DocType selecionado + InfoMap
      
    MIGA[S3.2]: "Ativar MDT-Writing"
      → MDT executa Chunk_Outline + Chunk_Drafting
      → Produção incremental (chunk por chunk)
      
    MIGA[S3.3]: "Ativar MDT-Auditor"
      → Auditor Independente avalia
      → Se FAILED → Retorna para MDT-Refactoring
      → Se PASSED → Prossegue
      
    MIGA[S3.4]: "Finalização"
      → MDT gera output final (LaTeX/Markdown)
      → MIGA valida contra requisitos originais
      
  Feedback_Loop:
    MIGA[S4] detecta qualidade insuficiente
    → Replaneja: "Adicionar mais chunks de EXEMPLO"
    → MDT reexecuta S3.2 com novo escopo
```
#### 3.2 Integração com Módulo de Pesquisa

```yaml
MDT_Pesquisa_Integration:
  
  When_Information_Gap_Detected:
    MDT[I] phase: "Mapear informação necessária"
    → Identifica claims que precisam de fonte
    
    Delegation: |
      MDT invoca MODULO-PESQUISA-SISTEMATICA
      → Pesquisa executa [S,Q,I,A] nas fontes
      → Retorna: Sources validadas + Quality scores
      
    Integration: |
      MDT incorpora sources no Information_Taxonomy
      → Marca cada claim com [^N^] citação
      → Adiciona bloco Sources_VVV
      
  Recency_Enforcement: |
    MDT automaticamente prioriza:
    - Fontes 2026: peso 1.0
    - Fontes 2025: peso 0.5 + [LEGACY] flag
    - Fontes < 2025: peso 0.2 ou rejeição (exceto fundamentos)
    
    Auditor verifica: "Toda informação volátil é 2026?"
```
---

## CHECKLIST DE PRODUÇÃO DOCUMENTAL

### Pre-Escrita (S1)
- Propósito documental escavado (PIER-[P])
- Tipo documental selecionado via critérios mensuráveis
- Audiência definida (persona clara)
- Information Taxonomy completa (o que precisa ser dito)
- Fontes primárias identificadas e validadas (VVV)

### Durante Escrita (S3)
- Outline de chunks aprovado
- Cada chunk escrito independentemente
- Chunks marcados [DRAFT] ou [REVIEWED]
- Cross-references entre chunks adicionadas
- Progressão pedagógica verificada (básico → avançado)

### Pós-Escrita (S4)
- Auditor Independente ativado
- Factual accuracy: 100% das claims verificadas
- Originality: Índice de plágio < 5%
- Coesão: Transições suaves entre chunks
- Veracidade: Fontes 2026 quando aplicável
- "Ensinar a pescar": Metodologia explicitada

### Entrega (S5)
- Template LaTeX/Markdown aplicado
- Metadata completa (docId, version, auditor)
- WAL atualizado com estado do documento
- Handoff para MIGA com relatório de qualidade
