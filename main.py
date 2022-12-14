from flask import Flask, request, render_template
import random
import json
import requests

server = Flask(__name__)

@server.route('/')
def homepage():
    #please note I use @server instead of @app
    return render_template('index.html')

@server.route('/chucknorris')
def chuck():
    return render_template('chucknorris.html')

@server.route('/cn_results')
def chuck_results():
    random_joke = request.args.get('random_joke')
    category = request.args.get('category')
    apicall = requests.get('https://api.chucknorris.io/jokes/random')
    joke_json = apicall.json()
    if random_joke == 'yes':
        result = joke_json['value']
    elif random_joke == 'no':
        if category == 'animal':
            apicall = requests.get('https://api.chucknorris.io/jokes/random?category=animal')
            joke_json = apicall.json()
            result = joke_json['value']
        elif category == 'movie':
            apicall = requests.get('https://api.chucknorris.io/jokes/random?category=movie')
            joke_json = apicall.json()
            result = joke_json['value']
    context = {
        'result' : result,
    }
    
    return render_template('cn_results.html', **context)

@server.route('/weather')
def weather():
    return render_template('weather.html')

@server.route('/w_results')
def weather_results():
    city = request.args.get('city')
    api_key = ""
    url = "https://api.openweathermap.org/data/2.5/weather?q=%s&units=metric&appid=%s" % (city, api_key)
    apicall = requests.get(url)
    data = apicall.json()
    current = data["main"]["temp"]
    description = data["weather"][0]["description"]
    context = {
        'description' : description,
        'current' : current,
        'city' : city,
    }
    return render_template('w_results.html', **context)

@server.route('/pokemon')
def pokemon():
    random_pokemon_num = random.randint(1, 151) 
    poke_url = "https://pokeapi.co/api/v2/pokemon/%s" % (random_pokemon_num)
    api_call = requests.get(poke_url)
    poke_data = api_call.json()
    name = poke_data['name']
    sprite = poke_data['sprites']['front_default']
    

    context = {
        'name' : name,
        'sprites' : sprite,
    }

    return render_template('pokemon.html', **context)

@server.route('/p_results')
def poke_results():
    poke_choice = request.args.get('choice')
    poke_url = "https://pokeapi.co/api/v2/pokemon/%s" % (poke_choice)
    api_call = requests.get(poke_url)
    poke_data = api_call.json()
    name = poke_data['name']
    sprite = poke_data['sprites']['front_default']
    type = poke_data['types'][0]['type']['name']
    poke_dex = poke_data['id']
    weight = poke_data['weight']
    hp = poke_data['stats'][0]['base_stat']
    context = {
        'name' : name,
        'sprite' : sprite,
        'type' : type,
        'poke_dex' : poke_dex,
        'weight' : weight,
        'hp' : hp,
    }

    return render_template('/p_results.html', **context)

if __name__ == '__main__':
    server.config['ENV'] = 'development'
    server.run(debug = True, port = 3000)