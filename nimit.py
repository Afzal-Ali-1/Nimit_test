file=open("data.txt")
data=file.read()
for var in data:
    print(var)
file.close()