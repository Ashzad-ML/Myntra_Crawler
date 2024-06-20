import time
import os
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



def each_link(url):
    options = Options()
    #options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # url="https://www.myntra.com/men-tshirts"
    # Automating the urls filter
    # parts = url.split('/')
    # a=parts[3]
    # partss = a.split('-')
    # tshirts = partss[1]
    # parts[-1] = parts[-1].replace(parts[3], tshirts)
    # new_url = '/'.join(parts)
    driver.get(url)
    time.sleep(3)
    # href_elements = driver.find_elements(By.XPATH,'//a[@href]')
    filtered_links=[]
    elements = driver.find_elements(By.CSS_SELECTOR, 'a[href]')
    href_links = [element.get_attribute('href') for element in elements]
    filtered_links.extend([links for links in href_links if '/buy' in links])
    # urls = [element.get_attribute('href') for element in elements]
    # urls = [element.get_attribute('href') for element in elements if new_url in element.get_attribute('href')]

    # Print the stored href links
    for link in filtered_links:
        print(link)
        
    # print(len(urls))
    # Close the browser
    driver.quit()
    return filtered_links

