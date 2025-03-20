count = 0
for numbers in range (1,10):
    
    if numbers % 2 == 0:
        count +=1
        print("EVEN NUMBER: ",numbers)
print("DONE")
print(f"we have {count} even numbers")