# Generated by Django 3.0.8 on 2020-07-28 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cargo', '0002_auto_20200727_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='sexe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cargo.Sexe'),
        ),
        migrations.AlterField(
            model_name='commande',
            name='pays',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cargo.Pays'),
        ),
    ]