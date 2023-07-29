from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
import django.contrib.auth.password_validation as validators

User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField(
        max_length=32, validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(validators=[validators.validate_password])

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password')
