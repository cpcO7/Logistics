from celery import shared_task
from django.core.mail import send_mail

from root.settings import EMAIL_HOST_USER


@shared_task
def send_email(email: str | list[str], msg: str, subject: str):
    send_mail(
        subject,
        "",
        EMAIL_HOST_USER,
        (email if isinstance(email, list) else [email]),
        html_message=msg,
        fail_silently=True
    )

    return f'send email to {email} successfully'
