# CNP-SEM-IV-Assignment FISAC-1
> Cisco Packet Tracer bullshitery

### `Files to submit`
- the pkt file
- writeup
- the typed report

# `Writeup`

## Network topology :
![image](https://github.com/user-attachments/assets/580f93ba-627d-4648-b197-c2877ae69b0c)


## Ip addressing :
consists of the networks :
- `111.169.1.0/8` with 2 hosts (class A | subnet mask `255.0.0.0`) with gateways at `111.169.1.1`
	- Server0 `111.169.1.2`
 	- Server1 `111.169.1.3`
- `192.168.1.0/24` with 5 hosts (class C | subnet mask `255.255.255.0`) with gateways at `192.168.1.1`
	- PC0 `192.168.1.2`
 	- PC1 `192.168.1.3`
  	- PC2 `192.168.1.4`
  	- PC3 `192.168.1.5`
  	- PC4 `192.168.1.6`
- `155.169.1.0/16` with 5 hosts (class B | subnet mask `255.255.0.0`) with gateways at `155.169.1.1`
  	- PC5 `155.169.1.2`
  	- PC6 `155.169.1.3`
  	- PC7 `155.169.1.4`
  	- PC8 `155.169.1.5`
  	- PC9 `155.169.1.6`
- `122.163.1.0/10` with 5 hosts (classless | subnet mask `255.192.0.0`) with gateways at `122.163.1.1`
  	- PC10 `122.163.1.2`
  	- PC11 `122.163.1.3`
  	- PC12 `122.163.1.4`
  	- PC13 `122.163.1.5`
  	- PC14 `122.163.1.6`

links :  (i think u could ignore these not too sure)
- `10.0.0.0`
- `20.0.0.0`
- `30.0.0.0`


  
## Router configs : 
### `Router 1`
```
Router>enable
Router#config t
Router(config)#interface FastEthernet4/0
Router(config-if)#ip address 192.168.1.1 255.255.255.0
Router(config-if)#no shutdown
Router(config-if)#exit
Router(config)#interface FastEthernet5/0
Router(config-if)#ip address 155.169.1.1 255.255.0.0
Router(config-if)#no shutdown
Router(config-if)#exit
Router(config)#interface Serial2/0
Router(config-if)#ip address 10.0.0.3 255.0.0.0
Router(config-if)#no shutdown
Router(config-if)#exit
Router(config)#interface Serial3/0
Router(config-if)#ip address 20.0.0.2 255.0.0.0
Router(config-if)#clock rate 64000
Router(config-if)#no shutdown
Router(config-if)#exit
Router(config)#exit
Router#copy running-config startup-config
```
### `Router 2`
```
Router>enable
Router#config t
Router(config)#interface FastEthernet0/0
Router(config-if)#ip address 111.169.1.1 255.0.0.0
Router(config-if)#no shutdown
Router(config-if)#exit
Router(config)#interface Serial2/0
Router(config-if)#clock rate 64000
Router(config-if)#ip address 10.0.0.2 255.0.0.0
Router(config-if)#no shutdown
Router(config-if)#exit
Router(config)#interface Serial3/0
Router(config-if)#ip address 30.0.0.3 255.0.0.0
Router(config-if)#no shutdown
Router(config-if)#exit
Router(config)#exit
Router#copy running-config startup-config
```
### `Router 3`
```
Router>enable
Router#config t
Router(config)#interface FastEthernet4/0
Router(config-if)#ip address 122.163.1.1 255.192.0.0
Router(config-if)#no shutdown
Router(config-if)#exit
Router(config)#interface Serial2/0
Router(config-if)#clock rate 64000
Router(config-if)#ip address 30.0.0.2 255.0.0.0
Router(config-if)#no shutdown
Router(config-if)#exit
Router(config)#interface Serial3/0
Router(config-if)#ip address 20.0.0.3 255.0.0.0
Router(config-if)#no shutdown
Router(config-if)#exit
Router(config)#exit
Router#copy running-config startup-config
```
Have a router configuration summary \
table with `Router | interface | IP | subnet mask | device` 

## Implementing RIP and setting up NTP server:
### `Perform the same below commands for Router1, Router2, Router3`
```
Router>enable
Router#config t
Router(config)#router rip
Router(config)#version 2
Router(config-router)#network 192.168.1.0
Router(config-router)#network 155.169.0.0
Router(config-router)#network 10.0.0.0
Router(config-router)#network 20.0.0.0
Router(config-router)#network 111.0.0.0
Router(config-router)#network 122.0.0.0
Router(config-router)#network 30.0.0.0
Router(config-router)#exit
Router(config)#ntp server 111.169.1.3
Router(config)#exit
Router#copy running-config startup-config
```

We decided to select the server at `111.169.1.3` i.e. `Sever1` to be our NTP server. \
and enabled it by turning on it's NTP service and setting any certain date + time \
![image](https://github.com/user-attachments/assets/756bf7f9-88ac-497f-81f5-24020c5ca5c6)


## Verifying RIP for each router. Performed via `show ip protocols`
### `Router 1` 
![image](https://github.com/user-attachments/assets/67516949-2854-4dde-b308-c6f52bd43a03)

### `Router 2` 
![image](https://github.com/user-attachments/assets/3514cf2e-d923-4aec-bdd1-9545b92f9c15)

### `Router 3`
![image](https://github.com/user-attachments/assets/613639c9-47c1-483d-b3b5-8ef859fb0ad1)


We can see on the first line the routing protocol being mentioned RIP on all three routers, thus indicating succesful setup and verifying RIP.

## Verifying NTP for each router. Performed via `show clock`
If NTP has been successfully seetup, the clock on each router would be synced to the clock on their corresponding NTP server \
in our case, we set the NTP server's date to 10th March 2025 

### `Router 1`
```
Router1>show clock
17:37:44.890 UTC Mon Mar 10 2025
```
### `Router 2`
```
Router>show clock
17:38:52.311 UTC Mon Mar 10 2025
```
### `Router 3`
```
Router>show clock
17:39:15.458 UTC Mon Mar 10 2025
```

Thus verified that all three are synced to the NTP server's clock.

## Routing tables :
Accessed on each router by running `show ip route`
> [!NOTE]
> i dont think u gotta rewrite the Codes section each table.

### `Router 1`
```
Router1#show ip route
Codes: C - connected, S - static, I - IGRP, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2, E - EGP
       i - IS-IS, L1 - IS-IS level-1, L2 - IS-IS level-2, ia - IS-IS inter area
       * - candidate default, U - per-user static route, o - ODR
       P - periodic downloaded static route

Gateway of last resort is not set

C    10.0.0.0/8 is directly connected, Serial2/0
C    20.0.0.0/8 is directly connected, Serial3/0
R    30.0.0.0/8 [120/1] via 20.0.0.3, 00:00:25, Serial3/0
                [120/1] via 10.0.0.2, 00:00:04, Serial2/0
R    111.0.0.0/8 [120/1] via 10.0.0.2, 00:00:04, Serial2/0
R    122.0.0.0/8 [120/1] via 20.0.0.3, 00:00:25, Serial3/0
C    155.169.0.0/16 is directly connected, FastEthernet5/0
C    192.168.1.0/24 is directly connected, FastEthernet4/0
```
### `Router 2`
```
Router>show ip route
Codes: C - connected, S - static, I - IGRP, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2, E - EGP
       i - IS-IS, L1 - IS-IS level-1, L2 - IS-IS level-2, ia - IS-IS inter area
       * - candidate default, U - per-user static route, o - ODR
       P - periodic downloaded static route

Gateway of last resort is not set

C    10.0.0.0/8 is directly connected, Serial2/0
R    20.0.0.0/8 [120/1] via 10.0.0.3, 00:00:04, Serial2/0
                [120/1] via 30.0.0.2, 00:00:16, Serial3/0
C    30.0.0.0/8 is directly connected, Serial3/0
C    111.0.0.0/8 is directly connected, FastEthernet0/0
R    122.0.0.0/8 [120/1] via 30.0.0.2, 00:00:16, Serial3/0
R    155.169.0.0/16 [120/1] via 10.0.0.3, 00:00:04, Serial2/0
R    192.168.1.0/24 [120/1] via 10.0.0.3, 00:00:04, Serial2/0
```

### `Router 3`
```
Router#show ip route
Codes: C - connected, S - static, I - IGRP, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2, E - EGP
       i - IS-IS, L1 - IS-IS level-1, L2 - IS-IS level-2, ia - IS-IS inter area
       * - candidate default, U - per-user static route, o - ODR
       P - periodic downloaded static route

Gateway of last resort is not set

R    10.0.0.0/8 [120/1] via 20.0.0.2, 00:00:10, Serial3/0
                [120/1] via 30.0.0.3, 00:00:02, Serial2/0
C    20.0.0.0/8 is directly connected, Serial3/0
C    30.0.0.0/8 is directly connected, Serial2/0
R    111.0.0.0/8 [120/1] via 30.0.0.3, 00:00:02, Serial2/0
     122.0.0.0/10 is subnetted, 1 subnets
C       122.128.0.0 is directly connected, FastEthernet4/0
R    155.169.0.0/16 [120/1] via 20.0.0.2, 00:00:10, Serial3/0
R    192.168.1.0/24 [120/1] via 20.0.0.2, 00:00:10, Serial3/0
```
![image](https://github.com/user-attachments/assets/2d2de0d6-4c2a-43da-b82e-4abee9da0b10)

![image](https://github.com/user-attachments/assets/1c3c15fc-99cb-42f0-ae1d-2c8a39c61d3d)

![image](https://github.com/user-attachments/assets/caccf4c7-cb52-4234-8517-2d9aae97a94e)



## Setting up the web server

After the network has been setup \
To setup a web server on Server0, we simply had to go on the server \
enable http service and set an index.html for the landing page. \
According to the question, set index.html to the below script to display `All the best` 

`index.html`
```html
<html>
<center><b><font size='+7' color='black'>All the best.</font></b></center>
</html>
```

then to view this, we go on `http://111.169.1.2` through the web browser \
(`111.169.1.2` being the ip address of Server0) 

![image](https://github.com/user-attachments/assets/ed954e98-d9b6-4149-972f-cd86759dfee7)

![image](https://github.com/user-attachments/assets/7632e9c7-d578-441c-bd5a-d8adddfa97f1)


## RIP AND NTP
### RIP (Routing Information Protocol) :
- RIP is a distance-vector routing protocol used in small to medium-sized networks for dynamically sharing routing information between routers.
- Operates at the network layer (Layer 3) of the OSI model. RIP is mainly used in small to medium-sized networks due to its simplicity and limited scalability.
- RIP uses hop count as the metric to measure the distance between networks. with 15 hops being the max.
- Each router maintains a routing table that stores the best-known paths to other networks.
- Routers exchange routing tables every 30 seconds by broadcasting them to their neighbors. Works on UDP port 520.
- RIP uses split horizon and route poisoning to prevent loops.

### NTP (Network Time Protocol):
- NTP is a time synchronization protocol used to synchronize the clocks of network devices (routers, switches, servers, computers, etc.).
- It ensures accurate timekeeping across the network, which is essential for logging, security, and network operations.
- NTP operates at the application layer (Layer 7) of the OSI model.
- uses UDP port 123.

  
## Ethernet Frame

An **Ethernet frame** is a structured data packet used in **Ethernet networks** to transmit information between devices in a **Local Area Network (LAN)**. It ensures data is properly formatted, addressed, and verified for errors.

### Structure of an Ethernet Frame
An Ethernet frame consists of several key components:

- **Preamble**: A 7-byte sequence used for synchronization between sender and receiver.
- **Start Frame Delimiter (SFD)**: A 1-byte field (10101011) that marks the beginning of the frame.
- **Destination MAC Address**: A 6-byte address identifying the receiving device.
- **Source MAC Address**: A 6-byte address identifying the sender.
- **EtherType / Length**: A 2-byte field indicating the type of protocol being used (IPv4, IPv6, ARP) or the length of the payload.
- **Payload (Data)**: The actual data being transmitted, ranging from 46 to 1500 bytes.
- **Frame Check Sequence (FCS)**: A 4-byte error-checking mechanism using Cyclic Redundancy Check (CRC).

Ethernet frame captured at Router2 when sending requests from PC0 to Server0 : \
![image](https://github.com/user-attachments/assets/b2af58b2-ca1c-4c04-beb8-54f3b468c59f)
