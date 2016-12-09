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
    colora= upload.getlistcolors(image)[0]
    colorb = upload.getlistcolors(image)[1]
    name = song.get_title(keywords)
    artist = song.get_artist(keywords)
    return render_template("result.html", tags=keywords, songname=name, songartist=artist, songlyrics=lyrics, back_color=colora, song_color=colorb)

@app.route("/about/")
def about():
    return render_template("about.html")



if __name__ == '__main__':
    app.debug = True
    app.run()
