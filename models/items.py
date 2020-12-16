#import sqlite3 No need to import
from db import db

# class Itemmodels:
class Itemmodels(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer,db.ForeignKey("store.id"))
    store = db.relationship("Storemodels")
    
    # def __init__(self,name,price):
    def __init__(self,name,price,store_id): #include Store_id
        self.store_id=store_id
        self.name=name
        self.price=price
        
    def json(self):
        #return {"name":self.name ,"price":self.price}
        return {"name":self.name ,"price":self.price,"store ID":self.store_id}
    
    @classmethod
    def find_name(cls, name):
        # con= sqlite3.connect('data.db')
        # cursor = con.cursor()

        # query = "SELECT * FROM items WHERE name=?"
        # result = cursor.execute(query, (name,))
        # row = result.fetchone()
        # con.close()
        # if row:
        #     return cls(*row)

        return cls.query.filter_by(name=name).first()   #Select * from items where name=name limit 1

    # def insert(self):
    #     con= sqlite3.connect('data.db')
    #     cursor = con.cursor()

    #     query = "Insert into items values (?,?)"
    #     cursor.execute(query, (self.name,self.price))
    #     con.commit()
    #     con.close()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    # def update(self):
    #     con= sqlite3.connect('data.db')
    #     cursor = con.cursor()
    #     query = "update items set price=? where name=? "
    #     cursor.execute(query, (self.price,self.name))
    #     con.commit()
    #     con.close()

    def delete_to_db(self):
        db.session.delete(self)
        db.session.commit()