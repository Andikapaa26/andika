# Generated by Django 4.1.2 on 2023-01-03 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_alter_home_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='foto',
            field=models.ImageField(upload_to='media'),
        ),
    ]
