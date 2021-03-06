# Generated by Django 2.1.2 on 2018-10-04 03:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_classe', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Famille',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_famille', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='NomScientifique',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_nomscientifique', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Ordre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_ordre', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='animal',
            name='classe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ifap.Classe'),
        ),
        migrations.AddField(
            model_name='animal',
            name='famille',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ifap.Famille'),
        ),
        migrations.AddField(
            model_name='animal',
            name='nomscientifique',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ifap.NomScientifique'),
        ),
        migrations.AddField(
            model_name='animal',
            name='ordre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ifap.Ordre'),
        ),
    ]
