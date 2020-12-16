import sqlite3
from flask_restful import Resource, reqparse
from models.user import Usermodel



class Register(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    def post(self):
        data = Register.parser.parse_args()

        if Usermodel.get_by_name(data["username"]):
            return {"Message " : "User already exists"},400 #Bad Request

        
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()

        # query = "INSERT INTO users VALUES (NULL, ?, ?)"
        # cursor.execute(query, (data['username'], data['password']))

        # connection.commit()
        # connection.close()

        user=Usermodel(**data)
        user.save_to_db()

        return {"message": "User created successfully."}, 201 #created
