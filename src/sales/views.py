
from ast import NamedExpr
from urllib import response
from django.shortcuts import render
from django.template import loader
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from sales.models import Product, Customer, Seller
from django.urls import reverse_lazy
from django.http import HttpResponse
# Create your views here.


def Index(request):
    return render(request, 'index.html')


# Product

# def productSearch(request):
#     return render(request, "product/product_search.html")


# def search(request):
#     # return HttpResponse(f"Searching for {request.GET['product_id']}")
#     if request.GET['product_id']:
#         product_id = request.GET['product_id']
#         product = Product.objects.filter(id__icontains=product_id)
#         return render(request, "product/product_search_result.html", {"product_id": product_id})
#     else:
#         response = "Ingresar un número de producto"
#     return HttpResponse(response)

class SearchResultsView(ListView):
    model = Product
    template_name = 'product/product_search_result.html'
    queryset = Product.objects.filter(id__icontains=1)


class ProductList(ListView):
    model = Product
    template_name = 'product/product_list.html'


class ProductDetail(DetailView):
    model = Product
    template_name = 'product/product_detail.html'


class ProductCreate(CreateView):
    model = Product
    template_name = 'product/product_create.html'
    success_url = reverse_lazy('product_list')
    fields = ['name', 'description', 'price']


class ProductUpdate(UpdateView):
    model = Product
    template_name = 'product/product_update.html'
    success_url = reverse_lazy('product_list')
    fields = ['name', 'description', 'price']


class ProductDelete(DeleteView):
    model = Product
    template_name = 'product/product_delete.html'
    success_url = reverse_lazy('product_list')

# Customer


class CustomerList(ListView):
    model = Customer
    template_name = 'customer/customer_list.html'


class CustomerDetail(DetailView):
    model = Customer
    template_name = 'customer/customer_detail.html'


class CustomerCreate(CreateView):
    model = Customer
    template_name = 'customer/customer_create.html'
    success_url = reverse_lazy('customer_list')
    fields = ['name', 'phone', 'email']


class CustomerUpdate(UpdateView):
    model = Customer
    template_name = 'customer/customer_update.html'
    success_url = reverse_lazy('customer_list')
    fields = ['name', 'phone', 'email']


class CustomerDelete(DeleteView):
    model = Customer
    template_name = 'customer/customer_delete.html'
    success_url = reverse_lazy('customer_list')


# Seller


class SellerList(ListView):
    model = Seller
    template_name = 'seller/seller_list.html'


class SellerDetail(DetailView):
    model = Seller
    template_name = 'seller/seller_detail.html'


class SellerCreate(CreateView):
    model = Seller
    template_name = 'seller/seller_create.html'
    success_url = reverse_lazy('seller_list')
    fields = ['name', 'phone', 'email']


class SellerUpdate(UpdateView):
    model = Seller
    template_name = 'seller/seller_update.html'
    success_url = reverse_lazy('seller_list')
    fields = ['name', 'phone', 'email']


class SellerDelete(DeleteView):
    model = Seller
    template_name = 'seller/seller_delete.html'
    success_url = reverse_lazy('seller_list')
