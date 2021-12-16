from django.db import models
from users.models import UserProfile


def upload_gallery_image(instance, filename):
    return "images/{}/gallery/{}".format(instance.user.name, filename)


class Photo(models.Model):
    image = models.ImageField(upload_to=upload_gallery_image)
    description = models.CharField(null=True,
                                   max_length=50,
                                   help_text='Enter short text description',
                                   blank=True
                                   )
    user = models.ForeignKey(UserProfile,
                             on_delete=models.CASCADE,
                             related_name='photo',
                             )

    def __str__(self):
        return 'Photo {}'.format(self.user.name)
