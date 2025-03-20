course = "   Python programming"

# everything in python is an object and object have functions we call methods that we can access using dot notation


print(course.upper()) # new string with capitalized letters, original string remains same
print(course.lower()) # new string with lower letters, original string remains same
print(course.title()) # new string with capitalized first character of each word, original string remains same
print(course.strip()) # to remove white spaces, original string remains same
print(course.lstrip()) # to remove white spaces from left, original string remains same
print(course.rstrip()) # to remove white spaces from right, original string remains same
print(course.find("pr")) # to find index of given character or a string, in case of string index is given when the first character of provided string mathces, -1 means not found
print(course.replace("pr","j")) # to replace the first provided string with second priovided one
print("pro" in course) # check if the given string/value exists in the input string (course here) returns a boolen, true or false
print("pro" not in course) # check if the given string/value does not exist in the input string (course here) returns a boolen, true or false
print(course)