counts = dict()
fname = input('Enter File name: ')
fhandle = open(fname)
line = fhandle.read()
words = line.split()
print('Words: ',words)
print('Counting...')
for word in words:
    counts[word] = counts.get(word,0)+1
max_key = max(counts, key=counts.get)
all = counts.values()
max_value = max(all)
z = str(max_value)
print(counts)
print('Most Used word: ' + max_key)
print('Number of time it is used: ' + z)

