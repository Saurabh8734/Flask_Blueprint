from flask import Flask
from blueprints.helloworld.helloworld import helloworld_bp

app = Flask(__name__)
app.register_blueprint(helloworld_bp)


if __name__ == "__main__":
    app.run(debug=True)