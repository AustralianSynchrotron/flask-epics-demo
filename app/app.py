from time import sleep

from flask import Flask, render_template, request
import epics

detector = epics.Device(prefix='SR00DEMO01:', mutable=False,
                        aliases={
                            'model': 'CAM1:Model_RBV',
                            'video_url': 'MPEG1:MJPG_URL_RBV',
                            'gain': 'CAM1:Gain',
                            'acquire': 'CAM1:Acquire',
                        })

app = Flask(__name__)


@app.route('/')
def index():
    video_url = detector.get('video_url', as_string=True)
    return render_template('index.html', detector=detector, video_url=video_url)


@app.route('/configure', methods=['POST'])
def configure():
    data = request.form
    detector.gain = float(data['gain'])
    sleep(.1)
    return 'configured!'


if __name__ == '__main__':
    app.run(debug=True)
