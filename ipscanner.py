import os

print("Scanning network...\n")

base_ip = "192.168.1.8"  

for i in range(1, 5): 
    ip = base_ip + str(i)

    response = os.system(f"ping -n 1 {ip} > nul") 

    if response == 0:
        print(f"{ip} is ACTIVE")
    else:
        print(f"{ip} is not reachable")
