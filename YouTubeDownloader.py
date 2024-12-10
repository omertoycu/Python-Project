import yt_dlp

url = input("Enter a video URL: ")
path = "C:\\Users\\omerf\\PycharmProjects\\YouTubeDownloader"

ydl_opts = {
    'outtmpl': f'{path}/%(title)s.%(ext)s',
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
