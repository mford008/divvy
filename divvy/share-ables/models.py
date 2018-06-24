from django.db import models
from django.contrib.auth.models import User


('''
This model should define share-ables, and link them to user_ids
more functionality later...
''')


class ShareItem(models.Model):
    item = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    image = models.FileField(upload_to='item-images', null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    
    
    
