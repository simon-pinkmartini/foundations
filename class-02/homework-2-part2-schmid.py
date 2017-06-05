#Simon Schmid
#2017-05-24
#Homework 2, Part 2

#DICTIONARIES

#1) Make a list called "countries" - it should contain seven different countries and NOT be in alphabetical order
countries = ['USA', 'Switzerland', 'France', 'Mexico', 'Germany']

#2) Using a for loop, print each element of the list
for country in countries:
    print (country)

#3) Sort the list permanently.
countries.sort()

#4) Display the first element of the list.
print (countries[0])

#5) Display the second-to-last element of the list.
print (countries[-2])

#6) Delete one of the countries from the list using its name.
countries.remove('USA')

#7) Using a for loop, print each country's name in all caps.
for country in countries:
    print (country.upper())

#1) Make a dictionary called 'tree' that responds to 'name', 'species', 'age', 'location_name', 'latitude' and 'longitude'. Pick a tree from: https://en.wikipedia.org/wiki/List_of_trees
tree = {
    'name': "Jaya Sri Maha Bodhi",
    'species': "Sacred fig",
    'age': 2300,
    'location_name': "Anuradhapura, Sri Lanka",
    'latitude': 8.344722,
    'longitude': 80.396667,
}

#2) Print the sentence "{name} is a {years} year old tree that is in {location_name}"
print (tree['name'], "is a", tree['age'], " years old tree that is in", tree['location_name'], ".")

#3) The coordinates of New York City are 40.7128° N, 74.0059° W. Check to see if the tree is south of NYC, and print "The tree {name} in {location} is south of NYC" if it is. If it isn't, print "The tree {name} in {location} is north of NYC"
if tree['latitude'] > 40.7128:
    print ("The tree", tree['name'], "in", tree['location_name'], "is north of NYC.")
else:
    print ("The tree", tree['name'], "in", tree['location_name'], "is south of NYC.")

#4) Ask the user how old they are. If they are older than the tree, display "you are {XXX} years older than {name}." If they are younger than the tree, display "{name} was {XXX} years old when you were born."
user_age = int(input("How old are you?"))
age_difference = user_age - tree['age']
if age_difference >= 0:
    print ("You are", age_difference, "years older than", tree['name'])
else:
    print (tree['name'], "was", tree['age']-user_age, "years old when you were born.")

#LIST OF DICTIONARIES

#1) Make a list of dictionaries of five places across the world - (1) Moscow, (2) Tehran, (3) Falkland Islands, (4) Seoul, and (5) Santiago. Each dictionary should include each city's name and latitude/longitude (see note above).
places = []
places.append({'name': "Moscow", 'latitude': 55.755826, 'longitude': 37.617300})
places.append({'name': "Tehran", 'latitude': 35.689197, 'longitude': 51.388974})
places.append({'name': "Falkland Islands", 'latitude': -51.796253, 'longitude': -59.523613})
places.append({'name': "Seoul", 'latitude': 37.566535, 'longitude': 126.977969})
places.append({'name': "Santiago", 'latitude': -33.448890, 'longitude': -70.669265})

#2) Loop through the list, printing each city's name and whether it is above or below the equator (How do you know? Think hard about the latitude.). When you get to the Falkland Islands, also display the message "The Falkland Islands are a biogeographical part of the mild Antarctic zone," which is a sentence I stole from Wikipedia.
for place in places:
    if place['latitude'] >= 0: hemisphere = "above"
    else: hemisphere = "below"
    print (place['name'], "is", hemisphere, "the equator.")
    if place['name'] == 'Falkland Islands': print ("The Falkland Islands are a biogeographical part of the mild Antarctic zone.")

#3) Loop through the list, printing whether each city is north of south of your tree from the previous section.
for place in places:
    if place['latitude'] >= tree['latitude']: hemisphere = "above"
    else: hemisphere = "below"
    print (place['name'], "is", hemisphere, "the", tree['name'], ".")
