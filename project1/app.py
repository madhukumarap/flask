from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, welcome to my Flask project!"

@app.route('/home/<name>')
def home(name):
    # Pass the `name` parameter and a list of names to the template
    return render_template('index.html', current_name=name, names=['name', 'admin'])

if __name__ == '__main__':
    app.run(debug=True)
