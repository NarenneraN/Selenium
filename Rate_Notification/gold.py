from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
import pywhatkit

website = 'https://www.goodreturns.in/gold-rates/chennai.html'
path = 'E:\MY_WORKS\chromedriver'

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)

# Price Xpath - //div[@id="corePrice_feature_div"]/div/span/span
price_place = driver.find_element(by="xpath",value='//strong[@id="el"]')
price = str(price_place.text)
print(price)
price=price.replace(",", "")
price=price.replace("₹", "")
price=price.replace(" ", "")
print(price)
price=int(price)

msg="This is computer generated message ! Today's Gold Rate is ₹"+str(price)

print(msg)
driver.quit()
# Whatsapp

# input place -> //div[@data-testid="chat-list-search"]

# website1='https://web.whatsapp.com/'
# # options = Options()
# # options.headless = True
# # service = Service(executable_path=path)
# driver1 = webdriver.Chrome(service=service)
# driver1.get(website1)
# WebDriverWait(driver, 600).until(
#             EC.presence_of_element_located((By.XPATH, '//div[@data-testid="chat-list-search"]')))
# search_box = driver.find_element(by="xpath",value='//div[@data-testid="chat-list-search"]')
# search_box.innerHTML='Naren'
pywhatkit.sendwhatmsg("+919384933498",msg,20,00)