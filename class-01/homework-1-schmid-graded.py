#Simon Schmid
#05-22-2017
#Homework 1

#Python: 10/10
#Command line: 5/5


#GK->I love your format_number function! Writing your own functions is a great way to keep your code organized and readable!

#6 define number formatting function used later
def format_number(number=0):
    if number > 1000000000:
        returnstring = str(round(number / 1000000000, 1)) + " billion"
    elif number > 1000000:
        returnstring = str(round(number / 1000000, 1)) + " million"
    else:
        returnstring = str(round(number, 0))
    return returnstring

#GK->Excellent use of a while loop to make sure you get the right input.
#GK-> Can you make it even simpler? Any way to accomplish the same task without using a separate "okanswer" variable?
#1 Ask year and test if given year is valid
okanswer = 0
while okanswer is 0:
    year = int(input("What year were you born in? "))
    if year > 2017:
        print ("Year is in the future. Please try again.")
    else:
        okanswer = 1

#2 Tell user how old they are
age = 2017 - year
print ("You are", age, "years old.")

#3 How many times their heart has beaten (assuming heart rate of 70/min)
strokes = age * 365 * 24 * 60 * 70
print ("Your heart has beaten", format_number(strokes), "times in your life.")

#4 How many times a whale's heart has beaten (assuming heart rate of 40/min)
whale_strokes = age * 365 * 24 * 60 * 40
print ("A blue whale's heart would have beaten", format_number(whale_strokes), "times in that time.")

#5 How many times a rabbit's heart has beaten (assuming heart rate of 200/min)
rabbit_strokes = age * 365 * 24 * 60 * 200
print ("A rabbit's heart would have beaten", format_number(rabbit_strokes), "times in that time.")

#7 Age in venus years (assuming one yenus year to be 224.65 earth days)
venus_years = age * 365 / 224.65
print ("In Venus years, you are", format_number(venus_years), "years old.")

#8 Age in neptune years (assuming one yenus year to be 164.5 earth years)
neptune_years = age / 164.5
print ("In Neptune years, you are", format_number(neptune_years), "years old.")

#9 Check if they are also born in 1981 and #10 give age difference

#GK->Changing the order of my_year - year vs. year - my_year is very clever! Another solution for getting the absolute value of the difference is using abs()

my_year = 1981
if year == my_year:
    print ("You are born in the same year as I am.")
else:
    print ("You aren't born in the same year as I am.")
    if year < my_year:
        print ("You are", my_year - year, "years older than I am.")
    else:
        print ("You are", year - my_year, "years younger than I am.")

#11 Check even or odd years
if year%2 == 0:
    evenodd = "even"
else:
    evenodd = "odd"
print ("You were born in an", evenodd, "year.")

#12 Number of Championships for the Pittsburgh Steelers
if year > 2009:
    no_steelers = 0
elif year > 2006:
    no_steelers = 1
elif year > 1980:
    no_steelers = 2
elif year > 1979:
    no_steelers = 3
elif year > 1976:
    no_steelers = 4
elif year > 1975:
    no_steelers = 5
else:
    no_steelers = 6
print ("The Pittsburgh Steelers have won", no_steelers, "superbowls in your lifetime.")

#Name of the US President in birth year
presidents = {2017: "Trump", 2009: "Obama", 2001: "Bush II", 1993: "Clinton", 1989: "Bush I", 1981: "Reagan", 1977: "Carter", 1974: "Ford", 1969: "Nixon", 1963: "Johnson", 1961: "Kennedy", 1953: "Eisenhower", 1945: "Truman", 1933: "Roosevelt"}

#GK-> This is a great solution! Excellent, very readable, clear and efficient.
for president_year in presidents.keys():
    if year >= president_year:
        president_name = presidents[president_year]
        break
print ("In your year of birth,", president_name, "was the president of the US.")
