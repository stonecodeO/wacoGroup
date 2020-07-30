# Generated by Django 3.0.8 on 2020-07-27 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Pays',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sexe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.IntegerField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('terminated', models.BooleanField(default=False)),
                ('price', models.FloatField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cargo.Client')),
                ('pays', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cargo.Pays')),
            ],
        ),
        migrations.CreateModel(
            name='Colis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poids', models.DecimalField(decimal_places=2, max_digits=5)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cargo.Client')),
                ('commande', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cargo.Commande')),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='sexe',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cargo.Sexe'),
        ),
    ]