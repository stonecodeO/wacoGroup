# Generated by Django 3.0.8 on 2020-07-27 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cargo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pays',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='sexe',
            name='name',
            field=models.CharField(max_length=2),
        ),
    ]
