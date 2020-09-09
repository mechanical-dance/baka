import requests, os, bs4, shutil, subprocess
from pathlib import Path


def onepiece_tome():
    print('This is the tome generator for One Piece')
    print('Chapters within a given range will be downloaded and converted into a single ebook, '
          'with a table of contents that links to each chapter')
    print()

    start = int(input('From which chapter of One Piece do you want to start? '))
    finish = int(input(' At which chapter do you want to end? '))

    folderName = 'One Piece Tome'
    bookName = f'One Piece {start}-{finish}'
    os.makedirs(folderName, exist_ok=True)
    c_file = open(Path(f'{folderName}/comics.txt'), 'a')
    startDir = Path('C:/Users/xjeng/OneDrive/Code/Scraper/tests/Windows Fork/')

    for chapter in range(start, finish + 1):

        # Search two sites for selected chapter, if found parse chapter for frames
        url = f'https://w5.onepiece-manga-read.com/manga/one-piece-chapter-{chapter}/'
        res = requests.get(url)
        res.raise_for_status()
        oneSoup = bs4.BeautifulSoup(res.text, 'html.parser')
        picDiv = oneSoup.select('div.separator > a > img')
        if len(picDiv) == 0:
            url = f'https://w16.read-onepiece.com/manga/one-piece-chapter-{chapter}/'
            res = requests.get(url)
            res.raise_for_status()
            oneSoup = bs4.BeautifulSoup(res.text, 'html.parser')
            picDiv = oneSoup.select('div.separator > a > img')

        # If chapter isn't found, exit
        if len(picDiv) == 0:
            print(f"Missing Chapter {chapter}. Aborting.")
            exit(0)

        # Make folders to store files and convert to cbz
        chapterName = f'{folderName}/One Piece Chapter {chapter}'
        os.makedirs(chapterName, exist_ok=True)

        # Counter to iterate list of tags
        count = 0

        for i in picDiv:
            pic_url = picDiv[count].get('src')
            print(f'Downloading {pic_url}')
            res2 = requests.get(pic_url)
            res2.raise_for_status()
            pic = open(os.path.join(chapterName, os.path.basename(pic_url)), 'wb')
            for j in res2.iter_content(100000):
                pic.write(j)
            pic.close()
            count += 1

        # Make a zip of the directory holding the pictures, then rename it to cbz file
        zippy = shutil.make_archive(chapterName, 'zip', Path(f'{startDir}/{chapterName}'))
        cbz = f'{chapterName}.cbz'
        os.rename(zippy, cbz)
        c_file.write(f'One Piece Chapter {chapter}.cbz:One Piece Chapter {chapter} \n')

        # Delete picture folders
        for file in os.listdir(chapterName):
            os.remove(Path(f'{startDir}/{chapterName}/{file}'))
        os.rmdir(Path(f'{startDir}/{chapterName}'))

    c_file.close()
    zippy_t = shutil.make_archive(folderName, 'zip', Path(f'{startDir}/{folderName}'))
    cbc = f'One Piece {start}-{finish}.cbc'
    os.rename(zippy_t, cbc)

    # Run calibre e-book converter as subprocess on cbz file
    # Subprocess will depending on location of your command tools for calibre
    subprocess.run([Path("C:/Program Files (x86)/calibre/ebook-convert"),
                    Path(f'{startDir}/{bookName}.cbc'), f'{bookName}.azw3', '--landscape', '--dont-add-comic-pages-to-toc'])

    shutil.move(f'{bookName}.azw3', Path(f'{startDir}/One Piece/{bookName}.azw3'))

    # Delete the unneeded pics, folder, and cbz
    os.remove(Path(f'{startDir}/{bookName}.cbc'))
    for file in os.listdir(folderName):
        os.remove(Path(f'{startDir}/{folderName}/{file}'))
    os.rmdir(Path(f'{startDir}/{folderName}'))


if __name__ == '__main__':
    onepiece_tome()
