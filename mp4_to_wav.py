def vid_to_aud():
    import subprocess
    from audio_chunk import aud_chunk
    command="ffmpeg -i static/files/test.mp4 -ar 16000 static/files/audio.wav"
    subprocess.call(command,shell=True)
    return aud_chunk()

#print(vid_to_aud())