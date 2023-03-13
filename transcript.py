'''
import subprocess

command = "ffmpeg -i test.mp4 -ab 160k -ac 2 -ar 16000 -vn audio.wav"

subprocess.call(command, shell=True)
'''


def query(filename):
    import json
    import requests
    headers = {"Authorization": f"Bearer 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"}
    API_URL = "https://api-inference.huggingface.co/models/facebook/wav2vec2-base-960h"
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))


def text(filenames):
    data = ""
    for i in range(0,len(filenames)):
        data = data + " " + query(filenames[i])["text"]
        print(i)
    return data

'''def text(filenames):
    print(query(filenames[0])["text"])
    return
    '''







'''data0 = query("static/files/chunk0.wav")
data1 = query("static/files/chunk1.wav")
print(data0["text"] +" " + data1["text"])'''