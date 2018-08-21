from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import path
from products import views as products_views
from accounts import views as accounts_views
from products import views as products_views
from comments import views as comments_views
urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('',products_views.home,name='home'),
    path('login/', accounts_views.login_view, name='login'),
    path('signup/', accounts_views.signUp, name='signup'),
    path('home/',products_views.home_view, name='home_product'),
    path('logout/',accounts_views.logout_view, name='logout'),
    path('create_comment',comments_views.create_comment, name='create_comment'),
    path('product/<slug:slug>/',products_views.ProductDetailView.as_view(), name='detail_view'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
