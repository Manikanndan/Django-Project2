from django.urls import path
from app2.views import *

app_name='application2'

urlpatterns =[
    path('app2_function/',app2_function,name='app2_function'),
]