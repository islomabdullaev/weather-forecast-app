from datetime import datetime
import requests
from django.shortcuts import render
from django.db.models import Count

from users.models import History
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="users/login")
def index(request):
    q = request.GET.get("q")
    context = {}
    history = History.objects.filter(user=request.user).last()
    if history:
        context['city'] = history.city
        context['main'] = history.main
        context['description'] = history.description
        context['temp'] = round(history.degree)
        context['weekday'] = history.created_at.strftime("%A")
        context['month'] = history.created_at.strftime("%B")
        context['day'] = history.created_at.day
    if q:
        url = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={q}&appid=74e591b860f44157397a248704e9842c")
        data = url.json()
        weather = data['weather']
        main = weather[0]['main']
        description = weather[0]['description']
        city = data['name']
        # here we are converting from Kelvin (K) to Celsius (°C)
        temp = data['main']['temp'] - 273.15

        now = datetime.now()

        context = {
            "main": main,
            "description": description,
            "city": city,
            "temp": round(temp),
            "weekday": now.strftime("%A"),
            "month": now.strftime("%B"),
            "day": now.day
        }
        History.objects.create(
            user=request.user,
            city=city,
            degree=temp,
            main=main,
            description=description
        )
    return render(request=request, template_name="weather.html", context=context)


@login_required(login_url="users/login")
def history(request):
    data = History.objects.filter(user=request.user)
    city_counts = History.objects.values('city').annotate(count=Count('city')).filter(user=request.user)
    context = {
        "data": data,
        "city_counts": city_counts
    }
    return render(request=request, template_name="history.html", context=context)