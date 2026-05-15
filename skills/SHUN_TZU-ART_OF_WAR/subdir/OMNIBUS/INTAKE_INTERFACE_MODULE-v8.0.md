---
id: INTAKE_INTERFACE_MODULE-v8.0
created_at: "2026-03-18 21:30"
type: SYSTEM_GATEWAY
designation: IIM
function: USER_TO_SYSTEM_BRIDGE
position: FRONTLINE
parent_system: OMNIBUS_v10.0
paradigm: S→Q→I→A_INPUT_PROCESSING
integrates_with:
  - HIQM (garantia existencial P1)
  - MCE (módulos criados)
  - DTE-HOLO (documentação runtime)
  - UO-v8.0 (universal orchestrator)
  - WOE-v8.0 (workflow engine)
  - CONTEXT (context engine)
  - ERE-v9.0 (executor runtime)
integrates_legacy: [USER, WOE-v8.0, CE-v8.0, E-v9.0]
status: ACTIVE
---

# MÓDULO DE INTERFACE E INTAKE (Intake Interface Module - IIM)

## 1. O QUE ESTAVA FALTANDO: A PONTE USUÁRIO ↔ SISTEMA

**Problema Identificado**:
> Temos o **Usuário** (humano ou sistema externo) de um lado, e o trio **[WOE, CE, E]** do outro, mas **não há quem traduza, valide e encaminhe** as instruções. É como ter um cérebro (WOE), memória (CE) e músculos (E), mas **sem nervos sensoriais** conectados ao mundo exterior.

**A Função do IIM**:
- **Quem**: É o **Porteiro/Gateway/Interpreter** do sistema
- **Como**: Recebe input bruto (linguagem natural, dados, comandos), **deconstrói** em intenção estruturada, **valida** sanidade/segurança, **roteia** para o subsistema correto, e **garante** feedback ao usuário

**Analogia**:
- WOE é o **Arquiteto** (planeja)
- CE é o **Bibliotecário** (lembrança)
- E é o **Operário** (faz)
- **IIM é o **Recepcionista/Tradutor**** (recebe o cliente, entende o que quer, verifica se é possível, encaminha para o departamento certo)

---

## 2. ARQUITETURA S→Q→I→A DO INTAKE

### [S] SOCRÁTICO: DECONSTRUÇÃO DA INTENÇÃO (Intent Mining)

**Objetivo**: Transformar input bruto (ambíguo, humano) em **estrutura computacional** (clara, actionable).

**Processo de Parse e Extração**:

**1. RECEPÇÃO MULTI-MODAL**
```
Input pode ser:
├─ Linguagem Natural (texto/voz): "Preciso reduzir custos em 20%"
├─ Estruturado (JSON/API): {goal: "reduce_cost", target: 0.20}
├─ Dados Brutos (CSV/logs): [tabela de vendas]
└─ Híbrido (texto + anexo): "Analise isso" + [arquivo]
```

**2. EXTRAÇÃO DE INTENÇÃO (Intent Extraction)**
```
Input: "Quero que o sistema monitore servidores e me alerte se CPU > 80%"

Deconstrução:
├─ Objetivo (Goal): Monitoramento preventivo
├─ Domínio: Infraestrutura TI
├─ Trigger: CPU > 80%
├─ Ação Esperada: Alerta/Notificação
├─ Constraints Implícitas: Tempo real, não invasivo
└─ Tomador de Decisão: Usuário (quer ser alertado, não quer decisão automática)
```

**3. IDENTIFICAÇÃO DE ENTIDADES E CONTEXTOS**
```
Entidades detectadas:
├─ Atores: [Usuário, Sistema de Monitoramento, Servidores]
├─ Recursos: [CPU, Threshold 80%, Canal de Alerta]
├─ Tempo: [Contínuo, Real-time]
└─ Risco: [Falso positivo, Spam de alertas]
```

