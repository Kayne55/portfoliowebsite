# Generated by Django 4.0.3 on 2022-07-17 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_job_body_job_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]