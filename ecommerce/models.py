from django.db import models


class Product(models.Model):

    code_a_barre = models.IntegerField( )
    name_product = models.CharField( max_length=200)
    prix_unitaire = models.FloatField()
    prix_vente = models.FloatField()
    categorie = models.CharField( max_length=10)
    quantite = models.IntegerField( )
    numero_fournisseur = models.IntegerField( blank=True )
    description = models.CharField( max_length=200, blank=True)
    image = models.ImageField(upload_to='produit_image',blank=True)

class Utilisateur(models.Model):

    prenom = models.CharField( max_length=20)
    nom = models.CharField( max_length=20)
    username = models.CharField( max_length=20)
    password = models.CharField( max_length=20)

    email = models.EmailField()
    numero_tel = models.IntegerField()
    ville = models.CharField(max_length=200)
    code_postal = models.IntegerField( )
    adresse = models.CharField(max_length=200)

class Utilisateur(models.Model):
    
    prenom = models.CharField( max_length=20)
    nom = models.CharField( max_length=20)
    username = models.CharField( max_length=20)
    password = models.CharField( max_length=20)

    email = models.EmailField()
    numero_tel = models.IntegerField()
    ville = models.CharField(max_length=200)
    code_postal = models.IntegerField( )
    adresse = models.CharField(max_length=200)



class Commande(models.Model):
    
    id_product = models.IntegerField( )
    id_utilisateur = models.CharField( max_length=20)
    etat = models.CharField( max_length=20)








