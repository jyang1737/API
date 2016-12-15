from flask import Flask, render_template, request, url_for, redirect
import urllib2, os
from utils import song, upload
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'ajfkdsjflkasd'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
@app.route("/")
@app.route("/home/")
def main():
    return render_template("main.html")

@app.route("/s/", methods=["POST"])
def s():
    print request.files
    if 'upload' not in request.files:
        search = request.form
        image = search["URL"]
        try:
            keywords = upload.getlist(image)
        except urllib2.HTTPError:
            return render_template("error.html")
        d = upload.getlistcolors(image)
        if len(d) < 2:
            colora = d[0]
            colorb = "#000000"
        else:
            colora= d[0]
            colorb= d[1]
    else:
        print 'upload sucess'
        try:
            filename = upload_file(request.files)
            keywords = upload.getlistlocal(filename)
            d = upload.getlistlocalcolors(filename)
            if len(d) < 2:
                colora = d[0]
                colorb = "#000000"
            else:
                colora= d[0]
                colorb= d[1]
        except urllib2.HTTPError:
            return render_template("error.html")
        try:
            os.remove("static/" + filename)
        except OSError:
            return render_template("error.html")
    listoftracks = song.get_tracks(keywords)
    dictsong = {}
    for ids in listoftracks:
        dictsong[song.get_title(ids)] = ids
        
    return render_template("result.html", tags=keywords, back_color=colora, song_color=colorb, songdict = dictsong)
def upload_file(r):
    file = r['upload']
    filename = "james.jpg"
    if file.filename == '':
        return render_template("error.html")
    try:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    except IOError:
        return render_template("error.html")
    return filename
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
    app.run(threaded=True)
