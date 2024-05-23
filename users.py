import json
import os

DATA_FILE = 'users.json'

def load_users():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_users(users):
    with open(DATA_FILE, 'w') as file:
        json.dump(users, file)

def register_user():
    users = load_users()
    print("Registro de Usuario")
    nombre = input("Nombre: ")
    correo = input("Correo: ")
    print(f"Correo ingresado: {correo}")  # Línea de depuración
    contraseña = input("Contraseña: ")
    print(f"Contraseña ingresada: {contraseña}")  # Línea de depuración

    if correo in users:
        print("Este correo ya está registrado. Intente iniciar sesión.")
    else:
        users[correo] = {'nombre': nombre, 'contraseña': contraseña, 'reservas': []}
        save_users(users)
        print("Registro exitoso. Ahora puede iniciar sesión.")
    input("Presione Enter para continuar...")

def login_user():
    users = load_users()
    print("Inicio de Sesión")
    correo = input("Correo: ")
    print(f"Correo ingresado: {correo}")  # Línea de depuración
    contraseña = input("Contraseña: ")
    print(f"Contraseña ingresada: {contraseña}")  # Línea de depuración

    if correo in users and users[correo]['contraseña'] == contraseña:
        print("Inicio de sesión exitoso.")
        input("Presione Enter para continuar...")
        return correo
    else:
        print("Correo o contraseña incorrectos.")
        input("Presione Enter para continuar...")
        return None
