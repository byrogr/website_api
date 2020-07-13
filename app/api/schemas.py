from marshmallow import fields
from app.ext import ma


class ProspectSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()
    email = fields.String()
    phone = fields.String()
    subject = fields.String()
    message = fields.String()
