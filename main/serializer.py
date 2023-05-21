from rest_framework import serializers

from main.models import Contact


class ContactSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()

    class Meta:
        model = Contact
        fields = "__all__"
