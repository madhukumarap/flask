from flask import Flask, redirect, url_for, render_template


app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hello welcome to the my flask project"

@app.route('/home/<name>')
def home(name):
    return render_template('index.html', name=name)
if __name__ == '__main__':
    app.run(debug=True)