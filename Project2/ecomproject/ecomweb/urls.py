from . import views
from django.urls import path
app_name='ecomweb'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.regform, name='register'),
    path('login/', views.login, name='login'),
    path('logout/',views.logout,name='logout')
]
