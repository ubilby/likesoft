from django.urls import include, path

urlpatterns = [
    path('api/books/', include('books.urls')),
    path('api/users/', include('users.urls')),
]
