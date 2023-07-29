from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator

User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
                  validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        max_length=32, validators=[UniqueValidator(queryset=User.objects.all())]
                                     )
    password = serializers.CharField()

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password')
