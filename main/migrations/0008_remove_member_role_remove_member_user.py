# Generated by Django 5.1.3 on 2024-11-11 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_member_role_member_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='role',
        ),
        migrations.RemoveField(
            model_name='member',
            name='user',
        ),
    ]
