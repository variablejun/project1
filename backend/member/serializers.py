from rest_framework import serializers
from member.models import Member

class MemberSerializers(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField()
    name = serializers.CharField()
    email = serializers.EmailField()

    class Meta:
        model = Member
        fields = ['username', 'password', 'name', 'email']

    def create(self, validated_data):


        return Member.objects.create(**validated_data)