def format_number(number=0):
    if number > 1000000000:
        returnstring = str(number / 1000000000) + " billion"
    else:
        returnstring = str(number)
    return returnstring

rawnumber = int(input ("please type number:"))
formattednumber = format_number(rawnumber)
print ("Here's your formatted number:", formattednumber)
