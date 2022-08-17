from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
import pywhatkit

website = 'https://www.amazon.in/boAt-Bluetooth-Resistance-Playtime-Multi-Compatibility/dp/B09TDK97JM/ref=sr_1_3?crid=1561ZEEGQLK1W&keywords=boat%2Bspeaker%2B350&qid=1660633322&sprefix=%2Caps%2C327&sr=8-3&th=1'
path = 'E:\MY_WORKS\chromedriver'

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)

# Price Xpath - //div[@id="corePrice_feature_div"]/div/span/span
price_place = driver.find_element(by="xpath",value='//div[@id="corePrice_feature_div"]/div/span/span/span/span/..')
price = str(price_place.text)
price=price.replace(",", "")
print(price)
price=int(price)
print(price)
max_price=1399
msg='This is computer generated message ! '
if price <max_price-300:
    msg+="Price has been drastically reduced ! Grab it"
elif price<max_price-200:
    msg+="Look out sson it's a good offer"
elif price<max_price-1:
    msg+="Some discount has been on the product ! Go and check out"
elif price>max_price:
    msg+="OMG! Price has increased... Please leave out the idea of buying it today"
else:
    msg+="No discounts as of today's search ! SADDDDD"
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
pywhatkit.sendwhatmsg("+919384933498",msg,16,27)