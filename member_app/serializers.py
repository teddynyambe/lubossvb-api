from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Member


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'is_active']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['is_active'] = False  # Set user as inactive on creation
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        instance.is_active = validated_data.get(
            'is_active', instance.is_active)
        password = validated_data.get('password')
        if password:
            instance.set_password(password)
        instance.save()
        return instance


class MemberSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Member
        fields = '__all__'
        read_only_fields = ['member_id']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(
            UserSerializer(), validated_data=user_data)
        member = Member.objects.create(user=user, **validated_data)
        return member

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', {})
        UserSerializer.update(
            UserSerializer(), instance=instance.user, validated_data=user_data)
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
