# Generated by Django 4.1 on 2022-09-12 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0003_rename_autor_noticia_autor_nombre_noticia_autor_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticia',
            name='autor_user',
        ),
    ]
