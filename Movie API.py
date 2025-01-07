import requests

# http://www.omdbapi.com/?apikey=[yourkey]&  - api for movies

api_key = '42393429'

a = True

while a == True:
    try: 
        movie_name = input("Type the name of the movie: ")
        new_movie_name = movie_name.replace(" ", "+")
        response = requests.get('http://www.omdbapi.com/?apikey='+api_key+'&t='+new_movie_name) # requesting data from the api 
        data = response.json() # If the response is accepted you can convert this into a readable format using .json() and then print the whole data or something specific from the data
        print(movie_name, "is rated", data['Rated'])
        a = False

    except:
        print("Error! Movie not found. Try again")

