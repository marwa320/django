from django import forms
from .models import Product,Utilisateur

C = (('0','Catégorie'),('aliment','aliment'),('vétement','vétement'), ('électromenager','électromenager'), ('informatique','informatique'))
VILLE = (('Tunis','Tunis'),('Bizert','Bizert'),('Manouba','Manouba'), ('Gafsa','Gafsa'), ('Nabeul','Nabeul'), ('Sousse','Sousse'))

class ProductsForm(forms.ModelForm):
    
    categorie = forms.ChoiceField(choices = C, label="", initial='', widget=forms.Select(attrs={'class':'form-control'}), required=True,)
    image = forms.ImageField(label='choisir une image',)

    class Meta:
        model = Product
        fields = ['code_a_barre','name_product', 'prix_unitaire','prix_vente','categorie','quantite','numero_fournisseur','description','image']
        widgets= {
            'code_a_barre' : forms.TextInput(attrs={'class':'form-control',}),
            'name_product' : forms.TextInput(attrs={'class':'form-control',}),
            'prix_unitaire' : forms.TextInput(attrs={'class':'form-control',}),
            'prix_vente' : forms.TextInput(attrs={'class':'form-control',}),
            #'categorie' :  forms.Select( choices=C,),
            'quantite' : forms.TextInput(attrs={'class':'form-control',}),
            'numero_fournisseur' : forms.TextInput(attrs={'class':'form-control',}),
            'description' : forms.Textarea(attrs={'class':'form-control',}),
        }

class LoginForm(forms.ModelForm):
    
    class Meta:
        model = Utilisateur
        fields = ['username','password']
        widgets= {
            'username' : forms.TextInput(attrs={'class':'form-control',}),
            'password' : forms.TextInput(attrs={'class':'form-control',}),
        }

class UtilisateursForm(forms.ModelForm):
    
    ville = forms.ChoiceField(choices = VILLE, label="", initial='', widget=forms.Select(attrs={'class':'form-control'}), required=True,)

    class Meta:
        model = Utilisateur
        fields = ['prenom','nom', 'username','password','email','numero_tel','ville','code_postal','adresse']
        widgets= {
            'prenom' : forms.TextInput(attrs={'class':'form-control',}),
            'nom' : forms.TextInput(attrs={'class':'form-control',}),
            'username' : forms.TextInput(attrs={'class':'form-control',}),
            'password' : forms.TextInput(attrs={'class':'form-control',}),
            'numero_tel' : forms.TextInput(attrs={'class':'form-control',}),
            'email' : forms.TextInput(attrs={'class':'form-control',}),
            'code_postal' : forms.TextInput(attrs={'class':'form-control',}),
            'adresse' : forms.Textarea(attrs={'class':'form-control',}),
        }

