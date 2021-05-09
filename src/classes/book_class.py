import os
from pathlib import Path

from src.classes.manga_class import Manga


class Book:
    """Instructions on type of book to build & chapters to download"""

    def __init__(self, manga: Manga, bookType: str):
        self.startDir = f'{Path.home()}/Downloads/Baka'
        self.manga = manga
        self.type = bookType
        self.series = f'{self.startDir}/{manga.title}'

    start: int = None
    finish: int = None
    range: int = None
    series: str
    chapDir: str = None
    bookDir: str = None

    def chapter_info(self) -> None:
        manga = self.manga

        if self.type == 'chapter':
            self.start = int(input(f'Which chapter of {manga.title} do you want to download?'))
            self.chapDir = f'{self.series}/{manga.title} Chapter {self.start}'
            os.makedirs(f'{self.series}', exist_ok=True)  # Series folder
            return

        elif self.type == 'collection':
            self.start = int(input(f'From which chapter of {manga.title} do you want to start? '))
            self.finish = int(input(' At which chapter do you want to end? '))
            self.range = self.finish - (self.start - 1)
            self.bookDir = f'{self.series}/{manga.title} {self.start}-{self.finish}'
            os.makedirs(f'{self.series}', exist_ok=True)  # Series folder
            os.makedirs(f'{self.bookDir}', exist_ok=True)  # Book Folder
            return

    def cleanup(self, count: int = None, book=False) -> None:
        """Cleans up files and folders upon success or failure.
            Accepts a collection boolean to know what files to remove"""
        if not count:
            if book:
                os.remove(f'{self.bookDir}.cbc')
                for file in os.listdir(f'{self.bookDir}'):
                    os.remove(f'{self.bookDir}/{file}')
                os.rmdir(f'{self.bookDir}')
            else:
                os.remove(f'{self.chapDir}.cbz')
                for file in os.listdir(f'{self.series}/{self.start}'):
                    os.remove(f'{self.series}/{self.start}/{file}')
                os.rmdir(f'{self.series}/{self.start}')

        else:
            for file in os.listdir(f'{self.bookDir}/{count}'):
                os.remove(f'{self.bookDir}/{count}/{file}')
            os.rmdir(f'{self.bookDir}/{count}')
