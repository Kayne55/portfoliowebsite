from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog/%Y/%m/')
    pubdate = models.DateTimeField()
    body = models.TextField()

    def summary(self):
        return self.body[:250]
