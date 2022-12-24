# File to create the Base Url
# https://www.adidas.ca/en/gazelle-shoes/BB5478.html?forceSelSize=BB5478_530 Size=4
# What sizes are currently available
# Add to Cart Button
# Checkout Pop up
# Checkout complete
# Payment complete


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from config import keys


def UrlGenwithSize(size,model,name):
     # Size for the shoe
     base=530 # for a shoe of size 4
     mySize=(size-4)*20 # the increment value to 530
     finalSize=base+mySize
     Url="https://www.adidas.ca/en/"+name+"/"+model+".html?forceSelSize="+model+"_"+str(finalSize)
     print(Url)
     return Url

def UrlGenProduct(name,model):
     url="https://www.adidas.ca/en/"+name+"/"+model+".html"
     return url

def CheckStock(myUrl,model):
    try:
        driver.get(myUrl)
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "add_to_bag_form___227O2")))
        username = driver.find_element_by_class_name('gl-dropdown__select-element')
        options = username.find_elements_by_tag_name("option")  # get all the options into a list
        optionsList = []
        for option in options:
            optionsList.append(option.get_attribute('innerHTML'))
        for sizes in optionsList:
            if sizes.isdigit():
                print("Size "+sizes+" for "+model+" is available ")
    finally:
        driver.quit()

