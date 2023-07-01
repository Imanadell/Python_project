from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup

driver_path = r"D:\app\chromedriver\chromedriver.exe"
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://divar.ir/s/mashhad/car")

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(10)
soup = BeautifulSoup(driver.page_source, 'html.parser')
car_ads = soup.select('.kt-post-card')
ad_list = []

for ad in car_ads:
    ad_title = ad.select_one('.kt-post-card__title').text
    ad_operation = ad.select_one('.kt-post-card__description').text
    ad_location = ad.select_one('.kt-post-card__bottom').text
