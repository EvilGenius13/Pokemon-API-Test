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
        'result' : result
    }
    
    return render_template('cn_results.html', **context)

    

if __name__ == '__main__':
    server.config['ENV'] = 'development'
    server.run(debug = True)