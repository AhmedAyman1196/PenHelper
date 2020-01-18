import logparser
import dirmonitor
import time

# this method takes access log file , gets all ips and number of their occurrence
def parse():
    while True :
        file = input("Enter name of access log file\n")
        try :
            # for static testing
            # lp = logparser.parser("log_test.txt")
            lp = logparser.parser(file)
            lp.printIps(True)
            lp.printIps(False)
            break ;
        except FileNotFoundError :
            print("OBAAAA!! : Cannot find this file, Check the name and permissions.")

#parse()


def monitor():
    while True :
        #file = input("Enter name of folder to monitor\n")
        # static testing
        file = "TestDirectory"
        try :
            interval = int(input("Enter an interval\n"))
            m = dirmonitor.monitor(file,interval)
            break
        except FileNotFoundError :
            print("OBAAAA!! : Cannot find this file, Check the name and permissions.")

monitor()

for i in range(1,100):
    time.sleep(100)
