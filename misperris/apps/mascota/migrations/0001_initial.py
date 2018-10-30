# Generated by Django 2.1.2 on 2018-10-29 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('adopcion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('raza', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=100)),
                ('state', models.CharField(choices=[('Disponible', 'Disponible'), ('Adoptado', 'Adoptado'), ('Rescatado', 'Rescatado')], default='Rescatado', max_length=10)),
                ('persona', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adopcion.Persona')),
            ],
        ),
    ]