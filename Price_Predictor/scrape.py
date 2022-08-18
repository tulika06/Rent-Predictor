import bs4
from bs4 import BeautifulSoup
import requests
import io
with io.open("kol.csv",'w',encoding="utf-8") as f1:
    f1.write('Title,Price,Area,Status,Bathrooms' + '\n')
    f1.close()

url1 = "https://www.makaan.com/bangalore-residential-property/rent-property-in-bangalore-city"
page1 = requests.get(url1)
page1 = page1.text
data1 = bs4.BeautifulSoup(page1,'lxml')
read1 = data1.find('strong',{'class':'val-count'})
read1 = read1.getText()
read1 = read1.replace(',','')
count = int(read1)
read2 = data1.select('.cardholder')
loop_count = int(count/(len(read2)))
dd = 1

for i in range(loop_count):
    url = "https://www.makaan.com/bangalore-residential-property/rent-property-in-bangalore-city?page=" + str(dd)
    page = requests.get(url)
    page = page.text

    data = bs4.BeautifulSoup(page,'lxml')
    read = data.select('.cardholder')
    print("page no" + str(dd))
    for i in read:  
        title = i.find_all('div',{'class':'title-line'})
        if len(title)>0:
            title = title[0].getText()
        price = i.find_all('td',{'class':'price'})
        if len(price)>0:
            price = price[0].getText()
            price = price.replace(',','')
        area = i.find_all('td',{'class':'size'})
        if len(area)>0:
            area = area[0].getText()
            area = area.replace(',','')
        status = i.find_all('td',{'class':'val'})
        if len(status)>0:
            status = status[0].getText()
        bathrooms = i.find_all('li',{'title':'bathrooms'})
        if len(bathrooms)>0:
            bathrooms = bathrooms[0].getText()
        location = i.find_all('span',{'itemprop':'addressLocality'})
        if len(location)>0:
            location = location[0].getText()
        scrapped_data = str(title) + "," + str(location) + "," + str(price) + "," + str(area) + "," + str(status) + "," + str(bathrooms)
        with io.open('kol.csv','a',encoding="utf-8") as f2:
            f2.write(scrapped_data + "\n")
            f2.close()
    dd=dd+1