# Generated by Django 4.0.2 on 2022-03-23 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_friend_request_remove_friendrequest_receiver_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(upload_to='event/`'),
        ),
    ]
