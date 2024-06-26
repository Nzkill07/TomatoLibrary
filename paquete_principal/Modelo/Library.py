import json
import os
import datetime


class Book:
    def __init__(self, titulo, autor, categoria, disponible):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.disponible = disponible


class Library:
    def __init__(self, books_file='books.json', reservations_file='reservations.json'):
        self.books_file = books_file
        self.reservations_file = reservations_file
        self.books = self.load_books()
        self.reservations = self.load_reservations()

    def load_books(self):
        if os.path.exists(self.books_file):
            with open(self.books_file, 'r') as file:
                return [Book(**book_dict) for book_dict in json.load(file)]
        return []

    def save_books(self):
        with open(self.books_file, 'w') as file:
            json.dump([book.__dict__ for book in self.books], file)

    def load_reservations(self):
        if os.path.exists(self.reservations_file):
            with open(self.reservations_file, 'r') as file:
                return json.load(file)
        return {}

    def save_reservations(self):
        with open(self.reservations_file, 'w') as file:
            json.dump(self.reservations, file)

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
            # Búsqueda por disponibilidad
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
                self.save_books()

                if user_email not in self.reservations:
                    self.reservations[user_email] = []
                self.reservations[user_email].append({'titulo': titulo, 'fecha_reserva': str(datetime.date.today())})
                self.save_reservations()

                return True

        return False

    def show_reserved_books(self, user_email):
        if not isinstance(user_email, str):
            raise TypeError("Email del usuario no válido")

        if user_email not in self.reservations:
            return []

        reservas = self.reservations[user_email]
        libros_reservados = []

        for reserva in reservas:
            titulo = reserva['titulo']
            fecha_reserva = datetime.date.fromisoformat(reserva['fecha_reserva'])
            dias_restantes = (fecha_reserva + datetime.timedelta(days=7) - datetime.date.today()).days
            libros_reservados.append({'titulo': titulo, 'dias_restantes': dias_restantes})

        return libros_reservados
