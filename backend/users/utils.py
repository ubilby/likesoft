from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_hello(email, user):
    send_mail(
        'Greeting',
        f'Hello {user}',
        'administrator@likesoft.ru',
        [email],
        fail_silently=False,
    )
