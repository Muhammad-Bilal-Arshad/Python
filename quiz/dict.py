# Store following word meanings in a python dictionary
#  table: "a piece of furniture", "list of facts and figures"
# cat : " a small animal"

dict = {}
dict["cat"] = "A small animal"
dict["table"] = ["a piece of furniture", " list of facts and figures"]
print(dict)



# METHOD 2

dict_2 = {}

dict_2.update({"cat":"A small animal", "table":["a piece of furniture","lists of facts and figures"]})
print(dict_2)