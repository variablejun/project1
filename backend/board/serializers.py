from rest_framework import serializers
from board.models import Post

class BoardSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    content = serializers.CharField()
    create_at = serializers.DateTimeField()
    update_at = serializers.DateTimeField()



    def create(self, validated_data):

        return Post.objects.create(**validated_data)