from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

"""said URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin, auth
from django.urls import path, include, re_path
from saidapp import views
urlpatterns = []
urlpatterns += [
    #re_path(r'^$', views.home, name='home'),
    path('', views.home, name='home')
    #re_path('products', views.products, name='products'),
    #re_path('markets/', views.Markets, name='markets'),
    #re_path('create/', views.create, name='create'),
    #re_path('createShop/', views.createShop, name='createShop'),
    #re_path('clients/', views.Client_page, name='client_page'),
    #re_path('createClient/', views.createClient, name='createShop'),
    #re_path('orders/', views.Orders, name='orders_page'),
    #re_path('createOrder', views.createOrder, name='createOrder'),
]

urlpatterns += [
    #path('', views.home, name='home'),
    #path('admin/', admin.site.urls),
    #path('files/', )
    re_path('accounts/logout', views.logout, name='logout'),
    re_path('admin/', admin.site.urls, name='admin'),
    re_path('accounts/', include('django.contrib.auth.urls'), name='accounts'),
    re_path('accounts/profile/', views.profile, name='profile'),
    re_path('accounts/logout/', views.logout, name='logout')
] 
urlpatterns += staticfiles_urlpatterns()

urlpatterns += [
    re_path('logout', views.logout, name='logout')
]
urlpatterns += staticfiles_urlpatterns()


urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls'), name='accounts'),
 #   path('accounts/profile/', views.profile, name='profile'),
    path('accounts/logout/', views.logout, name='logout'),
    path('accounts/password_change/', views.passwordchange, name='passwordchange')
]

urlpatterns += [
#    url(r'^$', views.home, name='home'),
#    url(r'^home$', views.home, name='home'),
    re_path('products/', views.products, name='products'),
    re_path('markets/', views.Markets, name='markets'),
    re_path('create/', views.create, name='create'),
    re_path('createShop/', views.createShop, name='createShop'),
    re_path('accounts/logout/', views.log_out, name='log_out'),
    re_path('clients/', views.Client_page, name='client_page'),
    re_path('createClient/', views.createClient, name='createShop'),
    re_path('orders/', views.Orders, name='orders_page'),
    re_path('createOrder/', views.createOrder, name='createOrder'),
    re_path('edit/', views.edit, name='UpdateOrder'),
    re_path('<int:pk>/delete', views.order_delete, name='DeleteProducts'),
	
]#urlpatterns += static(
#    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
#)
#urlpatterns += static(
#    settings.STATIC_URL, document_root=settings.STATIC_ROOT
#)
urlpatterns += [
    re_path('accounts/', include('django.contrib.auth.urls')),
    re_path('admin/', admin.site.urls, name='admin'),
    ]

