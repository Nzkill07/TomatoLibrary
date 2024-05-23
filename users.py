import json
import os

USERS_FILE = 'users.json'

def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_users(users):
    with open(USERS_FILE, 'w') as file:
        json.dump(users, file)

def register_user():
    users = load_users()
    print("Registro de Usuario")
    nombre = input("Nombre: ")
    correo = input("Correo: ")
    if correo in users:
        print("Este correo ya está registrado.")
        return
    contraseña = input("Contraseña: ")

    users[correo] = {
        "nombre": nombre,
        "contraseña": contraseña
    }
    save_users(users)
    print("Usuario registrado con éxito.")

def login_user(email, password):
    users = load_users()
    if email in users and users[email]['contraseña'] == password:
        return True
    return False
