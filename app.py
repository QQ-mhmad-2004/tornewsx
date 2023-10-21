from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)


def generate_frames():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            if ret:
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def mhmad():
    return render_template('index.html')




@app.route('/mhmad')
def index():
    return """
    <html>
    <head>
        <title>Camera Stream</title>
    </head>
    <body>
        <h1>تم فتح الكامرة</h1>
        <img src="/video_feed" width="640" height="480">
        <div>helo mhmad</div>
    </body>
    </html>
    """


@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
