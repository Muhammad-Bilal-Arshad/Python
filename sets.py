#sets are unique like 1,2,3,4 is ok but 1,2,3,2 is not cz 2 is repeating and non unique
# duplicate items will be ignored
# SET IS MUTABLE but ITS elements are immutable
#set is a collection of unordered items , each ELEMENTTTT in a set must be unique and immutable



collection_2 = {1,2,2,2,"hello",'world',"hello"}
print(collection_2)
print(len(collection_2))

collection = set()
print(collection)
print(type(collection))
collection.add("element") # adds an element
collection.remove("element") # removes an element
collection.clear() # empties the set
collection.pop() # removes a random value
collection.union(collection_2) # a set union just like in maths
collection.intersection(collection_2) # a set intersection just like in MATHS