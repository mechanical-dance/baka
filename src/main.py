from src.conversion_functions import convert_cbc, convert_cbz
from src.selections import mangaSelection, bookType
from src.scraper_functions import *


def main():
    print('Welcome to B.A.K.A, the Booking and Kindling Archiver!')
    print('This application allows you to download manga and convert it into a kindle formatted ebook.\n')

    # Choose manga
    manga = mangaSelection()
    # Choose chapter or collection
    book = bookType(manga)
    # Create get chapter info and create series dir
    book.chapter_info()

    if book.type == 'chapter':

        # Download image files and prepare cbz
        cbz = download_chapter(book)
        # Convert to ebook
        convert_cbz(cbz)
        # Clean up
        book.cleanup()

    elif book.type == 'collection':

        cFile = open(f'{book.bookDir}/comics.txt', 'a')  # Index for book conversion
        count = book.start

        # Download chapter by chapter
        for _ in range(book.range):
            print('Downloading Chapter', count)

            cFile.write(f'{count}.cbz: Chapter {count} \n')  # Add chapter to index
            download_chapter(book, count)  # Download image files and prepare cbz
            book.cleanup(count)  # Clean up chapter files
            count += 1

        cFile.close()
        prepare_cbc(book)
        convert_cbc(book.bookDir)
        book.cleanup(book=True)
    exit(0)

    # Thanks!


if __name__ == "__main__":
    main()
