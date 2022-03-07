from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "WELCOME TO THE BHANU PRAKASH WORLD"

if __name__ == "__main__":
    application.run()
