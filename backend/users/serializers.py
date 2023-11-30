from rest_framework import serializers

from .models import User
from .utils import send_mail


class UserSerialiser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')

    def create(self, validated_data):
        email = validated_data.get('email')
        user = validated_data.get('user')
        # send_mail.delay(email, user)
        return super().create(validated_data)
