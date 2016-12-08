from flask import Flask, render_template, request, url_for, redirect

from utils import song, upload

app = Flask(__name__)
app.secret_key = 'ajfkdsjflkasd'

@app.route("/")
@app.route("/home/")
def main():
    return render_template("main.html")

@app.route("/s/", methods=["POST"])
def s():
    search = request.form
    image = search["url"]
    keywords = upload.getlist(image)
    lyrics = song.lyrics(keywords)
    return render_template("result.html", tags=keywords)

@app.route("/about/")
def about():
    return render_template("about.html")



if __name__ == '__main__':
    app.debug = True
    app.run()
