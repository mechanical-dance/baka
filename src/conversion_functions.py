import subprocess

from src.globals import CALIBRE_LOCATION


def convert_cbz(cbzPath: str):
    subprocess.run([CALIBRE_LOCATION, f'{cbzPath}.cbz', f'{cbzPath}.azw3', '--landscape'])


def convert_cbc(cbcPath: str):
    subprocess.run([CALIBRE_LOCATION, f'{cbcPath}.cbc', f'{cbcPath}.azw3',
                    '--landscape', '--dont-add-comic-pages-to-toc'])


def main():
    convert_cbc('/Users/jenghis/Downloads/Baka/Berserk/Berserk 3-6')


if __name__ == '__main__':
    main()
