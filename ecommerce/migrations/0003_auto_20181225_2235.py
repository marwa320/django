# Generated by Django 2.1.4 on 2018-12-25 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0002_commande'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commande',
            name='id_utilisateur',
            field=models.CharField(max_length=20),
        ),
    ]
