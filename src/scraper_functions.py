import asyncio
import os
import shutil

import aiohttp
import bs4
from aiohttp import ClientSession

from src.classes.book_class import Book


async def download_chapter(book: Book, chapter: int = None, retry: bool = False) -> str:
    """Finds a manga chapter, loops through and downloads its images.
    Accepts an optional 'chapter' value for looping through chapters in collection mode
    and 'retry' boolean for checking backup sites."""

    location: str = f'{book.bookDir}/{chapter}' if chapter else f'{book.series}/{book.start}'
    chapter: int = chapter if chapter else book.start
    # If attempt is a retry, use backup variables
    url, div = (book.manga.url, book.manga.div) if not retry else (book.manga.url2, book.manga.div2)

    os.makedirs(location, exist_ok=True)

    asyncSession: ClientSession = aiohttp.ClientSession()

    try:
        res = await asyncSession.get(f'{url}{chapter}')
    except ConnectionError:
        print('It seems the info for that manga is outdated. Please open an issue')  # Todo: Link to github
        abort_cleanup(book)
        exit(0)
    res.raise_for_status()
    parser = bs4.BeautifulSoup(await res.text(), 'html.parser')
    imageArray = parser.select(div)

    if len(imageArray) == 0:
        if retry:
            print(f"\tCouldn't find chapter {chapter}. Exiting...")
            exit(0)
        else:
            return await download_chapter(book, chapter, retry=True)

    data = data_check(imageArray[0])
    urlArray: [str] = []

    if data:
        for _ in imageArray:
            url = _.get('data-src')
            if "google" in url:
                continue
            urlArray.append(url)
    else:
        for _ in imageArray:
            url = _.get('src')
            if "google" in url:
                continue
            urlArray.append(url)

    await asyncio.gather(*[download_img(url, location, asyncSession) for url in urlArray])

    await asyncSession.close()
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
    """Check to see if source is a data object or a string"""
    url = img.get('src')
    return True if 'data' in url else False


async def download_img(url: str, location: str, session: ClientSession):
    print(f'\tDownloading {url}')
    res = await session.get(url)
    res.raise_for_status()
    pic = open(os.path.join(location, os.path.basename(url)), 'wb')
    async for i in res.content.iter_chunked(100000):
        pic.write(i)
    pic.close()


def abort_cleanup(book: Book):
    """If download is aborted, remove dirs"""
    os.rmdir(f'{book.bookDir}') if book.type == 'book' else os.rmdir(f'{book.series}/{book.start}')
