from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory


from contacts.models import Contact
from contacts.views import ContactsViewSet


class ContactTestCase(TestCase):
    def test_contact_model(self):
        user = User.objects.create_user(
            username='test',
            password='test')

        contact = Contact(owner=user,
                          name="Adam",
                          number="+79214442233",
                          comment="Friend")

        self.assertEqual(contact.owner.username, "test")
        self.assertEqual(contact.name, "Adam")
        self.assertEqual(contact.number, "+79214442233")
        self.assertEqual(contact.comment, "Friend")

    def test_contact_view(self):
        # setup

        factory = APIRequestFactory()
        actions = {
            'get': 'retrieve',
            'post': 'create'
        }
        view = ContactsViewSet.as_view(actions)
        first_user = User.objects.create_user(username='first',
                                              password='first')
        second_user = User.objects.create_user(username='second',
                                               password='second')
        contact_data = {
            "name": "testcase",
            "number": "+79113332211",
            "comment": "testcase"
        }

        # creating contact with a first user as owner

        request = factory.post('/contacts/', contact_data, format='json')
        request.user = first_user
        response = view(request)

        # testing create operation response

        self.assertEqual(response.data.get('owner'), "first")
        self.assertEqual(response.data.get('name'), "testcase")
        self.assertEqual(response.data.get('number'), "+79113332211")
        self.assertEqual(response.data.get('comment'), "testcase")
        contact_pk = response.data.get('id')

        # testing retrieve response as first user

        request = factory.get('/contacts/')
        request.user = first_user
        response = view(request, pk=contact_pk)

        self.assertEqual(response.data.get('id'), contact_pk)
        self.assertEqual(response.data.get('owner'), "first")
        self.assertEqual(response.data.get('name'), "testcase")
        self.assertEqual(response.data.get('number'), "+79113332211")
        self.assertEqual(response.data.get('comment'), "testcase")

        # testing retrieve contact owned by first user as second user

        request.user = second_user
        response = view(request, pk=contact_pk)
        self.assertEqual(response.data.get('detail').code, 'permission_denied')
