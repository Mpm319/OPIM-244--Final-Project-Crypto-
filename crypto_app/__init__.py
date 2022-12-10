from flask import Flask

from Crypto_App.crypto_routes import crypto_routes



def create_app():
    app=Flask(__name__)

    app.register_blueprint(crypto_routes)


    return app

if __name__=="__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)
    #my_app=create_app()
    #my_app.run(debug=True)
    