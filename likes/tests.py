from django.test import TestCase
from rest_framework.test import APIClient
from .models import Like
from django.contrib.auth.models import User
from users.models import UserProfile
from datetime import datetime


class LikeTestAPI(TestCase):

    def setUp(self):
        self.api = APIClient()
        self.user_1 = User(username='Li_1')
        self.user_1.set_password('password_1')
        self.user_1.save()

        self.user_profile_1 = UserProfile(user=self.user_1,
                                          name='up_1',
                                          birthday=datetime(1987, 11, 9).date(),
                                          gender=UserProfile.Gender.men,
                                          sex_orientation=UserProfile.Gender.men,
                                          about='wow')
        self.user_profile_1.save()

        self.user_2 = User(username='Li_2')
        self.user_2.set_password('password_2')
        self.user_2.save()

        self.user_profile_2 = UserProfile(user=self.user_2,
                                          name='up_2',
                                          birthday=datetime(1987, 11, 9).date(),
                                          gender=UserProfile.Gender.men,
                                          sex_orientation=UserProfile.Gender.men,
                                          about='wow2')
        self.user_profile_2.save()

        self.user_3 = User(username='Li_3')
        self.user_3.set_password('password_3')
        self.user_3.save()

        self.user_profile_3 = UserProfile(user=self.user_3,
                                          name='up_3',
                                          birthday=datetime(1987, 11, 9).date(),
                                          gender=UserProfile.Gender.men,
                                          sex_orientation=UserProfile.Gender.men,
                                          about='wow3')
        self.user_profile_3.save()

        like_1 = Like.objects.create(sender=self.user_profile_1, recipient=self.user_profile_2)
        like_2 = Like.objects.create(sender=self.user_profile_1, recipient=self.user_profile_3)
        like_3 = Like.objects.create(sender=self.user_profile_2, recipient=self.user_profile_1)
        like_4 = Like.objects.create(sender=self.user_profile_2, recipient=self.user_profile_3)
        like_5 = Like.objects.create(sender=self.user_profile_3, recipient=self.user_profile_1)
        like_6 = Like.objects.create(sender=self.user_profile_3, recipient=self.user_profile_2)

    def tests_like_list(self):
        response = self.api.get('/likes/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),
                         [{
                             'id': 1,
                             'sender': 1,
                             'recipient': 2,

                         },
                         {
                             'id': 2,
                             'sender': 1,
                             'recipient': 3,

                         },
                         {
                             'id': 3,
                             'sender': 2,
                             'recipient': 1,

                         },
                         {
                             'id': 4,
                             'sender': 2,
                             'recipient': 3,

                         },
                         {
                             'id': 5,
                             'sender': 3,
                             'recipient': 1,

                         },
                         {
                             'id': 6,
                             'sender': 3,
                             'recipient': 2,

                         }
                         ])

