# Generated by Django 3.1.13 on 2021-11-17 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projekt', '0006_auto_20211117_1151'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gewerk2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gewerk', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Klassifizierung',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('klassifizierung', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='projektspezifikationen',
            name='projekt_gewerk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projekt.gewerk'),
        ),
        migrations.CreateModel(
            name='Nutzungsstammdaten_SIA2024',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leistung_pro_m2_Klassifizierung_Gewerk2', models.FloatField()),
                ('energie_pro_m2_Klassifizierung_Gewerk2', models.FloatField()),
                ('raumtemparatur', models.FloatField()),
                ('luftwechsel_Pro_Person', models.FloatField()),
                ('flaeche_Pro_Personenanzahl', models.FloatField()),
                ('beleuchtungsstaerke', models.FloatField()),
                ('gewerk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projekt.gewerk2')),
                ('klassifizierung', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projekt.klassifizierung')),
                ('raumnutzung', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projekt.raumnutzung')),
            ],
        ),
    ]
