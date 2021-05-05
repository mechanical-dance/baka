from src.selections import mangaSelection, bookType
from src.scraper_functions import *


def main():
    print('Welcome to B.A.K.A, the Booking and Kindling Archiver!')
    print('This application allows you to download manga and convert it into a kindle formatted ebook.\n')

    # Choose manga
    manga = mangaSelection()
    # Choose chapter or collection
    book = bookType(manga)
    # Create dirs for storage
    book.create_dirs()
    # Download image files
    download_chapter(book)
    exit(0)
    # Convert to ebook
    # convert()
    # Clean up

    #Thanks!


if __name__ == "__main__":
    main()
