from rembg import remove
from flask import Flask, request, render_template, redirect, send_from_directory
from time import time

app = Flask(__name__)


@app.get('/')
def index():
    return render_template("index.html")


@app.route('/removed/<path:path>')
def send_report(path):
    return send_from_directory('removed', path)


@app.post('/remove-bg')
def remove_bg():
    if request.files.get('inp') == None:
        return "please provide the image with inp key"
    f = request.files['inp']
    inp = f.stream.read()
    path = 'removed/no_bg-' + str(int(time())) + \
        "-" + f.filename.split(".")[0] + ".png"
    with open(path, "wb") as o:
        o.write(remove(inp))

    return redirect(path)


if __name__ == "__main__":
    app.run(debug=True, port=3000)
