import weakref


class Manga:
    """Manga to be downloaded w/ it's attributes"""
    mangaCount = 1
    mangaList = []

    def __init__(self, title: str):
        self.title = title
        self.code = Manga.mangaCount
        self.__class__.mangaList.append(weakref.proxy(self))
        Manga.mangaCount += 1

    url: str
    div_structure: str
    url2: str = None
    div_structure2: str = None
    format: str = '0'

    def get_url(self, chapter: int) -> str:
        return f'{self.url}{chapter:{self.format}}'
