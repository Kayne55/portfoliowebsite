from django.db import models
# from django.conf import settings
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=100)
    pubdate = models.DateTimeField()
    image = models.ImageField(upload_to='blog/%Y/%m/')
    body = models.TextField()
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        )

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:250]

    def pub_date_short(self):
        return self.pubdate.strftime('%e %b %Y')