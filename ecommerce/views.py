from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .form import ProductsForm,LoginForm,UtilisateursForm
from ecommerce.models import Product,Utilisateur,Commande


def login(request):
      form = LoginForm(request.POST or None)
      utilisateur = None
      if request.method == 'POST':
            try:
                  utilisateur = get_object_or_404(Utilisateur ,username=request.POST.get('username'), password=request.POST.get('password'))
                  request.session['id']=request.POST.get('id')
                  request.session['username']=request.POST.get('username')
                  request.session['password']=request.POST.get('password')
                  if request.session.get('username') == "admin":
                        return redirect('ecommerce:product_list')
                  return redirect('ecommerce:index')
            except :
                  return redirect('ecommerce:login')

      return render(request, 'login.html' ,{'form': form})

def logout(request):
            try:
                  del request.session['username']
                  del request.session['password']
                  return redirect('ecommerce:login')
            except :
                  return redirect('ecommerce:index')
                  

def inscription(request):
      form = UtilisateursForm(request.POST or None)

      if form.is_valid():
            utilisateur = form.save(commit=False)
            utilisateur.user = request.user
            utilisateur.save()
            return redirect('ecommerce:login')
      return render(request, 'inscription.html', {
            'form': form,
      })


def index(request):
      return render(request, 'index.html')


@login_required
def produit_client(request):  
      if request.user.is_superuser:
            produits = Product.objects.all()
      else:
            produits = Product.objects.filter(user=request.user)
      return render(request, 'produit_client.html', {
            'produits': produits,
      })

@login_required
def ajouter_au_panier(request, pk):
      if request.user.is_superuser:
            produits = get_object_or_404(Product, pk=pk)
      else:
            produits = get_object_or_404(Product, pk=pk, user=request.user)
      commandes = Commande(id_product=produits.id ,id_utilisateur = request.session['username'],etat='en_panier')
      #form = ProductsForm(request.POST or None, request.FILES or None, instance=produits)
      #if request.method == 'POST':
      commandes.user = request.user
      commandes.save()
      return redirect('ecommerce:panier')

@login_required
def panier(request):
      commandes = Commande.objects.filter(id_utilisateur = request.session['username'],etat='en_panier')
      allproducts = Product.objects.all()
      userProducts = []
      for product in allproducts:
            for commande in commandes:
                  if product.id == commande.id_product:
                        userProducts.append(product)

      #commandes = Commande.objects.filter(id_utilisateur = request.POST.get('username'),etat='en_panier')
      return render(request, 'panier.html', {
            'userProducts': userProducts,
      })

@login_required
def envoyer_commande(request):
      commandes = Commande.objects.filter(id_utilisateur = request.session['username'],etat='en_panier')
      for commande in commandes:
            commande.etat ='envoyer_au_admin'
            commande.save()
      return redirect('ecommerce:index')



def produit_detail(request,pk):
      product= get_object_or_404(Product, pk=pk)
      return render(request,'produit_detail.html',{'product':product})

class ProductView(DetailView):
      model = Product


def product_view(request, pk, template_name='template/product_detail.html'):
    product= get_object_or_404(Product, pk=pk)
    return render(request, template_name, {'object':product})


@login_required
def commande_list(request):
      if request.user.is_superuser:
            commandes = Commande.objects.all()
      else:
            commandes = Commande.objects.filter(user=request.user)
      return render(request, 'commande_list.html', {
            'commandes': commandes,
            'active_ajout' : '',
            'active_list':'',
            'active_commande' : 'active',
      })

@login_required
def product_list(request):
      if request.user.is_superuser:
            produits = Product.objects.all()
      else:
            produits = Product.objects.filter(user=request.user)
      return render(request, 'product_list.html', {
            'object_list': produits,
            'active_ajout' : '',
            'active_list':'active',
            'active_commande' : ''
      })


@login_required
def product_create(request):
      form = ProductsForm(request.POST or None, request.FILES)

      if form.is_valid():
            produits = form.save(commit=False)
            produits.user = request.user
            produits.save()
            return redirect('ecommerce:product_list')
      return render(request, 'product_form.html', {
            'form': form,
            'active_ajout' : 'active',
            'active_list':'',
            'active_commande' : ''
      })


@login_required
def product_update(request, pk):
      if request.user.is_superuser:
            produits = get_object_or_404(Product, pk=pk)
      else:
            produits = get_object_or_404(Product, pk=pk, user=request.user)
      form = ProductsForm(request.POST or None, request.FILES or None, instance=produits)
      if request.method == 'POST':
            update = form.save(commit=False)
            update.save()
            return redirect('ecommerce:product_list')
      return render(request,'product_form.html', {'form': form})


@login_required
def product_delete(request, pk):
      if request.user.is_superuser:
            produits = get_object_or_404(Product, pk=pk)
      else:
            produits = get_object_or_404(Product, pk=pk, user=request.user)
      if request.method == 'POST':
            produits.delete()
            return redirect('ecommerce:product_list')
      return render(request, 'confirm_delete.html', {'object': produits})