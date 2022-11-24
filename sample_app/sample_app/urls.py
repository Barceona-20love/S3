"""sample_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import pa

from django.urls import path
from .views import Products, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('', Products.as_view()),
    path('<int:pk>/', cache_page(60*10)(ProductDetailView.as_view()), name='product_detail'), # добавим кэширование на детали товара. Раз в 10 минут товар будет записываться в кэш для экономии ресурсов.
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('<int:pk>/update', ProductUpdateView.as_view(), name='product_update'),
    path('<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete'),
]
