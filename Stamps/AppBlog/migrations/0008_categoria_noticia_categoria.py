# Generated by Django 4.1 on 2022-09-16 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0007_merge_20220914_1433'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='noticia',
            name='categoria',
            field=models.CharField(default='placeholder', max_length=30),
        ),
    ]
