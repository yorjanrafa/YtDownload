import customtkinter as ctk
import tkinter as tk  # Importar tkinter
from ytdl import downloader  # Importar la función downloader

# Configurar ventana principal
ctk.set_appearance_mode("light")  # Opciones: "light", "dark"
ctk.set_default_color_theme("green")  # Cambiar el tema de color
root = ctk.CTk()
root.geometry('340x380')
root.resizable(0, 0)
root.title("YouTube Downloader & Converter")

# Crear un marco con padding usando tk.Frame
frame = ctk.CTkFrame(
    root, fg_color="transparent"
)
frame.pack(
    expand=True, fill='both', padx=30, pady=30
)  # Padding aquí

# Título
title_label = ctk.CTkLabel(
    frame, text='YouTube Video Downloader', font=('Arial', 20, 'bold')
)
title_label.pack(
    pady=25
)

# Campo para el link de YouTube
link = ctk.StringVar()
link_label = ctk.CTkLabel(
    frame, text='Pega el link de YouTube aquí:', anchor='w'
)
link_label.pack(
    pady=1, anchor='w'
)
link_entry = ctk.CTkEntry(
    frame, width=0, textvariable=link
)
link_entry.pack(
    pady=10, fill='x'
)

# Opciones de formato
format_var = ctk.StringVar(
    value="mp3"
)
format_label = ctk.CTkLabel(
    frame, text='Formato de salida:', anchor='w'
)
format_label.pack(
    pady=1, anchor='w'
)
format_combo = ctk.CTkComboBox(
    frame, variable=format_var, values=["mp3", "flac", "aac"]
)
format_combo.pack(
    pady=1, fill='x'
)

# Etiqueta para mostrar resultados
result_label = ctk.CTkLabel(
    frame, text=''
)
result_label.pack(
    pady=1
)

# Botón para descargar 
# Hagase notar que se llama a la funcion downloader la cual es la encargade la logica de la descarga
download_btn = ctk.CTkButton(
    frame, text='DESCARGAR', 
    command=lambda: downloader(
        link.get(), 
        format_var.get(), 
        result_label
    )
)
download_btn.pack(pady=1)

# Iniciar el bucle principal
def initApp():
    return root.mainloop()

