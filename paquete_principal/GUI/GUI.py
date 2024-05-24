import tkinter as tk
from tkinter import messagebox, ttk
from paquete_principal.Modelo.Library import Library, Users


class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Biblioteca")

        # Crear una instancia de la clase Library
        self.library = Library()

        # Variables de control para los campos de entrada
        self.email_var = tk.StringVar()
        self.password_var = tk.StringVar()

        # Configuración de la ventana principal
        self.setup_main_window()

    def setup_main_window(self):
        # Etiqueta de bienvenida
        welcome_label = tk.Label(self.root, text="Bienvenido a la Biblioteca", font=("Helvetica", 16))
        welcome_label.pack(pady=10)

        # Campos de entrada para inicio de sesión
        email_label = tk.Label(self.root, text="Correo electrónico:")
        email_label.pack()
        email_entry = tk.Entry(self.root, textvariable=self.email_var)
        email_entry.pack()

        password_label = tk.Label(self.root, text="Contraseña:")
        password_label.pack()
        password_entry = tk.Entry(self.root, textvariable=self.password_var, show="*")
        password_entry.pack()

        # Botón de inicio de sesión
        login_button = tk.Button(self.root, text="Iniciar Sesión", command=self.login)
        login_button.pack(pady=5)

        # Botón para registrar usuario
        register_button = tk.Button(self.root, text="Registrarse", command=self.open_register_window)
        register_button.pack()

    def open_register_window(self):
        register_window = tk.Toplevel()
        register_window.title("Registrar Usuario")
        register_window.geometry("400x400")

        # Campos de entrada para registro
        name_label = tk.Label(register_window, text="Nombre:")
        name_label.grid(row=0, column=0)
        name_entry = tk.Entry(register_window)
        name_entry.grid(row=0, column=1)

        email_label = tk.Label(register_window, text="Correo electrónico:")
        email_label.grid(row=1, column=0)
        email_entry = tk.Entry(register_window)
        email_entry.grid(row=1, column=1)

        password_label = tk.Label(register_window, text="Contraseña:")
        password_label.grid(row=2, column=0)
        password_entry = tk.Entry(register_window, show="*")
        password_entry.grid(row=2, column=1)

        confirm_password_label = tk.Label(register_window, text="Confirmar contraseña:")
        confirm_password_label.grid(row=3, column=0)
        confirm_password_entry = tk.Entry(register_window, show="*")
        confirm_password_entry.grid(row=3, column=1)

        # Botón de registro
        register_button = tk.Button(register_window, text="Registrar usuario",command=lambda: self.register_user(name_entry.get(), email_entry.get(),password_entry.get(), confirm_password_entry.get()))
        register_button.grid(row=4, columnspan=2, pady=10)

    def open_library_window(self):
        library_window = tk.Toplevel()
        library_window.title("Biblioteca")
        library_window.geometry("400x400")
        label_window = tk.Label(library_window, text="Busqueda de libros", font=("Helvetica", 16))
        label_window.pack(pady=10)

        # Crear lista desplegable para los filtros de libros
        filters_label = tk.Label(library_window, text="Filtros de libros:")
        filters_label.pack()

        filters = ["Autor", "Título", "Disponibles", "Categorias"]
        filter_var = tk.StringVar()
        filter_dropdown = ttk.Combobox(library_window, textvariable=filter_var, values=filters)
        filter_dropdown.pack()

        def select_filter():
            selected_filter = filter_dropdown.get()
            messagebox.showinfo("Filtro", f"El filtro aplicado es {selected_filter}")
            self.open_another_window(selected_filter)

        # Botón para seleccionar filtro
        select_books_button = tk.Button(library_window, text="Seleccionar filtro", command=select_filter)
        select_books_button.pack(pady=10)

    @staticmethod
    def open_another_window(title):
        another_window = tk.Toplevel()
        another_window.title(title)
        another_window.geometry("400x400")

        # Crear otro menú desplegable
        options_label = tk.Label(another_window, text="Opciones")
        options_label.pack()
        options = ""
        if title == "Categorias":
            options = ["Comedia", "Romance", "Accion", "Terror", "Sobrenatural"]
        elif title == "titulo":
            options = []
        elif title == "Disponibilidad":
            options = Library.disponibles
        option_var = tk.StringVar()
        option_dropdown = ttk.Combobox(another_window, textvariable=option_var, values=options)
        option_dropdown.pack()

        # Función para manejar la selección de opción
        def select_option():
            selected_option = option_dropdown.get()
            messagebox.showinfo(title, f"Usted selecciono {selected_option}")

        # Botón para seleccionar opción
        select_option_button = tk.Button(another_window, text="Seleccionar opción", command=select_option)
        select_option_button.pack(pady=10)

    def register_user(self, name, email, password, confirm_password):
        if password != confirm_password:
            messagebox.showerror("Error", "Las contraseñas no coinciden")
            return

        try:
            usuario = Users(name, email, password)
            self.library.registrar_user(usuario)
            messagebox.showinfo("Registro", "Usuario registrado exitosamente")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def login(self):
        email = self.email_var.get()
        password = self.password_var.get()
        usuario = Users("", email, password)
        try:
            if self.library.login_user(usuario):
                messagebox.showinfo("Inicio de sesión", "Inicio de sesión exitoso")
                # Abre la ventana de la biblioteca después de iniciar sesión
                self.open_library_window()
                # Oculta la ventana principal en lugar de destruirla
                self.root.withdraw()
            else:
                messagebox.showerror("Inicio de sesión", "Error: Correo electrónico o contraseña incorrectos")
        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x400")
    app = LibraryApp(root)
    root.mainloop()
