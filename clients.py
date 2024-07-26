import smtplib
from email.mime.text import MIMEText
#pip install aiosmtpd
msg = MIMEText('Este é um email de teste.')
msg['Subject'] = 'Teste'
msg['From'] = 'sender@example.com'
msg['To'] = 'receiver@example.com'
print("\x1bc\x1b[47;34m")
with smtplib.SMTP('127.0.0.1', 1025) as server:
    server.send_message(msg)

print('Email enviado')

