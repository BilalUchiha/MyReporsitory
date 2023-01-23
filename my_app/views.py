from django.shortcuts import render
from django.views.generic import CreateView,DeleteView,ListView,DetailView,UpdateView,View,FormView
from .models import Customer,City
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from .filter import CustomerFilter
# Create your views here.
class RegisterPage(FormView):
    template_name = 'my_app/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('login')


    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request,user)
        return super(RegisterPage,self).form_valid(form)

class CustomLoginView(LoginView):
    template_name = 'my_app/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('customers')
class BookList(LoginRequiredMixin,ListView):
   model = Customer


class CreateCustomer(LoginRequiredMixin,CreateView):
   model = Customer
   fields = '__all__'
   success_url = reverse_lazy('customers')

class CreatCity(LoginRequiredMixin,CreateView):
   model = City
   fields = '__all__'
   success_url = reverse_lazy('city')


class CityList(LoginRequiredMixin,ListView):
   model = City

class DeleteCustomer(DeleteView):
   model = Customer
   success_url = reverse_lazy('customers')
class UpdateCustomer(UpdateView):
   model = Customer
   fields = '__all__'
   success_url = reverse_lazy('customers')

class Display(LoginRequiredMixin,View):
   def get(self,request):
      str="0"
      instance = City.objects.all()
      instance2 = Customer.objects.all()
      if 'q' in request.GET:
         q= request.GET['q']
         instance2 =Customer.objects.all().filter(customername__icontains = q )
      else:
        instance = City.objects.all()
        instance2 = Customer.objects.all()
      return render(request,'my_app/customercity_form.html',{'city':instance,'Customer':instance2,'SelectedValue':str})
   def post(self,request):
      str=request.POST['selectCity']
      instance = City.objects.all()
      
      if str != "0":
         instance2 = Customer.objects.all().filter(address_id=str)
      else:
         instance2 = Customer.objects.all()

      # Entry.objects.all().filter(pub_date__year=2006)
      return render(request,'my_app/customercity_form.html',{'city':instance,'Customer':instance2,'SelectedValue':str})
     
3
   

def  SearchPost(request):

      return HttpResponse("this is string")

