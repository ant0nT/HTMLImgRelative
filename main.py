import pathlib
import os
import sys
import requests
import validators
from urllib.request import pathname2url
from pprint import pprint
from bs4 import *

directory_path = ''


def download_image(i, src, rel_path):
    """
    Function downloads images and saves they in img/HTMLImgRelative + rel_path

    :param i: ordinal number for images
    :param src: images url
    :param rel_path: relative path from directory path to html file)
    :return: local path where image has been saved
    """
    # calculating directory path for downloading images
    img_dir_path = os.path.join(directory_path, 'img/HTMLImgRelative/', rel_path,)
    # creating directories if they don't exist
    os.makedirs(img_dir_path, exist_ok=True)
    file_extension = pathlib.Path(src).suffix
    # calculating file path. File name is ordinal number + file extension
    path = os.path.join(img_dir_path, str(i) + file_extension)
    img_data = requests.get(src).content
    with open(path, 'wb') as handler:
        handler.write(img_data)
    return path
    pass


def find_imgs(html):
    """
    Function finds images tags, call download function and replaces source paths to locals

    :param html: path to html file
    :return: None
    """
    try:
        soup = BeautifulSoup(open(html))
    except:
        print ('error file ' + str(html))
        return
    images = soup.findAll('img')
    rel_path = os.path.relpath(html, directory_path)
    print(html)
    for i, img in enumerate(images):
        if img.has_attr('src'):
            if validators.url(img['src']):
                print('src', img['src'])
                path_to_image = download_image(i, img['src'], rel_path)
                #print(path_to_image)
                img['src'] = pathname2url(os.path.relpath(path_to_image, os.path.dirname(html)))
        pass
    with open(html, "w", encoding='utf-8') as file:
        file.write(str(soup))
    pass


def find_htmls():
    """
    :return: list of paths contained "**/*.html"
    """
    file_dir = directory_path
    file_ext = '**/*.html'
    return list(pathlib.Path(file_dir).glob(file_ext))
    pass


def main():
    htmls_list = find_htmls()
    for html in htmls_list:
        # exclude not files and finder (macos) service files
        if os.path.isfile(html) and not os.path.basename(html).startswith('._'):
            find_imgs(html)
    pass


if __name__ == '__main__':
    # path to parent dir. Global var
    directory_path = sys.argv[1]
    main()
    pass
