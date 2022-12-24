from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def UrlGenwithSize(size,model,name):
     # Size for the shoe
     base=530 # for a shoe of size 4
     mySize=(size-4)*20 # the value to increment 4.5 -4 =0.5 * 20=10;
     finalSize=base+mySize
     Url="https://www.adidas.ca/en/"+name+"/"+model+".html?forceSelSize="+model+"_"+str(finalSize)
     return Url

def UrlGenProduct(name,model):
     url="https://www.adidas.ca/en/"+name+"/"+model+".html"
     return url

def CheckStock(myUrl,model):
     try:
          driver = webdriver.Chrome()#initialising the chrome driver
          driver.get(myUrl)# specific url opens in chrome
          WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "add_to_bag_form___227O2")))#sets a time max of 10 secs and waits for the emlement identified to load
          username = driver.find_element_by_class_name('gl-dropdown__select-element')
          options = username.find_elements_by_tag_name("option")  # get all the options into a list
          optionsList = []
          for option in options:
               optionsList.append(option.get_attribute('innerHTML'))# a list with sizes
          for sizes in optionsList:
               if sizes.isdigit():# printing only if size in the list is a digit
                    print("Size " + sizes + " for " + model + " is available ")
     finally:
          driver.quit()

def addToCart(myUrl):
     driver = webdriver.Chrome()#initialising the chrome driver
     driver.get(myUrl) # specific url opens in chrome
     driver.find_element_by_xpath("(//SPAN[@class='gl-cta__text'][text()='Add To Bag'][text()='Add To Bag'])[1]").click() #find element
     element = WebDriverWait(driver, 10).until(
          EC.presence_of_element_located((By.CLASS_NAME, "gl-modal__main-content"))) #need to wait for pop to load
     driver.find_element_by_xpath("//SPAN[@class='gl-cta__text'][text()='Go to checkout']").click() #once pop up is up click button

url=UrlGenProduct("ultraboost-19-shoes","EF1345")
CheckStock(url,"EF1345")
size=int(input("Please enter size "))
myURL=UrlGenwithSize(size,"EF1345","ultraboost-19-shoes")
addToCart(myURL)













