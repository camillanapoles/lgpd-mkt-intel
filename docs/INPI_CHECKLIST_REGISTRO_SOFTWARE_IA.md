# CHECKLIST: Registro INPI Software IA + Contratação Direta Lei 14.133

## Contexto Específico
- **Software**: Algoritmos LGPD (tarjamento automático LAI/LGPD)
- **Enquadramento**: Decreto Brasil Art. 26 (contratação direta)
- **Prazo**: 6-12 meses (urgente para contratação direta)
- **Validade**: 50 anos (custo único, sem decênio)

---

## PARTE 1: REGISTRO INPI - CHECKLIST PASSO A PASSO

### FASE 1: PREPARAÇÃO (Semana 1-2)

#### 1.1 Cadastro e Acesso
- [ ] Criar conta GOV.BR nível Bronze ou superior
- [ ] Realizar cadastro no Sistema e-INPI
- [ ] Obter certificado digital ICP-Brasil (e-CPF ou e-CNPJ)
- [ ] Verificar acesso ao Sistema e-Software

#### 1.2 Documentação Técnica do Software
- [ ] Preparar código-fonte completo do software
- [ ] Documentar especificações técnicas do sistema
- [ ] Elaborar fluxogramas do funcionamento
- [ ] Descrever funcionalidades de tarjamento automático
- [ ] Mapear algoritmos de detecção de dados sensíveis LGPD
- [ ] Documentar integrações com LAI (Lei de Acesso à Informação)

#### 1.3 Categorização do Software
Para enquadramento correto, identificar:

**Categoria Principal**: Software de Inteligência Artificial
- Subcategoria: Processamento de Linguagem Natural (PLN)
- Aplicação: Tarjamento automático de documentos
- Conformidade: LGPD (Lei 13.709/2018) e LAI (Lei 12.527/2011)

**Elementos Inovadores** (para diferenciação):
- Algoritmos proprietários de detecção de dados pessoais
- Método de tarjamento contextual
- Integração com bases de dados de órgãos públicos

### FASE 2: GERAÇÃO DE HASH (Semana 2)

#### 2.1 Preparação do Arquivo para Hash
- [ ] Compilar todo código-fonte em único arquivo
- [ ] Formatos aceitos: PDF, DOC, TXT, ou ZIP/RAR (para múltiplos arquivos)
- [ ] Garantir que o arquivo contenha:
  - Código-fonte completo
  - Especificações técnicas
  - Fluxogramas
  - Documentação de algoritmos de IA

#### 2.2 Geração do Resumo Digital Hash
- [ ] Escolher algoritmo hash (recomendados):
  - SHA-256 (mais comum)
  - SHA-512
  - MD5 (menos recomendado)

- [ ] Comando para gerar hash (Linux/Mac):
  ```bash
  sha256sum arquivo_codigo_fonte.zip
  ```

- [ ] Comando para gerar hash (Windows PowerShell):
  ```powershell
  Get-FileHash arquivo_codigo_fonte.zip -Algorithm SHA256
  ```

- [ ] Anotar o hash gerado (será inserido no formulário)
- [ ] Fazer backup do arquivo em múltiplos locais
- [ ] Guardar o arquivo de forma segura (responsabilidade do titular)

### FASE 3: PAGAMENTO DA GRU (Semana 2-3)

#### 3.1 Emitir GRU
- [ ] Acessar sistema GRU do INPI
- [ ] Selecionar serviço: "Pedido de Registro de Programa de Computador"
- [ ] Código do serviço: **730**
- [ ] Valor atualizado: **R$ 210,00** (tabela 2025)

#### 3.2 Benefícios Fiscais Aplicáveis
Verificar se elegível para descontos:
- [ ] Pessoa física
- [ ] Microempreendedor Individual (MEI)
- [ ] Microempresa (ME)
- [ ] Empresa de Pequeno Porte (EPP)
- [ ] Instituição de ensino e pesquisa
- [ ] Entidade sem fins lucrativos

