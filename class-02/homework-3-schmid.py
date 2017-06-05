#Simon Schmid
#2017-05-27
#Homework 3

#LISTS

import statistics

numbers = [4, 5, 1, 10, 200, 34, 22, 19, 43, 56, 32, 11, 40, 82, 23, 43, 12, 65, 10]

#1) Count how many numbers are in the list. Use a for loop, do NOT use len.
#3) Count how many even numbers are in the list. Use a for loop.
#4) Count how many values are above the mean and how many are below the mean. Use a for loop.
#5) Total up the numbers. Use a for loop, do NOT use sum().
#6) Total up the numbers that are above the mean and the numbers below the mean. Use a for loop, do not use sum().
#7) Find the largest number. Use a for loop.

no_numbers = 0
no_even_numbers = 0
no_above_mean = 0
sum_total = 0
sum_above_mean = 0
sum_below_mean = 0
largest_number = 0
for number in numbers:
    no_numbers += 1
    if number%2 == 0:
        no_even_numbers += 1
    if number > statistics.mean(numbers):
        no_above_mean += 1
        sum_above_mean = sum_above_mean + number
    else:
        sum_below_mean = sum_below_mean + number
    sum_total = sum_total + number
    if number > largest_number:
        largest_number = number
print ("Number of numbers in the list:", no_numbers)
print ("Number of even numbers in the list:", no_even_numbers)
print ("Number of numbers above the mean:", no_above_mean)
print ("The total sum of the numbers is:", sum_total)
print ("The sum of all numbers above the mean is:", sum_above_mean)
print ("The sum of all numbers below the mean is:", sum_below_mean)
print ("The largest number is:", largest_number)

#2) Add another number to the list. You can pick the number!
numbers.append(23)

#8) You have a list of dogs, shown below. BUT YOU GOT ANOTHER DOG!!! His name is Maxwell, please add him to the list (and no, you don't just add him to the end of that line). Use a for loop.

dogs = ["Sparky", "Jane", "Matilda", "Blartsburg"]
dogs += ["Maxwell"]

#9) Make a list of all dogs that have names of 5 characters or less. Use a for loop.
dogs_with_small_names = 0
for dog in dogs:
    if len(dog) <= 5:
        dogs_with_small_names += 1
print ("Number of dogs with short names:", dogs_with_small_names)

#10) I'm on a web page with some links about Zurich, and the URL looks like this: http://important-swiss-things.ch/docs/download/ZH

#I want to get this link for every canton in Switzerland, not just Zurich, but I don't want to type the links manually. If I give you a list of the abbreviations, can you write out all of the URLs?

cantons = [ "ZH", "BE", "LU", "UR", "SZ", "OW", "NW", "GL", "ZG", "FR", "SO", "BS", "BL", "AR", "AI", "SG", "GR", "AG", "TG", "TI", "VD", "VS", "NE", "GE", "JU"]

print ("\n")
for canton in cantons:
    print ("http://important-swiss-things.ch/docs/download/" + canton)

#11) I'm trying to get some top-secret documents from top-secret-secrets.com, and while I know the URL pattern I don't want to type them all out individually!

#Each secret document has a document ID and is made up of 12 pages, pages "001.pdf" through "012.pdf". Each page is available at a different URL. For example, for the document ID of QQ7LTHM, the pages are available at

#www.top-secret-pdfs.com/content/secrets/QQ7LTHM/page/001.pdf
#www.top-secret-pdfs.com/content/secrets/QQ7LTHM/page/002.pdf
#www.top-secret-pdfs.com/content/secrets/QQ7LTHM/page/003.pdf
#...
#www.top-secret-pdfs.com/content/secrets/QQ7LTHM/page/012.pdf

#I have the following document IDs:

#qq7lthm
#jemsqhg
#O6itcke
#cp4Iua0
#bkijcmo
#ctoyjrm
#z8wc6xy
#zk4Bmm0

