from django.urls import include, path

urlpatterns = [
    path('api/books/', include('books.urls')),
]
