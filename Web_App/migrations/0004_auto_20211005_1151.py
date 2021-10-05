# Generated by Django 3.2.3 on 2021-10-05 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web_App', '0003_rename_eventorganizer_organizer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizer',
            name='address',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='organizer',
            name='code',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='organizer',
            name='email',
            field=models.EmailField(max_length=122),
        ),
        migrations.AlterField(
            model_name='organizer',
            name='first_name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='organizer',
            name='last_name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='organizer',
            name='phonenumber',
            field=models.IntegerField(max_length=12),
        ),
        migrations.AlterField(
            model_name='organizer',
            name='sport',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
