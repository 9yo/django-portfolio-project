from contacts.models import Contact
from rest_framework import serializers


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Contact
        fields = ['id', 'url', 'owner', 'name', 'number', 'comment']
