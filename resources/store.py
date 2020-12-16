from flask_restful import Resource
from models.store import Storemodels

class Store(Resource):
    def get(self,name):
        store = Storemodels.find_name(name)
        if store:
            return store.json(),200     #ok
        return {'message': 'Store not found'},404   #item not found

    def post(self,name):
        if Storemodels.find_name(name):
            return {'message': "A store with name '{}' already exists.".format(name)}, 400  #Bad Request

        store = Storemodels(name)
        try:
            store.save_to_db()
        except:
            return {"message": "An error occurred creating the store."}, 500    #Internal Server Error

        return store.json(), 201    #Created

    def delete(self,name):
        store = Storemodels.find_name(name)
        if store:
            store.delete_from_db()
            return {'message': 'Store deleted'}
        return {'message': 'Store Not found'}

class Storelist(Resource):
    def get(self):
        return {'stores': list(map(lambda x: x.json(), Storemodels.query.all()))}