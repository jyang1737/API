from flask import Flask, render_template, request, url_for, redirect

from utils import song, upload

app = Flask(__name__)
app.secret_key = 'ajfkdsjflkasd'

@app.route("/")
@app.route("/home/")
def main():
    return render_template("form_v2.html")

@app.route("/s/", methods=["POST"])
def s():
    search = request.form
    image = search["url"]
    keywords = upload.getlist(image)
    colora= upload.getlistcolors(image)[0]
    colorb = upload.getlistcolors(image)[1]
    listoftracks = song.get_tracks(keywords)
    dictsong = {}
    for ids in listoftracks:
        dictsong[song.get_title(ids)] = ids
            
    return render_template("result.html", tags=keywords, back_color=colora, song_color=colorb, songdict = dictsong)


@app.route("/s/<sid>", methods=["GET"])
def songinfo(sid):
    backcolor = "#" + request.args.get("back_color")
    songcolor = "#" + request.args.get("song_color")
    return render_template("song.html",lyrics= song.get_lyrics(sid), title = song.get_title(sid), artist = song.get_artist(sid), back_color = backcolor, song_color = songcolor) 

@app.route("/about/")
def about():
    return render_template("about.html")



if __name__ == '__main__':
    app.debug = True
    app.run()
