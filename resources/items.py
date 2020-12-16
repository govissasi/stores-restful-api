import sqlite3
from flask import Flask
from flask_restful import Resource,reqparse
from flask_jwt import jwt_required

from models.items import Itemmodels

class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('price',
             type=float,
             required=True,
             help="Price cannot be left blank!"
        )
    #include store id
    parser.add_argument('store_id',
             type=float,
             required=True,
             help="Item must be store id"
        )

    @jwt_required()
    def get(self,name): # /item/<string:name>    
        item = Itemmodels.find_name(name)
        
        if item:
            #return item,200 #Ok
            return item.json(),200 #Ok
        return {"Message":"Item not found"},404 #Not found

    

    def post(self,name): # /item/<string:name>       
        if Itemmodels.find_name(name):
            return ("message","Already item {} exsists".format(name)),400 #Bad request

        data=Item.parser.parse_args()
        #item={"name":name,"price":data["price"]}
        #item=Itemmodels(name,data["price"])
        #item=Itemmodels(name,data["price"],data["store_id"]) #Include store id
        item=Itemmodels(name,**data)

        try:
            #Itemmodels.insert(item)
            #item.insert()
            item.save_to_db() # insert mtd change to save_to_db mtd
        except:
            return {"message":"Can't insert item"},500 #Internal server Error

        #return item,201 #created
        return item.json(),201 #created
    
    
    
    def delete(self,name):   # /item/<string:name>
        # if Itemmodels.find_name(name):
        #     con= sqlite3.connect('data.db')
        #     cursor = con.cursor()

        #     query = "Delete from items where name =?"
        #     cursor.execute(query, (name,))
        #     con.commit()
        #     con.close()
        #     return {"Message":"Item Deleted"}
        # return {"Message":"Item not found"}
        item = Itemmodels.find_name(name)
        if item:
            item.delete_to_db()
            return {"Message":"Item Deleted"}
        return {"Message":"Item not found"}



    def put(self,name):
        data=Item.parser.parse_args()
        item = Itemmodels.find_name(name)
        #update_item = {'name': name, 'price': data['price']}
        #update_item = Itemmodels(name,data['price'])

        if item:
            # try:
            #     update_item.update()
            # except:
            #     return {"Message":"Error occur when update item {}".format(name)}

            item.price = data["price"]
        else:
            # try:
            #     update_item.insert()
            # except:
            #     return {"Message":"Error occur when Insert item {}".format(name)}

            # item = Itemmodels(name,data["price"])
            item=Itemmodels(name,**data) #include store id
        
        #return update_item    
        #return update_item.json()
        item.save_to_db()
        return item.json()


class Itemlist(Resource):
    def get(self):  # /Items
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()

        # query = "SELECT * FROM items"
        # result = cursor.execute(query)
        # items = []
        # for row in result:
        #     items.append({'name': row[0], 'price': row[1]})
        # connection.close()

        # return {'items': items}

        # return {"items":Itemmodels.query.all()}
        #return {"items":item.json() for item in Itemmodels.query.all()}
        return {"items":list(map(lambda x: x.json(),Itemmodels.query.all()))}
