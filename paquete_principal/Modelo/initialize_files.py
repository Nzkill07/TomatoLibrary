import json
import os


def initialize_files():
    users_file = 'users.json'
    books_file = 'books.json'
    reservations_file = 'reservations.json'

    if not os.path.exists(users_file):
        with open(users_file, 'w') as file:
            json.dump({}, file)

    if not os.path.exists(books_file):
        books = [
            {"titulo": "Libro1", "autor": "Autor1", "categoria": "Acción", "disponible": True},
            {"titulo": "Libro2", "autor": "Autor2", "categoria": "Comedia", "disponible": True}
        ]
        with open(books_file, 'w') as file:
            json.dump(books, file)

    if not os.path.exists(reservations_file):
        with open(reservations_file, 'w') as file:
            json.dump({}, file)
initialize_files()