import moviepy.editor

video = moviepy.editor.VideoFileClip("zarazarafbdownload.mp4")

audio = video.audio
audio.write_audiofile("extractedmp3song.mp3")