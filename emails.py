
import os
from aiosmtpd.controller import Controller
from aiosmtpd.handlers import Message
from email.message import EmailMessage
#pip install aiosmtpd
# Definindo o diretório onde os emails serão salvos
EMAILS_DIR = 'emails'
os.makedirs(EMAILS_DIR, exist_ok=True)

class SaveMessageHandler:
    async def handle_DATA(self, server, session, envelope):
        # Cria um email a partir dos dados recebidos
        email = EmailMessage()
        email.set_content(envelope.content.decode('utf8', errors='replace'))
        
        # Define os cabeçalhos do email
        email['From'] = envelope.mail_from
        email['To'] = ', '.join(envelope.rcpt_tos)
        email['Subject'] = 'No Subject'
        
        # Salva o email no diretório EMAILS_DIR
        email_id = len(os.listdir(EMAILS_DIR)) + 1
        email_path = os.path.join(EMAILS_DIR, f'email_{email_id}.eml')
        with open(email_path, 'w') as f:
            f.write(email.as_string())

        print(f'Email salvo em {email_path}')
        return '250 Message accepted for delivery'
print("\x1bc\x1b[47;34m")
if __name__ == '__main__':
    # Cria o controlador do servidor SMTP
    handler = SaveMessageHandler()
    controller = Controller(handler,hostname="192.168.1.2", port=1025)

    # Inicia o servidor SMTP
    controller.start()
    print('Servidor SMTP iniciado em 127.0.0.1:1025')

    # Mantém o servidor em execução
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print('Servidor SMTP encerrado')
        controller.stop()
