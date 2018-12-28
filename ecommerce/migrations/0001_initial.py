# Generated by Django 2.1.4 on 2018-12-24 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_a_barre', models.IntegerField()),
                ('name_product', models.CharField(max_length=200)),
                ('prix_unitaire', models.FloatField()),
                ('prix_vente', models.FloatField()),
                ('categorie', models.CharField(max_length=10)),
                ('quantite', models.IntegerField()),
                ('numero_fournisseur', models.IntegerField(blank=True)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='produit_image')),
            ],
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenom', models.CharField(max_length=20)),
                ('nom', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('numero_tel', models.IntegerField()),
                ('ville', models.CharField(max_length=200)),
                ('code_postal', models.IntegerField()),
                ('adresse', models.CharField(max_length=200)),
            ],
        ),
    ]
