from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import SubscriptionsSerialier, UserSubscriptionSerializer
from .models import Subscriptions, UserSubscription


class SubscriptionsView(generics.CreateAPIView):

    queryset = Subscriptions.objects.all()
    serializer_class = SubscriptionsSerialier
    permission_classes = (IsAuthenticated, IsAdminUser, )
    authentication_classes = (JSONWebTokenAuthentication, )


class ListSubscriptionsView(generics.ListAPIView):

    queryset = Subscriptions.objects.all()
    serializer_class = SubscriptionsSerialier
    authentication_classes = (JSONWebTokenAuthentication, )


class UserSubscriptionView(generics.CreateAPIView):

    queryset = UserSubscription.objects.all()
    serializer_class = UserSubscriptionSerializer
    authentication_classes = (JSONWebTokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DeleteUserSubscription(generics.DestroyAPIView):

    queryset = UserSubscription.objects.all()
    serializer_class = UserSubscriptionSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (JSONWebTokenAuthentication,)


class GetUserSubcription(generics.ListAPIView):

    serializer_class = UserSubscriptionSerializer
    authentication_classes = (JSONWebTokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        try:
            subscriptions = UserSubscription.objects.filter(user=request.user.id)

            data = []

            for items in subscriptions:
                data.append({
                    'subscription_id' : items.id,
                    'subscription_ref' : items.subscription_ref,
                    'subscription_details' : {
                        'name' : items.subscription.subscription_name,
                        'url' : items.subscription.website,
                        'logo' : items.subscription.logo,
                        'catergory' : items.subscription.category,
                        'background_image' : items.subscription.background_image,
                        'description' : items.subscription.description
                    },
                    'description' : items.description,
                    'date_of_subscription' : items.date_of_subscription
                })


            if data == []:
                response = {
                    'success' : 'True',
                    'message' : 'You do not have any subscription',
                    'data' : data
                }
                return Response(response, status=status.HTTP_200_OK)
            
            response = {
                'success' : 'True',
                'message' : 'Subscription list for {} retreived successfully'.format(request.user.username),
                'data' : data
            }
            
            return Response(response, status=status.HTTP_200_OK)
        
        except UserSubscription.DoesNotExist:
            response = {
                "success" : "False",
                "message" : "Invalid Request"
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)