# Generated by Django 4.0.3 on 2022-07-17 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='body',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='job',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
    ]
