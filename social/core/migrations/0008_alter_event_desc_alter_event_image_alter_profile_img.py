# Generated by Django 4.0.2 on 2022-03-25 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_event_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='desc',
            field=models.TextField(max_length=400, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(default='event/fireworks2.jpg', upload_to='event'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(default='core/user.jpg', upload_to='profile'),
        ),
    ]