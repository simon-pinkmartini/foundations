#Create a dictionary
myself = {
    "name": "Simon",
    "age": 35,
    "home": "Upper East Side"
}

print (myself)
print (myself.keys())

#Reference item in dictionary
print ("My name is", myself["name"],".")

#Loop through the keys
for attribute in myself:
    print (attribute,":",myself[attribute])