#### 3.3 Pagamento
- [ ] Pagar GRU antes de protocolar o pedido
- [ ] **ATENÇÃO**: Agendamento não é aceito
- [ ] Anotar número da GRU paga
- [ ] Guardar comprovante de pagamento

### FASE 4: DECLARAÇÃO DE VERACIDADE (Semana 3)

#### 4.1 Obter Documento DV
- [ ] Baixar Declaração de Veracidade no sistema GRU
- [ ] Ou baixar no formulário e-Software

#### 4.2 Assinatura Digital
- [ ] Assinar DV com certificado digital ICP-Brasil
- [ ] Titular do direito assina com e-CPF ou e-CNPJ
- [ ] Se houver procurador:
  - [ ] Titular assina procuração
  - [ ] Procurador assina DV com e-CPF

### FASE 5: FORMULÁRIO E-SOFTWARE (Semana 3-4)

#### 5.1 Acesso ao Sistema
- [ ] Fazer login no Sistema e-Software
- [ ] Iniciar novo pedido de registro

#### 5.2 Preenchimento do Formulário
**Dados do Titular:**
- [ ] Nome completo ou razão social
- [ ] CPF ou CNPJ
- [ ] Endereço completo
- [ ] Dados de contato

**Dados do Software:**
- [ ] Nome do programa de computador
- [ ] Descrição funcional (máx 2000 caracteres)
- [ ] Especificação do tipo de programa
- [ ] Linguagem de programação utilizada
- [ ] Data de criação/conclusão
- [ ] Número da GRU paga

**Dados Técnicos:**
- [ ] Inserir o resumo digital hash gerado
- [ ] Identificar o algoritmo utilizado (SHA-256, etc.)
- [ ] Fazer upload da Declaração de Veracidade assinada
- [ ] Se houver procurador: fazer upload da procuração assinada

#### 5.3 Descrição Funcional Modelo (para software IA LGPD)

```
Nome: [NOME DO SOFTWARE]

Descrição:
Sistema de inteligência artificial para tarjamento automático de documentos
conforme LGPD e LAI. Utiliza algoritmos proprietários de processamento de
linguagem natural para identificar e ocultar dados pessoais sensíveis em
textos, incluindo: nome, CPF, endereço, email, telefone e outras informações
pessoais regulamentadas pela Lei 13.709/2018 (LGPD) e Lei 12.527/2011 (LAI).

O sistema realiza:
- Detecção automática de dados pessoais e sensíveis
- Classificação contextual de informações
- Tarjamento seletivo baseado em regras de privacidade
- Geração de relatórios de auditoria de dados processados
- Conformidade com Art. 26 do Decreto e normas brasileiras de proteção de dados

Aplicável a órgãos públicos e empresas privadas para atendimento de solicitações
de acesso à informação (LAI) e resposta a titulares de dados (LGPD).
```

### FASE 6: PROTOCOLO E ACOMPANHAMENTO (Semana 4-5)

#### 6.1 Protocolo do Pedido
- [ ] Revisar todas as informações preenchidas
- [ ] Confirmar upload da DV assinada
- [ ] Confirmar número da GRU inserido
- [ ] Submeter o pedido
- [ ] Anotar número do processo gerado

#### 6.2 Acompanhamento
- [ ] Acompanhar pelo Sistema Busca Web
- [ ] Consultar Revista da Propriedade Industrial (RPI) - terças-feiras
- [ ] Cadastrar número do pedido em "Meus Pedidos" para alertas por email

#### 6.3 Prazos
- [ ] Prazo para expedição do certificado: **até 10 dias corridos**
- [ ] Meta atual: **7 dias úteis**
- [ ] Não há mais exigências ou recursos
- [ ] Apenas duas situações: registro concedido ou petição não conhecida

### FASE 7: CERTIFICADO (Semana 5-6)

#### 7.1 Obtenção do Certificado
- [ ] Acessar Sistema Busca Web
- [ ] Localizar processo pelo número
- [ ] Fazer download do certificado eletrônico
- [ ] Verificar todas as informações do certificado

