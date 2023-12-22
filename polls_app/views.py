
from rest_framework import generics
from .models import Poll, UserResponse
from .serializers import PollSerializer, UserResponseSerializer
from rest_framework.permissions import IsAuthenticated
from .task import send_poll_notification
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, this is the index view.")

class PollListCreateView(generics.ListCreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = [IsAuthenticated]

class PollRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = [IsAuthenticated]

class UserResponseListCreateView(generics.ListCreateAPIView):
    queryset = UserResponse.objects.all()
    serializer_class = UserResponseSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Call the Celery task asynchronously
        send_poll_notification.delay(serializer.validated_data['user_email'])
        serializer.save()

class UserResponseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserResponse.objects.all()
    serializer_class = UserResponseSerializer
    permission_classes = [IsAuthenticated]
