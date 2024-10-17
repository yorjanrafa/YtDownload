import customtkinter as ctk
import yt_dlp
import os
import tkinter as tk  # Importar tkinter

# Configurar ventana principal
ctk.set_appearance_mode("light")  # Opciones: "light", "dark"
ctk.set_default_color_theme("green")  # Cambiar el tema de color
root = ctk.CTk()
root.geometry('500x380')
root.resizable(0, 0)
root.title("YouTube Downloader & Converter")

# Crear un marco con padding usando tk.Frame
frame = tk.Frame(root)
frame.pack(expand=True, fill='both', padx=50, pady=40)  # Padding aquí

# Título
title_label = ctk.CTkLabel(frame, text='YouTube Video Downloader', font=('Arial', 20, 'bold'))
title_label.pack(pady=25)

# Campo para el link de YouTube
link = ctk.StringVar()
link_label = ctk.CTkLabel(frame, text='Pega el link de YouTube aquí:', anchor='w')  # Alinear a la izquierda
link_label.pack(pady=1, anchor='w')
link_entry = ctk.CTkEntry(frame, width=0, textvariable=link)  # Ancho automático
link_entry.pack(pady=10, fill='x')  # Llenar el ancho disponible

# Opciones de formato
format_var = ctk.StringVar(value="mp3")
# link_label.pack(pady=50, anchor='w')
format_label = ctk.CTkLabel(frame, text='Formato de salida:', font=('Times New Roman', 15), anchor='w')  # Alinear a la izquierda
format_label.pack(pady=1, anchor='w')
format_combo = ctk.CTkComboBox(frame, variable=format_var, values=["mp3", "flac", "aac"])
format_combo.pack(pady=1, fill='x')  # Llenar el ancho disponible

# Directorio de salida
output_dir = "Descargas"

# Función para descargar el video de YouTube
def downloader():
    video_url = str(link.get())
    select_format = format_var.get()
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': select_format,
            'preferredquality': '192',
        }]
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        result_label.configure(text='DESCARGADO', text_color='green')  # Cambiado a configure
    except Exception as e:
        result_label.configure(text='ERROR EN DESCARGA', text_color='red')  # Cambiado a configure

# Etiqueta para mostrar resultados
result_label = ctk.CTkLabel(frame, text='')
result_label.pack(pady=1)

# Botón para descargar
download_btn = ctk.CTkButton(frame, text='DESCARGAR', command=downloader)
download_btn.pack(pady=1)

# Iniciar el bucle principal
def initApp():
    return root.mainloop()