def addToCart(myUrl):
          province_init={"AB":"//li[contains(@class,'selectoption selected')]", "ON":"//div[contains(@class,'rbk-delivery-wrapper')]//li[10]", "BC":"//div[contains(@class,'ffSelectWrapper active')]//li[contains(@class,'selectoption on')]", "MB":"//div[contains(@class,'rbk-delivery-wrapper')]//li[4]","NB":"//div[contains(@class,'rbk-delivery-wrapper')]//li[5]","NL":"//div[contains(@class,'rbk-delivery-wrapper')]//li[6]","NT":"//div[contains(@class,'rbk-delivery-wrapper')]//li[7]","NS":"//div[contains(@class,'rbk-delivery-wrapper')]//li[8]","NU":"//div[contains(@class,'rbk-delivery-wrapper')]//li[9]","PE":"//div[contains(@class,'rbk-delivery-wrapper')]//li[11]","QC":"//div[contains(@class,'rbk-delivery-wrapper')]//li[12]","SK":"//div[contains(@class,'rbk-delivery-wrapper')]//li[13]","YT":"//div[contains(@class,'rbk-delivery-wrapper')]//li[14]"}
          province=str(province_init[str(keys['province_code'])])
          driver = webdriver.Chrome()
          driver.get(myUrl)
          driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "btn-bag", " " ))]').click()
          element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "gl-modal__main-content")))
          driver.find_element_by_xpath("//span[contains(text(),'Checkout')]").click()
          dropdown = driver.find_element_by_class_name("ffSelectButton")
          dropdown.click()
          element = WebDriverWait(driver, 20).until(
              EC.element_to_be_clickable((By.XPATH, province)))
          driver.execute_script("arguments[0].click();", element)
          driver.find_element_by_xpath("//input[@id='dwfrm_delivery_singleshipping_shippingAddress_addressFields_firstName']").send_keys(keys['first_name'])
          driver.find_element_by_xpath("//input[@id='dwfrm_delivery_singleshipping_shippingAddress_addressFields_lastName']").send_keys(keys['last_name'])
          driver.find_element_by_xpath("//input[@id='dwfrm_delivery_singleshipping_shippingAddress_addressFields_address1']").send_keys(keys['street_address'])
          driver.find_element_by_xpath("//input[@id='dwfrm_delivery_singleshipping_shippingAddress_addressFields_city']").send_keys(keys['city'])
          driver.find_element_by_xpath("//input[@id='dwfrm_delivery_singleshipping_shippingAddress_addressFields_zip']").send_keys(keys['zip_code'])
          driver.find_element_by_xpath("//input[@id='dwfrm_delivery_singleshipping_shippingAddress_addressFields_phone']").send_keys(keys['phone_number'])
          driver.find_element_by_xpath("//input[@id='dwfrm_delivery_singleshipping_shippingAddress_email_emailAddress']").send_keys(keys['email'])
          el = WebDriverWait(driver, 60).until(EC.element_to_be_clickable(
              (By.XPATH, '//*[@id="dwfrm_delivery"]/div[2]/div[2]/div[2]/div[2]/div[1]/div/div/span')))
          driver.execute_script("arguments[0].click();", el)
          myel=WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="dwfrm_delivery"]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div/div/div')))
          driver.execute_script("arguments[0].click();", myel)
          if keys['shipping'].lower()=="express":
            myel1=WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="shippingoptions"]/div/ul/li[2]/label/div[2]/span[1]')))
            driver.execute_script("arguments[0].click();", myel1)
          driver.find_element_by_xpath('//*[@id="dwfrm_delivery_savedelivery"]').click()

          WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='dwfrm_adyenencrypted_number']"))).send_keys(keys['card_number'])
          full_name=keys["first_name"]+" "+keys["last_name"]
          driver.find_element_by_xpath("//input[@id='dwfrm_adyenencrypted_holderName']").send_keys(full_name)
          driver.find_element_by_xpath("//input[@id='dwfrm_adyenencrypted_cvc']").send_keys(keys['card_cvv'])
          month=keys['expiry'].split('/')[0]
          year=keys['expiry'].split('/')[1]

          months={"01":"//div[contains(@class,'formfield month')]//li[2]","02":"//div[contains(@class,'formfield month')]//li[3]","03":"//div[contains(@class,'formfield month')]//li[4]","04":"//div[contains(@class,'formfield month')]//li[5]","05":"//div[contains(@class,'formfield month')]//li[6]","06":"//div[contains(@class,'formfield month')]//li[7]","07":"//div[contains(@class,'formfield month')]//li[8]","08":"//div[contains(@class,'formfield month')]//li[9]","09":"//div[contains(@class,'ffSelectWrapper active')]//li[contains(@class,'selectoption on')]","10":"//div[contains(@class,'formfield month')]//li[11]","11":"//div[contains(@class,'formfield month')]//li[12]","12":"//div[contains(@class,'formfield month')]//li[13]"}
          m = str(months[str(month)])
          dropdown = driver.find_element_by_class_name("ffSelectButton")
          dropdown.click()
          element = WebDriverWait(driver, 20).until(
              EC.element_to_be_clickable((By.XPATH, m)))
          driver.execute_script("arguments[0].click();", element)

          years={"2019":"//div[contains(@class,'formfield year nobr')]//li[2]","2020":"//div[contains(@class,'formfield year nobr')]//li[3]","2021":"//div[contains(@class,'formfield year nobr')]//li[4]","2022":"//div[contains(@class,'formfield year nobr')]//li[5]","2023":"//div[contains(@class,'formfield year nobr')]//li[6]","2024":"//div[contains(@class,'formfield year nobr')]//li[7]","2025":"//div[contains(@class,'formfield year nobr')]//li[8]","2026":"//div[contains(@class,'formfield year nobr')]//li[9]","2027":"//div[contains(@class,'formfield year nobr')]//li[10]","2028":"//div[contains(@class,'formfield year nobr')]//li[11]","2029":"//div[contains(@class,'formfield year nobr')]//li[12]","2030":"//div[contains(@class,'formfield year nobr')]//li[13]","2031":"//div[contains(@class,'formfield year nobr')]//li[14]","2032":"//div[contains(@class,'formfield year nobr')]//li[15]","2033":"//div[contains(@class,'formfield year nobr')]//li[16]","2034":"//div[contains(@class,'formfield year nobr')]//li[17]","2035":"//div[contains(@class,'formfield year nobr')]//li[18]","2036":"//div[contains(@class,'formfield year nobr')]//li[19]","2037":"//div[contains(@class,'formfield year nobr')]//li[20]","2038":"//div[contains(@class,'formfield year nobr')]//li[21]","2039":"//div[contains(@class,'formfield year nobr')]//li[22]"}
          dropdown = driver.find_element_by_xpath("//div[contains(@class,'formfield year nobr')]//a[contains(@class,'ffSelectButton')]")
          dropdown.click()
          y = str(years[str(year)])
          element = WebDriverWait(driver, 20).until(
              EC.element_to_be_clickable((By.XPATH, y)))
          driver.execute_script("arguments[0].click();", element)
          driver.find_element_by_xpath("//div[@class='outer-payment-submit stylerefresh']//button[@class='co-btn_primary btn_showcart button-full-width button-ctn button-brd adi-gradient-blue button-forward']").click()

if __name__ == '__main__':
     # load chrome
     driver = webdriver.Chrome()
     productUrl=UrlGenProduct(keys['product_name'],keys['product_model'])
     CheckStock(productUrl,keys['product_model'])
     size=int(input("From the size available list select size:"))
     myUrl=str(UrlGenwithSize(size,keys['product_model'],keys['product_name']))
     addToCart(myUrl)




