import base64
import datetime
import smtplib
from asyncio import shield
from dataclasses import dataclass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import ClassVar

import bcrypt
import requests
from googletrans import Translator


class Users:
    def __init__(self, name: str, email: str, password: str):
        self.name = name
        self.email = email
        self.password = password
        self.reservations = []


class Book:
    def __init__(self, titulo, autor, categoria, disponible):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.disponible = disponible


def translate_to_spanish(text):
    traductor = Translator()
    translated_text = traductor.translate(text)
    return translated_text.text


def enviar_correo(destinatario, asunto, mensaje):
    servidor_smtp = 'smtp.gmail.com'
    puerto_smtp = 587
    remitente = 'tomatolibraryeduco@gmail.com'
    admin_password = 'ngjq zhsg zbhn clso'

    msg = MIMEMultipart()
    msg['From'] = remitente
    msg['To'] = destinatario
    msg['Subject'] = asunto

    msg.attach(MIMEText(mensaje, 'plain'))

    servidor = smtplib.SMTP(host=servidor_smtp, port=puerto_smtp)
    servidor.starttls()
    servidor.login(remitente, admin_password)

    servidor.send_message(msg)
    servidor.quit()


def obtener_resenas_sinopsis(isbn):
    url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'items' in data:
            libro = data['items'][0]
            if 'description' in libro['volumeInfo']:
                sinopsis_ingles = libro['volumeInfo']['description']
                sinopsis_espanol = translate_to_spanish(sinopsis_ingles)

                # Return the translated synopsis instead of printing it
                return sinopsis_espanol

            else:
                # Handle the case where there's no description
                return None

        else:
            # Handle the case where no items are found
            return None

    else:
        # Handle HTTP errors
        return None


def encrypt_password(password):
    hash_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    return base64.b64encode(hash_password).decode("utf-8")


@dataclass
class Library:
    disponibles: ClassVar = []
    users: ClassVar = {}

    def registrar_user(self, user: Users):
        if user.email in self.users:
            raise ValueError("Email ya existe")
        else:
            self.users[user.email] = {"nombre": user.name, "contraseña": encrypt_password(user.password)}

    def login_user(self, user: Users):
        if user.email in self.users and self.verify_password(user):
            return True
        else:
            raise ValueError("El usuario ingresado no es correcto")

    def verify_password(self, user: Users):
        hashed_password_base64 = self.users[user.email]["contraseña"]
        hashed_password = base64.b64decode(hashed_password_base64.encode('utf-8'))
        return bcrypt.checkpw(user.password.encode("utf-8"), hashed_password)

    def reservar_libro(self, user: Users, titulo):
        tiempo_devolucion = datetime.datetime.now() + datetime.timedelta(days=7)
        mensaje = (f"¡Hola {user.name}!\n\nHas reservado el libro '{titulo}'.\n\n"
                   f"Por favor, devuélvelo antes de: {tiempo_devolucion.strftime('%Y-%m-%d %H:%M:%S')}")
        enviar_correo(user.email, "Reserva de libro", mensaje)
