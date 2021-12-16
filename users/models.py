from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class UserProfile(models.Model):
    user = models.OneToOneField(User,
                                null=True,
                                on_delete=models.CASCADE,
                                related_name='profile',
                                )
    name = models.CharField(max_length=100,
                            help_text='Enter your name',
                            )
    birthday = models.DateField(help_text='Enter date of your birthday', )

    @property
    def age(self):
        return int((datetime.now().date() - self.birthday).days / 365.25)

    class Gender:
        men = 'men'
        woman = 'woman'

    GENDER_CHOICE = (
        (Gender.men, 'men'),
        (Gender.woman, 'woman'),
    )

    gender = models.CharField(max_length=100,
                              choices=GENDER_CHOICE,
                              help_text='Choose your gender type',
                              )

    sex_orientation = models.CharField(max_length=100,
                                       choices=GENDER_CHOICE,
                                       help_text='Choose your gender preference',
                                       )
    about = models.CharField(max_length=1000,
                             help_text='Enter short text about yourself',
                             )

    def __str__(self):
        return '{}:  {} {} years, prefers - {}'.format(self.name, self.gender[0], self.age, self.sex_orientation)



