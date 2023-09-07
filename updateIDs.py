import pyperclip

#Create file and write to it
with open('directory_path/ids.txt', 'w+') as f:
    f.write(pyperclip.paste())
