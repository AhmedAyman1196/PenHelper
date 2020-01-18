import os
import hashlib
import time
from datetime import datetime
import threading

class monitor:
    def __init__(self, dir,interval):
        self.dirs = dict() # maps directory --> list of its (files, hash) tuple
        self.interval = interval
        self.dirSearch(dir)
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()
        #self.printDict()

    def dirSearch(self , dir):
        for (dirpath, dirnames, filenames) in os.walk(dir):
            files = [] # will store all (file,hashes) tuple in this directory
            for fx in filenames:
                if fx!=".DS_Store" :# because atom puts this file
                    path = dirpath + "/" +fx
                    hash = self.hashMe(path)
                    tup = (fx , hash)
                    files.append(list(tup))
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

    def check(self):
        for dir in self.dirs:
            # print(dir)
            if not os.path.isdir(dir):
                print(dir , " directory is deleted , yalahwaaaaaaaaay")
                continue
            for file in self.dirs[dir]:
                path = str(dir) + "/" + str(file[0])
                if not os.path.isfile(path):
                    print(dir , " file is deleted , ya5arashy")
                    continue
                hash = self.hashMe(path)
                if file[1] != hash : # a change happened in this file
                    # get current date and time
                    now = datetime.now()
                    current_time = now.strftime("%H:%M:%S")
                    print(current_time + " : "+path + " has been modified !!!!!")
                    # update the current hash
                    file[1] = hash

    def run(self):
        """ Method that runs forever """
        while True:
            self.check()
            time.sleep(self.interval)