#### 7.2 Após Registro
- [ ] Guardar certificado em local seguro
- [ ] Guardar arquivo com código-fonte usado para hash (prazo: 50 anos)
- [ ] Fazer backup múltiplo do código-fonte
- [ ] Não é necessário pagamento de decênio

---

## PARTE 2: CONTRATAÇÃO DIRETA LEI 14.133

### BASE LEGAL PARA CONTRATAÇÃO DIRETA

#### Decreto Brasil Art. 26 (Enquadramento)

**Hipóteses de Contratação Direta (Dispensa de Licitação):**

1. **Inexigibilidade** (Art. 75, Lei 14.133/2021):
   - Inviabilidade de competição
   - Fornecedor exclusivo
   - Software com características únicas

2. **Dispensa por Valor** (Art. 75, inciso II):
   - Para compras e serviços: até R$ 60.000,00
   - Para obras e engenharia: até R$ 150.000,00

3. **Dispensa por Emergência** (Art. 75, inciso IV):
   - Situação de emergência ou calamidade pública
   - Não há tempo para licitação

4. **Dispensa por Singularidade** (Art. 75, inciso VI):
   - Bens e serviços que só possam ser fornecidos por produtor/empresa exclusiva
   - **ENQUADRAMENTO IDEAL PARA SOFTWARE IA COM REGISTRO INPI**

### DOCUMENTOS PARA CONTRATAÇÃO DIRETA

#### 1. Justificativa Técnica
- [ ] Estudo Técnico Preliminar (ETP)
- [ ] Justificativa da escolha do fornecedor
- [ ] Demonstração de singularidade do software
- [ ] Comprovação de registro INPI (certificado)
- [ ] Parecer jurídico sobre enquadramento legal

#### 2. Documentação do Software
- [ ] Certificado de Registro INPI
- [ ] Memorial descritivo das funcionalidades
- [ ] Documentação técnica dos algoritmos
- [ ] Termo de titularidade e autoria

#### 3. Documentação Orçamentária
- [ ] Pesquisa de preços (mínimo 3 orçamentos, se aplicável)
- [ ] Justificativa de preço quando fornecedor exclusivo
- [ ] Dotação orçamentária disponível
- [ ] Nota de empenho

#### 4. Documentos Administrativos
- [ ] Termo de Referência (TR)
- [ ] Minuta de contrato
- [ ] Mapa de riscos da contratação
- [ ] Plano de suprimento

### MODELO: TERMO DE JUSTIFICATIVA PARA CONTRATAÇÃO DIRETA

