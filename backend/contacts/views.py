from rest_framework import viewsets
from rest_framework import permissions
from contacts.models import Contact
from contacts.serializers import ContactSerializer


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
