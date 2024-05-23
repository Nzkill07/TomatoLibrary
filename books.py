import json
import os
import datetime

BOOKS_FILE = 'books.json'
RESERVATIONS_FILE = 'reservations.json'

def load_books():
    if os.path.exists(BOOKS_FILE):
        with open(BOOKS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_books(books):
    with open(BOOKS_FILE, 'w') as file:
        json.dump(books, file)

def load_reservations():
    if os.path.exists(RESERVATIONS_FILE):
        with open(RESERVATIONS_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_reservations(reservations):
    with open(RESERVATIONS_FILE, 'w') as file:
        json.dump(reservations, file)

def show_books():
    books = load_books()
    print("Libros Disponibles:")
    for book in books:
        print(f"- {book['titulo']} (Autor: {book['autor']}, Categoría: {book['categoria']})")
    input("Presione Enter para continuar...")

def search_books():
    books = load_books()
    print("Buscar Libros")
    print("1. Por Autor")
    print("2. Por Categoría")
    print("3. Por Título")
    print("4. Por Disponibilidad")
    choice = input("Seleccione una opción: ")

    if choice == '1':
        autor = input("Ingrese el nombre del autor: ")
        filtered_books = [book for book in books if book['autor'].lower() == autor.lower()]
    elif choice == '2':
        print("Categorías: Comedia, Romance, Acción, Terror, Sobrenatural")
        categoria = input("Ingrese la categoría: ")
        filtered_books = [book for book in books if book['categoria'].lower() == categoria.lower()]
    elif choice == '3':
        titulo = input("Ingrese el título del libro: ")
        filtered_books = [book for book in books if book['titulo'].lower() == titulo.lower()]
    elif choice == '4':
        filtered_books = [book for book in books if book['disponible']]
    else:
        print("Opción inválida.")
        input("Presione Enter para continuar...")
        return

    if filtered_books:
        print("Resultados de la búsqueda:")
        for book in filtered_books:
            print(f"- {book['titulo']} (Autor: {book['autor']}, Categoría: {book['categoria']})")
    else:
        print("No se encontraron libros.")
    input("Presione Enter para continuar...")

def reserve_book(user_email):
    books = load_books()
    reservations = load_reservations()

    if user_email not in reservations:
        reservations[user_email] = []

    if len(reservations[user_email]) >= 3:
        print("Ya tiene el máximo de 3 libros reservados.")
        input("Presione Enter para continuar...")
        return

    titulo = input("Ingrese el título del libro a reservar: ")
    for book in books:
        if book['titulo'].lower() == titulo.lower() and book['disponible']:
            confirm = input(f"¿Desea reservar el libro '{titulo}'? (s/n): ")
            if confirm.lower() == 's':
                book['disponible'] = False
                reservations[user_email].append({'titulo': titulo, 'fecha_reserva': str(datetime.date.today())})
                save_books(books)
                save_reservations(reservations)
                print("Libro reservado con éxito.")
                input("Presione Enter para continuar...")
                return
    print("Libro no disponible o no encontrado.")
    input("Presione Enter para continuar...")

def show_reserved_books(user_email):
    reservations = load_reservations()

    if user_email in reservations and reservations[user_email]:
        print("Libros Reservados:")
        for reservation in reservations[user_email]:
            fecha_reserva = datetime.date.fromisoformat(reservation['fecha_reserva'])
            dias_restantes = (fecha_reserva + datetime.timedelta(days=7) - datetime.date.today()).days
            print(f"- {reservation['titulo']} (Días restantes: {dias_restantes})")
    else:
        print("No tiene libros reservados.")
    input("Presione Enter para continuar...")
