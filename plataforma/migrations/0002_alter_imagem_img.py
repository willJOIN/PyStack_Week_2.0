# Generated by Django 4.0.1 on 2022-01-14 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagem',
            name='img',
            field=models.ImageField(upload_to='assets'),
        ),
    ]
