from flask import Flask, render_template, request, url_for, redirect
import urllib2, os
from utils import song, upload
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/static'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'ajfkdsjflkasd'

@app.route("/")
@app.route("/home/")
def main():
    return render_template("form_v2.html")

@app.route("/s/", methods=["POST"])
def s():
    if 'file' not in request.files:
        search = request.form
        image = search["URL"]
        try:
            keywords = upload.getlist(image)
        except urllib2.HTTPError:
            return render_template("error.html")
        colora= upload.getlistcolors(image)[0]
        colorb = upload.getlistcolors(image)[1]

    else:
        file = request.files['file']
        if file.filename == '':
            return render_template("error.html")
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))       
            keywords = upload.getlistlocal(filename)
            colora= upload.getlistlocalcolors(filename)[0]
            colorb = upload.getlistlocalcolors(filename)[1]
    
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
