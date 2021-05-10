from src.classes.manga_class import Manga


# One Piece
one_piece = Manga('One Piece')
one_piece.url = 'https://onepiece-manga-online.net/manga/one-piece-chapter-'
one_piece.div = 'div.relative > picture > img'
one_piece.url2 = 'https://online-one-piece.com/manga/one-piece-chapter-'
one_piece.div2 = 'div.relative > picture > img'

# Berserk
berserk = Manga('Berserk')
berserk.url = 'https://readberserk.com/chapter/berserk-chapter-'
berserk.div = 'div.img_container > img'
berserk.format = '0>3'

# Yakusoku no Neverland
yakusoku = Manga('Yakusoku No Neverland')
yakusoku.url = 'https://www12.promised-neverland.com/manga/the-promised-neverland-chapter-'
yakusoku.div= 'div > figure > img'

