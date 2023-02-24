from django.shortcuts import render
from django.contrib.auth import logout as log_out
from typing import List, Any, Union
from django.forms import NumberInput, TextInput, Textarea
from django.shortcuts import render, redirect
from django.views.generic import UpdateView, DeleteView
from django.db.models import Value as V
from django.db.models import Q
from .models import product, Market, Client, Order, Employee
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from typing import List, Any, Union

from django.forms import NumberInput, TextInput, Textarea
from django.shortcuts import render, redirect
from django.views.generic import UpdateView, DeleteView
from django.db.models import Value as V
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import product, Market, Client, Order
from .forms import TaskForm, ShopForm, ClientForm, OrderForm

#def navbar(request):
#	return render(request, 'saidapp/home.html')
# Create your views here.
def home(request):
    if request.user.is_anonymous:
        return redirect('login')
    else:
        return render(request, 'saidapp/home.html')

def logout(request):
    if request.user.is_anonymous:
        return redirect('login')
    if request.user.is_authenticated:
        log_out(request)
        return render(request, 'registration/logout.html')

def profile(request):
    return render(request, 'registration/login.html')

def passwordchange(request):
    return render(request, 'registration/password_change_form.html')

def products(request):
    if request.user.is_anonymous:
        return redirect('login')
    if request.user.is_authenticated:
        global el
        search_query = request.GET.get('search', '')
        if search_query:
            tasks = product.objects.filter(Q(title=search_query) | Q(task=search_query))
        else:
            tasks = product.objects.all()
        return render(request, 'saidapp/products.html',
                      {'title': 'Список лекарств', 'tasks': tasks})

def createShop(request):
    if request.user.is_anonymous:
        return redirect('login')
    if not request.user.has_perm('admin_permission'):
        return redirect('LogError')
    if request.user.is_authenticated:
        error = ''
        if request.method == 'POST':
            form = ShopForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('markets')
            else:
                error = 'Форма была неверной'
        form = ShopForm()
        context = {
            'form': form,
            'error': error
        }
        return render(request, 'saidapp/createShop.html', context)

def Orders(request):
    global od
    if request.user.is_anonymous:
        return redirect('login')
    if request.user.is_authenticated:
        search_query = request.GET.get('search', '')
        if search_query:
            Orders = Order.objects.filter(Q(product_deal=search_query) | Q(idOrder=search_query))
        else:
            Orders = Order.objects.all()
        return render(request, 'saidapp/orders.html',
                      {'title': 'Список заказов', 'Order': Orders})


def createOrder(request):
    if request.user.is_anonymous:
        return redirect('login')
    if not request.user.has_perm('admin_permission'):
        return redirect('LogError')
    if request.user.is_authenticated:
        error = ''
        form = OrderForm()
        if request.method == 'POST':
            form = OrderForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('orders_page')
            else:
                error = 'Форма была неверной'
        context = {
            'form': form,
            'error': error
        }
        return render(request, 'saidapp/createOrder.html', context)

def order_add(request):
    return redirect('/admin/saidapp/order/add/')
    
def order_edit(request):
	return redirect('/admin/saidapp/order/edit/')

    
def order_delete(request):
    return render('/admin/saidapp/order/{{el.id}}delete/')

    
def Markets(request):
	markets = Market.objects.all()
	if request.user.is_anonymous: 
		return redirect('login')
		if request.user.is_authenticated: global em
		search_query = request.GET.get('search', '')
		if search_query:
			markets = Market.objects.filter(Q(address=search_query))
		else:
			markets = Market.objects.all()
			return render(request, 'saidapp/markets.html', {'title': 'Список аптек', 'markets': markets})
		return render(request, 'saidapp/markets.html', {'title': 'Список аптек', 'markets': markets})


from typing import List, Any, Union
from django.forms import NumberInput, TextInput, Textarea
from django.shortcuts import render, redirect
from django.views.generic import UpdateView, DeleteView
from django.db.models import Value as V
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import product, Market, Client, Order
from .forms import TaskForm, ShopForm, ClientForm, OrderForm


# Create your views here.


