# Generated by Django 2.2.16 on 2020-10-20 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto6', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Insumos',
            fields=[
                ('nombre', models.CharField(max_length=120, primary_key=True, serialize=False)),
                ('precio', models.IntegerField()),
                ('desccripsion', models.TextField()),
                ('stock', models.IntegerField()),
            ],
        ),
    ]
