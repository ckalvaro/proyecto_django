# Generated by Django 4.1 on 2022-09-22 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("AppBlog", "0017_alter_comentario_noticia"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comentario",
            name="texto",
            field=models.TextField(blank=True, max_length=255),
        ),
    ]
