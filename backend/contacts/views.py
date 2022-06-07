from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from contacts.models import Contact
from contacts.serializers import ContactSerializer


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


# Create your views here.
class ContactsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Contact.objects.all().order_by('name')
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
