# Daniel Mc Callion

with open("myfile.txt", "w") as f:
    print(f.tell())
    f.write("Hello, from the line!\n")
    print(f.tell())