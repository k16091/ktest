#1.import package flask
import flask

#2.create object
app = flask.Flask(__name__)

#3.add url
@app.route('/', methods=['GET'])
def home():
    return "Welcome to Web API"

#4.run applications
app.run()
