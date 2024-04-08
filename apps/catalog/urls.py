from django.urls import path

from .views import CataloglistView, ProductByCategoryView

app_name = 'catalog'

urlpatterns = [
    path('', CataloglistView.as_view(), name='index'),
    path('<slug:slug>/', ProductByCategoryView.as_view() , name='category'),
    path('<slug:category_slug>/<slug:product_slug>/', ProductByCategoryView.as_view(), name='product'),
]