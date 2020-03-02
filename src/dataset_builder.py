import shutil
import os
import time
import argparse
from image_uploader import upload_images_to_makesense
from selenium import webdriver
from flickr_scraper.flickr_scraper import get_urls


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--output-directory', type=str, default='../data/')
    parser.add_argument('--limit', type=int, default=5)
    parser.add_argument('--delete-history', action='store_true')
    parser.add_argument(
        '--task', type=str, choices=['classification', 'detection', 'segmentation'], default='detection')
    parser.add_argument('--driver', type=str, default='../driver/chromedriver')
    args = parser.parse_args()

    print('Hello there. Want to build you custom computer vision dataset? Let\'s go !')

    keywords = []
    i = 1
    while True:
        print(f'Define class {i} [Type q to quit] :')
        keyword = input()
        if keyword == 'q':
            if i == 1:
                print('You have to define at least one class')
            else:
                break
        else:
            i += 1
            keywords.append(keyword)

    if args.delete_history:
        print('removing downloads history ...')
        for folder in os.listdir(args.output_directory):
            if os.path.isdir(os.path.join(args.output_directory, folder)):
                shutil.rmtree(os.path.join(args.output_directory, folder))

    for keyword in keywords:
        get_urls(search=keyword,
                 n=args.limit,
                 output_directory=args.output_directory,
                 download=True)

    if args.task in ['detection', 'segmentation']:
        driver = webdriver.Chrome(args.driver)
        driver.maximize_window()
        upload_images_to_makesense(args, driver)
