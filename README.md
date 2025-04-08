# Monitor de Documentos - Grupo Petrópolis

Este script monitora o site do escritório Zveiter para novos documentos relacionados ao processo de recuperação judicial do Grupo Petrópolis e envia notificações por email quando novos documentos são encontrados.

## Para Analistas de Equity Research

Este monitor foi desenvolvido especificamente para auxiliar analistas de equity research a acompanhar o processo de recuperação judicial do Grupo Petrópolis. Ele oferece várias vantagens:

### Acompanhamento Automático
- 🔄 Verificação automática a cada hora, eliminando a necessidade de checar o site manualmente
- ⏰ Notificações imediatas quando novos documentos são publicados
- 📊 Histórico completo de todos os documentos já encontrados

### Documentos Relevantes para Análise
- 📈 **Relatórios Mensais (RMA)**: Acompanhe a evolução financeira e operacional da empresa
- ⚖️ **Decisões Judiciais**: Monitore desenvolvimentos importantes no processo judicial
- 📑 **Outros Documentos**: Receba atualizações sobre comunicados e informações adicionais

### Benefícios para Análise
- 🎯 Economia de tempo ao automatizar a coleta de informações
- 📱 Acesso rápido aos documentos através de links diretos nos emails
- 📝 Títulos formatados para fácil identificação do conteúdo
- 🔍 Evita perder documentos importantes para a análise

### Integração com Fluxo de Trabalho
- 📧 Notificações por email se integram ao fluxo de trabalho existente
- 📂 Histórico de documentos facilita a organização de referências
- 🔗 Links diretos permitem acesso rápido aos documentos originais

### Exemplos de Uso para Analistas

#### Análise Financeira
- **Acompanhamento de Indicadores**: Use os RMAs para acompanhar a evolução de indicadores financeiros como EBITDA, receita líquida e fluxo de caixa
- **Comparação Período a Período**: Compare os dados do RMA atual com os anteriores para identificar tendências
- **Projeções de Recuperação**: Utilize os dados financeiros para ajustar suas projeções de recuperação da empresa

#### Análise Jurídica
- **Avaliação de Riscos**: Monitore decisões judiciais para avaliar riscos legais e seu impacto no processo de recuperação
- **Timeline do Processo**: Mantenha um cronograma atualizado com base nas decisões judiciais publicadas
- **Identificação de Eventos Críticos**: Identifique rapidamente eventos críticos como homologações de planos ou mudanças de administradores

#### Relatórios e Apresentações
- **Atualização de Relatórios**: Atualize seus relatórios de análise com as informações mais recentes dos documentos
- **Apresentações para Clientes**: Prepare apresentações com dados atualizados sobre o processo de recuperação
- **Notas de Investimento**: Elabore notas de investimento com base nas informações mais recentes

#### Monitoramento de Oportunidades
- **Identificação de Catalisadores**: Identifique potenciais catalisadores de preço com base em decisões judiciais
- **Avaliação de Timing**: Avalie o timing de entrada e saída de posições com base no progresso do processo
- **Comparação com Peers**: Compare o progresso da recuperação judicial com outras empresas em situação similar

## Funcionalidades

- ✅ Monitoramento automático do site do Grupo Petrópolis
- 📧 Notificações por email com design moderno e responsivo
- 🔍 Detecção inteligente de novos documentos
- 📝 Histórico de documentos para evitar duplicatas
- 🎯 Links diretos para download dos PDFs
- 🕒 Verificação automática a cada hora
- 📋 Formatação inteligente de títulos de documentos

## Tipos de Documentos

O monitor identifica e formata automaticamente os seguintes tipos de documentos:

### Relatórios Mensais (RMA)
- Formato: "Xº Relatório Mensal de Atividades (RMA)"
- Exemplo: "12º Relatório Mensal de Atividades (RMA)"
- Identificação: Detectado através do padrão "RMA" no nome do arquivo
- Número do RMA: Extraído do nome do arquivo (ex: "RMA12.pdf" → "12º RMA")

