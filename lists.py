# can store data of any type


marks = [12,15,18,23,675]
print(marks)
print(marks[0])
# marks[0] = 'bilal'
# print(marks)

#lists can be sliced , same rules as strings in slicing
#list methods

marks.append(4) # to add an element at the end
print(marks)
marks.sort() # ascending sort
print(marks)
marks.sort(reverse=True) # descending sort
print(marks)
marks.reverse() # to reverse a list
print(marks)
marks.insert(2, 'hello') # to add ab element at a specified index
print(marks)