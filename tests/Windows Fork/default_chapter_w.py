import requests, os, bs4, shutil, subprocess
from pathlib import Path


def manga_chapter(name, in_url, zeros, filepath):

    # zeros should look something like 0>{zeros}
    num = int(input(f'Which chapter of {name} do you want to download? '))
    chapterName = f'{name} Chapter {num}'
    folderName = f'{name}'
    # Will be replaced later with filepath
    startDir = Path('C:/Users/xjeng/OneDrive/Code/Scraper/tests/Windows Fork/')

    # Search site for selected chapter, if found parse chapter for frames
    url = f'{in_url}{num:{zeros}}/'
    res = requests.get(url)
    res.raise_for_status()
    oneSoup = bs4.BeautifulSoup(res.text, 'html.parser')
    picDiv = oneSoup.select('div.img_container > img')

    # If chapter isn't found, exit
    if len(picDiv) == 0:
        print("Sorry, couldn't find that chapter.")
        exit(0)

    # Make folders to store files and convert to cbz
    os.makedirs(folderName, exist_ok=True)
    os.makedirs(chapterName, exist_ok=True)

    # Counter to iterate list of tags
    count = 0
    for i in picDiv:
        pic_url = picDiv[count].get('src')
        print(f'Downloading {pic_url}')
        res2 = requests.get(pic_url)
        res2.raise_for_status()
        pic = open(os.path.join(chapterName, f'{count:0>2}.png'), 'wb')
        for j in res2.iter_content(100000):
            pic.write(j)
        pic.close()
        count += 1

    # Make a zip of the directory holding the pictures, then rename it to cbz file
    zippy = shutil.make_archive(chapterName, 'zip', Path(f'{startDir}/{chapterName}'))
    cbz = f'{chapterName}.cbz'
    os.rename(zippy, cbz)

    # Run calibre e-book converter as subprocess on cbz file
    # Subprocess will depending on location of your command tools for calibre
    subprocess.run([Path("C:/Program Files (x86)/calibre/ebook-convert"),
                    Path(f'{startDir}/{chapterName}.cbz'), f'{chapterName}.azw3', '--landscape'])

    shutil.move(f'{chapterName}.azw3', Path(f'{startDir}/{folderName}/{chapterName}.azw3'))

    # Delete the unneeded pics, folder, and cbz
    os.remove(Path(f'{startDir}/{chapterName}.cbz'))
    for file in os.listdir(chapterName):
        os.remove(Path(f'{startDir}/{chapterName}/{file}'))
    os.rmdir(Path(f'{startDir}/{chapterName}'))
