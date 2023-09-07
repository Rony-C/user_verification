import pyperclip

#Create file and write to it
with open('/Users/rony/vs_code/python/work_files/ids.txt', 'w+') as f:
    f.write(pyperclip.paste())
