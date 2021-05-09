import os
import shutil

import bs4
import requests
from requests import Response

from src.classes.book_class import Book


def download_chapter(book: Book, chapter: int = None) -> str:
    """Finds a manga chapter, loops through and downloads its images.
    Accepts an optional 'chapter' value for looping through chapters in collection mode."""

    location: str = f'{book.bookDir}/{chapter}' if chapter else f'{book.series}/{book.start}'
    chapter: int = chapter if chapter else book.start

    os.makedirs(location, exist_ok=True)

    res: Response = Response()

    try:
        res: Response = requests.get(f'{book.manga.url}{chapter}')
    except ConnectionError:
        print('It seems the info for that manga is outdated. Please open an issue')  # Todo: Link to github
        # TODO Cleanup Directories
        exit(0)
    res.raise_for_status()
    parser = bs4.BeautifulSoup(res.text, 'html.parser')
    imageArray: [str] = parser.select(book.manga.div)

    if len(imageArray) == 0:
        print(f"\tCouldn't find chapter {chapter}. Exiting...")
        exit(0)

    count: int = 0

    data = data_check(imageArray[0])

    if data:
        for _ in imageArray:
            url = imageArray[count].get('data-src')
            download_img(url, location)
            count += 1
    else:
        for _ in imageArray:
            url = imageArray[count].get('src')
            download_img(url, location)
            count += 1

    return prepare_cbz(book, location)


def prepare_cbz(book: Book, location: str) -> str:
    arch = shutil.make_archive(location, 'zip', location)  # Archive chapter folder
    cbzPath = book.chapDir if book.chapDir else location
    os.rename(arch, f'{cbzPath}.cbz')
    return cbzPath


def prepare_cbc(book: Book):
    arch = shutil.make_archive(book.bookDir, 'zip', book.bookDir)
    os.rename(arch, f'{book.bookDir}.cbc')


def data_check(img) -> bool:
    """Check to see if source is normal or data-type"""
    url = img.get('src')
    return True if 'data' in url else False


def download_img(url: str, location: str):
    print(f'\tDownloading {url}')
    res2 = requests.get(url)
    res2.raise_for_status()
    pic = open(os.path.join(location, os.path.basename(url)), 'wb')
    for i in res2.iter_content(100000):
        pic.write(i)
    pic.close()
