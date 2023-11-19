import requests

#12.1
request = 'https://api.chucknorris.io/jokes/random'
response = requests.get(request).json()
print(response['value'])

# 12.2
api = '1737b1b55068501f60e1db8789e54867'
while True:
    city = input("Type a city name: ")
    if city == "":
        print("Stopping")
        break
    else:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}"
        data = requests.get(url)
        data_json = data.json()
        if data_json['cod'] == '404':
            print("Invalid city. Try again!")
            continue
        else:
            weather = data_json['weather'][0]['main']
            degrees = data_json['main']['temp'] - 273.15
            degrees_max = data_json['main']['temp_max'] - 273.15
            degrees_min = data_json['main']['temp_min'] - 273.15
            degrees_feel = data_json['main']['feels_like'] - 273.15
            print(data_json)
            print(f"City: {city.capitalize()}")
            print(f"Weather: {weather}")
            print(f"Degrees: {degrees:.2f}º")
            print(f"Min. Degrees: {degrees_min:.2f}º")
            print(f"Max. Degrees: {degrees_max:.2f}º")
            print(f"Feels like: {degrees_feel:.2f}º\n")
            break