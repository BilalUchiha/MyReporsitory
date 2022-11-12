from django.urls import path
from . import views
urlpatterns = [
    path('',views.BookList.as_view(),name='customers'),
    path('create_customer',views.CreateCustomer.as_view(),name='createcustomer'),
    path('city',views.CityList.as_view(),name="city"),
    path('create_city',views.CreatCity.as_view(),name="createcity"),
    path('delete_customer/<int:pk>',views.DeleteCustomer.as_view()),
    path('update_customer/<int:pk>',views.UpdateCustomer.as_view()),
]