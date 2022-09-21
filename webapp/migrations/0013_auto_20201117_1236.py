# Generated by Django 3.1.2 on 2020-11-17 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0012_auto_20201116_1952'),
    ]

    operations = [
        migrations.CreateModel(
            name='documentos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, null=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, null=True)),
                ('_data', models.TextField(blank=True, db_column='data')),
            ],
        ),
        migrations.CreateModel(
            name='tipo_participante_empresa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
            ],
        ),
        migrations.AlterField(
            model_name='empresa',
            name='rut',
            field=models.CharField(max_length=13, verbose_name='rut'),
        ),
        migrations.CreateModel(
            name='log_proyecto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('proyecto_id', models.IntegerField()),
                ('observacion', models.CharField(blank=True, max_length=45, null=True)),
                ('fecha', models.CharField(blank=True, max_length=45, null=True)),
                ('usuario_rut', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuarioSecondary', to='webapp.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='persona_juridica_usuario',
            name='tipo_participante_empresa_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='tipo_participante_empresa_secondary', to='webapp.tipo_participante_empresa'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='persona_juridica_usuario',
            unique_together={('usuario_rut', 'persona_juridic', 'tipo_participante_empresa_id')},
        ),
    ]