# Generated by Django 4.1.4 on 2022-12-14 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_delete_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thread',
            name='image',
        ),
    ]
