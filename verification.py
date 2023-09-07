import webbrowser,argparse, pyperclip, time

#Parse CLI arguments
parser = argparse.ArgumentParser()
parser.add_argument('--input', '-i', required=True, help='Input file of IDs to check Verification.')
args = parser.parse_args()
file = args.input

#Open program in Chrome instead of default browser
chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

#Stores URLs to be checked
urlList = []

#Create file and write to it
def updateIDs():
        print("Creating ID list...")
        with open('/Users/rony/vs_code/python/work_files/idVerification/ids.txt', 'w+') as f:
                f.write(pyperclip.paste())

def processURLs():
        print("Processing URLs...")
#Open file added via CLI
        with open(file, 'r') as f:
                ids = f.readline().strip("/n")
                idList = ids.split(",")
                for id in idList:
                        url = f'https://admin.gigable.app/admin/users/{id}/identity-check'
                        urlList.append(url)
        #    lines = f.readline()
        #    for line in lines:
        #        #Gets ID digits only
        #        line = line.strip(',')
        #        #Creates full URL and stores it in list
        #        url = f'https://admin.gigable.app/admin/users/{line}/identity-check'
        #        urlList.append(url)      
        #Loops through URL List and opens it in Chrome
        counter = 1
        for url in urlList:
                if (counter % 10 == 0):
                        print('Sos beag... Resuming shortly...')
                        print(f'{counter} IDs checked...')
                        time.sleep(10)
                webbrowser.get(chrome_path).open_new_tab(url) 
                counter += 1
#Initialisation
updateIDs()
processURLs()
#Prints how many IDs have been checked
print(f'{len(urlList)} IDs checked')
        