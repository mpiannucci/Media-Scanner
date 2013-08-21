import fnmatch
import os
import shutil
import sys
import transmissionrpc
import ConfigParser
from TextMessage import SendText

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

# Define where you want to look for files
dlPath = '/media/MattsMedia/Downloads/'
moviePath = '/media/MattsMedia/Media/Movies/'
musicPath = '/media/MattsMedia/Media/Music/'

# Set the file destinations
famguyPath = '/media/MattsMedia/Media/TV Shows/Family Guy/'
personPath = '/media/MattsMedia/Media/TV Shows/Person of Interest/'
psychPath = '/media/MattsMedia/Media/TV Shows/Psych/'
entouragePath = '/media/MattsMedia/Media/TV Shows/Entourage/'
bbPath = '/media/MattsMedia/Media/TV Shows/Breaking Bad/'
suitsPath = '/media/MattsMedia/Media/TV Shows/Suits/'
modfamPath = '/media/MattsMedia/Media/TV Shows/Modern Family/'
wdPath = '/media/MattsMedia/Media/TV Shows/The Walking Dead/'
himymPath = '/media/MattsMedia/Media/TV Shows/How I Met Your Mother/'
burnPath = '/media/MattsMedia/Media/TV Shows/Burn Notice/'
gamePath = '/media/MattsMedia/Media/TV Shows/Game of Thrones/'
arrestPath = '/media/MattsMedia/Media/TV Shows/Arrested Development/'
gracePath = '/media/MattsMedia/Media/TV Shows/Graceland/'
fbashPath = '/media/MattsMedia/Media/TV Shows/Franklin and Bash/'

# Create list of extenstions
movtypes = ["*.mp4", "*.avi", "*.mkv"]
mustypes = ["*.mp3"]

# Create the tv show dictionary
tvshows = {
    "fam*" : famguyPath,
    "Fam*" : famguyPath,
    "Person*" : personPath,
    "person*" : personPath,
    "psych*" : psychPath,
    "Psych*" : psychPath,
    "ent*" : entouragePath,
    "Ent*" : entouragePath,
    "break*" : bbPath,
    "Break*" : bbPath,
    "suit*" : suitsPath,
    "Suit*" : suitsPath,
    "modern*" : modfamPath,
    "Modern*" : modfamPath,
    "walk*" : wdPath,
    "Walk*" : wdPath,
    "how*" : himymPath,
    "How*" : himymPath,
    "burn*" : burnPath,
    "Burn*" : burnPath,
    "game*" : gamePath,
    "Game*" : gamePath,
    "arrest*" : arrestPath,
    "Arrest*" : arrestPath,
    "grace*" : gracePath,
    "Grace*" : gracePath,
    "franklin*" : fbashPath,
    "Franklin*" : fbashPath
}

# Empty list for the matches to get copied too
matches = []

# Make some cute command line colors
class bcolor:
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    
    def disable(self):
        self.BLUE = ''
        self.GREEN = ''
        self.RED = ''
        self.ENDC = ''

"""
Iterate through possible file types to find potential movie files
"""
def MovieScan():
    for root, dirnames, filenames in os.walk(dlPath):
        for extend in movtypes:
            for filename in fnmatch.filter(filenames, extend):
                matches.append(os.path.join(root, filename))
                print(os.path.join(root, filename))
                shutil.move(os.path.join(root, filename), os.path.join(moviePath, filename))
                print bcolor.GREEN + 'File succesfully moved!' + bcolor.ENDC
    print "Finished Scanning For Movies"

"""
Iterate through the TV show dictionary to mvoe tv show episodes into respective folders
"""
def TvScan():
    for root, dirnames, filenames in os.walk(dlPath):
        for key, location in tvshows.iteritems():
            for filename in fnmatch.filter(filenames, key):
                matches.append(os.path.join(root, filename))
                print(os.path.join(root, filename))
                shutil.move(os.path.join(root, filename), os.path.join(location, filename))
                print bcolor.GREEN + 'File succesfully moved!' + bcolor.ENDC
    print "Finished Scanning For TV Shows"

def MusicScan():
    for root, dirnames, filenames in os.walk(dlPath):
        for extend in mustypes:
            for filename in fnmatch.filter(filenames, extend):
                matches.append(os.path.join(root, filename))
                print(os.path.join(root, filename))
                shutil.move(os.path.join(root, filename), os.path.join(musicPath, filename))
                print bcolor.GREEN + 'File succesfully moved!' + bcolor.ENDC
    print "Finished Scanning For Music"

"""
Smart Scan scans tv shows then movies to weed out tv shows from movie searches in one step
"""
def ScanAll():
    MusicScan()
    TvScan()
    MovieScan()
    SendText(textSender, textPassword, textNumber, textMessage)
    print "SmartScan complete. Exiting.."

""" Get the current torrents and cycle through to check all are finished. If all torrents 
    are finished downloading, continue on to scanning and moving the files 
"""
def TorrentHandle():
    tc = transmissionrpc.Client('localhost', port=9091, user=trpcUser, password=trpcPassword)
    currentTorrents = tc.get_torrents()
    for torrent in currentTorrents:
        if not torrent.status == 'downloading':
            tc.remove_torrent(torrent.hashString)
            print "Torrent removed"
        else:
            print bcolor.RED + "Error: " + torrent.status + bcolor.ENDC
            SendText(textSender, textPassword, textNumber, torrent.status)
            pickle.dump( torrent.status, open( "tor.p", "wb" ) )
            sys.exit(0)

if __name__ == "__main__":
    TorrentHandle()
    ScanAll()
