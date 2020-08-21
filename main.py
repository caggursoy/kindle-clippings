# import extract-kindle-clippings
import sys
import os
import re
import hashlib
from dateutil.parser import parse
import os
from datetime import datetime, timedelta, timezone
import getpass
import sys

# define main
def main():
    # initialize folders and stuff
    kindlePath = '/Volumes/Kindle/'
    documentsPath = kindlePath + 'documents/'
    clipPath = documentsPath + 'My Clippings.txt'
    outPath = os.getcwd() + '/outputs/'
    # use ekc with the folders defined
    sys.argv = [kindlePath, outPath]
    # subprocess.call('./extract-kindle-clippings.py', shell=True)
    os.system('python3 extract-kindle-clippings.py'+ ' '+ kindlePath +' '+ outPath)

# run main
if __name__ == '__main__':
    print('Running main...')
    main()
