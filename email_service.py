import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

def enviar_correo(destinatario, asunto, mensaje):
    servidor_smtp = 'smtp.gmail.com'
    puerto_smtp = 587
    remitente = 'tomatolibraryeduco@gmail.com'
    contraseña = 'ngjq zhsg zbhn clso'

    msg = MIMEMultipart()
    msg['From'] = remitente
    msg['To'] = destinatario
    msg['Subject'] = asunto

    msg.attach(MIMEText(mensaje, 'plain'))

    servidor = smtplib.SMTP(host=servidor_smtp, port=puerto_smtp)
    servidor.starttls()
    servidor.login(remitente, contraseña)

    servidor.send_message(msg)
    servidor.quit()

def reservar_libro(libro, usuario, correo_usuario):
    tiempo_devolucion = datetime.datetime.now() + datetime.timedelta(days=7)
    mensaje = f"¡Hola {usuario}!\n\nHas reservado el libro '{libro}'.\n\nPor favor, devuélvelo antes de: {tiempo_devolucion.strftime('%Y-%m-%d %H:%M:%S')}"
    enviar_correo(correo_usuario, "Reserva de libro", mensaje)

