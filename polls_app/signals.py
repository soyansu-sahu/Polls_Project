
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserResponse
from .task import send_poll_notification

@receiver(post_save, sender=UserResponse)
def send_notification_on_poll_completion(sender, instance, **kwargs):
    # Send email notification when a user responds to a poll
    send_poll_notification.delay(instance.user_email)
