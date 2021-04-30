import requests, os, bs4, shutil, subprocess

def berserk_tome():
    
    # Command line instructions 
    print('This is the tome generator for Berserk')
    print('Chapters within a given range will be downloaded and converted into a single ebook, '
          'with a table of contents that links to each chapter \n')

    start = int(input('From which chapter of Berserk do you want to start? '))
    finish = int(input(' At which chapter do you want to end? '))

    # File system setup
    folderName = 'Berserk Tome'
    bookName = f'Berserk {start}-{finish}'
    os.makedirs(folderName, exist_ok= True)
    c_file = open(f'{folderName}/comics.txt', 'a')
    startDir = '/Users/jenghis/OneDrive/Code/Scraper/tests/'

    for chapter in range(start, finish + 1):

        # Search site for selected chapter, if found parse chapter for frames
        url = f'https://readberserk.com/chapter/berserk-chapter-{chapter:0>3}/'
        res = requests.get(url)
        res.raise_for_status()
        oneSoup = bs4.BeautifulSoup(res.text, 'html.parser')
        picDiv = oneSoup.select('div.img_container > img')

        # If chapter isn't found, exit
        if len(picDiv) == 0:
            print("Sorry, couldn't find that chapter.")
            exit(0)

        # Make folders to store files and convert to cbz
        chapterName = f'{folderName}/Berserk Chapter {chapter}'
        os.makedirs(chapterName, exist_ok= True)


        # Counter to iterate list of tags
        count = 0

        for i in picDiv:
            pic_url = picDiv[count].get('src')
           
            # Circumvent automation detectors
            if "google" in pic_url:
                continue
            
            print(f'Downloading {pic_url}')
            res2 = requests.get(pic_url)
            res2.raise_for_status()
            pic = open(os.path.join(chapterName, f'{count:0>2}.png'), 'wb')
            for j in res2.iter_content(100000):
                pic.write(j)
            pic.close()
            count += 1

        # Make a zip of the directory holding the pictures, then rename it to cbz file
        zippy = shutil.make_archive(chapterName, 'zip', f'{startDir}/{chapterName}')
        cbz = f'{chapterName}.cbz'
        os.rename(zippy, cbz)
        c_file.write(f'Berserk Chapter {chapter}.cbz:Berserk Chapter {chapter} \n')

        # Delete picture folders
        for file in os.listdir(chapterName):
            os.remove(f'{startDir}{chapterName}/{file}')
        os.rmdir(f'{startDir}{chapterName}')

    c_file.close()
    zippy_t = shutil.make_archive(folderName, 'zip', f'{startDir}/{folderName}')
    cbc = f'Berserk {start}-{finish}.cbc'
    os.rename(zippy_t, cbc)

    # Run calibre e-book converter as subprocess on cbz file
    # Subprocess will depend on location of command tools for calibre
    subprocess.run(['/Applications/calibre.app/Contents/MacOS/ebook-convert',
                    f'{startDir}{bookName}.cbc', f'{bookName}.azw3', '--landscape', '--dont-add-comic-pages-to-toc'])


    # Delete unneeded pics, folder, and cbz
    os.remove(f'{startDir}{bookName}.cbc')
    for file in os.listdir(folderName):
        os.remove(f'{startDir}{folderName}/{file}')
    os.rmdir(f'{startDir}{folderName}')
    
    print('Conversion complete, enjoy your book!')

if __name__ == "__main__":
    berserk_tome()
