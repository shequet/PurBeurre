from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('legal_mentions/', views.legal_mentions, name='legal_mentions'),
    path('contact/', views.contact, name='contact'),
    path('myfood/', views.myfood, name='myfood'),
    path('product/search/', views.product_search, name='product_search'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]

