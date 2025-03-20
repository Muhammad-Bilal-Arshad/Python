number = 100
while number > 0:
    print(number)
    number //=2
#one way
# command = ""
# while command  != "quit":
#     command = input('enter your input: ')
#     print("YOUR INPUT: ",command)


#NORMAL WAY

while True:
    command = input('enter your input: ')
    print("YOUR INPUT: ",command)
    if command == 'quit':
        break