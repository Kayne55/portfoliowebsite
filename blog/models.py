from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog/%Y/%m/')
    pubdate = models.DateTimeField()
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:250]

    def pub_date_short(self):
        return self.pubdate.strftime('%e %b %Y')