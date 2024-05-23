import tkinter as tk

def show_books():
    pass
def search_books():
    pass

def reserve_book():
    pass

def show_reserved_books():
    pass

root = tk.Tk()
root.title("Biblioteca Python")

# Crear un frame para el contenido principal
content_frame = tk.Frame(root)
content_frame.pack(padx=10, pady=10)

# Crear botones para cada acción
show_books_button = tk.Button(content_frame, text="Mostrar Libros", command=show_books)
show_books_button.pack(pady=5)

search_books_button = tk.Button(content_frame, text="Buscar Libros", command=search_books)
search_books_button.pack(pady=5)

reserve_book_button = tk.Button(content_frame, text="Reservar Libro", command=reserve_book)
reserve_book_button.pack(pady=5)

show_reserved_books_button = tk.Button(content_frame, text="Ver Reservas", command=show_reserved_books)
show_reserved_books_button.pack(pady=5)

# Iniciar el bucle principal de la interfaz
root.mainloop()
