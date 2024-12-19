# Product Service

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Product(Resource):
    def get(self):
        return {
            'products': [
                'Product 1',
                'Product 2',
                'Product 3',
                'Product 4',
                'Product 5']
            }
    
api.add_resource(Product, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)