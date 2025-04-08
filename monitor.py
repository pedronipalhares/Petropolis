import os
import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
URL = "https://www.zveiter.com.br/post/grupo-petr%C3%B3polis"
HISTORY_FILE = "document_history.json"

def load_history():
    """Load the history of previously found documents."""
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'r') as f:
            return json.load(f)
    return []

def save_history(history):
    """Save the document history to a file."""
    with open(HISTORY_FILE, 'w') as f:
        json.dump(history, f)

def get_documents():
    """Fetch and parse the website for documents."""
    try:
        response = requests.get(URL)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all document links - adjust the selector based on the website's structure
        documents = []
        
        # First, try to find download buttons/links
        download_links = soup.find_all('a', href=True, class_='w-button')
        if not download_links:
            download_links = soup.find_all('a', href=True)

        for link in download_links:
            href = link['href']
            if 'Fazer download' in link.text or any(ext in href.lower() for ext in ['.pdf', '.doc', '.docx']):
                # Extract title from URL first
                title = None
                url_parts = href.split('/')
                filename = url_parts[-1]
                
                # Try to extract date and document type from filename and URL
                if 'RMA' in filename:
                    try:
                        # Get the RMA number from the filename
                        rma_number = filename.split('o-RMA')[0]
                        if not rma_number:
                            rma_number = filename.split('.pdf')[0].replace('o-RMA', '')
                            
                        title = f"{rma_number}º Relatório Mensal de Atividades (RMA)"
                    except Exception as e:
                        print(f"Error extracting RMA info: {e}")
                        title = f"RMA {filename.replace('.pdf', '')}"
                elif 'Decisao' in filename:
                    # For decision documents, format the date if present
                    parts = filename.split('-')
                    if len(parts) >= 3 and parts[0] == 'Decisao':
                        try:
                            day = parts[1].strip()
                            month = parts[2].strip()
                            year = parts[3].split('.')[0].strip()  # Remove .pdf and any extra spaces
                            rest = ' '.join([p for p in parts[3:] if p and '.pdf' not in p])
                            title = f"Decisão de {day.zfill(2)}/{month.zfill(2)}/{year}"
                            if rest:
                                title += f" - {rest.replace('-', ' ').title()}"
                        except:
                            title = "Decisão " + filename.replace('.pdf', '').replace('Decisao-', '').replace('-', '/')
                    else:
                        title = "Decisão " + filename.replace('.pdf', '').replace('Decisao-', '').replace('-', '/')
                else:
                    # For other documents, use a default format
                    title = filename.replace('.pdf', '').replace('-', ' ').title()

                # Clean up the URL
                if not href.startswith(('http://', 'https://')):
                    if href.startswith('//'):
                        href = 'https:' + href
                    elif href.startswith('/'):
                        href = 'https://www.zveiter.com.br' + href
                    else:
                        href = 'https://www.zveiter.com.br/' + href

                print(f"\nFound document:")
                print(f"Title: {title}")
                print(f"URL: {href}")

                documents.append({
                    'title': title,
                    'url': href,
                    'date_found': datetime.now().isoformat()
                })
        
        print(f"\nTotal documents found: {len(documents)}")
        return documents
    except Exception as e:
        print(f"Error fetching documents: {e}")
        import traceback
        print(f"Full traceback: {traceback.format_exc()}")
        return []

