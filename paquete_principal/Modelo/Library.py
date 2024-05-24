import datetime
import smtplib
from dataclasses import dataclass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import ClassVar
import requests
from googletrans import Translator


class Users:
    reservations = {}

    def __init__(self, name: str, email: str, password: str):
        self.name = name
        self.email = email
        self.password = password


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


@dataclass
class Library:
    disponibles: ClassVar = []
    users: ClassVar = {}
    books: ClassVar = [{"title": "Cien años de soledad", "autor": "Gabriel garcia marquez", "categoria": "Romance", "disponible": True},
    {"title": "El señor de los anillos", "autor": "J R R Tolkien", "categoria": "Sobrenatural", "disponible": True},
    {"title": "Orgullo y prejuicio", "autor": " jane austen", "categoria": "Romance" , "disponible": True},
    {"title": "Don quijote de la mancha", "autor": "miguel de cervantes" , "categoria": "Comedia", "disponible": True},
    {"title": "Hamlet", "autor": "william   Shakespeare", "categoria": "Romance", "disponible": True},
    {"title": "La odisea", "autor": "homero", "categoria": "Sobrenatural", "disponible": True},
    {"title": "Caperucita roja", "autor": "Charles Perrault", "categoria": "Fantasia", "disponible": True},
    {"title": "Drácula", "autor": "Bram Stoker", "categoria": "Terror", "disponible": True},
    {"title": "En las montañas de la locura", "autor": "Howard Phillips Lovecraft", "categoria": "Terror", "disponible": True}]




    user: Users = None

    def registrar_user(self, user: Users):
        if user.email in self.users:
            raise ValueError("Email ya existe")
        else:
            self.users[user.email] = {"nombre": user.name, "contraseña": user.password}

    def login_user(self, user: Users):
        if user.email in self.users and self:
            return True
        else:
            raise ValueError("El usuario ingresado no es correcto")

    def show_books(self):
        libros_disponibles = []
        for book in self.books:
            libros_disponibles.append(f"- {book}")
        return libros_disponibles

    def search_books(self, criterio_busqueda=None):
        if criterio_busqueda is None:
            return self.books

        filtered_books = []

        if isinstance(criterio_busqueda, str):
            criterio_busqueda = criterio_busqueda.lower()
            for book in self.books:
                if book.autor.lower().find(criterio_busqueda) != -1 or \
                        book.titulo.lower().find(criterio_busqueda) != -1 or \
                        book.categoria.lower().find(criterio_busqueda) != -1:
                    filtered_books.append(book)
        elif isinstance(criterio_busqueda, bool):
            filtered_books = [book for book in self.books if book.disponible == criterio_busqueda]
        else:
            raise TypeError("Criterio de búsqueda no válido")

        return filtered_books

    def reserve_book(self, user_email, titulo):
        if not isinstance(user_email, str):
            raise TypeError("Email del usuario no válido")
        if not isinstance(titulo, str):
            raise TypeError("Título del libro no válido")

        titulo = titulo.lower()

        for book in self.books:
            if book.titulo.lower() == titulo and book.disponible:
                book.disponible = False
                if user_email not in Users.reservations:
                    Users.reservations[user_email] = []
                    Users.reservations[user_email].append(
                        {'titulo': titulo, 'fecha_reserva': str(datetime.date.today())})
                return True
        self.reservar_libro(titulo)

        return False

    def reservar_libro(self, titulo):
        tiempo_devolucion = datetime.datetime.now() + datetime.timedelta(days=7)
        mensaje = (f"¡Hola {self.user.name}!\n\nHas reservado el libro '{titulo}'.\n\n"
                   f"Por favor, devuélvelo antes de: {tiempo_devolucion.strftime('%Y-%m-%d %H:%M:%S')}")
        enviar_correo(self.user.email, "Reserva de libro", mensaje)
