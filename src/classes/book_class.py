import os
from pathlib import Path

from src.classes.manga_class import Manga


class Book:
    """Instructions on type of book to build & chapters to download"""

    def __init__(self, manga: Manga, bookType: str):
        self.manga = manga
        self.type = bookType

    start: int = None
    finish: int = None
    directory: str

    def create_dirs(self):
        manga = self.manga
        startDir = f'{Path.home()}/Downloads/Baka'
        folderName = f'{manga.title}'

        if self.type == 'chapter':
            self.start = int(input(f'Which chapter of {manga.title} do you want to download?'))
            self.directory = f'{manga.title} Chapter {self.start}'
            os.makedirs(f'{startDir}/{folderName}', exist_ok=True)
            os.makedirs(f'{startDir}/{self.directory}', exist_ok=True)
            return

        elif self.type == 'collection':
            self.start = int(input('From which chapter of One Piece do you want to start? '))
            self.finish = int(input(' At which chapter do you want to end? '))
            self.directory = f'{manga.title} {self.start}-{self.finish}'
            os.makedirs(f'{startDir}/{folderName}', exist_ok=True)
            return
