import requests
import json
import csv
from datetime import datetime, timedelta

key = 'db5bd5cb135c49a0997145153241704'
endpoint = 'http://api.weatherapi.com/v1/history.json'

cities = ['Miass', 'London', 'Los Angeles', 'Colombo', 'Oslo']

end_date = datetime.now().date()
start_date = end_date - timedelta(days=30)

with open('weather_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['city', 'date', 'max_temp'])

    for city in cities:
        params = {
            'key': key,
            'q': city,
            'dt': start_date.strftime('%Y-%m-%d'),
            'end_dt': end_date.strftime('%Y-%m-%d')
        }
    
        response = requests.get(endpoint, params=params)
        data = response.json()
        
        for day in data['forecast']['forecastday']:
                date = datetime.strptime(day['date'], '%Y-%m-%d').date()
                row = [city, date, day['day']['maxtemp_c']]
                writer.writerow(row)
    