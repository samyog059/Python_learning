with open("example.txt", "w") as f:
    f.write("Hello, World!\n")
    f.write("This is a new line.\n")
    f.write("Writing to a file is easy in Python.\n")

#Reading files from the same file to verify the content
with open("example.txt", "r") as f:
    content = f.read()
    print(content)