### Decisões Judiciais
- Formato: "Decisão de DD/MM/YYYY - Descrição"
- Exemplo: "Decisão de 12/12/2023 - Homologação Proposta Alienação UPI"
- Identificação: Detectado através do padrão "Decisao" no nome do arquivo
- Data: Extraída do nome do arquivo (ex: "Decisao12122023.pdf" → "12/12/2023")
- Descrição: Extraída do conteúdo do documento ou nome do arquivo

### Outros Documentos
- Formato: Nome do arquivo original
- Exemplo: "Comunicado_Recuperacao_Judicial.pdf"
- Identificação: Qualquer documento que não se encaixe nos padrões acima

## Configuração

1. Clone o repositório:
```bash
git clone [url-do-repositorio]
cd petropolis
```

2. Crie e ative um ambiente virtual:
```bash
python3 -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente:
```bash
cp .env.example .env
```

5. Edite o arquivo `.env` com suas configurações:
```
SMTP_SERVER=seu.servidor.smtp.com
SMTP_PORT=465
EMAIL_USER=seu.email@dominio.com
EMAIL_PASSWORD=sua-senha
NOTIFICATION_EMAIL=email.para.notificacoes@dominio.com
```

## Uso

### Execução Manual

Para verificar novos documentos manualmente:
```bash
python monitor.py
```

### Execução Automática

O script verifica automaticamente novos documentos a cada hora. Para iniciar o monitoramento contínuo:
```bash
python monitor.py
```

### Agendamento Automático

Para executar automaticamente, você pode usar o cron (Linux/Mac) ou Agendador de Tarefas (Windows).

#### Usando Cron (Linux/Mac)

1. Abra o editor cron:
```bash
crontab -e
```

2. Adicione uma linha para executar o script (exemplo: a cada hora):
```bash
0 * * * * cd /caminho/para/petropolis && /caminho/para/petropolis/venv/bin/python monitor.py >> /caminho/para/petropolis/monitor.log 2>&1
```

#### Usando o Agendador de Tarefas (Windows)

1. Abra o Agendador de Tarefas
2. Crie uma nova tarefa
3. Configure para executar `python monitor.py` no diretório do projeto
4. Defina a frequência para a cada hora

## Formato do Email

O script envia emails com:
- 📋 Lista organizada de novos documentos
- 🔗 Botões de acesso direto aos PDFs
- 📅 Data e hora de descoberta de cada documento
- 🎨 Design moderno e responsivo
- 📝 Títulos formatados de acordo com o tipo de documento

### Exemplo de Email
```
Novos Documentos Encontrados (19)

📄 12º Relatório Mensal de Atividades (RMA)
   Data: 2024-02-14 15:30:45
   Link: https://exemplo.com/RMA12.pdf

📄 Decisão de 12/12/2023 - Homologação Proposta Alienação UPI
   Data: 2024-02-14 15:30:45
   Link: https://exemplo.com/Decisao12122023.pdf
