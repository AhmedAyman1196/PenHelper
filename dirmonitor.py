import os

class monitor:
    def __init__(self, dir):
        self.files = []
        self.dirs = []
        self.dirSearch(dir)
        
        self.printDirs()
        print("-------------------")
        self.printFiles()

    def dirSearch(self , dir):
        #print("Searching in" , dir)
        self.dirs.append(dir) # add current directory to path
        for (dirpath, dirnames, filenames) in os.walk(dir):
            self.dirs.extend(dirnames)
            self.files.extend(filenames)
            for x in dirnames:
                str = dir + "/"+x
                self.dirSearch(str)
            break

    def printDirs(self):
        print("Directories are :")
        for i in self.dirs:
            print(i)

    def printFiles(self):
        print("Files are :")
        for i in self.files:
            print(i)
#
# import sys
# import hashlib
#
# # BUF_SIZE is totally arbitrary, change for your app!
# BUF_SIZE = 65536  # lets read stuff in 64kb chunks!
#
# md5 = hashlib.md5()
# sha1 = hashlib.sha1()
#
# with open(sys.argv[1], 'rb') as f:
#     while True:
#         data = f.read(BUF_SIZE)
#         if not data:
#             break
#         md5.update(data)
#         sha1.update(data)
#
# print("MD5: {0}".format(md5.hexdigest()))
# print("SHA1: {0}".format(sha1.hexdigest()))
