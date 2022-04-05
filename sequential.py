import random
import matplotlib.pyplot as plt
import numpy as np

runs = 3
OMEGA = 100000
Total_vulnerable_ip = 1000
total_simulation_steps = 10000
SCAN_RATE = 5

data = []
for t in range(20):
    ip_addr_space = ['immune' for i in range(OMEGA+1)]
    for i in range(int(100/10)):
        for j in range(1, 101):
            ip_addr_space[j + (i * 10000)] = 'vulnerable'
    ip_addr_space[10050]='infected'
    num_of_infected_ip=1
    count=0
    ip = 10050
    for tick in range(total_simulation_steps):
        count+=1
        num_of_ips_to_scan = num_of_infected_ip * SCAN_RATE
        rule = np.random.choice(['rule1', 'rule2'], 1, p=[0.8, 0.2])
        if rule[0]=='rule1':
            if ip+1+num_of_ips_to_scan<OMEGA:
                for y in range(ip+1,ip+1+num_of_ips_to_scan):
                    if ip_addr_space[y]=='vulnerable':
                        ip_addr_space[y]='infected'
                        num_of_infected_ip += 1
                ip=ip+num_of_ips_to_scan
    #             print(ip, num_of_infected_ip)


            else:
                z = num_of_ips_to_scan -OMEGA + ip
                for y in range(ip+1,OMEGA+1):
                    if ip_addr_space[y]=='vulnerable':
                        ip_addr_space[y]='infected'
                        num_of_infected_ip+=1
                ip=0
                for i in range(z):
                    if ip_addr_space[i]=='vulnerable':
                        ip_addr_space[i]='infected'
                        num_of_infected_ip+=1
                ip=ip+z
                data.append(num_of_infected_ip)
    #             print(ip, num_of_infected_ip)
        else:
            infect_ip = random.sample(range(1, OMEGA + 1), num_of_ips_to_scan)
            for ip1 in infect_ip:
                if ip_addr_space[ip1] == 'vulnerable':
                    ip_addr_space[ip1] = 'infected'
                    num_of_infected_ip += 1
                    if num_of_infected_ip == 1000:
                        break
            ip = ip1
            data.append(num_of_infected_ip)
#         plot_simulation(num_of_infected_ip, t)
#         plt.plot(num_of_infected_ip, "-", label="Run #{}".format(t + 1))
        if num_of_infected_ip==1000:
            print(f"Infected 1000 ip in time steps: {count}")
#             plt.plot(num_of_infected_ip, "-", label="Run #{}".format(t + 1))
#             plt.plot(data, color='magenta', marker='o',mfc='pink' ) #plot the data
#             plt.xticks(range(0,len(data)+1, 10)) #set the tick frequency on x-axis

#             plt.ylabel('data') #set the label for y axis
#             plt.xlabel('time') #set the label for x-axis
#             plt.title("Plotting a list") #set the title of the graph
#             plt.show() #display the graph
#             data = []
            break
        


    print(count)    
