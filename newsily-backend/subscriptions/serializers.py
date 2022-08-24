from rest_framework import serializers
from .models import Subscriptions, UserSubscription


class SubscriptionsSerialier(serializers.ModelSerializer):
    
    class Meta:
        model = Subscriptions
        fields = "__all__"



class UserSubscriptionSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source='user.username')
    subscriptions = SubscriptionsSerialier(many=True, read_only=True)
    description = serializers.CharField(max_length=255)

    class Meta:
        model = UserSubscription
        fields = "__all__"
    
    def get_description(self, obj):
        return obj.description