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
    # Download image files and prepare cbz
    download_chapter(book)
    # Clean up chapter files
    book.cleanup()

    # Convert to ebook
    exit(0)
    # convert()
    # Clean up

    # Thanks!


if __name__ == "__main__":
    main()