```
JUSTIFICATIVA DE CONTRATAÇÃO DIRETA
Lei nº 14.133, de 1º de abril de 2021
Decreto Brasil, Art. 26

1. OBJETO
Contratação de [NOME DA EMPRESA] para fornecimento de software de inteligência
artificial para tarjamento automático de documentos conforme LGPD e LAI.

2. ENQUADRAMENTO LEGAL
Dispensa de licitação com base no Art. 75, inciso VI, da Lei nº 14.133/2021,
que permite a contratação direta quando se tratar de bem ou serviço que só
possa ser fornecido por produtor, empresa ou representante comercial exclusivo.

3. JUSTIFICATIVA DA SINGULARIDADE
O software objeto desta contratação possui características únicas que o
diferenciam de soluções disponíveis no mercado:

a) Algoritmos proprietários de detecção de dados pessoais baseados em
   inteligência artificial, com registro no INPI sob nº [NÚMERO DO REGISTRO];

b) Funcionalidade específica de tarjamento contextual que considera as
   particularidades da legislação brasileira (LGPD e LAI);

c) Integração proprietária com sistemas de gestão documental de órgãos públicos;

d) Métrica de precisão superior a [X]% na detecção de dados sensíveis,
   atestada por [INSTITUIÇÃO/TESTE];

e) Inexistência de software alternativo no mercado nacional que apresente
   conjunto de funcionalidades equivalentes.

4. REGISTRO INPI
O software encontra-se devidamente registrado no Instituto Nacional da
Propriedade Industrial (INPI) sob o nº [NÚMERO DO REGISTRO], conforme
certificado em anexo, o que atesta sua singularidade e propriedade intelectual.

5. PESQUISA DE MERCADO
Foram consultados os seguintes fornecedores/desenvolvedores de software similar:
- [Fornecedor 1]: não atende requisito [X]
- [Fornecedor 2]: não atende requisito [Y]
- [Fornecedor 3]: não atende requisito [Z]

6. VANTAGENS DA CONTRATAÇÃO
a) Conformidade imediata com LGPD e LAI;
b) Redução de [X]% no tempo de processamento de solicitações de acesso à informação;
c) Eliminação de riscos de vazamento de dados pessoais;
d) Economia estimada de R$ [VALOR]/ano em comparação com processo manual;

7. CONCLUSÃO
Face ao exposto, requer-se a autorização para contratação direta, nos termos
do Art. 75, inciso VI, da Lei nº 14.133/2021, visando a aquisição do software
[NOME DO SOFTWARE], de propriedade da empresa [NOME DA EMPRESA], pelo valor
total de R$ [VALOR], conforme Dotação Orçamentária nº [NÚMERO].

[Local], [Data]

_______________________________________
[Nome do Responsável]
[Cargo/Matrícula]
```

---

## PARTE 3: DOCUMENTOS PRONTOS

### DOCUMENTO 1: Declaração de Veracidade (Template)

```declaração
DECLARAÇÃO DE VERACIDADE

Ao Instituto Nacional da Propriedade Industrial - INPI

[Nome Completo ou Razão Social], inscrito(a) no CPF/CNPJ sob o nº
[CPF/CNPJ], declaro, para os devidos fins, sob as penas da lei, que:

1. As informações prestadas no pedido de registro de programa de
   computador sob o nº [NÚMERO DA GRU/PROCESSO] são verdadeiras e
   correspondem à realidade dos fatos;

2. O programa de computador denominado "[NOME DO SOFTWARE]" foi
   desenvolvido por [NOME DO DESENVOLVEDOR/EMPRESA], sendo o
   declarante titular dos direitos patrimoniais sobre o mesmo;

3. O código-fonte apresentado para geração do resumo digital hash
   corresponde integralmente ao programa de computador objeto do
   pedido de registro;

4. O programa de computador não viola direitos de terceiros, incluindo
   direitos autorais, propriedade intelectual ou outros direitos
   protegidos por lei;

5. Estou ciente de que a guarda da documentação técnica (código-fonte)
   é de minha exclusiva responsabilidade, devendo mantê-la íntegra
   pelo prazo de vigência do registro (50 anos);

6. Estou ciente de que o resumo digital hash gerado através do
   algoritmo [ALGORITMO - ex: SHA-256] será inserido no Certificado
   de Registro e servirá como prova da integridade do código-fonte.

Declaro ainda que estou ciente de que qualquer falsidade nas informações
prestadas configurará crime contra a administração pública, nos termos
da legislação penal aplicável.

[Local], [Data]

_______________________________________
Assinatura Digital ICP-Brasil
[Nome do Declarante]
[Cargo/Qualificação - se aplicável]
```

### DOCUMENTO 2: Memorial Descritivo do Software (Template)

