from django.urls import path

from . import views

app_name = "shop"
urlpatterns = [
    path('', views.index, name='index'),
    path('products', views.ProductList.as_view(), name='product-all-list'), #product_all/ = /shop/product_all/
    path('products/search', views.ProductList.as_view(), name='product-search'),   #detailView
    path('products/<uuid:pk>', views.ProductDetail.as_view(), name='product-detail'),   #detailView
    ##############################
    #create form
    path('products/create', views.ProductCreate.as_view(), name='product-create'),   #createView
    path('products/update/<uuid:pk>', views.ProductUpdate.as_view(), name='product-update'),   #updateView
    ####################
    #ajax
    path('products/delete', views.ProductDeleteAjax, name='product-delete'),   #detailView

]