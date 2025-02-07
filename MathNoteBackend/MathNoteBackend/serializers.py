from rest_framework import serializers


class ImageDataSerializer(serializers.Serializer):
    image = serializers.CharField()  # Base64 encoded image
    dict_of_vars = serializers.DictField()
