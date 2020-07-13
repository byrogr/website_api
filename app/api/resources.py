from flask import request, Blueprint
from flask_restful import Api, Resource

from .schemas import ProspectSchema
from ..models.prospect import Prospect

api_v1 = Blueprint('api_v1', __name__)

prospect_schema = ProspectSchema()

api = Api(api_v1)


class ProspectResource(Resource):
    def get(self):
        prospects = Prospect.get_all()
        result = prospect_schema.dump(prospects, many=True)
        return result

    def post(self):
        data = request.get_json()
        cd = prospect_schema.load(data)
        contact = Prospect(
            name=cd.get('name'),
            email=cd.get('email'),
            phone=cd.get('phone'),
            subject=cd.get('subject'),
            message=cd.get('message'))
        contact.save()
        resp = prospect_schema.dump(contact)
        return resp, 201


api.add_resource(ProspectResource, '/api/v1/prospects/',
                 endpoint='prospect_resource')
