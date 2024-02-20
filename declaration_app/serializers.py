from rest_framework import serializers
from .models import Declaration
from member_app.serializers import MemberSerializer
from member_app.models import Member


class DeclareSerializer(serializers.ModelSerializer):
    # Use the MemberSerializer to represent the member_id field

    class Meta:
        model = Declaration
        fields = '__all__'
