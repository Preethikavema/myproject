from django.urls import path
from.import views
urlpatterns =[
    path('',views.home,name='home'),
    path('first/',views.firstpage,name='first'),
    path('second/',views.secondpage,name='second'),
    path('third/',views.thirdpage,name='third'),
    path('html_page/',views.html,name='html')
]