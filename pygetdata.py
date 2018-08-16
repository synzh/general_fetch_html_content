import urllib.request
import os
from bs4 import BeautifulSoup

def RemoveDup(duplicate):
    final_list = []
    for item in duplicate:
        if item not in final_list:
            final_list.append(item)
    return final_list
    
# Put your link below
website = "http://TheWebsiteThatYouWantToFetch" 
os.environ["LANG"]="en_US.UTF-8"
with urllib.request.urlopen(website) as response:
   html = response.read()
   text = html.decode('utf-8')

soup = BeautifulSoup(text, 'lxml')
titles = soup.find_all('a')
titlesarr = []
for content in titles:
  if "title" in content.attrs:
    titlesarr.append(content.attrs['title'] + "\r\n" + content.attrs['href'])

Refiners = RemoveDup(titlesarr)
for ref in Refiners:
   print(ref)
   print ("==============================")
   
