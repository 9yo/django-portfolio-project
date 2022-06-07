from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate
from django.contrib.auth.models import User
from contacts.views import ContactsView


factory = APIRequestFactory()
user = User.objects.get(username='root')
view = ContactsView.as_view()

# Make an authenticated request to the view...
request = factory.get('/contacts/')
force_authenticate(request, user=user)
response = view(request)




factory = APIRequestFactory()
user = User.objects.get(username='root')
view = ContactsView.as_view()

# Make an authenticated request to the view...
json = {'owner': 'root', 'name': 'Adam', 'number': '+79117363277', 'comment': 'Friend'}
request = factory.post('/contacts/', json=json)
force_authenticate(request, user=user)
response = view(request)
