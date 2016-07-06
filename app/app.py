from time import sleep

from flask import Flask, render_template, request, redirect
from flask_httpauth import HTTPBasicAuth
from flask_bootstrap import Bootstrap
import epics


detector = epics.Device(prefix='SR00DEMO01:', mutable=False,
                        aliases={
                            'model': 'CAM1:Model_RBV',
                            'video_url': 'MPEG1:MJPG_URL_RBV',
                            'gain': 'CAM1:Gain',
                            'acquire': 'CAM1:Acquire',
                        })

app = Flask(__name__)
auth = HTTPBasicAuth()
Bootstrap(app)

# Needed after Flask-Bootstrap is added to preserve auto-reload functionality
app.jinja_env.auto_reload = True


@auth.get_password
def get_password(username):
    return '1234'


@app.route('/')
def index():
    video_url = detector.get('video_url', as_string=True)
    return render_template('index.html', detector=detector, video_url=video_url)


@app.route('/configure', methods=['POST'])
@auth.login_required
def configure():
    data = request.form
    detector.gain = float(data['gain'])
    detector.acquire = 1 if 'acquire' in data else 0
    sleep(.1)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
