import os

directory_path = r'C:\Users\UseR\Desktop\python chapter-01'

contents = os.listdir(directory_path)

for item in contents:
    print(item)