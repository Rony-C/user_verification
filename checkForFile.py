import os, pyperclip
from pandas import *

#Search downloads folder, find file and open
def checkForFile():
    for file in os.listdir("directory_path"):
        if not file.startswith("file name"):
            pass
        else:
            print(f"Found file '{file}' successfully")
            fullPath = f"directory_path/{file}"
            data = read_csv(fullPath)
            ids = data["Users → ID"].tolist()

            #convert list to string
            listToStr = ','.join([str(elem) for elem in ids])
            #copy to clipboard
            pyperclip.copy(listToStr)
            
checkForFile()
