from django.urls import path
from .views import GetTask

urlpatterns = [
    path('task/', GetTask.as_view()),
    
]
