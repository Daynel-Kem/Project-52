import yt_dlp
import os, zipfile, io, shutil

def youtube_playlist_to_mp3(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'playlists/%(playlist_title)s/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'ignoreerrors': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as dlp:
        dlp.download([url])
        info = dlp.extract_info(url, download=False)
        return info["title"]


def create_zip_from_folder(folder_path):
    zip_buffer = io.BytesIO()

    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, folder_path)
                zipf.write(full_path, rel_path)

    zip_buffer.seek(0)

    shutil.rmtree(folder_path)

    return zip_buffer