```memorial
MEMORIAL DESCRITIVO DO SOFTWARE
[NOME DO SOFTWARE]

1. IDENTIFICAÇÃO
Nome do Programa: [NOME DO SOFTWARE]
Versão: [X.X]
Data de Criação: [DD/MM/AAAA]
Desenvolvedor: [NOME DA EMPRESA/DESENVOLVEDOR]
Titular: [NOME DO TITULAR DOS DIREITOS]

2. FINALIDADE
O software tem como finalidade realizar o tarjamento automático de
documentos de texto, identificando e ocultando informações pessoais
e sensíveis conforme determina a Lei Geral de Proteção de Dados (LGPD -
Lei nº 13.709/2018) e a Lei de Acesso à Informação (LAI - Lei nº 12.527/2011).

3. DESCRIÇÃO FUNCIONAL

3.1. Funcionalidades Principais:
a) Detecção automática de dados pessoais:
   - Nome completo
   - CPF
   - RG
   - Endereço
   - Email
   - Telefone
   - Data de nascimento
   - Outros dados pessoais identificadores

b) Detecção de dados sensíveis (LGPD Art. 5º, inciso II):
   - Origem racial ou étnica
   - Convicção religiosa
   - Opinião política
   - Filiação a sindicato ou organização religiosa
   - Saúde ou vida sexual
   - Biometria

c) Métodos de tarjamento:
   - Substituição por caracteres [XXXX]
   - Substituição por tags descritivas [<NOME>]
   - Remoção completa
   - Mascaramento parcial

d) Geração de relatórios:
   - Log de processamento
   - Estatísticas de detecção
   - Auditoria de dados sensíveis

3.2. Tecnologias Utilizadas:
- Linguagem de programação: [Ex: Python 3.10+]
- Framework de IA: [Ex: TensorFlow, PyTorch]
- Modelo de NLP: [Ex: BERT customizado]
- Formatos suportados: PDF, DOCX, TXT, RTF

4. CARACTERÍSTICAS INOVADORAS
4.1. Algoritmos Proprietários:
- Modelo de detecção de entidades nomeadas treinado especificamente
  para documentos em língua portuguesa do contexto brasileiro
- Sistema de contextualização que determina o nível de tarjamento
  adequado conforme o tipo de documento e finalidade

4.2. Integrações:
- API REST para integração com sistemas externos
- Suporte a processamento em lote
- Compatibilidade com sistemas de gestão documental

5. CONFORMIDADE LEGAL
5.1. LGPD - Lei nº 13.709/2018:
- Atende aos princípios de minimização de dados (Art. 6º)
- Suporta anonimização e pseudonimização (Art. 11, §1º)
- Facilita resposta a direitos dos titulares (Arts. 18-22)

5.2. LAI - Lei nº 12.527/2011:
- Auxilia no cumprimento de prazos de resposta
- Permite atendimento de solicitações de acesso à informação
- Mantém segurança de informações sigilosas

6. ESPECIFICAÇÕES TÉCNICAS
6.1. Requisitos de Sistema:
- Processador: [mínimo recomendado]
- Memória RAM: [mínimo recomendado]
- Espaço em disco: [mínimo recomendado]
- Sistema operacional: [compatíveis]

6.2. Performance:
- Velocidade de processamento: [X] páginas por minuto
- Precisão média de detecção: [X]%
- Tempo médio de resposta via API: [X] milissegundos

7. DIREITOS DE PROPRIEDADE INTELECTUAL
O software é protegido por direitos autorais conforme Lei nº 9.610/1998
e Lei nº 9.609/1998, estando devidamente registrado no INPI sob nº
[NÚMERO DO REGISTRO INPI], com validade por 50 anos.

[Local], [Data]

_______________________________________
[Nome do Responsável]
[Cargo/Qualificação]
```

### DOCUMENTO 3: Termo de Titularidade (Template)

