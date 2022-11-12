from django.shortcuts import render
from django.views.generic import CreateView,DeleteView,ListView,DetailView,UpdateView
from .models import Customer,City
from django.urls import reverse_lazy
# Create your views here.

def home(request):
   return render (request, 'my_app/index.html')
class BookList(ListView):
   model = Customer

class CreateCustomer(CreateView):
   model = Customer
   fields = '__all__'
   success_url = reverse_lazy('customers')

class CreatCity(CreateView):
   model = City
   fields = '__all__'
   success_url = reverse_lazy('city')


class CityList(ListView):
   model = City

class DeleteCustomer(DeleteView):
   model = Customer
   success_url = reverse_lazy('customers')
class UpdateCustomer(UpdateView):
   model = Customer
   fields = '__all__'
   success_url = reverse_lazy('customers')


