from app.db import db, BaseModelMixin


class Contact(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(180))
    email = db.Column(db.String)
    phone = db.Column(db.String(9), nullable=True)
    subject = db.Column(db.String)
    message = db.Column(db.Text)

    def __init__(self, name, email, phone, subject, message):
        self.name = name
        self.email = email
        self.phone = phone
        self.subject = subject
        self.message = message

    def __repr__(self):
        return f'Contact{self.name}'

    def __str__(self):
        return f'{self.name}'
