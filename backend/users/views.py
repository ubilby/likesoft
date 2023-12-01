from rest_framework.viewsets import ModelViewSet

from .serializers import UserSerialiser
from .models import User


class UserViewSet(ModelViewSet):
    serializer_class = UserSerialiser
    queryset = User.objects.all()
    http_method_names = ['post']
