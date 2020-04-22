from django.test import TestCase
from rest_framework.test import APITestCase
from .models import Profile, Item, Payment
from PIL import Image
from io import BytesIO
from django.core.files.base import File
import datetime
from django.utils import timezone

'''
Run with:
python manage.py test vueapi
'''

class LoginTest(APITestCase):

    def setUp(self):
        self.profile = Profile.objects.create(
            username='testuser', name='georges stpierre', shipping_addr='123 the street')
        self.profile.set_password('123123')
        self.profile.save()

    def test_correct(self):
        '''
        Test correct login information
        '''
        resp = self.client.post('/api/rest-auth/login/',
                                {'username': 'testuser', 'password': '123123'})
        self.assertEqual(200, resp.status_code)

    def test_incorrect(self):
        '''
        Test logging in with incorrect password
        '''
        resp = self.client.post('/api/rest-auth/login/',
                                {'username': 'testuser', 'password': 'asdasd'})
        self.assertEqual(400, resp.status_code)

    def test_userdoesntexist(self):
        ''' 
        Test loggin in with non existent user
        '''
        resp = self.client.post(
            '/api/rest-auth/login/', {'username': 'bigdawg', 'password': 'youngthug123'})
        self.assertEqual(400, resp.status_code)


class ItemTest(APITestCase):
    def setUp(self):
        self.profile = Profile.objects.create(
            username='testuser', name='georges stpierre', shipping_addr='123 the street')
        self.profile.set_password('123123')
        self.profile.save()
        resp = self.client.post('/api/rest-auth/login/',
                                {'username': 'testuser', 'password': '123123'})

    def get_img(self):
        '''
        create temp image file to test with
        '''
        thefile = BytesIO()
        img = Image.new("RGBA", size=(50, 50), color=(110, 0, 0))
        img.save(thefile, 'png')
        thefile.name = 'test.png'
        thefile.seek(0)
        return thefile

    def test_createitem(self):
        '''
        Test creating an item
        '''
        pic = self.get_img()
        print(self.profile.id)
        data = {'username': self.profile.id, 'mediatype': 'cd', 'genre': 'grindcore', 'artist': 'sufjan stevens', 'title': 'heavy weather',
                'description': 'it slaps', 'inventory_count': 5, 'price': 5.99, 'release_year': '2019-01-01', 'photo': pic}
        resp = self.client.post('/api/items/', data)
        self.assertEqual(201, resp.status_code)

    def test_updateitem(self):
        '''
        Test updating the item defined above
        '''
        data = {'genre': 'crustpunk', 'artist': 'justin bieber', 'title': 'harvest'}
        resp = self.client.patch('/api/partialupdate/1/', data)
        self.assertEqual(200, resp.status_code)


class PaymentTest(APITestCase):

    def get_img(self):
        '''
        create temp image file to test with
        '''
        thefile = BytesIO()
        img = Image.new("RGBA", size=(50, 50), color=(110, 0, 0))
        img.save(thefile, 'png')
        thefile.name = 'test.png'
        thefile.seek(0)
        return thefile

    def setUp(self):

        self.profile = Profile.objects.create(
            username='testuser', name='georges stpierre', shipping_addr='123 the street')
        self.profile.set_password('123123')
        self.profile.save()
        resp = self.client.post('/api/rest-auth/login/',
                                {'username': 'testuser', 'password': '123123'})

        

    def test_paymentnotinfuture(self):
        '''
        assert that a payment creation date is now or in the past
        '''
        pic = self.get_img()
        data = {'username': self.profile.id, 'mediatype': 'cd', 'genre': 'grindcore', 'artist': 'sufjan stevens', 'title': 'heavy weather',
                'description': 'it slaps', 'inventory_count': 5, 'price': 5.99, 'release_year': '2019-01-01', 'photo': pic}
        resp = self.client.post('/api/items/', data)
        self.item = Item.objects.get(pk=1)
        self.payment = Payment.objects.create(username=self.profile, iId=self.item, shipping_addr='asd', total_amt=5.99)
        time = timezone.now()
        self.assertLessEqual(self.payment.pDate, time.date())