import socket 
import threading
import socket
import iptc

class detector:
    def __init__(self , port):
        print("monitoring port:",port)
        self.port = port
        self.blockedips = []
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()
    	
       
    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('127.0.0.1', self.port)
        sock.bind(server_address)
        while True :
            sock.listen(1)
            connection, client = sock.accept()
            self.block(client[0])
            connection.close()

    def block(self, ip):
        print("!!!!!!! blocking :", ip , "3ashan ye7aram")
        chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "INPUT")
        rule = iptc.Rule()
        rule.in_interface = "lo"
        rule.target = iptc.Target(rule, "DROP")
        rule.src = ip  # ip in string format
        chain.insert_rule(rule)
#View rules     :    iptables-legacy -L
#Flush all rules:    iptables-legacy -F

        



