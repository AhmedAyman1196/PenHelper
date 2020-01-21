import os
import time
import threading

class myobject:
    def __init__(self, str , interval):# object beya5od 7agteen string we interval 
        self.str = str # a string that i will print everywhile
        self.interval = interval
        
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True # Daemonize thread
        thread.start()

    def run(self):
        """ Method that runs forever """
        while True:
            time.sleep(self.interval) # sleep until the interval pass
            print(self.str)


# Main

ahmed = myobject("ana batba3 kol 5 sec" , 5) # keda 3amlt thread we shaghal fel background
joey = myobject("ana batba3 kol 12 sec" , 12) # keda 3amlt thread we shaghal fel background

while(True):
    input("Etkalem M3aya shewaya\n ")