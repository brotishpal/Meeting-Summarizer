'''
import requests

API_URL = "https://api-inference.huggingface.co/models/openai/whisper-large-v2"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

output = query("sample1.flac")
'''
def query(filename):
    import json
    import requests
    headers = {"Authorization": f"Bearer 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"}
    API_URL = "https://api-inference.huggingface.co/models/openai/whisper-large-v2"
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))


def text(filenames):
    data = ""
    for i in range(0,len(filenames)):
        data = data + " " + query(filenames[i])["text"]
        print(i)
    from delete import clean
    clean()
    return data
