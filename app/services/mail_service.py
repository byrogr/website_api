from smtplib import SMTPException
from threading import Thread

from flask import current_app, render_template
from flask_mail import Message

from ..ext import mail


def _send_async_mail(app, msg):
    with app.app_context():
        try:
            mail.send(msg)
        except SMTPException:
            print("Ocurrio un error al enviar el email")


def new_prospect_mail(prospect):
    subject = f'¡Atención! Nuevo prospecto {prospect.id}'
    sender = ('RMSolutions', 'no-reply@rmsolutions.pe')
    recipents = ["venta@rmsolutions.pe"]
    html = render_template('emails/new_prospect.html', prospect=prospect)
    msg = Message(subject, recipents, sender=sender)
    msg.html = html
    Thread(target=_send_async_mail, args=(current_app._get_current_object(), msg)).start()
