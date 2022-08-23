file = open('test.txt', mode='r')

data = file.readline()

print(data)

file.close()

# alternative
with open('test.txt', mode='r') as file:
data = file.readline()
print(data)

try:
with open('sample/newfile.txt', 'w') as file:
    file.writelines(["Hello", "\nThere", "\nThird line!"])

with open('sample/newfile.txt', 'a') as file:
    file.writelines(["\nHello", "\nThere", "\nThird line!"])
except FileNotFoundError as e:
print("Error: ", e)
