# Generated by Django 3.2.3 on 2021-10-05 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Web_App', '0008_alter_organizer_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organizer',
            name='gender',
        ),
    ]