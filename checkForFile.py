import os, pyperclip
from pandas import *

#Search downloads folder, find file and open
def checkForFile():
    for file in os.listdir("/Users/rony/vs_code/python/work_files/idVerification"):
        if not file.startswith("ID Verification"):
            pass
        else:
            print(f"Found file '{file}' successfully")
            fullPath = f"/Users/rony/vs_code/python/work_files/idVerification/{file}"
            data = read_csv(fullPath)
            ids = data["Users → ID"].tolist()

            #convert list to string
            listToStr = ','.join([str(elem) for elem in ids])
            #copy to clipboard
            pyperclip.copy(listToStr)
            
checkForFile()