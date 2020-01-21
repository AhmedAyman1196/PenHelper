import logparser
import dirmonitor
import time
import htmlParser
import nscanner
import defender
import subprocess
import requests
# ------------------Access Log parser-----------------------------------------

def logparse():
    print("This service will get all ips in your access log and the number of their occurences\n")
    while True :
        file = input("Enter name of access log file ( make sure the file is in the same dircetory)\n")
        try :
            lp = logparser.parser(file)
            return lp.printIps()
            break ;
        except FileNotFoundError :
            print("OBAAAA!! : Cannot find this file, Check the name and permissions.")


# ------------------------- Monitor -----------------------------------------
def monitor():
    while True :
        file = input("Enter name of folder to monitor\n")
        try :
            interval = int(input("complete the following sentence.\nWe will check every interval, interval = ??\n"))
            monitor = dirmonitor.monitor(file,interval)
            print("Started monitoring " + file +" in the background")
            print("3ala wad3ak zy manta")
            break
        except FileNotFoundError :
            print("OBAAAA!! : Cannot find this file, Check the name and permissions.")


# ----------------------------- Network Scanner ------------------------------------

def scan():
    try :
        print("This service will scan all ips in your network and scan first 100 ports on them")
        input("Press any key to continue ..\n")
        print("Scanning ... please wait")
        scanner = nscanner.scanner()
        return scanner.printReport()
    except requests.exceptions.ConnectionError :
        print("Failed to connect :(")

# ----------------------------- defender ------------------------------------

def defend():
    print("This service will monitor port in the backgroun and will bloack all ips thath try to connect on thath port")
    port = int(input("Enter port number\n"))
    detector = defender.detector(port)
    print("Working in the background , kamel zymanta")
    wellknown = [1, 5, 7, 18, 20, 21, 22, 23, 25, 29, 37, 42, 43, 49, 53,
     69, 70, 79, 80, 103, 108, 109, 110, 115, 118, 119, 137, 139, 143, 
     150, 156, 161, 179, 190,194, 197, 389, 396, 443, 444, 445, 458, 546,
     547, 563, 569, 1080]


# ----------------------------- Html Parser -----------------------------------

def hparse():
    url = input("Enter URL\n")
    try :
        parser = htmlParser.hparser(url)
        res = ""
        res += "Tags found :\n"
        for i in parser.tags:
            res+= i +"\n"
        res+= "---------------------------------\n"
        res+= "---------------------------------\n"

        res+= "Links found :\n"
        for i in parser.links:
            res+= i +"\n"
        res +="---------------------------------\n"
        res+= "---------------------------------\n"
        res+= "Comments found :\n"
        for i in parser.comments:
            res+= i +"\n"
        
    except requests.exceptions.ConnectionError :
        res = "Failed to connect :("
    except :
        res = "Wrong Url format"
    return res


#-------------------------------- HELPER METHODS -------------------------
def clear():
    #subprocess.Popen("clear")
    print("\n\n\n\n\n\n\n")

def printToFile(str,filename):
    f = open(filename,"w+")
    f.write(str+"\n")
    f.close()
# Main

while(True):
    try :
        serv = input("3awez te3mel eh?\n1- Parse access log files.\n2- Monitor a directory.\n"+
            "3- Scan your network\n4- Defend a port\n5- Analyze a website\n6- exit bye\n")
        out = "empty"
        if serv == "1":
            clear()
            out = logparse()
        elif serv == "2" :
            monitor()
        elif serv == "3":
            out = scan()
        elif serv == "4" :
            defend()
        elif serv == "5":
            out = hparse()
        elif serv == "6":
            print("\n\nSalaaaaam")
            break
        else :
            print("Wrong Input ??!!")

        if out != "empty":
            y = input("print to file (will name it out.txt) ? (y/n)\n")
            if y =="y":
                printToFile(out,"out.txt")
            else :
                print(out)
    except :
        print("An unexpected error have occured , please try again we shokran")
    input("Press any key to continue \n")
    clear()