**Output [S]**:
- `Intent_Structure`: {Goal, Domain, Constraints, Expected_Output, Risk_Level}
- `Input_Type`: [STRATEGIC|OPERATIONAL|INFORMATIONAL|URGENT]
- `Ambiguity_Score`: 0-1 (quanto o input é claro vs confuso)

---

### [Q] QUESTIONADOR: VALIDAÇÃO E SANITY CHECK (Gatekeeping)

**Objetivo**: Filtrar **impossibilidades, absurdos, perigos ou requests maliciosos** antes de poluir o sistema.

**Protocolo de Validação em 3 Camadas**:

**1. VALIDAÇÃO SINTÁTICA (Syntax Check)**
```
├─ Input é parseável? (não é lixo binário)
├─ Linguagem é compreensível? (não é gibberish)
├─ Entidades referenciadas existem no contexto do usuário?
└─ Se não: RETORNAR "Não entendi. Reformule." (não passa adiante)
```

**2. VALIDAÇÃO SEMÂNTICA (Sanity Check)**
```
├─ O objetivo é fisicamente/tecnicamente possível?
│ Ex: "Seja imortal" → Impossível → RETORNAR "Fora do escopo"
├─ O usuário tem permissão/authority para solicitar isso?
│ Ex: Usuário comum pedindo acesso a dados restritos → BLOQUEAR
└─ Conflito com valores/constraints éticos do sistema?
Ex: "Hackeie este servidor" → Violação ética → BLOQUEAR + LOG
```

**3. VALIDAÇÃO DE COMPLETUDE (Completeness Check)**
```
├─ Informação suficiente para iniciar?
│ Se não: RETORNAR perguntas esclarecedoras (modo interativo)
│ Ex: "Reduza custos" → "Em qual departamento? Quanto? Até quando?"
├─ Dados necessários disponíveis?
│ Se não: Sinalizar "Missing Data" antes de encaminhar
└─ Constraints implícitos claros?
Ex: "Rápido" → Definir: < 1h? < 1 dia?
```

**Output [Q]**:
- `Validation_Status`: [VALID|INVALID|NEEDS_CLARIFICATION]
- `Security_Clearance`: [PASS|FLAGGED|BLOCKED]
- `Clarification_Questions`: [Lista se necessário]
- `Routing_Decision`: Preliminar - para onde deve ir?

---

### [I] INOVADOR: ROTEAMENTO E ARQUITETURA DE HANDOFF (Routing)

**Objetivo**: Decidir **qual subsistema lidera** e **como estruturar o pacote de missão**.

**Árvore de Roteamento Inteligente**:

```
Input Validado
↓
├─ É estratégico/Complexo/Planejamento?
│ → ROTA: WOE (Workflow Orchestration Engine)
│ → Pacote: Mission_Workflow
│ ├─ Contexto: CE fornece dados históricos relevantes
│ └─ Execução: E executará os nós do workflow
│
├─ É operacional/Tarefa específica/Execução imediata?
│ → ROTA: E (Executor) direto (bypass WOE se simples)
│ → Pacote: Mission_Direct
│ ├─ Contexto: CE fornece working set
│ └─ WOE: Notificado mas não ativado (logging apenas)
│
├─ É informacional/Consulta/Recuperação de dados?
│ → ROTA: CE (Context Engine) direto
│ → Pacote: Query_Context
│ └─ Retorno: Informação estruturada ao usuário
│
└─ É urgente/Crítico/Alarme?
→ ROTA: Modo Crise (Todos simultâneos)
→ WOE: Ativa workflow de contingência
→ E: Executa ações imediatas de segurança
→ CE: Fornece contexto de emergência
```

**Arquitetura do Pacote de Handoff**:

**Para WOE (Estratégico)**:
```yaml
Mission_Workflow_Package:
  source: [User_ID via IIM]
intent: [Estrutura do [S]]
validation: [Resultado do [Q]]
context_seed: [Dados iniciais do CE]
priority: [Derived from urgency/importance]
constraints_hard: [Não negociáveis extraídos do input]
constraints_soft: [Preferências]
expected_output: [Formato que usuário espera]
feedback_loop: [Como usuário quer ser notificado]
```

