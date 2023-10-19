from django.urls import path
from . import views
app_name='mylistapp'
urlpatterns = [
    path('',views.demo,name='demo'),
    path('carlist/<int:car_id>/',views.details,name='details'),
    path('add/',views.add_car,name='add_car'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')
]