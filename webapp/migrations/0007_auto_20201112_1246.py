# Generated by Django 3.1.3 on 2020-11-12 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_album_track'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona_juridica_usuario',
            name='usuario_rut',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario_rut', to='webapp.usuario'),
        ),
    ]