def Markets(request):
    markets = Market.objects.all()
    if request.user.is_anonymous:
        return redirect('login')
    if request.user.is_authenticated:
        global em
        search_query = request.GET.get('search', '')
        if search_query:
            markets = Market.objects.filter(Q(address=search_query))
        else:
            markets = Market.objects.all()
        return render(request, 'saidapp/markets.html', {'title': 'Список Аптек', 'markets': markets})


def products(request):
    if request.user.is_anonymous:
        return redirect('login')
    if request.user.is_authenticated:
        global el
        search_query = request.GET.get('search', '')
        if search_query:
            tasks = product.objects.filter(Q(title=search_query) | Q(task=search_query))
        else:
            tasks = product.objects.all()
        return render(request, 'saidapp/products.html',
                      {'title': 'Список товаров', 'tasks': tasks})


def create(request):
    if request.user.is_anonymous:
        return redirect('login')
    if not request.user.has_perm('admin_permission'):
        return redirect('LogError')
    if request.user.is_authenticated:
        error = ''
        if request.method == 'POST':
            form = TaskForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('products')
            else:
                error = 'Форма была неверной'

        form = TaskForm()
        context = {
            'form': form,
            'error': error
        }
        return render(request, 'saidapp/create.html', context)


def edit(request):
    if request.user.is_anonymous:
        return redirect('login')
    if not request.user.has_perm('admin_permission'):
        return redirect('LogError')
    if request.user.is_authenticated:
        error = ''
        if request.method == 'POST':
            form = TaskForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('products')
            else:
                error = 'Форма была неверной'
        form = TaskForm()
        context = {
            'form': form,
            'error': error
        }
        return render(request, 'saidapp/edit.html', context)


def createShop(request):
    if request.user.is_anonymous:
        return redirect('login')
    if not request.user.has_perm('admin_permission'):
        return redirect('LogError')
    if request.user.is_authenticated:
        error = ''
        if request.method == 'POST':
            form = ShopForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('markets')
            else:
                error = 'Форма была неверной'
        form = ShopForm()
        context = {
            'form': form,
            'error': error
        }
        return render(request, 'saidapp/createShop.html', context)



#def password_reset(request):
 #\   return render(request, 'accounts:password_reset')



def Client_page(request):
    if request.user.is_anonymous:
        return redirect('login')
    if request.user.is_authenticated:
        global ej
        search_query = request.GET.get('search', '')
        if search_query:
            list_clients = Client.objects.filter(Q(surname=search_query))
        else:
            list_clients = Client.objects.all()
        return render(request, 'saidapp/clients.html',
                      {'title': 'Список клиентов', 'list_clients': list_clients})

def employee(request):
    if request.user.is_anonymous:
        return redirect('login')
    if request.user.is_authenticated:
        global ej
        search_query = request.GET.get('search', '')
        if search_query:
            list_employee = Employee.objects.filter(Q(surname=search_query))
        else:
            list_employee = Employee.objects.all()
        return render(request, 'saidapp/empoloyee.html',
                      {'title': 'Список сотрудников', 'list_employee': list_employee})


def createClient(request):
    if request.user.is_anonymous:
        return redirect('login')
    if not request.user.has_perm('admin_permission'):
        return redirect('LogError')	
    if request.user.is_authenticated:
        error = ''
        if request.method == 'POST':
            form = ClientForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('client_page')
            else:
                error = 'Форма была неверной'

        form = ClientForm()
        context = {
            'form': form,
            'error': error
        }
        return render(request, 'saidapp/createClient.html', context)


def createOrder(request):
    if request.user.is_anonymous:
        return redirect('login')
    if not request.user.has_perm('admin_permission'):
        return redirect('LogError')
    if request.user.is_authenticated:
        error = ''
        form = OrderForm()
        if request.method == 'POST':
            form = OrderForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('orders_page')
            else:
                error = 'Форма была неверной'
        context = {
            'form': form,
            'error': error
        }
        return render(request, 'saidapp/createOrder.html', context)

def order_add(request):
    return redirect('/admin/saidapp/order/add/')
