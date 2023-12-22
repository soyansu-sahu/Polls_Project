
from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_poll_notification(email):
    send_mail(
        'Poll Notification',
        'Thank you for participating in the poll!',
        'from@example.com',
        [email],
        fail_silently=False,
    )
