from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS
from api.applying import Applications, SpecificApp
from db.dbfunc import connectToServer

app = Flask(__name__)
CORS(app)
api = Api(app)

# api.add_resource(Users, '/users')
api.add_resource(Applications, '/applications')
api.add_resource(SpecificApp, '/applications/<int:id>')
# api.add_resource()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
    app.run(debug=True)