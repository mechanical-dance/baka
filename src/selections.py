from src.manga.berserk.Berserk_Chapter import berserk_chapter
from src.manga.one_piece.OnePiece_Chapter import op_chapter
from src.manga.berserk.Tome_Raider_Berserk import berserk_tome
from src.manga.one_piece.Tome_Raider_OnePiece import onepiece_tome
from src.manga.yakusoku_no_neverland.Yakusoku_Chapter import ynn_chapter


def mangaSelection():
    manga = input('What manga are you looking to download today?'
                  '\n\t a. One Piece'
                  '\n\t b. Berserk'
                  '\n\t c. Yakusoku No Neverland \n')

    if manga == 'a':
        title = 'One Piece'
    elif manga == 'b':
        title = 'Berserk'
    elif manga == 'c':
        title = 'Yakusoku No Neverland'
    else:
        print("Please type a, b, or c")
        return mangaSelection()
    return bookType(manga, title)


def bookType(manga, title):
    print(f'{title}, a solid choice.')
    sel = input('Are you looking to download a single chapter (a) or make a collection (b)? \n\t')
    if sel == 'a':
        if title == 'One Piece':
            return op_chapter()
        elif title == 'Berserk':
            return berserk_chapter()
        elif title == 'Yakusoku No Neverland':
            return ynn_chapter()
    elif sel == 'b':
        if manga == 'a':
            return onepiece_tome()
        elif manga == 'b':
            return berserk_tome()
        else:
            res = input('Only One Piece and Berserk are available as collections at the moment. Start Over?\n\t')
            return mangaSelection() if res == 'y' else quit(0)
    else:
        print('Please enter "a" for a chapter or "b" for a collection\n')
        return bookType(manga, title)
