# BAKA
### booking and kindle archiver

BAKA is a simple command line tool that allows users to download manga from the internet and
converts the downloaded images into azw3 formatted ebooks for use with kindle devices. It uses
BeautifulSoup 4 to parse the web for images, and the ebook converter included in Calibre by Kovid Goyal
for formatting. 
In chapter mode, the images are compiled and converted into a single ebook, but more powerful functionality is
found in Tome mode. Tome, meaning a large or heavy book or collection of works, collects the previously converted chapters
into a single file, and separates the individual chapters in a table of contents. In both modes, BAKA cleans up after itself, removing
the individual pictures as well as the chapters used in Tome mode, leaving behind only a single, instantly accesible ebook.
 
Developing Baka is my first utilitarian passion project, so I plan to update it as I grow as a software developer. Eventually I want to replace the Calibre ebook converter with my own code. Other potential upgrades include:
 - a larger manga library
 - concurrent file/chapter downloading
 - a TKinter based GUI
 - a user mode where users can locate good manga sources and save their own profiles for manga not initially built in
