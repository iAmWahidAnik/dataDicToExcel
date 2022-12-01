from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://chaldal.com/meat-new")

totalProduct = 9
titleList = []
priceList = []
qList = []

for i in range(3, totalProduct+1):
    title = driver.find_element(by=By.XPATH, value='//*[@id="page"]/div/div[6]/section/div/div/div/div/section/div[2]/div/div['+str(i)+']/div/div/div[2]')
    quantity = driver.find_element(by=By.XPATH, value='//*[@id="page"]/div/div[6]/section/div/div/div/div/section/div[2]/div/div['+str(i)+']/div/div/div[3]')
    price = driver.find_element(by=By.XPATH, value='//*[@id="page"]/div/div[6]/section/div/div/div/div/section/div[2]/div/div['+str(i)+']/div/div/div[4]/div[1]/span[2]')

    titleList.append(title.text,)
    qList.append(quantity.text,)
    priceList.append(price.text,)

# print(titleList)

data = {'productName': titleList,
        'Quantity': qList,
        'Price': priceList,
        }


df = pd.DataFrame(data)

df.to_excel(r'G:\EuropeanITSoulution\Class 15\dataDicToExcel\scrapeData.xlsx', index=False)

driver.quit() 
