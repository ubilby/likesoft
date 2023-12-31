from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from .serializers import BookSerializer
from .models import Book


class BookViewSet(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [AllowAny]
