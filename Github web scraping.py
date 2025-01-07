import requests


username = input('Input the github username: ')

response = requests.get('https://api.github.com/users/'+username) #if response is = <Response [200]> that means the response has been accepted

data = response.json() # data = to the github user information

print(data['avatar_url']) # This prints out the profile picture of the github user 