from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
import uuid

User = get_user_model()

class Subscriptions(models.Model):

    CHOICES = (
        ('general', 'General'),
        ('finance', 'Finance'),
        ('sports', 'Sports'),
    )
    
    subscription_name = models.CharField(max_length=255)
    category = models.CharField(choices=CHOICES, max_length=10, default='general')
    description = models.TextField(max_length=1000)
    background_image = models.URLField(default="https://img")
    logo = models.URLField()
    website = models.URLField()
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.subscription_name


class UserSubscription(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    subscription_ref = models.UUIDField(default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=255, default='description')
    subscription = models.ForeignKey(Subscriptions, related_name='subscriptions', on_delete=models.CASCADE)
    date_of_subscription = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = (
            "-date_of_subscription",
            "user",
        )

    def __str__(self):
        return "Subscription to {} made by {} on {}.".format(self.subscription.subscription_name, 
                                                            self.user, 
                                                            self.date_of_subscription)