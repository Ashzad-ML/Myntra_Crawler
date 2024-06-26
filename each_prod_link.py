import time
import os
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



def each_link(url):
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get(url)
    time.sleep(3)
    filtered_links=[]
    elements = driver.find_elements(By.CSS_SELECTOR, 'a[href]')
    href_links = [element.get_attribute('href') for element in elements]
    filtered_links.extend([links for links in href_links if '/buy' in links])
    
    for link in filtered_links:
        print(link)
        
    driver.quit()
    return filtered_links

