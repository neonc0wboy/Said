from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns =+ [
        re_path('/', views.home, name='home'),
    url(r'^home$', views.home, name='home'),
    url('products', views.products, name='products'),
    url('markets/', views.Markets, name='markets'),
    url('create/', views.create, name='create'),
    url('createShop/', views.createShop, name='createShop'),
    url('accounts/logout/', views.log_out, name='log_out'),
    url('clients/', views.Client_page, name='client_page'),
    url('createClient/', views.createClient, name='createShop'),
    url('orders/', views.Orders, name='orders_page'),
    url('createOrder', views.createOrder, name='createOrder'),
    url('change_password', admin.site.urls, name='passwordchange')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls, name='admin'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
