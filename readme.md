# Flask API Tests

**Quick Note-**
## Usually I only do pokemon examples but due to the nature of viewing different API's pokemon are not the only examples. If you are a hardcore pokemon person just use the pokemon data. 

### As of this current commit, all API's are working.

### This repo will bring you through what API's look like at their basic level, and show you how to manipulate that data.

## API Options :
### Chuck Norris
- Pull a completely random joke
- Get a random joke based on one of two categories (animals, movies)
### Weather
-Input a city and it will give you the temperature and weather description in celcius
- ** Please note **
- You need your own API key for this to work. You can get one at https://openweathermap.org/ You will place your key at api_key = in the main.py app under "def weather_results(): 
- Example : api_key = "0f04hv84h2n3v94jv"
### Pokemon
- A randomly picked pokemon out of the original 151 will show on the main screen with their picture.
- Input the name of a pokemon and it will pull their name, pokedex#, weight, type, and hp.