import yt_dlp
import os

def descargar_mix(url):
    # Carpeta de destino
    output_folder = 'Descargas'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Configuración de yt-dlp
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': f'{output_folder}/%(title)s.%(ext)s',
        'yes_playlist': True, # Cambiar a False si solo se quiere un video
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            print(f"Iniciando descarga: {url}")
            ydl.download([url])
            print("\n¡Descarga completada con éxito!")
        except Exception as e:
            print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    link = input("Pega el link del Mix o Video de YouTube: ")
    descargar_mix(link)