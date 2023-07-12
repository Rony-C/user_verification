import webbrowser
import argparse

#Parse CLI arguments
parser = argparse.ArgumentParser()
parser.add_argument('--input', '-i', required=True, help='Input file of IDs to check Verification.')
args = parser.parse_args()
file = args.input

#Open program in Chrome instead of default browser
chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

#Stores URLs to be checked
urlList = []

#Open file added via CLI
with open(file, 'r') as f:
    lines = f.readlines()
    for line in lines:
        #Gets ID digits only
        line = line.strip('\n')
        #Creates full URL and stores it in list
        url = f'https://test.com/login/{line}/check-id'
        urlList.append(url)      
#Loops through URL List and opens it in Chrome
for url in urlList:
        webbrowser.get(chrome_path).open_new_tab(url) 
#Prints how many IDs have been checked
print(f'{len(urlList)} IDs checked')
        
