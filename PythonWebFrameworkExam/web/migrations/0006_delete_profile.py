# Generated by Django 4.1.4 on 2022-12-11 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_remove_comment_email_remove_comment_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
