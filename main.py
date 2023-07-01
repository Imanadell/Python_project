from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup

driver_path = r"D:\app\chromedriver\chromedriver.exe"
service = Service(executable_path=driver_path)