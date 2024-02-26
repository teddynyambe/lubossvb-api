from rest_framework import serializers
from .models import Declaration
from member_app.serializers import MemberSerializer
from member_app.models import Member


class DeclareSerializer(serializers.ModelSerializer):
    # Use the MemberSerializer to represent the member_id field
    member_first_name = serializers.SerializerMethodField()
    member_last_name = serializers.SerializerMethodField()
    member = serializers.PrimaryKeyRelatedField(queryset=Member.objects.all())

    class Meta:
        model = Declaration
        fields = '__all__'

    def get_member_first_name(self, obj):
        # Safely get the first name if the member exists
        return obj.member.first_name if obj.member else None

    def get_member_last_name(self, obj):
        # Safely get the last name if the member exists
        return obj.member.last_name if obj.member else None

    def create(self, validated_data):
        # Correctly create a Declaration instance
        declaration = Declaration.objects.create(**validated_data)
        return declaration
