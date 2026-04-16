import smtplib
from email.message import EmailMessage

FILE="/home/soso/miniprojet/archive/message_mail.txt"

def sendMail(sonde, valeur):
    username = "adminprojetsoso@gmail.com"
    password = 'fgjslwlxefljetqi'

    msg = EmailMessage()
    msg['Subject'] = f"ALERTE SERVEUR : {sonde}"
    msg['From'] = username
    msg['To'] = "soufian.ajbilou84@gmail.com"
    with open(FILE,"r",encoding="utf-8") as file:
        contenue = file.read()
    
    contenue = contenue + "\n Valeur anormal récupéré sur " + str(sonde) + " : " + str(valeur)
    msg.set_content(contenue)

    smtp_server = 'smtp.gmail.com'
    port = 587
    try:
    	with smtplib.SMTP(smtp_server, port) as server:
        	server.starttls()
        	server.login(username, password)
        	server.send_message(msg)
    except smtplib.SMTPConnectError:
    	print("Erreur de connexion au serveur SMTP.")
    except smtplib.SMTPAuthenticationError:
    	print("Erreur d'authentification. Veuillez vérifier vos identifiants.")
    except Exception as e:
    	print(f"Une erreur s'est produite : {e}")


