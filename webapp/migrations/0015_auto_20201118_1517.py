# Generated by Django 3.1.2 on 2020-11-18 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0014_persona_juridica_documentos_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='destino',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=45, null=True)),
                ('tipo', models.CharField(blank=True, max_length=45, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='uso_suelo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=45, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='vehiculos_equivalente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=45, null=True)),
                ('factor', models.CharField(blank=True, max_length=45, null=True)),
                ('estado', models.CharField(blank=True, max_length=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='dproyecto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=45, null=True)),
                ('destino_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destinoSecondary', to='webapp.destino')),
            ],
        ),
        migrations.AddField(
            model_name='destino',
            name='uso_suelo_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uso_sueloSecondary', to='webapp.uso_suelo'),
        ),
    ]
