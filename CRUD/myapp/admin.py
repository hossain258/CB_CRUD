from django.contrib import admin
from myapp.models import Student




@admin.register(Student)

class StudentAdmin(admin.ModelAdmin):
    list_display=['id','student_roll','student_name','student_course']
    
    


# Register your models here.
