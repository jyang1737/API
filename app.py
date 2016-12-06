from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route("/")
@app.route("/home/")
def main():


@app.route("/s/<query>", methods=["GET","POST"])
def query(query):


@app.route("/s/<song>")
def song(song):




if __name__ == '__main__':
    app.debug = True
    app.run()
