import subprocess
import re 
import socket 
import os

class scanner:
    def __init__(self):
    	self.ips = []
    	self.openports= dict()
    	self.arpScan()
    	# print(self.ips)
    	self.scanAll()
    	self.printReport()
       

    def printReport(self):
        res = ""
        for i in self.openports:
            res += "IP --> " + i +"\n"
            res+= "----------------------------\n"
            for j in self.openports[i] :
                port = j[0]
                portn , service , version = self.parsenmap(j[1])
                res+= "~~~~\n"
                res+= "Port is : "+ portn +"\n"
                res+= "Service is : "+ service +"\n"
                res+= "Version is :" + version +"\n"
            res+= "----------------------------\n"
        return res

    def parsenmap(self , nout):
        n = nout.split("\n")
        info = n[5].split(" ")
        port = info[0]
        try :
            service = info[3]
            version = n[5].split(service,1)[1]
        except :
            service = ""
            version = ""
        return port,service,version

    def scanAll(self):
    	for ip in self.ips:
    		#print("--------------------------------------------------")
    		#print("scanning :",ip)
    		openports = []
    		for port in range(0,100):
    			#print("scanning port :" , port)
    			tcpscan = self.portScan(ip,port, True)
    			if tcpscan==0:
    				#print("TCP Port",port,"is open")
    				openports.append([port ,self.nmap(ip,port,True) ])

                #  !!!!!! I commented udp scan because it is too slow

    			# udpscan = self.portScan(ip,port, False).split(" ")
    			# #print(udpscan) 
    			# if "open" in udpscan:
    			# 	#print("UDP Port",port, "is open")
    			# 	openports.append([port ,self.nmap(ip,port,False) ])
    		self.openports[ip] = openports

    			
        #self.printDict()
    def nmap(self,addr , port, TCP):
    	if not TCP :
    		udpnmap = subprocess.Popen("nmap -sU -p "+str(port)+" "+str(addr),shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    		res  = str(udpnmap.stdout.read(),"utf-8")
    		return res
    	else :
    		udpnmap = subprocess.Popen("nmap -sC -sV -p "+str(port)+" "+str(addr),shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    		res  = str(udpnmap.stdout.read(),"utf-8")
    		return res
    

    def arpScan(self):
    	try:
    		arp = subprocess.Popen("arp-scan -l",shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    		reg  = str(arp.stdout.read(),"utf-8")
    		self.ips = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",reg)
    	except:
    		print("error while scanning IPs in network")
    
    def portScan(self ,addr , port , TCP): 
    	if TCP :
    		socket_obj = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    		socket.setdefaulttimeout(1)
    		result = socket_obj.connect_ex((addr,port))
    		socket_obj.close()
    		return result
    	else :
    		udpnmap = subprocess.Popen("nmap -sU -p "+str(port)+" "+str(addr),shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    		res  = str(udpnmap.stdout.read(),"utf-8")
    		return res

    def rangePortScan(address , start , end  , TCP):
    	if(start < 0 or end >65535) :
    		return []
    	ports = []
    	for i in range(start , end+1):
    		pscan = portScan(address , i,  TCP)
    		print(pscan)
    	return ports

