from manga.manga_list import *
from src.classes.book_class import Book


def mangaSelection() -> Manga:
    print('What manga are you looking to download today?')
    for i in Manga.mangaList:
        print(f'\t{i.code}. {i.title}')
    sel = int(input())
    for x in Manga.mangaList:
        if x.code == sel:
            manga = x
            return manga
    print("Please select an available manga by number")
    return mangaSelection()


def bookType(manga: Manga) -> Book:
    print(f'{manga.title}, a solid choice.')
    sel = input('Are you looking to download a single chapter (a) or make a collection (b)? \n\t')
    if sel == 'a':
        return Book(manga, 'chapter')
    elif sel == 'b':
        if manga != yakusoku:
            return Book(manga, 'collection')
        else:
            res = input('Only One Piece and Berserk are available as collections at the moment. Start Over?\n\t')
            return mangaSelection() if res == 'y' else quit(0)
    else:
        print('Please enter "a" for a chapter or "b" for a collection\n')
        return bookType(manga)
