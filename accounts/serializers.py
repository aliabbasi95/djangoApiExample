from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=32)
    password = serializers.CharField()

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password')