#Can you print out all of the URLs? Note that the document IDs need to be capitalized in the URL!
doc_ids = ["qq7lthm", "jemsqhg", "O6itcke", "cp4Iua0", "bkijcmo", "ctoyjrm", "z8wc6xy", "zk4Bmm0"]
for doc_id in doc_ids:
    for i in range(12):
        three_digit_number = "%03d" % i
        print ("www.top-secret-pdfs.com/content/secrets/" + doc_id.upper() + "/page/" + three_digit_number)

#DICTIONARIES

#1) Let's say we are terrible doctors and we have a patient. Define a dictionary called patient that works with the following code.

print ("\n")
patient = {
    'complaint': "fever",
}
print("Doctor, it looks like the patient's is complaining about", patient['complaint'])

#2) We aren't really listening to their complaint, but as more test results come in, we'll add these things to the patient's record. Add the following to the patient dictionary:

#Heart rate: 70
patient['heartrate'] = 70
#Temperature: 98.6
patient['temperature'] = 98.6
#Infection: No
patient['infection'] = False

#3) Now let's be doctors! First, if they have a heart rate about 100, we should tell them to relax. Store your diagnosis in a key called 'diagnosis'.
def diagnose(patient = {'complaint': "", 'heartrate': 0, 'temperature': 0, 'infection': False, 'diagnosis':"" }):
    if 95 < patient['heartrate'] < 105:
        patient['diagnosis'] = "relax"
    else:
        #* If their temperature is above 102 but they do not have an infection, they have heat stroke.
        if patient['temperature'] > 102 and patient['infection'] == False:
            patient['diagnosis'] = "heat stroke"
        #* If they have a high temperature and they have an infection, they have the flu.
        if patient['temperature'] > 102 and patient['infection'] == True:
            patient['diagnosis'] = "flu"
        #* If they have an infection but no high temperature, it's probably a cold.
        if patient['temperature'] < 102 and patient['infection'] == True:
            patient['diagnosis'] = "cold"
        #* If none of the above, tell them to take an aspirin and call you in the morning.
        if patient['temperature'] < 102 and patient['infection'] == False:
            patient['diagnosis'] = "aspirin"
    #When you are finished, print "Your diagnosis is _______."
    print ("Your diagnonsis is: ", patient['diagnosis'])

#4) Make a list of 3 different patients, each with different complaint, heart rate, temperature, and whether they have an infection or not. Use a for loop to diagnose each of them.
patients = [
    {'complaint': "sore throat", 'heartrate': 80, 'temperature': 105, 'infection': False, 'diagnosis':"" },
    {'complaint': "sore throat", 'heartrate': 100, 'temperature': 80, 'infection': True, 'diagnosis':"" },
    {'complaint': "sore throat", 'heartrate': 70, 'temperature': 100, 'infection': True, 'diagnosis':"" },
]
for patient in patients:
    diagnose(patient)

#5) Because you're such a bad doctor, they've put you in the back. You don't get to talk to patients any more, you just get to diagnose them based on their temperatures. And these ones aren't even sick! They just might have heat stroke.

#Using the following list and a for loop, create some new patient records (a list of dictionaries). Each dictionary should include a tempearture and whether the patient has heat stroke or not. When completed, my "for patient in patients..." code should be able to run.

temperatures = [ 99, 105, 98, 99, 100, 104, 105, 100 ]
records = []
for temperature in temperatures:
    if temperature > 102:
        diagnosis = "heatstroke"
    else:
        diagnosis = ""
    records.append({'complaint': "", 'heartrate': 0, 'temperature': temperature, 'infection': False, 'diagnosis': diagnosis})

for record in records:

  if record['diagnosis'] == 'heatstroke':
      print ("This patient has heat stroke!")
  else:
      print ("This patient does not have heat stroke")


#CSV Files

import csv

csvfile = open('countries.csv', 'r')
reader = csv.DictReader(csvfile)
data = list(reader)
csvfile.close()

