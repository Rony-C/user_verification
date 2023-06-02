import webbrowser
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', '-i', required=True, help='Input file of IDs to check Verification.')

args = parser.parse_args()
file = args.input

urlList = []

with open(file, 'r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip('\n')
        url = f'https://test.com/login/{line}/check-id'
        urlList.append(url)      
for url in urlList:
        webbrowser.open_new_tab(url) 
print(f'{len(urlList)} IDs checked')
        
