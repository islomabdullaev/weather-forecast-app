from django.urls import path
from users.views import signin, register, signout

app_name = 'users'

urlpatterns = [
    path('', register, name='register'),
    path('login/', signin, name='login'),
    path('logout/', signout, name='logout'),
]