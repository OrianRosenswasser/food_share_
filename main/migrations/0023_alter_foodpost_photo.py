# Generated by Django 5.1.3 on 2024-11-14 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_alter_foodpost_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodpost',
            name='photo',
            field=models.ImageField(blank=True, default='/placeholder.png', null=True, upload_to='food_posts/'),
        ),
    ]
