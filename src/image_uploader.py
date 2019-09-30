import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('../driver/chromedriver')
driver.get('http://localhost:3000')
button = driver.find_element_by_xpath("//div[@class='RightColumn']//div[@class='TextButton']")
button.click()

time.sleep(2)

input_upload = driver.find_element_by_xpath("//div[@class='ImagesDropZone']//div[@class='DropZone']//input")


data_path = '/Users/ahmedbesbes/Documents/perso/dataset_builder/data/'
filenames = []
folders = os.listdir(data_path)
for folder in folders:
    for filename in os.listdir(os.path.join(data_path, folder)):
        filename = os.path.join(data_path, folder, filename)
        filenames.append(filename)

input_upload.send_keys('\n'.join(filenames))


