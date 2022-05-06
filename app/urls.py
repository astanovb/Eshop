from django.urls import path
from . import views

urlpatterns = [
    path('login', views.LogIN, name='login'),
    path('', views.index, name='index'),
    path('categories/<path:pk>', views.category, name='cats' ),
    path('buy/<int:pk>', views.buypage, name='product' ),
    path('search', views.search_results, name ='search'),
    path('logout', views.LogOUT, name='logout')
]
