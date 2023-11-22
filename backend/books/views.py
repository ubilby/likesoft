from rest_framework.viewsets import ModelViewSet

from .serializer import BookSerializer
from .models import Book


class BookViewSet(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
