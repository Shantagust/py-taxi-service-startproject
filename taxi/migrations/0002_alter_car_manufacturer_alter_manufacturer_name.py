# Generated by Django 5.0.3 on 2024-03-12 18:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='taxi.manufacturer'),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]