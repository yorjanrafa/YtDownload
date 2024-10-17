import os
import yt_dlp

def downloader(link, format, output_dir, result_label):
    video_url = str(link)
    select_format = format
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
        result_label.configure(text='ERROR EN DESCARGA', text_color='red')  # 
