#Create List
cat_ages = [5, 23, 6, 9]

#print List
print (cat_ages)

#Reference item in List
print (cat_ages[0])

#Sort List
print (sorted(cat_ages)) #sorts it but doesn't change it
print (cat_ages)
cat_ages.sort() #sorts it and stores it
print (cat_ages)

#Number of Element in the List
print ("Number of cats: ", len(cat_ages))

#Counting number of instances in List
print ("Number of 23s in list:", cat_ages.count(23))

#Max and min in List
print ("Maximum number is:", max(cat_ages))
print ("Maximum number is:", min(cat_ages))

#Mean of List
import statistics
print ("Mean is:", statistics.mean(cat_ages))

#Loop over List
for cat_age in cat_ages:
    cat_age = cat_age + 1
    print (cat_age)
