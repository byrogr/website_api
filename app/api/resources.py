from flask import request, Blueprint
from flask_restful import Api, Resource

from .schemas import ProspectSchema
from ..models.prospect import Prospect
from ..services.mail_service import new_prospect_mail

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
        ps = prospect_schema.load(data)
        prospect = Prospect(
            name=ps.get('name'),
            email=ps.get('email'),
            phone=ps.get('phone'),
            subject=ps.get('subject'),
            message=ps.get('message'))
        prospect.save()
        new_prospect_mail(prospect)
        resp = prospect_schema.dump(prospect)
        return resp, 201


api.add_resource(ProspectResource, '/api/v1/prospects/',
                 endpoint='prospect_resource')
