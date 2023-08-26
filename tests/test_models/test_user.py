#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ """
        f_name = {'first_name': 'Bob'}
        new = self.value(**f_name)
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ """
        last_name = {'last_name': 'Smith'}
        new = self.value(**last_name)
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ """
        mail = {'email': 'user@email.com'}
        new = self.value(**mail)
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ """
        passwd = {'password' : 'password'}
        new = self.value(**passwd)
        self.assertEqual(type(new.password), str)
