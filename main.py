from flask import Flask
from flask_restful import Api

from controllers.verify_domain import VerifyDomain

app = Flask(__name__)
api = Api(app)

# version 2 apis
api.add_resource(VerifyDomain, "/v2/verify-domain")

if __name__ == "__main__":
    app.run()
