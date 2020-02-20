# Record Collection Application
# Tim Ahlqvist - 2020

import os

collections = []
releases = []
songNames = []
songLengthList = []

class CreateCollection():
    def __init__(self, name, description):
        self.name = name
        self.description = description

        collection = name, description
        collections.append(collection)

class CreateRelease():
    def __init__(self, artist, title, year, label, type, songNames, recordLength):
        self.artist = artist
        self.title = title
        self.year = year
        self.label = label
        self.type = type
        self.songNames = songNames
        self.recordLength = recordLength

        release = artist, title, year, label, type, songNames, songLengthList, recordLength
        releases.append(release)

def listCollections():
    os.system("CLS")
    print("Collections:")
    print(collections)
    os.system("PAUSE")
    start()

def listReleases():
    os.system("CLS")
    print("Releases:")
    print(releases)
    os.system("PAUSE")
    start()

def createCollection():
    os.system("CLS")
    print("Name your collection")
    collectionName = input(": ")
    print("Describe your collection")
    collectionDescription = input(": ")

    collection1 = CreateCollection(collectionName, collectionDescription)
    listCollections()

def createRelease():
    minutes = 0
    seconds = 0

    os.system("CLS")
    print("Artist:")
    artist = input(": ")
    print("Title:")
    title = input(": ")
    print("Year:")
    year = int(input(": "))
    print("Label (optional)")
    label = input(": ")
    print("Type, (CD, Vinyl, CD-Single, Vinyl-Single)")
    type = input(": ")
    print("How many songs is it on this release?")
    songsInput = int(input(": "))
    os.system("CLS")

    for i in range(songsInput):
        print("Name of song", i + 1, ": ")
        songName = input(": ")
        songNames.append(songName)

    os.system("CLS")
    x = 0
    for i in range(songsInput):
        print("(optional) Length of", songNames[x])
        print("Minutes: ")
        songMinutes = int(input(": "))
        print("Seconds: ")
        songSeconds = int(input(": "))

        songLength = songMinutes, ":", songSeconds
        songLengthList.append(songLength)

        minutes += songMinutes
        seconds += songSeconds

        x += 1

    recordLength = minutes, ":", seconds

    CreateRelease(artist, title, year, label, type, songNames, recordLength)
    listReleases()

def collection(choosenCollection):
    os.system("CLS")
    print("You are in", collections[choosenCollection])
    print("1) Back to start")
    collectionInput = int(input(": "))
    if collectionInput == 1:
        start()

def loadCollection():
    os.system("CLS")
    x = 0

    print("Choose which collection you want to edit")
    for i in collections:
        print(x + 1, collections[x])
        x += 1
    choosenCollection = int(input(": ")) - 1
    collection(choosenCollection)

def information():
    os.system("CLS")
    print("This is an application / a computer program were you can store your record collection. You can search for artists and records in your collection and look at the songlist, length of the record and more. This project is made in Python and I do this to practice Python.")
    os.system("PAUSE")
    start()

def start():
    os.system("CLS")
    print("Record Collection Application")
    print("Organize your record collection")
    print("1) Create new collection")
    print("2) Create new release")
    print("3) Load collection")
    print("4) Information")
    print("5) Quit application")
    startInput = int(input(": "))

    if startInput == 1:
        createCollection()
    elif startInput == 2:
        createRelease()
    elif startInput == 3:
        loadCollection()
    elif startInput == 4:
        information()
    elif startInput == 5:
        quit()

start()