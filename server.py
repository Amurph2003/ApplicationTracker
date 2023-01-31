from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS
from api.applying import Applications, Login
from db.dbfunc import connectToServer

app = Flask(__name__)
CORS(app)
api = Api(app)

# api.add_resource(Companies, '/companies')
api.add_resource(Applications, '/<int:uid>/applications')
api.add_resource(Login, '/login')

if __name__ == '__main__':
    app.run(port=5001)
    app.run(debug=True)