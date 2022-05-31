from django.urls import path
from sales import views

urlpatterns = [
    path('', views.ProductList.as_view(), name='product_list'),
    # Product
    path('product_search/', views.ProductSearch.as_view(), name='product_search'),
    path('product_list/', views.ProductList.as_view(), name='product_list'),
    path('product_detail/<pk>', views.ProductDetail.as_view(), name='product_detail'),
    path('product_create/', views.ProductCreate.as_view(), name='product_create'),
    path('product_update/<pk>', views.ProductUpdate.as_view(), name='product_update'),
    path('product_delete/<pk>', views.ProductDelete.as_view(), name='product_delete'),
    # Customer
    path('seller_search/', views.SellerSearch.as_view(), name='seller_search'),
    path('customer_list/', views.CustomerList.as_view(), name='customer_list'),
    path('customer_detail/<pk>', views.CustomerDetail.as_view(),
         name='customer_detail'),
    path('customer_create/', views.CustomerCreate.as_view(), name='customer_create'),
    path('customer_update/<pk>', views.CustomerUpdate.as_view(),
         name='customer_update'),
    path('customer_delete/<pk>', views.CustomerDelete.as_view(),
         name='customer_delete'),
    # Seller
    path('customer_search/', views.CustomerSearch.as_view(), name='customer_search'),
    path('seller_list/', views.SellerList.as_view(), name='seller_list'),
    path('seller_detail/<pk>', views.SellerDetail.as_view(), name='seller_detail'),
    path('seller_create/', views.SellerCreate.as_view(), name='seller_create'),
    path('seller_update/<pk>', views.SellerUpdate.as_view(), name='seller_update'),
    path('seller_delete/<pk>', views.SellerDelete.as_view(), name='seller_delete'),

]
