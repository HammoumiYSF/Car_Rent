from django.conf.urls import url
from first_app import views

urlpatterns=[
url('',views.index,name='Home'),
url('login/', views.login, name='login'),
]
