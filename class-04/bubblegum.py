#import the request library
import request

#1 Url to retrieve info on "Burny"
url = "http://api.bubblegum.com/gum/d0g/show.json?APITKEY=b335"

#make http request
response = request.get(url)

#get a json feed out of the response
data = response.json()

#2 Construct new url to get info on flavors
url = "http://api.bubblegum.com/flavors/list.json?APIKEY=b335"

#make http request
response = request.get(url)

#get json feed out of response
data = response.json()

print (data['flavors'])

#3 Url to get info on "minty frest"
url = "http://api.bubblegum.com/gum/ca7/show.json?APIKEY=b335"

response = request.get(url)
data = response.json()
if data['popularity'] > 100:
    print ("Wow, that's popular!")
