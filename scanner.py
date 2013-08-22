import fnmatch
import os
import shutil
import sys
import transmissionrpc
import ConfigParser

from TextMessage import SendText
from pyColor import color

configPath = '/home/pi/Media-Scanner/scanner.cfg'
config = ConfigParser.RawConfigParser()
config.read(configPath)

# Define the server which the torrent is stored on
trpcUser = config.get('user-info', 'trpcUser')
trpcPassword = config.get('user-info', 'trpcPassword')

# Define the text message variables
textSender = config.get('extras', 'textSender')
textPassword = config.get('extras', 'textPassword')
textNumber = config.get('extras', 'textNumber')
textMessage = 'Torrents finished and scanned!'

# Get the path options
dlPath = config.get('path', 'dlPath')
moviePath = config.get('path', 'moviePath')
musicPath = config.get('path', 'musicPath')
tvShowPath = config.get('path', 'tvShowPath')

# Get the tv shows from config file
titles = config.get('tv-shows', 'allShows').split(',')
tvshows = {
    
}

for title in titles:
    tvshows[title[:3].lower()+'*'] = tvShowPath + title + '/'
    tvshows[title[:3].upper()+'*'] = tvShowPath + title + '/'

# Create list of extenstions
movtypes = ["*.mp4", "*.avi", "*.mkv"]
mustypes = ["*.mp3"]

# Empty list for the matches to get copied too
matches = []

def MovieScan():
    """ Scan and mvoe movie files """
    for root, dirnames, filenames in os.walk(dlPath):
        for extend in movtypes:
            for filename in fnmatch.filter(filenames, extend):
                matches.append(os.path.join(root, filename))
                print(os.path.join(root, filename))
                shutil.move(os.path.join(root, filename), os.path.join(moviePath, filename))
                print color.GREEN + 'File succesfully moved!' + color.ENDC
    print "Finished Scanning For Movies"

def TvScan():
    """ Scan and move Tv Shows """
    for root, dirnames, filenames in os.walk(dlPath):
        for key, location in tvshows.iteritems():
            for filename in fnmatch.filter(filenames, key):
                matches.append(os.path.join(root, filename))
                print(os.path.join(root, filename))
                shutil.move(os.path.join(root, filename), os.path.join(location, filename))
                print color.GREEN + 'File succesfully moved!' + color.ENDC
    print "Finished Scanning For TV Shows"

def MusicScan():
    """ Scan and move music """
    for root, dirnames, filenames in os.walk(dlPath):
        for extend in mustypes:
            for filename in fnmatch.filter(filenames, extend):
                matches.append(os.path.join(root, filename))
                print(os.path.join(root, filename))
                shutil.move(os.path.join(root, filename), os.path.join(musicPath, filename))
                print color.GREEN + 'File succesfully moved!' + color.ENDC
    print "Finished Scanning For Music"

def ScanAll():
    MusicScan()
    TvScan()
    MovieScan()
    SendText(textSender, textPassword, textNumber, textMessage)
    print "Scan complete. Exiting.."

def TorrentHandle():
    """ 
    Get the current torrents and cycle through to check all are finished. If all torrents 
    are finished downloading, continue on to scanning and moving the files 
    """
    tc = transmissionrpc.Client('localhost', port=9091, user=trpcUser, password=trpcPassword)
    currentTorrents = tc.get_torrents()
    for torrent in currentTorrents:
        if not torrent.status == 'downloading':
            tc.remove_torrent(torrent.hashString)
            print "Torrent removed"
        else:
            print color.RED + "Error: " + torrent.status + color.ENDC
            sys.exit(0)

if __name__ == "__main__":
    TorrentHandle()
    ScanAll()
