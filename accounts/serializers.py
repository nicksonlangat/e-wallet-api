from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    # wallet = 
    class Meta:
        model = get_user_model()
        fields = [
            "id", "email", "first_name",
            "last_name","phone_number",
             "profile_image","date_joined",
            "is_superuser", "is_staff",
            "is_active",
        ]
    
    # def get_wallet(self, obj):
    #     id = obj['id']


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["email", "first_name", "last_name", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        user = get_user_model()(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user


