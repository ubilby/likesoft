from celery import shared_task
from django.core.mail import send_mail


@shared_task
def token_to_email(email, user):
    send_mail(
        f'Hello {user}',
        [email],
        fail_silently=False,
    )
