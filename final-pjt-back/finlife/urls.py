from django.urls import path
from . import views

app_name = 'finlifes'
urlpatterns = [
    path('deposit-products/', views.deposit_products),
    path('saving-products/', views.saving_products),
    path('exchangeinfo/', views.exchangeinfo),
    # path('deposit-products/top-rate/', views.top_rate),
]