from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/music")
def music():
    return send_from_directory("static/music/", "music.mp3")

@app.route("/gif")
def gif():
    return send_from_directory("static/gif/", "tree-animation.gif")

def main():
    app.run(debug=False)

if __name__ == '__main__':
    main()