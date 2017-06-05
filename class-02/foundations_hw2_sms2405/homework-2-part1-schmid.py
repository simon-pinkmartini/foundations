#Simon Schmid
#2017-05-24
#Homework 2, Part 1

#LISTS
"""
COMMENTS - JAGER HARTMAN
SCORe 4/5

* Interesting approach for number 7.  If you are to keep the subtractor variable set up the way it is, make sure to not
include the negative for these numbers.  Otherwise, if you wish to keep the negative, add the subtractor rather than subtract.
Otherwise there is a double negative and you're only adding the value.
Also, you don't use the multiplier variable.  Instead of number *30 it should be number * multiplier.

Consider the following code rewritten in a more mathematical (though robust) manner.

    for number in numberlist:
        translator = 0  #b from y=mx+b where x = number, y = output
        scalar = 1      #m from y=mx+b where x = number, y = output
        if number != -10:
            translator += -1
        if number%2 == 0:
            translator += 6
        if number < 10:
            scalar *= 30
            
        print ("Original:", number, "|   new number:", scalar * number + translator)

* Forgot to divide by 2 in question 8.  instead of sum(number_list) do (1.0/2) * sum(number_list) or sum(number_list)/2

* question 10 can be done more succinctly with an elif statement.
"""
#1) Make a list of the following numbers: 22, 90, 0, -10, 3, 22, and 48
numberlist = [22,  90, 0, -10, 3, 22, 48]

#2) Display the number of elements in the list.
print ("Number of Elements:", len(numberlist))

#3) Display the 4th element of this list.
print ("4th Element:", numberlist[3])

#4) Display the sum of the 2nd and 4th element of the list.
print ("Sum of 2nd and 4th Element:", numberlist[1] + numberlist[3])

#5) Display the 2nd-largest value in the list.
print ("2nd largest Value:", sorted(numberlist)[-2])

#6) Display the last element of the original unsorted list
print ("Last Element of original List:", numberlist[-1])

#7) For each number, display a number: if your original number is less than 10, multiply it by thirty. If it's also even, add six. If it's greater than 50 subtract ten. If it's not negative ten, subtract one. (For example: 2 is less than 10, so 2 * 30 = 60, 2 is also even, so 60 + 6 = 66, 2 is not negative ten, so 66 - 1 = 65.)
for number in numberlist:
    subtractor = 0
    summand = 0
    multiplier = 1
    if number != -10:
        subtractor = -1
    if number%2 == 0:
        summand = 6
    if number < 10:
        multiplier = 30
    print ("Original:", number, "|   new number:", (number * 30) + summand - subtractor)

#8) Display the sum of all of the numbers divided by two.
print ("The sum of all numbers is:", sum(numberlist))

#DICTIONARIES

#8) Sometimes dictionaries are used to describe multiple aspects of a single object. Like, say, a movie. Define a dictionary called movie that works with the following code.
 #print("My favorite movie is", movie['title'], "which was released in", movie['year'], "and was directed by", movie['director'])
movie = {
    'title': "Titanic",
    'year': 1997,
    'director': "James Cameron",
}

#9) On the lines after that, add entries to the movie dictionary for budget and revenue (you'll use code like movie['budget'] = 1000), and print out the difference between the two.
movie['budget'] = 1000
movie['revenue'] = 10000
profit = movie['revenue'] - movie['budget']
print (movie['title'], "made a profit of", profit, "dollars.")

#10) If the movie cost more to make than it made in theaters, print "It was a flop". If the film's revenue was more than five times the amount it cost to make, print "That was a good investment."
if profit < 0:
    print ("It was a flop.")
else:
    if movie['revenue'] > 5 * movie ['budget']:
        print ("That was a good investment")

#11) Sometimes dictionaries are used to describe the same aspects of many different objects. Make ONE dictionary that describes the population of the boroughs of NYC. Manhattan has 1.6 million residents, Brooklyn has 2.6m, Bronx has 1.4m, Queens has 2.3m and Staten Island has 470,000. (Tip: keeping it all in either millions or thousands is a good idea)
boroughs = {
    'Manhattan': 1.6,
    'Brooklyn': 2.6,
    'Bronx': 1.4,
    'Queens': 2.3,
    'Staten Island': 0.47,
}

#12) Display the population of Brooklyn.
print ("The population of Brooklyn is:", boroughs['Brooklyn'])

#13) Display the combined population of all five boroughs.
print ("The combined population is:", sum(boroughs.values()))

#14) Display what percent of NYC's population lives in Manhattan.
print (round(boroughs['Manhattan'] / sum(boroughs.values()) * 100), "percent of NYC's population lives in Manhattan." )
