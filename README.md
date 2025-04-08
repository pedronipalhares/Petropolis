# Monitor de Documentos - Grupo Petrópolis

Este script monitora o site do escritório Zveiter para novos documentos relacionados ao processo de recuperação judicial do Grupo Petrópolis e envia notificações por email quando novos documentos são encontrados.

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