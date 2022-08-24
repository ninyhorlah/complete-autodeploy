from django.urls import path, include
from . import views


urlpatterns = [
    path('signup/', views.UserRegistrationView.as_view(), name='signup'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('admin-list-user/', views.AdminListUserView.as_view()),
    path('repubblica/', views.SetCookiesRepubblica.as_view())
]