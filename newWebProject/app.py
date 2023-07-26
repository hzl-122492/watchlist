from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>你好 迪西!</h1><img src="http://helloflask.com/totoro.gif">'