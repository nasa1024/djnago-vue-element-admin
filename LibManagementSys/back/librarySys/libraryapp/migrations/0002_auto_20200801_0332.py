# Generated by Django 2.2 on 2020-07-31 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='role',
            new_name='usertype',
        ),
    ]
