from flask import flask

from crypto_app.crypto_routes import crypto_routes


def create_app():
    app=flask(__name__)

    app.register_blueprint(crypto_routes)

    return app

if __name__=="__main__":
    my_app=create_app()
    my_app.run(debug=True)
    