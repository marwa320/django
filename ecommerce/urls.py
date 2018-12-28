from django.urls import path

from . import views

app_name = "ecommerce"

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('inscription/', views.inscription, name='inscription'),
    path('index/', views.index, name='index'),
    path('produit_client/', views.produit_client, name='produit_client'),
    path('ajouter_au_panier//(?P<pk>\d+)$', views.ajouter_au_panier, name='ajouter_au_panier'),
    path('panier/', views.panier, name='panier'),
    path('produit_detail/(?P<pk>\d+)$', views.produit_detail, name='produit_detail'),
    path('product_list/', views.product_list, name='product_list'),
    path('commande_list/', views.commande_list, name='commande_list'),
    path('envoyer_commande/', views.envoyer_commande, name='envoyer_commande'),
    path('product_create/', views.product_create, name='product_create'),
    path('product_update/(?P<pk>\d+)$', views.product_update, name='product_update'),
    path('product_delete/(?P<pk>\d+)$', views.product_delete, name='product_delete'),
    path('view/<int:pk>', views.ProductView.as_view(), name='product_view'),

]
