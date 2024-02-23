
from django.urls import path

from .import views

urlpatterns = [
    path('', views.add,name='home'),
    # path('details/',views.details,name='details')
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:taskid>/',views.update,name='update'),
]