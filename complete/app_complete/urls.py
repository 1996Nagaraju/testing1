from django.conf.urls import url
from app_complete import views

app_name='app_complete'

urlpatterns=[
    url('register/',views.register,name='register'),
    url('user_login/',views.user_login,name='user_login')
]