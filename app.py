from flask import Flask
from application import create_app
from dotenv import load_dotenv


load_dotenv()

app = create_app()




if __name__ == "__main__":
    app.run(debug=False)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"