from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--headless')
options.add_argument('--disable-dev-shm-usage')

options.add_argument("start-maximized"); 
options.add_argument("disable-infobars"); 
options.add_argument("--disable-extensions"); 
options.add_argument("--disable-gpu"); 
options.add_argument("--disable-dev-shm-usage"); 

driver = webdriver.Chrome(options=options)


# driver = webdriver.Edge()
url = "https://www.lazada.com.my/tag/socking/?spm=a2o4k.homepage.search.d_go&q=socking&catalog_redirect_tag=true"
driver.get(url)

WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#root")))
time.sleep(2)

soup = BeautifulSoup(driver.page_source, 'html.parser')
product = []
for item in soup.findAll('div', class_="Bm3ON", limit=10):
  product_name = item.find('div', class_="RfADt").text
  product_price = item.find('span', class_="ooOxS").text
  product_url = item.find('div', class_="RfADt").find('a', href=True)
  product_link = product_url['href']
  if product_link.startswith("//"):
      modified_product_link = "https:" + product_link
  product_info = {
      'product_name': product_name,
      'product_price': product_price,
      'product_link': modified_product_link
  }
  product.append(product_info)

num_flag = 1
for a in product:
  print(f"{num_flag}. {a['product_name']} - {a['product_price']} - {a['product_link']}")
  num_flag+=1

driver.close()


