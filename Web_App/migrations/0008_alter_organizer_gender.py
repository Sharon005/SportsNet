# Generated by Django 3.2.3 on 2021-10-05 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web_App', '0007_organizer_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizer',
            name='gender',
            field=models.CharField(max_length=10),
        ),
    ]
