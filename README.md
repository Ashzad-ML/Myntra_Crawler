# Myntra Crawler
The Myntra Product Image Crawler is a specialized tool designed to extract product images from various categories of men's and women's fashion on the Myntra platform. This innovative crawler is developed with the purpose of gathering diverse and extensive collections of fashion products to be used in training and developing an image classifier. By systematically capturing images from a wide array of clothing, footwear, and accessories categories, the Myntra Product Image Crawler aims to create a rich and comprehensive dataset that can facilitate the development of advanced image classification models.

With a focus on extracting high-quality product images, the crawler navigates through Myntra's extensive range of men's and women's fashion categories, including but not limited to apparel, footwear, and accessories. The collected images will serve as valuable resources for training machine learning models aimed at classifying and categorizing fashion products with high accuracy and precision. This initiative not only showcases the potential of leveraging web crawling techniques for data acquisition but also highlights the significance of utilizing real-world product images to enhance the performance of image recognition and classification algorithms.

The Myntra Product Image Crawler endeavors to contribute to the advancement of image recognition technology within the realm of fashion and e-commerce, ultimately fostering the development of more efficient and intuitive product recommendation systems, trend analysis tools, and personalized shopping experiences. Through its meticulous extraction and compilation of product images, the crawler lays the foundation for empowering future machine learning endeavors in the domain of fashion and e-commerce, setting the stage for groundbreaking advancements in image-based product classification and analysis.

### File Structure
Myntra_Crawler/
  │
  ├── Image_Download.py
  ├── Each_Product_Link.py
  ├── Category.py
  ├── Cloth_Categorizer.py
  ├── pycacle file
  └── requirements.txt

## **Image_Download.py**<br>
For the project my first Approach was that I should be able to download the product images using the link and also I should be able to store them in my local system. So for achieving this I created a python script.

Importing all the necessary python modules
```
import time
import requests
import os
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import urllib.parse
```
Setting up the server
```
options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    current_directory = os.getcwd()
    parent_directory = os.path.join(current_directory, 'Men-Categories')
    os.makedirs(parent_directory, exist_ok=True)
```
```
current_directory = os.getcwd()
    parent_directory = os.path.join(current_directory, 'Men-Categories')
    os.makedirs(parent_directory, exist_ok=True)
    
    parsed_url = urllib.parse.urlparse(url)
    path_parts = parsed_url.path.split('/')
    product_name = path_parts[-3]
```
Creating the directories for Men and Women Categories
```
current_directory = os.getcwd()
    parent_directory = os.path.join(current_directory, 'Women-Categories')
    os.makedirs(parent_directory, exist_ok=True)
    
    parsed_url = urllib.parse.urlparse(url)
    path_parts = parsed_url.path.split('/')
    product_name = path_parts[-3]
```
**current_directory :** It will store the current directory.<br>
**parent_directory :** Creating a directory for both men and women categories<br>
**pare_url :** Parsing the the url for extracting the product name and saving it in product_name<br>

Extracting and downloading images from the urls
```
image_elements = driver.find_elements(By.CLASS_NAME, "image-grid-image")
    for index, image in enumerate(image_elements):
        style_attribute = image.get_attribute('style')
        if 'background-image' in style_attribute:
            url_start = style_attribute.find('url("') + len('url("')
            url_end = style_attribute.find('")', url_start)
            image_url = style_attribute[url_start:url_end]
                
            # Download the image
            response = requests.get(image_url)
            if response.status_code == 200:
                # Format the filename with product name and index
                filename = f"{product_name}_{index + 1}.jpeg"
                # Save the image in the new directory
                with open(os.path.join(parent_directory, filename), 'wb') as file:
                    file.write(response.content)
                print(f"Image {index + 1} downloaded: {image_url}")
            else:
                print(f"Failed to download image {index + 1}: {image_url}")
    driver.close()
```
**image_elements :** Getting the elements present in div class with name "image-grid-image".<br>
**url_start ,url_end:** Custom Splitting and extracting the urls in image_url from the style attribute present in the div<br>
**response :** Requesting to get access to the image urls<br>
**filename :** setting the name of the image downlaod file <br>

## **Each_Product_Link.py**<br>
After successfully creating the downloading images script next I planned to build a script which wil;l extract all the product links of a given category.

Extracting and downloading images from the urls
```
filtered_links=[]
    elements = driver.find_elements(By.CSS_SELECTOR, 'a[href]')
    href_links = [element.get_attribute('href') for element in elements]
    filtered_links.extend([links for links in href_links if '/buy' in links])
    driver.close()
```
**elements :** Getting the elements present in CSS section having an "a" or "href" tag .<br>
**href_links :** Getting all the urls present in href and storing them.<br>
**filtered_links :** Filtering the links which has "/buy"  in it as it redirects to the products pages.<br>



## **Category.py**<br>
Creating the main function and the pipeline for running all the codes from main.<br>

Extracting and downloading images from the urls
```
filtered_links=[]
    href_store= []
    catergory_links=driver.find_elements(By.CLASS_NAME, 'desktop-categoryLink')
    for link in catergory_links:
        href=link.get_attribute('href')
        href_store.append(href)

    driver.quit()
    return href_store
```
**href_store :** Creating a list to store the links .<br>
**catergory_links :** Extracting the urls using the div class with name ""desktop-categoryLink  <br>

## **Cloth_Categorizer.py**<br>
A fucntion to categorize the products as T-Shirt,Shirt etc etc for bth men and women.<br>

## **requirements.txt**<br>
This file conatins all the modules that are need:

run the Syntax : **pip install -r requirements.txt** in Command Prompt



