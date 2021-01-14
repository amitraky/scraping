from selenium import webdriver
import bs4
import pandas as pd
driver = webdriver.Chrome("C:\chromium/chromedriver.exe")
from pathlib import Path
from urllib.request import urlretrieve as download

products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
driver.get("https://www.goole.com")

content = driver.page_source
soup = bs4.BeautifulSoup(content, 'html.parser')

a = soup.find('img',attrs={'id':'captcha'}).attrs['src']
img = 'https://www.goole.com'+a
print(img)

#df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings}) 
#df.to_csv('products.csv', index=False, encoding='utf-8')
id = 'tt5057054'
directory = "images"
Path(directory).mkdir(exist_ok=True)
download(img,'abc.png')
