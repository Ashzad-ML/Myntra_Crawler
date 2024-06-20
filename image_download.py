# vim test.py
import time
import requests
import os
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import urllib.parse



# def image_downlaod(url):
#     options = Options()
#     #options.add_argument('--headless')
#     options.add_argument('--no-sandbox')
#     options.add_argument('--disable-dev-shm-usage')
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#     current_directory = os.getcwd()
#     # Create a directory to save images in the current working directory
#     images_directory = os.path.join(current_directory, 'downloaded_images')
#     os.makedirs(images_directory, exist_ok=True)


#     driver.get(url)
#     #print(driver.title)
#     time.sleep(5)





#     image_elements = driver.find_elements(By.CLASS_NAME, "image-grid-image")
#     for index, image in enumerate(image_elements):
#         style_attribute = image.get_attribute('style')
#         if 'background-image' in style_attribute:
#             url_start = style_attribute.find('url("') + len('url("')
#             url_end = style_attribute.find('")', url_start)
#             image_url = style_attribute[url_start:url_end]
                
#             # Download the image
#             response = requests.get(image_url)
#             if response.status_code == 200:
#                 # Save the image in the 'downloaded_images' folder
#                 with open(f'downloaded_images/image_{index + 1}.jpeg', 'wb') as file:
#                     file.write(response.content)
#                 print(f"Image {index + 1} downloaded: {image_url}")
#             else:
#                 print(f"Failed to download image {index + 1}: {image_url}")

#     time.sleep(10)
#     driver.close()

def men_image_download(url):
    options = Options()
    # options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    current_directory = os.getcwd()
    parent_directory = os.path.join(current_directory, 'Men-Categories')
    os.makedirs(parent_directory, exist_ok=True)
    
    # Parse the URL to get the path
    parsed_url = urllib.parse.urlparse(url)
    # Extract the directory name from the URL path
    path_parts = parsed_url.path.split('/')
    # dir_name = '-'.join(path_parts[2:-1])  # Join the relevant parts of the path
    product_name = path_parts[-3]
    # Create the full path for the new directory
    # images_directory = os.path.join(parent_directory, product_name)
    # os.makedirs(images_directory, exist_ok=True)

    driver.get(url)
    time.sleep(3)

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
    # time.sleep(10)
    driver.close()
    
    
def women_image_download(url):
    options = Options()
    # options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    current_directory = os.getcwd()
    parent_directory = os.path.join(current_directory, 'Women-Categories')
    os.makedirs(parent_directory, exist_ok=True)
    
    # Parse the URL to get the path
    parsed_url = urllib.parse.urlparse(url)
    # Extract the directory name from the URL path
    path_parts = parsed_url.path.split('/')
    dir_name = '-'.join(path_parts[2:-1])  # Join the relevant parts of the path
    product_name=path_parts[-3]
    # Create the full path for the new directory
    images_directory = os.path.join(parent_directory, product_name)
    os.makedirs(images_directory, exist_ok=True)

    driver.get(url)
    time.sleep(3)

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
                with open(os.path.join(images_directory, filename), 'wb') as file:
                    file.write(response.content)
                print(f"Image {index + 1} downloaded: {image_url}")
            else:
                print(f"Failed to download image {index + 1}: {image_url}")
    # time.sleep(10)
    driver.close()
    
    
# url="https://www.myntra.com/tshirts/blackberrys/blackberrys-printed-polo-collar-t-shirt/24334936/buy"
# men_image_download(url)