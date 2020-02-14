# Record Collection Application
# Tim Ahlqvist - 2020

import os

collections = []
releases = []

class CreateCollection():
    def __init__(self, name, description):
        self.name = name
        self.description = description

        collection = name, description
        collections.append(collection)

class CreateRelease():
    def __init__(self, artist, title, year, label, type):
        self.artist = artist
        self.title = title
        self.year = year
        self.label = label
        self.type = type

        release = artist, title, year, label, type
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
    kent = CreateRelease("kent", "kent", 1995, "RCA, BMG", "CD")
    maggio = CreateRelease("Veronica Maggio", "Fiender är tråkigt", 2019, "Universal Music", "Vinyl")

def loadCollection():
    os.system("CLS")
    x = 0

    print("Choose which collection you want to edit")
    for i in collections:
        print(x + 1, collections[x])
        x += 1
    choosenCollection = int(input(": ")) - 1

    os.system("CLS")
    print("You are in", collections[choosenCollection])
    os.system("PAUSE")
    start()

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
    print("2) Load collection")
    print("3) Information")
    print("4) Quit application")
    startInput = int(input(": "))

    if startInput == 1:
        createCollection()
    elif startInput == 2:
        loadCollection()
    elif startInput == 3:
        information()
    elif startInput == 4:
        quit()

start()