import os
directory_path ='/'
contents = os.listdir(directory_path)
for item in contents:
    # prints the name of the file or directory
    print(item)
    # print(os.path.join(directory_path, item))