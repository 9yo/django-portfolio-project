from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from contacts.models import Contact, ContactBook
from contacts.serializers import ContactSerializer, ContactBookSerializer
from contacts.permissions import IsOwner


# Create your views here.
class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all().order_by('name')
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def list(self, request, *args, **kwargs):
        if request.user.is_superuser:
            queryset = self.queryset
        else:
            queryset = self.queryset.filter(owner=request.user)

        queryset = self.filter_queryset(queryset)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class ContactBookViewSet(viewsets.ModelViewSet):
    queryset = ContactBook.objects.all().order_by('name')
    serializer_class = ContactBookSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def list(self, request, *args, **kwargs):
        if request.user.is_superuser:
            queryset = self.queryset
        else:
            queryset = self.queryset.filter(owner=request.user)

        queryset = self.filter_queryset(queryset)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
