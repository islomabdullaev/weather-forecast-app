from django.urls import path
from pages.views import index, history

app_name = 'pages'

urlpatterns = [
    path('', index, name='index'),
    path('history/', history, name='history')
]