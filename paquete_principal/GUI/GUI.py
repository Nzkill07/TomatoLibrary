import tkinter as tk

# Function to open login window
def open_login_window():
    # Create login window
    login_window = tk.Toplevel(root)
    login_window.title("Biblioteca - Iniciar Sesión")

    # Create the login_label variable and assign a value
    login_label = tk.Label(login_window, text="Iniciar Sesión")

    # Login section widgets with labels
    username_label = tk.Label(login_window, text="Nombre de Usuario:")
    username_entry = tk.Entry(login_window)
    password_label = tk.Label(login_window, text="Contraseña:")
    password_entry = tk.Entry(login_window, show="*")
    login_button = tk.Button(login_window, text="Iniciar Sesión")

    # Grid layout for login section widgets
    login_label.grid(row=0, column=0, sticky=tk.W)
    username_label.grid(row=1, column=0, sticky=tk.W)
    username_entry.grid(row=1, column=1, padx=5)
    password_label.grid(row=2, column=0, sticky=tk.W)
    password_entry.grid(row=2, column=1, padx=5)
    login_button.grid(row=3, column=0, columnspan=2, pady=10)

    # Login window loop
    login_window.mainloop()

# Function to open register window
def open_register_window():
    # Create register window
    register_window = tk.Toplevel(root)
    register_window.title("Biblioteca - Registro")

    # Register section widgets
    name_label = tk.Label(register_window, text="Nombre de Usuario:")
    name_entry = tk.Entry(register_window)
    email_label = tk.Label(register_window, text="Correo electrónico:")
    email_entry = tk.Entry(register_window)
    password_label = tk.Label(register_window, text="Contraseña:")
    register_password_entry = tk.Entry(register_window, show="*")
    register_button = tk.Button(register_window, text="Registrarse")

    # Grid layout for register section widgets
    name_label.grid(row=0, column=0, sticky=tk.W)
    name_entry.grid(row=0, column=1, padx=5)
    email_label.grid(row=1, column=0, sticky=tk.W)
    email_entry.grid(row=1, column=1, padx=5)
    password_label.grid(row=2, column=0, sticky=tk.W)
    register_password_entry.grid(row=2, column=1, padx=5)
    register_button.grid(row=3, column=0, columnspan=2, pady=10)

    # Register window loop
    register_window.mainloop()

# Main window (root)
root = tk.Tk()
root.title("Biblioteca - Principal")

# Login button
login_button = tk.Button(root, text="Iniciar Sesión", command=open_login_window)
login_button.pack(pady=10)

# Register button
register_button = tk.Button(root, text="Registrarse", command=open_register_window)
register_button.pack(pady=10)

# Rest of your code for buttons (show_books, etc.) goes here

# Start the main window loop
root.mainloop()
