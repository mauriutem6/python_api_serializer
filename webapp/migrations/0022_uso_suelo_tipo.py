# Generated by Django 3.1.2 on 2020-11-19 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0021_auto_20201119_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='uso_suelo',
            name='tipo',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
    ]
