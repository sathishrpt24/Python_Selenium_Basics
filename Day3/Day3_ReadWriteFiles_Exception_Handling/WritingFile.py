file = open("demo1.txt","w+")
file.write("Hello How are you- file2")
file.close()

with open("demo1.txt","r") as readdemo:
    print(readdemo.read())
    readdemo.close()