import re

class parser:
    def __init__(self, file):
        self.file = file
        f = open(file, "r")
        self.content = f.read().split("\n") # split log file  by line
        # urlRe = re.compile(r'(http://|https).+') --> extracting urls (work in progress)
        ipRe = re.compile(r'\d?\d?\d\.\d?\d?\d\.\d?\d?\d\.\d?\d?\d')
        ipDict = dict() # this will map the ip to the number of appearences
        for i in self.content:
            try :
                ip = ipRe.search(i).group(0)
                if ip in ipDict:
                    ipDict[ip] += 1
                else :
                    ipDict[ip] = 1
            except :
                x = 1 # just ingore
                # print("la2 , no ip hena noooo")
        self.ipDict = ipDict

    def printFile(self):
        print("file is " + self.file)

    def printIps(self , toFile):
        print("2y 7aga")
        if not toFile :
            for i in self.ipDict :
                print("IP" , i )
                print("Appearences : " , str(self.ipDict[i]))
        else :
            f = open(self.file+".out","w+")
            for i in self.ipDict :
                f.write("IP: " + str(i)+"\n")
                f.write("Appearences : " +str(self.ipDict[i])+"\n")
