from django.test import TestCase
from contacts.models import Contact
from django.contrib.auth.models import User


class ContactTestCase(TestCase):
    def testContactModel(self):
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
