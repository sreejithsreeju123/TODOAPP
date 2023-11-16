from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView,FormView,ListView,DetailView,UpdateView,DeleteView
from django.contrib.auth.forms import UserCreationForm     
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import tasks

# Create your views here.
class Taskcreate(LoginRequiredMixin,CreateView):
    model=tasks
    fields=['task','description','completed',]
    success_url=reverse_lazy('task')
    template_name='taskcreate.html'
    
    def form_valid(self, form):
        form.instance.user=self.request.user
        return super(Taskcreate,self).form_valid(form)
    
    
class RegisterPage(FormView):
    template_name='register.html'
    form_class=UserCreationForm
    redirect_authenticated_user=True
    success_url=reverse_lazy('task')
    
    def form_valid(self,form):
        user = form.save()
        if user is not None:
            login(self.request,user)
        return super(RegisterPage,self).form_valid(form)
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('task')
        return super(RegisterPage,self).get( *args, **kwargs)

class CustomLoginView(LoginView):
    template_name='login.html'
    fields='__all__'
    redirect_authenticated_user=True
        
    def get_success_url(self):
        return reverse_lazy("task")
    
class Tasklist(LoginRequiredMixin,ListView):
    model=tasks
    context_object_name='task'
    template_name='tasklist.html'
    
    def get_queryset(self):
        return tasks.objects.filter(user=self.request.user)
    
class TaskDetailview(DetailView):
    model=tasks
    template_name='taskdetail.html'
    
class TaskUpdate(UpdateView):
    model=tasks
    fields=['task','description','completed']
    success_url=reverse_lazy('task')
    template_name='taskcreate.html'
    
class TaskDelete(DeleteView):
    model=tasks
    success_url=reverse_lazy('task')
    template_name='taskdelete.html'
    