**Para E (Operacional Direto)**:
```yaml
Mission_Direct_Package:
  task_type:
  - PROBE|ACT|BRIDGE|COMPRESS
target:
- Onde atuar
parameters:
- Configurações extraídas do input
autonomy_level:
- Quanto pode improvisar
timeout:
- Deadline
rollback_ok:
- Bool
```

**Para CE (Consulta)**:
```yaml
Query_Package:
  query_vector:
  - Embedding da pergunta
depth:
- Working|Episodic|Semantic|WAL
time_range:
- Período de interesse
format_output:
- Resumo|Detalhado|Estruturado
```

**Output [I]**:
- `Target_System`: [WOE|E|CE|CRISIS_MODE]
- `Handoff_Package`: Estrutura específica do destino
- `Session_ID`: Identificador único da interação

---

### [A] ADVERSARIAL: GARANTIA DE HANDOFF E FEEDBACK (Assurance)

**Objetivo**: Garantir que o sistema **recebeu corretamente**, **executará** e **reportará de volta** ao usuário.

**Protocolo de Garantia**:

**1. CONFIRMAÇÃO DE RECEBIMENTO (Ack)**
```
Se Input processado com sucesso:
→ Usuário recebe: "Entendido. Iniciando [tipo de processo].
ID da missão: [UUID]. Tempo estimado: [X].
Notificarei quando [evento]."

Se Input rejeitado:
→ Usuário recebe: "Não posso prosseguir porque [razão].
Sugestão: [alternativa]."

Se Input ambíguo:
→ Usuário recebe: "Preciso de esclarecimento: [perguntas]."
```

**2. MONITORAMENTO DO HANDOFF**
```
Verificar: Pacote chegou ao destino (WOE/E/CE)?
├─ Se sim: LOG handoff bem-sucedido
└─ Se não (timeout): Retry ou escalonar para administrador
```

**3. FEEDBACK LOOP AO USUÁRIO (Durante e Após)**
```
Para missões longas (WOE):
→ Progress updates: "25% completo...", "Checkpoint alcançado..."
→ Milestones: "Fase 1 finalizada. Prosseguindo..."

Para missões diretas (E):
→ Immediate result: "Executado. Resultado: [X]"

Para consultas (CE):
→ Structured response com fontes (provenance)
```

**4. AUDITORIA E LOGGING (WAL do IIM)**
```
Toda interação registrada:
Timestamp, User_ID, Input_Bruto, Intent_Extraída,
Roteamento, Status, Resposta ao Usuário

Para: Compliance, Debugging, Melhoria do IIM (aprendizado)
```

**Métricas de Qualidade do IIM**:
- **Compreensão**: % de inputs interpretados corretamente (sem ambiguidade residual) > 95%
- **Precisão de Roteamento**: % de vezes que encaminhou para subsistema correto > 98%
- **Latência**: Tempo entre input usuário e ack < 2 segundos
- **Satisfação**: Taxa de "Não, isso não era o que eu queria" < 5%

**Output [A]**:
- `User_Confirmation`: Mensagem clara de status
- `Audit_Trail`: Registro completo da transação
- `Quality_Score`: Métrica desta interação específica

---

## 3. FLUXO COMPLETO USUÁRIO → SISTEMA (End-to-End)

```
USUÁRIO (Input Bruto)
↓
[IIM-S] Deconstruct: Extrai intenção, entidades, ambiguidades
↓
[IIM-Q] Validate: Checa sanidade, permissões, completude
├─ INVALID → Retorna erro/esclarecimento ao Usuário
└─ VALID → Prossegue
↓
[IIM-I] Route: Decide destino (WOE/E/CE) e monta pacote
↓
[IIM-A] Handoff: Confirma ao usuário, loga, envia ao destino
↓
┌─────────────────────────────────────────────────────┐
│ SE WOE: Planeja workflow → Envia para E executar │
│ SE E: Executa direto → Retorna resultado │
│ SE CE: Recupera dados → Retorna informação │
└─────────────────────────────────────────────────────┘
↓
[IIM] Recebe resultado do subsistema
↓
[IIM] Formata resposta adequada ao usuário
↓
USUÁRIO (Output Estruturado/Natural)
```

