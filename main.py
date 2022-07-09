import pathlib
import os
import sys
import requests
import validators
from pprint import pprint
from bs4 import *

directory_path = ''


def download_image(i, src, rel_path):
    #result = ''
    img_dir_path = os.path.join(directory_path, 'img/HTMLImgRelative/', rel_path,)
    os.makedirs(img_dir_path, exist_ok=True)
    file_extension = pathlib.Path(src).suffix
    path = os.path.join(img_dir_path, str(i) + file_extension)
    img_data = requests.get(src).content
    with open(path, 'wb') as handler:
        handler.write(img_data)
    return path
    pass


def find_imgs(html):
    if os.path.basename(html).startswith('._'):
        return
    try:
        soup = BeautifulSoup(open(html))
    except:
        print ('error file ' + str(html))
    images = soup.findAll('img')
    rel_path = os.path.relpath(html, directory_path)
    print(html)
    for i, img in enumerate(images):
        if img.has_attr('src'):
            if validators.url(img['src']):
                print('src', img['src'])
                path_to_image = download_image(i, img['src'], rel_path)
                print(path_to_image)
                #new_relative = os.path.relpath(path_to_image, )
                img['src'] = str(os.path.relpath(path_to_image, os.path.dirname(html)))
        pass
    with open(html, "w", encoding='utf-8') as file:
        file.write(str(soup))
    #return images
    pass


def find_htmls():
    file_dir = directory_path
    file_ext = '**/*.html'
    return list(pathlib.Path(file_dir).glob(file_ext))
    pass


def main():
    htmls_list = find_htmls()
    for html in htmls_list:
        if os.path.isfile(html):
            find_imgs(html)
    pass


if __name__ == '__main__':
    directory_path = sys.argv[1]
    main()
    pass
