from django.db import models

from users.models import UserProfile


class Like(models.Model):
    sender = models.ForeignKey(UserProfile,
                               null=True,
                               on_delete=models.CASCADE,
                               related_name='like_sender',
                               blank=True
                               )
    recipient = models.ForeignKey(UserProfile,
                                  null=True,
                                  on_delete=models.CASCADE,
                                  related_name='like_recipient',
                                  blank=True
                                  )

    def __str__ (self):
        return "{} like's {}".format(self.sender, self.recipient)
