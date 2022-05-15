from django.urls import path,include
from . import views 
from .views import *
from .views import studentListView
from .views import UpdatePostView
from .views import DeletePostView
from .views import StudentDetailsView

urlpatterns = [
   
   

    path('', studentListView.as_view(), name='student-list'),
    path('create', CreateStudentView.as_view(), name='student-create'),
    path('view/<int:pk>',StudentDetailsView.as_view(), name='student-detail'),
    path('update/<int:pk>',UpdatePostView.as_view(), name='student-update'),
    path('delete/<int:pk>',DeletePostView.as_view(), name='student-delete'),
    
]
    

