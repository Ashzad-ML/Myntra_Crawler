# vim test.py
import image_download as download_each_image
import each_prod_link as product_links
import cloth_catgorizer as categorizer
import time
import os
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def category_link(url):
    options = Options()
    #options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # url="https://www.myntra.com/"
    driver.get(url)
    time.sleep(3)
    href_store= []
    catergory_links=driver.find_elements(By.CLASS_NAME, 'desktop-categoryLink')
    for link in catergory_links:
        href=link.get_attribute('href')
        # print(href)
        href_store.append(href)

    # print(href_store)

    driver.quit()
    return href_store


if __name__ == "__main__":
    
    url="https://www.myntra.com/"
    links = category_link(url)
    # print(links)
    # links.index("https://www.myntra.com/women-accessories")
    # links.index("https://www.myntra.com/women-watches")

    # print (links[0])
    # idw.image_downlaod(links[0])
    # prod_link=ipl.each_link(links[0])
    # for i in range (4):
    #     idw.image_downl0oad(prod_link[i])
    
    # for i in range(18):
    #     eachlink=[]
    #     eachlink = product_links.each_link(links[i])
    #     for j in range(10):
    #         download_each_image.men_image_download(eachlink[j])
    
    # categorizer.men_categorize_images()

    for i in range(76,77):
        eachlink=[]
        eachlink = product_links.each_link(links[i])
        for j in range(10):
            download_each_image.women_image_download(eachlink[j])        
    
    categorizer.women_categorize_images()