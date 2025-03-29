from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': False}}  # Prevents password from being exposed in responses

    def create(self, validated_data):
        print("🔍 Debug: Creating user with hashed password...")
        user = User(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])  # Ensure password is hashed
        user.save()
        print("✅ Password stored as:", user.password)  # Check if it's hashed
        return user
