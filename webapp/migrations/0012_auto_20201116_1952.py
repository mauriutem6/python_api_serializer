# Generated by Django 3.1.2 on 2020-11-16 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0011_auto_20201116_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='fecha_modificacion',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
