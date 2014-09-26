#simple script to strip relevant info from a web page stored on hard drive table using beautiful soup
from bs4 import BeautifulSoup
import os
import csv
from pprint import pprint
from urlparse import urljoin
os.chdir('archeage')


#f = csv.writer(open("archeage.csv", "w"))
#f.writerow(
toscrape = 'RawGoods.html'

soup = BeautifulSoup (open(toscrape))
table = soup.find("table", {"id" : "MainItemTable"})
rows = table.find_all('tr')   
for row in rows:
   item_id = row.findAll("td", {"class":"dt-id"})
   name = row.findAll('b')
   data = item_id, name
   print data

#would like to iterate further on this to clean the data of the tags ( use beautifulsoup generator maybe?)
#and then dump it into a database(mongoDB). 
