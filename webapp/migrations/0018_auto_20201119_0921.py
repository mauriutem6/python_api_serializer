# Generated by Django 3.1.2 on 2020-11-19 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0017_auto_20201118_1805'),
    ]

    operations = [
        migrations.CreateModel(
            name='direccion_rol',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('direccion', models.CharField(blank=True, max_length=45, null=True)),
                ('numero', models.CharField(blank=True, max_length=45, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='persona_proyecto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(blank=True, max_length=45, null=True)),
                ('ap_paterno', models.CharField(blank=True, max_length=45, null=True)),
                ('ap_materno', models.CharField(blank=True, max_length=45, null=True)),
                ('via', models.CharField(blank=True, max_length=45, null=True)),
                ('direccion', models.CharField(blank=True, max_length=45, null=True)),
                ('numero', models.CharField(blank=True, max_length=45, null=True)),
                ('email', models.CharField(blank=True, max_length=45, null=True)),
                ('telefono', models.CharField(blank=True, max_length=45, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='proyecto_ficha',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='rol',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rol', models.CharField(blank=True, max_length=45, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='rol_proyecto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(blank=True, max_length=1, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='persona_juridica',
            old_name='documentos_id',
            new_name='acto_constitutivo_documentos_id',
        ),
        migrations.RenameField(
            model_name='persona_juridica',
            old_name='rut_dv',
            new_name='dv',
        ),
        migrations.RenameField(
            model_name='persona_juridica',
            old_name='nombre',
            new_name='razon_social',
        ),
        migrations.RemoveField(
            model_name='log_proyecto',
            name='proyecto_id',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='ape_mat',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='ape_pat',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='comuna_cod_comu',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='direccion_calle',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='direccion_numero',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='email',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='fecha_creacion',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='fecha_modificacion',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='perfil_id',
        ),
        migrations.AddField(
            model_name='direccion_via',
            name='estado',
            field=models.CharField(default='', max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='persona_juridica',
            name='direccion',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='persona_juridica',
            name='direccion_depto',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='persona_juridica',
            name='direccion_numero',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='persona_juridica',
            name='estado',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='persona_juridica_usuario',
            name='estado',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='persona_juridica_usuario',
            name='persona_juridica_rut',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='persona_juridic_track', to='webapp.persona_juridica'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proyecto',
            name='colinda_camino_publico',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='colinda_red_vial_basica',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='descripcion',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='proposito',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='rol_fusion',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='tipo_crecimiento',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='ap_materno',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='ap_paterno',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='cod_comuna',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='usuario_comuna', to='webapp.comuna'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='direccion',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='estado',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='nombres',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='persona_juridica_usuario',
            unique_together={('usuario_rut', 'persona_juridica_rut', 'tipo_participante_empresa_id')},
        ),
        migrations.RemoveField(
            model_name='persona_juridica_usuario',
            name='persona_juridic',
        ),
        migrations.RemoveField(
            model_name='persona_juridica_usuario',
            name='tipo',
        ),
    ]
