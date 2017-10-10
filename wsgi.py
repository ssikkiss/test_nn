from flask import Flask
import mynn
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    application.run()
