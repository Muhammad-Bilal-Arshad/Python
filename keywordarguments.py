def increment(number, by):
    return number + by

result = increment( 2,by= 1) # by = 1 is a keyword argument
print(result)


#DEFault parameter

def increase(number,by = 1): # here we have setted the by to a defailt value, optional parameters should always come after required aprameters

    return number+by

print(increase(3)) # u can see we didn't need to give a value here
print(increase(4,2)) # here we ghave the value which overrode the default value 