import os
from pathlib import Path

from src.classes.manga_class import Manga


class Book:
    """Instructions on type of book to build & chapters to download"""

    def __init__(self, manga: Manga, bookType: str):
        self.startDir = f'{Path.home()}/Downloads/Baka'
        self.manga = manga
        self.type = bookType

    start: int = None
    finish: int = None
    directory: str

    def create_dirs(self) -> None:
        manga = self.manga
        folderName = f'{manga.title}'

        if self.type == 'chapter':
            self.start = int(input(f'Which chapter of {manga.title} do you want to download?'))
            self.directory = f'{manga.title} Chapter {self.start}'
            os.makedirs(f'{self.startDir}/{folderName}', exist_ok=True)
            os.makedirs(f'{self.startDir}/{self.directory}', exist_ok=True)
            return

        elif self.type == 'collection':
            self.start = int(input('From which chapter of One Piece do you want to start? '))
            self.finish = int(input(' At which chapter do you want to end? '))
            self.directory = f'{manga.title} {self.start}-{self.finish}'
            os.makedirs(f'{self.startDir}/{folderName}', exist_ok=True)
            return
