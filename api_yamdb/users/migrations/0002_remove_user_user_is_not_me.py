# Generated by Django 3.2 on 2022-12-28 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='user',
            name='user_is_not_me',
        ),
    ]
