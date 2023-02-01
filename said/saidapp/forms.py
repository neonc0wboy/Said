from .models import product, Market, Employee, Client, Order
from django.forms import ModelForm, TextInput, Textarea, NumberInput, DateInput, Select, CheckboxInput, SplitDateTimeWidget
from django import forms

class TaskForm(ModelForm):
    class Meta:
        model = product
        fields = ['title', 'task', 'price', 'distributor', 'type_good']
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
            "price": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите цену'
            }),
            "distributor": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Укажите поставщика'
            }),
            "type_good": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Укажите тип товара'
            }),
        }


class ShopForm(ModelForm):
    class Meta:
        model = Market
        fields = ['admin_id', 'address']
        widgets = {
            "address": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите адрес'
            }),
            "admin_id": Select(attrs={
                'choices': Market.objects.all()
            }),

        }


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['surname', 'name', 'middlename', 'telephone']
        widgets = {
            "surname": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите Фамилию'
            }),
            "name": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите Имя'
            }),
            "middlename": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите Отчество'
            }),
            "telephone": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите номер телефона'
            }),

        }


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['product_deal', 'delivery', 'address', 'idClient', 'payment', 'admin_id', 'date_order']

        widgets = {
            "product_deal": Select(attrs={
                'choices': product.objects.all()
            }),
            "delivery": CheckboxInput(attrs={
                'class': 'control-group'
            }),
            "date_order": DateInput(attrs={
                'type': 'text',
                'class': "vDateField"
                }),
            "address": Select(attrs={
                'choices': Market.objects.all()
            }),
            "admin_id": Select(attrs={
                'choices': Market.objects.all()
            }),
            "idClient": Select(attrs={
                'choices': Client.objects.all()
            }),
            "payment": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Укажите способ оплаты'
            }),

        }

class RegisterForm(forms.Form):
    username = forms.CharField()
    email    = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username is taken")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password2 != password:
            raise forms.ValidationError("Passwords must match.")
        return data