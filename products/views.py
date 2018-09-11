from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView
from products.models import Product, ProductImage, ProductCategory
from comments.forms import CommentForm
from django.views.generic.list import ListView
import stripe
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products':products})
def home_view(request):
    products = Product.objects.all()
    images = ProductImage.objects.all()
    return render(request, 'products/home.html', {'products':products, 'images':images})

class ProductDetailView(DetailView):
    """docstring for DetailView."""
    model = Product
    template_name="products/detail_view.html"
    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        comment_form=CommentForm()
        context['comment_form'] = comment_form
        return context

class ProductBuyView(DetailView):

    model = Product
    template_name = 'products/buy.html'

    def post(self,request,*args, **kwargs):

        stripe.api_key = settings.STRIPE_API_KEY
        token = request.POST['stripeToken']
        product = self.get_object()
        charge = stripe.Charge.create(
            amount = product.price * 100,
            currency = 'usd',
            description = 'cobro por {} del usuario {}'.format(product.title,request.user.first_name),
            statement_descriptor = "cobro al usuario {}".format(request.user.username),
            source = token
        )
        return render(request,'products/succes.html', {'title':product.title, 'price':product.price})

def searchProduct(request, query):
    query = request.GET['query']
    product = Product.objects.filter( title__icontains=query)
    if product:
        return render(request, 'products/home.html',{'products':product})
    else:
        return render(request, 'products/home.html',{'error':'No se encuentra el producto'})

def productCategory(request, category):
    products = Product.objects.all()
    return render(request, 'products/category.html',{'products':products, 'category': category})
