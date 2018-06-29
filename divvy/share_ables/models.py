from django.db import models
from divvy.users.models import User


('''
This model should define share-ables, and link them to user_ids
more functionality later...
''')


class ShareItem(models.Model):
    username = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    item_name = models.CharField(max_length=120)
    avail_time = models.CharField(max_length=20)
    borrow_time = models.CharField(max_length=20)
    descript = models.CharField(max_length=255)
    image = models.FileField(upload_to='divvy/static/images', null=True, blank=True)

    def __str__(self):
        return self.username
