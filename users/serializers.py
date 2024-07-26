from rest_framework import serializers

from django.core.validators import EmailValidator

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[EmailValidator()])

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password']
