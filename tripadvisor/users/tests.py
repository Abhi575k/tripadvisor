from django.test import TestCase
from django.contrib.auth import get_user_model

class TripUserManagerTestCase(TestCase):
    '''
    
    '''
    def setUp(self):
        self.User = get_user_model()
    
    def test_create_user(self):
        username = 'testuser'
        email = 'testuser@test.com'
        password = 'testpassword'

        user = self.User.objects.create_user(username, email, password)
        self.assertEqual(user.username, username)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertTrue(user.is_active)
        try:
            self.User.objects.create_user(None, email, password)
        except ValueError as e:
            self.assertEqual(str(e), 'Username is required')
        try:
            self.User.objects.create_user(username, None, password)
        except ValueError as e:
            self.assertEqual(str(e), 'Email is required')
        try:
            self.User.objects.create_user(username, email, None)
        except ValueError as e:
            self.assertEqual(str(e), 'Password is required')

    def test_create_super_user(self):
        username = 'admin'
        email = 'admin@test.com'
        password = 'adminpassword'

        user = self.User.objects.create_super_user(username, email, password)
        self.assertEqual(user.username, username)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_active)

        try:
            self.User.objects.create_super_user(username, email, password, is_staff=False)
        except ValueError as e: 
            self.assertEqual(str(e), 'Superuser must have is_staff=True.')
        try:
            self.User.objects.create_super_user(username, email, password, is_superuser=False)
        except ValueError as e:
            self.assertEqual(str(e), 'Superuser must have is_superuser=True.')


