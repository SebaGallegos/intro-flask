# Init file to execute app
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Hola mundo"

# example with bootstrap in a html file
@app.route("/1")
def firstpage():
    return render_template('1/index.html')

if __name__ == "__main__":
    app.run(debug=True)
