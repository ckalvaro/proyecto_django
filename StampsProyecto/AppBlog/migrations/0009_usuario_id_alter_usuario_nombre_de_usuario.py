# Generated by Django 4.1 on 2022-09-14 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0008_remove_usuario_id_alter_usuario_nombre_de_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombre_de_usuario',
            field=models.CharField(max_length=80),
        ),
    ]
