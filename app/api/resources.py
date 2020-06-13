from flask import request, Blueprint
from flask_restful import Api, Resource

from .schemas import ContactSchema
from ..models.contact import Contact

api_v1 = Blueprint('api_v1', __name__)

contact_schema = ContactSchema()

api = Api(api_v1)


class ContactResource(Resource):
    def get(self):
        contacts = Contact.get_all()
        result = contact_schema.dump(contacts, many=True)
        return result

    def post(self):
        pass


api.add_resource(ContactResource, '/api/v1/contacts/',
                 endpoint='contact_resource')