```

## Estrutura do Projeto

```
petropolis/
├── monitor.py          # Script principal
├── requirements.txt    # Dependências do projeto
├── .env.example       # Exemplo de configuração
├── .env               # Configurações reais (não versionado)
└── document_history.json  # Histórico de documentos (gerado automaticamente)
```

## Arquitetura do Código

### Estrutura do Script Principal (monitor.py)

O script é organizado em funções modulares, cada uma com uma responsabilidade específica:

1. **Configuração e Inicialização**
   - `load_env()`: Carrega variáveis de ambiente do arquivo `.env`
   - `load_history()`: Carrega o histórico de documentos do arquivo JSON
   - `save_history()`: Salva o histórico atualizado no arquivo JSON

2. **Monitoramento e Coleta**
   - `get_documents()`: Função principal que:
     - Acessa o site do escritório
     - Extrai links de documentos
     - Identifica o tipo de cada documento
     - Formata os títulos de acordo com o tipo
     - Retorna lista de documentos encontrados

3. **Processamento de Documentos**
   - `extract_rma_info()`: Extrai número do RMA do nome do arquivo
   - `extract_decision_info()`: Extrai data e descrição de decisões
   - `format_title()`: Formata o título de acordo com o tipo do documento

4. **Notificação por Email**
   - `send_email()`: Envia email com os novos documentos
   - `create_email_content()`: Gera o conteúdo HTML do email
   - `create_email_button()`: Cria botões de acesso aos PDFs

### Design Decisions

1. **Modularidade**
   - Funções pequenas e focadas
   - Fácil manutenção e teste
   - Separação clara de responsabilidades

2. **Tratamento de Erros**
   - Try/except em operações críticas
   - Logs detalhados para debugging
   - Continuação do script mesmo com erros parciais

3. **Formatação de Títulos**
   - Lógica específica para cada tipo de documento
   - Extração de informações do nome do arquivo
   - Fallback para títulos padrão quando necessário

4. **Histórico de Documentos**
   - Armazenamento em JSON para persistência
   - Evita notificações duplicadas
   - Fácil backup e restauração

5. **Email HTML**
   - Design responsivo
   - Botões de acesso direto
   - Formatação clara e organizada

### Fluxo de Execução

1. O script inicia carregando configurações e histórico
2. A cada hora:
   - Verifica novos documentos no site
   - Compara com o histórico
   - Formata títulos dos novos documentos
   - Envia email se houver novidades
   - Atualiza o histórico
3. Continua em loop até ser interrompido

## Detalhes Técnicos

### Histórico de Documentos
- Armazenado em `document_history.json`
- Evita notificações duplicadas
- Mantém registro de todos os documentos já encontrados
- Formato:
```json
{
    "documentos": [
        {
            "titulo": "12º Relatório Mensal de Atividades (RMA)",
            "url": "https://exemplo.com/RMA12.pdf",
            "data_descoberta": "2024-02-14 15:30:45"
        }
    ]
}
```

### Processo de Monitoramento
1. Verifica o site a cada hora
2. Compara novos documentos com o histórico
3. Formata os títulos de acordo com o tipo
4. Envia email apenas para documentos novos
5. Atualiza o histórico

## Melhorias Futuras para Analistas

### Extração de Dados
- **OCR de PDFs**: Extração automática de dados financeiros dos RMAs
- **Tabelas Estruturadas**: Conversão de tabelas dos documentos para formatos analisáveis (CSV, Excel)
- **Indicadores-Chave**: Identificação e extração automática de indicadores financeiros importantes

### Análise Avançada
- **Comparação Automática**: Comparação automática de indicadores entre RMAs consecutivos
- **Alertas Personalizados**: Configuração de alertas baseados em thresholds específicos
- **Análise de Sentimento**: Análise de sentimento em decisões judiciais para identificar tendências

### Integração com Ferramentas
- **Exportação para Excel**: Exportação direta de dados para planilhas Excel
- **Integração com Bloomberg/Refinitiv**: Envio de dados para plataformas de análise financeira
- **APIs para Sistemas Internos**: APIs para integração com sistemas internos de análise

### Visualização e Relatórios
- **Dashboard Interativo**: Dashboard para visualização de dados extraídos dos documentos
- **Relatórios Automáticos**: Geração automática de relatórios baseados nos documentos
- **Timeline Visual**: Timeline visual do processo de recuperação judicial

### Personalização
- **Filtros por Tipo de Documento**: Configuração de notificações por tipo de documento
- **Palavras-Chave**: Alertas baseados em palavras-chave específicas nos documentos
- **Múltiplos Destinatários**: Envio de notificações para diferentes equipes com diferentes focos

## Solução de Problemas

### Email não está chegando
- Verifique as configurações SMTP no arquivo `.env`
- Confirme se a porta está correta (geralmente 465 para SSL)
- Verifique se a senha do email está correta
- Para Gmail, use uma "Senha de App" em vez da senha normal

### Links não funcionam
- Verifique sua conexão com a internet
- Certifique-se de que os PDFs ainda estão disponíveis no servidor
- Tente acessar os links diretamente no navegador

### Problemas com Títulos
- Verifique se o nome do arquivo segue o padrão esperado
- Para RMAs: deve conter "RMA" seguido do número
- Para Decisões: deve conter "Decisao" seguido da data

## Contribuindo

Sinta-se à vontade para:
- Reportar bugs
- Sugerir melhorias
- Enviar pull requests