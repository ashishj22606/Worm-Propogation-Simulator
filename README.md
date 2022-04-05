# Worm-Propogation-Simulator

1 Design 

In this assignment, I have implemented the simulation of simple worm propagation in a medium-scale 
network by using discrete-time simulation method. We assume an isolated network with omega(Ω = 
100,000) IP address space which means the IP range in our network ranges from 1 to 100,000. It is 
assumed that there are N = 1,000 computers that are vulnerable to the worm in this isolated network. 
The IP addresses of the vulnerable computer has the following pattern of IP addresses: 

1, 2, 3,. . . , 10, 
10001, 10002, . . . ., 10100, 
20001, 20002, . . . , 20100
....

From this we can see that, each cluster of 100 computers with the consecutive IPs are vulnerable to the 
worm, and in every 1000 consecutive IP addresses there will be one cluster of 100 vulnerable computers 
(so there are 10 clusters of vulnerable computers overall). We further assume that worm starts to 
propagate infection within the network initially from 1 machine which has IP address of 10050. The scan 
rate (n) of infected machine is 5. This implies that a worm-infected computer can scan to 5 other IP 
addresses in the network at each time step. A vulnerable computer is immediately infected if a scan 
finds it and this newly infected computer can also begin infection other 5 IP addresses from the next 
time step. In this way the worm propagates and infect the whole computer in a network.


2 Implementation 
We need to find the number of infected computers at each time step t(t=1,2,3...) which is represented 
as I(t). We simulate the worm propagation 3 times to get the three vector of the number of infected IP, 
I(t). The simulation ends when all the vulnerable machines are infected. At initial point, I(0) = 1. I have 
implemented simulation of two kinds of scanning:

1) Random Scanning
Here I infect IP’s based on random function output and infect it if it is vulnerable

2) Sequential Scanning
Here I infect IP's in sequence and see no of time ticks it takes to infect all the vulnerable IP's. Here we make sequential access based on initial infected IP and probability of 80%. If probalility is 20% than we do random scanning and begin infecting ips in its order.

Order in which we infect IP's is based on the below equation:
num_of_ips_to_scan = num_of_infected_ip * SCAN_RATE

3. Output:
Simulation method of worm propagation
              Run1 Run2 Run3
Random_scan   281 320 257
Sequential    218 423 219
Table to show the time steps required to infect all the vulnerable computers in the network

