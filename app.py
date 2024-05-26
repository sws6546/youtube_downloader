from flask import Flask, render_template, request, send_file
from pytube import YouTube

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/download', methods=['GET'])
def download():
    url = request.args.get('url')
    YouTube(f'{url}').streams.first().download("static", filename="video.mp4")
    return send_file("static/video.mp4", as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)