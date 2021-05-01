from src.manga.manga_class import Manga


# One Piece
one_piece = Manga('One Piece')
one_piece.url = 'https://online-one-piece.com/manga/one-piece-chapter-'
one_piece.div_structure = 'div.relative > picture > img'

# Berserk
berserk = Manga('Berserk')
berserk.url = 'https://readberserk.com/chapter/berserk-chapter-'
berserk.div_structure = 'div.img_container > img'
berserk.format = '0>3'

# Yakusoku no Neverland
yakusoku = Manga('Yakusoku No Neverland')
yakusoku.url = 'https://www12.promised-neverland.com/manga/the-promised-neverland-chapter-'
yakusoku.div_structure = 'div > figure > img'

