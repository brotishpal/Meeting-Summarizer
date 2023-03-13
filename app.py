from flask import Flask, render_template, url_for
from flask import request as req
import requests
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
from title import heading
import os
from mp4_to_wav import vid_to_aud

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/files'

class UploadFileForm(FlaskForm):
    file = FileField("File")
    submit = SubmitField("Upload File")

@app.route("/",methods = ["GET","POST"])
@app.route("/File", methods = ["GET","POST"])

#File Upload


def Index():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename("test.mp4")))
        output=vid_to_aud()
        #print(app.config['UPLOAD_FOLDER']+"/"+file.filename)
        #print(output)
        return render_template("index.html",output=output,form=form)
    return render_template("index.html",form=form)


#Summarization
@app.route("/Summarize", methods = ["GET","POST"])

def Summarize():
    form1 = UploadFileForm()
    if req.method=="POST":
        API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
        headers = {"Authorization": f"Bearer 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"}

        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()

        data = req.form["data"]

        maxL = int(req.form["maxL"])
        minL = maxL//4
        output = query({
            "inputs": data,
            "parameters": {"min_length": minL,"max_length": maxL},
        })[0]["summary_text"]

        return render_template("index.html",result = heading(output),form=form1,output=data)
    else:
        return render_template("index.html",form=form1,output=data)
        

'''@app.route("/File", methods = ["GET","POST"])
def fileUpload():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
        return "File has been uploaded"
    return render_template("index.html",form=form)
'''


if __name__ == "__main__":
    app.debug = True
    app.run()