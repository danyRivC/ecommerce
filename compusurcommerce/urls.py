from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import path
from products import views as products_views
from accounts import views as accounts_views
from products import views as products_views
from comments import views as comments_views
from contacts import views as contacts_views
from django.contrib.auth.decorators import login_required, permission_required


urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('',products_views.home,name='home'),
    path('login/', accounts_views.login_view, name='login'),
    path('signup/', accounts_views.signUp, name='signup'),
    path('home/',products_views.home_view, name='home_product'),
    path('logout/',accounts_views.logout_view, name='logout'),
    path('create_comment',comments_views.create_comment, name='create_comment'),
    path('product/<slug:slug>/',products_views.ProductDetailView.as_view(), name='detail_view'),
    path('products/<slug:slug>/buy/', login_required(products_views.ProductBuyView.as_view()),name="buy"),
    path('contacts/', contacts_views.contacts, name='contacts'),
    path('search/<query>/', products_views.searchProduct, name='search_product'),
    path('products/categories/<category>', products_views.productCategory, name='categories')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
