from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('shashank.html')

@app.route('/submit')
def shashank():
    return render_template('dbdb.html')

app.run(debug=True)