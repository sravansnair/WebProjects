from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from todoapp.models import Task
from .forms import Todoforms
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView,DeleteView
# Create your views here.
class Tasklistview(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task1'

class Taskdetail(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task'

class updateview(UpdateView):
    model = Task
    template_name = 'updatenew.html'
    context_object_name = 'task'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('detail',kwargs={'pk':self.object.id})

class deleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('listview')



def home(request):
    task1 = Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task=Task(name=name,priority=priority,date=date)
        task.save()
    return render(request,'home.html',{'task1':task1})

def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    task=Task.objects.get(id=id)
    f=Todoforms(request.POST or None,instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'update.html',{'f':f,'task':task})