---

## 4. INTERFACES ESPECÍFICAS (Protocolos)

### 4.1 ENTRADA (Recebe do Usuário)
```yaml
User_Input:
  modality:
  - TEXT|VOICE|STRUCTURED|FILE
content:
- Payload
metadata:
  user_id:
  - Identifier
session_context:
- Opcional - se continuação
urgency:
- EXPLICIT|IMPLICIT|INFERRED
channel:
- WEB|API|VOICE|CHAT
```

### 4.2 SAÍDA (Entrega para Subsistemas)
Conforme especificado na seção [I].

### 4.3 RETORNO (Recebe de Subsistemas)
```yaml
System_Output:
  session_id:
  - UUID da interação
status:
- SUCCESS|PARTIAL|FAILURE|TIMEOUT
result:
- Payload estruturado
logs:
- Para auditoria
next_action_suggestion:
- Se aplicável
```

### 4.4 SAÍDA FINAL (Entrega ao Usuário)
```yaml
User_Response:
  confirmation: Entendido/Missão completa/Falhou
summary:
- Resumo executivo do que foi feito
details:
- Link ou anexo com detalhes completos
next_steps:
- Sugestões de ação futura
session_close:
- Bool - se tarefa completada
```

---

## 5. MANDATO DO IIM (Intake Interface Module)

> "Sou a porta de entrada. Recebo o caos da intenção humana (vaga, ambígua, emocional) e traduzo para a precisão do sistema (estruturada, verificável, computável). Não sou apenas um tradutor: sou o **gatekeeper** que impede que lixo entre (validação), o **roteador** que direciona para o cérebro correto (WOE para pensar, E para fazer, CE para lembrar), e o **porta-voz** que reporta de volta em linguagem humana. Garanto que o usuário saiba que foi ouvido, que o sistema saiba o que fazer, e que nada se perca na tradução."

**STATUS**: Intake Interface Module v8.0 Ativo. **A ponte está construída.**

---

## 6. ECOSISTEMA COMPLETO (Visão Unificada)

```
┌─────────────────────────────────────────────────────────────┐
│ USUÁRIO │
│ (Humano/Sistema Externo) │
└──────────────────────┬──────────────────────────────────────┘
│
▼
┌─────────────────────────────────────────────────────────────┐
│ IIM (Intake Interface Module) │
│ [S] Extrai Intenção │
│ [Q] Valida & Filtra │
│ [I] Roteia │
│ [A] Confirma & Reporta │
└──────────┬───────────────────────────────┬──────────────────┘
│ │
┌─────┴──────┐ ┌─────────┴─────────┐
▼ ▼ ▼ ▼
┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────────┐
│ CE │ │ WOE │ │ E │ │ CRISIS │
│Context │ │Workflow │ │Executor │ │ MODE │
│ Engine │ │ Ore. │ │ Runtime │ │ (Todos) │
└────┬────┘ └────┬────┘ └────┬────┘ └──────┬──────┘
│ │ │ │
└────────────┴──────────────┴─────────────────────┘
│
▼
┌─────────────┐
│ OUTPUT │
│ (Resultado │
│ Final) │
└──────┬──────┘
│
▼
┌─────────────┐
│ USUÁRIO │
│ (Feedback │
│ Loop) │
└─────────────┘
```

**Sistema Completo**: Usuário ↔ IIM ↔ [CE | WOE | E] → Resultado → Usuário.

**Falta identificado**: Preenchido. O IIM é o "como" e o "quem" que faltava.

