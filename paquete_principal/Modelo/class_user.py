from paquete_principal.Modelo.Library import Book


class Users:
    def __init__(self, name: str, email: str, password: str):
        self.name = name
        self.email = email
        self.password = password
        self.reservations: list[Book] = []

