import os

file_path = '/Users/isisdev/Downloads/delete.png'

print(file_path)

if os.path.isfile(file_path):
    os.remove(file_path)
    print("File successfully deleted.")
else:
    print("This file does not exist.")
