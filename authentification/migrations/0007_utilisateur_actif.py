# Generated by Django 4.1.7 on 2023-03-08 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentification', '0006_alter_utilisateur_ispasswordset'),
    ]

    operations = [
        migrations.AddField(
            model_name='utilisateur',
            name='actif',
            field=models.BooleanField(default=True),
        ),
    ]
