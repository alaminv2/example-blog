from rest_framework import viewsets
from .serializers import CustomUserSerializer
from authentication.models import CustomUser

# Create your views here.


class CustomUserViewSet(viewsets.ModelViewSet):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
