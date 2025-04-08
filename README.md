# Monitor de Documentos - Grupo Petrópolis

Este script monitora o site do escritório Zveiter para novos documentos relacionados ao processo de recuperação judicial do Grupo Petrópolis e envia notificações por email quando novos documentos são encontrados.

## Funcionalidades

- ✅ Monitoramento automático do site do Grupo Petrópolis
- 📧 Notificações por email com design moderno e responsivo
- 🔍 Detecção inteligente de novos documentos
- 📝 Histórico de documentos para evitar duplicatas
- 🎯 Links diretos para download dos PDFs
- 🕒 Verificação automática a cada 5 minutos
- 📋 Formatação inteligente de títulos de documentos

## Tipos de Documentos

O monitor identifica e formata automaticamente os seguintes tipos de documentos:

### Relatórios Mensais (RMA)
- Formato: "Xº Relatório Mensal de Atividades (RMA)"
- Exemplo: "12º Relatório Mensal de Atividades (RMA)"

### Decisões Judiciais
- Formato: "Decisão de DD/MM/YYYY - Descrição"
- Exemplo: "Decisão de 12/12/2023 - Homologação Proposta Alienação UPI"

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

O script verifica automaticamente novos documentos a cada 5 minutos. Para iniciar o monitoramento contínuo:
```bash
python monitor.py
```

## Formato do Email

O script envia emails com:
- 📋 Lista organizada de novos documentos
- 🔗 Botões de acesso direto aos PDFs
- 📅 Data e hora de descoberta de cada documento
- 🎨 Design moderno e responsivo
- 📝 Títulos formatados de acordo com o tipo de documento

## Estrutura do Projeto

```
petropolis/
├── monitor.py          # Script principal
├── requirements.txt    # Dependências do projeto
├── .env.example       # Exemplo de configuração
├── .env               # Configurações reais (não versionado)
└── document_history.json  # Histórico de documentos (gerado automaticamente)
```

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

## Contribuindo

Sinta-se à vontade para:
- Reportar bugs
- Sugerir melhorias
- Enviar pull requests