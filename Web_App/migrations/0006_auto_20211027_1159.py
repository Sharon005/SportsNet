# Generated by Django 3.2.7 on 2021-10-27 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web_App', '0005_event'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organizer',
            name='lastname',
        ),
        migrations.AddField(
            model_name='organizer',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
