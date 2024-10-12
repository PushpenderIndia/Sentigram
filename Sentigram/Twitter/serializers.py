from rest_framework import serializers

class SentimentSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=512)