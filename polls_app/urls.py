
from django.urls import path
from .views import PollListCreateView, PollRetrieveUpdateDestroyView, UserResponseListCreateView, UserResponseRetrieveUpdateDestroyView
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    path('api-token-auth/', ObtainAuthToken.as_view(), name='api_token_auth'),
    path('polls/', PollListCreateView.as_view(), name='poll-list-create'),
    path('polls/<int:pk>/', PollRetrieveUpdateDestroyView.as_view(), name='poll-retrieve-update-destroy'),
    path('responses/', UserResponseListCreateView.as_view(), name='user-response-list-create'),
    path('responses/<int:pk>/', UserResponseRetrieveUpdateDestroyView.as_view(), name='user-response-retrieve-update-destroy'),
]
