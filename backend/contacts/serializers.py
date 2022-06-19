from contacts.models import Contact, ContactBook
from rest_framework import serializers


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Contact
        fields = ['id', 'url', 'owner', 'name', 'number', 'comment']

class ContactBookSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    contacts = serializers.PrimaryKeyRelatedField(many=True,
                                                queryset=Contact.objects.all())

    class Meta:
        model = ContactBook
        fields = ['id', 'url', 'owner', 'name','desc', 'contacts']
