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
        data = request.get_json()
        cd = contact_schema.load(data)
        contact = Contact(
            name=cd.get('name'),
            email=cd.get('email'),
            phone=cd.get('phone'),
            subject=cd.get('subject'),
            message=cd.get('message'))
        contact.save()
        resp = contact_schema.dump(contact)
        return resp, 201


api.add_resource(ContactResource, '/api/v1/contacts/',
                 endpoint='contact_resource')
