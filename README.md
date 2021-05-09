# BAKA
### booking and kindle archiver

BAKA is a simple command line tool that allows users to download manga from the internet and
converts it into azw3 formatted ebooks for use with kindle devices. It uses
BeautifulSoup 4 to parse hosting sites for images, and currently relies on the ebook converter included in [Calibre](https://github.com/kovidgoyal/calibre) by [Kovid Goyal](https://kovidgoyal.net) for the conversion. 

In chapter mode images are compiled and converted into a single ebook, but more powerful functionality is
found in collection mode. This mode collects multiple chapters into a single file and separates the individual chapters with a table of contents. 
In both modes, BAKA cleans up after itself, leaving behind only a ready to read ebook.
 
Baka is my first personal project, so I plan to update it as I grow as a developer. As of now, it's usable if you know how to run python scripts but eventually there will just be a binary.

## Usage:
To use BAKA just clone this repo, navigate to the baka folder, use pip to install the requirements.txt file, and in the src folder run main.py 

❗Note that at the moment, BAKA relies on Calibre being installed in its default location and works on Mac OSX
<hr>

### Dev roadmap:
  - faster parsing
  - larger library with backup sources
  - concurrent file/chapter downloading
  - book batch mode (download several collections of a certain size)
  - make it pretty with blessing
  - write independent conversion tool in either go or rust

##### Wishful thinking:
  - a user mode where users can locate good manga sources and save their own profiles for manga not built in
