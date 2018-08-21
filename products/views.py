from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from products.models import Product, ProductImage
from comments.forms import CommentForm
from django.views.generic.list import ListView
import stripe
from django.conf import settings
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')
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
