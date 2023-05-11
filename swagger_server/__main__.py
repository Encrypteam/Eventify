#!/usr/bin/env python3
import os
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import connexion

from swagger_server import encoder



db = SQLAlchemy()

def main():
    load_dotenv()
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://' + os.getenv('DATABASE_USER') + ':' + os.getenv(
        'DATABASE_PASSWORD') + '@' + os.getenv('DATABASE_URL') + ':' + os.getenv('DATABASE_PORT') + '/' + os.getenv(
        'DATABASE_NAME')
    app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Swagger Eventstore - OpenAPI 3.1'}, pythonic_params=True)
    db.init_app(app.app)
    app.app.app_context().push()
    db.create_all()
    app.run(debug=True, port=os.getenv('PORT'), host='0.0.0.0')
    return app


if __name__ == '__main__':
    main()
