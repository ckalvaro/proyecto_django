# Generated by Django 4.1 on 2022-09-25 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0018_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='imagen',
            field=models.ImageField(blank=True, default='default.png', upload_to='avatares'),
        ),
    ]
