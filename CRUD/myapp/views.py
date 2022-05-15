from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from .models import Student 
from .forms import *
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.


def Home(request):
    diction={}
    return render(request, 'index.html', context =diction)



class studentListView(ListView):

    model = Student
    template_name='index.html'
    context_object_name='student_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        return context



class UpdatePostView(SuccessMessageMixin,UpdateView):
    model = Student
    form_class = StudentForm
    success_url = '/'
    #  messages.success=(" successfully Edited !!")
    template_name = 'student_update.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)                      
        return context
    
    success_message = 'The Student data successfully updated'
        

class DeletePostView(DeleteView):
    model = Student    
    success_url = '/'
    #  messages.success=(" successfully Edited !!")
    template_name = 'student_delete.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)                      
        return context
    

class CreateStudentView(SuccessMessageMixin, CreateView):
    model = Student
    form_class = StudentForm
    success_url = '/'
    #  messages.success=(" successfully Edited !!")
    template_name = 'student_create.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)                      
        return context
    success_message = 'The Student data successfully created'
    
class StudentDetailsView(DetailView):
    model =Student  
    # context_object_name='student_list' 
    
    #  messages.success=(" successfully Edited !!")
    template_name = 'student_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)                          
        return context
        
