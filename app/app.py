from flask import Flask, render_template
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
    return render_template('index.html', detector=detector)


if __name__ == '__main__':
    app.run(debug=True)
