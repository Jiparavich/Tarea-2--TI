# Generated by Django 3.0.4 on 2020-05-04 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Hamburguesa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('precio', models.IntegerField()),
                ('descripcion', models.CharField(max_length=400)),
                ('imagen', models.URLField(max_length=255)),
                ('ingredientes', models.ManyToManyField(blank=True, related_name='burguers', to='burguers.Ingrediente')),
            ],
        ),
    ]
