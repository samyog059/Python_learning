import os
directory_path ='/'
contents = os.listdir(directory_path)
for item in contents:
    print(item)
    # print(os.path.join(directory_path, item))