import requests
from bs4 import BeautifulSoup
import re
from csv import writer
import os

os.system("COLOR A0")
os.system("TITLE Made by Anshuman Fauzdar")

# Check URL webparsing

url2 = input("Enter your qwiklab account URL: ")

page2 = requests.get(url2)

soup2 = BeautifulSoup(page2.text, 'html.parser')

for el2 in soup2.find_all('span', attrs={'class': 'ql-subhead-1 l-mts'}):
    main2 = el2.get_text()
    edit2 = re.sub(r'\n','', main2)
    f = open("check.txt", "a")
    f.write(edit2 + '\n')
    f.close()

# convert master data into array
a_file = open("master.txt", "r")

list_of_lists = []
for line in a_file:
  list_of_lists.append(line)

a_file.close()

# convert check data into array

b_file = open("check.txt", "r")

list_of_lists2 = []
for line in b_file:
  list_of_lists2.append(line)

b_file.close()

# compare in multiple text

print("[x] Means completed and [ ] Not completed \n")

for x in list_of_lists:
    flag = 0
    for y in list_of_lists2:
        if x == y :
            print("[x] " + x)
            flag = 1

    if flag == 0 :
        print("[ ] " + x)

os.remove("check.txt")
