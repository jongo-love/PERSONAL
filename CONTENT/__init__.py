#This is where we initialize the flask application. LOL TSCHUSS
from flask import Flask
def CREATE_APP():
    app=Flask(__name__)

    #Here I'm importing.
    from .views import views
    from .auth import auth
    #register the blueprints.
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    

    return app