```titularidade
TERMO DE TITULARIDADE E AUTORIA

Pelo presente instrumento, as partes abaixo identificadas:

1. DO DESENVOLVEDOR:
[NOME DO DESENVOLVEDOR/EMPRESA], inscrito(a) no CPF/CNPJ sob o nº
[CPF/CNPJ], com sede em [Endereço Completo], neste ato representado(a)
por [Nome do Representante], doravante denominado DESDENVOLVEDOR;

2. DO TITULAR:
[NOME DO TITULAR], inscrito(a) no CPF/CNPJ sob o nº [CPF/CNPJ],
com sede em [Endereço Completo], neste ato representado(a) por
[Nome do Representante], doravante denominado TITULAR;

Têm justo e contratado o seguinte:

CLÁUSULA PRIMEIRA - DO OBJETO
O presente Termo tem por objeto estabelecer a titularidade e autoria do
programa de computador denominado "[NOME DO SOFTWARE]", versão [X.X],
desenvolvido pelo DESDENVOLVEDOR a pedido e/ou encomenda do TITULAR.

CLÁUSULA SEGUNDA - DA AUTORIA
O DESSENVOLVEDOR declara, expressamente, que é autor do programa de
computador objeto deste Termo, tendo desenvolvido o código-fonte,
estruturas algorítmicas e funcionalidades que compõem o software.

CLÁUSULA TERCEIRA - DA TITULARIDADE
Por força deste instrumento e nos termos da legislação aplicável
(Lei nº 9.609/1998, Art. 4º), o TITULAR é detentor da titularidade
dos direitos patrimoniais sobre o programa de computador, podendo
explorá-lo comercialmente, registrá-lo e exercer todos os direitos
inerentes à condição de titular.

CLÁUSULA QUARTA - DA CESSÃO DE DIREITOS
O DESSENVOLVEDOR cede e transfere, em caráter definitivo, exclusivo e
irrevogável, todos os direitos patrimoniais sobre o software ao TITULAR,
podendo este:
a) Registrar o programa de computador em seu nome junto ao INPI;
b) Explorar comercialmente o software;
c) Licenciar ou sublicenciar o software;
d) Alterar, modificar ou adaptar o software;
e) Exercer todos os demais direitos de titular.

CLÁUSULA QUINTA - DOS DIREITOS MORAIS
Nos termos do Art. 27 da Lei nº 9.610/1998, o DESSENVOLVEDOR mantém os
direitos morais sobre a obra, incluindo o direito de ser identificado como
autor do software, sem prejuízo dos direitos patrimoniais transferidos
ao TITULAR.

CLÁUSULA SEXTA - DA RESPONSABILIDADE
O TITULAR assume inteira responsabilidade pelo uso e exploração do
software, isentando o DESSENVOLVEDOR de qualquer reclamação ou
demanda decorrente de sua utilização.

CLÁUSULA SÉTIMA - DISPOSIÇÕES GERAIS
7.1. O presente Termo entra em vigor na data de sua assinatura;
7.2. As partes elegem o foro de [Cidade/Estado] para dirimir quaisquer
     dúvidas decorrentes deste instrumento;
7.3. Este Termo constitui título hábil para registro do software no INPI.

E por estarem justos e contratados, as partes assinam o presente
instrumento em duas vias de igual teor.

[Local], [Data]

_______________________________________
DESSENVOLVEDOR
[Nome do Desenvolvedor]

_______________________________________
TITULAR
[Nome do Titular]
```

---

## PARTE 4: CUSTOS E PRAZOS

### CUSTOS TOTAIS ESTIMADOS

1. **Registro INPI** (único):
   - Taxa código 730: R$ 210,00
   - Sem descontos: R$ 210,00
   - Com descontos (ME/EPP/MEI): conforme regulamentação

2. **Certificado Digital** (se não possuir):
   - e-CPF (pessoa física): R$ 80,00 - R$ 150,00
   - e-CNPJ (pessoa jurídica): R$ 150,00 - R$ 300,00

3. **Profissionais (opcional)**:
   - Advogado/Contador para registro: R$ 1.000,00 - R$ 3.000,00
   - Consultor em propriedade intelectual: R$ 2.000,00 - R$ 5.000,00

**Custo Total Mínimo**: R$ 210,00 (se já tiver certificado digital e fazer DIY)
**Custo Total Típico**: R$ 1.500,00 - R$ 8.000,00 (com assistência profissional)

### PRAZOS

1. **Registro INPI**:
   - Preparação documental: 2-4 semanas
   - Pagamento GRU: 1-3 dias úteis
   - Protocolo: imediato
   - Expedição do certificado: até 10 dias corridos
   - **Total típico**: 4-6 semanas

