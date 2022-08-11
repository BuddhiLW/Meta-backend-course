file = open('test.txt', mode='r')

data = file.readline()

print(data)

file.close()

# alternative
with open('test.txt', mode='r') as file:
    data = file.readline()
    print(data)

with open('newfile.txt', 'w') as file:
    file.writelines(["Hello", "There", "Third line!"])
