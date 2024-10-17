import os
import yt_dlp

# Directorio de salida
output_dir = "Descargas"

def downloader(video_url, select_format, result_label):
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
