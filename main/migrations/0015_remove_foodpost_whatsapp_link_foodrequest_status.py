# Generated by Django 5.1.3 on 2024-11-13 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_foodpost_whatsapp_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foodpost',
            name='whatsapp_link',
        ),
        migrations.AddField(
            model_name='foodrequest',
            name='status',
            field=models.CharField(default='pending', max_length=100),
        ),
    ]
