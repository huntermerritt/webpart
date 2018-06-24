from flask import Flask, render_template, request, url_for
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/enterprise')
def enterprise():
    return render_template('enterprise.html')

@app.route('/successfulsignup', methods=['POST'])
def createbusiness():

    return render_template('success.html')

if __name__ == '__main__':
    app.run()
