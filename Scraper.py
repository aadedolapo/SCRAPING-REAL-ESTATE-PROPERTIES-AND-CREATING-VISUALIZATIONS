import requests
from bs4 import BeautifulSoup
import pandas as pd

l=[]

base_url="https://www.privateproperty.com.ng/property-for-rent?page="

items = int(soup.find_all('div',{'class':'listing-count'})[0].get_text().strip().split()[-1])
listings = 25
page_nr = int(items/listings)

for page in range(1,int(page_nr),1):
    print(base_url+str(page))
    r= requests.get(base_url+str(page))
    c= r.content
    soup= BeautifulSoup(c,"html.parser")
        
    classes = ["item-body table-cell"]
    for class_ in classes:
        real=soup.find_all("div",{"class":class_})

        for i in list(range(0,len(real))):
            d={}
            d["page" ] = page
            try:
                d["title"]=real[i].find('h2', {'class':'property-title'}).get_text().strip()
            except (IndexError,TypeError,AttributeError) as e:
                d["title"]= None
            try:
                d["description"]=real[i].find('div', {'class':'property-title-default'}).get_text().strip()
            except (IndexError,TypeError,AttributeError) as e:
                d["description"]= None
            try:
                d["bedrooms"]= real[i].find('span',{'class':'h-beds'}).get_text().strip()
            except (IndexError,TypeError,AttributeError) as e:
                d["bedrooms"]= None 
            try:
                d["bathrooms"]= real[i].find('span',{'class':'h-baths'}).get_text().strip()
            except (IndexError,TypeError,AttributeError) as e:
                d["bathrooms"]= None
            try:
                d["garage"] = real[i].find('span',{'class':'h-garage'}).get_text().strip()
            except (IndexError,TypeError,AttributeError) as e:
                d["garage"] = None
            try:
                d["location"] = real[i].find('div', {'class':'property-location overflow-ellipse-mobile'}).get_text().strip()
            except (IndexError,TypeError,AttributeError):
                d["location"] = None
            try:
                d["location_s"] = real[i].find('div', {'class':'property-location overflow-ellipse-mobile'}).get_text().strip().split()[-1]
            except(IndexError,TypeError,AttributeError):
                d['location_s'] = None
            try:
                d["price"]=real[i].find('div', {'class':'info-row price'}).get_text().strip().split()[0]
            except (IndexError,TypeError,AttributeError) as e:
                d["price"] = None            
            l.append(d)
            #print(l)

            
df = pd.DataFrame(l)
print(df.head())