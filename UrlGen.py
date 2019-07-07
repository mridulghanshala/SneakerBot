# File to create the Base Url
# https://www.adidas.ca/en/gazelle-shoes/BB5478.html?forceSelSize=BB5478_530 Size=4
# What sizes are currently available

from time import sleep
import requests
import bs4
import random
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait

def UrlGen(name,model,size):
     # Size for the shoe
     base=530
     mySize=(size-4)*20
     finalSize=base+mySize
     Url="https://www.adidas.ca/en/"+name+"/"+model+".html?forceSelSize="+model+"_"+str(finalSize)
     print(Url)
     return Url

def CheckStock(myUrl,model):
     driver = webdriver.Chrome()
     driver.get(myUrl)
     element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "add_to_bag_form___227O2")))
     username = driver.find_element_by_class_name('gl-dropdown__select-element')
     options = username.find_elements_by_tag_name("option")  # get all the options into a list
     optionsList = []

     for option in options:
          if option!="":
               optionsList.append(option.get_attribute('innerHTML'))
     for sizes in optionsList:
          print("Size "+sizes+" for "+model+" is available ")


name=input("Name:")
model=input("Model:")
size=(int(input("Size:")))
url=UrlGen(name,model,size)
CheckStock(url,model)


