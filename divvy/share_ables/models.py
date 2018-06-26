from django.db import models
from django.contrib.auth.models import User


('''
This model should define share-ables, and link them to user_ids
more functionality later...
''')


class ShareItem(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

<<<<<<< HEAD:divvy/share-ables/models.py
    image = models.FileField(upload_to='item_images/', null=True, blank=True)

=======
    image = models.FileField(upload_to='item-images', null=True, blank=True)
    
    item_name = models.CharField(max_length=40)
    
    username = models.User.name
    
    available = models.CharField(max_length=40)
    
    borrow_time = models.CharField(max_length=40)
    
>>>>>>> 0d82ec841c4e80a84a5ebdb5eeb742b00115f598:divvy/share_ables/models.py
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
