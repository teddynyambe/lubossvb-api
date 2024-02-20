from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Member  # Adjust the import according to your app structure


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

    def create(self, validated_data):
        """Custom creation logic."""
        member = Member.objects.create(**validated_data)
        # Example: send a welcome email or initialize settings
        return member


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    # Temporary field to handle role in view
    role = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'role']

    def create(self, validated_data):
        # Remove role from validated_data as it's not part of the User model
        validated_data.pop('role', None)
        user = User.objects.create_user(**validated_data)
        return user
