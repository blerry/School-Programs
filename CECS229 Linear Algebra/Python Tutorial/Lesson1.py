
colors = ["red", "green", "blue", "purple"]
for i in colors:
    print(i)
#To loop every key and value from a dictionary
#for k, v in dict.items():
#	    print(k,v)
stocks = {'IBM': 146.48,'MSFT':44.11,'CSCO':25.54}
#print out all the keys
for c in stocks:
    print(c)
#print key n values
for k, v in stocks.items():
    print("Code : {0}, Value : {1}".format(k, v))