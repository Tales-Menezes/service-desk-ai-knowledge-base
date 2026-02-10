from flask import Flask
from app.routes.upload import upload_bp

def create_app():
    flask_app = Flask(__name__)
    flask_app.register_blueprint(upload_bp)
    return flask_app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
