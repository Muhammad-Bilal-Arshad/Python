def greet(first_name, last_name):
    print("Hello: ",first_name)
    print('welcome: ',last_name)

greet('bilal','arshad')



# two types of functions
# perform a task
# returning a value
# main diff is between pritning and returning
# by defauolt all functions return none
def get_greeting(name):
    return f"Hi{name}"


welcome = get_greeting("Bilal")
file = open("context.txt","w")
file.write(welcome)