def send_email_notification(new_documents):
    """Send email notification about new documents."""
    if not new_documents:
        return

    # Email configuration
    smtp_server = os.getenv('SMTP_SERVER')
    smtp_port = int(os.getenv('SMTP_PORT'))
    email_user = os.getenv('EMAIL_USER')
    email_password = os.getenv('EMAIL_PASSWORD')
    notification_email = os.getenv('NOTIFICATION_EMAIL')

    print(f"Attempting to send email using SMTP server: {smtp_server}:{smtp_port}")
    print(f"From: {email_user}")
    print(f"To: {notification_email}")

    # Create message
    msg = MIMEMultipart('alternative')
    msg['From'] = email_user
    msg['To'] = notification_email
    msg['Subject'] = f"📄 Novos Documentos Grupo Petrópolis - {datetime.now().strftime('%d/%m/%Y %H:%M')}"

    # Create the HTML email content
    html = f"""
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 20px;
                color: #333;
            }}
            .header {{
                background-color: #f8f9fa;
                padding: 20px;
                border-radius: 5px;
                margin-bottom: 20px;
                border-left: 4px solid #007bff;
            }}
            .document-card {{
                background-color: white;
                border: 1px solid #e9ecef;
                border-radius: 5px;
                padding: 15px;
                margin-bottom: 15px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.05);
            }}
            .document-title {{
                color: #007bff;
                font-size: 16px;
                margin: 0 0 10px 0;
            }}
            .document-url {{
                display: inline-block;
                background-color: #28a745;
                color: white;
                padding: 8px 15px;
                border-radius: 4px;
                text-decoration: none;
                margin-top: 10px;
                font-weight: bold;
            }}
            .document-url:hover {{
                background-color: #218838;
                text-decoration: none;
            }}
            .document-date {{
                color: #6c757d;
                font-size: 14px;
                margin-top: 10px;
            }}
            .footer {{
                margin-top: 30px;
                padding-top: 20px;
                border-top: 1px solid #e9ecef;
                color: #6c757d;
                font-size: 14px;
            }}
        </style>
    </head>
    <body>
        <div class="header">
            <h2 style="margin:0;color:#007bff;">🔔 Novos Documentos Encontrados</h2>
            <p style="margin:10px 0 0 0;color:#6c757d;">
                {len(new_documents)} novo(s) documento(s) encontrado(s) no site do Grupo Petrópolis
            </p>
        </div>
        
        <div class="documents">
    """

    # Add each document to the HTML
    for doc in new_documents:
        date_found = datetime.fromisoformat(doc['date_found']).strftime('%d/%m/%Y às %H:%M')
        html += f"""
            <div class="document-card">
                <h3 class="document-title">📄 {doc['title']}</h3>
                <div class="document-date">📅 Encontrado em: {date_found}</div>
                <a href="{doc['url']}" class="document-url" target="_blank">🔗 Acessar documento</a>
            </div>
        """

    # Add footer
    html += f"""
        </div>
        <div class="footer">
            <p>Este é um email automático do monitor de documentos do Grupo Petrópolis.</p>
            <p>Data da verificação: {datetime.now().strftime('%d/%m/%Y às %H:%M')}</p>
        </div>
    </body>
    </html>
    """

    # Create both plain text and HTML versions
    text = f"Novos Documentos Encontrados - Grupo Petrópolis\n\n"
    text += f"{len(new_documents)} novo(s) documento(s) encontrado(s):\n\n"
    for doc in new_documents:
        date_found = datetime.fromisoformat(doc['date_found']).strftime('%d/%m/%Y às %H:%M')
        text += f"Título: {doc['title']}\n"
        text += f"URL: {doc['url']}\n"
        text += f"Data: {date_found}\n\n"

    msg.attach(MIMEText(text, 'plain'))
    msg.attach(MIMEText(html, 'html'))

    try:
        # Send email
        print("Connecting to SMTP server...")
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        print("Connected to SMTP server")
        print("Logging in...")
        server.login(email_user, email_password)
        print("Logged in successfully")
        print("Sending message...")
        server.send_message(msg)
        print("Message sent successfully")
        server.quit()
        print(f"Email notification sent successfully for {len(new_documents)} new documents")
    except Exception as e:
        print(f"Error sending email: {str(e)}")
        print(f"Error type: {type(e)}")
        import traceback
        print(f"Full traceback: {traceback.format_exc()}")

def check_for_new_documents():
    """Main function to check for new documents and send notifications."""
    current_time = datetime.now()
    print(f"Checking for new documents at {current_time}")
    
    # Load previous history
    history = load_history()
    known_urls = {doc['url'] for doc in history}
    
    # Get current documents
    current_documents = get_documents()
    
    # Find new documents
    new_documents = [doc for doc in current_documents if doc['url'] not in known_urls]
    
    if new_documents:
        print(f"Found {len(new_documents)} new documents")
        # Send email notification
        send_email_notification(new_documents)
        # Update history
        history.extend(new_documents)
        save_history(history)
    else:
        print("No new documents found")

if __name__ == "__main__":
    check_for_new_documents() 