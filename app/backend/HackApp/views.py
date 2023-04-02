from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.files.storage import default_storage
import os
import requests
import json, csv

@csrf_exempt
def test(request):
    if request.method=='GET':
        print("ahoj")
        return JsonResponse("Chill",safe=False)

@csrf_exempt
def weather(request):
    if request.method=='GET':
        API_KEY = "db4897bc76b7dc4b33fc3830abe755be"
        CITY_NAME = "Kosice"
        COUNTRY_CODE = "SK"  # Slovakia
        UNITS = "metric"  # For temperature in Celsius

        url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY_NAME},{COUNTRY_CODE}&appid={API_KEY}&units={UNITS}"

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            main = data["main"]
            weather_desc = data["weather"][0]["description"]
            temp = main["temp"]
            temp_min = main["temp_min"]
            temp_max = main["temp_max"]
            humidity = main["humidity"]

            weather_data = {
                "weather_desc": weather_desc,
                "temp": temp,
                "temp_min": temp_min,
                "temp_max": temp_max,
                "humidity": humidity
            }
            return JsonResponse(weather_data,safe=False)
        else:
            return JsonResponse("Fail",safe=False)

@csrf_exempt
def amenity(request,amenity_type):
    if request.method=='GET':
        overpass_url = "http://overpass-api.de/api/interpreter"
        amenity_types = [amenity_type]
        lat, lon = 48.723798, 21.257799
        radius = 1000

        def create_query(amenity_type, lat, lon, radius):
            return f"""
            [out:json];
            node[amenity={amenity_type}](around:{radius},{lat},{lon});
            out;
            """

        def fetch_pois(amenity_type):
            query = create_query(amenity_type, lat, lon, radius)
            response = requests.get(overpass_url, params={'data': query})

            if response.status_code == 200:
                return response.json()["elements"]
            else:
                print(f"Error fetching data for amenity type: {amenity_type}")
                print(f"Status code: {response.status_code}")
                print(f"Error message: {response.text}")
                return []

        data = {}
        for amenity_type in amenity_types:
            data[amenity_type] = fetch_pois(amenity_type)
        return JsonResponse(data,safe=False)



        fetch_pois_and_print_json(amenity_types, lat, lon, radius)

@csrf_exempt
def stations(request,stationss):
    if request.method=='GET':
        print(stationss)
        csv_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'zastavky.csv')

        data = []

        with open(csv_file, newline='', encoding='ISO-8859-1') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)

        filtered_data = [item for item in data if item['Sever'] == stationss]

        return JsonResponse(filtered_data,safe=False)

@csrf_exempt
def buslines(request):
    if request.method=='GET':
        csv_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'linky.csv')

        data = []

        with open(csv_file, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)

        return JsonResponse(data,safe=False)




