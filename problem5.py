import os

# Select the directory whose Content you want to list
directory_path = "/"

# Use the os module to list the directory Content
Contents = os.listdir(directory_path)


print(Contents)