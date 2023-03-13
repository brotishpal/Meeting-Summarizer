'''import librosa
import soundfile as sf

input_file = "static/files/audio.wav"
stream = librosa.stream(
    input_file,
    block_length=60,
    frame_length = 16000,
    hop_length = 16000
)

for i, speech in enumerate(stream):
  sf.write(f'static/files/chunk{i}.wav',speech,16000)
'''
def aud_chunk():
  import librosa
  import soundfile as sf

  input_file = "static/files/audio.wav"
  stream = librosa.stream(
      input_file,
      block_length=60,
      frame_length = 16000,
      hop_length = 16000
  )

  filename = []
  for i, speech in enumerate(stream):
    filename.append('static/files/chunk'+str(i)+'.wav')
    sf.write(filename[i],speech,16000)
  
  #from transcript import text
  from trans_text import text

  return text(filename)

  '''from transcript import query
  data = ""
  for i, speech in enumerate(stream):
    filename = "static/files/chunk" + str(i) + ".wav"
    data = data + " " + query(filename)["text"]
    print(i + "/n"+query(filename)["text"]+"/n")
  return
'''
#print(aud_chunk())