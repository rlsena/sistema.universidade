# Generated by Django 3.2.8 on 2021-10-24 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('codigo', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('professor', models.CharField(max_length=50)),
                ('creditos', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
