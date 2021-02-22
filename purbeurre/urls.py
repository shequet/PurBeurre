"""
Urls for the purbeurre app
"""

from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('legal_mentions/', views.legal_mentions, name='legal_mentions'),
    path('contact/', views.contact, name='contact'),
    path('product_substitute/', views.product_substitute, name='product_substitute'),
    path('product_substitute/<int:product_id>/<int:substitute_product_id>/add/',
         views.product_substitute_add,
         name='product_substitute_add'),
    path('product_substitute/<int:product_id>/<int:substitute_product_id>/delete/',
         views.product_substitute_delete,
         name='product_substitute_delete'),
    path('product/search/', views.product_search, name='product_search'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]
