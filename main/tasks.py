from django.core.mail import send_mail

from main.models import Contact
from send_email.celery import app


@app.task
def send_email(email):
    send_mail(
        'Вы зарегистрировалис в этой херне и каждую минуту будете получать спам',
        'Thank you for contacting us. We will get back to you as soon as possible.',
        'testtesttesttesttesttes0@gmail.com',
        [email],
        fail_silently=False,
    )

@app.task
def send_beat_email():
    for contact in Contact.objects.all():
        send_mail(
            'прошло 1 минута',
            'sdf',
            'testtesttesttesttesttes0@gmail.com',
            [contact.email],
            fail_silently=False,
        )