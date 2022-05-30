
from django.shortcuts import render
from django.template import loader
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from sales.models import Product, Customer, Seller
# Create your views here.


def Index(request):
    return render(request, 'index.html')


# Product
class ProductList(ListView):
    model = Product
    template_name = 'product_list.html'


class ProductDetail(DetailView):
    model = Product
    template_name = 'product_detail.html'


class ProductCreate(CreateView):
    model = Product
    template_name = 'product_create.html'


class ProductUpdate(UpdateView):
    model = Product
    template_name = 'product_update.html'


class ProductDelete(DeleteView):
    model = Product
    template_name = 'product_delete.html'

# Customer


class CustomerList(ListView):
    model = Customer
    template_name = 'customer_list.html'


class CustomerDetail(DetailView):
    model = Customer
    template_name = 'customer_detail.html'


class CustomerCreate(CreateView):
    model = Customer
    template_name = 'customer_create.html'


class CustomerUpdate(UpdateView):
    model = Customer
    template_name = 'customer_update.html'


class CustomerDelete(DeleteView):
    model = Customer
    template_name = 'customer_delete.html'

# Seller


class SellerList(ListView):
    model = Seller
    template_name = 'seller_list.html'


class SellerDetail(DetailView):
    model = Seller
    template_name = 'seller_detail.html'


class SellerCreate(CreateView):
    model = Seller
    template_name = 'seller_create.html'


class SellerUpdate(UpdateView):
    model = Seller
    template_name = 'seller_update.html'


class SellerDelete(DeleteView):
    model = Seller
    template_name = 'seller_delete.html'
