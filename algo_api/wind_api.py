from flask import Flask, request
import json

app = Flask(__name__)

lat= 0.0
lon=0.0
API_key = "cda97d333d8abcf19e10eed321011666"
cnt=16

@app.route('api.openweathermap.org/data/2.5/forecast/daily?lat={lat}&lon={lon}&cnt={cnt}&appid={API_key}', methods=['GET'])
def get_wind_speed():
    print(request.data["list"]["speed"])