2. **Contratação Direta** (após registro):
   - Preparação de documents: 2-4 semanas
   - Análise jurídica: 1-2 semanas
   - Autorização administrativa: 1-4 semanas
   - **Total típico**: 4-10 semanas

**Prazo Total Urgente (6-12 meses)**: totalmente viável mesmo com todas as etapas

---

## PARTE 5: DICAS E RECOMENDAÇÕES

### DURANTE O REGISTRO INPI

1. **Antes de Protocolar**:
   - Verifique se o software está suficientemente finalizado
   - Softwares apenas conceituais não podem ser registrados
   - Prepare versões do software para registro futuro

2. **Geração do Hash**:
   - Use SHA-256 ou superior
   - Faça múltiplos backups do arquivo usado
   - Anote o algoritmo utilizado

3. **Preenchimento do Formulário**:
   - Seja preciso na descrição funcional
   - Destaque características inovadoras
   - Mencione conformidade com legislação brasileira

### PARA CONTRATAÇÃO DIRETA

1. **Enquadramento Legal**:
   - Art. 75, VI é o mais adequado para software proprietário
   - Certificado INPI comprova singularidade
   - Parecer jurídico é essencial

2. **Justificativa**:
   - Enfatize características únicas
   - Demonstre inexistência de alternativas
   - Quantifique benefícios da contratação

3. **Documentação**:
   - Certificado INPI é prova fundamental
   - Memorial descritivo detalhado é essencial
   - Termo de titularidade regulariza direitos

### APÓS O REGISTRO

1. **Manutenção**:
   - Guardar código-fonte por 50 anos
   - Fazer backups regulares
   - Atualizar registro para novas versões

2. **Exploração Comercial**:
   - Usar certificado em materiais de marketing
   - Negociar licenciamento com segurança jurídica
   - Definir cláusulas de confidencialidade em contratos

---

## PARTE 6: REFERÊNCIAS NORMATIVAS

### Legislação Aplicável

1. **Propriedade Intelectual de Software**:
   - Lei nº 9.609/1998 (Lei do Software)
   - Lei nº 9.610/1998 (Lei de Direitos Autorais)
   - Decreto nº 2.556/1998 (Regulamenta registro no INPI)
   - Instrução Normativa INPI nº 099/2019

2. **Proteção de Dados**:
   - Lei nº 13.709/2018 (LGPD)
   - Lei nº 12.527/2011 (LAI)

3. **Licitações Públicas**:
   - Lei nº 14.133/2021 (Nova Lei de Licitações)
   - Decreto [NÚMERO] Art. 26 (Contratação Direta)

### Documentos INPI

1. Manual do Usuário - Programas de Computador
2. Guia Básico - Registro de Software
3. Tabela de Retribuições - Taxas atualizadas

### Canais Oficiais

- INPI: www.gov.br/inpi
- Sistema e-INPI: [URL]
- Sistema e-Software: [URL]
- Compras.gov.br: www.gov.br/compras

---

## CHECKLIST FINAL

### ANTES DE INICIAR
- [ ] Software está finalizado e funcional
- [ ] Tem certificado digital ICP-Brasil
- [ ] Tem conta GOV.BR nível Bronze ou superior
- [ ] Código-fonte está organizado e documentado

### DURANTE O PROCESSO
- [ ] GRU foi paga antes do protocolo
- [ ] Hash foi gerado corretamente
- [ ] DV foi assinada digitalmente
- [ ] Formulário foi preenchido sem erros
- [ ] Número do processo foi anotado

### APÓS O REGISTRO
- [ ] Certificado foi baixado e salvo
- [ ] Backup do código-fonte está seguro
- [ ] Registro está sendo usado em contratações
- [ ] Versões futuras serão registradas

---

**Documento elaborado em**: [DATA]
**Validade**: Até atualização legislativa
**Contato para dúvidas**: [EMAIL/TELEFONE]
