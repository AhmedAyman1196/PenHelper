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

    def printIps(self):
        res = ""
        print("2y 7aga")
        for i in self.ipDict :
            res += "IP : " + i +"\nAppearences : " + str(self.ipDict[i]) +"\n"
        return res 
