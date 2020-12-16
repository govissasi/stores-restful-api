from db import db

# class Usermodel:
class Usermodel(db.Model): 
    __tablename__ = "users"
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))

    # def __init__(self,_id, username, password):
    #     self.id = _id

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def get_by_name(cls,username):
        # con = sqlite3.connect('data.db')
        # cursor = con.cursor()
        # query = "SELECT * FROM users WHERE username=?"
        # result = cursor.execute(query, (username,))
        # row = result.fetchone()
        # if row:
        #     user = cls(*row)
        # else:
        #     user = None

        # con.close()
        # return user

        return cls.query.filter_by(username=username).first()   #SELECT * FROM users WHERE username=username limit 1

    @classmethod
    def get_by_id(cls,_id):
        # con = sqlite3.connect('data.db')
        # cursor = con.cursor()
        # query = "SELECT * FROM users WHERE id=?"
        # result = cursor.execute(query, (_id,))
        # row = result.fetchone()
        # if row:
        #     id = cls(*row)
        # else:
        #     id = None

        # con.close()
        # return id

        return cls.query.filter_by(id=_id).first()   #SELECT * FROM users WHERE id=id limit 1

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
