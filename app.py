## author: https://dev.to/arjunpraveen2008/create-a-simple-web-app-with-python-and-flask-in-5-minutes-22kd
# app.py
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    # return "Hello, world!"
    return render_template('index.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
