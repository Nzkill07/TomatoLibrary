import json
import os
import bcrypt

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
    hashed_contraseña = bcrypt.hashpw(contraseña.encode('utf-8'), bcrypt.gensalt())

    users[correo] = {
        "nombre": nombre,
        "contraseña": hashed_contraseña.decode('utf-8')
    }
    save_users(users)
    print("Usuario registrado con éxito.")

def login_user(email, password):
    users = load_users()
    if email in users and bcrypt.checkpw(password.encode('utf-8'), users[email]['contraseña'].encode('utf-8')):
        return True
    return False
