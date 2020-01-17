import os
import hashlib

class monitor:
    def __init__(self, dir):
        self.dirs = dict() # maps directory --> list of its (files, hash) tuple
        self.dirSearch(dir)
        self.printDict()

    def dirSearch(self , dir):
        for (dirpath, dirnames, filenames) in os.walk(dir):
            files = [] # will store all (file,hashes) tuple in this directory
            for fx in filenames:
                if fx!=".DS_Store" :# because atom puts this file
                    path = dirpath + "/" +fx
                    hash = self.hashMe(path)
                    tup = (fx , hash)
                    files.append(tup)
            self.dirs[dirpath] = files

    def printDict(self):
        for i in self.dirs:
            print("Directory : " , i)
            print("Files : " , self.dirs[i])

    def hashMe(self , file): # reads a file and hash it
        BLOCK_SIZE = 65536
        file_hash = hashlib.sha256()
        with open(file, 'rb') as f:
            fb = f.read(BLOCK_SIZE)
            while len(fb) > 0:
                file_hash.update(fb)
                fb = f.read(BLOCK_SIZE)
        return file_hash.hexdigest() # Get the hexadecimal digest of the hash
