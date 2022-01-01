from django.test import TestCase
from rest_framework.test import APIClient
from .models import UserProfile
from django.contrib.auth.models import User
from datetime import datetime


class UserProfileTestAPI(TestCase):

    def setUp(self):
        self.api = APIClient()
        self.user_1 = User(username='Li_1')
        self.user_1.set_password('password_1')
        self.user_1.save()

        user_profile_1 = UserProfile.objects.create(user=self.user_1,
                                                    name='up_1',
                                                    birthday=datetime(1987, 11, 9).date(),
                                                    gender=UserProfile.Gender.men,
                                                    sex_orientation=UserProfile.Gender.men,
                                                    about='wow')

        self.user_2 = User(username='Li_2')
        self.user_2.set_password('password_2')
        self.user_2.save()

        user_profile_2 = UserProfile.objects.create(user=self.user_2,
                                                    name='up_2',
                                                    birthday=datetime(1987, 11, 9).date(),
                                                    gender=UserProfile.Gender.men,
                                                    sex_orientation=UserProfile.Gender.men,
                                                    about='wow2')

        self.user_3 = User(username='Li_3')
        self.user_3.set_password('password_3')
        self.user_3.save()

        user_profile_3 = UserProfile.objects.create(user=self.user_3,
                                                    name='up_3',
                                                    birthday=datetime(1987, 11, 9).date(),
                                                    gender=UserProfile.Gender.men,
                                                    sex_orientation=UserProfile.Gender.men,
                                                    about='wow3')

    def tests_user_profile_list(self):
        response = self.api.get('/users/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),
                         [{
                             'name': 'up_1',
                             'gender': 'men',
                             'age': 34,
                             'sex_orientation': 'men',


                         },
                         {
                             'name': 'up_2',
                             'gender': 'men',
                             'age': 34,
                             'sex_orientation': 'men',


                         },
                         {
                             'name': 'up_3',
                             'gender': 'men',
                             'age': 34,
                             'sex_orientation': 'men',


                         },
                         ])
