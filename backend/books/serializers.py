from rest_framework import serializers

from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'author', 'year', 'isbn')

    def validate(self, data):
        title = data.get('title')
        author = data.get('author')
        year = data.get('year')
        if Book.objects.filter(
            title=title,
            author=author,
            year=year
        ).exists():
            raise serializers.ValidationError(
                "Такая книга уже существует!"
            )
        return data

    def validate_isbn(self, value):
        if len(value) != 13 or not value.isdigit():
            raise serializers.ValidationError(
                "Некорректный ISBN"
            )
        return value
