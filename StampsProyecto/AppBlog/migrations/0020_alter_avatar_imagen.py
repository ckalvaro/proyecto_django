# Generated by Django 4.1 on 2022-09-25 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0019_alter_avatar_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='imagen',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='avatares'),
        ),
    ]