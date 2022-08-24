from django.urls import path, include
from . import views


urlpatterns = [
    
    #admin access only
    path('subscriptions/', views.SubscriptionsView.as_view(), name='add-subscriptions'),
    path('list-publishers/', views.ListSubscriptionsView.as_view(), name='list-publishers'),
    #user access
    path('subscribe/', views.UserSubscriptionView.as_view(), name='subscribe'),
    path('unsubscribe/<int:pk>/', views.DeleteUserSubscription.as_view(), name='unsubscribe'),
    path('get-subscription/', views.GetUserSubcription.as_view(), name='get-subscription'),
]

