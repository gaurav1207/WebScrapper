import requests
import bs4
import lxml
import csv
b=input("Enter site to scrape from")
f=0
h=requests.get(b)
s=bs4.BeautifulSoup(h.text,'lxml')
k=[]
o=0;
file=open("Text file name to safe the info at","w")
for i in s.find_all('a',href=True):
  
  if(i['href'][0]=='h'):
   file.write(i['href'])
   file.write("\n")
print("Done")   
