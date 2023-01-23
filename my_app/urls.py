from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('logout',LogoutView.as_view(next_page ='login'),name='logout'),
    path('login',views.CustomLoginView.as_view(),name = 'login'),
    path('register/',views.RegisterPage.as_view(),name ='register'),
    path('',views.BookList.as_view(),name='customers'),
    path('create_customer',views.CreateCustomer.as_view(),name='createcustomer'),
    path('city',views.CityList.as_view(),name="city"),
    path('create_city',views.CreatCity.as_view(),name="createcity"),
    path('delete_customer/<int:pk>',views.DeleteCustomer.as_view()),
    path('update_customer/<int:pk>',views.UpdateCustomer.as_view()),
    path('search',views.Display.as_view(),name='search'),
    path("SearchPost",views.SearchPost, name='SearchPost')
]