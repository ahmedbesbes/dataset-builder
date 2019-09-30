import shutil
import os
import argparse
from google_images_download import google_images_download
from image_uploader import upload_images_to_makesense


def download(keywords, args):
    if args.delete_history == 'yes':
        folders = os.listdir(args.output_directory)
        for folder in folders:
            if os.path.isdir(os.path.join(args.output_directory, folder)):
                shutil.rmtree(os.path.join(args.output_directory, folder))

    print(f'download {args.limit} images realed to the query {keywords}')
    response = google_images_download.googleimagesdownload()
    arguments = {
        "keywords": keywords,
        "limit": args.limit,
        "print_urls": True,
        "output_directory": args.output_directory
    }
    paths = response.download(arguments)
    return paths


def process_downloads(args):
    class_folders = os.listdir(args.output_directory)
    for class_folder in class_folders:
        if os.path.isdir(os.path.join(args.output_directory, class_folder)):
            filenames = os.listdir(os.path.join(
                args.output_directory, class_folder))
            for i, filename in enumerate(filenames):
                extension = filename.split('.')[-1]
                old_path = os.path.join(
                    args.output_directory, class_folder, filename)
                new_path = os.path.join(
                    args.output_directory, class_folder, f'{class_folder}_{i+1}.{extension}')
                os.rename(old_path, new_path)

    if args.task in ['detection', 'segmentation']:
        upload_images_to_makesense(args)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--output_directory', type=str, default='../data/')
    parser.add_argument('--limit', type=int, default=20)
    parser.add_argument('--delete_history', type=str,
                        default=0, choices=['yes', 'no'])
    parser.add_argument(
        '--task', type=str, choices=['classification', 'detection', 'segmentation'])
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

    keywords = ','.join(keywords)
    _ = download(keywords, args)
    process_downloads(args)
