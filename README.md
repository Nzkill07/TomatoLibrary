# Tomato Library

Tomato Library es una aplicación de escritorio con interfaz gráfica para la gestión de una biblioteca virtual. Permite a los usuarios registrarse, iniciar sesión, ver libros disponibles, buscar libros, reservar libros y consultar libros reservados. Además, envía un correo electrónico de confirmación cuando un usuario reserva un libro.

![DiagramaClases  (2).drawio.png](..%2F..%2FDownloads%2FDiagramaClases%20%20%282%29.drawio.png)


## Características

- Registro de usuario
- Inicio de sesión
- Ver libros disponibles
- Buscar libros por filtro (autor, categoría, título, disponibilidad)
- Reservar libros
- Consultar libros reservados
- Envío de correo electrónico de confirmación de reserva
- Contraseñas encriptadas

## Requisitos

- Python 3.x
- `bcrypt` (para encriptar contraseñas)
- `requests` (para la API de Google Books)
- `smtplib` (para enviar correos electrónicos)
- `email` (para construir correos electrónicos)
- `translate` (para traducir sinopsis)
- `tkinter` (para la interfaz gráfica)

## Instalación

1. Clona este repositorio:

    ```sh
    git clone https://github.com/tu_usuario/tomato-library.git
    cd tomato-library
    ```

2. Instala las dependencias necesarias:

    ```sh
    pip install bcrypt requests translate
    ```

## Estructura del Proyecto

```plaintext
tomato-library/
├── books.py
├── email_service.py
├── main.py
├── user_management.py
├── tkinter_app.py
└── README.md
# Tomato Library

Tomato Library es una aplicación de escritorio con interfaz gráfica para la gestión de una biblioteca virtual. Permite a los usuarios registrarse, iniciar sesión, ver libros disponibles, buscar libros, reservar libros y consultar libros reservados. Además, envía un correo electrónico de confirmación cuando un usuario reserva un libro.

## Características

- Registro de usuario
- Inicio de sesión
- Ver libros disponibles
- Buscar libros por filtro (autor, categoría, título, disponibilidad)
- Reservar libros
- Consultar libros reservados
- Envío de correo electrónico de confirmación de reserva
- Contraseñas encriptadas

## Requisitos

- Python 3.x
- `bcrypt` (para encriptar contraseñas)
- `requests` (para la API de Google Books)
- `smtplib` (para enviar correos electrónicos)
- `email` (para construir correos electrónicos)
- `translate` (para traducir sinopsis)
- `tkinter` (para la interfaz gráfica)

## Instalación

1. Clona este repositorio:

    ```sh
    git clone https://github.com/Nzkill2/tomato-library.git
    cd tomato-library
    ```

2. Instala las dependencias necesarias:

    ```sh
    pip install bcrypt requests translate
    ```

## Estructura del Proyecto

```plaintext
tomato-library/
├── books.py
├── email_service.py
├── main.py
├── user_management.py
├── tkinter_app.py
└── README.md
