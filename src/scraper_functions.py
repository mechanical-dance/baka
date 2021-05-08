import os
import shutil

import bs4
import requests
from requests import Response

from src.classes.book_class import Book


def download_chapter(book: Book, chapter: int = None):
    """Finds a manga chapter, loops through and downloads its images.
    Accepts an optional 'chapter' value for looping through chapters in collection mode."""

    chapter = chapter if chapter else book.start

    os.makedirs(f'{book.series}/{chapter}', exist_ok=True)

    res: Response = Response()

    try:
        res: Response = requests.get(f'{book.manga.url}{chapter}')
    except ConnectionError:
        print('It seems the info for that manga is outdated. Please open an issue')  # Todo: Link to github
        # TODO Cleanup Directories
        exit(0)
    res.raise_for_status()
    parser = bs4.BeautifulSoup(res.text, 'html.parser')
    imageArray: [str] = parser.select(book.manga.div_structure)

    if len(imageArray) == 0:
        print(f"Couldn't find chapter {chapter}. Exiting...")
        exit(0)

    count: int = 0

    data = data_check(imageArray[0])

    if data:
        for _ in imageArray:
            url = imageArray[count].get('data-src')
            download_img(book, chapter, url, count)
            count += 1
    else:
        for _ in imageArray:
            url = imageArray[count].get('src')
            download_img(book, chapter, url, count)
            count += 1

    prepare_cbz(book, chapter)


def prepare_cbz(book: Book, chapter: int) -> None:
    arch = shutil.make_archive(f'{book.series}/{chapter}', 'zip', f'{book.series}/{chapter}')  # Archive chapter folder
    cbz = f'{book.chapDir}.cbz' if book.chapDir else f'{book.series}/{chapter}.cbz'
    os.rename(arch, cbz)


def data_check(img) -> bool:
    """Check to see if source is normal or data-type"""
    url = img.get('src')
    return True if 'data' in url else False


def download_img(book: Book, chapter, url: str, count: int):
    print(f'Downloading {url}')
    res2 = requests.get(url)
    res2.raise_for_status()
    pic = open(os.path.join(f'{book.series}/{chapter}', os.path.basename(url)), 'wb')
    for i in res2.iter_content(100000):
        pic.write(i)
    pic.close()
    count += 1
