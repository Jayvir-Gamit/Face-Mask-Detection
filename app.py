from templates import webCamera
from templates import deviceVideo

from flask import Flask, render_template, Response, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/webCam')
def webCam():
    return Response(webCamera.generateFrames(), mimetype='multipart/x-mixed-replace; boundary=frame')



# External Video on web screen
ALLOWED_EXTENSIONS = ['mp4']

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# video = 0
@app.route('/upload', methods=['POST'])
def upload():
    if 'video' not in request.files:
        return 'No video file found'
    video = request.files['video']
    if video.filename == '':
        return 'No video selected'
    if video and allowed_file(video.filename):
        video.save('static/videos/' + video.filename)
        # video_name = deviceVideo.generateFrames2(video.filename)
        # return render_template('preview.html',video_name=video.filename)
        return Response(deviceVideo.generateFrames2(video.filename), mimetype='multipart/x-mixed-replace; boundary=frame')
        # return Response(setSRC)
        # return render_template("index.html")
    return 'Invalid video file'

@app.route('/setSRC')
def setSRC():
    video = request.files['video']
    return Response(deviceVideo.generateFrames2(video.filename), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug="true")
