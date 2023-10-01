from django.urls import path
from .views import input,curd,cv,delete,pdf
urlpatterns = [
    path('', input,name='input'),
    path('al', curd, name='curd'),
    path('cv/ <int:id>', cv, name='cv'),
    path('delete/ <int:id>', delete, name='delete'),
    path('pdf/<int:id>', pdf, name='pdf'),
    
]