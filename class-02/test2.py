import csv
import statistics

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
life_expectancy = []
for country in data:
    life_expectancy.append(float(country['life_expectancy']))
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
