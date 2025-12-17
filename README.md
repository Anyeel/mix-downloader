# MP3 Downloader

Este proyecto es una herramienta automatizada desarrollada en **Python** que permite descargar listas de reproducción o videos individuales de YouTube y convertirlos directamente a formato **MP3**.

Utiliza `yt-dlp` para gestionar las descargas y `FFmpeg` para la conversión de audio.

## 🚀 Características
* **Soporte de Listas de Reproducción:** Descarga mixes completos con un solo enlace.
* **Conversión Automática:** Transforma el audio a MP3 (192kbps por defecto).
* **Nomenclatura Limpia:** Organiza los archivos automáticamente usando el título original del video.

## 🛠️ Requisitos Previos

Antes de ejecutar el script, asegúrate de tener instalado:

1.  **Python 3.8+**

2.  **FFmpeg:**
    * *Windows:* `choco install ffmpeg` o descarga el binario oficial.
    * *macOS:* `brew install ffmpeg`
    * *Linux:* `sudo apt install ffmpeg`

## 📦 Instalación

1.  **Clona este repositorio:**
    ```bash
    git clone https://github.com/Anyeel/mix-downloader.git
    cd mix-downloader
    ```

2.  **Crea y activa un entorno virtual:**
    ```bash
    python -m venv venv
    # Windows
    .\venv\Scripts\activate
    # Mac/Linux
    source venv/bin/activate
    ```

3.  **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

## ⚙️ Uso

1.  Ejecuta el script principal:
    ```bash
    python downloader.py
    ```

2.  Cuando el programa lo solicite, pega la URL del Mix o video de YouTube.

3.  Busca tus archivos en la carpeta creada automáticamente: `/Descargas`.

## Enlace Post

Click aquí para apoyarme. Se agradece un me gusta. <3
