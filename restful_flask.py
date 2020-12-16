from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate,identity
from resources.user import Register
from resources.items import Item,Itemlist
from resources.store import Store,Storelist #import store list

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' #To tell SQlAlchemy to db location
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False    #To stop to track modifications of objects and save storage
app.secret_key = "mine"
api=Api(app)

#MOVE TO RUN.PY FILE
# @app.before_request
# def table():
#     db.create_all()


jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(Item,"/Item/<string:name>")
api.add_resource(Itemlist,"/Items")
api.add_resource(Register,"/register")
api.add_resource(Storelist,"/stores")
api.add_resource(Store,"/Store/<string:name>")
if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True)



