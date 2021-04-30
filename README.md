# BAKA
### booking and kindle archiver

#### ❗ This repo is currently being refactored to have a file structure that makes sense. As proud as I was to have something that I worked a few months ago, it's pretty painful to look at now. Check out the branches to see the latest progress and feel free to fork/contribute site recipes to the manga_list.py file


BAKA is a simple command line tool that allows users to download manga from the internet and
converts the downloaded images into azw3 formatted ebooks for use with kindle devices. It uses
BeautifulSoup 4 to parse the sites for images, and the ebook converter included in Calibre by Kovid Goyal
for formatting. 
In chapter mode, the images are compiled and converted into a single ebook, but more powerful functionality is
found in Tome (collection) mode. Tome, meaning a large or heavy book or collection of works, collects multiple chapters
into a single file and separates the individual chapters with a table of contents. In both modes, BAKA cleans up after itself, removing
the individual pictures as well as the chapters used in Tome mode, leaving behind only a single, instantly accesible ebook.
 
Baka is my first software passion project, so I plan to update it as I grow as a developer. Eventually I want to replace the Calibre ebook converter with my own code. Other potential upgrades include:
 - a larger manga library
 - concurrent file/chapter downloading
 - a TKinter based GUI
 - a user mode where users can locate good manga sources and save their own profiles for manga not initially built in
