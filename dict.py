# key value pairs
# KEY:Value
#unordered, mutable and dont allow duplciate keys


dict = {
    "name":"bilal",
    "age": 15,
    "marks": [25,67,34],
    "is_adult" : True,
    "interest": ('dict','set'),
    "friend" : {
    "name":"bilal",
    "age": 15,
    "marks": [25,67,34],
    "is_adult" : True,
    "interest": ('dict','set')
}
}

# keys cannot be lists or dictionaries, values can be any data type

print(dict)
print(dict["name"])
dict["name"] = "bilal arshad"
print(dict)
dict["surname"] = "satti"
print(dict)
null_dict = {}
print(type(null_dict))

print(dict.keys()) # return all keys
print(dict.values())# return all values
print(dict.items())# return all key value pairs as tuples
print(dict.get("name"))# return the valeu of provided key
dict.update({"city":"hello", "sport":"football"}) # isnerts the specidfied item to the dictionary
print(dict)
