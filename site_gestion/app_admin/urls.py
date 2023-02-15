from django.urls import path
from .views import *

urlpatterns=[
    path('',dashboard,name='dashboard'),
    path('my_articles/',user_articles,name='my-articles'),
    path('ajouter-article/',AddArticle.as_view(),name='ajouter-article'),
    path('update-article/<int:pk>', UpdateArticle.as_view(),name='update-article'),
    path('delete-article/<int:pk>',DeleteArticle.as_view(),name='delete-article'),
    path('add-panier/<int:id>',add_panier,name='add_panier'),
    path('mon_panier/',panier,name='panier'),
    path('incrementer-quantite/<int:achat_id>/', ajouter_achat, name='incrementer_achat'),
    path('decrementer-quantite/<int:achat_id>/', retirer_achat, name='decrementer_achat'),
    path('generate-pdf/', generer_pdf, name='generate-pdf'),



]