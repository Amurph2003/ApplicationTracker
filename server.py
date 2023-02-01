from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS
from api.applying import Application, Login, Overview
from db.dbfunc import connectToServer

app = Flask(__name__)
CORS(app)
api = Api(app)

# api.add_resource(Companies, '/companies')
api.add_resource(Application, '/<int:uid>/application')
api.add_resource(Login, '/login')
api.add_resource(Overview, '/overview/<int:uid>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
    app.run(debug=True)