# Generated by Django 5.0.3 on 2024-03-23 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0003_vote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id_number',
            field=models.CharField(max_length=9, unique=True),
        ),
    ]
