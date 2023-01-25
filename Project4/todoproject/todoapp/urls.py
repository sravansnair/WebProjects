from . import views
from django.urls import path
app_name='todoapp'
urlpatterns = [
    path('', views.home,name='home'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('listview/',views.Tasklistview.as_view(),name='listview'),
    path('detail/<int:pk>/',views.Taskdetail.as_view(),name='detail'),
    path('cbvupdate/<int:pk>/',views.updateview.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.deleteview.as_view(),name='cbvdelete')
]