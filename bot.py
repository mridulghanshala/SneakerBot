from selenium import webdriver
from bs4 import BeautifulSoup  
browser = webdriver.Chrome()

def getSizes(name, model):
    browser.get("https://www.adidas.com/us/"+name+"/"+model+".html")
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    x=soup.find_all("button", class_="gl-label size___2lbev")
    for a in x:
        print(str(a).split('<span>')[1].split('</span')[0])

getSizes('samba-og-shoes','HP7901')

