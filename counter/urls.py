from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('calorie/',views.calorie,name='calorie'),
    path('calorieintake/',views.calorieintake,name='calorieintake'),
    path('daily/',views.daily,name="daily"),
    path('daily/addfood',views.addfood,name='addfood'),
    path('about/',views.about, name='about'), 
]