#1) What are the rows in our dataset?
print ("The columns in the dataset are:")
for key in data[0].keys():
    print (key)

#2) How many countries do we have in our dataset?
print ("\nThe number of rows in the dataset is:", len(data))

#3) How many countries in Asia? How about North America?
no_asia = 0
no_america = 0
for country in data:
    if country['Continent'] == "Asia":
        no_asia += 1
    elif country['Continent'] == "N. America":
        no_america += 1
print ("\nThe number of asian countries is:", no_asia)
print ("The number of north american countries is:", no_america)

#4) What is the total population of the world?
total_pop = 0
for country in data:
    total_pop += int(country['Population'])
print ("\nThe total population of the world is:", total_pop)

#5) Which has a larger population, Africa or South America?
pop_africa = 0
pop_s_america = 0
for country in data:
    if country['Continent'] == "Africa":
        pop_africa += int(country['Population'])
    elif country['Continent'] == "S. America":
        pop_s_america += int(country['Population'])
if pop_africa > pop_s_america:
    print ("\nAfrica has the bigger population")
else:
    print ("\nSouth America has the bigger population")

#6) Calculate the total GDP of each country and print it out (right now it's per capita).
print ("\nHere's a list of all countries and their GDP:")
for country in data:
    print ("The GDP of", country['Country'], "is: ", int(country['Population']) * int(country['GDP_per_capita']), "dollars.")

#7) What is the median life expectancy of the world?
#life_expectancy = []
#for country in data:
#    life_expectancy.append(float(country['life_expectancy']))
life_expectancy = [float(country['life_expectancy']) for country in data]
print ("\nThe median life expectancy is: ", "%.2f" % statistics.median(life_expectancy), "years.")

#8) What is the median life expectancy of Europe?
life_expectancy = []
for country in data:
    if country['Continent'] == "Europe":
        life_expectancy.append(float(country['life_expectancy']))
print ("\nThe median life expectancy in Europe is: ", "%.2f" % statistics.median(life_expectancy), "years")

#9) Print out each country that has a below-average life expectancy.
life_expectancy = []
for country in data:
    life_expectancy.append(float(country['life_expectancy']))
avg_life_expectancy = statistics.mean(life_expectancy)
print ("\nThe countries with below-average life expectancy are:")
for country in data:
    if float(country['life_expectancy']) < avg_life_expectancy:
        print (country['Country'])

#10) Print out each country that has a below-average GDP but an above-average life expectancy.
GDP_per_capita =[]
for country in data:
    GDP_per_capita.append(float(country['GDP_per_capita']))
avg_GDP_per_capita = statistics.mean(GDP_per_capita)
print ("\nHere's a list of all countries with below-average GDP per capita and above-average life expectancy:")
for country in data:
    if float(country['GDP_per_capita']) < avg_GDP_per_capita and float(country['life_expectancy']) > avg_life_expectancy:
        print (country['Country'])

#11) Calculate the 75th percentile of GDP.
above_median_GDP_per_capita = []
median_GDP_per_capita = statistics.median(GDP_per_capita)
for country in data:
    if float(country['GDP_per_capita']) > median_GDP_per_capita:
        above_median_GDP_per_capita.append(float(country['GDP_per_capita']))
print ("\nThe 75th percentile of GDP per capita is:", statistics.median(above_median_GDP_per_capita))

#12) What percent of the world population has a life expectancy of below 50 years? Above 80 years?
no_countries_below_50 = 0
no_countries_above_80 = 0
for country in data:
    if float(country['life_expectancy']) < 50:
        no_countries_below_50 += 1
    elif float(country['life_expectancy']) > 80:
        no_countries_above_80 += 1
print ("\nThe percentage of countries with life expectancy below 50 is:", "%.1f" % float(no_countries_below_50 / len(data) * 100))
print ("\nThe percentage of countries with life expectancy above 80 is:", "%.1f" % float(no_countries_above_80 / len(data) * 100))
