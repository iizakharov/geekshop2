from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from datetime import timedelta


def activation_key_expires():
    return now() + timedelta(hours=48)


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    # age = models.PositiveSmallIntegerField(verbose_name='возраст', default=18)
    age = models.PositiveSmallIntegerField(verbose_name='возраст', null=True)
    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(default=activation_key_expires)

    def is_activation_key_valid(self):
        return now() <= self.activation_key_expires


class ShopUserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'W'

    GENDER_CHOICES = (
        (MALE, 'МУЖСКОЙ'),
        (FEMALE, 'ЖЕНСКИЙ'),
    )

    user = models.OneToOneField(ShopUser, primary_key=True, on_delete=models.CASCADE)
    tagline = models.CharField(verbose_name='теги', max_length=128, blank=True)
    aboutMe = models.TextField(verbose_name='о себе', max_length=512, blank=True)
    gender = models.CharField(verbose_name='пол', max_length=1,
                              choices=GENDER_CHOICES, blank=True)
