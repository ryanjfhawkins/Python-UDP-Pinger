#This Program sends 'n' pings to and times each one. If it takes longer than 2 seconds then it gets timed out
#It records the times for the 'n' pings and calculates the maximum, minimum, average, and standard deviation of succesful pings in milliseconds
#It also calculates and shows the packet loss rate 
#Finally it graphs the RTT vs Number of Pings and outputs it in a histogram



import time
from socket import *
import numpy as np
import matplotlib.pyplot as plt

min = 100
max = 0
total = 0
data = 0
loss = 0
x = []

n = 100
    
#Sends 10 pings
for pings in range(n):
    
    #Create UDP socket
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    
    #Create timeout value of 2 seconds
    clientSocket.settimeout(2)
    
    #Ping message
    message = "message"
    
    #Sets Server name and port number
    serverNamePort = ("127.0.0.1", 12000)

    #Starts timer
    start = time.time()
    #Send ping
    clientSocket.sendto(message.encode(), serverNamePort)
    
    #If the data is recieved in time
    try:
        
        modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
        
        #Ends timer
        end = time.time()
        RTT = (end - start) * 1000
            
        x.append(RTT)
            
        total = total + RTT
        
        if RTT < min:
            min = RTT
            
        if RTTms > max:
            max = RTT    
            
        data = data + 1   
        
    #If the data is not recieved in time    
    except timeout:
        loss = loss + 1
        
    clientSocket.close()
    
avg = total / data
std = np.std(x, ddof=1)
    
print ("Minimum RTT=" + str(min) + "ms \nMaximum RTT=" + str(max) + "ms \nAverage RTT=" + str(avg) + "ms \nStandard deviation of RTT=" + str(std) + "ms\n")
print ("Packet loss ratio is " + str(loss / 200 * 100) + "%")

plt.hist(x)
plt.xlabel("RTT")
plt.ylabel("Number of Pings")
plt.title("Histogram of RTTS")
plt.grid(True)
plt.show()

    
