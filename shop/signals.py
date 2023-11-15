from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from shop.models import Client
import os

@receiver(post_save, sender=Client)
def send_notification_email(sender, instance, created, **kwargs):
    if created:
        subject = 'Added new client'
        template_path = 'email/new_client_notification.html'
        try:
            template = get_template(template_path)
            message = template.render({'client': instance})
        except Exception as e:
            print(f"Failed to load template at path: {template_path}")
            print(f"Error: {e}")
            return

        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = settings.DEFAULT_TO_EMAIL

        email = EmailMultiAlternatives(subject, body=message, from_email=from_email, to=[to_email])
        email.attach_alternative(message, "text/html")

        try:
            email.send()
            print(f"Email sent successfully to {to_email}")
        except Exception as e:
            print(f"Failed to send email. Error: {e}")