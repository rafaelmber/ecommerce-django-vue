from django.urls import path, include

from product import views

urlpatterns = [
    path('latest-products/', view=views.LatestProductsList.as_view()), 
    path('products/<slug:category_slug>/<slug:product_slug>/',view=views.ProductDetail.as_view())
]