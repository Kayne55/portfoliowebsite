from distutils.command.upload import upload
from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=100, default='')
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    body = models.TextField(blank=True, default='')
    job_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

    def job_date_short(self):
        return self.job_date.strftime('%e %b %Y')