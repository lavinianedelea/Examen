# Generated by Django 2.2.5 on 2019-09-22 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myusers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='number_of_login',
            field=models.IntegerField(),
        ),
    ]