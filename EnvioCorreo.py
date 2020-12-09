import email, smtplib, ssl
import argparse

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


#parser = argparse.ArgumentParser()
#parser.add_argument("-a", dest="asunto", help="El asunto del correo")
#parser.add_argument("-c", dest="cuerpo", help="El cuerpo del correo")
#parser.add_argument("-r", dest="remi", help="El remitente del correo")
#parser.add_argument("-d", dest="dest", help="El destinatario del correo")
#parser.add_argument("-p", dest="psw", help="La contraseña del correo a utilizar")
#parser.add_argument("-i", dest="img", help="El nombre del archivo que se mandará")
#params = parser.parse_args()
def Envio(remi, dest, asunto, filename, msg, psw):
    print(asunto)
    print(msg)
    print(remi)
    print(dest)
    print(psw)
    print(filename)

    message = MIMEMultipart()
    #message["From"] = params.remi
    #message["To"] = params.dest
    #message["Subject"] = params.asunto
    #message["Bcc"] = params.dest  

    message.attach(MIMEText(msg, "plain"))


    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())  
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    message.attach(part)
    text = message.as_string()
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(remi ,psw)
        server.sendmail(remi, dest, text)
