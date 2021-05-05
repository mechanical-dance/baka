import os
from time import sleep

import bs4
import requests

from src.classes.book_class import Book


def download_chapter(book: Book):
    try:
        res = requests.get(f'{book.manga.url}{book.start}')
    except ConnectionError:
        print('It seems the info for that manga is outdated. Please open an issue')  # Todo: Link to github
        # Todo Cleanup Directories
        exit(0)
    res.raise_for_status()
    parser = bs4.BeautifulSoup(res.text, 'html.parser')
    imageArray: [str] = parser.select(book.manga.div_structure)

    if len(imageArray) == 0:
        print(f"Couldn't find chapter {book.start}. Exiting...")
        exit(0)

    count: int = 0

    for image in imageArray:
        url = imageArray[count].get('src')
        # Check to see if the source is normal or 'data-source' type
        if 'data' in url:
            # Nested/ broken loop so that source type only needs to be checked once
            for dataImage in imageArray:
                url = imageArray[count].get('data-src')
                download_img(book, url, count)
            break
        download_img(book, url, count)


def download_img(book: Book, url: str, count: int):
    print(f'Downloading {url}')
    res2 = requests.get(url)
    res2.raise_for_status()
    pic = open(os.path.join(f'{book.startDir}/{book.directory}', os.path.basename(url)), 'wb')
    for i in res2.iter_content(100000):
        pic.write(i)
    pic.close()
    count += 1
