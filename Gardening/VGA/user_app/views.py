from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.

def UserProjectHomePage(request):
    return render(request,'user_app/UserProjectHomePage.html',)


def weatherintegration(request):
    return render(request,'user_app/weatherintegration.html')


from django.http import JsonResponse

from django.shortcuts import render
from django.http import JsonResponse
import requests

API_KEY = 'e77153ac7e627cd798e837deadcb64dd'

def weatherintegration(request):
    return render(request, 'user_app/weatherintegration.html')

def get_weather(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        if not city:
            return JsonResponse({'error': 'City not provided'}, status=400)

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)

        if response.status_code == 200:
            return JsonResponse(response.json())
        elif response.status_code == 404:
            return JsonResponse({'error': 'City not found'}, status=404)
        else:
            return JsonResponse({'error': 'Failed to fetch weather data'}, status=response.status_code)

    return JsonResponse({'error': 'Invalid request'}, status=400)
