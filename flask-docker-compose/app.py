import os
from flask import Flask

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URL"] = os.getenv("DATABASE_URL")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

@app.route("/")
def hello():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
