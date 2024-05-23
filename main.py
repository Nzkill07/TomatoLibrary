from users import register_user, login_user
from books import show_books, search_books, reserve_book, show_reserved_books
from utils import clear_screen

def main():
    while True:
        print("1. Iniciar Sesión")
        print("2. Registrarse")
        print("3. Salir")
        choice = input("Seleccione una opción: ")

        if choice == '1':
            email = input("Correo: ")
            password = input("Contraseña: ")
            if login_user(email, password):
                user_menu(email)
            else:
                print("Credenciales incorrectas. Inténtelo de nuevo.")
        elif choice == '2':
            register_user()
        elif choice == '3':
            break
        else:
            print("Opción inválida. Inténtelo de nuevo.")

def user_menu(user_email):
    while True:
        clear_screen()
        print("Menú de Biblioteca")
        print("1. Libros Disponibles")
        print("2. Buscar Libros por Filtro")
        print("3. Reservar Libro")
        print("4. Consultar Libros Reservados")
        print("5. Salir")
        choice = input("Seleccione una opción: ")

        if choice == '1':
            show_books()
        elif choice == '2':
            search_books()
        elif choice == '3':
            reserve_book(user_email)
        elif choice == '4':
            show_reserved_books(user_email)
        elif choice == '5':
            break
        else:
            print("Opción inválida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()
