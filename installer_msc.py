import yt_dlp

# import whisper

diretorio ='C:/Users/PC/OneDrive/Documentos/Pasta dos scripts/project/automo/Musicas/%(title)s.%(ext)s'
def download_audio(video_url, output_path='audio.mp3'):
    global diretorio
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': diretorio,
        '--cookies-from-browser': True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

# def transcribe_audio(audio_path):
#     model = whisper.load_model("base")
#     result = model.transcribe(audio_path)
#     return result["text"]

download_audio("https://www.youtube.com/watch?v=QmNfa3CtYMI") #video_url = "https://www.youtube.com/watch?v=QmNfa3CtYMI"

# audio_path = ""

# transcription = transcribe_audio(audio_path)

# print("Transcrição:")
# print(transcription)