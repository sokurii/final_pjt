from django.urls import path
from . import views

app_name = 'finlifes'
urlpatterns = [
    path('deposit-products/', views.deposit_products),
    path('deposit-product-options/<fin_prdt_cd>/', views.deposit_product_options),
    path('saving-products/', views.saving_products),
    path('saving-product-options/<fin_prdt_cd>/', views.saving_product_options),
    path('exchangeinfo/', views.exchangeinfo),
    # path('deposit-products/top-rate/', views.top_rate),
]