from pytube import YouTube
Yt = YouTube("https://youtu.be/HoCwa6gnmM0?si=5hNMQklh_yXT580Z")
print("The stream is avalabile", Yt.streams.all())
video = Yt.streams.first()
video.download("D:\ME\OH")
