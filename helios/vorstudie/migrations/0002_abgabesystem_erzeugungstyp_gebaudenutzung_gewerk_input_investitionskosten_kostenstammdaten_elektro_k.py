# Generated by Django 3.1.13 on 2021-11-16 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vorstudie', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Abgabesystem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abgabesystem', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Erzeugungstyp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('erzeugungstyp', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Gebaudenutzung',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gebaudenutzung', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Gewerk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gewerk', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Kostenstammdaten_HLKS_Erzeugung',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('erzeugungstyp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vorstudie.erzeugungstyp')),
                ('gewerk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vorstudie.gewerk')),
            ],
        ),
        migrations.CreateModel(
            name='Kostenstammdaten_HLKS_Abgabe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abgabesystem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vorstudie.abgabesystem')),
                ('gebaudenutzung', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vorstudie.gebaudenutzung')),
                ('gewerk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vorstudie.gewerk')),
                ('raumnutzung', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vorstudie.raumnutzung')),
            ],
        ),
        migrations.CreateModel(
            name='Kostenstammdaten_Elektro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gebaudenutzung', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vorstudie.gebaudenutzung')),
                ('gewerk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vorstudie.gewerk')),
                ('raumnutzung', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vorstudie.raumnutzung')),
            ],
        ),
        migrations.CreateModel(
            name='Input_Investitionskosten',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abgabesystem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vorstudie.abgabesystem')),
                ('einheitspreis_pro_m2_elektro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vorstudie.kostenstammdaten_elektro')),
                ('einheitspreis_pro_m2_hlks_abgabe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vorstudie.kostenstammdaten_hlks_abgabe')),
                ('einheitspreis_pro_m2_hlks_erzeugung', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vorstudie.kostenstammdaten_hlks_erzeugung')),
                ('gebaudenutzung', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vorstudie.gebaudenutzung')),
                ('gewerk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vorstudie.gewerk')),
                ('raumnutzung', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vorstudie.raumnutzung')),
            ],
        ),
    ]
