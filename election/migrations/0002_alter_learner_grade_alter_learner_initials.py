# Generated by Django 5.1.7 on 2025-06-24 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learner',
            name='grade',
            field=models.CharField(choices=[('7A', '7A'), ('7B', '7B'), ('7C', '7C'), ('8A', '8A'), ('8B', '8B')], max_length=10),
        ),
        migrations.AlterField(
            model_name='learner',
            name='initials',
            field=models.CharField(blank=True, max_length=10, unique=True),
        ),
    ]
