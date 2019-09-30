import os
import time
from selenium.webdriver.common.keys import Keys


def upload_images_to_makesense(args, driver):
    driver.get('http://localhost:3000')
    button = driver.find_element_by_xpath(
        "//div[@class='RightColumn']//div[@class='TextButton']")
    button.click()
    time.sleep(2)

    input_upload = driver.find_element_by_xpath(
        "//div[@class='ImagesDropZone']//div[@class='DropZone']//input")
    data_path = os.path.abspath(args.output_directory)
    filenames = []
    folders = os.listdir(data_path)
    folders = [folder for folder in folders if folder != ".gitkeep"]
    for folder in folders:
        if os.path.isdir(os.path.join(data_path, folder)):
            for filename in os.listdir(os.path.join(data_path, folder)):
                filename = os.path.join(data_path, folder, filename)
                filenames.append(filename)

    input_upload.send_keys('\n'.join(filenames))

    detection_button = driver.find_element_by_xpath(
        '//div[@class="DropZoneButtons"]//div[@class="TextButton"]')
    detection_button.click()

    plus_button = driver.find_element_by_xpath(
        '//div[@class="LeftContainer"]//div[@class="ImageButton"]')

    for _ in range(len(folders)):
        plus_button.click()

    input_texts = driver.find_elements_by_xpath(
        "//div[@class='InsertLabelNamesPopupContent']//div[@class='LabelEntry']//div[@class='TextInput']//input")
    for i, input_text in enumerate(input_texts):
        input_text.send_keys(folders[i])

    start_button = driver.find_element_by_xpath(
        "//div[@class='Footer']//div[@class='TextButton accept']")
    start_button.click()

    on_my_own_button = driver.find_element_by_xpath(
        "//div[@class='Footer']//div[@class='TextButton reject']")
    on_my_own_button.click()
