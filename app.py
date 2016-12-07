from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)
app.secret_key = 'ajfkdsjflkasd'

@app.route("/")
@app.route("/home/")
def main():
    return render_template("main.html")

@app.route("/s/", methods=["POST"])
def query():
    response = request.form
    image = response["img"]
    return render_template("navbar.html")

@app.route("/s/<song>")
def song(song):
    return render_template("main.html")


@app.route("/about/")
def about():
    return render_template("about.html")



if __name__ == '__main__':
    app.debug = True
    app.run()
